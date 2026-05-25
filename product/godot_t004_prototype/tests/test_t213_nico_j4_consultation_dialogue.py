#!/usr/bin/env python3
"""T213: Nico J4 consultation scene reacts to Sarah J4 flags without omniscience."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NICO_PATH = DATA / "nico_j4_v2_experimental.json"
NICO = json.loads(NICO_PATH.read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in NICO["nodes"]}
ENTRY_VARIANTS = [
    "after_sarah_pending_check",
    "after_direct_sarah_answer",
    "after_sarah_delay",
    "after_sarah_defensive",
    "default",
]
CENTRAL_CHOICES = [
    "j4_02_nico_ask_advice",
    "j4_02_nico_ask_cover",
    "j4_02_nico_release_him",
    "j4_02_nico_joke_escape",
    "j4_02_nico_game_evening",
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
        if current == "j4_02_choice_nico_consultation":
            break
        current = NODES[current].get("next", "")
    return seen


def test_t213_metadata_and_placeholder_removed() -> None:
    serialized = json.dumps(NICO, ensure_ascii=False)
    assert "[J4 placeholder Nico consultation]" not in serialized
    assert NICO["schema_version"] == "0.1-j4-v2-experimental"
    assert NICO["day"] == 4
    assert NICO["experimental"] is True
    assert NICO["conversation_id"] == "nico_j4_v2"


def test_t213_entry_variants_exact_priority_and_converge() -> None:
    ids = [variant["id"] for variant in NICO["entry_variants"]]
    assert ids == ENTRY_VARIANTS
    assert ids.index("after_sarah_pending_check") < ids.index("after_sarah_delay")
    variants = {variant["id"]: variant for variant in NICO["entry_variants"]}
    assert variants["after_sarah_pending_check"]["conditions"] == {"flags": ["j4_sarah_answer_pending_nico_check"]}
    assert variants["after_direct_sarah_answer"]["conditions"] == {"flags": ["j4_player_given_direct_sarah_answer"]}
    assert variants["after_sarah_delay"]["conditions"] == {"flags": ["j4_player_delayed_sarah_answer"]}
    assert variants["after_sarah_defensive"]["conditions"] == {"flags": ["j4_player_defensive_with_sarah"]}
    assert variants["default"]["conditions"] == {}
    for variant in NICO["entry_variants"]:
        assert variant["start_node"] in NODES
        assert "j4_02_choice_nico_consultation" in follow_until_choice(variant["start_node"])


def test_t213_single_replies_are_safe_and_mirrored() -> None:
    single_replies = [node for node in NICO["nodes"] if "_single_reply_" in node["id"]]
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


def test_t213_central_choice_has_five_effectful_j4_choices() -> None:
    central = NODES["j4_02_choice_nico_consultation"]
    assert central["type"] == "choice"
    assert central["text"] == "Que demander à Nico ?"
    assert [choice["id"] for choice in central["choices"]] == CENTRAL_CHOICES
    for choice in central["choices"]:
        assert isinstance(choice.get("effects"), dict)
        flags = choice["effects"].get("flags", [])
        assert any(str(flag).startswith("j4_") for flag in flags)
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]


def test_t213_expected_effects_for_key_branches() -> None:
    choices = {choice["id"]: choice for choice in NODES["j4_02_choice_nico_consultation"]["choices"]}
    cover = choices["j4_02_nico_ask_cover"]["effects"]
    assert cover["dette_nico"] == 2
    assert cover["risque_exposition"] == 2
    assert "j4_nico_cover_requested" in cover["flags"]
    released = choices["j4_02_nico_release_him"]["effects"]
    assert released["dette_nico"] == -1
    assert "j4_nico_released_again" in released["flags"]
    game = choices["j4_02_nico_game_evening"]["effects"]
    assert game["fatigue_emotionnelle"] == -1
    assert "j4_nico_game_evening_seed" in game["flags"]


def test_t213_each_central_branch_ends_on_end_node() -> None:
    for choice in NODES["j4_02_choice_nico_consultation"]["choices"]:
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


def test_t213_visible_text_has_no_forbidden_omniscience_and_no_media() -> None:
    assert all(node.get("type") != "media" for node in NICO["nodes"])
    visible_text = "\n".join(
        [node.get("text", "") for node in NICO["nodes"]]
        + [choice.get("text", "") for node in NICO["nodes"] for choice in node.get("choices", [])]
    )
    for forbidden in [
        "Camille",
        "Maya",
        "Inès",
        "Sarah m’a dit",
        "Sarah pense",
        "Sarah sait",
        "elle m’a parlé",
        "elle a compris",
    ]:
        assert forbidden not in visible_text


def test_t213_other_unwritten_j4_conversations_remain_skeletons() -> None:
    for name in OTHER_STILL_SKELETON_J4:
        data = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert len(data["nodes"]) == 2
        assert len(data["entry_variants"]) == 1
        assert data["entry_variants"][0]["id"] == "default"
        assert "placeholder" in json.dumps(data, ensure_ascii=False).lower()
        assert all("effects" not in node for node in data["nodes"])
        assert all(node.get("type") != "media" for node in data["nodes"])


if __name__ == "__main__":
    test_t213_metadata_and_placeholder_removed()
    test_t213_entry_variants_exact_priority_and_converge()
    test_t213_single_replies_are_safe_and_mirrored()
    test_t213_central_choice_has_five_effectful_j4_choices()
    test_t213_expected_effects_for_key_branches()
    test_t213_each_central_branch_ends_on_end_node()
    test_t213_visible_text_has_no_forbidden_omniscience_and_no_media()
    test_t213_other_unwritten_j4_conversations_remain_skeletons()
    print("T213 Nico J4 consultation dialogue tests OK")
