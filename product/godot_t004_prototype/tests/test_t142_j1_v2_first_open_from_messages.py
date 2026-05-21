from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
LIST = ROOT / "scripts" / "conversation_list.gd"

CORE_CONVERSATIONS = [
    ("sarah_j1_v2", "first_reply_sarah", "delayed_reply_sarah_j1"),
    ("camille_j1_v2", "first_reply_camille", "delayed_reply_camille_j1"),
    ("nico_j1_v2", "first_reply_nico", "delayed_reply_nico_j1"),
    ("maya_j1_v2", "first_reply_maya", "delayed_reply_maya_j1"),
    ("ines_j1_v2", "first_reply_ines", "delayed_reply_ines_j1"),
]


def state_text() -> str:
    return STATE.read_text(encoding="utf-8")


def list_text() -> str:
    return LIST.read_text(encoding="utf-8")


def body(source: str, func_name: str, next_func_name: str) -> str:
    start = source.index(f"func {func_name}")
    end = source.index(f"func {next_func_name}", start)
    return source[start:end]


def test_t142_has_dedicated_first_open_mapping_and_handler() -> None:
    source = state_text()
    assert "const J1_V2_FIRST_OPEN_FLAGS :=" in source
    assert "const J1_V2_DELAYED_REPLY_FLAGS :=" in source
    for conversation_id, first_flag, delayed_flag in CORE_CONVERSATIONS:
        assert f'"{conversation_id}": "{first_flag}"' in source
        assert f'"{conversation_id}": "{delayed_flag}"' in source
    assert "func handle_j1_v2_first_open_from_messages(conversation_id: String) -> void:" in source


def test_t142_first_open_sets_first_flag_and_delays_all_other_core_conversations() -> None:
    source = state_text()
    handler = body(source, "handle_j1_v2_first_open_from_messages", "_j1_v2_first_open_already_chosen")
    assert "apply_global_effects" in handler
    assert "J1_V2_FIRST_OPEN_FLAGS[conversation_id]" in handler
    assert "for other_id in J1_V2_CORE_CONVERSATIONS:" in handler
    assert "if other_id == conversation_id:" in handler
    assert "J1_V2_DELAYED_REPLY_FLAGS[other_id]" in handler
    assert '"j1_00_reveil_v2"' not in handler


def test_t142_active_messages_list_exposes_core_j1_v2_conversations_not_reveil_menu() -> None:
    source = state_text()
    active = body(source, "active_conversation_ids", "archived_conversation_ids")
    assert "_j1_v2_message_list_core_ids()" in active
    assert "_j1_v2_forced_first_reply_conversation_id" not in active
    assert 'id == "j1_00_reveil_v2"' in active
    assert "continue" in active
    defaults = body(source, "_unlock_j1_v2_core_from_messages", "_j1_v2_message_list_core_ids")
    for conversation_id, _, _ in CORE_CONVERSATIONS:
        assert f'conversations["{conversation_id}"]["available"] = true' in defaults
        assert f'mark_conversation_new("{conversation_id}"' in defaults


def test_t142_conversation_list_shows_non_blocking_first_open_note() -> None:
    source = list_text()
    assert "j1_v2_should_show_first_open_note" in source
    assert "Ton téléphone s’allume" in source
    assert "La première que tu ouvres donnera le ton" in source


def test_t142_breathing_scenes_still_wait_for_five_core_conversations_done() -> None:
    source = state_text()
    core = body(source, "_j1_v2_core_conversations_done", "_unlock_j1_v2_breathing_scenes_if_ready")
    for conversation_id, _, _ in CORE_CONVERSATIONS:
        assert f'"{conversation_id}"' in core
    unlock = body(source, "_unlock_j1_v2_breathing_scenes_if_ready", "_attach_j1_v2_followup_scene")
    assert "if not _j1_v2_core_conversations_done():" in unlock
    assert "sarah_meal_j1_v2_experimental.json" in unlock
    assert "nico_respiration_j1_v2_experimental.json" in unlock


if __name__ == "__main__":
    test_t142_has_dedicated_first_open_mapping_and_handler()
    test_t142_first_open_sets_first_flag_and_delays_all_other_core_conversations()
    test_t142_active_messages_list_exposes_core_j1_v2_conversations_not_reveil_menu()
    test_t142_conversation_list_shows_non_blocking_first_open_note()
    test_t142_breathing_scenes_still_wait_for_five_core_conversations_done()
    print("T142 J1 V2 first open from Messages tests OK")
