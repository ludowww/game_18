#!/usr/bin/env python3
"""T148: entry variants must not sound omniscient."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def test_nico_after_sarah_variant_is_suspicion_not_omniscience():
    nico = load("nico_j1_v2_experimental.json")
    nodes = nodes_by_id(nico)
    assert nodes["j1_03_nico_entry_after_sarah_001"]["text"] == (
        "parce que j’ai eu l’impression hier que j’allais finir dans ta version officielle sans avoir lu le script"
    )
    all_text = "\n".join(str(node.get("text", "")) for node in nico["nodes"])
    assert "si mon nom est déjà dans la phrase" not in all_text
    assert "version officielle sans avoir lu le script" in all_text
    assert "bah là, tu m’y mets déjà un peu." in all_text


def test_nico_after_sarah_single_reply_confirms_player_puts_nico_in_story():
    nico = load("nico_j1_v2_experimental.json")
    nodes = nodes_by_id(nico)
    single = nodes["j1_03_nico_single_reply_after_sarah_001"]
    assert single["type"] == "choice"
    assert len(single["choices"]) == 1
    option = single["choices"][0]
    player = nodes[option["next"]]
    assert option["text"] == "Je voulais pas t’y mettre plus que ça."
    assert player["sender"] == "player"
    assert player["text"] == option["text"]
    assert player["next"] == "j1_03_nico_entry_after_sarah_002"
    assert "effects" not in player
    assert "choices" not in player


def test_known_omniscient_phrases_are_absent_from_j1_v2_entry_texts():
    forbidden = [
        "si mon nom est déjà dans la phrase",
        "tu as déjà dit",
        "Sarah m’a tout dit",
        "Je sais que tu as parlé à Camille",
        "Tu m’as utilisé comme alibi",
        "Maya a une preuve",
    ]
    for path in DATA.glob("*j1_v2_experimental.json"):
        data = load(path.name)
        text = "\n".join(str(node.get("text", "")) for node in data.get("nodes", []))
        for phrase in forbidden:
            assert phrase not in text, f"{path.name}: omniscient phrase still present: {phrase}"


if __name__ == "__main__":
    test_nico_after_sarah_variant_is_suspicion_not_omniscience()
    test_nico_after_sarah_single_reply_confirms_player_puts_nico_in_story()
    test_known_omniscient_phrases_are_absent_from_j1_v2_entry_texts()
    print("T148 no omniscient entry variants tests OK")
