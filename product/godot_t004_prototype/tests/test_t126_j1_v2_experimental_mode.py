from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
LIST_SCRIPT = ROOT / "scripts" / "conversation_list.gd"
DATA = ROOT / "data"


def state_text() -> str:
    return STATE_SCRIPT.read_text(encoding="utf-8")


def list_text() -> str:
    return LIST_SCRIPT.read_text(encoding="utf-8")


def test_t126_experimental_j1_v2_json_files_exist_and_are_validated() -> None:
    for filename in [
        "j1_00_reveil_messages_v2_experimental.json",
        "sarah_j1_v2_experimental.json",
        "camille_j1_v2_experimental.json",
    ]:
        path = DATA / filename
        assert path.exists(), filename
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data.get("experimental") is True
        assert data.get("start_node")
        assert data.get("nodes")
    assert (ROOT / "tools" / "validate_j1_v2_experimental.py").exists()


def test_t126_state_declares_opt_in_experimental_j1_v2_mode() -> None:
    source = state_text()
    assert "var experimental_j1_v2_enabled: bool = false" in source
    assert "func set_experimental_j1_v2_enabled(enabled: bool) -> void:" in source
    assert "experimental_j1_v2_enabled = enabled" in source
    assert '"j1_00_reveil_v2"' in source
    assert '"sarah_j1_v2"' in source
    assert '"camille_j1_v2"' in source
    assert '"experimental": experimental' in source
    assert "func _conversation_allowed_in_current_mode(id: String, state: Dictionary) -> bool:" in source
    assert "if day == 1:" in source
    assert "if bool(state.get(\"experimental\", false)) and not experimental_j1_v2_enabled:" in source


def test_t126_experimental_j1_v2_can_play_without_conversation_blocks() -> None:
    source = state_text()
    assert '"start_node": start_node' in source
    assert '"j1_00_sys_001"' in source
    assert '"j1_01_sarah_001"' in source
    assert '"j1_02_camille_001"' in source
    assert 'if bool(state.get("experimental", false)):' in source
    assert 'return str(state.get("start_node", ""))' in source
    assert 'return current_block_id() != "" or str(state.get("start_node", "")) != ""' in source


def test_t126_experimental_j1_v2_does_not_replace_existing_j1_conversations() -> None:
    source = state_text()
    assert '"camille",' in source
    assert '"res://data/camille_j1_complete.json"' in source
    assert '"sarah",' in source
    assert '"res://data/sarah_j1_complete.json"' in source
    assert '"res://data/j1_00_reveil_messages_v2_experimental.json"' in source
    assert '"res://data/sarah_j1_v2_experimental.json"' in source
    assert '"res://data/camille_j1_v2_experimental.json"' in source


def test_t126_list_has_debug_toggle_for_j1_v2_without_auto_enabling_it() -> None:
    source = list_text()
    assert "_make_experimental_j1_v2_button" in source
    assert "Mode J1 V2 : ON" in source
    assert "Mode J1 V2 : OFF" in source
    assert "ConversationState.set_experimental_j1_v2_enabled" in source
    assert "ConversationState.experimental_j1_v2_enabled" in source


if __name__ == "__main__":
    test_t126_experimental_j1_v2_json_files_exist_and_are_validated()
    test_t126_state_declares_opt_in_experimental_j1_v2_mode()
    test_t126_experimental_j1_v2_can_play_without_conversation_blocks()
    test_t126_experimental_j1_v2_does_not_replace_existing_j1_conversations()
    test_t126_list_has_debug_toggle_for_j1_v2_without_auto_enabling_it()
    print("T126 J1 V2 experimental mode tests OK")
