from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"
STATE = ROOT / "scripts" / "conversation_state.gd"
DATA = ROOT / "data"
PROFILE = ROOT.parents[1]
T003_SCHEMA = PROFILE / "product" / "t003_mini_schema_json_godot.md"

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
EXPECTED_T003_HASH = "a29efe00e4ef1d7d96245296bb83ab2a410386f711b273f64ddcce8757b78f19"


def read_screen() -> str:
    return SCREEN.read_text(encoding="utf-8")


def section(source: str, start: str, end: str) -> str:
    return source.split(start, 1)[1].split(end, 1)[0]


def test_t103_quick_switch_toast_has_refresh_helper_not_ready_only() -> None:
    source = read_screen()
    assert "func _refresh_quick_switch_notification" in source
    build_section = section(source, "func _build_ui", "func _make_header")
    ready_section = section(source, "func _ready", "func _build_ui")
    assert "_refresh_quick_switch_notification()" in build_section
    assert "root.add_child(_make_quick_switch_notification" not in source
    assert ready_section.count("quick_switch_new_conversation_id") == 0


def test_t103_refresh_helper_updates_existing_toast_in_place() -> None:
    source = read_screen()
    refresh = section(source, "func _refresh_quick_switch_notification", "func _make_quick_switch_notification")
    assert "ConversationState.quick_switch_new_conversation_id()" in refresh
    assert "quick_switch_button" in source
    assert "remove_child(quick_switch_button)" in refresh
    assert "quick_switch_button.queue_free()" in refresh
    assert "root_container.add_child(quick_switch_button)" in refresh
    assert "root_container.move_child(quick_switch_button, 1)" in refresh


def test_t103_refresh_is_called_after_notification_creating_progression_paths() -> None:
    source = read_screen()
    advance = section(source, "func _advance_to", "func _wait_before_node")
    assert "ConversationState.handle_dynamic_notification(current_contact_id, node_id)" in advance
    dynamic_index = advance.index("ConversationState.handle_dynamic_notification(current_contact_id, node_id)")
    assert "_refresh_quick_switch_notification()" in advance[dynamic_index:]
    assert "ConversationState.complete_current_block(next_id)" in advance
    block_index = advance.index("ConversationState.complete_current_block(next_id)")
    refresh_after_block = advance.index("_refresh_quick_switch_notification()", block_index)
    waiting_index = advance.index("_show_waiting_state()", block_index)
    assert block_index < refresh_after_block < waiting_index
    assert "ConversationState.complete_current_block(\"\")" in advance
    end_block_index = advance.index("ConversationState.complete_current_block(\"\")")
    assert "_refresh_quick_switch_notification()" in advance[end_block_index:]


def test_t103_keeps_t102_open_action_and_current_day_filter() -> None:
    screen = read_screen()
    state = STATE.read_text(encoding="utf-8")
    action = section(screen, "func _open_quick_switch_conversation", "func _load_conversation")
    assert "ConversationState.set_current_conversation(target_id)" in action
    assert "ConversationState.mark_conversation_read(target_id)" in action
    assert "change_scene_to_file(\"res://scenes/conversation_screen.tscn\")" in action
    helper = section(state, "func quick_switch_new_conversation_id", "func set_current_conversation")
    assert "active_conversation_ids()" in helper
    assert "archived_conversation_ids()" not in helper
    assert "id == current_conversation_id" in helper


def test_t103_runtime_scope_keeps_dialogues_blocks_and_t003_unchanged() -> None:
    screen = read_screen()
    assert "conversation_blocks.json" not in screen
    for filename, expected_hash in EXPECTED_UNCHANGED_HASHES.items():
        path = DATA / filename
        assert path.exists(), filename
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, filename
    assert T003_SCHEMA.exists()
    assert hashlib.sha256(T003_SCHEMA.read_bytes()).hexdigest() == EXPECTED_T003_HASH


if __name__ == "__main__":
    test_t103_quick_switch_toast_has_refresh_helper_not_ready_only()
    test_t103_refresh_helper_updates_existing_toast_in_place()
    test_t103_refresh_is_called_after_notification_creating_progression_paths()
    test_t103_keeps_t102_open_action_and_current_day_filter()
    test_t103_runtime_scope_keeps_dialogues_blocks_and_t003_unchanged()
    print("T103 quick-switch live refresh tests OK")
