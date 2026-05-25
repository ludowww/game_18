#!/usr/bin/env python3
"""T192: Nico J3 availability scene replaces placeholder with structured dialogue."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NICO_PATH = DATA / "nico_j3_v2_experimental.json"
NICO = json.loads(NICO_PATH.read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in NICO["nodes"]}

ENTRY_VARIANTS = ["after_hold_line", "after_released", "after_partial_truth", "after_joke_escape", "default"]
CENTRAL_CHOICES = [
    "j3_02_nico_respect_limit",
    "j3_02_nico_ask_more_help",
    "j3_02_nico_sarah_observes",
    "j3_02_nico_deflect_to_his_life",
]
OTHER_J3 = []


def test_t192_placeholder_removed_and_entry_variants_exact() -> None:
    serialized = json.dumps(NICO, ensure_ascii=False)
    assert "[J3 placeholder Nico matin]" not in serialized
    assert [variant["id"] for variant in NICO["entry_variants"]] == ENTRY_VARIANTS


def test_t192_entry_variant_conditions_and_start_nodes_exist() -> None:
    variants = {variant["id"]: variant for variant in NICO["entry_variants"]}
    assert variants["after_hold_line"]["conditions"] == {"flags": ["j2_nico_hold_line"]}
    assert variants["after_released"]["conditions"] == {"flags": ["j2_nico_released_from_alibi"]}
    assert variants["after_partial_truth"]["conditions"] == {"flags": ["j2_nico_partial_truth_camille"]}
    assert variants["after_joke_escape"]["conditions"] == {"flags": ["j2_nico_joke_escape"]}
    assert variants["default"]["conditions"] == {}
    for variant in variants.values():
        assert variant["start_node"] in NODES


def follow_path(start_node: str) -> list[str]:
    seen = []
    current = start_node
    while current:
        assert current in NODES, f"missing node {current}"
        assert current not in seen, f"loop at {current}"
        seen.append(current)
        if current == "j3_02_choice_nico_availability":
            break
        current = NODES[current].get("next", "")
    return seen


def test_t192_each_entry_variant_converges_to_central_choice() -> None:
    for variant in NICO["entry_variants"]:
        assert "j3_02_choice_nico_availability" in follow_path(variant["start_node"])


def test_t192_single_replies_have_one_choice_no_effects_and_matching_player_text() -> None:
    single_replies = [node for node in NICO["nodes"] if "_single_reply_" in node["id"]]
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


def test_t192_central_choice_has_four_effectful_choices_with_j3_flags() -> None:
    central = NODES["j3_02_choice_nico_availability"]
    assert central["type"] == "choice"
    assert central["text"] == "Que répondre à Nico ?"
    assert [choice["id"] for choice in central["choices"]] == CENTRAL_CHOICES
    for choice in central["choices"]:
        effects = choice.get("effects")
        assert isinstance(effects, dict)
        assert any(flag.startswith("j3_") for flag in effects.get("flags", []))
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]


def test_t192_each_central_branch_ends_on_end_node() -> None:
    for choice in NODES["j3_02_choice_nico_availability"]["choices"]:
        current = choice["next"]
        seen = set()
        while current:
            assert current in NODES
            assert current not in seen
            seen.add(current)
            node = NODES[current]
            if node["type"] == "end":
                break
            current = node.get("next", "")
        assert NODES[current]["type"] == "end"


def test_t192_no_media_no_betrayal_and_life_tease_without_maya() -> None:
    assert [node["id"] for node in NICO["nodes"] if node.get("type") == "media"] == [
        "j3_02_nico_media_social_life_001"
    ]
    nico_text = "\n".join(node.get("text", "") for node in NICO["nodes"] if node.get("sender") == "nico")
    assert "Maya" not in nico_text
    assert "Camille m’a dit" not in nico_text
    assert "Sarah m’a dit" not in nico_text
    assert "quelqu’un m’a écrit" in nico_text


def test_t192_other_unwritten_j3_conversations_remain_skeletons() -> None:
    for name in OTHER_J3:
        data = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert len(data["nodes"]) == 2
        assert len(data["entry_variants"]) == 1
        assert data["entry_variants"][0]["id"] == "default"
        assert "placeholder" in json.dumps(data, ensure_ascii=False).lower()


if __name__ == "__main__":
    test_t192_placeholder_removed_and_entry_variants_exact()
    test_t192_entry_variant_conditions_and_start_nodes_exist()
    test_t192_each_entry_variant_converges_to_central_choice()
    test_t192_single_replies_have_one_choice_no_effects_and_matching_player_text()
    test_t192_central_choice_has_four_effectful_choices_with_j3_flags()
    test_t192_each_central_branch_ends_on_end_node()
    test_t192_no_media_no_betrayal_and_life_tease_without_maya()
    test_t192_other_unwritten_j3_conversations_remain_skeletons()
    print("T192 Nico J3 availability dialogue tests OK")
