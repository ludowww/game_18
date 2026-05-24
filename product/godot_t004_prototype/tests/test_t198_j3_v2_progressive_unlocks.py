#!/usr/bin/env python3
"""T198: J3 V2 progressive runtime unlocks match the complete written day."""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")

def function_body(name: str) -> str:
    marker = f"func {name}"
    assert marker in STATE, f"missing function {name}"
    return STATE.split(marker, 1)[1].split("\nfunc ", 1)[0]

def test_t198_j3_required_conversations_are_sarah_nico_camille_maya_only() -> None:
    required = function_body("_required_conversations_for_current_mode(day: int) -> Array:")
    match = re.search(r"if experimental_j1_v2_enabled and day == 3:\n\t\treturn \[(.*?)\n\t\t\]", required, re.S)
    assert match, "missing experimental J3 required branch"
    body = match.group(1)
    for cid in ["sarah_j3_v2", "nico_j3_v2", "camille_j3_v2", "maya_j3_v2"]:
        assert f'"{cid}"' in body
    assert '"ines_j3_v2"' not in body

def test_t198_j3_progression_repair_function_exists_and_is_called() -> None:
    assert "func _repair_j3_v2_progression_unlocks() -> void:" in STATE
    assert "_repair_j3_v2_progression_unlocks()" in function_body("mark_current_done() -> void:")
    assert "_repair_j3_v2_progression_unlocks()" in function_body("refresh_day_progression() -> void:")

def test_t198_camille_unlocks_after_sarah_or_nico_done() -> None:
    body = function_body("_repair_j3_v2_progression_unlocks() -> void:")
    assert 'not experimental_j1_v2_enabled or current_day != 3' in body
    assert 'conversations["sarah_j3_v2"].get("done", false)' in body
    assert 'conversations["nico_j3_v2"].get("done", false)' in body
    assert "morning_done" in body
    assert 'mark_conversation_new("camille_j3_v2", "Camille revient dans l’après-midi.")' in body

def test_t198_maya_unlocks_after_camille_done() -> None:
    body = function_body("_repair_j3_v2_progression_unlocks() -> void:")
    assert 'conversations["camille_j3_v2"].get("done", false)' in body
    assert 'mark_conversation_new("maya_j3_v2", "Maya revient sur l’ambiance.")' in body

def test_t198_ines_unlocks_after_maya_done_but_stays_optional() -> None:
    body = function_body("_repair_j3_v2_progression_unlocks() -> void:")
    assert 'conversations["maya_j3_v2"].get("done", false)' in body
    assert 'mark_conversation_new("ines_j3_v2", "Inès écrit en soirée.")' in body
    required = function_body("_required_conversations_for_current_mode(day: int) -> Array:")
    match = re.search(r"if experimental_j1_v2_enabled and day == 3:\n\t\treturn \[(.*?)\n\t\t\]", required, re.S)
    assert match
    assert '"ines_j3_v2"' not in match.group(1)

def test_t198_legacy_j3_filter_remains_active_in_experimental_mode() -> None:
    filter_body = function_body("_conversation_allowed_in_current_mode(id: String, state: Dictionary) -> bool:")
    assert "if day == 3:" in filter_body
    assert 'return bool(state.get("experimental", false))' in filter_body
    active = function_body("active_conversation_ids() -> Array:")
    assert 'id == "sarah_j3"' not in active
    assert 'id == "camille_j3"' not in active

if __name__ == "__main__":
    test_t198_j3_required_conversations_are_sarah_nico_camille_maya_only()
    test_t198_j3_progression_repair_function_exists_and_is_called()
    test_t198_camille_unlocks_after_sarah_or_nico_done()
    test_t198_maya_unlocks_after_camille_done()
    test_t198_ines_unlocks_after_maya_done_but_stays_optional()
    test_t198_legacy_j3_filter_remains_active_in_experimental_mode()
    print("T198 J3 V2 progressive unlock tests OK")
