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


def test_t135_breathing_jsons_are_not_separate_message_conversations() -> None:
    source = state_text()
    default_conversations = function_body(source, "_default_conversations")
    conversation_ids = function_body(source, "conversation_ids")
    for duplicate_id in ["sarah_meal_j1_v2", "nico_respiration_j1_v2"]:
        assert f'"{duplicate_id}": _new_conversation_state' not in default_conversations
        assert f'"{duplicate_id}"' not in conversation_ids


def test_t135_breathing_scenes_attach_to_existing_sarah_and_nico_threads() -> None:
    source = state_text()
    assert "func _attach_j1_v2_followup_scene(conversation_id: String, json_path: String, start_node: String, title: String, preview: String) -> void:" in source
    unlock_body = function_body(source, "_unlock_j1_v2_breathing_scenes_if_ready")
    assert '_attach_j1_v2_followup_scene("sarah_j1_v2", "res://data/sarah_meal_j1_v2_experimental.json", "j1_06_sarah_001", "J1 V2 — Rentrer manger", "Sarah parle du repas.")' in unlock_body
    assert '_attach_j1_v2_followup_scene("nico_j1_v2", "res://data/nico_respiration_j1_v2_experimental.json", "j1_07_nico_001", "J1 V2 — Respiration", "Nico tente une respiration.")' in unlock_body
    assert 'conversations["sarah_meal_j1_v2"]' not in unlock_body
    assert 'conversations["nico_respiration_j1_v2"]' not in unlock_body


def test_t135_attach_helper_reopens_existing_thread_with_followup_json() -> None:
    source = state_text()
    helper = function_body(source, "_attach_j1_v2_followup_scene")
    for expected in [
        'state["json_path"] = json_path',
        'state["start_node"] = start_node',
        'state["title"] = title',
        'state["available"] = true',
        'state["done"] = false',
        'state["next_node"] = start_node',
        'state["active_choice_node"] = ""',
        'mark_conversation_new(conversation_id, preview)',
    ]:
        assert expected in helper


def test_t135_j1_v2_day_completion_uses_existing_threads_not_duplicate_followup_ids() -> None:
    source = state_text()
    required = function_body(source, "_required_conversations_for_current_mode")
    assert '"sarah_j1_v2"' in required
    assert '"nico_j1_v2"' in required
    assert '"sarah_meal_j1_v2"' not in required
    assert '"nico_respiration_j1_v2"' not in required


def test_t135_followup_threads_do_not_hide_j2_transition_after_core_done() -> None:
    source = state_text()
    is_day_complete = function_body(source, "_is_day_complete")
    assert "_is_required_conversation_complete(id, day)" in is_day_complete
    helper = function_body(source, "_is_required_conversation_complete")
    assert 'id == "sarah_j1_v2" and json_path.contains("sarah_meal_j1_v2")' in helper
    assert 'id == "nico_j1_v2" and json_path.contains("nico_respiration_j1_v2")' in helper
    assert "experimental_j1_v2_enabled and day == 1" in helper


if __name__ == "__main__":
    test_t135_breathing_jsons_are_not_separate_message_conversations()
    test_t135_breathing_scenes_attach_to_existing_sarah_and_nico_threads()
    test_t135_attach_helper_reopens_existing_thread_with_followup_json()
    test_t135_j1_v2_day_completion_uses_existing_threads_not_duplicate_followup_ids()
    test_t135_followup_threads_do_not_hide_j2_transition_after_core_done()
    print("T135 J1 V2 followup threading tests OK")
