from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"


def state_text() -> str:
    return STATE.read_text(encoding="utf-8")


def test_t132_priority_choice_mapping_remains_available_for_reveil_archive_fallback() -> None:
    source = state_text()
    assert "const J1_V2_FIRST_REPLY_CHOICES :=" in source
    for choice_id, conversation_id in [
        ("j1_00_reply_sarah_first", "sarah_j1_v2"),
        ("j1_00_reply_camille_first", "camille_j1_v2"),
        ("j1_00_reply_nico_first", "nico_j1_v2"),
        ("j1_00_reply_maya_first", "maya_j1_v2"),
        ("j1_00_reply_ines_first", "ines_j1_v2"),
    ]:
        assert f'"{choice_id}": "{conversation_id}"' in source
    assert "func _j1_v2_forced_first_reply_conversation_id() -> String:" in source
    assert 'var reveil_choices: Array = conversations["j1_00_reveil_v2"].get("choices", [])' in source


def test_t132_messages_list_exposes_core_conversations_instead_of_forced_first_reply() -> None:
    source = state_text()
    active_start = source.index("func active_conversation_ids")
    active_end = source.index("func archived_conversation_ids", active_start)
    active_body = source[active_start:active_end]
    assert "var source_ids: Array = _j1_v2_message_list_core_ids()" in active_body
    assert 'id == "j1_00_reveil_v2"' in active_body
    assert "_j1_v2_forced_first_reply_conversation_id" not in active_body


def test_t132_direct_selection_sets_first_open_flags_without_tunneling() -> None:
    source = state_text()
    select_start = source.index("func set_current_conversation")
    select_end = source.index("func handle_j1_v2_first_open_from_messages", select_start)
    select_body = source[select_start:select_end]
    assert "handle_j1_v2_first_open_from_messages(id)" in select_body
    assert "current_conversation_id = id" in select_body
    assert "forced_j1_v2_id" not in select_body

    handler_start = source.index("func handle_j1_v2_first_open_from_messages")
    handler_end = source.index("func _j1_v2_first_open_already_chosen", handler_start)
    handler_body = source[handler_start:handler_end]
    assert "J1_V2_FIRST_OPEN_FLAGS[conversation_id]" in handler_body
    assert "J1_V2_DELAYED_REPLY_FLAGS[other_id]" in handler_body


if __name__ == "__main__":
    test_t132_priority_choice_mapping_remains_available_for_reveil_archive_fallback()
    test_t132_messages_list_exposes_core_conversations_instead_of_forced_first_reply()
    test_t132_direct_selection_sets_first_open_flags_without_tunneling()
    print("T132 J1 V2 first reply compatibility tests OK")
