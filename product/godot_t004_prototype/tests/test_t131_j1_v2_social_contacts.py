from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
DATA = ROOT / "data"
VALIDATOR = ROOT / "tools" / "validate_j1_v2_experimental.py"


def state_text() -> str:
    return STATE.read_text(encoding="utf-8")


def load_json(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def test_t131_nico_maya_ines_j1_v2_json_files_exist() -> None:
    for filename, conversation_id in [
        ("nico_j1_v2_experimental.json", "nico_j1_v2"),
        ("maya_j1_v2_experimental.json", "maya_j1_v2"),
        ("ines_j1_v2_experimental.json", "ines_j1_v2"),
    ]:
        data = load_json(filename)
        assert data["experimental"] is True
        assert data["conversation_id"] == conversation_id
        assert data["nodes"]
        assert any(node.get("type") == "choice" for node in data["nodes"])
        assert any(node.get("type") == "end" for node in data["nodes"])


def test_t131_validator_tracks_nico_maya_ines_v2_files() -> None:
    source = VALIDATOR.read_text(encoding="utf-8")
    assert 'DATA / "nico_j1_v2_experimental.json"' in source
    assert 'DATA / "maya_j1_v2_experimental.json"' in source
    assert 'DATA / "ines_j1_v2_experimental.json"' in source


def test_t131_state_declares_nico_maya_ines_v2_conversations_and_unlocks_them() -> None:
    source = state_text()
    for conversation_id, filename, start_node in [
        ("nico_j1_v2", "nico_j1_v2_experimental.json", "j1_03_nico_001"),
        ("maya_j1_v2", "maya_j1_v2_experimental.json", "j1_04_maya_001"),
        ("ines_j1_v2", "ines_j1_v2_experimental.json", "j1_05_ines_001"),
    ]:
        assert f'"{conversation_id}": _new_conversation_state' in source
        assert f'"res://data/{filename}"' in source
        assert f'"{start_node}"' in source
        assert f'conversations["{conversation_id}"]["available"] = true' in source
        assert f'mark_conversation_new("{conversation_id}"' in source


if __name__ == "__main__":
    test_t131_nico_maya_ines_j1_v2_json_files_exist()
    test_t131_validator_tracks_nico_maya_ines_v2_files()
    test_t131_state_declares_nico_maya_ines_v2_conversations_and_unlocks_them()
    print("T131 J1 V2 social contacts integration tests OK")
