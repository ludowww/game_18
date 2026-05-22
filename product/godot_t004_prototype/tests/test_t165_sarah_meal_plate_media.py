#!/usr/bin/env python3
"""T165: Sarah meal includes a domestic plate photo placeholder media node."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SARAH_MEAL = DATA / "sarah_meal_j1_v2_experimental.json"

CHOICE_IDS = [
    "j1_06_come_home",
    "j1_06_later",
    "j1_06_uncertain",
    "j1_06_work_excuse",
]
LATE_REOPEN_IDS = [
    "j1_06_sarah_late_reopen_001",
    "j1_06_sarah_late_reopen_002",
    "j1_06_sarah_single_reply_late_reopen_001",
    "j1_06_sarah_player_late_reopen_001",
    "j1_06_sarah_late_reopen_003",
    "j1_06_sarah_late_reopen_004",
]


def load():
    return json.loads(SARAH_MEAL.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def test_sarah_meal_contains_plate_media_placeholder():
    nodes = nodes_by_id(load())
    media = nodes["j1_06_sarah_media_plate_001"]
    assert media["type"] == "media"
    assert media["sender"] == "sarah"
    assert media["media_type"] == "image"
    assert media["caption"] == "[photo de l’assiette envoyée]"
    assert media["asset"] == ""


def test_plate_media_is_inserted_after_sarah_002_and_returns_to_flow():
    nodes = nodes_by_id(load())
    assert nodes["j1_06_sarah_002"]["text"] == "J’ai fait trop de pâtes. Comme toujours."
    assert nodes["j1_06_sarah_002"]["next"] == "j1_06_sarah_media_plate_001"
    assert nodes["j1_06_sarah_media_plate_001"]["next"] == "j1_06_sarah_002b"
    assert nodes["j1_06_sarah_002b"]["text"] == "j’ai pas fait exprès que ça ressemble à une mise en scène."
    assert nodes["j1_06_sarah_002b"]["next"] == "j1_06_sarah_003"
    assert nodes["j1_06_sarah_003"]["text"] == "Et ton pull est encore sur la chaise."


def test_sarah_meal_choice_node_is_unchanged():
    nodes = nodes_by_id(load())
    choice = nodes["j1_06_choice_sarah_meal"]
    assert [item["id"] for item in choice["choices"]] == CHOICE_IDS
    for item in choice["choices"]:
        assert isinstance(item.get("effects"), dict)
        assert isinstance(item["effects"].get("flags"), list)


def test_sarah_meal_late_reopen_nodes_still_exist_and_keep_path():
    nodes = nodes_by_id(load())
    for node_id in LATE_REOPEN_IDS:
        assert node_id in nodes
    assert nodes["j1_06_sarah_late_reopen_001"]["text"] == "J’ai mangé un peu."
    assert nodes["j1_06_sarah_late_reopen_002"]["text"] == "J’ai laissé ton assiette sur le côté."
    assert nodes["j1_06_sarah_late_reopen_004"]["next"] == "j1_06_choice_sarah_meal"


if __name__ == "__main__":
    test_sarah_meal_contains_plate_media_placeholder()
    test_plate_media_is_inserted_after_sarah_002_and_returns_to_flow()
    test_sarah_meal_choice_node_is_unchanged()
    test_sarah_meal_late_reopen_nodes_still_exist_and_keep_path()
    print("T165 Sarah meal plate media tests OK")
