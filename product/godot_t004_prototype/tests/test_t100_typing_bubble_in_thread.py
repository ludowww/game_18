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


def test_t100_typing_indicator_is_temporary_bubble_inside_message_thread() -> None:
    source = read_screen()
    assert "var typing_row: HBoxContainer" in source
    assert "var typing_bubble: PanelContainer" in source
    assert "func _add_typing_bubble" in source
    assert "func _remove_typing_bubble" in source
    assert "message_list.add_child(typing_row)" in source
    assert "typing_row.queue_free()" in source
    assert "root.add_child(typing_container)" not in source
    assert "func _build_typing_indicator" not in source


def test_t100_typing_bubble_looks_like_contact_bubble_and_animates_points() -> None:
    source = read_screen()
    assert "style.bg_color = _contact_color(sender)" in source or "style.bg_color = _contact_color(sender).lightened" in source
    assert "style.corner_radius_bottom_left = 5" in source
    assert "row.add_child(bubble)" in source
    assert "row.add_child(right_spacer)" in source
    assert "_typing_indicator_text" in source
    assert '"..."' in source or '".".repeat(typing_dot_count)' in source
    assert "await get_tree().create_timer(0.32).timeout" in source
    assert "typing_label.modulate.a" in source
    assert "_ensure_last_message_visible()" in source


def test_t100_typing_bubble_is_removed_before_real_message_arrives() -> None:
    source = read_screen()
    wait_section = source.split("func _wait_before_node", 1)[1].split("func _show_choice", 1)[0]
    assert "_show_typing_indicator(sender)" in wait_section
    assert "_hide_typing_indicator()" in wait_section
    assert wait_section.index("_show_typing_indicator(sender)") < wait_section.index("_hide_typing_indicator()")
    add_bubble_section = source.split("func _add_bubble", 1)[1].split("func _add_system_note", 1)[0]
    assert "message_list.add_child(row)" in add_bubble_section


def test_t100_dialogue_json_and_conversation_blocks_are_unchanged() -> None:
    for filename, expected_hash in EXPECTED_UNCHANGED_HASHES.items():
        path = DATA / filename
        assert path.exists(), filename
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, filename


if __name__ == "__main__":
    test_t100_typing_indicator_is_temporary_bubble_inside_message_thread()
    test_t100_typing_bubble_looks_like_contact_bubble_and_animates_points()
    test_t100_typing_bubble_is_removed_before_real_message_arrives()
    test_t100_dialogue_json_and_conversation_blocks_are_unchanged()
    print("T100 typing bubble in thread tests OK")
