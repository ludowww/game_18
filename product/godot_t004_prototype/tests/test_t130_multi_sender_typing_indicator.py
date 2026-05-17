from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"


def screen_text() -> str:
    return SCREEN.read_text(encoding="utf-8")


def test_t130_typing_indicator_supports_any_contact_sender_not_only_current_contact() -> None:
    source = screen_text()
    assert "var typing_sender_id: String = \"\"" in source
    assert "func _add_typing_bubble(sender: String) -> void:" in source
    assert "style.bg_color = _contact_color(sender).lightened(0.08)" in source
    assert "style.border_color = _contact_color(sender).lightened(0.32)" in source
    assert "await _add_typing_bubble(sender)" in source
    assert "typing_sender_id = sender" in source
    assert "if sender == \"player\" or sender == \"system\":" in source
    assert "if sender != current_contact_id:" not in source.split("func _show_typing_indicator", 1)[1].split("func ", 1)[0]


def test_t130_wait_before_node_shows_typing_for_non_player_non_system_senders() -> None:
    source = screen_text()
    body = source.split("func _wait_before_node(node: Dictionary) -> void:", 1)[1].split("func ", 1)[0]
    assert "if sender != \"player\" and sender != \"system\":" in body
    assert "await _show_typing_indicator(sender)" in body
    assert "await get_tree().create_timer(_display_delay_for_text" in body
    assert "else:" in body and "* 0.65" in body


if __name__ == "__main__":
    test_t130_typing_indicator_supports_any_contact_sender_not_only_current_contact()
    test_t130_wait_before_node_shows_typing_for_non_player_non_system_senders()
    print("T130 multi-sender typing indicator tests OK")
