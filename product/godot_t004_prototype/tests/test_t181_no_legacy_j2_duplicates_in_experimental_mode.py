#!/usr/bin/env python3
"""T181: experimental J2 message list must not show legacy MVP duplicates."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")


def _function_body(name: str) -> str:
    marker = f"func {name}"
    assert marker in STATE, f"missing {name}"
    return STATE.split(marker, 1)[1].split("\nfunc ", 1)[0]


def test_t181_conversation_mode_filter_is_centralized_for_experimental_days() -> None:
    body = _function_body("_conversation_allowed_in_current_mode")
    assert 'if bool(state.get("experimental", false)) and not experimental_j1_v2_enabled:' in body
    assert "if experimental_j1_v2_enabled:" in body
    assert 'var day: int = int(state.get("day", 1))' in body
    assert "if day == 1:" in body
    assert "if day == 2:" in body
    assert 'return bool(state.get("experimental", false))' in body
    assert "return true" in body


def test_t181_active_conversations_apply_filter_before_day_availability() -> None:
    body = _function_body("active_conversation_ids() -> Array:")
    assert "_conversation_allowed_in_current_mode(id, state)" in body
    assert 'id == "j1_00_reveil_v2"' in body  # J1 V2 special message-list behavior stays explicit.
    assert 'id == "camille_j2"' not in body
    assert 'id == "sarah_j2"' not in body


def test_t181_archives_apply_same_filter_so_current_day_legacy_duplicates_do_not_return() -> None:
    body = _function_body("archived_conversation_ids() -> Array:")
    assert "_conversation_allowed_in_current_mode(id, state)" in body
    assert 'id == "camille_j2"' not in body
    assert 'id == "sarah_j2"' not in body


def test_t181_non_experimental_mode_still_declares_legacy_j2_conversations() -> None:
    assert '"camille_j2": _new_conversation_state(' in STATE
    assert '"sarah_j2": _new_conversation_state(' in STATE
    assert '"Jour 2 — conversation complète MVP"' in STATE
    assert '"camille_j2"' in _function_body("conversation_ids() -> Array:")
    assert '"sarah_j2"' in _function_body("conversation_ids() -> Array:")


def test_t181_experimental_j2_v2_conversations_remain_available_by_state_not_hardcoded_required() -> None:
    for conversation_id in ["sarah_j2_v2", "nico_j2_v2", "camille_j2_v2", "maya_j2_v2", "ines_j2_v2"]:
        assert f'"{conversation_id}": _new_conversation_state(' in STATE
    required_body = _function_body("_required_conversations_for_current_mode(day: int) -> Array:")
    assert '"ines_j2_v2"' not in required_body


if __name__ == "__main__":
    test_t181_conversation_mode_filter_is_centralized_for_experimental_days()
    test_t181_active_conversations_apply_filter_before_day_availability()
    test_t181_archives_apply_same_filter_so_current_day_legacy_duplicates_do_not_return()
    test_t181_non_experimental_mode_still_declares_legacy_j2_conversations()
    test_t181_experimental_j2_v2_conversations_remain_available_by_state_not_hardcoded_required()
    print("T181 no legacy J2 duplicates experimental mode tests OK")
