from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
SCREEN = ROOT / "scripts" / "conversation_screen.gd"

INITIAL_PLAYER_REPLIES = {
    "sarah_j1_v2": "Oui. Je viens de voir ton message.",
    "camille_j1_v2": "Tu crois ?",
    "nico_j1_v2": "À pied. Pourquoi ?",
    "maya_j1_v2": "non. pourquoi ?",
    "ines_j1_v2": "Oui, dis-moi.",
}


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def body(source: str, func_name: str, next_func_name: str) -> str:
    start = source.index(f"func {func_name}")
    end = source.index(f"func {next_func_name}", start)
    return source[start:end]


def test_t144_state_exposes_initial_player_replies_for_five_core_conversations() -> None:
    source = text(STATE)
    assert "const J1_V2_INITIAL_PLAYER_REPLIES :=" in source
    assert "func j1_v2_initial_player_reply_for(conversation_id: String) -> String:" in source
    for conversation_id, reply in INITIAL_PLAYER_REPLIES.items():
        assert f'"{conversation_id}": "{reply}"' in source


def test_t144_screen_injects_initial_exchange_before_entry_variant_start_node() -> None:
    source = text(SCREEN)
    ready = body(source, "_ready", "_build_ui")
    assert "var start_node := _resolved_start_node()" in ready
    assert "await _show_j1_v2_initial_exchange_if_needed(start_node)" in ready
    assert "_show_j1_v2_initial_message_if_needed" not in ready
    assert ready.index("await _show_j1_v2_initial_exchange_if_needed(start_node)") < ready.index("_advance_to(start_node, true)")


def test_t144_initial_exchange_order_is_contact_message_then_player_reply() -> None:
    source = text(SCREEN)
    exchange = body(source, "_show_j1_v2_initial_exchange_if_needed", "_node_text_matches_initial_message")
    assert "ConversationState.j1_v2_initial_message_for" in exchange
    assert "ConversationState.j1_v2_initial_player_reply_for" in exchange
    assert 'await _add_bubble(current_contact_id, initial_message)' in exchange
    assert 'await _add_bubble("player", player_reply)' in exchange
    assert exchange.index('await _add_bubble(current_contact_id, initial_message)') < exchange.index('await _add_bubble("player", player_reply)')


def test_t144_initial_exchange_has_duplicate_guards_for_message_and_reply() -> None:
    source = text(SCREEN)
    exchange = body(source, "_show_j1_v2_initial_exchange_if_needed", "_node_text_matches_initial_message")
    assert "ConversationState.current_has_message_text(initial_message)" in exchange
    assert "ConversationState.current_has_message_text(player_reply)" in exchange
    assert "_node_text_matches_initial_message(start_node, initial_message)" in exchange


def test_t144_unread_navigation_still_routes_multiple_unread_to_messages() -> None:
    source = text(SCREEN)
    assert 'Messages non lus...' in source
    assert 'res://scenes/conversation_list.tscn' in source
    assert 'target_id == "__unread_messages__"' in source


if __name__ == "__main__":
    test_t144_state_exposes_initial_player_replies_for_five_core_conversations()
    test_t144_screen_injects_initial_exchange_before_entry_variant_start_node()
    test_t144_initial_exchange_order_is_contact_message_then_player_reply()
    test_t144_initial_exchange_has_duplicate_guards_for_message_and_reply()
    test_t144_unread_navigation_still_routes_multiple_unread_to_messages()
    print("T144 J1 V2 initial player replies tests OK")
