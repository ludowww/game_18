#!/usr/bin/env python3
"""T146: neutral player replies must be manual single-choice clicks."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FILES = [
    "sarah_j1_v2_experimental.json",
    "camille_j1_v2_experimental.json",
    "nico_j1_v2_experimental.json",
    "maya_j1_v2_experimental.json",
    "ines_j1_v2_experimental.json",
    "sarah_meal_j1_v2_experimental.json",
    "nico_respiration_j1_v2_experimental.json",
]


def load(name):
    with (DATA / name).open(encoding="utf-8") as fh:
        return json.load(fh)


def assert_single_replies(data, name):
    nodes = {node["id"]: node for node in data["nodes"]}
    single_reply_ids = [node_id for node_id in nodes if "_single_reply_" in node_id]
    assert single_reply_ids, f"{name}: no _single_reply_ choice nodes found"

    for node_id in single_reply_ids:
        node = nodes[node_id]
        assert node.get("type") == "choice", f"{name}:{node_id} must be a choice node"
        choices = node.get("choices", [])
        assert len(choices) == 1, f"{name}:{node_id} must contain exactly one option"
        option = choices[0]
        target_id = option.get("next", "")
        assert target_id in nodes, f"{name}:{node_id} points to missing {target_id}"
        assert "_player_" in target_id, f"{name}:{node_id} must point to a _player_ node"
        target = nodes[target_id]
        assert target.get("sender") == "player", f"{name}:{target_id} must be sender player"
        assert target.get("type") == "message", f"{name}:{target_id} must be a message"
        assert option.get("text") == target.get("text"), f"{name}:{node_id} option text must match {target_id} text"
        assert "effects" not in target, f"{name}:{target_id} must not have effects"
        assert "choices" not in target, f"{name}:{target_id} must not have choices"
        next_id = target.get("next", "")
        assert next_id in nodes, f"{name}:{target_id} must lead to an existing node"


def assert_no_auto_player_nodes(data, name):
    offenders = [node["id"] for node in data["nodes"] if "_auto_player_" in node.get("id", "")]
    assert not offenders, f"{name}: _auto_player_ nodes still present: {offenders}"


def assert_multiple_choice_ids_preserved(data_by_name):
    expected = {
        "sarah_j1_v2_experimental.json": "j1_01_choice_version_sarah",
        "camille_j1_v2_experimental.json": "j1_02_choice_camille_dehors",
        "nico_j1_v2_experimental.json": "j1_03_choice_nico_version",
        "maya_j1_v2_experimental.json": "j1_04_choice_maya_pique",
        "ines_j1_v2_experimental.json": "j1_05_choice_ines_faille",
        "sarah_meal_j1_v2_experimental.json": "j1_06_choice_sarah_meal",
        "nico_respiration_j1_v2_experimental.json": "j1_07_choice_nico_respiration",
    }
    for name, choice_id in expected.items():
        ids = {node["id"] for node in data_by_name[name]["nodes"]}
        assert choice_id in ids, f"{name}: missing existing multiple choice {choice_id}"


def main():
    data_by_name = {name: load(name) for name in FILES}
    for name, data in data_by_name.items():
        assert_single_replies(data, name)
        assert_no_auto_player_nodes(data, name)
    assert_multiple_choice_ids_preserved(data_by_name)
    print("T146 single reply nodes tests OK")


if __name__ == "__main__":
    main()
