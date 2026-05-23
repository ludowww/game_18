#!/usr/bin/env python3
"""T177: Maya J2 social scene replaces placeholder with validated structure."""

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
MAYA = DATA / "maya_j2_v2_experimental.json"

EXPECTED_VARIANTS = [
    "photo_possible",
    "played_dumb",
    "not_involve",
    "timing_noted",
    "default",
]
EXPECTED_CHOICES = [
    "j2_04_maya_ask_direct",
    "j2_04_maya_admit_malaise",
    "j2_04_maya_play_innocent",
    "j2_04_maya_ask_discretion",
]


def load(path=MAYA):
    return json.loads(path.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def reaches_choice(start_id, nodes, target="j2_04_choice_maya_social"):
    current = start_id
    seen = set()
    while current and current not in seen:
        if current == target:
            return True
        seen.add(current)
        current = nodes[current].get("next", "")
    return False


def terminal_node(start_id, nodes):
    current = start_id
    seen = set()
    while current and current not in seen:
        seen.add(current)
        node = nodes[current]
        if node.get("type") == "end":
            return node
        current = node.get("next", "")
    return None


def test_placeholder_is_removed_and_entry_variants_are_ordered():
    data = load()
    assert "[J2 placeholder Maya après-midi]" not in json.dumps(data, ensure_ascii=False)
    assert [variant["id"] for variant in data["entry_variants"]] == EXPECTED_VARIANTS
    nodes = nodes_by_id(data)
    for variant in data["entry_variants"]:
        assert variant["start_node"] in nodes
        assert reaches_choice(variant["start_node"], nodes), variant["id"]


def test_maya_j2_contains_one_photo_media_node():
    nodes = nodes_by_id(load())
    media_nodes = [node for node in nodes.values() if node.get("type") == "media"]
    assert len(media_nodes) == 1
    media = media_nodes[0]
    assert media["id"] == "j2_04_maya_media_group_001"
    assert media["sender"] == "maya"
    assert media["media_type"] == "image"
    assert media["asset"] == "res://assets/media/j1_v2/maya_photo_groupe_j1.png"
    assert media["caption"] == "[photo de groupe envoyée]"


def test_single_reply_nodes_follow_manual_reply_convention():
    nodes = nodes_by_id(load())
    single_replies = [node for node in nodes.values() if "_single_reply_" in node["id"]]
    assert len(single_replies) == 5
    for node in single_replies:
        assert node["type"] == "choice"
        assert "effects" not in node
        assert len(node["choices"]) == 1
        choice = node["choices"][0]
        assert "effects" not in choice
        player = nodes[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]
        assert "effects" not in player


def test_central_choice_has_four_effectful_j2_choices_with_player_echoes():
    nodes = nodes_by_id(load())
    choice_node = nodes["j2_04_choice_maya_social"]
    assert choice_node["type"] == "choice"
    assert [choice["id"] for choice in choice_node["choices"]] == EXPECTED_CHOICES
    for choice in choice_node["choices"]:
        effects = choice.get("effects")
        assert isinstance(effects, dict)
        flags = effects.get("flags")
        assert isinstance(flags, list) and flags
        assert all(flag.startswith("j2_") for flag in flags)
        player = nodes[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]
        assert terminal_node(player["id"], nodes) is not None


def test_maya_j2_branches_end_with_expected_end_nodes():
    nodes = nodes_by_id(load())
    for end_id in [
        "j2_04_end_maya_social_read_opened",
        "j2_04_end_maya_malaise_named",
        "j2_04_end_maya_suspicion_grows",
        "j2_04_end_maya_sarah_protected",
    ]:
        assert nodes[end_id]["type"] == "end"


def test_previous_j2_tests_and_j1_validator_stay_green():
    for command in (
        ["python3", "tests/test_t176_camille_j2_tension_dialogue.py"],
        ["python3", "tests/test_t175_nico_j2_alibi_dialogue.py"],
        ["python3", "tests/test_t174_sarah_j2_morning_dialogue.py"],
        ["python3", "tests/test_t173_j2_v2_structure.py"],
        ["python3", "tools/validate_j1_v2_experimental.py"],
    ):
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        assert result.returncode == 0, result.stdout + result.stderr


if __name__ == "__main__":
    test_placeholder_is_removed_and_entry_variants_are_ordered()
    test_maya_j2_contains_one_photo_media_node()
    test_single_reply_nodes_follow_manual_reply_convention()
    test_central_choice_has_four_effectful_j2_choices_with_player_echoes()
    test_maya_j2_branches_end_with_expected_end_nodes()
    test_previous_j2_tests_and_j1_validator_stay_green()
    print("T177 Maya J2 social dialogue tests OK")
