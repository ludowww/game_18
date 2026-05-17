from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
CONFIG = ROOT / "data" / "conversation_blocks.json"


def text() -> str:
    return STATE_SCRIPT.read_text(encoding="utf-8")


def config() -> dict:
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def test_t063_j2_conversations_are_connected_to_complete_json() -> None:
    source = text()
    assert '"camille_j2"' in source
    assert '"sarah_j2"' in source
    assert '"res://data/camille_j2_complete.json"' in source
    assert '"res://data/sarah_j2_complete.json"' in source
    assert '"Jour 2 — conversation complète MVP"' in source


def test_t063_declares_runtime_blocks_for_camille_and_sarah_j2() -> None:
    data = config()
    for marker in [
        "camille_c2a", "camille_c2b", "camille_c2c",
        "sarah_s2a", "sarah_s2b", "sarah_s2c",
    ]:
        assert marker in data["block_order"]
        assert marker in data["blocks"]
    assert data["blocks"]["camille_c2a"]["start_node"] == "c2_block_a"
    assert data["blocks"]["sarah_s2a"]["start_node"] == "s2_block_a"
    assert "c2_009_a" in data["blocks"]["camille_c2a"]["end_nodes"]
    assert "s2_009_a" in data["blocks"]["sarah_s2a"]["end_nodes"]


def test_t063_j2_blocks_are_available_from_day_two_and_can_play() -> None:
    source = text()
    assert 'current_day < int(state.get("day", 1))' in source
    assert 'block_id == "camille_c1a" or block_id == "camille_c2a"' in source
    assert '"camille_j2", "sarah_j2"' in source
    assert '2: ["camille_j2", "sarah_j2"]' in source


def test_t063_save_and_notifications_support_j2_blocks() -> None:
    source = text()
    assert 'const SAVE_VERSION := 4' in source
    assert '"conversation_blocks": conversation_blocks.duplicate(true)' in source
    assert 'has_available_block_for_conversation(target_id)' in source
    assert 'mark_conversation_new(target_id, _notification_preview_for_target(target_id))' in source
    assert 'func _notification_preview_for_target' in source


if __name__ == "__main__":
    test_t063_j2_conversations_are_connected_to_complete_json()
    test_t063_declares_runtime_blocks_for_camille_and_sarah_j2()
    test_t063_j2_blocks_are_available_from_day_two_and_can_play()
    test_t063_save_and_notifications_support_j2_blocks()
    print("T063 J2 integration tests OK")
