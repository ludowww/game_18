from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
LIST_SCRIPT = ROOT / "scripts" / "conversation_list.gd"
CONFIG = ROOT / "data" / "conversation_blocks.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_t070_block_unlocks_use_same_badge_preview_pipeline_as_messages_list() -> None:
    state = read(STATE_SCRIPT)
    assert "func _can_emit_block_unlock_notification" in state
    assert "func _notification_preview_for_target" in state
    assert "mark_conversation_new(target_id, _notification_preview_for_target(target_id))" in state
    assert "state[\"has_new\"] = true" in state
    assert "state[\"last_preview\"] = preview" in state
    assert "ConversationState.preview_text(conversation_id)" in read(LIST_SCRIPT)
    assert "ConversationState.has_new(conversation_id)" in read(LIST_SCRIPT)


def test_t070_unlock_notifications_are_guarded_without_losing_save() -> None:
    state = read(STATE_SCRIPT)
    assert 'str(block_state.get("status", BLOCK_STATUS_LOCKED)) != BLOCK_STATUS_LOCKED' in state
    assert 'target_id == "" or target_id == current_conversation_id' in state
    assert 'not bool(target_state.get("available", false))' in state
    assert 'bool(target_state.get("done", false))' in state
    assert "else:\n\t\tsave_progression()" in state


def test_t071_unlock_badge_guard_does_not_requery_available_block_after_unlock() -> None:
    state = read(STATE_SCRIPT)
    guard_start = state.index("func _can_emit_block_unlock_notification")
    guard_end = state.index("func has_available_block_for_conversation", guard_start)
    guard_body = state[guard_start:guard_end]
    assert "has_available_block_for_conversation" not in guard_body
    assert "unlocked_block_id" in guard_body


def test_t070_config_keeps_neutral_notification_targets_for_all_unlocked_blocks() -> None:
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    blocks = data["blocks"]
    expected_targets = {
        "camille_c1a": "sarah",
        "sarah_s1a": "camille",
        "camille_c1b": "sarah",
        "sarah_s1b": "camille",
        "camille_c1c": "sarah",
        "camille_c2a": "sarah_j2",
        "sarah_s2a": "camille_j2",
        "camille_c2b": "sarah_j2",
        "sarah_s2b": "camille_j2",
        "camille_c2c": "sarah_j2",
    }
    for block_id, target_id in expected_targets.items():
        assert blocks[block_id]["notification_target"] == target_id
        assert blocks[block_id]["unlock_on_done"] != ""
    assert blocks["sarah_s1c"]["notification_target"] == ""
    assert blocks["sarah_s2c"]["notification_target"] == ""


if __name__ == "__main__":
    test_t070_block_unlocks_use_same_badge_preview_pipeline_as_messages_list()
    test_t070_unlock_notifications_are_guarded_without_losing_save()
    test_t071_unlock_badge_guard_does_not_requery_available_block_after_unlock()
    test_t070_config_keeps_neutral_notification_targets_for_all_unlocked_blocks()
    print("T070/T071 block unlock badge/preview regression tests OK")
