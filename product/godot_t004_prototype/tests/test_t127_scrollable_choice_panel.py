from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"


def screen_text() -> str:
    return SCREEN.read_text(encoding="utf-8")


def test_t127_choice_panel_uses_scroll_container_with_capped_height() -> None:
    source = screen_text()
    assert "var choice_scroll: ScrollContainer" in source
    assert "const CHOICE_PANEL_MAX_HEIGHT := 260.0" in source
    assert "choice_scroll = ScrollContainer.new()" in source
    assert "choice_scroll.custom_minimum_size = Vector2(0, CHOICE_PANEL_MAX_HEIGHT)" in source
    assert "choice_scroll.size_flags_vertical = Control.SIZE_SHRINK_END" in source
    assert "choice_scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED" in source
    assert "choice_scroll.vertical_scroll_mode = ScrollContainer.SCROLL_MODE_AUTO" in source
    assert "choice_panel.add_child(choice_scroll)" in source
    assert "choice_scroll.add_child(choice_box)" in source
    assert "choice_panel.add_child(choice_box)" not in source


def test_t127_choice_buttons_stay_inside_scrollable_reply_area() -> None:
    source = screen_text()
    assert "choice_box.size_flags_horizontal = Control.SIZE_EXPAND_FILL" in source
    assert "choice_box.size_flags_vertical = Control.SIZE_SHRINK_BEGIN" in source
    assert "await get_tree().process_frame\n\tchoice_scroll.scroll_vertical = 0" in source


if __name__ == "__main__":
    test_t127_choice_panel_uses_scroll_container_with_capped_height()
    test_t127_choice_buttons_stay_inside_scrollable_reply_area()
    print("T127 scrollable choice panel tests OK")
