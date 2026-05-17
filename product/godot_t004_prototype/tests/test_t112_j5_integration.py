from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NARRATIVE = ROOT.parents[1] / "narrative"
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
BLOCKS_CONFIG = DATA / "conversation_blocks.json"
VALIDATOR = ROOT / "tools" / "validate_dialogues_and_blocks.py"

J5_CONVERSATIONS = {
    "sarah_j5": {"file": "sarah_j5_complete.json", "source": "t107_sarah_j5_complete.json", "contact": "sarah", "conversation_id": "sarah_j5_complete", "start": "s5_block_a", "nodes": 54, "choices": 6, "ends": ["s5_end_presence", "s5_end_fragile", "s5_end_distance"]},
    "camille_j5": {"file": "camille_j5_complete.json", "source": "t108_camille_j5_complete.json", "contact": "camille", "conversation_id": "camille_j5_complete", "start": "c5_block_a", "nodes": 54, "choices": 6, "ends": ["c5_end_a", "c5_end_b", "c5_end_c"]},
    "nico_j5": {"file": "nico_j5_complete.json", "source": "t109_nico_j5_complete.json", "contact": "nico", "conversation_id": "nico_j5_complete", "start": "n5_block_a", "nodes": 33, "choices": 4, "ends": ["n5_end_cover", "n5_end_warned", "n5_end_cost"]},
    "maya_j5": {"file": "maya_j5_complete.json", "source": "t109_maya_j5_complete.json", "contact": "maya", "conversation_id": "maya_j5_complete", "start": "m5_block_a", "nodes": 32, "choices": 4, "ends": ["m5_end_watch", "m5_end_minimized", "m5_end_distance"]},
}

J5_BLOCK_ORDER = [
    "sarah_s5a", "camille_c5a", "nico_n5a", "sarah_s5b", "camille_c5b", "maya_m5a", "sarah_s5c", "camille_c5c"
]

