#!/usr/bin/env python3
"""T180: J2 dialogue polish stays text-only in spirit and preserves choice/player echoes."""

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


def test_t180_key_reframe_phrases_are_present():
    checks = {
        "sarah_j2_v2_experimental.json": [
            "J’ai l’impression qu’on devient très doués pour éviter les vraies phrases.",
            "Quand tu demandes du temps, moi je reste avec ce que je ne sais pas.",
        ],
        "camille_j2_v2_experimental.json": [
            "Je veux juste pas être le moment que tu utilises quand ça t’arrange.",
            "Je ne veux pas être la pause qui te permet d’éviter le reste.",
        ],
        "maya_j2_v2_experimental.json": [
            "et peut-être que je me trompe.",
            "Si tu en parles à quelqu’un, fais-le parce que tu t’inquiètes. Pas pour me mettre au pied du mur.",
        ],
        "ines_j2_v2_experimental.json": [
            "Je vais pas très bien. Mais je veux te parler sans me cacher derrière toi.",
            "je préfère ça à quelque chose de doux mais pas clair.",
        ],
    }
    for filename, expected_phrases in checks.items():
        serialized = json.dumps(load(filename), ensure_ascii=False)
        for phrase in expected_phrases:
            assert phrase in serialized, f"{phrase!r} missing from {filename}"


def test_t180_old_overwritten_phrases_are_absent():
    old_phrases = {
        "sarah_j2_v2_experimental.json": [
            "J’ai l’impression qu’on devient très doués pour éviter les vrais sons.",
            "Quand tu demandes du temps, moi je reste avec la place vide entre les deux.",
        ],
        "camille_j2_v2_experimental.json": [
            "Je veux juste pas devenir le mot que tu utilises pour éviter les autres.",
            "Je ne veux pas être ton air de secours.",
        ],
        "maya_j2_v2_experimental.json": [
            "elle rappelle qu’il y avait une place bizarre dans l’image.",
            "Dis-moi franchement ce que tu penses avoir compris.",
        ],
        "ines_j2_v2_experimental.json": [
            "Je vais pas très bien. Mais je veux te répondre sans faire de toi une échappatoire.",
            "ça me va mieux qu’une douceur qui ne sait pas où elle va.",
        ],
    }
    for filename, phrases in old_phrases.items():
        serialized = json.dumps(load(filename), ensure_ascii=False)
        for phrase in phrases:
            assert phrase not in serialized, f"{phrase!r} still present in {filename}"


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


def test_j1_validator_stays_green():
    result = subprocess.run(
        ["python3", "tools/validate_j1_v2_experimental.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


if __name__ == "__main__":
    test_t180_key_reframe_phrases_are_present()
    test_t180_old_overwritten_phrases_are_absent()
    test_all_j2_choice_texts_match_player_echo_nodes()
    test_j1_validator_stays_green()
    print("T180 J2 story reframe text polish tests OK")
