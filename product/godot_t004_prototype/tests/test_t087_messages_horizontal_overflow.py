from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIST = ROOT / "scripts" / "conversation_list.gd"
DATA_DIR = ROOT / "data"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_messages_screen_constrains_width_and_moves_debug_controls_off_subtitle_line():
    listing = read(LIST)

    # Header: subtitle should keep the full width; debug/test controls live on a compact second line.
    assert "func _make_header_debug_controls() -> HBoxContainer:" in listing
    assert "header_stack := VBoxContainer.new()" in listing
    assert "subtitle_row.add_child(_make_header_debug_controls())" not in listing
    debug_body = listing.split("func _make_header_debug_controls() -> HBoxContainer:", 1)[1].split("func _make_day_transition_button", 1)[0]
    assert "debug_row.alignment = BoxContainer.ALIGNMENT_END" in debug_body
    assert 'button.text = "Mode test rapide : ON"' in listing
    assert 'button.text = "Mode test rapide : OFF"' in listing
    assert "button.custom_minimum_size = Vector2(0, 28)" in debug_body

    # Messages cards: no fixed horizontal minimum, no horizontal scroll, children shrink to available width.
    assert "scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED" in listing
    assert "list.custom_minimum_size = Vector2(0, 0)" in listing
    assert "button.custom_minimum_size = Vector2(0, 140)" in listing
    entry_body = listing.split("func _make_conversation_entry", 1)[1].split("func _make_new_badge", 1)[0]
    assert "row.size_flags_horizontal = Control.SIZE_EXPAND_FILL" in entry_body
    assert "row.custom_minimum_size = Vector2(0, 0)" in entry_body
    assert "text_box.custom_minimum_size = Vector2(0, 0)" in entry_body
    assert "line.size_flags_horizontal = Control.SIZE_EXPAND_FILL" in entry_body
    assert "TextServer.OVERRUN_TRIM_ELLIPSIS" in entry_body
    assert "preview.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART" in entry_body

    # T087 is UI-only: dialogue JSON / block config stay out of the fix.
    assert (DATA_DIR / "conversation_blocks.json").exists()


if __name__ == "__main__":
    test_messages_screen_constrains_width_and_moves_debug_controls_off_subtitle_line()
    print("T087 messages horizontal overflow static checks OK")
