#!/usr/bin/env python3
"""T157: Sarah meal late reopen flow after leaving the meal choice open."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")
SCREEN = (ROOT / "scripts" / "conversation_screen.gd").read_text(encoding="utf-8")
SARAH_MEAL = DATA / "sarah_meal_j1_v2_experimental.json"

LATE_NODES = [
    "j1_06_sarah_late_reopen_001",
    "j1_06_sarah_late_reopen_002",
    "j1_06_sarah_single_reply_late_reopen_001",
    "j1_06_sarah_player_late_reopen_001",
    "j1_06_sarah_late_reopen_003",
    "j1_06_sarah_late_reopen_004",
]
PLAYER_TEXT = "Désolé. J’ai laissé passer le message."


def load():
    return json.loads(SARAH_MEAL.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def test_late_reopen_nodes_exist_with_expected_texts():
    nodes = nodes_by_id(load())
    for node_id in LATE_NODES:
        assert node_id in nodes
    assert nodes["j1_06_sarah_late_reopen_001"]["text"] == "J’ai mangé un peu."
    assert nodes["j1_06_sarah_late_reopen_002"]["text"] == "J’ai laissé ton assiette sur le côté."
    assert nodes["j1_06_sarah_late_reopen_003"]["text"] == "J’ai vu."
    assert nodes["j1_06_sarah_late_reopen_004"]["text"] == "Tu peux encore rentrer. Mais ce sera pas tout à fait le même repas."


def test_late_reopen_path_returns_to_existing_choice_node():
    nodes = nodes_by_id(load())
    assert nodes["j1_06_sarah_late_reopen_001"]["next"] == "j1_06_sarah_late_reopen_002"
    assert nodes["j1_06_sarah_late_reopen_002"]["next"] == "j1_06_sarah_single_reply_late_reopen_001"
    assert nodes["j1_06_sarah_player_late_reopen_001"]["next"] == "j1_06_sarah_late_reopen_003"
    assert nodes["j1_06_sarah_late_reopen_003"]["next"] == "j1_06_sarah_late_reopen_004"
    assert nodes["j1_06_sarah_late_reopen_004"]["next"] == "j1_06_choice_sarah_meal"


def test_late_reopen_single_reply_respects_convention():
    nodes = nodes_by_id(load())
    choice = nodes["j1_06_sarah_single_reply_late_reopen_001"]
    assert choice["type"] == "choice"
    assert "_single_reply_" in choice["id"]
    assert len(choice["choices"]) == 1
    option = choice["choices"][0]
    assert option["text"] == PLAYER_TEXT
    assert option["next"] == "j1_06_sarah_player_late_reopen_001"
    player = nodes["j1_06_sarah_player_late_reopen_001"]
    assert player["sender"] == "player"
    assert player["text"] == PLAYER_TEXT
    assert "effects" not in player
    assert "choices" not in player


def test_runtime_selects_sarah_meal_late_reopen_from_left_open_state():
    assert "func current_late_reopen_start_node" in STATE
    assert "late_reply_sarah_meal_j1" in STATE
    assert "j1_06_sarah_late_reopen_001" in STATE
    assert "late_reply_prepared" in STATE
    assert "left_open" in STATE
    assert "late_reopen_consumed" in STATE
    assert "ConversationState.current_late_reopen_start_node()" in SCREEN


def test_late_reopen_is_consumed_and_not_replayed():
    assert "consume_current_late_reopen" in STATE
    assert "late_reopen_consumed" in STATE
    consume_body = STATE[STATE.index("func consume_current_late_reopen"):]
    consume_body = consume_body.split("\nfunc ", 1)[0]
    assert "late_reopen_consumed" in consume_body
    assert "late_reply_prepared" in consume_body
    assert "left_open" in consume_body


if __name__ == "__main__":
    test_late_reopen_nodes_exist_with_expected_texts()
    test_late_reopen_path_returns_to_existing_choice_node()
    test_late_reopen_single_reply_respects_convention()
    test_runtime_selects_sarah_meal_late_reopen_from_left_open_state()
    test_late_reopen_is_consumed_and_not_replayed()
    print("T157 Sarah meal late reopen tests OK")
