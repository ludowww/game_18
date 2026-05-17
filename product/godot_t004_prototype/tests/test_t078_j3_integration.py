from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
CONFIG = ROOT / "data" / "conversation_blocks.json"
DATA = ROOT / "data"

J3_CONVERSATIONS = {
    "camille_j3": "camille_j3_complete.json",
    "sarah_j3": "sarah_j3_complete.json",
}

J3_BLOCKS = [
    "camille_c3a",
    "sarah_s3a",
    "camille_c3b",
    "sarah_s3b",
    "camille_c3c",
    "sarah_s3c",
]

EXPECTED_BLOCKS = {
    "camille_c3a": ("camille_j3", "c3_block_a", ["c3_009_a", "c3_009_b", "c3_009_c"], "sarah_s3a", "sarah_j3"),
    "sarah_s3a": ("sarah_j3", "s3_block_a", ["s3_009_a", "s3_009_b", "s3_009_c"], "camille_c3b", "camille_j3"),
    "camille_c3b": ("camille_j3", "c3_block_b", ["c3_020_a", "c3_020_b", "c3_020_c"], "sarah_s3b", "sarah_j3"),
    "sarah_s3b": ("sarah_j3", "s3_block_b", ["s3_018_a", "s3_018_b", "s3_018_c"], "camille_c3c", "camille_j3"),
    "camille_c3c": ("camille_j3", "c3_block_c", ["c3_end_pull", "c3_end_boundary", "c3_end_trace"], "sarah_s3c", "sarah_j3"),
    "sarah_s3c": ("sarah_j3", "s3_block_c", ["s3_end_presence", "s3_end_fragile", "s3_end_distance"], "", ""),
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_dialogue(path: Path) -> dict:
    data = load_json(path)
    ids = [node["id"] for node in data["nodes"]]
    assert len(ids) == len(set(ids)), f"duplicate ids in {path.name}"
    id_set = set(ids)
    missing = []
    for node in data["nodes"]:
        nxt = node.get("next", "")
        if nxt and nxt not in id_set:
            missing.append((node["id"], nxt))
        for choice in node.get("choices", []):
            choice_next = choice.get("next", "")
            if choice_next and choice_next not in id_set:
                missing.append((choice.get("id", node["id"]), choice_next))
    assert missing == [], f"missing targets in {path.name}: {missing}"
    return data


def test_t078_j3_json_files_are_valid_and_mvp_schema_unchanged() -> None:
    for conversation_id, filename in J3_CONVERSATIONS.items():
        path = DATA / filename
        assert path.exists(), filename
        data = validate_dialogue(path)
        assert data["schema_version"] == "0.1"
        assert data["conversation_id"] == f"{conversation_id}_complete"
        assert data["day"] == 3
        assert data["contact_id"] in ["camille", "sarah"]
        assert len([n for n in data["nodes"] if n.get("type") == "choice"]) >= 5
        assert len([n for n in data["nodes"] if n.get("type") == "end"]) == 3


def test_t078_state_declares_j3_conversations_and_day3_progression() -> None:
    source = STATE_SCRIPT.read_text(encoding="utf-8")
    assert '3: ["camille_j3", "sarah_j3"]' in source
    assert '"camille_j3": _new_conversation_state' in source
    assert '"res://data/camille_j3_complete.json"' in source
    assert '"sarah_j3": _new_conversation_state' in source
    assert '"res://data/sarah_j3_complete.json"' in source
    assert '"camille_j3", "sarah_j3"' in source
    for conversation_id in ["camille", "sarah", "camille_j2", "sarah_j2", "camille_j3", "sarah_j3"]:
        assert f'"{conversation_id}"' in source
    assert "current_day >= 4" in source or "current_day > 4" in source


def test_t078_conversation_blocks_config_declares_j3_rhythm() -> None:
    data = load_json(CONFIG)
    assert data["block_order"][12:18] == J3_BLOCKS
    assert len(data["block_order"]) >= 18
    assert len(data["blocks"]) >= 18
    for block_id, (conversation_id, start_node, end_nodes, unlock, notification_target) in EXPECTED_BLOCKS.items():
        block = data["blocks"][block_id]
        assert block["conversation_id"] == conversation_id
        assert block["start_node"] == start_node
        assert block["end_nodes"] == end_nodes
        assert block["unlock_on_done"] == unlock
        assert block["notification_target"] == notification_target
        dialogue = validate_dialogue(DATA / J3_CONVERSATIONS[conversation_id])
        dialogue_ids = {node["id"] for node in dialogue["nodes"]}
        assert start_node in dialogue_ids
        for node_id in end_nodes:
            assert node_id in dialogue_ids


if __name__ == "__main__":
    test_t078_j3_json_files_are_valid_and_mvp_schema_unchanged()
    test_t078_state_declares_j3_conversations_and_day3_progression()
    test_t078_conversation_blocks_config_declares_j3_rhythm()
    print("T078 J3 integration tests OK")
