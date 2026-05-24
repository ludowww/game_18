#!/usr/bin/env python3
"""T191: Sarah J3 morning scene replaces placeholder with structured dialogue."""

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SARAH_PATH = DATA / "sarah_j3_v2_experimental.json"
SARAH = json.loads(SARAH_PATH.read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in SARAH["nodes"]}

ENTRY_VARIANTS = [
    "after_concrete",
    "after_delay",
    "after_minimized",
    "after_fragile_incoherence",
    "default",
]
CENTRAL_CHOICES = [
    "j3_01_sarah_show_with_actions",
    "j3_01_sarah_honest_uncertainty",
    "j3_01_sarah_ask_more_time",
    "j3_01_sarah_defensive",
]
OTHER_J3 = [
    "camille_j3_v2_experimental.json",
    "maya_j3_v2_experimental.json",
    "ines_j3_v2_experimental.json",
]


def test_t191_placeholder_removed_and_entry_variants_exact() -> None:
    serialized = json.dumps(SARAH, ensure_ascii=False)
    assert "[J3 placeholder Sarah matin]" not in serialized
    assert [variant["id"] for variant in SARAH["entry_variants"]] == ENTRY_VARIANTS


def test_t191_entry_variant_conditions_and_start_nodes_exist() -> None:
    variants = {variant["id"]: variant for variant in SARAH["entry_variants"]}
    assert variants["after_concrete"]["conditions"] == {"flags": ["j2_sarah_try_concrete"]}
    assert variants["after_delay"]["conditions"] == {"flags": ["j2_sarah_asked_time"]}
    assert variants["after_minimized"]["conditions"] == {"flags": ["j2_sarah_minimized_again"]}
    # Runtime currently supports all-of flags; Sarah J2 sets these two together on the fragile route.
    assert variants["after_fragile_incoherence"]["conditions"] == {
        "flags": ["j2_sarah_admitted_incoherence", "j2_sarah_version_fragile_named"]
    }
    assert variants["default"]["conditions"] == {}
    for variant in variants.values():
        assert variant["start_node"] in NODES


def follow_path(start_node: str) -> list[str]:
    seen: list[str] = []
    current = start_node
    while current:
        assert current in NODES, f"missing node {current}"
        assert current not in seen, f"loop at {current}"
        seen.append(current)
        if current == "j3_01_choice_sarah_place":
            break
        current = NODES[current].get("next", "")
    return seen


def test_t191_each_entry_variant_converges_to_central_choice() -> None:
    for variant in SARAH["entry_variants"]:
        path = follow_path(variant["start_node"])
        assert "j3_01_choice_sarah_place" in path


def test_t191_single_replies_have_one_choice_no_effects_and_matching_player_text() -> None:
    single_replies = [node for node in SARAH["nodes"] if "_single_reply_" in node["id"]]
    assert len(single_replies) == 5
    for node in single_replies:
        assert node["type"] == "choice"
        assert "effects" not in node
        assert len(node["choices"]) == 1
        option = node["choices"][0]
        player = NODES[option["next"]]
        assert player["sender"] == "player"
        assert player["text"] == option["text"]
        assert "effects" not in player


def test_t191_central_choice_has_four_effectful_choices_with_j3_flags() -> None:
    central = NODES["j3_01_choice_sarah_place"]
    assert central["type"] == "choice"
    assert central["text"] == "Que répondre à Sarah ?"
    assert [choice["id"] for choice in central["choices"]] == CENTRAL_CHOICES
    for choice in central["choices"]:
        effects = choice.get("effects")
        assert isinstance(effects, dict), f"missing effects for {choice['id']}"
        flags = effects.get("flags", [])
        assert any(flag.startswith("j3_sarah_") for flag in flags)
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]


def test_t191_each_central_branch_ends_on_end_node() -> None:
    for choice in NODES["j3_01_choice_sarah_place"]["choices"]:
        current = choice["next"]
        seen = set()
        while current:
            assert current in NODES, f"missing node {current}"
            assert current not in seen, f"loop in branch {choice['id']} at {current}"
            seen.add(current)
            node = NODES[current]
            if node["type"] == "end":
                break
            current = node.get("next", "")
        assert NODES[current]["type"] == "end"


def test_t191_no_media_and_no_forbidden_omniscience_terms() -> None:
    assert all(node.get("type") != "media" for node in SARAH["nodes"])
    serialized = json.dumps(SARAH, ensure_ascii=False).lower()
    for forbidden in ["maya", "inès", "ines", "camille", "nico"]:
        assert forbidden not in serialized


def test_t191_other_j3_conversations_remain_skeletons() -> None:
    for name in OTHER_J3:
        data = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert len(data["nodes"]) == 2
        assert len(data["entry_variants"]) == 1
        assert data["entry_variants"][0]["id"] == "default"
        assert "placeholder" in json.dumps(data, ensure_ascii=False).lower()


if __name__ == "__main__":
    test_t191_placeholder_removed_and_entry_variants_exact()
    test_t191_entry_variant_conditions_and_start_nodes_exist()
    test_t191_each_entry_variant_converges_to_central_choice()
    test_t191_single_replies_have_one_choice_no_effects_and_matching_player_text()
    test_t191_central_choice_has_four_effectful_choices_with_j3_flags()
    test_t191_each_central_branch_ends_on_end_node()
    test_t191_no_media_and_no_forbidden_omniscience_terms()
    test_t191_other_j3_conversations_remain_skeletons()
    print("T191 Sarah J3 morning dialogue tests OK")
