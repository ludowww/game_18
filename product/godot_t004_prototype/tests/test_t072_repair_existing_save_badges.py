from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
LIST_SCRIPT = ROOT / "scripts" / "conversation_list.gd"


def state_text() -> str:
    return STATE_SCRIPT.read_text(encoding="utf-8")


def list_text() -> str:
    return LIST_SCRIPT.read_text(encoding="utf-8")


def test_t072_repair_helper_exists_and_runs_after_load() -> None:
    source = state_text()
    assert "func repair_available_block_notifications" in source
    assert "repair_available_block_notifications()" in source
    assert "load_progression()" in source


def test_t072_repair_only_targets_relevant_available_unopened_blocks() -> None:
    source = state_text()
    assert 'status != BLOCK_STATUS_AVAILABLE' in source
    assert 'bool(state.get("done", false))' in source
    assert 'conversation_id == current_conversation_id' in source
    assert 'not bool(state.get("available", false))' in source
    assert '_has_started_available_block' in source
    assert 'next_node != start_node' in source


def test_t072_repair_restores_badge_without_overwriting_started_blocks() -> None:
    source = state_text()
    assert 'state["has_new"] = true' in source
    assert '"Nouveau message de "' in source
    assert '_has_started_available_block(conversation_id, block_def)' in source


def test_t072_messages_screen_refresh_triggers_repair() -> None:
    source = list_text()
    assert "ConversationState.repair_available_block_notifications()" in source


if __name__ == "__main__":
    test_t072_repair_helper_exists_and_runs_after_load()
    test_t072_repair_only_targets_relevant_available_unopened_blocks()
    test_t072_repair_restores_badge_without_overwriting_started_blocks()
    test_t072_messages_screen_refresh_triggers_repair()
    print("T072 repair existing save badge tests OK")
