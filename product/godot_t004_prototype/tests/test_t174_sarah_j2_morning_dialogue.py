#!/usr/bin/env python3
"""T174: Sarah J2 morning scene replaces the placeholder with validated structure."""

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SARAH = DATA / "sarah_j2_v2_experimental.json"
OTHER_J2 = [
    DATA / "nico_j2_v2_experimental.json",
    DATA / "camille_j2_v2_experimental.json",
    DATA / "maya_j2_v2_experimental.json",
    DATA / "ines_j2_v2_experimental.json",
]
EXPECTED_VARIANTS = [
    "after_nico_version",
    "after_camille_minimized",
    "after_domestic_presence",
    "after_late_meal",
    "default",
]
EXPECTED_CHOICES = [
    "j2_01_sarah_be_concrete",
    "j2_01_sarah_need_time",
    "j2_01_sarah_minimize_again",
    "j2_01_sarah_admit_incoherence",
]


def load(path=SARAH):
    return json.loads(path.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def reaches_choice(start_id, nodes, target="j2_01_choice_sarah_morning"):
    current = start_id
    seen = set()
    while current and current not in seen:
        if current == target:
            return True
        seen.add(current)
        node = nodes[current]
        current = node.get("next", "")
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
    serialized = json.dumps(data, ensure_ascii=False)
    assert "[J2 placeholder Sarah matin]" not in serialized
    assert [variant["id"] for variant in data["entry_variants"]] == EXPECTED_VARIANTS
    nodes = nodes_by_id(data)
    for variant in data["entry_variants"]:
        assert variant["start_node"] in nodes
        assert reaches_choice(variant["start_node"], nodes), variant["id"]


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
        assert player.get("choices") is None


def test_central_choice_has_four_effectful_j2_choices_with_player_echoes():
    nodes = nodes_by_id(load())
    choice_node = nodes["j2_01_choice_sarah_morning"]
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


def test_sarah_j2_branches_end_with_expected_end_nodes():
    nodes = nodes_by_id(load())
    for end_id in [
        "j2_01_end_sarah_concrete_fragile",
        "j2_01_end_sarah_time_distance",
        "j2_01_end_sarah_colder",
        "j2_01_end_sarah_fragile_named",
    ]:
        assert nodes[end_id]["type"] == "end"
    assert nodes["j2_01_sarah_player_be_concrete"]["next"] == "j2_01_sarah_concrete_001"
    assert nodes["j2_01_sarah_player_need_time"]["next"] == "j2_01_sarah_time_001"
    assert nodes["j2_01_sarah_player_minimize_again"]["next"] == "j2_01_sarah_minimize_001"
    assert nodes["j2_01_sarah_player_admit_incoherence"]["next"] == "j2_01_sarah_incoherence_001"


def test_other_j2_skeletons_remain_placeholders():
    expected = {
        "camille_j2_v2": "[J2 placeholder Camille après-midi]",
        "maya_j2_v2": "[J2 placeholder Maya après-midi]",
        "ines_j2_v2": "[J2 placeholder Inès soir]",
    }
    for path in OTHER_J2:
        data = load(path)
        node_ids = {node["id"] for node in data["nodes"]}
        if data["conversation_id"] == "nico_j2_v2":
            assert "j2_02_choice_nico_alibi" in node_ids
            continue
        if data["conversation_id"] == "camille_j2_v2":
            assert "j2_03_choice_camille_tension" in node_ids
            continue
        first_message = next(node for node in data["nodes"] if node.get("type") == "message")
        assert first_message["text"] == expected[data["conversation_id"]]


def test_j1_v2_validator_stays_green():
    result = subprocess.run(
        ["python3", "tools/validate_j1_v2_experimental.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


if __name__ == "__main__":
    test_placeholder_is_removed_and_entry_variants_are_ordered()
    test_single_reply_nodes_follow_manual_reply_convention()
    test_central_choice_has_four_effectful_j2_choices_with_player_echoes()
    test_sarah_j2_branches_end_with_expected_end_nodes()
    test_other_j2_skeletons_remain_placeholders()
    test_j1_v2_validator_stays_green()
    print("T174 Sarah J2 morning dialogue tests OK")
