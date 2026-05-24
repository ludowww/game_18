#!/usr/bin/env python3
"""T190: J3 V2 structural skeleton exists without writing real scenes."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
STATE = (ROOT / "scripts" / "conversation_state.gd").read_text(encoding="utf-8")

CONVERSATIONS = {
    "sarah_j3_v2": ("sarah", "j3_01_sarah_001", "[J3 placeholder Sarah matin]", "J3 V2 — Matin"),
    "nico_j3_v2": ("nico", "j3_02_nico_001", "[J3 placeholder Nico matin]", "J3 V2 — Disponibilité"),
    "camille_j3_v2": ("camille", "j3_03_camille_001", "[J3 placeholder Camille après-midi]", "J3 V2 — Tension"),
    "maya_j3_v2": ("maya", "j3_04_maya_001", "[J3 placeholder Maya après-midi]", "J3 V2 — Signaux"),
    "ines_j3_v2": ("ines", "j3_05_ines_001", "[J3 placeholder Inès soir]", "J3 V2 — Calme"),
}


def function_body(name: str) -> str:
    marker = f"func {name}"
    assert marker in STATE, f"missing function {name}"
    return STATE.split(marker, 1)[1].split("\nfunc ", 1)[0]


def conversation_state_block(conversation_id: str) -> str:
    marker = f'"{conversation_id}": _new_conversation_state('
    assert marker in STATE, f"missing declaration for {conversation_id}"
    return STATE.split(marker, 1)[1].split("\n\t\t),", 1)[0]


def test_t190_j3_json_skeleton_files_exist_and_are_minimal() -> None:
    for conversation_id, (contact_id, start_node, placeholder, _title) in CONVERSATIONS.items():
        path = DATA / f"{conversation_id}_experimental.json"
        assert path.exists(), f"missing {path}"
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["schema_version"] == "0.1-j3-v2-experimental"
        assert data["conversation_id"] == conversation_id
        assert data["day"] == 3
        assert data["contact_id"] == contact_id
        assert data["start_node"] == start_node
        assert data["experimental"] is True
        assert any(node.get("id") == start_node and node.get("text") == placeholder for node in data["nodes"])
        assert any(node.get("type") == "end" for node in data["nodes"])
        default_variants = [variant for variant in data["entry_variants"] if variant.get("id") == "default"]
        assert default_variants, f"missing default entry variant for {conversation_id}"
        assert default_variants[0].get("conditions", {}) == {}
        assert default_variants[0].get("start_node") == start_node


def test_t190_conversation_state_declares_j3_v2_conversations_locked_by_default() -> None:
    ids_body = function_body("conversation_ids() -> Array:")
    for conversation_id, (_contact_id, start_node, _placeholder, title) in CONVERSATIONS.items():
        assert f'"{conversation_id}"' in ids_body
        block = conversation_state_block(conversation_id)
        assert f'"{title}"' in block
        assert f'"res://data/{conversation_id}_experimental.json"' in block
        assert "\n\t\t\t3," in block
        assert "\n\t\t\tfalse," in block, f"{conversation_id} should be unavailable by default"
        assert "\n\t\t\ttrue," in block, f"{conversation_id} should be experimental"
        assert f'"{start_node}"' in block


def test_t190_j3_initial_unlocks_only_sarah_and_nico() -> None:
    assert "func _unlock_j3_v2_initial_conversations() -> void:" in STATE
    body = function_body("_unlock_j3_v2_initial_conversations() -> void:")
    assert 'conversations["sarah_j3_v2"]["available"] = true' in body
    assert 'mark_conversation_new("sarah_j3_v2", "Sarah observe la journée.")' in body
    assert 'conversations["nico_j3_v2"]["available"] = true' in body
    assert 'mark_conversation_new("nico_j3_v2", "Nico répond plus tard que d’habitude.")' in body
    assert 'conversations["camille_j3_v2"]["available"] = true' not in body
    assert 'conversations["maya_j3_v2"]["available"] = true' not in body
    assert 'conversations["ines_j3_v2"]["available"] = true' not in body

    advance = function_body("_advance_day_unchecked() -> void:")
    assert "experimental_j1_v2_enabled and current_day == 3" in advance
    assert "_unlock_j3_v2_initial_conversations()" in advance


def test_t190_j3_required_conversations_are_sarah_and_nico_only() -> None:
    required = function_body("_required_conversations_for_current_mode(day: int) -> Array:")
    match = re.search(r"if experimental_j1_v2_enabled and day == 3:\n\t\treturn \[(.*?)\n\t\t\]", required, re.S)
    assert match, "missing experimental J3 required branch"
    body = match.group(1)
    assert '"sarah_j3_v2"' in body
    assert '"nico_j3_v2"' in body
    assert '"camille_j3_v2"' not in body
    assert '"maya_j3_v2"' not in body
    assert '"ines_j3_v2"' not in body


def test_t190_j3_progression_can_unlock_camille_only_after_sarah_or_nico() -> None:
    assert "func _repair_j3_v2_progression_unlocks() -> void:" in STATE
    body = function_body("_repair_j3_v2_progression_unlocks() -> void:")
    assert 'not experimental_j1_v2_enabled or current_day != 3' in body
    assert 'conversations["sarah_j3_v2"].get("done", false)' in body
    assert 'conversations["nico_j3_v2"].get("done", false)' in body
    assert 'mark_conversation_new("camille_j3_v2"' in body
    assert 'mark_conversation_new("maya_j3_v2"' not in body
    assert 'mark_conversation_new("ines_j3_v2"' not in body
    assert "_repair_j3_v2_progression_unlocks()" in function_body("mark_current_done() -> void:")
    assert "_repair_j3_v2_progression_unlocks()" in function_body("refresh_day_progression() -> void:")


def test_t190_experimental_day3_filter_hides_legacy_j3() -> None:
    body = function_body("_conversation_allowed_in_current_mode(id: String, state: Dictionary) -> bool:")
    assert "if day == 3:" in body
    assert 'return bool(state.get("experimental", false))' in body
    active = function_body("active_conversation_ids() -> Array:")
    assert 'id == "camille_j3"' not in active
    assert 'id == "sarah_j3"' not in active


if __name__ == "__main__":
    test_t190_j3_json_skeleton_files_exist_and_are_minimal()
    test_t190_conversation_state_declares_j3_v2_conversations_locked_by_default()
    test_t190_j3_initial_unlocks_only_sarah_and_nico()
    test_t190_j3_required_conversations_are_sarah_and_nico_only()
    test_t190_j3_progression_can_unlock_camille_only_after_sarah_or_nico()
    test_t190_experimental_day3_filter_hides_legacy_j3()
    print("T190 J3 V2 structure tests OK")
