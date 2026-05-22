#!/usr/bin/env python3
"""T161: refresh unread prompt immediately after J1 V2 breathing scenes unlock."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")
SCREEN = (ROOT / "scripts" / "conversation_screen.gd").read_text(encoding="utf-8")


def function_body(source: str, name: str) -> str:
    marker = f"func {name}"
    assert marker in source, marker
    body = source[source.index(marker):]
    return body.split("\nfunc ", 1)[0]


def test_breathing_unlock_attaches_sarah_and_nico_followups_as_new_messages():
    body = function_body(STATE, "_unlock_j1_v2_breathing_scenes_if_ready")
    assert "sarah_meal_j1_v2_experimental.json" in body
    assert "nico_respiration_j1_v2_experimental.json" in body
    attach_body = function_body(STATE, "_attach_j1_v2_followup_scene")
    assert "mark_conversation_new(conversation_id, preview)" in attach_body
    assert 'state["done"] = false' in attach_body


def test_mark_current_done_unlocks_breathing_scenes_before_refresh_possible():
    body = function_body(STATE, "mark_current_done")
    assert "_unlock_j1_v2_breathing_scenes_if_ready()" in body
    assert "refresh_day_progression()" in body


def test_conversation_screen_refreshes_quick_switch_after_mark_current_done():
    body = function_body(SCREEN, "_advance_to")
    end_branch = body[body.index("if node_type == \"end\":"):]
    end_branch = end_branch.split("\n\t\treturn", 1)[0]
    marker = "ConversationState.mark_current_done()"
    assert marker in end_branch
    after = end_branch[end_branch.index(marker):]
    assert "ConversationState.repair_available_block_notifications()" in after
    assert "_refresh_quick_switch_notification()" in after


def test_quick_switch_can_show_messages_non_lus_when_multiple_unread_exist():
    quick_body = function_body(STATE, "quick_switch_new_conversation_id")
    assert 'return "__unread_messages__"' in quick_body
    button_body = function_body(SCREEN, "_make_quick_switch_notification")
    assert 'display_name: String = "Messages non lus..."' in button_body
    assert 'target_id == "__unread_messages__"' in button_body


if __name__ == "__main__":
    test_breathing_unlock_attaches_sarah_and_nico_followups_as_new_messages()
    test_mark_current_done_unlocks_breathing_scenes_before_refresh_possible()
    test_conversation_screen_refreshes_quick_switch_after_mark_current_done()
    test_quick_switch_can_show_messages_non_lus_when_multiple_unread_exist()
    print("T161 breathing unlock unread refresh tests OK")
