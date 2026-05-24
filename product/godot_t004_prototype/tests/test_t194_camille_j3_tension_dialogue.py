#!/usr/bin/env python3
"""T194: Camille J3 tension scene replaces placeholder with structured dialogue."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CAMILLE = json.loads((DATA / "camille_j3_v2_experimental.json").read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in CAMILLE["nodes"]}
ENTRY_VARIANTS = ["after_assumed_tension", "after_clear_boundary", "after_minimized_again", "after_refuge_attempt", "default"]
CENTRAL_CHOICES = ["j3_03_camille_recognize_without_using", "j3_03_camille_keep_boundary", "j3_03_camille_reopen_tension", "j3_03_camille_close_down"]
OTHER_UNWRITTEN_J3 = []

def test_t194_placeholder_removed_and_entry_variants_exact():
    serialized = json.dumps(CAMILLE, ensure_ascii=False)
    assert "[J3 placeholder Camille après-midi]" not in serialized
    assert [v["id"] for v in CAMILLE["entry_variants"]] == ENTRY_VARIANTS

def test_t194_entry_conditions_and_start_nodes_exist():
    variants = {v["id"]: v for v in CAMILLE["entry_variants"]}
    assert variants["after_assumed_tension"]["conditions"] == {"flags": ["j2_camille_assumed_tension"]}
    assert variants["after_clear_boundary"]["conditions"] == {"flags": ["j2_camille_clear_boundary"]}
    assert variants["after_minimized_again"]["conditions"] == {"flags": ["j2_camille_minimized_again"]}
    assert variants["after_refuge_attempt"]["conditions"] == {"flags": ["j2_camille_refuge_attempt"]}
    assert variants["default"]["conditions"] == {}
    for variant in variants.values():
        assert variant["start_node"] in NODES

def follow_path(start):
    seen=[]; current=start
    while current:
        assert current in NODES, f"missing {current}"
        assert current not in seen, f"loop {current}"
        seen.append(current)
        if current == "j3_03_choice_camille_line": break
        current = NODES[current].get("next", "")
    return seen

def test_t194_entry_variants_converge_to_central_choice():
    for variant in CAMILLE["entry_variants"]:
        assert "j3_03_choice_camille_line" in follow_path(variant["start_node"])

def test_t194_single_replies_have_one_choice_no_effects_matching_player_text():
    singles = [n for n in CAMILLE["nodes"] if "_single_reply_" in n["id"]]
    assert len(singles) == 5
    for node in singles:
        assert node["type"] == "choice"
        assert "effects" not in node
        assert len(node["choices"]) == 1
        opt = node["choices"][0]
        player = NODES[opt["next"]]
        assert player["sender"] == "player"
        assert player["text"] == opt["text"]
        assert "effects" not in player

def test_t194_central_choice_has_four_effectful_choices_with_j3_flags():
    central = NODES["j3_03_choice_camille_line"]
    assert central["type"] == "choice"
    assert central["text"] == "Que répondre à Camille ?"
    assert [c["id"] for c in central["choices"]] == CENTRAL_CHOICES
    for choice in central["choices"]:
        effects = choice.get("effects")
        assert isinstance(effects, dict)
        assert any(flag.startswith("j3_camille_") for flag in effects.get("flags", []))
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]

def test_t194_each_central_branch_ends_on_end_node():
    for choice in NODES["j3_03_choice_camille_line"]["choices"]:
        current = choice["next"]; seen=set()
        while current:
            assert current in NODES
            assert current not in seen
            seen.add(current)
            node=NODES[current]
            if node["type"] == "end": break
            current=node.get("next", "")
        assert NODES[current]["type"] == "end"

def test_t194_no_media_and_no_forbidden_names_in_camille_text():
    assert all(node.get("type") != "media" for node in CAMILLE["nodes"])
    camille_text = "\n".join(n.get("text", "") for n in CAMILLE["nodes"] if n.get("sender") == "camille")
    for forbidden in ["Sarah", "Nico", "Maya", "Inès"]:
        assert forbidden not in camille_text

def test_t194_other_unwritten_j3_conversations_remain_skeletons():
    for name in OTHER_UNWRITTEN_J3:
        data = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert len(data["nodes"]) == 2
        assert len(data["entry_variants"]) == 1
        assert data["entry_variants"][0]["id"] == "default"
        assert "placeholder" in json.dumps(data, ensure_ascii=False).lower()

if __name__ == "__main__":
    test_t194_placeholder_removed_and_entry_variants_exact()
    test_t194_entry_conditions_and_start_nodes_exist()
    test_t194_entry_variants_converge_to_central_choice()
    test_t194_single_replies_have_one_choice_no_effects_matching_player_text()
    test_t194_central_choice_has_four_effectful_choices_with_j3_flags()
    test_t194_each_central_branch_ends_on_end_node()
    test_t194_no_media_and_no_forbidden_names_in_camille_text()
    test_t194_other_unwritten_j3_conversations_remain_skeletons()
    print("T194 Camille J3 tension dialogue tests OK")
