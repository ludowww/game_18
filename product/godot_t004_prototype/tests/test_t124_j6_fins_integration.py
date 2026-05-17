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
T003_SCHEMA = ROOT.parents[0] / "t003_mini_schema_json_godot.md"

T003_SHA256 = "a29efe00e4ef1d7d96245296bb83ab2a410386f711b273f64ddcce8757b78f19"

J6_CONVERSATIONS = {
    "sarah_j6": {"file": "sarah_j6_complete.json", "source": "t120_sarah_j6_complete.json", "contact": "sarah", "conversation_id": "sarah_j6_complete", "start": "s6_block_a", "nodes": 50, "choices": 6, "ends": ["s6_end_repair", "s6_end_uncertain", "s6_end_distance"]},
    "camille_j6": {"file": "camille_j6_complete.json", "source": "t120_camille_j6_complete.json", "contact": "camille", "conversation_id": "camille_j6_complete", "start": "c6_block_a", "nodes": 50, "choices": 6, "ends": ["c6_end_chosen_seed", "c6_end_respect_distance", "c6_end_cuts_short"]},
    "nico_j6": {"file": "nico_j6_complete.json", "source": "t121_nico_j6_complete.json", "contact": "nico", "conversation_id": "nico_j6_complete", "start": "n6_block_a", "nodes": 32, "choices": 4, "ends": ["n6_end_loyal_limit", "n6_end_steps_back", "n6_end_friend_hurt"]},
    "maya_j6": {"file": "maya_j6_complete.json", "source": "t121_maya_j6_complete.json", "contact": "maya", "conversation_id": "maya_j6_complete", "start": "m6_block_a", "nodes": 32, "choices": 4, "ends": ["m6_end_warned", "m6_end_soft_cover", "m6_end_minimized"]},
    "ines_j6": {"file": "ines_j6_complete.json", "source": "t121_ines_j6_complete.json", "contact": "ines", "conversation_id": "ines_j6_complete", "start": "i6_block_a", "nodes": 25, "choices": 3, "ends": ["i6_end_boundary", "i6_end_ambiguous", "i6_end_flight"]},
    "finales_mvp": {"file": "finales_mvp_complete.json", "source": "t122_finales_mvp_complete.json", "contact": "system", "conversation_id": "finales_mvp_complete", "start": "final_block_a", "nodes": 50, "choices": 1, "ends": ["final_end_reparation_fragile", "final_end_camille_assumee", "final_end_double_vie_maintenue", "final_end_tout_se_fissure", "final_end_fuite_en_avant"]},
}

J6_BLOCK_ORDER = [
    "sarah_s6a", "camille_c6a", "nico_n6a", "maya_m6a", "sarah_s6b", "camille_c6b", "ines_i6a", "finale_fin"
]

