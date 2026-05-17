from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"


def script_text() -> str:
    return STATE_SCRIPT.read_text(encoding="utf-8")


def test_dynamic_notifications_require_relevant_target_state() -> None:
    text = script_text()
    assert "func _can_emit_dynamic_notification" in text
    assert 'bool(target_state.get("done", false))' in text
    assert 'bool(target_state.get("available", false))' in text
    assert "current_day > 1" in text


def test_dynamic_notification_guard_runs_before_fired_event_is_recorded() -> None:
    text = script_text()
    guard_index = text.index("_can_emit_dynamic_notification")
    append_index = text.index("dynamic_notifications_fired.append(event_id)")
    assert guard_index < append_index


if __name__ == "__main__":
    test_dynamic_notifications_require_relevant_target_state()
    test_dynamic_notification_guard_runs_before_fired_event_is_recorded()
    print("T053 notification guard tests OK")
