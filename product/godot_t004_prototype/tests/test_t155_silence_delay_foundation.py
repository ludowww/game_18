#!/usr/bin/env python3
"""T155: foundation for silence / delayed reply state in J1 V2."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
STATE = (SCRIPTS / "conversation_state.gd").read_text(encoding="utf-8")
SCREEN = (SCRIPTS / "conversation_screen.gd").read_text(encoding="utf-8")


def test_state_distinguishes_single_reply_from_narrative_multiple_choice():
    assert "func is_single_reply_choice_node" in STATE
    assert "_single_reply_" in STATE
    assert "func is_narrative_multiple_choice_pending" in STATE
    assert "pending_choice_option_count" in STATE


def test_screen_records_pending_choice_metadata_when_showing_choice():
    assert "ConversationState.set_current_active_choice(node_id, node.get(\"choices\", []).size())" in SCREEN
    assert "func set_current_active_choice(node_id: String, option_count: int = 0)" in STATE


def test_leaving_single_reply_does_not_set_silence_flag():
    assert "func mark_current_left_open_if_pending_choice" in STATE
    function_body = STATE[STATE.index("func mark_current_left_open_if_pending_choice"):]
    function_body = function_body.split("\nfunc ", 1)[0]
    assert "is_single_reply_choice_node" in function_body
    assert "return false" in function_body


def test_leaving_multiple_choice_marks_conversation_left_open_once():
    assert "left_open" in STATE
    assert "left_open_choice_node" in STATE
    assert "left_open_count" in STATE
    assert "if bool(state.get(\"left_open\", false))" in STATE
    assert "return false" in STATE


def test_completed_conversations_are_not_marked_left_open():
    function_body = STATE[STATE.index("func mark_current_left_open_if_pending_choice"):]
    function_body = function_body.split("\nfunc ", 1)[0]
    assert "done" in function_body
    assert "return false" in function_body


def test_back_to_messages_invokes_left_open_preparation():
    assert "ConversationState.mark_current_left_open_if_pending_choice()" in SCREEN
    assert "change_scene_to_file(\"res://scenes/conversation_list.tscn\")" in SCREEN


def test_left_open_state_is_saved_and_loaded():
    for key in [
        "left_open",
        "left_open_choice_node",
        "left_open_count",
        "left_open_flag",
        "late_reply_prepared",
    ]:
        assert f'\"{key}\"' in STATE


def test_silence_and_delay_flags_are_prepared_for_known_contexts():
    for flag in [
        "left_sarah_on_read_j1",
        "left_camille_on_read_j1",
        "ignored_nico_respiration_j1",
        "late_reply_sarah_meal_j1",
    ]:
        assert flag in STATE
    assert "not global_game_state[\"flags\"].has(silence_flag)" in STATE


if __name__ == "__main__":
    test_state_distinguishes_single_reply_from_narrative_multiple_choice()
    test_screen_records_pending_choice_metadata_when_showing_choice()
    test_leaving_single_reply_does_not_set_silence_flag()
    test_leaving_multiple_choice_marks_conversation_left_open_once()
    test_completed_conversations_are_not_marked_left_open()
    test_back_to_messages_invokes_left_open_preparation()
    test_left_open_state_is_saved_and_loaded()
    test_silence_and_delay_flags_are_prepared_for_known_contexts()
    print("T155 silence/delay foundation tests OK")
