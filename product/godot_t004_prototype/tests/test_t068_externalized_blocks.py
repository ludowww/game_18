from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
CONFIG = ROOT / "data" / "conversation_blocks.json"


def state_text() -> str:
    return STATE_SCRIPT.read_text(encoding="utf-8")


def test_t068_conversation_blocks_config_exists_and_declares_j1_j2_blocks() -> None:
    assert CONFIG.exists()
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    assert "block_order" in data
    assert "blocks" in data
    for block_id in [
        "camille_c1a", "camille_c1b", "camille_c1c",
        "sarah_s1a", "sarah_s1b", "sarah_s1c",
        "camille_c2a", "camille_c2b", "camille_c2c",
        "sarah_s2a", "sarah_s2b", "sarah_s2c",
    ]:
        assert block_id in data["block_order"]
        assert block_id in data["blocks"]
        block = data["blocks"][block_id]
        assert "conversation_id" in block
        assert "start_node" in block
        assert "end_nodes" in block
        assert "unlock_on_done" in block
        assert "notification_target" in block


def test_t068_state_loads_blocks_from_json_config_not_hardcoded_const() -> None:
    source = state_text()
    assert 'const BLOCKS_CONFIG_PATH := "res://data/conversation_blocks.json"' in source
    assert "func _load_conversation_block_defs" in source
    assert "FileAccess.open(BLOCKS_CONFIG_PATH, FileAccess.READ)" in source
    assert "conversation_block_defs" in source
    assert "CONVERSATION_BLOCKS :=" not in source
    assert "const BLOCK_ORDER :=" not in source


def test_t068_existing_save_and_notification_behaviour_are_preserved() -> None:
    source = state_text()
    assert '"conversation_blocks": conversation_blocks.duplicate(true)' in source
    assert 'payload.get("conversation_blocks", {})' in source
    assert "_migrate_blocks_from_existing_save" in source
    assert "has_available_block_for_conversation(target_id)" in source
    assert "notification_target" in source


if __name__ == "__main__":
    test_t068_conversation_blocks_config_exists_and_declares_j1_j2_blocks()
    test_t068_state_loads_blocks_from_json_config_not_hardcoded_const()
    test_t068_existing_save_and_notification_behaviour_are_preserved()
    print("T068 externalized block config tests OK")
