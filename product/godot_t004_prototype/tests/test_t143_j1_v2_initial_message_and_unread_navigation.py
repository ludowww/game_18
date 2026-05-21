from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
SCREEN = ROOT / "scripts" / "conversation_screen.gd"

CORE_INITIAL_MESSAGES = {
    "sarah_j1_v2": "T’es réveillé ?",
    "camille_j1_v2": "Je crois qu’on a été moins discrets qu’on pensait.",
    "nico_j1_v2": "T’es rentré comment ?",
    "maya_j1_v2": "tu dors encore ?",
    "ines_j1_v2": "Je peux te parler ?",
}


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def body(source: str, func_name: str, next_func_name: str) -> str:
    start = source.index(f"func {func_name}")
    end = source.index(f"func {next_func_name}", start)
    return source[start:end]


def test_t143_state_exposes_initial_message_for_each_j1_v2_core_conversation() -> None:
    source = text(STATE)
    assert "func j1_v2_initial_message_for(conversation_id: String) -> String:" in source
    assert "const J1_V2_INITIAL_MESSAGES :=" in source
    for conversation_id, initial in CORE_INITIAL_MESSAGES.items():
        assert f'"{conversation_id}": "{initial}"' in source


def test_t143_conversation_screen_injects_initial_message_before_entry_variant() -> None:
    source = text(SCREEN)
    ready = body(source, "_ready", "_build_ui")
    assert "var start_node := _resolved_start_node()" in ready
    assert "await _show_j1_v2_initial_exchange_if_needed(start_node)" in ready
    assert ready.index("await _show_j1_v2_initial_exchange_if_needed(start_node)") < ready.index("_advance_to(start_node, true)")
    assert "func _show_j1_v2_initial_exchange_if_needed(start_node: String) -> void:" in source


def test_t143_initial_message_injection_has_duplicate_guards() -> None:
    source = text(SCREEN)
    injection = body(source, "_show_j1_v2_initial_exchange_if_needed", "_node_text_matches_initial_message")
    assert "ConversationState.j1_v2_initial_message_for" in injection
    assert "ConversationState.current_has_message_text(initial_message)" in injection
    assert "_node_text_matches_initial_message(start_node, initial_message)" in injection
    assert 'await _add_bubble(current_contact_id, initial_message)' in injection


def test_t143_unread_navigation_is_generic_when_multiple_unread_conversations_exist() -> None:
    state = text(STATE)
    screen = text(SCREEN)
    assert "func unread_conversation_ids_except_current() -> Array:" in state
    quick = body(state, "quick_switch_new_conversation_id", "set_current_conversation")
    assert "unread_conversation_ids_except_current()" in quick
    assert 'if unread_ids.size() == 1:' in quick
    assert 'return "__unread_messages__"' in quick
    assert 'Messages non lus...' in screen
    assert 'res://scenes/conversation_list.tscn' in screen


if __name__ == "__main__":
    test_t143_state_exposes_initial_message_for_each_j1_v2_core_conversation()
    test_t143_conversation_screen_injects_initial_message_before_entry_variant()
    test_t143_initial_message_injection_has_duplicate_guards()
    test_t143_unread_navigation_is_generic_when_multiple_unread_conversations_exist()
    print("T143 J1 V2 initial messages + unread navigation tests OK")
