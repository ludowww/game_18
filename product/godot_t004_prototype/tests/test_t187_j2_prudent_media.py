#!/usr/bin/env python3
"""T187: Camille/Inès J2 get only prudent symbolic media moments."""

import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ASSETS = ROOT / "assets" / "media" / "j2_v2"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def nodes_by_id(data: dict) -> dict:
    return {node["id"]: node for node in data["nodes"]}


def assert_valid_png(path: Path) -> None:
    raw = path.read_bytes()
    assert raw.startswith(b"\x89PNG\r\n\x1a\n"), path
    width, height = struct.unpack(">II", raw[16:24])
    assert width > 0 and height > 0, path


def media_nodes(data: dict) -> list:
    return [node for node in data["nodes"] if node.get("type") == "media"]


def test_t187_assets_exist_and_are_valid_pngs() -> None:
    for filename in ["camille_dehors_j2.png", "ines_fenetre_soir_j2.png"]:
        path = ASSETS / filename
        assert path.exists(), path
        assert_valid_png(path)


def test_t187_camille_has_single_dehors_media_in_tension_acknowledged_path() -> None:
    nodes = nodes_by_id(load("camille_j2_v2_experimental.json"))
    media = nodes["j2_03_camille_media_dehors_001"]
    assert media["type"] == "media"
    assert media["sender"] == "camille"
    assert media["media_type"] == "image"
    assert media["asset"] == "res://assets/media/j2_v2/camille_dehors_j2.png"
    assert media["caption"] == "[photo du dehors envoyée]"
    assert media["delay"] == 30
    assert nodes["j2_03_camille_entry_tension_ack_002"]["next"] == "j2_03_camille_media_dehors_001"
    assert media["next"] == "j2_03_camille_entry_tension_ack_003"
    assert [node["id"] for node in media_nodes(load("camille_j2_v2_experimental.json"))] == ["j2_03_camille_media_dehors_001"]


def test_t187_ines_has_single_calm_media_in_opened_softly_path() -> None:
    nodes = nodes_by_id(load("ines_j2_v2_experimental.json"))
    media = nodes["j2_05_ines_media_calm_001"]
    assert media["type"] == "media"
    assert media["sender"] == "ines"
    assert media["media_type"] == "image"
    assert media["asset"] == "res://assets/media/j2_v2/ines_fenetre_soir_j2.png"
    assert media["caption"] == "[photo d’un coin calme envoyée]"
    assert media["delay"] == 30
    assert nodes["j2_05_ines_entry_opened_003"]["next"] == "j2_05_ines_media_calm_001"
    assert media["next"] == "j2_05_ines_entry_opened_004"
    assert [node["id"] for node in media_nodes(load("ines_j2_v2_experimental.json"))] == ["j2_05_ines_media_calm_001"]


def test_t187_no_extra_media_added_to_sarah_nico_or_maya_j2() -> None:
    assert media_nodes(load("sarah_j2_v2_experimental.json")) == []
    assert media_nodes(load("nico_j2_v2_experimental.json")) == []
    maya_media = media_nodes(load("maya_j2_v2_experimental.json"))
    assert [node["id"] for node in maya_media] == ["j2_04_maya_media_group_001"]
    assert maya_media[0]["asset"] == "res://assets/media/j1_v2/maya_photo_groupe_j1.png"


if __name__ == "__main__":
    test_t187_assets_exist_and_are_valid_pngs()
    test_t187_camille_has_single_dehors_media_in_tension_acknowledged_path()
    test_t187_ines_has_single_calm_media_in_opened_softly_path()
    test_t187_no_extra_media_added_to_sarah_nico_or_maya_j2()
    print("T187 J2 prudent media tests OK")
