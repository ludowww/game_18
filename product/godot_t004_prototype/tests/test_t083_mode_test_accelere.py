from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"
LIST = ROOT / "scripts" / "conversation_list.gd"
STATE = ROOT / "scripts" / "conversation_state.gd"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_fast_test_mode_toggle_and_delays_are_code_side_only():
    screen = read(SCREEN)
    listing = read(LIST)
    state = read(STATE)

    # Normal rhythm stays unchanged.
    assert "const DEBUG_DELAY_MIN_SECONDS := 1.1" in screen
    assert "const DEBUG_DELAY_MAX_SECONDS := 6.5" in screen
    assert "const PRE_CHOICE_DELAY_SECONDS := 0.8" in screen
    assert "const NARRATION_READ_SECONDS := 1.6" in screen
    assert "const MIN_BETWEEN_MESSAGES_SECONDS := 0.6" in screen

    # Fast values are opt-in and stay in code, not in dialogue JSON.
    assert "FAST_TYPING_DELAY_MAX_SECONDS := 0.35" in screen
    assert "FAST_PRE_CHOICE_DELAY_SECONDS := 0.1" in screen
    assert "FAST_NARRATION_READ_SECONDS := 0.2" in screen
    assert "FAST_MIN_BETWEEN_MESSAGES_SECONDS := 0.1" in screen
    assert "ConversationState.test_fast_mode_enabled" in screen
    assert "_pre_choice_delay_seconds()" in screen
    assert "_narration_read_seconds()" in screen
    assert "_between_messages_delay_seconds()" in screen
    assert "_display_delay_for_text" in screen and "FAST_TYPING_DELAY_MAX_SECONDS" in screen

    # Discreet Messages-screen toggle; default OFF and reset does not toggle it.
    assert "test_fast_mode_enabled: bool = false" in state
    assert "func set_test_fast_mode_enabled(enabled: bool)" in state
    assert "Mode test rapide : ON" in listing
    assert "Mode test rapide : OFF" in listing
    assert "_make_test_fast_mode_button" in listing
    assert "_on_test_fast_mode_pressed" in listing
    assert "_make_force_day_button" in listing
    assert "force_advance_to_next_day_for_testing" in listing
    assert "func force_advance_to_next_day_for_testing() -> void:" in state
    assert "func _advance_day_unchecked() -> void:" in state
    reset_body = state.split("func reset_progression() -> void:", 1)[1].split("# Compatibilité", 1)[0]
    assert "test_fast_mode_enabled" not in reset_body

    # No save/schema migration for debug-only mode.
    save_body = state.split("func save_progression() -> void:", 1)[1].split("func load_progression()", 1)[0]
    load_body = state.split("func load_progression() -> void:", 1)[1].split("func _merge_saved_global_game_state", 1)[0]
    assert "test_fast_mode_enabled" not in save_body
    assert "test_fast_mode_enabled" not in load_body
    for mutable_field in ["available", "title", "json_path", "start_node"]:
        assert f'"{mutable_field}":' in save_body
        assert f'state["{mutable_field}"] =' in load_body


if __name__ == "__main__":
    test_fast_test_mode_toggle_and_delays_are_code_side_only()
    print("T083 fast test mode static checks OK")
