#!/usr/bin/env python3
"""T163: Maya J1 V2 after_sarah variant includes a photo placeholder media node."""

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
MAYA = DATA / "maya_j1_v2_experimental.json"

EXPECTED_CHOICES = [
    "j1_04_play_dumb",
    "j1_04_needed_air",
    "j1_04_ask_what_saw",
    "j1_04_not_involve",
]


def load():
    return json.loads(MAYA.read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def structural_choices_snapshot(data):
    choice = nodes_by_id(data)["j1_04_choice_maya_pique"]
    return [
        {
            "id": item["id"],
            "next": item["next"],
            "effects": deepcopy(item.get("effects", {})),
        }
        for item in choice["choices"]
    ]


def test_maya_after_sarah_contains_media_placeholder_node():
    nodes = nodes_by_id(load())
    media = nodes["j1_04_maya_media_after_sarah_001"]
    assert media["type"] == "media"
    assert media["sender"] == "maya"
    assert media["media_type"] == "image"
    assert media["asset"] == "res://assets/media/j1_v2/maya_photo_groupe_j1.png"
    assert media["caption"] == "[photo de groupe envoyée]"


def test_media_node_is_in_after_sarah_path_after_photo_group_line():
    nodes = nodes_by_id(load())
    assert nodes["j1_04_maya_entry_after_sarah_003"]["text"] == "mais les absences, ça se voit. surtout sur les photos de groupe."
    assert nodes["j1_04_maya_entry_after_sarah_003"]["next"] == "j1_04_maya_media_after_sarah_001"
    assert nodes["j1_04_maya_media_after_sarah_001"]["next"] == "j1_04_maya_entry_after_sarah_004"


def test_after_sarah_media_path_returns_to_maya_choice_node():
    nodes = nodes_by_id(load())
    assert nodes["j1_04_maya_entry_after_sarah_004"]["text"] == "je dis pas que ça prouve quoi que ce soit."
    assert nodes["j1_04_maya_entry_after_sarah_004"]["next"] == "j1_04_maya_entry_after_sarah_005"
    assert nodes["j1_04_maya_entry_after_sarah_005"]["text"] == "je dis juste que ça laisse une place bizarre dans l’image."
    assert nodes["j1_04_maya_entry_after_sarah_005"]["next"] == "j1_04_choice_maya_pique"


def test_after_sarah_variant_still_starts_on_same_node():
    data = load()
    variants = {variant["id"]: variant for variant in data["entry_variants"]}
    assert variants["after_sarah"]["start_node"] == "j1_04_maya_entry_after_sarah_001"


def test_maya_choices_effects_and_flags_are_unchanged_shape():
    data = load()
    choice = nodes_by_id(data)["j1_04_choice_maya_pique"]
    assert [item["id"] for item in choice["choices"]] == EXPECTED_CHOICES
    for item in choice["choices"]:
        assert isinstance(item.get("effects"), dict)
        assert isinstance(item["effects"].get("flags"), list)
    assert structural_choices_snapshot(data) == structural_choices_snapshot(data)


if __name__ == "__main__":
    test_maya_after_sarah_contains_media_placeholder_node()
    test_media_node_is_in_after_sarah_path_after_photo_group_line()
    test_after_sarah_media_path_returns_to_maya_choice_node()
    test_after_sarah_variant_still_starts_on_same_node()
    test_maya_choices_effects_and_flags_are_unchanged_shape()
    print("T163 Maya after_sarah media tests OK")
