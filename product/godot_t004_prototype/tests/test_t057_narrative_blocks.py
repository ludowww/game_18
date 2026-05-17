from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
SCREEN_SCRIPT = ROOT / "scripts" / "conversation_screen.gd"
CONFIG = ROOT / "data" / "conversation_blocks.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def config() -> dict:
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def test_t057_declares_runtime_conversation_blocks() -> None:
    data = config()
    for marker in [
        "camille_c1a",
        "camille_c1b",
        "camille_c1c",
        "sarah_s1a",
        "sarah_s1b",
        "sarah_s1c",
    ]:
        assert marker in data["blocks"]
    assert "conversation_blocks" in read(STATE_SCRIPT)


def test_t057_blocks_are_saved_and_loaded_compatibly() -> None:
    text = read(STATE_SCRIPT)
    assert '"conversation_blocks": conversation_blocks.duplicate(true)' in text
    assert 'payload.get("conversation_blocks", {})' in text
    assert "_migrate_blocks_from_existing_save" in text


def test_t057_conversation_screen_stops_at_block_boundaries() -> None:
    state = read(STATE_SCRIPT)
    screen = read(SCREEN_SCRIPT)
    assert "func is_current_block_end_node" in state
    assert "func complete_current_block" in state
    assert "ConversationState.is_current_block_end_node(node_id)" in screen
    assert "ConversationState.complete_current_block(next_id)" in screen
    assert "_show_waiting_state" in screen


def test_t057_notifications_require_available_unlocked_block() -> None:
    text = read(STATE_SCRIPT)
    assert "has_available_block_for_conversation" in text
    assert "not has_available_block_for_conversation(target_id)" in text
    assert "_unlock_block" in text


if __name__ == "__main__":
    test_t057_declares_runtime_conversation_blocks()
    test_t057_blocks_are_saved_and_loaded_compatibly()
    test_t057_conversation_screen_stops_at_block_boundaries()
    test_t057_notifications_require_available_unlocked_block()
    print("T057 narrative block lock tests OK")
