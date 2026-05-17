from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"


def state_text() -> str:
    return STATE.read_text(encoding="utf-8")


def test_t132_priority_choice_maps_explicit_choice_ids_to_forced_conversation() -> None:
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
    assert "for index in range(reveil_choices.size() - 1, -1, -1):" in source
    assert 'not bool(target_state.get("started", false))' in source


def test_t132_messages_list_only_exposes_forced_first_reply_until_it_starts() -> None:
    source = state_text()
    active_start = source.index("func active_conversation_ids")
    active_end = source.index("func archived_conversation_ids", active_start)
    active_body = source[active_start:active_end]
    assert "var forced_j1_v2_id: String = _j1_v2_forced_first_reply_conversation_id()" in active_body
    assert 'if forced_j1_v2_id != "" and id != forced_j1_v2_id:' in active_body
    assert "continue" in active_body


def test_t132_direct_selection_and_unlock_route_to_forced_first_reply() -> None:
    source = state_text()
    select_start = source.index("func set_current_conversation")
    select_end = source.index("func current()", select_start)
    select_body = source[select_start:select_end]
    assert "var forced_j1_v2_id: String = _j1_v2_forced_first_reply_conversation_id()" in select_body
    assert 'if forced_j1_v2_id != "" and id != forced_j1_v2_id:' in select_body
    assert "return" in select_body

    unlock_start = source.index("func _unlock_j1_v2_after_priority_choice")
    unlock_end = source.index("func has_new", unlock_start)
    unlock_body = source[unlock_start:unlock_end]
    assert "var forced_j1_v2_id: String = _j1_v2_forced_first_reply_conversation_id()" in unlock_body
    assert 'if forced_j1_v2_id != "":' in unlock_body
    assert "current_conversation_id = forced_j1_v2_id" in unlock_body


if __name__ == "__main__":
    test_t132_priority_choice_maps_explicit_choice_ids_to_forced_conversation()
    test_t132_messages_list_only_exposes_forced_first_reply_until_it_starts()
    test_t132_direct_selection_and_unlock_route_to_forced_first_reply()
    print("T132 J1 V2 forced first reply tests OK")
