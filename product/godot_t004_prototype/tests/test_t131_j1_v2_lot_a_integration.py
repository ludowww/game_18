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


def test_t131_lot_a_json_files_exist_and_have_choice_nodes() -> None:
    expected = {
        "nico_j1_v2_experimental.json": "j1_03_choice_nico_version",
        "maya_j1_v2_experimental.json": "j1_04_choice_maya_pique",
        "ines_j1_v2_experimental.json": "j1_05_choice_ines_faille",
    }
    for filename, choice_id in expected.items():
        data = load_json(filename)
        assert data.get("experimental") is True
        assert data.get("start_node")
        node_ids = {node["id"] for node in data["nodes"]}
        assert choice_id in node_ids
        assert any(node.get("type") == "end" for node in data["nodes"])


def test_t131_state_declares_lot_a_conversations_initially_locked() -> None:
    source = state_text()
    for conversation_id, json_file, start_node in [
        ("nico_j1_v2", "nico_j1_v2_experimental.json", "j1_03_nico_001"),
        ("maya_j1_v2", "maya_j1_v2_experimental.json", "j1_04_maya_001"),
        ("ines_j1_v2", "ines_j1_v2_experimental.json", "j1_05_ines_001"),
    ]:
        assert f'"{conversation_id}"' in source
        assert f'"res://data/{json_file}"' in source
        assert f'"{start_node}"' in source
    # Lot A should be present but not available before the j1_00 priority choice completes.
    assert '"nico_j1_v2",' in source and '"J1 V2 — Couverture"' in source
    assert '"maya_j1_v2",' in source and '"J1 V2 — Timing"' in source
    assert '"ines_j1_v2",' in source and '"J1 V2 — Faille"' in source


def test_t131_priority_completion_unlocks_lot_a_conversations() -> None:
    source = state_text()
    for conversation_id in ["nico_j1_v2", "maya_j1_v2", "ines_j1_v2"]:
        assert f'conversations["{conversation_id}"]["available"] = true' in source
        assert f'mark_conversation_new("{conversation_id}"' in source


def test_t131_validator_includes_lot_a_files() -> None:
    source = VALIDATOR.read_text(encoding="utf-8")
    for filename in [
        "nico_j1_v2_experimental.json",
        "maya_j1_v2_experimental.json",
        "ines_j1_v2_experimental.json",
    ]:
        assert filename in source


if __name__ == "__main__":
    test_t131_lot_a_json_files_exist_and_have_choice_nodes()
    test_t131_state_declares_lot_a_conversations_initially_locked()
    test_t131_priority_completion_unlocks_lot_a_conversations()
    test_t131_validator_includes_lot_a_files()
    print("T131 J1 V2 lot A integration tests OK")
