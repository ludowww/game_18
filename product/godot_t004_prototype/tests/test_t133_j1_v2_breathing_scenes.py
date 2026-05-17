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


def test_t133_breathing_scene_json_files_exist_and_have_choice_nodes() -> None:
    expected = {
        "sarah_meal_j1_v2_experimental.json": "j1_06_choice_sarah_meal",
        "nico_respiration_j1_v2_experimental.json": "j1_07_choice_nico_respiration",
    }
    for filename, choice_id in expected.items():
        data = load_json(filename)
        assert data.get("experimental") is True
        assert data.get("start_node")
        node_ids = {node["id"] for node in data["nodes"]}
        assert choice_id in node_ids
        assert any(node.get("type") == "end" for node in data["nodes"])


def test_t133_state_declares_breathing_scenes_initially_locked() -> None:
    source = state_text()
    for conversation_id, json_file, start_node, title in [
        ("sarah_meal_j1_v2", "sarah_meal_j1_v2_experimental.json", "j1_06_sarah_001", "J1 V2 — Rentrer manger"),
        ("nico_respiration_j1_v2", "nico_respiration_j1_v2_experimental.json", "j1_07_nico_001", "J1 V2 — Respiration"),
    ]:
        assert f'"{conversation_id}"' in source
        assert f'"res://data/{json_file}"' in source
        assert f'"{start_node}"' in source
        assert f'"{title}"' in source
    assert '"sarah_meal_j1_v2",' in source
    assert '"nico_respiration_j1_v2",' in source


def test_t133_priority_completion_unlocks_breathing_scenes() -> None:
    source = state_text()
    for conversation_id in ["sarah_meal_j1_v2", "nico_respiration_j1_v2"]:
        assert f'conversations["{conversation_id}"]["available"] = true' in source
        assert f'mark_conversation_new("{conversation_id}"' in source


def test_t133_validator_includes_breathing_scene_files() -> None:
    source = VALIDATOR.read_text(encoding="utf-8")
    for filename in [
        "sarah_meal_j1_v2_experimental.json",
        "nico_respiration_j1_v2_experimental.json",
    ]:
        assert filename in source


if __name__ == "__main__":
    test_t133_breathing_scene_json_files_exist_and_have_choice_nodes()
    test_t133_state_declares_breathing_scenes_initially_locked()
    test_t133_priority_completion_unlocks_breathing_scenes()
    test_t133_validator_includes_breathing_scene_files()
    print("T133 J1 V2 breathing scenes tests OK")
