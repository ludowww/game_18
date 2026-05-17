from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"
DATA = ROOT / "data"

EXPECTED_UNCHANGED_HASHES = {
    "conversation_blocks.json": "5bee89f1e5d8422a8d368f2afda4071b3a05aea6011e60708dcd1a34c7d6f6b0",
    "camille_j1_complete.json": "365ee9d64240da7101452ff64ddb189b7aada92ede25e147b5cdb45a6507b980",
    "sarah_j1_complete.json": "4c197ef3bd59784f1559ad3a33184d912331a0a41fe80974e3c405e7ac10336a",
    "camille_j2_complete.json": "a0ff3e17c38ed542cb558fdf505d587251cbe9632736c2f3ab2eed1557000fef",
    "sarah_j2_complete.json": "2740b0d0c5cdd042eff874a8a6414bfb1575c9668ab6763626603b582c14e357",
    "camille_j3_complete.json": "3ed12d5e7af784c5c82a16dbc1ea0a8096867f164d2ac32ae7c76aa126f10bd2",
    "sarah_j3_complete.json": "6c0992a9ac099bde19f7d56c94bd354f5338978b49bae53306e35e0c2a891a6b",
    "camille_j4_complete.json": "d013fc4d361e22abf5317022b0dfdda8dcf76764eda8227d0a42a5d97277ccb9",
    "maya_j4_complete.json": "2c9ca743f608a2a0106cd216995b84766d737edaa50b3ecc253412f298848458",
    "ines_j4_complete.json": "8bde309a9fca94bb7469e4e28cd1d668803011bc8e2ce4726f71152d4e40737e",
    "nico_j4_complete.json": "efeacf9cf4b8c11c3fe4bcc75e1e5b899f15e4b18a22f24e69e4d1227205d8ad",
}


def read_screen() -> str:
    return SCREEN.read_text(encoding="utf-8")


def section(source: str, start: str, end: str) -> str:
    return source.split(start, 1)[1].split(end, 1)[0]


def test_t101_typing_bubble_is_inside_scrollable_message_list() -> None:
    source = read_screen()
    add_section = section(source, "func _add_typing_bubble", "func _remove_typing_bubble")
    assert "message_list.add_child(typing_row)" in add_section
    assert "root.add_child(typing" not in source
    assert "typing_container" not in source
    assert "func _build_typing_indicator" not in source


def test_t101_typing_bubble_scrolls_after_layout_frame() -> None:
    source = read_screen()
    add_section = section(source, "func _add_typing_bubble", "func _remove_typing_bubble")
    assert "message_list.add_child(typing_row)" in add_section
    assert "await get_tree().process_frame" in add_section
    assert "_ensure_last_message_visible()" in add_section
    assert add_section.index("message_list.add_child(typing_row)") < add_section.index("await get_tree().process_frame") < add_section.index("_ensure_last_message_visible()")
    wait_section = section(source, "func _wait_before_node", "func _show_choice")
    assert "await _show_typing_indicator(sender)" in wait_section


def test_t101_typing_bubble_is_removed_before_real_message() -> None:
    source = read_screen()
    wait_section = section(source, "func _wait_before_node", "func _show_choice")
    assert "await _show_typing_indicator(sender)" in wait_section
    assert "_hide_typing_indicator()" in wait_section
    assert wait_section.index("await _show_typing_indicator(sender)") < wait_section.index("_hide_typing_indicator()")
    remove_section = section(source, "func _remove_typing_bubble", "func _show_typing_indicator")
    assert "message_list.remove_child(typing_row)" in remove_section
    assert "typing_row.queue_free()" in remove_section


def test_t101_friendly_visual_tuning_is_larger_and_readable() -> None:
    source = read_screen()
    add_section = section(source, "func _add_typing_bubble", "func _remove_typing_bubble")
    assert "typing_bubble.custom_minimum_size = Vector2(96, 44)" in add_section
    assert "style.border_color = _contact_color(sender).lightened(0.32)" in add_section
    assert "style.set_border_width_all(1)" in add_section
    assert "typing_label.add_theme_font_size_override(\"font_size\", 24)" in add_section
    assert "typing_label.vertical_alignment = VERTICAL_ALIGNMENT_CENTER" in add_section
    assert "typing_label.add_theme_color_override(\"font_color\", Color(\"f7f7fb\"))" in add_section


def test_t101_json_blocks_and_save_contract_are_unchanged() -> None:
    source = read_screen()
    assert "SAVE_PATH" not in source
    for filename, expected_hash in EXPECTED_UNCHANGED_HASHES.items():
        path = DATA / filename
        assert path.exists(), filename
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, filename


if __name__ == "__main__":
    test_t101_typing_bubble_is_inside_scrollable_message_list()
    test_t101_typing_bubble_scrolls_after_layout_frame()
    test_t101_typing_bubble_is_removed_before_real_message()
    test_t101_friendly_visual_tuning_is_larger_and_readable()
    test_t101_json_blocks_and_save_contract_are_unchanged()
    print("T101 typing bubble scroll/friendly tests OK")
