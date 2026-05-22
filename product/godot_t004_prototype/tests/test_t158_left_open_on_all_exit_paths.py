#!/usr/bin/env python3
"""T158: all conversation exits mark left_open before leaving."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = (ROOT / "scripts" / "conversation_screen.gd").read_text(encoding="utf-8")
MARK = "ConversationState.mark_current_left_open_if_pending_choice()"
LIST_EXIT = 'get_tree().change_scene_to_file("res://scenes/conversation_list.tscn")'
SWITCH_EXIT = "ConversationState.set_current_conversation(target_id)"


def function_body(name: str) -> str:
    marker = f"func {name}"
    assert marker in SCREEN, marker
    body = SCREEN[SCREEN.index(marker):]
    return body.split("\nfunc ", 1)[0]


def test_back_button_still_marks_left_open_before_returning_to_messages():
    body = function_body("_make_header")
    assert MARK in body
    assert LIST_EXIT in body
    assert body.index(MARK) < body.index(LIST_EXIT)


def test_quick_switch_marks_left_open_before_unread_messages_exit():
    body = function_body("_open_quick_switch_conversation")
    assert MARK in body
    assert LIST_EXIT in body
    assert body.index(MARK) < body.index(LIST_EXIT)


def test_quick_switch_marks_left_open_before_switching_conversation():
    body = function_body("_open_quick_switch_conversation")
    assert MARK in body
    assert SWITCH_EXIT in body
    assert body.index(MARK) < body.index(SWITCH_EXIT)


if __name__ == "__main__":
    test_back_button_still_marks_left_open_before_returning_to_messages()
    test_quick_switch_marks_left_open_before_unread_messages_exit()
    test_quick_switch_marks_left_open_before_switching_conversation()
    print("T158 left_open exit path tests OK")
