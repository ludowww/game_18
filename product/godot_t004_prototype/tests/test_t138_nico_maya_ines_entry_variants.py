from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

EXPECTED = {
    "nico_j1_v2_experimental.json": {
        "default_start": "j1_03_nico_001",
        "choice_node": "j1_03_choice_nico_version",
        "variant_ids": [
            "first_reply_nico",
            "after_sarah_nico_version",
            "after_camille_confusion",
            "late_or_delayed",
            "default",
        ],
    },
    "maya_j1_v2_experimental.json": {
        "default_start": "j1_04_maya_001",
        "choice_node": "j1_04_choice_maya_pique",
        "variant_ids": [
            "first_reply_maya",
            "after_sarah",
            "after_camille",
            "late_or_delayed",
            "default",
        ],
    },
    "ines_j1_v2_experimental.json": {
        "default_start": "j1_05_ines_001",
        "choice_node": "j1_05_choice_ines_faille",
        "variant_ids": [
            "first_reply_ines",
            "after_conflict",
            "late_or_delayed",
            "default",
        ],
    },
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
        node = nodes[current]
        current = node.get("next", "")
    return False


def test_t138_nico_maya_ines_jsons_define_expected_entry_variants_in_order() -> None:
    for filename, expected in EXPECTED.items():
        data = load_json(filename)
        variants = data.get("entry_variants")
        assert isinstance(variants, list)
        assert [variant.get("id") for variant in variants] == expected["variant_ids"]


def test_t138_each_entry_variant_has_conditions_and_existing_start_node() -> None:
    for filename in EXPECTED:
        data = load_json(filename)
        nodes = node_map(data)
        for variant in data["entry_variants"]:
            assert isinstance(variant.get("id"), str) and variant["id"]
            assert isinstance(variant.get("conditions"), dict)
            assert isinstance(variant.get("start_node"), str) and variant["start_node"]
            assert variant["start_node"] in nodes


def test_t138_default_variant_points_to_current_start_node() -> None:
    for filename, expected in EXPECTED.items():
        data = load_json(filename)
        default = next(variant for variant in data["entry_variants"] if variant["id"] == "default")
        assert data["start_node"] == expected["default_start"]
        assert default["start_node"] == data["start_node"]
        assert default["conditions"] == {}


def test_t138_all_entry_variants_converge_to_existing_choice_nodes() -> None:
    for filename, expected in EXPECTED.items():
        data = load_json(filename)
        nodes = node_map(data)
        assert expected["choice_node"] in nodes
        assert nodes[expected["choice_node"]]["type"] == "choice"
        for variant in data["entry_variants"]:
            assert reaches_choice(variant["start_node"], nodes, expected["choice_node"]), variant["id"]


if __name__ == "__main__":
    test_t138_nico_maya_ines_jsons_define_expected_entry_variants_in_order()
    test_t138_each_entry_variant_has_conditions_and_existing_start_node()
    test_t138_default_variant_points_to_current_start_node()
    test_t138_all_entry_variants_converge_to_existing_choice_nodes()
    print("T138 J1 V2 Nico/Maya/Inès entry variants tests OK")
