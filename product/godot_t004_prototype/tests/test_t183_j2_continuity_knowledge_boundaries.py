#!/usr/bin/env python3
"""T183: J2 continuity fixes preserve character knowledge boundaries."""

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

FILES = [
    "sarah_j2_v2_experimental.json",
    "nico_j2_v2_experimental.json",
    "camille_j2_v2_experimental.json",
    "maya_j2_v2_experimental.json",
    "ines_j2_v2_experimental.json",
]


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def nodes_by_id(data):
    return {node["id"]: node for node in data["nodes"]}


def serialized(name):
    return json.dumps(load(name), ensure_ascii=False)


def test_sarah_nico_entry_no_longer_implies_private_nico_answer():
    data = load("sarah_j2_v2_experimental.json")
    nodes = nodes_by_id(data)
    assert nodes["j2_01_sarah_single_reply_after_nico_001"]["choices"][0]["text"] == "À Nico ?"
    assert nodes["j2_01_sarah_player_after_nico_001"]["text"] == "À Nico ?"
    assert nodes["j2_01_sarah_entry_after_nico_002"]["text"] == "À la place qu’il prend dans ton histoire."
    assert nodes["j2_01_sarah_entry_after_nico_003"]["text"] == "Je ne sais pas ce qu’il dirait, et c’est bien ça qui me gêne."
    assert nodes["j2_01_sarah_entry_after_nico_004"]["text"] == "Tu m’as donné un prénom, mais pas vraiment une réponse."

    text = serialized("sarah_j2_v2_experimental.json")
    assert "Qu’est-ce qu’il a dit ?" not in text
    assert "Pas assez pour m’aider." not in text
    assert "Assez pour que je sente qu’il faisait attention à chaque mot." not in text


def test_nico_alibi_entry_stays_on_uncertainty_not_magic_knowledge():
    nodes = nodes_by_id(load("nico_j2_v2_experimental.json"))
    assert nodes["j2_02_nico_entry_alibi_used_002"]["text"] == "je vais te poser une question sans faire semblant de savoir."
    assert nodes["j2_02_nico_entry_alibi_used_003"]["text"] == "si mon prénom doit servir de repère à quelqu’un, j’aimerais l’apprendre par toi."
    assert nodes["j2_02_nico_entry_alibi_used_004"]["text"] == "donc, si elle me demande quelque chose, je réponds quoi ?"
    assert nodes["j2_02_nico_entry_second_cover_003"]["text"] == "mais seulement si personne ne me demande pourquoi je réponds comme si j’avais appris un texte."

    text = serialized("nico_j2_v2_experimental.json")
    assert "mon prénom pouvait devenir une version officielle" not in text
    assert "pourquoi on a tous l’air de réciter" not in text


def test_maya_outputs_remain_impressions_not_proofs():
    nodes = nodes_by_id(load("maya_j2_v2_experimental.json"))
    assert nodes["j2_04_maya_ask_direct_002"]["text"] == "j’ai juste l’impression que tu évites de regarder au même endroit que nous."
    assert nodes["j2_04_end_maya_social_read_opened"]["text"] == "Maya ne prouve rien, mais elle met son impression en mots."
    assert nodes["j2_04_end_maya_sarah_protected"]["text"] == "Maya reste loyale à Sarah, sans transformer son impression en accusation."

    text = serialized("maya_j2_v2_experimental.json")
    assert "tout le monde évite de regarder au même endroit" not in text
    assert "met le malaise en mots" not in text
    assert "transformer le malaise en accusation" not in text


def test_camille_and_ines_stay_centered_on_their_own_knowledge():
    camille = nodes_by_id(load("camille_j2_v2_experimental.json"))
    assert camille["j2_03_camille_entry_boundary_003"]["text"] == "ça m’a évité de me sentir mise de côté au moment où ça devenait trop simple pour toi."
    assert camille["j2_03_camille_entry_boundary_004"]["text"] == "Mais je ne sais toujours pas si tu m’as vraiment protégée, ou si tu as juste trouvé une sortie propre."

    ines = nodes_by_id(load("ines_j2_v2_experimental.json"))
    assert ines["j2_05_ines_open_003"]["text"] == "je veux juste rester quelqu’un, pas seulement un endroit où tu te poses quand ça déborde."
    assert ines["j2_05_ines_refuge_003"]["text"] == "si tu viens ici pour ne pas répondre ailleurs, je crois que je finirai par le sentir."


def test_all_j2_choice_texts_match_player_echo_nodes():
    for filename in FILES:
        data = load(filename)
        nodes = nodes_by_id(data)
        for node in data["nodes"]:
            if node.get("type") != "choice":
                continue
            for choice in node.get("choices", []):
                next_id = choice.get("next", "")
                assert next_id in nodes, f"{filename}: missing next node {next_id}"
                player = nodes[next_id]
                assert player.get("sender") == "player", f"{filename}: {next_id} is not a player node"
                assert player.get("text") == choice.get("text"), f"{filename}: {choice['id']} text mismatch"


def test_previous_j2_tests_and_j1_validator_stay_green():
    commands = [
        ["python3", "tests/test_t181_no_legacy_j2_duplicates_in_experimental_mode.py"],
        ["python3", "tests/test_t180_j2_reframe_text_polish.py"],
        ["python3", "tests/test_t178_ines_j2_calm_fuite_dialogue.py"],
        ["python3", "tests/test_t177_maya_j2_social_dialogue.py"],
        ["python3", "tests/test_t176_camille_j2_tension_dialogue.py"],
        ["python3", "tests/test_t175_nico_j2_alibi_dialogue.py"],
        ["python3", "tests/test_t174_sarah_j2_morning_dialogue.py"],
        ["python3", "tests/test_t173_j2_v2_structure.py"],
        ["python3", "tools/validate_j1_v2_experimental.py"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        assert result.returncode == 0, result.stdout + result.stderr


if __name__ == "__main__":
    test_sarah_nico_entry_no_longer_implies_private_nico_answer()
    test_nico_alibi_entry_stays_on_uncertainty_not_magic_knowledge()
    test_maya_outputs_remain_impressions_not_proofs()
    test_camille_and_ines_stay_centered_on_their_own_knowledge()
    test_all_j2_choice_texts_match_player_echo_nodes()
    test_previous_j2_tests_and_j1_validator_stay_green()
    print("T183 J2 continuity knowledge boundary tests OK")
