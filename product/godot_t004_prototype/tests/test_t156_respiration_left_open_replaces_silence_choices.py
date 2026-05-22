#!/usr/bin/env python3
"""T156: respiration scenes move silence/late reply choices to left_open state."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")

SARAH_CHOICES = [
    "j1_06_come_home",
    "j1_06_later",
    "j1_06_uncertain",
    "j1_06_work_excuse",
]

NICO_CHOICES = [
    "j1_07_share_joke",
    "j1_07_ask_real_advice",
    "j1_07_second_cover",
    "j1_07_joke_avoid",
]


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def choice_ids(data, node_id):
    return [choice["id"] for choice in nodes_by_id(data)[node_id]["choices"]]


def test_sarah_meal_late_reply_choice_removed_and_four_choices_remain():
    data = load("sarah_meal_j1_v2_experimental.json")
    ids = choice_ids(data, "j1_06_choice_sarah_meal")
    assert "j1_06_late_reply" not in ids
    assert ids == SARAH_CHOICES


def test_nico_respiration_silence_choice_removed_and_four_choices_remain():
    data = load("nico_respiration_j1_v2_experimental.json")
    ids = choice_ids(data, "j1_07_choice_nico_respiration")
    assert "j1_07_silence" not in ids
    assert ids == NICO_CHOICES


def test_archive_end_nodes_remain_present_for_future_fallbacks():
    sarah_nodes = nodes_by_id(load("sarah_meal_j1_v2_experimental.json"))
    nico_nodes = nodes_by_id(load("nico_respiration_j1_v2_experimental.json"))
    assert "j1_06_end_late_cold" in sarah_nodes
    assert "j1_07_end_friend_waits" in nico_nodes


def test_removed_choices_are_not_referenced_from_choice_nodes():
    for name, removed_next in [
        ("sarah_meal_j1_v2_experimental.json", "j1_06_end_late_cold"),
        ("nico_respiration_j1_v2_experimental.json", "j1_07_end_friend_waits"),
    ]:
        data = load(name)
        for node in data["nodes"]:
            if node.get("type") != "choice":
                continue
            for choice in node.get("choices", []):
                assert choice.get("next") != removed_next, (name, node["id"], choice["id"])


def test_left_open_flags_and_marking_function_remain_available():
    assert "late_reply_sarah_meal_j1" in STATE
    assert "ignored_nico_respiration_j1" in STATE
    assert "func mark_current_left_open_if_pending_choice" in STATE
    assert "late_reply_prepared" in STATE
    assert "left_open" in STATE


if __name__ == "__main__":
    test_sarah_meal_late_reply_choice_removed_and_four_choices_remain()
    test_nico_respiration_silence_choice_removed_and_four_choices_remain()
    test_archive_end_nodes_remain_present_for_future_fallbacks()
    test_removed_choices_are_not_referenced_from_choice_nodes()
    test_left_open_flags_and_marking_function_remain_available()
    print("T156 respiration left_open replacement tests OK")