EXPECTED_J5_BLOCKS = {
    "sarah_s5a": ("sarah_j5", "s5_block_a", ["s5_009_a", "s5_009_b", "s5_009_c"], "camille_c5a", "camille_j5"),
    "camille_c5a": ("camille_j5", "c5_block_a", ["c5_008_a", "c5_008_b", "c5_008_c"], "nico_n5a", "nico_j5"),
    "nico_n5a": ("nico_j5", "n5_block_a", ["n5_end_cover", "n5_end_warned", "n5_end_cost"], "sarah_s5b", "sarah_j5"),
    "sarah_s5b": ("sarah_j5", "s5_block_b", ["s5_018_a", "s5_018_b", "s5_018_c"], "camille_c5b", "camille_j5"),
    "camille_c5b": ("camille_j5", "c5_block_b", ["c5_016_a", "c5_016_b", "c5_016_c"], "maya_m5a", "maya_j5"),
    "maya_m5a": ("maya_j5", "m5_block_a", ["m5_end_watch", "m5_end_minimized", "m5_end_distance"], "sarah_s5c", "sarah_j5"),
    "sarah_s5c": ("sarah_j5", "s5_block_c", ["s5_end_presence", "s5_end_fragile", "s5_end_distance"], "camille_c5c", "camille_j5"),
    "camille_c5c": ("camille_j5", "c5_block_c", ["c5_end_a", "c5_end_b", "c5_end_c"], "", ""),
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def reachable(data: dict) -> set[str]:
    nodes = {node["id"]: node for node in data["nodes"]}
    seen = set()
    stack = [data["start_node"]]
    while stack:
        node_id = stack.pop()
        if node_id in seen or node_id not in nodes:
            continue
        seen.add(node_id)
        node = nodes[node_id]
        if node.get("next"):
            stack.append(node["next"])
        for choice in node.get("choices", []):
            if choice.get("next"):
                stack.append(choice["next"])
    return seen


def assert_dialogue_valid(runtime_id: str, spec: dict) -> None:
    data = load_json(DATA / spec["file"])
    source = load_json(NARRATIVE / spec["source"])
    assert data == source
    assert data["schema_version"] == "0.1"
    assert data["conversation_id"] == spec["conversation_id"]
    assert data["day"] == 5
    assert data["contact_id"] == spec["contact"]
    assert data["start_node"] == spec["start"]
    ids = [node["id"] for node in data["nodes"]]
    assert len(ids) == len(set(ids))
    id_set = set(ids)
    missing = []
    for node in data["nodes"]:
        if node.get("next") and node["next"] not in id_set:
            missing.append((node["id"], node["next"]))
        for choice in node.get("choices", []):
            if choice.get("next") and choice["next"] not in id_set:
                missing.append((choice["id"], choice["next"]))
    assert missing == []
    assert reachable(data) == id_set
    assert len(data["nodes"]) == spec["nodes"]
    assert len([n for n in data["nodes"] if n.get("type") == "choice"]) == spec["choices"]
    assert [n["id"] for n in data["nodes"] if n.get("type") == "end"] == spec["ends"]
    for node in data["nodes"]:
        if node.get("sender") is not None:
            assert node.get("sender") in {"player", "system", spec["contact"]}
        for choice in node.get("choices", []):
            effects = choice.get("effects", {})
            assert isinstance(effects.get("flags", []), list)
            assert all(isinstance(flag, str) for flag in effects.get("flags", []))
            assert all(isinstance(value, int) for key, value in effects.items() if key != "flags")


def test_t112_j5_dialogue_files_are_valid_and_t003_compliant() -> None:
    for runtime_id, spec in J5_CONVERSATIONS.items():
        assert_dialogue_valid(runtime_id, spec)


def test_t112_state_declares_j5_conversations_progression_and_no_ines_j5() -> None:
    source = STATE_SCRIPT.read_text(encoding="utf-8")
    assert '5: ["sarah_j5", "camille_j5", "nico_j5", "maya_j5"]' in source
    for runtime_id, spec in J5_CONVERSATIONS.items():
        assert f'"{runtime_id}": _new_conversation_state' in source
        assert f'"res://data/{spec["file"]}"' in source
        assert f'"{spec["contact"]}"' in source
    assert '"ines_j5"' not in source
    assert 'ines_j5_complete.json' not in source
    assert 'current_day >= 5' in source or 'current_day > 5' in source
    assert '"sarah_j5", "camille_j5", "nico_j5", "maya_j5"' in source
    for older in ["camille_j4", "maya_j4", "ines_j4", "nico_j4"]:
        assert older in source


def test_t112_conversation_blocks_declares_j5_unlock_rhythm_and_no_ines_j5() -> None:
    config = load_json(BLOCKS_CONFIG)
    assert config["block_order"][-16:-8] == J5_BLOCK_ORDER
    assert len(config["block_order"]) == 46
    assert len(config["blocks"]) == 46
    assert not any("i5" in block_id or "ines_j5" in str(block) for block_id, block in config["blocks"].items())
    for old_block in ["camille_c1a", "sarah_s2c", "camille_c3c", "nico_n4c"]:
        assert old_block in config["blocks"]
    for block_id, (conversation_id, start_node, end_nodes, unlock, notification_target) in EXPECTED_J5_BLOCKS.items():
        block = config["blocks"][block_id]
        assert block["conversation_id"] == conversation_id
        assert block["start_node"] == start_node
        assert block["end_nodes"] == end_nodes
        assert block["unlock_on_done"] == unlock
        assert block["notification_target"] == notification_target
        data = load_json(DATA / J5_CONVERSATIONS[conversation_id]["file"])
        ids = {node["id"] for node in data["nodes"]}
        assert start_node in ids
        for node_id in end_nodes:
            assert node_id in ids


def test_t112_t090_validator_covers_j1_to_j5_after_integration() -> None:
    completed = subprocess.run(
        [sys.executable, str(VALIDATOR), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    report = json.loads(completed.stdout)
    assert report["ok"] is True
    assert report["counts"]["dialogues"] == 20
    assert report["counts"]["blocks"] == 46
    for runtime_id, spec in J5_CONVERSATIONS.items():
        assert spec["conversation_id"] in report["active_dialogues"]
        assert report["dialogues"][spec["conversation_id"]]["source_copy_match"] is True
    assert "ines_j5_complete" not in report["active_dialogues"]


if __name__ == "__main__":
    test_t112_j5_dialogue_files_are_valid_and_t003_compliant()
    test_t112_state_declares_j5_conversations_progression_and_no_ines_j5()
    test_t112_conversation_blocks_declares_j5_unlock_rhythm_and_no_ines_j5()
    test_t112_t090_validator_covers_j1_to_j5_after_integration()
    print("T112 J5 integration tests OK")
