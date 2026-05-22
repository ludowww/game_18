#!/usr/bin/env python3
"""T147: compact single-choice UI and robust player-bubble dedupe."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"
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
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def test_choice_panel_height_is_dynamic():
    source = SCREEN.read_text(encoding="utf-8")
    assert "func _choice_panel_height_for_choices(choices: Array) -> float:" in source
    assert "choices.size() <= 1" in source
    assert "_choice_button_height(text) + 42" in source
    assert "min(float(total), CHOICE_PANEL_MAX_HEIGHT)" in source
    assert "choice_scroll.custom_minimum_size = Vector2(0, _choice_panel_height_for_choices(choices))" in source


def test_choice_dedupe_uses_next_player_node_not_text_equality():
    source = SCREEN.read_text(encoding="utf-8")
    assert "func _choice_next_is_player_node(next_id: String) -> bool:" in source
    assert "return str(next_node.get(\"sender\", \"\")) == \"player\"" in source
    assert "if not _choice_next_is_player_node(next_id):" in source
    assert "_choice_text_is_repeated_by_next_player_node" not in source


def iter_choices(data):
    nodes = {node["id"]: node for node in data["nodes"]}
    for node in data["nodes"]:
        if node.get("type") != "choice":
            continue
        for choice in node.get("choices", []):
            yield node, choice, nodes


def test_choice_text_matches_next_player_node_text():
    for name in FILES:
        data = load(name)
        for choice_node, choice, nodes in iter_choices(data):
            next_id = choice.get("next", "")
            if next_id not in nodes:
                continue
            target = nodes[next_id]
            if target.get("sender") != "player":
                continue
            assert choice.get("text") == target.get("text"), (
                f"{name}:{choice_node['id']}->{next_id} choice text differs from player node text"
            )


def test_single_reply_nodes_stay_valid():
    for name in FILES:
        data = load(name)
        nodes = {node["id"]: node for node in data["nodes"]}
        singles = [node for node in data["nodes"] if "_single_reply_" in node["id"]]
        assert singles, f"{name}: no single reply nodes"
        for node in singles:
            assert node.get("type") == "choice"
            assert len(node.get("choices", [])) == 1
            option = node["choices"][0]
            target = nodes[option["next"]]
            assert target.get("sender") == "player"
            assert option.get("text") == target.get("text")
            assert "effects" not in target
            assert "choices" not in target


if __name__ == "__main__":
    test_choice_panel_height_is_dynamic()
    test_choice_dedupe_uses_next_player_node_not_text_equality()
    test_choice_text_matches_next_player_node_text()
    test_single_reply_nodes_stay_valid()
    print("T147 choice UI and player duplicate tests OK")