EXPECTED_J6_BLOCKS = {
    "sarah_s6a": ("sarah_j6", "s6_block_a", ["s6_013_a", "s6_013_b", "s6_013_c"], "camille_c6a", "camille_j6"),
    "camille_c6a": ("camille_j6", "c6_block_a", ["c6_013_a", "c6_013_b", "c6_013_c"], "nico_n6a", "nico_j6"),
    "nico_n6a": ("nico_j6", "n6_block_a", ["n6_end_loyal_limit", "n6_end_steps_back", "n6_end_friend_hurt"], "maya_m6a", "maya_j6"),
    "maya_m6a": ("maya_j6", "m6_block_a", ["m6_end_warned", "m6_end_soft_cover", "m6_end_minimized"], "sarah_s6b", "sarah_j6"),
    "sarah_s6b": ("sarah_j6", "s6_block_b", ["s6_end_repair", "s6_end_uncertain", "s6_end_distance"], "camille_c6b", "camille_j6"),
    "camille_c6b": ("camille_j6", "c6_block_b", ["c6_end_chosen_seed", "c6_end_respect_distance", "c6_end_cuts_short"], "ines_i6a", "ines_j6"),
    "ines_i6a": ("ines_j6", "i6_block_a", ["i6_end_boundary", "i6_end_ambiguous", "i6_end_flight"], "finale_fin", "finales_mvp"),
    "finale_fin": ("finales_mvp", "final_block_a", ["final_end_reparation_fragile", "final_end_camille_assumee", "final_end_double_vie_maintenue", "final_end_tout_se_fissure", "final_end_fuite_en_avant"], "", ""),
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    assert data["day"] == 6
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
    allowed_senders = {"player", "system", spec["contact"]}
    if runtime_id == "finales_mvp":
        allowed_senders.update({"sarah", "camille", "nico", "maya", "ines"})
    for node in data["nodes"]:
        if node.get("sender") is not None:
            assert node.get("sender") in allowed_senders
        for choice in node.get("choices", []):
            effects = choice.get("effects", {})
            assert isinstance(effects.get("flags", []), list)
            assert all(isinstance(flag, str) for flag in effects.get("flags", []))
            assert all(isinstance(value, int) for key, value in effects.items() if key != "flags")


def test_t124_j6_and_finale_dialogue_files_are_valid_and_unchanged() -> None:
    assert sha256(T003_SCHEMA) == T003_SHA256
    for runtime_id, spec in J6_CONVERSATIONS.items():
        assert_dialogue_valid(runtime_id, spec)


def test_t124_state_declares_j6_finale_day6_and_preserves_j5() -> None:
    source = STATE_SCRIPT.read_text(encoding="utf-8")
    assert '6: ["sarah_j6", "camille_j6", "nico_j6", "maya_j6", "ines_j6", "finales_mvp"]' in source
    for runtime_id, spec in J6_CONVERSATIONS.items():
        assert f'"{runtime_id}": _new_conversation_state' in source
        assert f'"res://data/{spec["file"]}"' in source
        assert f'"{spec["contact"]}"' in source
    assert 'current_day >= 6' in source or 'current_day > 6' in source
    assert '"sarah_j5", "camille_j5", "nico_j5", "maya_j5"' in source
    assert 'current_day == 6' in source and '"sarah_s6a"' in source


def test_t124_conversation_blocks_declares_j6_finale_unlock_chain() -> None:
    config = load_json(BLOCKS_CONFIG)
    assert config["block_order"][-8:] == J6_BLOCK_ORDER
    assert len(config["block_order"]) == 46
    assert len(config["blocks"]) == 46
    assert config["block_order"][-16:-8] == ["sarah_s5a", "camille_c5a", "nico_n5a", "sarah_s5b", "camille_c5b", "maya_m5a", "sarah_s5c", "camille_c5c"]
    for block_id, (conversation_id, start_node, end_nodes, unlock, notification_target) in EXPECTED_J6_BLOCKS.items():
        block = config["blocks"][block_id]
        assert block["conversation_id"] == conversation_id
        assert block["start_node"] == start_node
        assert block["end_nodes"] == end_nodes
        assert block["unlock_on_done"] == unlock
        assert block["notification_target"] == notification_target
        data = load_json(DATA / J6_CONVERSATIONS[conversation_id]["file"])
        ids = {node["id"] for node in data["nodes"]}
        assert start_node in ids
        for node_id in end_nodes:
            assert node_id in ids


def test_t124_validator_covers_j1_to_j6_and_finale_after_integration() -> None:
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
    for runtime_id, spec in J6_CONVERSATIONS.items():
        assert spec["conversation_id"] in report["active_dialogues"]
        assert report["dialogues"][spec["conversation_id"]]["source_copy_match"] is True


if __name__ == "__main__":
    test_t124_j6_and_finale_dialogue_files_are_valid_and_unchanged()
    test_t124_state_declares_j6_finale_day6_and_preserves_j5()
    test_t124_conversation_blocks_declares_j6_finale_unlock_chain()
    test_t124_validator_covers_j1_to_j6_and_finale_after_integration()
    print("T124 J6/finale integration tests OK")
