#!/usr/bin/env python3
"""T184: J2 choices must not create magical knowledge or off-screen effects."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

J2_FILES = [
    "sarah_j2_v2_experimental.json",
    "nico_j2_v2_experimental.json",
    "camille_j2_v2_experimental.json",
    "maya_j2_v2_experimental.json",
    "ines_j2_v2_experimental.json",
]


def load(filename: str) -> dict:
    return json.loads((DATA / filename).read_text(encoding="utf-8"))


def nodes(data: dict) -> dict:
    return {node["id"]: node for node in data["nodes"]}


def find_choice(data: dict, choice_id: str) -> dict:
    for node in data["nodes"]:
        for choice in node.get("choices", []):
            if choice.get("id") == choice_id:
                return choice
    raise AssertionError(f"missing choice {choice_id}")


def player_text_for_choice(data: dict, choice_id: str) -> str:
    choice = find_choice(data, choice_id)
    return str(nodes(data)[choice["next"]]["text"])


def test_t184_sarah_need_time_uses_unpaid_later_not_tonight() -> None:
    data = load("sarah_j2_v2_experimental.json")
    choice = find_choice(data, "j2_01_sarah_need_time")
    player_text = player_text_for_choice(data, "j2_01_sarah_need_time")
    assert choice["text"] == player_text
    assert "ce soir" not in choice["text"]
    assert "plus tard" in choice["text"]


def test_t184_nico_release_does_not_magically_raise_sarah_trust() -> None:
    data = load("nico_j2_v2_experimental.json")
    choice = find_choice(data, "j2_02_nico_release_him")
    effects = choice["effects"]
    assert "confiance_sarah" not in effects
    assert effects["dette_nico"] == -3
    assert effects["coherence"] == 1
    assert effects["fatigue_emotionnelle"] == -1
    assert effects["flags"] == ["j2_nico_released_from_alibi", "j2_nico_friend_not_tool"]


def test_t184_nico_alibi_entry_stays_hypothetical() -> None:
    text = "\n".join(str(node.get("text", "")) for node in load("nico_j2_v2_experimental.json")["nodes"])
    assert "sans faire semblant de savoir" in text
    assert "si mon prénom doit servir de repère" in text


def test_t184_camille_refuge_targets_camille_not_ines() -> None:
    data = load("camille_j2_v2_experimental.json")
    choice = find_choice(data, "j2_03_camille_seek_refuge")
    effects = choice["effects"]
    assert "fuite_ines" not in effects
    assert effects["tension_camille"] == 2
    assert effects["pression_camille"] == 3
    assert effects["respect_camille"] == -1
    assert effects["culpabilite"] == 1


def test_t184_ines_repair_misstep_is_generic_and_choice_matches_player_node() -> None:
    data = load("ines_j2_v2_experimental.json")
    choice = find_choice(data, "j2_05_ines_repair_misstep")
    expected = "Hier, je crois que je n’ai pas été très clair. Je cherchais peut-être quelqu’un qui me remarque, sans savoir quoi en faire."
    assert choice["text"] == expected
    assert player_text_for_choice(data, "j2_05_ines_repair_misstep") == expected


def test_t184_maya_discretion_is_not_sarah_specific_in_choice_or_response() -> None:
    data = load("maya_j2_v2_experimental.json")
    choice = find_choice(data, "j2_04_maya_ask_discretion")
    player_text = player_text_for_choice(data, "j2_04_maya_ask_discretion")
    assert choice["text"] == player_text
    assert not choice["text"].startswith("Si tu parles à Sarah")
    assert "Si tu en parles à quelqu’un" in choice["text"]
    assert "si j’en parle, ce sera pas pour te coincer" in "\n".join(str(node.get("text", "")) for node in data["nodes"])
    # T184 intentionally keeps this old flag to avoid breaking future dependencies;
    # it may need a later rename to j2_maya_discretion_requested_for_others.
    assert "j2_maya_sarah_protection_named" in find_choice(data, "j2_04_maya_ask_discretion")["effects"]["flags"]


def test_t184_all_j2_choice_texts_match_player_nodes() -> None:
    for filename in J2_FILES:
        data = load(filename)
        by_id = nodes(data)
        for node in data["nodes"]:
            for choice in node.get("choices", []):
                next_id = choice.get("next")
                if not next_id or next_id not in by_id:
                    continue
                next_node = by_id[next_id]
                if str(next_node.get("speaker", "player")) == "system":
                    continue
                assert choice.get("text") == next_node.get("text"), (filename, choice.get("id"), next_id)


if __name__ == "__main__":
    test_t184_sarah_need_time_uses_unpaid_later_not_tonight()
    test_t184_nico_release_does_not_magically_raise_sarah_trust()
    test_t184_nico_alibi_entry_stays_hypothetical()
    test_t184_camille_refuge_targets_camille_not_ines()
    test_t184_ines_repair_misstep_is_generic_and_choice_matches_player_node()
    test_t184_maya_discretion_is_not_sarah_specific_in_choice_or_response()
    test_t184_all_j2_choice_texts_match_player_nodes()
    print("T184 J2 choice/effect coherence tests OK")
