#!/usr/bin/env python3
"""T215: Camille J4 work-pause scene stays concrete, bounded, and non-explicit."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CAMILLE = json.loads((DATA / "camille_j4_v2_experimental.json").read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in CAMILLE["nodes"]}
ENTRY_VARIANTS = [
    "after_boundary_respected",
    "after_tension_reopened",
    "after_pressure_high",
    "after_minimized",
    "default",
]
CENTRAL_CHOICES = [
    "j4_04_camille_tease_lightly",
    "j4_04_camille_respect_pause",
    "j4_04_camille_name_trouble",
    "j4_04_camille_push_too_much",
    "j4_04_camille_cut_short",
]
OTHER_STILL_SKELETON_J4 = [
    "maya_j4_v2_experimental.json",
    "ines_j4_v2_experimental.json",
]


def follow_until_choice(start_node: str) -> list[str]:
    seen: list[str] = []
    current = start_node
    while current:
        assert current in NODES, f"missing node {current}"
        assert current not in seen, f"loop at {current}"
        seen.append(current)
        if current == "j4_04_choice_camille_pause":
            break
        current = NODES[current].get("next", "")
    return seen


def visible_text() -> str:
    return "\n".join(
        [node.get("text", "") for node in CAMILLE["nodes"]]
        + [choice.get("text", "") for node in CAMILLE["nodes"] for choice in node.get("choices", [])]
    )


def test_t215_metadata_and_placeholder_removed() -> None:
    serialized = json.dumps(CAMILLE, ensure_ascii=False)
    assert "[J4 placeholder Camille pause]" not in serialized
    assert CAMILLE["schema_version"] == "0.1-j4-v2-experimental"
    assert CAMILLE["day"] == 4
    assert CAMILLE["experimental"] is True
    assert CAMILLE["conversation_id"] == "camille_j4_v2"


def test_t215_entry_variants_exact_order_conditions_and_converge() -> None:
    assert [variant["id"] for variant in CAMILLE["entry_variants"]] == ENTRY_VARIANTS
    variants = {variant["id"]: variant for variant in CAMILLE["entry_variants"]}
    assert variants["after_boundary_respected"]["conditions"] == {"flags_any": ["j3_camille_boundary_kept", "j3_camille_confusion_not_shifted"]}
    assert variants["after_tension_reopened"]["conditions"] == {"flags": ["j3_camille_tension_reopened"]}
    assert variants["after_pressure_high"]["conditions"] == {"flags": ["j3_camille_pressure_rises"]}
    assert variants["after_minimized"]["conditions"] == {"flags_any": ["j3_camille_minimized_again", "j3_camille_closes_badly"]}
    assert variants["default"]["conditions"] == {}
    for variant in CAMILLE["entry_variants"]:
        assert variant["start_node"] in NODES
        assert "j4_04_choice_camille_pause" in follow_until_choice(variant["start_node"])


def test_t215_single_replies_are_safe_and_mirrored() -> None:
    single_replies = [node for node in CAMILLE["nodes"] if "_single_reply_" in node["id"]]
    assert len(single_replies) == 5
    for node in single_replies:
        assert node["type"] == "choice"
        assert "effects" not in node
        assert len(node["choices"]) == 1
        choice = node["choices"][0]
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert "effects" not in player
        assert player["text"] == choice["text"]
        assert node["next"] == choice["next"]


def test_t215_central_choice_has_five_effectful_j4_choices() -> None:
    central = NODES["j4_04_choice_camille_pause"]
    assert central["type"] == "choice"
    assert central["text"] == "Que répondre à Camille ?"
    assert [choice["id"] for choice in central["choices"]] == CENTRAL_CHOICES
    for choice in central["choices"]:
        assert isinstance(choice.get("effects"), dict)
        flags = choice["effects"].get("flags", [])
        assert any(str(flag).startswith("j4_") for flag in flags)
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]


def test_t215_expected_effects_reward_respect_and_sanction_pressure() -> None:
    choices = {choice["id"]: choice for choice in NODES["j4_04_choice_camille_pause"]["choices"]}
    assert choices["j4_04_camille_respect_pause"]["effects"]["respect_camille"] == 2
    assert choices["j4_04_camille_respect_pause"]["effects"]["pression_camille"] == -1
    assert choices["j4_04_camille_push_too_much"]["effects"]["pression_camille"] == 2
    assert choices["j4_04_camille_push_too_much"]["effects"]["respect_camille"] == -1
    assert choices["j4_04_camille_name_trouble"]["effects"]["tension_camille"] == 2


def test_t215_each_central_branch_ends_on_end_node() -> None:
    for choice in NODES["j4_04_choice_camille_pause"]["choices"]:
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


def test_t215_visible_text_boundaries_no_external_names_no_explicit_no_media() -> None:
    assert all(node.get("type") != "media" for node in CAMILLE["nodes"])
    text = visible_text()
    for forbidden in ["Sarah", "Nico", "Maya", "Inès"]:
        assert forbidden not in text
    for forbidden_word in ["sexe", "nu", "nue", "nude", "lingerie"]:
        assert not re.search(rf"\\b{re.escape(forbidden_word)}\\b", text, flags=re.IGNORECASE)
    for required in ["pause", "minutes", "bosser", "travail"]:
        assert required in text


def test_t215_other_unwritten_j4_conversations_remain_skeletons() -> None:
    for name in OTHER_STILL_SKELETON_J4:
        data = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert len(data["nodes"]) == 2
        assert len(data["entry_variants"]) == 1
        assert data["entry_variants"][0]["id"] == "default"
        assert "placeholder" in json.dumps(data, ensure_ascii=False).lower()
        assert all("effects" not in node for node in data["nodes"])
        assert all(node.get("type") != "media" for node in data["nodes"])


if __name__ == "__main__":
    test_t215_metadata_and_placeholder_removed()
    test_t215_entry_variants_exact_order_conditions_and_converge()
    test_t215_single_replies_are_safe_and_mirrored()
    test_t215_central_choice_has_five_effectful_j4_choices()
    test_t215_expected_effects_reward_respect_and_sanction_pressure()
    test_t215_each_central_branch_ends_on_end_node()
    test_t215_visible_text_boundaries_no_external_names_no_explicit_no_media()
    test_t215_other_unwritten_j4_conversations_remain_skeletons()
    print("T215 Camille J4 work pause dialogue tests OK")
