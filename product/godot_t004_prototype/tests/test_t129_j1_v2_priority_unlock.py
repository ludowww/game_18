from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
DATA = ROOT / "data"


def state_text() -> str:
    return STATE.read_text(encoding="utf-8")


def load_json(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def test_t129_j1_v2_only_reveil_is_available_before_priority_choice() -> None:
    source = state_text()
    assert '"j1_00_reveil_v2"' in source
    assert '"sarah_j1_v2"' in source
    assert '"camille_j1_v2"' in source
    assert '"j1_00_reveil_v2",' in source
    assert '"sarah_j1_v2",' in source
    assert '"camille_j1_v2",' in source
    assert '"J1 V2 — Où tu étais ?"' in source
    assert '"J1 V2 — Dehors"' in source
    assert '"j1_00_reveil_v2"' in source and 'true,\n\t\t\ttrue,\n\t\t\ttrue,\n\t\t\t"j1_00_sys_001"' in source
    assert '"sarah_j1_v2"' in source and 'false,\n\t\t\tfalse,\n\t\t\ttrue,\n\t\t\t"j1_01_sarah_001"' in source
    assert '"camille_j1_v2"' in source and 'false,\n\t\t\tfalse,\n\t\t\ttrue,\n\t\t\t"j1_02_camille_001"' in source


def test_t129_j1_00_choice_sets_delay_flags_for_non_first_converted_contacts() -> None:
    data = load_json("j1_00_reveil_messages_v2_experimental.json")
    choice_node = next(node for node in data["nodes"] if node["id"] == "j1_00_choice_priority")
    effects_by_id = {choice["id"]: choice["effects"] for choice in choice_node["choices"]}
    assert "delayed_reply_camille_j1" in effects_by_id["j1_00_reply_sarah_first"]["flags"]
    assert "delayed_reply_sarah_j1" in effects_by_id["j1_00_reply_camille_first"]["flags"]


def test_t129_state_unlocks_converted_v2_conversations_after_priority_completion() -> None:
    source = state_text()
    assert "func _unlock_j1_v2_after_priority_choice() -> void:" in source
    assert 'if current_conversation_id == "j1_00_reveil_v2":' in source
    assert '_unlock_j1_v2_after_priority_choice()' in source
    assert 'conversations["sarah_j1_v2"]["available"] = true' in source
    assert 'conversations["camille_j1_v2"]["available"] = true' in source
    assert 'mark_conversation_new("sarah_j1_v2"' in source
    assert 'mark_conversation_new("camille_j1_v2"' in source


if __name__ == "__main__":
    test_t129_j1_v2_only_reveil_is_available_before_priority_choice()
    test_t129_j1_00_choice_sets_delay_flags_for_non_first_converted_contacts()
    test_t129_state_unlocks_converted_v2_conversations_after_priority_completion()
    print("T129 J1 V2 priority unlock tests OK")
