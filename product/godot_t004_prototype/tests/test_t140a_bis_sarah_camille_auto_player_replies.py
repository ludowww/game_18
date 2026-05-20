from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

EXPECTED_PLAYER_NODES = {
    "sarah_j1_v2_experimental.json": [
        "j1_01_sarah_auto_player_default_001",
        "j1_01_sarah_auto_player_first_reply_001",
        "j1_01_sarah_auto_player_after_camille_001",
    ],
    "camille_j1_v2_experimental.json": [
        "j1_02_camille_auto_player_default_001",
        "j1_02_camille_auto_player_first_reply_001",
        "j1_02_camille_auto_player_after_sarah_001",
    ],
}

CHOICE_NODES = {
    "sarah_j1_v2_experimental.json": "j1_01_choice_version_sarah",
    "camille_j1_v2_experimental.json": "j1_02_choice_camille_dehors",
}

EXPECTED_CHOICE_IDS = {
    "sarah_j1_v2_experimental.json": [
        "j1_01_needed_air",
        "j1_01_nico_alibi",
        "j1_01_camille_minimized",
        "j1_01_vulnerable",
        "j1_01_silence",
    ],
    "camille_j1_v2_experimental.json": [
        "j1_02_admit_tension",
        "j1_02_respect_boundary",
        "j1_02_minimize",
        "j1_02_early_desire",
        "j1_02_uncertain",
        "j1_02_silence",
    ],
}


def load_json(filename: str) -> dict:
    return json.loads((DATA / filename).read_text(encoding="utf-8"))


def node_map(data: dict) -> dict:
    return {node["id"]: node for node in data["nodes"]}


def reaches_choice(start_node: str, nodes: dict, choice_node: str) -> bool:
    current = start_node
    seen = set()
    while current and current not in seen:
        if current == choice_node:
            return True
        seen.add(current)
        current = nodes[current].get("next", "")
    return False


def test_t140a_bis_auto_player_reply_nodes_exist_and_are_neutral_messages() -> None:
    for filename, node_ids in EXPECTED_PLAYER_NODES.items():
        nodes = node_map(load_json(filename))
        for node_id in node_ids:
            assert node_id in nodes
            node = nodes[node_id]
            assert node["type"] == "message"
            assert node["sender"] == "player"
            assert isinstance(node.get("text"), str) and node["text"]
            assert "delay" in node
            assert "next" in node
            assert "effects" not in node
            assert "choices" not in node


def test_t140a_bis_choice_ids_and_effects_remain_unchanged() -> None:
    for filename, choice_node in CHOICE_NODES.items():
        data = load_json(filename)
        choice = node_map(data)[choice_node]
        assert [item["id"] for item in choice["choices"]] == EXPECTED_CHOICE_IDS[filename]
        for item in choice["choices"]:
            assert "effects" in item
            assert "flags" in item["effects"]


def test_t140a_bis_entry_variants_still_converge_to_central_choice_nodes() -> None:
    for filename, choice_node in CHOICE_NODES.items():
        data = load_json(filename)
        nodes = node_map(data)
        for variant in data["entry_variants"]:
            assert reaches_choice(variant["start_node"], nodes, choice_node), variant["id"]


if __name__ == "__main__":
    test_t140a_bis_auto_player_reply_nodes_exist_and_are_neutral_messages()
    test_t140a_bis_choice_ids_and_effects_remain_unchanged()
    test_t140a_bis_entry_variants_still_converge_to_central_choice_nodes()
    print("T140A-bis Sarah/Camille automatic player replies tests OK")
