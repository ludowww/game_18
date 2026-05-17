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


def test_t133_breathing_scenes_are_followup_jsons_not_separate_threads() -> None:
    source = state_text()
    for json_file, start_node, title in [
        ("sarah_meal_j1_v2_experimental.json", "j1_06_sarah_001", "J1 V2 — Rentrer manger"),
        ("nico_respiration_j1_v2_experimental.json", "j1_07_nico_001", "J1 V2 — Respiration"),
    ]:
        assert f'"res://data/{json_file}"' in source
        assert f'"{start_node}"' in source
        assert f'"{title}"' in source
    conversation_ids_start = source.index("func conversation_ids")
    conversation_ids_end = source.index("func active_conversation_ids", conversation_ids_start)
    conversation_ids_body = source[conversation_ids_start:conversation_ids_end]
    assert '"sarah_meal_j1_v2"' not in conversation_ids_body
    assert '"nico_respiration_j1_v2"' not in conversation_ids_body


def test_t133_breathing_scenes_are_deferred_until_late_j1_v2_unlock() -> None:
    source = state_text()
    assert "func _unlock_j1_v2_breathing_scenes_if_ready() -> void:" in source
    unlock_start = source.index("func _unlock_j1_v2_after_priority_choice")
    unlock_end = source.index("func _j1_v2_core_conversations_done", unlock_start)
    priority_unlock_body = source[unlock_start:unlock_end]
    assert '_attach_j1_v2_followup_scene("sarah_j1_v2", "res://data/sarah_meal_j1_v2_experimental.json", "j1_06_sarah_001", "J1 V2 — Rentrer manger", "Sarah parle du repas.")' in source
    assert '_attach_j1_v2_followup_scene("nico_j1_v2", "res://data/nico_respiration_j1_v2_experimental.json", "j1_07_nico_001", "J1 V2 — Respiration", "Nico tente une respiration.")' in source


def test_t133_validator_includes_breathing_scene_files() -> None:
    source = VALIDATOR.read_text(encoding="utf-8")
    for filename in [
        "sarah_meal_j1_v2_experimental.json",
        "nico_respiration_j1_v2_experimental.json",
    ]:
        assert filename in source


if __name__ == "__main__":
    test_t133_breathing_scene_json_files_exist_and_have_choice_nodes()
    test_t133_breathing_scenes_are_followup_jsons_not_separate_threads()
    test_t133_breathing_scenes_are_deferred_until_late_j1_v2_unlock()
    test_t133_validator_includes_breathing_scene_files()
    print("T133 J1 V2 breathing scenes tests OK")
