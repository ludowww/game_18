from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NARRATIVE = ROOT.parents[1] / "narrative"
STATE_SCRIPT = ROOT / "scripts" / "conversation_state.gd"
BLOCKS_CONFIG = DATA / "conversation_blocks.json"
VALIDATOR = ROOT / "tools" / "validate_dialogues_and_blocks.py"

J4_CONVERSATIONS = {
    "camille_j4": {"file": "camille_j4_complete.json", "source": "t092_camille_j4_complete.json", "contact": "camille", "conversation_id": "camille_j4_complete", "start": "c4_block_a", "prefix": "c4", "ends": ["c4_end_window", "c4_end_trace", "c4_end_retreat"]},
    "maya_j4": {"file": "maya_j4_complete.json", "source": "t093_maya_j4_complete.json", "contact": "maya", "conversation_id": "maya_j4_complete", "start": "m4_block_a", "prefix": "m4", "ends": ["m4_end_gratitude", "m4_end_cover", "m4_end_distance"]},
    "ines_j4": {"file": "ines_j4_complete.json", "source": "t094_ines_j4_complete.json", "contact": "ines", "conversation_id": "ines_j4_complete", "start": "i4_block_a", "prefix": "i4", "ends": ["i4_end_open", "i4_end_boundary", "i4_end_complication"]},
    "nico_j4": {"file": "nico_j4_complete.json", "source": "t095_nico_j4_complete.json", "contact": "nico", "conversation_id": "nico_j4_complete", "start": "n4_block_a", "prefix": "n4", "ends": ["n4_end_clarify", "n4_end_cloud", "n4_end_silence"]},
}

J4_BLOCK_ORDER = [
    "camille_c4a", "maya_m4a", "ines_i4a", "nico_n4a",
    "camille_c4b", "maya_m4b", "ines_i4b", "nico_n4b",
    "camille_c4c", "maya_m4c", "ines_i4c", "nico_n4c",
]

EXPECTED_BLOCKS = {
    "camille_c4a": ("camille_j4", "c4_block_a", ["c4_009_a", "c4_009_b", "c4_009_c"], "maya_m4a", "maya_j4"),
    "maya_m4a": ("maya_j4", "m4_block_a", ["m4_009_a", "m4_009_b", "m4_009_c"], "ines_i4a", "ines_j4"),
    "ines_i4a": ("ines_j4", "i4_block_a", ["i4_009_a", "i4_009_b", "i4_009_c"], "nico_n4a", "nico_j4"),
    "nico_n4a": ("nico_j4", "n4_block_a", ["n4_009_a", "n4_009_b", "n4_009_c"], "camille_c4b", "camille_j4"),
    "camille_c4b": ("camille_j4", "c4_block_b", ["c4_018_a", "c4_018_b", "c4_018_c"], "maya_m4b", "maya_j4"),
    "maya_m4b": ("maya_j4", "m4_block_b", ["m4_018_a", "m4_018_b", "m4_018_c"], "ines_i4b", "ines_j4"),
    "ines_i4b": ("ines_j4", "i4_block_b", ["i4_018_a", "i4_018_b", "i4_018_c"], "nico_n4b", "nico_j4"),
    "nico_n4b": ("nico_j4", "n4_block_b", ["n4_018_a", "n4_018_b", "n4_018_c"], "camille_c4c", "camille_j4"),
    "camille_c4c": ("camille_j4", "c4_block_c", ["c4_end_window", "c4_end_trace", "c4_end_retreat"], "maya_m4c", "maya_j4"),
    "maya_m4c": ("maya_j4", "m4_block_c", ["m4_end_gratitude", "m4_end_cover", "m4_end_distance"], "ines_i4c", "ines_j4"),
    "ines_i4c": ("ines_j4", "i4_block_c", ["i4_end_open", "i4_end_boundary", "i4_end_complication"], "nico_n4c", "nico_j4"),
    "nico_n4c": ("nico_j4", "n4_block_c", ["n4_end_clarify", "n4_end_cloud", "n4_end_silence"], "", ""),
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
    assert data["day"] == 4
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
    assert len(data["nodes"]) == 54
    assert len([n for n in data["nodes"] if n.get("type") == "choice"]) == 6
    assert [n["id"] for n in data["nodes"] if n.get("type") == "end"] == spec["ends"]
    for node in data["nodes"]:
        assert node.get("sender") in {"player", "system", spec["contact"]}
        for choice in node.get("choices", []):
            effects = choice.get("effects", {})
            assert isinstance(effects.get("flags", []), list)
            assert all(isinstance(flag, str) for flag in effects.get("flags", []))
            assert all(isinstance(value, int) for key, value in effects.items() if key != "flags")


def test_t097_j4_dialogue_files_are_valid_and_t003_compliant() -> None:
    for runtime_id, spec in J4_CONVERSATIONS.items():
        assert_dialogue_valid(runtime_id, spec)


def test_t097_state_declares_j4_conversations_and_day4_progression() -> None:
    source = STATE_SCRIPT.read_text(encoding="utf-8")
    assert '4: ["camille_j4", "maya_j4", "ines_j4", "nico_j4"]' in source
    for runtime_id, spec in J4_CONVERSATIONS.items():
        assert f'"{runtime_id}": _new_conversation_state' in source
        assert f'"res://data/{spec["file"]}"' in source
        assert f'"{spec["contact"]}"' in source
    for conversation_id in ["camille", "sarah", "camille_j4", "maya_j4", "ines_j4", "nico_j4", "finales_mvp"]:
        assert f'"{conversation_id}"' in source
    assert "current_day >= 4" in source or "current_day > 4" in source
    assert "J1 → J2 puis J2 → J3 puis J3 → J4" in source or "J1 → J2 → J3 → J4" in source


def test_t097_conversation_blocks_declares_j4_unlock_rhythm_and_preserves_prior_days() -> None:
    config = load_json(BLOCKS_CONFIG)
    assert config["block_order"][-28:-16] == J4_BLOCK_ORDER
    assert len(config["block_order"]) == 46
    assert len(config["blocks"]) == 46
    for old_block in ["camille_c1a", "sarah_s1c", "camille_c2a", "sarah_s2c", "camille_c3a", "sarah_s3c"]:
        assert old_block in config["blocks"]
    for block_id, (conversation_id, start_node, end_nodes, unlock, notification_target) in EXPECTED_BLOCKS.items():
        block = config["blocks"][block_id]
        assert block["conversation_id"] == conversation_id
        assert block["start_node"] == start_node
        assert block["end_nodes"] == end_nodes
        assert block["unlock_on_done"] == unlock
        assert block["notification_target"] == notification_target
        data = load_json(DATA / J4_CONVERSATIONS[conversation_id]["file"])
        ids = {node["id"] for node in data["nodes"]}
        assert start_node in ids
        for node_id in end_nodes:
            assert node_id in ids


def test_t097_t090_validator_covers_j1_to_j4_after_integration() -> None:
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
    for runtime_id, spec in J4_CONVERSATIONS.items():
        assert spec["conversation_id"] in report["active_dialogues"]
        assert report["dialogues"][spec["conversation_id"]]["source_copy_match"] is True


if __name__ == "__main__":
    test_t097_j4_dialogue_files_are_valid_and_t003_compliant()
    test_t097_state_declares_j4_conversations_and_day4_progression()
    test_t097_conversation_blocks_declares_j4_unlock_rhythm_and_preserves_prior_days()
    test_t097_t090_validator_covers_j1_to_j4_after_integration()
    print("T097 J4 integration tests OK")
