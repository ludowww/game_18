#!/usr/bin/env python3
"""T214: Sarah J4 follow-up closes Sarah/Nico cross-thread without Sarah omniscience."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SARAH_FOLLOWUP_PATH = DATA / "sarah_j4_followup_v2_experimental.json"
SARAH = json.loads(SARAH_FOLLOWUP_PATH.read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in SARAH["nodes"]}
ENTRY_VARIANTS = [
    "after_nico_helped_version",
    "after_nico_advice",
    "after_nico_released",
    "after_delay_only",
    "after_defensive",
    "default",
]
CENTRAL_CHOICES = [
    "j4_03_sarah_own_delay",
    "j4_03_sarah_simple_answer",
    "j4_03_sarah_minimize_detail",
    "j4_03_sarah_searched_words",
    "j4_03_sarah_defensive_followup",
]
OTHER_STILL_SKELETON_J4 = [
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
        if current == "j4_03_choice_sarah_followup":
            break
        current = NODES[current].get("next", "")
    return seen


def test_t214_metadata_and_placeholder_removed() -> None:
    serialized = json.dumps(SARAH, ensure_ascii=False)
    assert "[J4 placeholder Sarah retour]" not in serialized
    assert SARAH["schema_version"] == "0.1-j4-v2-experimental"
    assert SARAH["day"] == 4
    assert SARAH["experimental"] is True
    assert SARAH["conversation_id"] == "sarah_j4_followup_v2"


def test_t214_entry_variants_exact_order_conditions_and_converge() -> None:
    ids = [variant["id"] for variant in SARAH["entry_variants"]]
    assert ids == ENTRY_VARIANTS
    variants = {variant["id"]: variant for variant in SARAH["entry_variants"]}
    assert variants["after_nico_helped_version"]["conditions"] == {"flags": ["j4_nico_helped_version"]}
    assert variants["after_nico_advice"]["conditions"] == {"flags": ["j4_nico_advised_direct_answer"]}
    assert variants["after_nico_released"]["conditions"] == {"flags_any": ["j4_nico_released_again", "j4_player_chooses_own_answer"]}
    assert variants["after_delay_only"]["conditions"] == {"flags": ["j4_player_delayed_sarah_answer"]}
    assert variants["after_defensive"]["conditions"] == {"flags_any": ["j4_player_defensive_with_sarah", "j4_nico_joke_escape"]}
    assert variants["default"]["conditions"] == {}
    for variant in SARAH["entry_variants"]:
        assert variant["start_node"] in NODES
        assert "j4_03_choice_sarah_followup" in follow_until_choice(variant["start_node"])


def test_t214_single_replies_are_safe_and_mirrored() -> None:
    single_replies = [node for node in SARAH["nodes"] if "_single_reply_" in node["id"]]
    assert len(single_replies) == 6
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


def test_t214_central_choice_has_five_effectful_j4_choices() -> None:
    central = NODES["j4_03_choice_sarah_followup"]
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


def test_t214_expected_effects_for_followup_postures() -> None:
    choices = {choice["id"]: choice for choice in NODES["j4_03_choice_sarah_followup"]["choices"]}
    assert choices["j4_03_sarah_own_delay"]["effects"]["confiance_sarah"] == 1
    assert "j4_player_owns_delay" in choices["j4_03_sarah_own_delay"]["effects"]["flags"]
    assert choices["j4_03_sarah_simple_answer"]["effects"]["confiance_sarah"] == 2
    assert choices["j4_03_sarah_simple_answer"]["effects"]["distance_sarah"] == -1
    assert choices["j4_03_sarah_minimize_detail"]["effects"]["distance_sarah"] == 1
    assert choices["j4_03_sarah_defensive_followup"]["effects"]["distance_sarah"] == 2


def test_t214_each_central_branch_ends_on_end_node() -> None:
    for choice in NODES["j4_03_choice_sarah_followup"]["choices"]:
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


def test_t214_visible_text_has_no_nico_or_forbidden_omniscience_and_no_media() -> None:
    assert all(node.get("type") != "media" for node in SARAH["nodes"])
    visible_text = "\n".join(
        [node.get("text", "") for node in SARAH["nodes"]]
        + [choice.get("text", "") for node in SARAH["nodes"] for choice in node.get("choices", [])]
    )
    for forbidden in [
        "Nico",
        "tu as demandé à Nico",
        "Nico t’a aidé",
        "vous vous êtes mis d’accord",
        "je sais que tu as vérifié",
        "je sais que tu as demandé",
    ]:
        assert forbidden not in visible_text
    serialized = json.dumps(SARAH, ensure_ascii=False)
    assert "j4_nico_helped_version" in serialized
    assert "j4_nico_advised_direct_answer" in serialized


def test_t214_other_unwritten_j4_conversations_remain_skeletons() -> None:
    for name in OTHER_STILL_SKELETON_J4:
        data = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert len(data["nodes"]) == 2
        assert len(data["entry_variants"]) == 1
        assert data["entry_variants"][0]["id"] == "default"
        assert "placeholder" in json.dumps(data, ensure_ascii=False).lower()
        assert all("effects" not in node for node in data["nodes"])
        assert all(node.get("type") != "media" for node in data["nodes"])


if __name__ == "__main__":
    test_t214_metadata_and_placeholder_removed()
    test_t214_entry_variants_exact_order_conditions_and_converge()
    test_t214_single_replies_are_safe_and_mirrored()
    test_t214_central_choice_has_five_effectful_j4_choices()
    test_t214_expected_effects_for_followup_postures()
    test_t214_each_central_branch_ends_on_end_node()
    test_t214_visible_text_has_no_nico_or_forbidden_omniscience_and_no_media()
    test_t214_other_unwritten_j4_conversations_remain_skeletons()
    print("T214 Sarah J4 follow-up dialogue tests OK")
