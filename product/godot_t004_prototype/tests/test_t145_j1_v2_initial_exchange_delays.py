from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"


def source() -> str:
    return SCREEN.read_text(encoding="utf-8")


def body(text: str, func_name: str, next_func_name: str) -> str:
    start = text.index(f"func {func_name}")
    end = text.index(f"func {next_func_name}", start)
    return text[start:end]


def test_t145_initial_exchange_waits_between_contact_message_and_player_reply() -> None:
    exchange = body(source(), "_show_j1_v2_initial_exchange_if_needed", "_node_text_matches_initial_message")
    contact = 'await _add_bubble(current_contact_id, initial_message)'
    delay = 'await get_tree().create_timer(_between_messages_delay_seconds()).timeout'
    reply = 'await _add_bubble("player", player_reply)'
    assert contact in exchange
    assert delay in exchange
    assert reply in exchange
    assert exchange.index(contact) < exchange.index(delay) < exchange.index(reply)


def test_t145_initial_exchange_waits_before_resolved_entry_variant() -> None:
    ready = body(source(), "_ready", "_build_ui")
    assert "await _show_j1_v2_initial_exchange_if_needed(start_node)" in ready
    assert "await get_tree().create_timer(_between_messages_delay_seconds()).timeout" in ready
    assert "_advance_to(start_node)" in ready
    assert "_advance_to(start_node, true)" not in ready
    assert ready.index("await _show_j1_v2_initial_exchange_if_needed(start_node)") < ready.index("await get_tree().create_timer(_between_messages_delay_seconds()).timeout") < ready.index("_advance_to(start_node)")


def test_t145_initial_exchange_still_uses_fast_mode_aware_delay_helper() -> None:
    text = source()
    assert "func _between_messages_delay_seconds() -> float:" in text
    helper = body(text, "_between_messages_delay_seconds", "_ensure_last_message_visible")
    assert "ConversationState.test_fast_mode_enabled" in helper
    assert "FAST_MIN_BETWEEN_MESSAGES_SECONDS" in helper
    assert "MIN_BETWEEN_MESSAGES_SECONDS" in helper


if __name__ == "__main__":
    test_t145_initial_exchange_waits_between_contact_message_and_player_reply()
    test_t145_initial_exchange_waits_before_resolved_entry_variant()
    test_t145_initial_exchange_still_uses_fast_mode_aware_delay_helper()
    print("T145 J1 V2 initial exchange delays tests OK")
