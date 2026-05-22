#!/usr/bin/env python3
"""T173: J2 V2 structural skeleton exists without making J2 fully available."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")

CONVERSATIONS = {
    "sarah_j2_v2": ("sarah", "j2_01_sarah_001"),
    "nico_j2_v2": ("nico", "j2_02_nico_001"),
    "camille_j2_v2": ("camille", "j2_03_camille_001"),
    "maya_j2_v2": ("maya", "j2_04_maya_001"),
    "ines_j2_v2": ("ines", "j2_05_ines_001"),
}
REQUIRED_J2 = ["sarah_j2_v2", "nico_j2_v2", "camille_j2_v2", "maya_j2_v2"]
OPTIONAL_J2 = "ines_j2_v2"


def load_json(conversation_id: str) -> dict:
    return json.loads((DATA / f"{conversation_id}_experimental.json").read_text(encoding="utf-8"))


def test_j2_v2_json_skeletons_exist_and_are_minimal():
    for conversation_id, (contact_id, start_node) in CONVERSATIONS.items():
        path = DATA / f"{conversation_id}_experimental.json"
        assert path.exists(), path
        data = load_json(conversation_id)
        assert data["schema_version"] == "0.1-j2-v2-experimental"
        assert data["conversation_id"] == conversation_id
        assert data["day"] == 2
        assert data["contact_id"] == contact_id
        assert data["start_node"] == start_node
        assert data["experimental"] is True
        assert any(node.get("id") == start_node for node in data["nodes"])
        assert any(node.get("type") == "end" for node in data["nodes"])
        default = next((variant for variant in data["entry_variants"] if variant.get("id") == "default"), None)
        assert default is not None
        assert default["conditions"] == {}
        assert default["start_node"] == start_node


def test_conversation_state_declares_j2_v2_conversations_locked_by_default():
    for conversation_id, (contact_id, start_node) in CONVERSATIONS.items():
        assert f'"{conversation_id}": _new_conversation_state(' in STATE
        assert f'"{conversation_id}",' in STATE
        assert f'"{contact_id}",' in STATE
        assert f'"res://data/{conversation_id}_experimental.json"' in STATE
        assert f'"{start_node}"' in STATE
    for title in ["J2 V2 — Matin", "J2 V2 — Alibi", "J2 V2 — Tension", "J2 V2 — Groupe", "J2 V2 — Calme"]:
        assert title in STATE


def test_j2_v2_initial_unlock_only_makes_sarah_and_nico_available():
    assert "func _unlock_j2_v2_initial_conversations() -> void:" in STATE
    unlock_body = STATE.split("func _unlock_j2_v2_initial_conversations() -> void:", 1)[1].split("\nfunc ", 1)[0]
    assert 'mark_conversation_new("sarah_j2_v2", "Sarah a écrit ce matin.")' in unlock_body
    assert 'mark_conversation_new("nico_j2_v2", "Nico vérifie si ça tient encore.")' in unlock_body
    assert 'conversations["camille_j2_v2"]["available"] = true' not in unlock_body
    assert 'conversations["maya_j2_v2"]["available"] = true' not in unlock_body
    assert 'conversations["ines_j2_v2"]["available"] = true' not in unlock_body
    assert "if experimental_j1_v2_enabled and current_day == 2:" in STATE
    assert "_unlock_j2_v2_initial_conversations()" in STATE


def test_j2_v2_after_morning_unlock_prepares_camille_only():
    assert "func _unlock_j2_v2_after_morning_if_ready() -> void:" in STATE
    body = STATE.split("func _unlock_j2_v2_after_morning_if_ready() -> void:", 1)[1].split("\nfunc ", 1)[0]
    assert 'bool(conversations["sarah_j2_v2"].get("done", false))' in body
    assert 'bool(conversations["nico_j2_v2"].get("done", false))' in body
    assert 'mark_conversation_new("camille_j2_v2"' in body
    assert 'mark_conversation_new("maya_j2_v2"' not in body
    assert 'mark_conversation_new("ines_j2_v2"' not in body


def test_required_conversations_for_day_2_experimental_exclude_ines():
    match = re.search(r"if experimental_j1_v2_enabled and day == 2:\n\t\treturn \[(.*?)\n\t\t\]", STATE, re.S)
    assert match, "missing experimental day 2 required conversations branch"
    body = match.group(1)
    for conversation_id in REQUIRED_J2:
        assert f'"{conversation_id}"' in body
    assert f'"{OPTIONAL_J2}"' not in body


if __name__ == "__main__":
    test_j2_v2_json_skeletons_exist_and_are_minimal()
    test_conversation_state_declares_j2_v2_conversations_locked_by_default()
    test_j2_v2_initial_unlock_only_makes_sarah_and_nico_available()
    test_j2_v2_after_morning_unlock_prepares_camille_only()
    test_required_conversations_for_day_2_experimental_exclude_ines()
    print("T173 J2 V2 structure tests OK")
