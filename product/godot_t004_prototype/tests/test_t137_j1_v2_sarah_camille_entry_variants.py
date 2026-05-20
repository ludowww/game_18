from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

EXPECTED = {
    "sarah_j1_v2_experimental.json": {
        "default_start": "j1_01_sarah_001",
        "choice_node": "j1_01_choice_version_sarah",
        "variant_ids": {
            "default",
            "first_reply_sarah",
            "after_camille_first",
            "after_nico_first",
            "late_or_delayed",
        },
    },
    "camille_j1_v2_experimental.json": {
        "default_start": "j1_02_camille_001",
        "choice_node": "j1_02_choice_camille_dehors",
        "variant_ids": {
            "default",
            "first_reply_camille",
            "after_sarah_first",
            "late_or_left_open",
            "after_nico_first",
        },
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


def test_t137_sarah_and_camille_jsons_define_expected_entry_variants() -> None:
    for filename, expected in EXPECTED.items():
        data = load_json(filename)
        variants = data.get("entry_variants")
        assert isinstance(variants, list)
        assert {variant.get("id") for variant in variants} == expected["variant_ids"]


def test_t137_each_entry_variant_has_conditions_and_existing_start_node() -> None:
    for filename in EXPECTED:
        data = load_json(filename)
        nodes = node_map(data)
        for variant in data["entry_variants"]:
            assert isinstance(variant.get("id"), str) and variant["id"]
            assert isinstance(variant.get("conditions"), dict)
            assert isinstance(variant.get("start_node"), str) and variant["start_node"]
            assert variant["start_node"] in nodes


def test_t137_default_variant_points_to_current_start_node() -> None:
    for filename, expected in EXPECTED.items():
        data = load_json(filename)
        default = next(variant for variant in data["entry_variants"] if variant["id"] == "default")
        assert data["start_node"] == expected["default_start"]
        assert default["start_node"] == data["start_node"]
        assert default["conditions"] == {}


def test_t137_all_entry_variants_converge_to_existing_choice_nodes() -> None:
    for filename, expected in EXPECTED.items():
        data = load_json(filename)
        nodes = node_map(data)
        assert expected["choice_node"] in nodes
        assert nodes[expected["choice_node"]]["type"] == "choice"
        for variant in data["entry_variants"]:
            assert reaches_choice(variant["start_node"], nodes, expected["choice_node"]), variant["id"]


if __name__ == "__main__":
    test_t137_sarah_and_camille_jsons_define_expected_entry_variants()
    test_t137_each_entry_variant_has_conditions_and_existing_start_node()
    test_t137_default_variant_points_to_current_start_node()
    test_t137_all_entry_variants_converge_to_existing_choice_nodes()
    print("T137 J1 V2 Sarah/Camille entry variants tests OK")
