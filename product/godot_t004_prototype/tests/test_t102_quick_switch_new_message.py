from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
SCREEN = ROOT / "scripts" / "conversation_screen.gd"
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


def read_state() -> str:
    return STATE.read_text(encoding="utf-8")


def read_screen() -> str:
    return SCREEN.read_text(encoding="utf-8")


def section(source: str, start: str, end: str) -> str:
    return source.split(start, 1)[1].split(end, 1)[0]


def test_t102_state_helper_returns_current_day_new_conversation_only() -> None:
    source = read_state()
    helper = section(source, "func quick_switch_new_conversation_id", "func set_current_conversation")
    assert "active_conversation_ids()" in helper
    assert "id == current_conversation_id" in helper
    assert "has_new(id)" in helper
    assert "done" in helper
    assert "archived_conversation_ids()" not in helper
    assert "visible_conversation_ids()" not in helper


def test_t102_conversation_screen_has_discreet_in_app_open_banner() -> None:
    source = read_screen()
    assert "quick_switch_target_id" in source
    assert "func _make_quick_switch_notification" in source
    banner = section(source, "func _make_quick_switch_notification", "func _open_quick_switch_conversation")
    assert "Nouveau message de " in banner
    assert "Ouvrir" in banner
    assert "Button.new()" in banner
    assert "_refresh_quick_switch_notification()" in source
    assert "root_container.add_child(quick_switch_button)" in source
    assert "OS" not in banner
    assert "create_timer" not in banner


def test_t102_open_action_reuses_chat_open_path_and_marks_only_target_read() -> None:
    source = read_screen()
    action = section(source, "func _open_quick_switch_conversation", "func _load_conversation")
    assert "ConversationState.set_current_conversation(target_id)" in action
    assert "ConversationState.mark_conversation_read(target_id)" in action
    assert "change_scene_to_file(\"res://scenes/conversation_screen.tscn\")" in action
    assert "mark_current_opened" not in action
    assert "reset_progression" not in action


def test_t102_runtime_scope_does_not_touch_dialogue_json_blocks_or_t003() -> None:
    state = read_state()
    screen = read_screen()
    assert "conversation_blocks.json" not in screen
    assert "conversation_blocks.json" in state  # state reads existing config but T102 must not alter it.
    for filename, expected_hash in EXPECTED_UNCHANGED_HASHES.items():
        path = DATA / filename
        assert path.exists(), filename
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, filename
    assert T003_SCHEMA.exists()
    assert hashlib.sha256(T003_SCHEMA.read_bytes()).hexdigest() == EXPECTED_T003_HASH


if __name__ == "__main__":
    test_t102_state_helper_returns_current_day_new_conversation_only()
    test_t102_conversation_screen_has_discreet_in_app_open_banner()
    test_t102_open_action_reuses_chat_open_path_and_marks_only_target_read()
    test_t102_runtime_scope_does_not_touch_dialogue_json_blocks_or_t003()
    print("T102 quick-switch new-message tests OK")
