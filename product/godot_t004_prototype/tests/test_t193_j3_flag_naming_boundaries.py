#!/usr/bin/env python3
"""T193: J3 Nico/Sarah pressure flags name their source correctly."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NICO = json.loads((DATA / "nico_j3_v2_experimental.json").read_text(encoding="utf-8"))
J3_TEXT = "\n".join(path.read_text(encoding="utf-8") for path in DATA.glob("*_j3_v2_experimental.json"))
NODES = {node["id"]: node for node in NICO["nodes"]}

OLD_FLAGS = [
    "j3_nico_knows_sarah_observes",
    "j3_sarah_gestures_pressure_named",
]
NEW_FLAGS = [
    "j3_player_told_nico_sarah_observes",
    "j3_player_named_sarah_gestures_pressure",
]


def test_t193_old_ambiguous_flags_are_absent_from_j3_files() -> None:
    for flag in OLD_FLAGS:
        assert flag not in J3_TEXT


def test_t193_new_source_accurate_flags_are_present_in_nico_j3() -> None:
    serialized = json.dumps(NICO, ensure_ascii=False)
    for flag in NEW_FLAGS:
        assert flag in serialized


def test_t193_nico_j3_choice_and_player_texts_still_match() -> None:
    for node in NICO["nodes"]:
        if node.get("type") != "choice":
            continue
        for option in node.get("choices", []):
            player = NODES[option["next"]]
            assert player["sender"] == "player"
            assert player["text"] == option["text"]


def test_t193_only_sarah_observes_choice_flag_names_changed() -> None:
    central = NODES["j3_02_choice_nico_availability"]
    target = next(choice for choice in central["choices"] if choice["id"] == "j3_02_nico_sarah_observes")
    effects = target["effects"]
    assert effects["dette_nico"] == 0
    assert effects["coherence"] == 1
    assert effects["risque_exposition"] == 1
    assert effects["fatigue_emotionnelle"] == 1
    assert effects["flags"] == NEW_FLAGS


if __name__ == "__main__":
    test_t193_old_ambiguous_flags_are_absent_from_j3_files()
    test_t193_new_source_accurate_flags_are_present_in_nico_j3()
    test_t193_nico_j3_choice_and_player_texts_still_match()
    test_t193_only_sarah_observes_choice_flag_names_changed()
    print("T193 J3 flag naming boundary tests OK")
