#!/usr/bin/env python3
"""T164: Nico respiration includes a meme placeholder media node."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NICO = DATA / "nico_respiration_j1_v2_experimental.json"

CHOICE_IDS = [
    "j1_07_share_joke",
    "j1_07_ask_real_advice",
    "j1_07_second_cover",
    "j1_07_joke_avoid",
]
LATE_REOPEN_IDS = [
    "j1_07_nico_late_reopen_001",
    "j1_07_nico_late_reopen_002",
    "j1_07_nico_single_reply_late_reopen_001",
    "j1_07_nico_player_late_reopen_001",
    "j1_07_nico_late_reopen_003",
    "j1_07_nico_late_reopen_004",
]


def load():
    return json.loads(NICO.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def test_nico_respiration_contains_meme_media_placeholder():
    nodes = nodes_by_id(load())
    media = nodes["j1_07_nico_media_meme_001"]
    assert media["type"] == "media"
    assert media["sender"] == "nico"
    assert media["media_type"] == "image"
    assert media["caption"] == "[meme envoyé]"
    assert media["asset"] == ""


def test_meme_media_is_inserted_after_nico_002_and_returns_to_flow():
    nodes = nodes_by_id(load())
    assert nodes["j1_07_nico_002"]["text"] == "il est nul, donc il devrait te parler."
    assert nodes["j1_07_nico_002"]["next"] == "j1_07_nico_media_meme_001"
    assert nodes["j1_07_nico_media_meme_001"]["next"] == "j1_07_nico_002b"
    assert nodes["j1_07_nico_002b"]["text"] == "voilà. zéro budget, mais intention sincère."
    assert nodes["j1_07_nico_002b"]["next"] == "j1_07_nico_003"


def test_nico_respiration_choice_node_is_unchanged():
    nodes = nodes_by_id(load())
    choice = nodes["j1_07_choice_nico_respiration"]
    assert [item["id"] for item in choice["choices"]] == CHOICE_IDS
    for item in choice["choices"]:
        assert isinstance(item.get("effects"), dict)
        assert isinstance(item["effects"].get("flags"), list)


def test_nico_late_reopen_nodes_still_exist_and_keep_path():
    nodes = nodes_by_id(load())
    for node_id in LATE_REOPEN_IDS:
        assert node_id in nodes
    assert nodes["j1_07_nico_late_reopen_004"]["next"] == "j1_07_choice_nico_respiration"


if __name__ == "__main__":
    test_nico_respiration_contains_meme_media_placeholder()
    test_meme_media_is_inserted_after_nico_002_and_returns_to_flow()
    test_nico_respiration_choice_node_is_unchanged()
    test_nico_late_reopen_nodes_still_exist_and_keep_path()
    print("T164 Nico respiration meme media tests OK")
