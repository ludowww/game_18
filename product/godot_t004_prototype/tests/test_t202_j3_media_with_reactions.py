#!/usr/bin/env python3
"""T202: J3 media nodes include safe assets and follow-up reactions."""

import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ASSETS = ROOT / "assets" / "media" / "j3_v2"

SARAH_ASSET = "res://assets/media/j3_v2/sarah_trace_matin_j3.png"
NICO_ASSET = "res://assets/media/j3_v2/nico_sortie_floue_j3.png"

J1_J2_MEDIA_FILES = [
    "maya_j1_v2_experimental.json",
    "nico_respiration_j1_v2_experimental.json",
    "sarah_meal_j1_v2_experimental.json",
    "camille_j2_v2_experimental.json",
    "ines_j2_v2_experimental.json",
    "maya_j2_v2_experimental.json",
]


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def nodes(name: str) -> dict:
    return {node["id"]: node for node in load(name)["nodes"]}


def assert_valid_png(path: Path) -> None:
    raw = path.read_bytes()
    assert raw.startswith(b"\x89PNG\r\n\x1a\n"), path
    width, height = struct.unpack(">II", raw[16:24])
    assert width > 0 and height > 0


def test_t202_j3_assets_exist_and_are_valid_pngs() -> None:
    assert_valid_png(ASSETS / "sarah_trace_matin_j3.png")
    assert_valid_png(ASSETS / "nico_sortie_floue_j3.png")


def test_t202_sarah_media_inserted_with_reaction_chain() -> None:
    n = nodes("sarah_j3_v2_experimental.json")
    media = n["j3_01_sarah_media_morning_trace_001"]
    assert media["type"] == "media"
    assert media["sender"] == "sarah"
    assert media["media_type"] == "image"
    assert media["asset"] == SARAH_ASSET
    assert media["caption"] == "[photo du matin envoyée]"
    assert n["j3_01_sarah_response_actions_002"]["next"] == "j3_01_sarah_media_morning_trace_001"
    assert media["next"] == "j3_01_sarah_response_actions_photo_001"
    assert n["j3_01_sarah_response_actions_photo_001"]["type"] == "message"
    assert n["j3_01_sarah_response_actions_photo_001"]["text"] == "C’est pas grand-chose."
    assert n["j3_01_sarah_response_actions_photo_001"]["next"] == "j3_01_sarah_response_actions_photo_002"
    assert n["j3_01_sarah_response_actions_photo_002"]["type"] == "message"
    assert n["j3_01_sarah_response_actions_photo_002"]["text"] == "Mais c’est le genre de petit truc que je remarque maintenant."
    assert n["j3_01_sarah_response_actions_photo_002"]["next"] == "j3_01_sarah_response_actions_003"


def test_t202_nico_media_inserted_with_reaction_chain() -> None:
    n = nodes("nico_j3_v2_experimental.json")
    media = n["j3_02_nico_media_social_life_001"]
    assert media["type"] == "media"
    assert media["sender"] == "nico"
    assert media["media_type"] == "image"
    assert media["asset"] == NICO_ASSET
    assert media["caption"] == "[photo de sortie envoyée]"
    assert n["j3_02_nico_response_life_teased_003"]["next"] == "j3_02_nico_media_social_life_001"
    assert media["next"] == "j3_02_nico_response_life_photo_001"
    assert n["j3_02_nico_response_life_photo_001"]["type"] == "message"
    assert n["j3_02_nico_response_life_photo_001"]["text"] == "preuve que j’ai une vie. floue, certes."
    assert n["j3_02_nico_response_life_photo_001"]["next"] == "j3_02_nico_response_life_photo_002"
    assert n["j3_02_nico_response_life_photo_002"]["type"] == "message"
    assert n["j3_02_nico_response_life_photo_002"]["text"] == "mais une vie quand même."
    assert n["j3_02_nico_response_life_photo_002"]["next"] == "j3_02_nico_response_life_teased_004"


def test_t202_no_j3_media_added_to_camille_maya_or_ines() -> None:
    for name in [
        "camille_j3_v2_experimental.json",
        "maya_j3_v2_experimental.json",
        "ines_j3_v2_experimental.json",
    ]:
        assert [node for node in load(name)["nodes"] if node.get("type") == "media"] == []


def test_t202_j1_j2_media_have_follow_up_reactions() -> None:
    for name in J1_J2_MEDIA_FILES:
        dialogue = load(name)
        n = {node["id"]: node for node in dialogue["nodes"]}
        media_nodes = [node for node in dialogue["nodes"] if node.get("type") == "media"]
        assert media_nodes, name
        for media in media_nodes:
            follow = n[media["next"]]
            assert follow["type"] != "end", f"{name} {media['id']} goes directly to end"
            assert follow["type"] in {"message", "choice"}, f"{name} {media['id']} has no reaction/choice"
            if follow["type"] == "message":
                assert follow.get("text", "").strip(), f"{name} {media['id']} empty follow-up text"
            if follow["type"] == "choice":
                assert follow.get("choices"), f"{name} {media['id']} empty follow-up choice"


def test_t202_asset_names_and_captions_are_not_suggestive() -> None:
    forbidden = ["sexy", "nude", "lingerie", "maya", "camille", "ines"]
    for asset in [SARAH_ASSET, NICO_ASSET]:
        lowered = asset.lower()
        assert not any(word in lowered for word in forbidden)
    for name in ["sarah_j3_v2_experimental.json", "nico_j3_v2_experimental.json"]:
        for node in load(name)["nodes"]:
            if node.get("type") == "media":
                caption = node.get("caption", "").lower()
                assert not any(word in caption for word in ["sexy", "nude", "lingerie", "intime"])


if __name__ == "__main__":
    test_t202_j3_assets_exist_and_are_valid_pngs()
    test_t202_sarah_media_inserted_with_reaction_chain()
    test_t202_nico_media_inserted_with_reaction_chain()
    test_t202_no_j3_media_added_to_camille_maya_or_ines()
    test_t202_j1_j2_media_have_follow_up_reactions()
    test_t202_asset_names_and_captions_are_not_suggestive()
    print("T202 J3 media with reactions tests OK")
