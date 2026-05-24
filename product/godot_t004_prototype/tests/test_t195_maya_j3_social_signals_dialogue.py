#!/usr/bin/env python3
"""T195: Maya J3 social signals scene replaces placeholder with structured dialogue."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
MAYA = json.loads((DATA / "maya_j3_v2_experimental.json").read_text(encoding="utf-8"))
NODES = {node["id"]: node for node in MAYA["nodes"]}
ENTRY_VARIANTS = ["after_social_read_opened", "after_malaise_admitted", "after_defensive", "after_discretion", "default"]
CENTRAL_CHOICES = ["j3_04_maya_ask_what_changed", "j3_04_maya_keep_group_boundary", "j3_04_maya_minimize_signals", "j3_04_maya_ask_if_others_notice"]
OTHER_UNWRITTEN_J3 = ["ines_j3_v2_experimental.json"]

def test_t195_placeholder_removed_and_entry_variants_exact():
    serialized = json.dumps(MAYA, ensure_ascii=False)
    assert "[J3 placeholder Maya après-midi]" not in serialized
    assert [v["id"] for v in MAYA["entry_variants"]] == ENTRY_VARIANTS

def test_t195_entry_conditions_and_start_nodes_exist():
    variants = {v["id"]: v for v in MAYA["entry_variants"]}
    assert variants["after_social_read_opened"]["conditions"] == {"flags": ["j2_maya_social_read_opened"]}
    assert variants["after_malaise_admitted"]["conditions"] == {"flags": ["j2_maya_malaise_admitted"]}
    assert variants["after_defensive"]["conditions"] == {"flags": ["j2_maya_defensive"]}
    assert variants["after_discretion"]["conditions"] == {"flags": ["j2_maya_discretion_requested"]}
    assert variants["default"]["conditions"] == {}
    for variant in variants.values():
        assert variant["start_node"] in NODES

def follow_path(start):
    seen=[]; current=start
    while current:
        assert current in NODES, f"missing {current}"
        assert current not in seen, f"loop {current}"
        seen.append(current)
        if current == "j3_04_choice_maya_signals": break
        current = NODES[current].get("next", "")
    return seen

def test_t195_entry_variants_converge_to_central_choice():
    for variant in MAYA["entry_variants"]:
        assert "j3_04_choice_maya_signals" in follow_path(variant["start_node"])

def test_t195_single_replies_have_one_choice_no_effects_matching_player_text():
    singles = [n for n in MAYA["nodes"] if "_single_reply_" in n["id"]]
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

def test_t195_central_choice_has_four_effectful_choices_with_j3_flags():
    central = NODES["j3_04_choice_maya_signals"]
    assert central["type"] == "choice"
    assert central["text"] == "Que répondre à Maya ?"
    assert [c["id"] for c in central["choices"]] == CENTRAL_CHOICES
    for choice in central["choices"]:
        effects = choice.get("effects")
        assert isinstance(effects, dict)
        assert any(flag.startswith("j3_maya_") for flag in effects.get("flags", []))
        player = NODES[choice["next"]]
        assert player["sender"] == "player"
        assert player["text"] == choice["text"]

def test_t195_each_central_branch_ends_on_end_node():
    for choice in NODES["j3_04_choice_maya_signals"]["choices"]:
        current = choice["next"]; seen=set()
        while current:
            assert current in NODES
            assert current not in seen
            seen.add(current)
            node=NODES[current]
            if node["type"] == "end": break
            current=node.get("next", "")
        assert NODES[current]["type"] == "end"

def test_t195_no_media_forbidden_names_or_detective_certainty():
    assert all(node.get("type") != "media" for node in MAYA["nodes"])
    maya_text = "\n".join(n.get("text", "") for n in MAYA["nodes"] if n.get("sender") == "maya")
    for forbidden in ["Sarah", "Nico", "Camille", "Inès", "preuve absolue", "je sais tout", "j’ai tout compris"]:
        assert forbidden not in maya_text

def test_t195_other_unwritten_j3_conversations_remain_skeletons():
    for name in OTHER_UNWRITTEN_J3:
        data = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert len(data["nodes"]) == 2
        assert len(data["entry_variants"]) == 1
        assert data["entry_variants"][0]["id"] == "default"
        assert "placeholder" in json.dumps(data, ensure_ascii=False).lower()

if __name__ == "__main__":
    test_t195_placeholder_removed_and_entry_variants_exact()
    test_t195_entry_conditions_and_start_nodes_exist()
    test_t195_entry_variants_converge_to_central_choice()
    test_t195_single_replies_have_one_choice_no_effects_matching_player_text()
    test_t195_central_choice_has_four_effectful_choices_with_j3_flags()
    test_t195_each_central_branch_ends_on_end_node()
    test_t195_no_media_forbidden_names_or_detective_certainty()
    test_t195_other_unwritten_j3_conversations_remain_skeletons()
    print("T195 Maya J3 social signals dialogue tests OK")
