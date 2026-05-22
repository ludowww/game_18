#!/usr/bin/env python3
"""T160: Nico respiration late reopen flow after leaving its choice open."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")
NICO = DATA / "nico_respiration_j1_v2_experimental.json"
SARAH = DATA / "sarah_meal_j1_v2_experimental.json"

LATE_NODES = [
    "j1_07_nico_late_reopen_001",
    "j1_07_nico_late_reopen_002",
    "j1_07_nico_single_reply_late_reopen_001",
    "j1_07_nico_player_late_reopen_001",
    "j1_07_nico_late_reopen_003",
    "j1_07_nico_late_reopen_004",
]
PLAYER_TEXT = "J’ai décroché deux minutes."


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def function_body(name: str) -> str:
    marker = f"func {name}"
    assert marker in STATE, marker
    body = STATE[STATE.index(marker):]
    return body.split("\nfunc ", 1)[0]


def test_nico_late_reopen_nodes_exist_with_expected_texts():
    nodes = nodes_by_id(load(NICO))
    for node_id in LATE_NODES:
        assert node_id in nodes
    assert nodes["j1_07_nico_late_reopen_001"]["text"] == "ok donc même mon meme tu l’as laissé en vu"
    assert nodes["j1_07_nico_late_reopen_002"]["text"] == "violent mais je respecte la constance"
    assert nodes["j1_07_nico_late_reopen_003"]["text"] == "deux minutes chez toi c’est une unité très souple"
    assert nodes["j1_07_nico_late_reopen_004"]["text"] == "bon. pizza, fuite ou vraie phrase ?"


def test_nico_late_reopen_path_returns_to_existing_choice_node():
    nodes = nodes_by_id(load(NICO))
    assert nodes["j1_07_nico_late_reopen_001"]["next"] == "j1_07_nico_late_reopen_002"
    assert nodes["j1_07_nico_late_reopen_002"]["next"] == "j1_07_nico_single_reply_late_reopen_001"
    assert nodes["j1_07_nico_player_late_reopen_001"]["next"] == "j1_07_nico_late_reopen_003"
    assert nodes["j1_07_nico_late_reopen_003"]["next"] == "j1_07_nico_late_reopen_004"
    assert nodes["j1_07_nico_late_reopen_004"]["next"] == "j1_07_choice_nico_respiration"


def test_nico_late_reopen_single_reply_respects_convention():
    nodes = nodes_by_id(load(NICO))
    choice = nodes["j1_07_nico_single_reply_late_reopen_001"]
    assert choice["type"] == "choice"
    assert "_single_reply_" in choice["id"]
    assert len(choice["choices"]) == 1
    option = choice["choices"][0]
    assert option["text"] == PLAYER_TEXT
    assert option["next"] == "j1_07_nico_player_late_reopen_001"
    player = nodes["j1_07_nico_player_late_reopen_001"]
    assert player["sender"] == "player"
    assert player["text"] == PLAYER_TEXT
    assert "effects" not in player
    assert "choices" not in player


def test_runtime_selects_nico_late_reopen_from_left_open_state():
    assert "ignored_nico_respiration_j1" in STATE
    assert "j1_07_choice_nico_respiration" in STATE
    assert "j1_07_nico_late_reopen_001" in STATE
    assert "late_reply_prepared" in STATE
    assert "left_open" in STATE
    assert "_late_reopen_start_for_context" in STATE


def test_nico_late_reopen_uses_t159_consumed_context_to_avoid_loop():
    body = function_body("mark_current_left_open_if_pending_choice")
    assert "same_late_reopen_already_consumed" in body
    assert "late_reopen_consumed_flag" in body
    assert "late_reopen_consumed_choice_node" in body
    assert "ignored_nico_respiration_j1" in STATE


def test_sarah_late_reopen_still_exists():
    nodes = nodes_by_id(load(SARAH))
    assert "j1_06_sarah_late_reopen_001" in nodes
    assert "j1_06_choice_sarah_meal" in STATE
    assert "j1_06_sarah_late_reopen_001" in STATE


if __name__ == "__main__":
    test_nico_late_reopen_nodes_exist_with_expected_texts()
    test_nico_late_reopen_path_returns_to_existing_choice_node()
    test_nico_late_reopen_single_reply_respects_convention()
    test_runtime_selects_nico_late_reopen_from_left_open_state()
    test_nico_late_reopen_uses_t159_consumed_context_to_avoid_loop()
    test_sarah_late_reopen_still_exists()
    print("T160 Nico respiration late reopen tests OK")
