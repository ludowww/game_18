from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"


def state_text() -> str:
    return STATE.read_text(encoding="utf-8")


def function_body(source: str, name: str) -> str:
    start = source.index(f"func {name}")
    rest = source[start + 5:]
    next_func = rest.find("\nfunc ")
    if next_func == -1:
        return source[start:]
    return source[start:start + 5 + next_func]


def test_t134_reset_progression_resets_global_v2_state() -> None:
    source = state_text()
    body = function_body(source, "reset_progression")
    assert "global_game_state = _default_global_game_state()" in body
    assert body.index("dynamic_notifications_fired = []") < body.index("global_game_state = _default_global_game_state()")
    assert body.index("global_game_state = _default_global_game_state()") < body.index("conversations = _default_conversations()")


def test_t134_day_completion_uses_mode_specific_required_conversations() -> None:
    source = state_text()
    assert "func _required_conversations_for_current_mode(day: int) -> Array:" in source
    helper = function_body(source, "_required_conversations_for_current_mode")
    assert "if experimental_j1_v2_enabled and day == 1:" in helper
    assert "if _has_j1_v2_progression() and day == 1:" in helper
    for conversation_id in [
        "j1_00_reveil_v2",
        "sarah_j1_v2",
        "camille_j1_v2",
        "nico_j1_v2",
        "maya_j1_v2",
        "ines_j1_v2",
    ]:
        assert f'"{conversation_id}"' in helper
    assert '"sarah_meal_j1_v2"' not in helper
    assert '"nico_respiration_j1_v2"' not in helper
    is_day_complete = function_body(source, "_is_day_complete")
    assert "var required_ids: Array = _required_conversations_for_current_mode(day)" in is_day_complete
    assert "REQUIRED_CONVERSATIONS_BY_DAY[day]" not in is_day_complete
    refresh = function_body(source, "refresh_day_progression")
    assert "_required_conversations_for_current_mode(current_day).is_empty()" in refresh


def test_t134_breathing_scenes_unlock_only_after_core_j1_v2_done() -> None:
    source = state_text()
    priority_unlock = function_body(source, "_unlock_j1_v2_after_priority_choice")
    assert 'conversations["sarah_meal_j1_v2"]["available"] = true' not in priority_unlock
    assert 'conversations["nico_respiration_j1_v2"]["available"] = true' not in priority_unlock

    assert "func _unlock_j1_v2_breathing_scenes_if_ready() -> void:" in source
    breathing_unlock = function_body(source, "_unlock_j1_v2_breathing_scenes_if_ready")
    assert "if not _j1_v2_core_conversations_done():" in breathing_unlock
    assert '_attach_j1_v2_followup_scene("sarah_j1_v2", "res://data/sarah_meal_j1_v2_experimental.json", "j1_06_sarah_001", "J1 V2 — Rentrer manger", "Sarah parle du repas.")' in breathing_unlock
    assert '_attach_j1_v2_followup_scene("nico_j1_v2", "res://data/nico_respiration_j1_v2_experimental.json", "j1_07_nico_001", "J1 V2 — Respiration", "Nico tente une respiration.")' in breathing_unlock
    assert 'conversations["sarah_meal_j1_v2"]' not in breathing_unlock
    assert 'conversations["nico_respiration_j1_v2"]' not in breathing_unlock
    for conversation_id in ["sarah_j1_v2", "camille_j1_v2", "nico_j1_v2", "maya_j1_v2", "ines_j1_v2"]:
        assert f'"{conversation_id}"' in function_body(source, "_j1_v2_core_conversations_done")

    mark_done = function_body(source, "mark_current_done")
    assert "_unlock_j1_v2_breathing_scenes_if_ready()" in mark_done


if __name__ == "__main__":
    test_t134_reset_progression_resets_global_v2_state()
    test_t134_day_completion_uses_mode_specific_required_conversations()
    test_t134_breathing_scenes_unlock_only_after_core_j1_v2_done()
    print("T134 J1 V2 state guard tests OK")
