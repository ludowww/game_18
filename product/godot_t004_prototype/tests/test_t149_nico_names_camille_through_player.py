#!/usr/bin/env python3
"""T149: Nico must not name Camille before the player does in after_camille_confusion."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NICO = DATA / "nico_j1_v2_experimental.json"


def load_nico():
    return json.loads(NICO.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def test_after_camille_variant_starts_with_suspicion_not_camille_name():
    data = load_nico()
    nodes = nodes_by_id(data)
    start_id = next(v["start_node"] for v in data["entry_variants"] if v["id"] == "after_camille_confusion")
    first = nodes[start_id]
    assert first["id"] == "j1_03_nico_entry_after_camille_001"
    assert first["text"] == "j’ai l’impression qu’il y a un truc que tu tournes autour sans le nommer."
    assert "Camille" not in first["text"]
    assert first["next"] == "j1_03_nico_single_reply_after_camille_001"


def test_player_names_camille_before_nico_uses_name():
    data = load_nico()
    nodes = nodes_by_id(data)
    single = nodes["j1_03_nico_single_reply_after_camille_001"]
    assert single["type"] == "choice"
    assert len(single["choices"]) == 1
    option = single["choices"][0]
    assert option["text"] == "Camille."
    player = nodes[option["next"]]
    assert player["id"] == "j1_03_nico_player_after_camille_001"
    assert player["sender"] == "player"
    assert player["text"] == "Camille."
    assert "effects" not in player
    assert "choices" not in player


def test_nico_after_player_keeps_boundary_and_reaches_existing_choice():
    data = load_nico()
    nodes = nodes_by_id(data)
    assert nodes["j1_03_nico_entry_after_camille_002"]["text"] == "ok. donc c’est pas juste une parenthèse."
    assert nodes["j1_03_nico_entry_after_camille_003"]["text"] == "je te juge pas. mais faut que tu me dises si tu veux un ami ou un alibi."
    current = "j1_03_nico_entry_after_camille_001"
    seen = set()
    while current and current not in seen:
        if current == "j1_03_choice_nico_version":
            return
        seen.add(current)
        node = nodes[current]
        current = node.get("next") or (node.get("choices", [{}])[0].get("next") if node.get("type") == "choice" else "")
    raise AssertionError("after_camille_confusion path does not reach j1_03_choice_nico_version")


if __name__ == "__main__":
    test_after_camille_variant_starts_with_suspicion_not_camille_name()
    test_player_names_camille_before_nico_uses_name()
    test_nico_after_player_keeps_boundary_and_reaches_existing_choice()
    print("T149 Nico names Camille through player tests OK")
