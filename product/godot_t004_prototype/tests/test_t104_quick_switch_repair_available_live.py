from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
SCREEN = ROOT / "scripts" / "conversation_screen.gd"
LIST = ROOT / "scripts" / "conversation_list.gd"
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


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(source: str, start: str, end: str) -> str:
    return source.split(start, 1)[1].split(end, 1)[0]


def test_t104_live_repair_runs_before_quick_switch_refresh_after_block_completion() -> None:
    source = read(SCREEN)
    advance = section(source, "func _advance_to", "func _wait_before_node")
    boundary = "ConversationState.complete_current_block(next_id)"
    assert boundary in advance
    after_boundary = advance[advance.index(boundary):]
    assert "ConversationState.repair_available_block_notifications()" in after_boundary
    assert "_refresh_quick_switch_notification()" in after_boundary
    assert after_boundary.index("ConversationState.repair_available_block_notifications()") < after_boundary.index("_refresh_quick_switch_notification()")
    end_boundary = "ConversationState.complete_current_block(\"\")"
    assert end_boundary in advance
    after_end = advance[advance.index(end_boundary):]
    assert "ConversationState.repair_available_block_notifications()" in after_end
    assert after_end.index("ConversationState.repair_available_block_notifications()") < after_end.index("_refresh_quick_switch_notification()")


def test_t104_repair_available_block_covers_available_without_badge_current_day_only() -> None:
    state = read(STATE)
    repair = section(state, "func repair_available_block_notifications", "func _has_started_available_block")
    assert "status != BLOCK_STATUS_AVAILABLE" in repair
    assert "state[\"has_new\"] = true" in repair
    assert "state[\"last_preview\"] = _notification_preview_for_target(conversation_id)" in repair
    assert "int(state.get(\"day\", 1)) != current_day" in repair
    assert "bool(state.get(\"has_new\", false))" in repair
    assert "conversation_id == current_conversation_id" in repair
    assert "bool(state.get(\"done\", false))" in repair
    assert "_has_started_available_block(conversation_id, block_def)" in repair


def test_t104_repair_is_not_only_messages_list_lifecycle() -> None:
    screen = read(SCREEN)
    list_source = read(LIST)
    assert "ConversationState.repair_available_block_notifications()" in list_source
    assert screen.count("ConversationState.repair_available_block_notifications()") >= 2
    assert "func _refresh_quick_switch_notification" in screen


def test_t104_addendum_removes_godot_name_shadowing_warnings() -> None:
    screen = read(SCREEN)
    list_source = read(LIST)
    assert "var name :=" not in screen
    assert "var name :=" not in list_source
    assert "header_name_label" in screen
    assert "contact_name_label" in list_source


def test_t104_keeps_protected_files_unchanged() -> None:
    screen = read(SCREEN)
    assert "conversation_blocks.json" not in screen
    for filename, expected_hash in EXPECTED_UNCHANGED_HASHES.items():
        path = DATA / filename
        assert path.exists(), filename
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, filename
    assert T003_SCHEMA.exists()
    assert hashlib.sha256(T003_SCHEMA.read_bytes()).hexdigest() == EXPECTED_T003_HASH


if __name__ == "__main__":
    test_t104_live_repair_runs_before_quick_switch_refresh_after_block_completion()
    test_t104_repair_available_block_covers_available_without_badge_current_day_only()
    test_t104_repair_is_not_only_messages_list_lifecycle()
    test_t104_addendum_removes_godot_name_shadowing_warnings()
    test_t104_keeps_protected_files_unchanged()
    print("T104 quick-switch available-block live repair tests OK")
