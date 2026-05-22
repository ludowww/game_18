#!/usr/bin/env python3
"""T154: Nico respiration choices should follow naturally from the pizza/pause beat."""

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FILE = DATA / "nico_respiration_j1_v2_experimental.json"


def load():
    return json.loads(FILE.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def choice_by_id(choice_node, choice_id):
    for choice in choice_node["choices"]:
        if choice["id"] == choice_id:
            return choice
    raise AssertionError(f"missing choice {choice_id}")


def structural_snapshot(data):
    """Keep only structure/mechanics fields that T154 must not alter."""
    snapshot = []
    for node in data["nodes"]:
        node_copy = deepcopy(node)
        node_copy.pop("text", None)
        for choice in node_copy.get("choices", []):
            choice.pop("text", None)
        snapshot.append(node_copy)
    return snapshot


BEFORE_STRUCTURE = structural_snapshot(load())


def test_nico_pause_line_keeps_food_joke_and_opens_the_rest():
    nodes = nodes_by_id(load())
    text = nodes["j1_07_nico_004"]["text"]
    assert "pizza" in text
    assert "stress" in text
    assert "café froid" in text
    assert "parler du reste" in text


def test_real_advice_choice_starts_from_pizza_or_pause():
    choice_node = nodes_by_id(load())["j1_07_choice_nico_respiration"]
    text = choice_by_id(choice_node, "j1_07_ask_real_advice")["text"]
    assert text.startswith(("Pizza", "Pause", "Après", "Avant"))
    assert "sans vanne" in text


def test_second_cover_choice_no_longer_starts_with_sarah_or_maya():
    choice_node = nodes_by_id(load())["j1_07_choice_nico_respiration"]
    text = choice_by_id(choice_node, "j1_07_second_cover")["text"]
    assert not text.startswith("Si Sarah ou Maya")
    assert "rester vague" in text


def test_choice_ids_effects_and_flags_remain_present():
    choice_node = nodes_by_id(load())["j1_07_choice_nico_respiration"]
    expected_ids = [
        "j1_07_share_joke",
        "j1_07_ask_real_advice",
        "j1_07_second_cover",
        "j1_07_joke_avoid",
    ]
    assert [choice["id"] for choice in choice_node["choices"]] == expected_ids
    for choice in choice_node["choices"]:
        effects = choice.get("effects")
        assert isinstance(effects, dict), choice["id"]
        assert isinstance(effects.get("flags"), list), choice["id"]


def test_only_text_fields_changed_from_t154_baseline():
    assert structural_snapshot(load()) == BEFORE_STRUCTURE


if __name__ == "__main__":
    test_nico_pause_line_keeps_food_joke_and_opens_the_rest()
    test_real_advice_choice_starts_from_pizza_or_pause()
    test_second_cover_choice_no_longer_starts_with_sarah_or_maya()
    test_choice_ids_effects_and_flags_remain_present()
    test_only_text_fields_changed_from_t154_baseline()
    print("T154 Nico respiration pause-choice alignment tests OK")
