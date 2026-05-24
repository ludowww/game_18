#!/usr/bin/env python3
"""T196: Inès J3 evening scene replaces placeholder with structured dialogue."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
INES = json.loads((DATA / "ines_j3_v2_experimental.json").read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in INES["nodes"]}
ENTRY_VARIANTS = ["after_careful_opening", "after_boundary", "after_refuge", "after_repair", "default"]
CENTRAL_CHOICES = ["j3_05_ines_clear_presence", "j3_05_ines_keep_soft_distance", "j3_05_ines_seek_refuge_again", "j3_05_ines_step_back"]

def test_t196_placeholder_removed_and_entry_variants_exact():
    serialized = json.dumps(INES, ensure_ascii=False)
    assert "[J3 placeholder Inès soir]" not in serialized
    assert [v["id"] for v in INES["entry_variants"]] == ENTRY_VARIANTS

def test_t196_entry_conditions_and_start_nodes_exist():
    variants = {v["id"]: v for v in INES["entry_variants"]}
    assert variants["after_careful_opening"]["conditions"] == {"flags": ["j2_ines_careful_opening"]}
    assert variants["after_boundary"]["conditions"] == {"flags": ["j2_ines_boundary_kept"]}
    assert variants["after_refuge"]["conditions"] == {"flags": ["j2_ines_refuge_attempt"]}
    assert variants["after_repair"]["conditions"] == {"flags": ["j2_ines_repair_misstep"]}
    assert variants["default"]["conditions"] == {}
    for variant in variants.values():
        assert variant["start_node"] in NODES

def follow_path(start):
    seen=[]; current=start
    while current:
        assert current in NODES, f"missing {current}"
        assert current not in seen, f"loop {current}"
        seen.append(current)
        if current == "j3_05_choice_ines_evening": break
        current = NODES[current].get("next", "")
    return seen

def test_t196_entry_variants_converge_to_central_choice():
    for variant in INES["entry_variants"]:
        assert "j3_05_choice_ines_evening" in follow_path(variant["start_node"])

def test_t196_single_replies_have_one_choice_no_effects_matching_player_text():
    singles = [n for n in INES["nodes"] if "_single_reply_" in n["id"]]
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

def test_t196_central_choice_has_four_effectful_choices_with_j3_flags():
    central = NODES["j3_05_choice_ines_evening"]
    assert central["type"] == "choice"
    assert central["text"] == "Que répondre à Inès ?"
    assert [c["id"] for c in central["choices"]] == CENTRAL_CHOICES
    for choice in central["choices"]:
        effects = choice.get("effects")
        assert isinstance(effects, dict)
        assert any(flag.startswith("j3_ines_") for flag in effects.get("flags", []))
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]

def test_t196_each_central_branch_ends_on_end_node():
    for choice in NODES["j3_05_choice_ines_evening"]["choices"]:
        current = choice["next"]; seen=set()
        while current:
            assert current in NODES
            assert current not in seen
            seen.add(current)
            node=NODES[current]
            if node["type"] == "end": break
            current=node.get("next", "")
        assert NODES[current]["type"] == "end"

def test_t196_no_media_forbidden_names_or_forbidden_knowledge():
    assert all(node.get("type") != "media" for node in INES["nodes"])
    ines_text = "\n".join(n.get("text", "") for n in INES["nodes"] if n.get("sender") == "ines")
    for forbidden in ["Sarah", "Nico", "Camille", "Maya", "je sais ce qui s’est passé", "le groupe", "photo"]:
        assert forbidden not in ines_text

if __name__ == "__main__":
    test_t196_placeholder_removed_and_entry_variants_exact()
    test_t196_entry_conditions_and_start_nodes_exist()
    test_t196_entry_variants_converge_to_central_choice()
    test_t196_single_replies_have_one_choice_no_effects_matching_player_text()
    test_t196_central_choice_has_four_effectful_choices_with_j3_flags()
    test_t196_each_central_branch_ends_on_end_node()
    test_t196_no_media_forbidden_names_or_forbidden_knowledge()
    print("T196 Inès J3 evening dialogue tests OK")
