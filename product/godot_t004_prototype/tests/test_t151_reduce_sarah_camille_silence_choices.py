#!/usr/bin/env python3
"""T151: remove explicit silence choices from Sarah and Camille multi-choice nodes."""

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

SARAH_CHOICES = [
    "j1_01_needed_air",
    "j1_01_nico_alibi",
    "j1_01_camille_minimized",
    "j1_01_vulnerable",
]

CAMILLE_REQUIRED_CHOICES = [
    "j1_02_admit_tension",
    "j1_02_respect_boundary",
    "j1_02_minimize",
    "j1_02_early_desire",
    "j1_02_uncertain",
]

SILENCE_ARCHIVE_NODES = {
    "sarah_j1_v2_experimental.json": [
        "j1_01_sys_006e",
        "j1_01_sys_007e",
        "j1_01_sarah_008e",
        "j1_01_sarah_009e",
        "j1_01_end_no_clear_version",
    ],
    "camille_j1_v2_experimental.json": [
        "j1_02_sys_005f",
        "j1_02_sys_006f",
        "j1_02_camille_007f",
        "j1_02_camille_008f",
        "j1_02_end_camille_left_on_read",
    ],
}


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def choice_node(data, node_id):
    return nodes_by_id(data)[node_id]


def choice_by_id(choice_node_data, choice_id):
    for choice in choice_node_data["choices"]:
        if choice["id"] == choice_id:
            return choice
    raise AssertionError(f"missing choice {choice_id}")


def test_sarah_silence_choice_removed_and_four_choices_remain():
    data = load("sarah_j1_v2_experimental.json")
    choice = choice_node(data, "j1_01_choice_version_sarah")
    ids = [item["id"] for item in choice["choices"]]
    assert "j1_01_silence" not in ids
    assert ids == SARAH_CHOICES


def test_camille_silence_choice_removed_and_uncertain_kept():
    data = load("camille_j1_v2_experimental.json")
    choice = choice_node(data, "j1_02_choice_camille_dehors")
    ids = [item["id"] for item in choice["choices"]]
    assert "j1_02_silence" not in ids
    for required_id in CAMILLE_REQUIRED_CHOICES:
        assert required_id in ids
    assert ids == CAMILLE_REQUIRED_CHOICES


def test_kept_choice_effects_and_flags_are_still_present():
    for name, node_id, expected_ids in [
        ("sarah_j1_v2_experimental.json", "j1_01_choice_version_sarah", SARAH_CHOICES),
        ("camille_j1_v2_experimental.json", "j1_02_choice_camille_dehors", CAMILLE_REQUIRED_CHOICES),
    ]:
        choice = choice_node(load(name), node_id)
        for choice_id in expected_ids:
            item = choice_by_id(choice, choice_id)
            effects = item.get("effects")
            assert isinstance(effects, dict), (name, choice_id)
            assert isinstance(effects.get("flags"), list), (name, choice_id)


def test_silence_archive_nodes_remain_unreferenced_from_choice_nodes():
    for name, archive_ids in SILENCE_ARCHIVE_NODES.items():
        data = load(name)
        nodes = nodes_by_id(data)
        for archive_id in archive_ids:
            assert archive_id in nodes, (name, archive_id)
        for node in data["nodes"]:
            if node.get("type") != "choice":
                continue
            for item in node.get("choices", []):
                assert item.get("next") not in archive_ids, (name, node["id"], item["id"], item.get("next"))


if __name__ == "__main__":
    test_sarah_silence_choice_removed_and_four_choices_remain()
    test_camille_silence_choice_removed_and_uncertain_kept()
    test_kept_choice_effects_and_flags_are_still_present()
    test_silence_archive_nodes_remain_unreferenced_from_choice_nodes()
    print("T151 Sarah/Camille silence choice reduction tests OK")
