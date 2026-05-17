from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "conversation_screen.gd"
LIST = ROOT / "scripts" / "conversation_list.gd"
DATA = ROOT / "data"

EXPECTED_UNCHANGED_HASHES = {
    "conversation_blocks.json": "5bee89f1e5d8422a8d368f2afda4071b3a05aea6011e60708dcd1a34c7d6f6b0",
    "camille_j1_complete.json": "365ee9d64240da7101452ff64ddb189b7aada92ede25e147b5cdb45a6507b980",
    "sarah_j1_complete.json": "4c197ef3bd59784f1559ad3a33184d912331a0a41fe80974e3c405e7ac10336a",
    "camille_j2_complete.json": "a0ff3e17c38ed542cb558fdf505d587251cbe9632736c2f3ab2eed1557000fef",
    "sarah_j2_complete.json": "2740b0d0c5cdd042eff874a8a6414bfb1575c9668ab6763626603b582c14e357",
    "camille_j3_complete.json": "3ed12d5e7af784c5c82a16dbc1ea0a8096867f164d2ac32ae7c76aa126f10bd2",
    "sarah_j3_complete.json": "6c0992a9ac099bde19f7d56c94bd354f5338978b49bae53306e35e0c2a891a6b",
    "camille_j4_complete.json": "d013fc4d361e22abf5317022b0dfdda8dcf76764eda8227d0a42a5d97277ccb9",
    "maya_j4_complete.json": "2c9ca743f608a2a0106cd216995b84766d737edaa50b3ecc253412f298848458",
    "ines_j4_complete.json": "8bde309a9fca94bb7469e4e28cd1d668803011bc8e2ce4726f71152d4e40737e",
    "nico_j4_complete.json": "efeacf9cf4b8c11c3fe4bcc75e1e5b899f15e4b18a22f24e69e4d1227205d8ad",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_color(source: str, const_name: str) -> str:
    match = re.search(rf"const {const_name} := Color\(\"([0-9a-fA-F]+)\"\)", source)
    assert match, const_name
    return match.group(1).lower()


def test_t099_j4_contacts_have_distinct_centralized_colors_in_chat_and_list() -> None:
    screen = read(SCREEN)
    list_source = read(LIST)

    for const_name in ["CAMILLE_COLOR", "SARAH_COLOR", "MAYA_COLOR", "INES_COLOR", "NICO_COLOR"]:
        assert const_name in screen
        assert const_name in list_source

    screen_colors = {name: extract_color(screen, name) for name in ["CAMILLE_COLOR", "SARAH_COLOR", "MAYA_COLOR", "INES_COLOR", "NICO_COLOR"]}
    list_colors = {name: extract_color(list_source, name) for name in ["CAMILLE_COLOR", "SARAH_COLOR", "MAYA_COLOR", "INES_COLOR", "NICO_COLOR"]}

    assert screen_colors == list_colors
    assert len(set(screen_colors.values())) == 5
    assert screen_colors["MAYA_COLOR"] != screen_colors["INES_COLOR"]
    assert screen_colors["MAYA_COLOR"] != screen_colors["NICO_COLOR"]
    assert screen_colors["INES_COLOR"] != screen_colors["NICO_COLOR"]

    for contact, const_name in [("maya", "MAYA_COLOR"), ("ines", "INES_COLOR"), ("nico", "NICO_COLOR")]:
        assert f'contact_id == "{contact}"' in screen
        assert f'return {const_name}' in screen
        assert f'conversation_id.begins_with("{contact}")' in list_source
        assert f'return {const_name}' in list_source

    assert 'return Color("3b516a")' not in screen
    assert 'return Color("3b516a")' not in list_source


def test_t099_typing_indicator_is_near_message_flow_and_animated() -> None:
    screen = read(SCREEN)
    assert "var typing_row: HBoxContainer" in screen
    assert "func _add_typing_bubble" in screen
    assert "message_list.add_child(typing_row)" in screen
    assert "typing_indicator_active" in screen
    assert "typing_dot_count" in screen
    assert "func _animate_typing_indicator" in screen
    assert "await get_tree().create_timer(0.32).timeout" in screen
    assert "_typing_indicator_text" in screen
    assert "typing_label.modulate.a" in screen


def test_t099_dialogue_json_and_conversation_blocks_are_unchanged() -> None:
    for filename, expected_hash in EXPECTED_UNCHANGED_HASHES.items():
        path = DATA / filename
        assert path.exists(), filename
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        assert actual_hash == expected_hash, filename


if __name__ == "__main__":
    test_t099_j4_contacts_have_distinct_centralized_colors_in_chat_and_list()
    test_t099_typing_indicator_is_near_message_flow_and_animated()
    test_t099_dialogue_json_and_conversation_blocks_are_unchanged()
    print("T099 contact colors + typing indicator tests OK")
