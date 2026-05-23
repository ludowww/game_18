#!/usr/bin/env python3
"""T175: Nico J2 alibi scene replaces placeholder with validated structure."""

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NICO = DATA / "nico_j2_v2_experimental.json"
OTHER_J2 = [
    DATA / "sarah_j2_v2_experimental.json",
    DATA / "camille_j2_v2_experimental.json",
    DATA / "maya_j2_v2_experimental.json",
    DATA / "ines_j2_v2_experimental.json",
]
EXPECTED_VARIANTS = ["alibi_used", "second_cover", "asked_real_advice", "ignored_respiration", "default"]
EXPECTED_CHOICES = [
    "j2_02_nico_hold_line",
    "j2_02_nico_release_him",
    "j2_02_nico_partial_truth",
    "j2_02_nico_joke_escape",
]


def load(path=NICO):
    return json.loads(path.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def reaches_choice(start_id, nodes, target="j2_02_choice_nico_alibi"):
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
    assert "[J2 placeholder Nico matin]" not in json.dumps(data, ensure_ascii=False)
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


def test_central_choice_has_four_effectful_j2_choices_with_player_echoes():
    nodes = nodes_by_id(load())
    choice_node = nodes["j2_02_choice_nico_alibi"]
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


def test_nico_j2_branches_end_with_expected_end_nodes():
    nodes = nodes_by_id(load())
    for end_id in [
        "j2_02_end_nico_line_cost",
        "j2_02_end_nico_released",
        "j2_02_end_nico_partial_truth",
        "j2_02_end_nico_joke_warning",
    ]:
        assert nodes[end_id]["type"] == "end"
    assert nodes["j2_02_nico_player_hold_line"]["next"] == "j2_02_nico_hold_line_001"
    assert nodes["j2_02_nico_player_release_him"]["next"] == "j2_02_nico_release_001"
    assert nodes["j2_02_nico_player_partial_truth"]["next"] == "j2_02_nico_partial_truth_001"
    assert nodes["j2_02_nico_player_joke_escape"]["next"] == "j2_02_nico_joke_001"


def test_other_j2_files_are_not_rewritten_by_t175():
    expected = {
        "camille_j2_v2": "[J2 placeholder Camille après-midi]",
        "maya_j2_v2": "[J2 placeholder Maya après-midi]",
        "ines_j2_v2": "[J2 placeholder Inès soir]",
    }
    for path in OTHER_J2:
        data = load(path)
        if data["conversation_id"] == "sarah_j2_v2":
            assert "j2_01_choice_sarah_morning" in {node["id"] for node in data["nodes"]}
            continue
        first_message = next(node for node in data["nodes"] if node.get("type") == "message")
        assert first_message["text"] == expected[data["conversation_id"]]


def test_t173_and_j1_validator_stay_green():
    for command in (["python3", "tests/test_t173_j2_v2_structure.py"], ["python3", "tools/validate_j1_v2_experimental.py"]):
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        assert result.returncode == 0, result.stdout + result.stderr


if __name__ == "__main__":
    test_placeholder_is_removed_and_entry_variants_are_ordered()
    test_single_reply_nodes_follow_manual_reply_convention()
    test_central_choice_has_four_effectful_j2_choices_with_player_echoes()
    test_nico_j2_branches_end_with_expected_end_nodes()
    test_other_j2_files_are_not_rewritten_by_t175()
    test_t173_and_j1_validator_stay_green()
    print("T175 Nico J2 alibi dialogue tests OK")
