#!/usr/bin/env python3
"""T185: J2 V2 progressive runtime unlocks are complete."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")


def function_body(name: str) -> str:
    marker = f"func {name}"
    assert marker in STATE, f"missing function {name}"
    return STATE.split(marker, 1)[1].split("\nfunc ", 1)[0]


def test_t185_j2_progression_repair_function_exists_and_is_called() -> None:
    assert "func _repair_j2_v2_progression_unlocks() -> void:" in STATE
    mark_done = function_body("mark_current_done() -> void:")
    refresh = function_body("refresh_day_progression() -> void:")
    legacy = function_body("_unlock_j2_v2_after_morning_if_ready() -> void:")
    assert "_repair_j2_v2_progression_unlocks()" in mark_done
    assert "_repair_j2_v2_progression_unlocks()" in refresh
    assert "_repair_j2_v2_progression_unlocks()" in legacy


def test_t185_camille_unlocks_after_sarah_or_nico_done() -> None:
    body = function_body("_repair_j2_v2_progression_unlocks() -> void:")
    assert 'not experimental_j1_v2_enabled or current_day != 2' in body
    assert 'conversations["sarah_j2_v2"].get("done", false)' in body
    assert 'conversations["nico_j2_v2"].get("done", false)' in body
    assert "morning_done" in body
    assert 'mark_conversation_new("camille_j2_v2", "Camille reprend le fil.")' in body


def test_t185_maya_unlocks_after_camille_done() -> None:
    body = function_body("_repair_j2_v2_progression_unlocks() -> void:")
    assert 'conversations["camille_j2_v2"].get("done", false)' in body
    assert 'mark_conversation_new("maya_j2_v2", "Maya revient sur la photo.")' in body


def test_t185_ines_unlocks_after_maya_done_but_stays_optional() -> None:
    body = function_body("_repair_j2_v2_progression_unlocks() -> void:")
    assert 'conversations["maya_j2_v2"].get("done", false)' in body
    assert 'mark_conversation_new("ines_j2_v2", "Inès écrit plus tard.")' in body

    required = function_body("_required_conversations_for_current_mode(day: int) -> Array:")
    match = re.search(r"if experimental_j1_v2_enabled and day == 2:\n\t\treturn \[(.*?)\n\t\t\]", required, re.S)
    assert match, "missing experimental J2 required branch"
    body_required = match.group(1)
    for conversation_id in ["sarah_j2_v2", "nico_j2_v2", "camille_j2_v2", "maya_j2_v2"]:
        assert f'"{conversation_id}"' in body_required
    assert '"ines_j2_v2"' not in body_required


def test_t185_legacy_j2_does_not_return_to_experimental_visible_flow() -> None:
    filter_body = function_body("_conversation_allowed_in_current_mode(id: String, state: Dictionary) -> bool:")
    assert "if day == 2:" in filter_body
    assert 'return bool(state.get("experimental", false))' in filter_body
    active = function_body("active_conversation_ids() -> Array:")
    assert "_conversation_allowed_in_current_mode(id, state)" in active
    assert 'id == "camille_j2"' not in active
    assert 'id == "sarah_j2"' not in active


if __name__ == "__main__":
    test_t185_j2_progression_repair_function_exists_and_is_called()
    test_t185_camille_unlocks_after_sarah_or_nico_done()
    test_t185_maya_unlocks_after_camille_done()
    test_t185_ines_unlocks_after_maya_done_but_stays_optional()
    test_t185_legacy_j2_does_not_return_to_experimental_visible_flow()
    print("T185 J2 V2 progressive unlock tests OK")
