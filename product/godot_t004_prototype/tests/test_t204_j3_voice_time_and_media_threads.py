#!/usr/bin/env python3
"""T204: J3 voice/time polish and media mini-discussion chains."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
J3_FILES = [
    "sarah_j3_v2_experimental.json",
    "nico_j3_v2_experimental.json",
    "camille_j3_v2_experimental.json",
    "maya_j3_v2_experimental.json",
    "ines_j3_v2_experimental.json",
]
NEW_SINGLE_REPLIES = {
    "sarah_j3_v2_experimental.json": ["j3_01_sarah_single_reply_photo_morning_001"],
    "nico_j3_v2_experimental.json": ["j3_02_nico_single_reply_life_photo_001"],
}


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def nodes(name: str) -> dict:
    return {node["id"]: node for node in load(name)["nodes"]}


def all_text() -> str:
    return "\n".join(json.dumps(load(name), ensure_ascii=False) for name in J3_FILES)


def assert_contains(name: str, *texts: str) -> None:
    serialized = json.dumps(load(name), ensure_ascii=False)
    for text in texts:
        assert text in serialized, f"missing in {name}: {text}"


def test_t204_repetition_markers_reduced() -> None:
    text = all_text()
    for forbidden in [
        "j’ai repensé à ta phrase",
        "j’ai repensé à ce que tu m’as dit",
        "J’ai repensé à ta limite",
        "J’ai repensé à ton histoire de respiration",
    ]:
        assert forbidden not in text
    assert text.lower().count("j’ai repensé") <= 2


def test_t204_character_signatures_are_present() -> None:
    assert_contains("sarah_j3_v2_experimental.json", "J’ai laissé ta tasse sur la table.", "J’ai fait le café avant d’écrire.")
    assert_contains("nico_j3_v2_experimental.json", "update : je suis vivant. émotionnellement discutable, mais vivant.", "ce soir je lance la console.")
    assert_contains("camille_j3_v2_experimental.json", "pause de trois minutes.", "ta limite tient toujours ?", "je suis censée bosser, donc évidemment je t’écris.")
    assert_contains("maya_j3_v2_experimental.json", "bon. j’ai fait semblant de rien voir pendant presque 24h.", "j’ai réussi à ne pas en faire un sujet de groupe.")
    assert_contains("ines_j3_v2_experimental.json", "j’ai écrit trois messages et j’en ai effacé deux.", "j’ai relu ton message sans savoir quoi en faire.")


def test_t204_sarah_photo_is_a_mini_discussion() -> None:
    n = nodes("sarah_j3_v2_experimental.json")
    assert n["j3_01_sarah_media_morning_trace_001"]["next"] == "j3_01_sarah_single_reply_photo_morning_001"
    single = n["j3_01_sarah_single_reply_photo_morning_001"]
    player = n["j3_01_sarah_player_photo_morning_001"]
    assert single["type"] == "choice"
    assert player["type"] == "message"
    assert player["next"] == "j3_01_sarah_response_actions_photo_001"
    assert n["j3_01_sarah_response_actions_photo_001"]["text"] == "Rien d’énorme."
    assert n["j3_01_sarah_response_actions_photo_002"]["next"] == "j3_01_sarah_response_actions_photo_003"
    assert n["j3_01_sarah_response_actions_photo_003"]["next"] == "j3_01_sarah_response_actions_003"


def test_t204_nico_photo_is_a_mini_discussion() -> None:
    n = nodes("nico_j3_v2_experimental.json")
    assert n["j3_02_nico_media_social_life_001"]["next"] == "j3_02_nico_single_reply_life_photo_001"
    single = n["j3_02_nico_single_reply_life_photo_001"]
    player = n["j3_02_nico_player_life_photo_001"]
    assert single["type"] == "choice"
    assert player["type"] == "message"
    assert player["next"] == "j3_02_nico_response_life_photo_001"
    assert n["j3_02_nico_response_life_photo_001"]["text"] == "ah."
    assert n["j3_02_nico_response_life_photo_002"]["next"] == "j3_02_nico_response_life_photo_003"
    assert n["j3_02_nico_response_life_photo_004"]["next"] == "j3_02_nico_response_life_teased_004"


def test_t204_new_single_replies_are_safe_and_mirrored() -> None:
    for name, ids in NEW_SINGLE_REPLIES.items():
        n = nodes(name)
        for node_id in ids:
            node = n[node_id]
            assert node["type"] == "choice"
            assert "effects" not in node
            assert len(node["choices"]) == 1
            choice = node["choices"][0]
            player = n[choice["next"]]
            assert player["sender"] == "player"
            assert "effects" not in player
            assert player["text"] == choice["text"]
            assert node["next"] == choice["next"]


def test_t204_media_counts_are_unchanged() -> None:
    expected = {
        "sarah_j3_v2_experimental.json": ["j3_01_sarah_media_morning_trace_001"],
        "nico_j3_v2_experimental.json": ["j3_02_nico_media_social_life_001"],
        "camille_j3_v2_experimental.json": [],
        "maya_j3_v2_experimental.json": [],
        "ines_j3_v2_experimental.json": [],
    }
    for name, ids in expected.items():
        assert [node["id"] for node in load(name)["nodes"] if node.get("type") == "media"] == ids


if __name__ == "__main__":
    test_t204_repetition_markers_reduced()
    test_t204_character_signatures_are_present()
    test_t204_sarah_photo_is_a_mini_discussion()
    test_t204_nico_photo_is_a_mini_discussion()
    test_t204_new_single_replies_are_safe_and_mirrored()
    test_t204_media_counts_are_unchanged()
    print("T204 J3 voice/time/media thread tests OK")
