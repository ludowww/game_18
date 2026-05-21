from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"


def source() -> str:
    return SCREEN.read_text(encoding="utf-8")


def function_body(text: str, name: str) -> str:
    start = text.index(f"func {name}")
    rest = text[start + 5:]
    next_func = rest.find("\nfunc ")
    if next_func == -1:
        return text[start:]
    return text[start:start + 5 + next_func]


def test_t139_choice_press_displays_player_choice_before_advancing_to_next_node_when_not_duplicate() -> None:
    body = function_body(source(), "_on_choice_pressed")
    assert 'var next_id := str(choice.get("next", ""))' in body
    assert 'if not _choice_text_is_repeated_by_next_player_node(choice, next_id):' in body
    assert 'await _add_bubble("player", str(choice.get("text", "")))' in body
    assert body.index('await _add_bubble("player", str(choice.get("text", "")))') < body.index('_advance_to(next_id, true)')


def test_t139_choice_press_records_choice_before_player_message_for_state_flags() -> None:
    body = function_body(source(), "_on_choice_pressed")
    assert body.index('ConversationState.record_current_choice(str(choice.get("id", "")))') < body.index('await _add_bubble("player", str(choice.get("text", "")))')
    assert body.index('_apply_effects(choice.get("effects", {}))') < body.index('await _add_bubble("player", str(choice.get("text", "")))')


if __name__ == "__main__":
    test_t139_choice_press_displays_player_choice_before_advancing_to_next_node_when_not_duplicate()
    test_t139_choice_press_records_choice_before_player_message_for_state_flags()
    print("T139 choice response before system end tests OK")
