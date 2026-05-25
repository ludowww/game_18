#!/usr/bin/env python3
"""T212: Sarah J4 morning scene replaces placeholder and prepares Sarah/Nico cross-thread safely."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SARAH_PATH = DATA / "sarah_j4_v2_experimental.json"
SARAH = json.loads(SARAH_PATH.read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in SARAH["nodes"]}
ENTRY_VARIANTS = [
    "after_actions_promised",
    "after_honest_uncertainty",
    "after_more_time",
    "after_defensive",
    "default",
]
CENTRAL_CHOICES = [
    "j4_01_sarah_answer_directly",
    "j4_01_sarah_prudent_truth",
    "j4_01_sarah_delay_answer",
    "j4_01_sarah_check_before_answer",
    "j4_01_sarah_defensive",
]
OTHER_J4 = [
    "sarah_j4_followup_v2_experimental.json",
    "camille_j4_v2_experimental.json",
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
        if current == "j4_01_choice_sarah_morning_detail":
            break
        current = NODES[current].get("next", "")
    return seen


def test_t212_metadata_and_placeholder_removed() -> None:
    serialized = json.dumps(SARAH, ensure_ascii=False)
    assert "[J4 placeholder Sarah matin]" not in serialized
    assert SARAH["schema_version"] == "0.1-j4-v2-experimental"
    assert SARAH["day"] == 4
    assert SARAH["experimental"] is True
    assert SARAH["conversation_id"] == "sarah_j4_v2"


def test_t212_entry_variants_exact_and_converge() -> None:
    assert [variant["id"] for variant in SARAH["entry_variants"]] == ENTRY_VARIANTS
    variants = {variant["id"]: variant for variant in SARAH["entry_variants"]}
    assert variants["after_actions_promised"]["conditions"] == {"flags": ["j3_sarah_promises_actions"]}
    assert variants["after_honest_uncertainty"]["conditions"] == {"flags": ["j3_sarah_honest_uncertainty"]}
    assert variants["after_more_time"]["conditions"] == {"flags": ["j3_sarah_more_time"]}
    assert variants["after_defensive"]["conditions"] == {"flags_any": ["j3_sarah_defensive", "j3_sarah_feels_unheard"]}
    assert variants["default"]["conditions"] == {}
    for variant in SARAH["entry_variants"]:
        assert variant["start_node"] in NODES
        assert "j4_01_choice_sarah_morning_detail" in follow_until_choice(variant["start_node"])


def test_t212_single_replies_are_safe_and_mirrored() -> None:
    single_replies = [node for node in SARAH["nodes"] if "_single_reply_" in node["id"]]
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


def test_t212_central_choice_has_five_effectful_j4_choices() -> None:
    central = NODES["j4_01_choice_sarah_morning_detail"]
    assert central["type"] == "choice"
    assert central["text"] == "Que répondre à Sarah ?"
    assert [choice["id"] for choice in central["choices"]] == CENTRAL_CHOICES
    for choice in central["choices"]:
        assert isinstance(choice.get("effects"), dict)
        flags = choice["effects"].get("flags", [])
        assert any(str(flag).startswith("j4_") for flag in flags)
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]


def test_t212_each_central_branch_ends_on_end_node() -> None:
    for choice in NODES["j4_01_choice_sarah_morning_detail"]["choices"]:
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


def test_t212_visible_text_has_no_external_character_knowledge_and_no_media() -> None:
    assert all(node.get("type") != "media" for node in SARAH["nodes"])
    visible_text = "\n".join(
        [node.get("text", "") for node in SARAH["nodes"]]
        + [choice.get("text", "") for node in SARAH["nodes"] for choice in node.get("choices", [])]
    )
    for forbidden in ["Nico", "Camille", "Maya", "Inès", "tu as demandé à Nico", "Nico m’a dit", "vous vous êtes mis d’accord"]:
        assert forbidden not in visible_text
    serialized = json.dumps(SARAH, ensure_ascii=False)
    assert "j4_player_checked_with_nico" in serialized


def test_t212_other_j4_conversations_remain_skeletons() -> None:
    for name in OTHER_J4:
        data = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert len(data["nodes"]) == 2
        assert len(data["entry_variants"]) == 1
        assert data["entry_variants"][0]["id"] == "default"
        assert "placeholder" in json.dumps(data, ensure_ascii=False).lower()
        assert all("effects" not in node for node in data["nodes"])
        assert all(node.get("type") != "media" for node in data["nodes"])


if __name__ == "__main__":
    test_t212_metadata_and_placeholder_removed()
    test_t212_entry_variants_exact_and_converge()
    test_t212_single_replies_are_safe_and_mirrored()
    test_t212_central_choice_has_five_effectful_j4_choices()
    test_t212_each_central_branch_ends_on_end_node()
    test_t212_visible_text_has_no_external_character_knowledge_and_no_media()
    test_t212_other_j4_conversations_remain_skeletons()
    print("T212 Sarah J4 morning dialogue tests OK")
