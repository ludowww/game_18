#!/usr/bin/env python3
"""T159: a consumed Sarah meal late reopen must not be re-armed in a loop."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")


def function_body(name: str) -> str:
    marker = f"func {name}"
    assert marker in STATE, marker
    body = STATE[STATE.index(marker):]
    return body.split("\nfunc ", 1)[0]


def test_consumed_context_fields_exist():
    assert "late_reopen_consumed_flag" in STATE
    assert "late_reopen_consumed_choice_node" in STATE


def test_consume_current_late_reopen_memorizes_consumed_context_before_clearing():
    body = function_body("consume_current_late_reopen")
    assert "consumed_flag" in body
    assert "consumed_choice_node" in body
    assert 'state["late_reopen_consumed_flag"] = consumed_flag' in body
    assert 'state["late_reopen_consumed_choice_node"] = consumed_choice_node' in body
    assert body.index("consumed_flag") < body.index('state["left_open"] = false')


def test_mark_left_open_does_not_reprepare_same_consumed_reopen():
    body = function_body("mark_current_left_open_if_pending_choice")
    assert "same_late_reopen_already_consumed" in body
    assert 'state["late_reply_prepared"] = false' in body
    assert 'state["late_reply_prepared"] = true' in body
    assert 'state["late_reopen_consumed"] = false' in body
    assert 'state["late_reopen_consumed_flag"] = ""' in body
    assert 'state["late_reopen_consumed_choice_node"] = ""' in body
    assert body.index("same_late_reopen_already_consumed") < body.index('state["late_reply_prepared"] = false')


def test_current_late_reopen_start_node_stays_blocked_after_consumption():
    body = function_body("current_late_reopen_start_node")
    assert 'bool(state.get("late_reopen_consumed", false))' in body
    assert 'return ""' in body
    assert body.index('bool(state.get("late_reopen_consumed", false))') < body.index('return "j1_06_sarah_late_reopen_001"')


def test_consumed_context_fields_are_saved_and_loaded():
    for key in ["late_reopen_consumed_flag", "late_reopen_consumed_choice_node"]:
        assert f'"{key}": str(state.get("{key}", ""))' in STATE
        assert f'state["{key}"] = str(saved_state.get("{key}", state.get("{key}", "")))' in STATE


if __name__ == "__main__":
    test_consumed_context_fields_exist()
    test_consume_current_late_reopen_memorizes_consumed_context_before_clearing()
    test_mark_left_open_does_not_reprepare_same_consumed_reopen()
    test_current_late_reopen_start_node_stays_blocked_after_consumption()
    test_consumed_context_fields_are_saved_and_loaded()
    print("T159 late reopen loop prevention tests OK")
