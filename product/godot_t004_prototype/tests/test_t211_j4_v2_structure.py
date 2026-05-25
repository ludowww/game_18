#!/usr/bin/env python3
"""T211: J4 V2 structural skeleton and runtime progression declarations."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
STATE = ROOT / "scripts" / "conversation_state.gd"

CONVERSATIONS = {
    "sarah_j4_v2": {
        "file": "sarah_j4_v2_experimental.json",
        "contact": "sarah",
        "start": "j4_01_sarah_001",
        "placeholder": "[J4 placeholder Sarah matin]",
        "end": "j4_01_end",
        "title": "J4 V2 — Matin",
    },
    "nico_j4_v2": {
        "file": "nico_j4_v2_experimental.json",
        "contact": "nico",
        "start": "j4_02_nico_001",
        "placeholder": "[J4 placeholder Nico consultation]",
        "end": "j4_02_end",
        "title": "J4 V2 — Consultation",
    },
    "sarah_j4_followup_v2": {
        "file": "sarah_j4_followup_v2_experimental.json",
        "contact": "sarah",
        "start": "j4_03_sarah_followup_001",
        "placeholder": "[J4 placeholder Sarah retour]",
        "end": "j4_03_end",
        "title": "J4 V2 — Retour",
    },
    "camille_j4_v2": {
        "file": "camille_j4_v2_experimental.json",
        "contact": "camille",
        "start": "j4_04_camille_001",
        "placeholder": "[J4 placeholder Camille pause]",
        "end": "j4_04_end",
        "title": "J4 V2 — Pause",
    },
    "maya_j4_v2": {
        "file": "maya_j4_v2_experimental.json",
        "contact": "maya",
        "start": "j4_05_maya_001",
        "placeholder": "[J4 placeholder Maya social]",
        "end": "j4_05_end",
        "title": "J4 V2 — Ambiance",
    },
    "ines_j4_v2": {
        "file": "ines_j4_v2_experimental.json",
        "contact": "ines",
        "start": "j4_06_ines_001",
        "placeholder": "[J4 placeholder Inès soir]",
        "end": "j4_06_end",
        "title": "J4 V2 — Soir",
    },
}
REQUIRED_J4 = ["sarah_j4_v2", "nico_j4_v2", "sarah_j4_followup_v2", "camille_j4_v2", "maya_j4_v2"]


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def state_text() -> str:
    return STATE.read_text(encoding="utf-8")


def function_body(text: str, signature: str) -> str:
    start = text.index(signature)
    next_func = text.find("\nfunc ", start + 1)
    if next_func == -1:
        return text[start:]
    return text[start:next_func]


def test_t211_j4_json_skeletons_exist_and_are_valid() -> None:
    for conversation_id, spec in CONVERSATIONS.items():
        path = DATA / spec["file"]
        assert path.exists(), path
        data = load(spec["file"])
        assert data["schema_version"] == "0.1-j4-v2-experimental"
        assert data["conversation_id"] == conversation_id
        assert data["day"] == 4
        assert data["contact_id"] == spec["contact"]
        assert data["start_node"] == spec["start"]
        assert data["experimental"] is True
        nodes = {node["id"]: node for node in data["nodes"]}
        assert any(node.get("type") == "end" for node in data["nodes"])
        assert all(node.get("type") != "media" for node in data["nodes"])
        if conversation_id == "sarah_j4_v2":
            assert "[J4 placeholder Sarah matin]" not in json.dumps(data, ensure_ascii=False)
            assert "j4_01_choice_sarah_morning_detail" in nodes
        elif conversation_id == "nico_j4_v2":
            assert "[J4 placeholder Nico consultation]" not in json.dumps(data, ensure_ascii=False)
            assert "j4_02_choice_nico_consultation" in nodes
        elif conversation_id == "sarah_j4_followup_v2":
            assert "[J4 placeholder Sarah retour]" not in json.dumps(data, ensure_ascii=False)
            assert "j4_03_choice_sarah_followup" in nodes
        elif conversation_id == "camille_j4_v2":
            assert "[J4 placeholder Camille pause]" not in json.dumps(data, ensure_ascii=False)
            assert "j4_04_choice_camille_pause" in nodes
        else:
            assert data["entry_variants"] == [{"id": "default", "conditions": {}, "start_node": spec["start"]}]
            assert nodes[spec["start"]]["text"] == spec["placeholder"]
            assert nodes[spec["start"]]["next"] == spec["end"]
            assert "effects" not in json.dumps(data, ensure_ascii=False)


def test_t211_runtime_declares_j4_conversations() -> None:
    text = state_text()
    ids_line = function_body(text, "func conversation_ids() -> Array:")
    for conversation_id, spec in CONVERSATIONS.items():
        assert f'"{conversation_id}": _new_conversation_state(' in text
        assert f'"{conversation_id}"' in ids_line
        assert f'"res://data/{spec["file"]}"' in text
        assert f'"{spec["title"]}"' in text
        assert f'"{spec["start"]}"' in text


def test_t211_initial_unlock_and_progression_functions_exist() -> None:
    text = state_text()
    initial = function_body(text, "func _unlock_j4_v2_initial_conversations() -> void:")
    assert "experimental_j1_v2_enabled" in initial
    assert "current_day != 4" in initial
    assert 'conversations["sarah_j4_v2"]["available"] = true' in initial
    assert 'mark_conversation_new("sarah_j4_v2", "Sarah a remarqué un détail ce matin.")' in initial
    for locked in ["nico_j4_v2", "sarah_j4_followup_v2", "camille_j4_v2", "maya_j4_v2", "ines_j4_v2"]:
        assert f'conversations["{locked}"]["available"] = true' not in initial
    assert "current_day == 4" in text
    assert "_unlock_j4_v2_initial_conversations()" in function_body(text, "func _advance_day_unchecked() -> void:")


def test_t211_j4_progression_chain_and_badges() -> None:
    body = function_body(state_text(), "func _repair_j4_v2_progression_unlocks() -> void:")
    expected_pairs = [
        ("sarah_j4_v2", "nico_j4_v2", "Nico répond quand il peut."),
        ("nico_j4_v2", "sarah_j4_followup_v2", "Sarah attend toujours ta réponse."),
        ("sarah_j4_followup_v2", "camille_j4_v2", "Camille écrit pendant sa pause."),
        ("camille_j4_v2", "maya_j4_v2", "Maya revient sur l’ambiance."),
        ("maya_j4_v2", "ines_j4_v2", "Inès écrit tard."),
    ]
    assert "experimental_j1_v2_enabled" in body
    assert "current_day != 4" in body
    for source, target, badge in expected_pairs:
        assert f'conversations.has("{source}") and bool(conversations["{source}"].get("done", false))' in body
        assert f'conversations["{target}"]["available"] = true' in body
        assert f'mark_conversation_new("{target}", "{badge}")' in body
    assert "_repair_j4_v2_progression_unlocks()" in function_body(state_text(), "func mark_current_done() -> void:")
    assert "_repair_j4_v2_progression_unlocks()" in function_body(state_text(), "func refresh_day_progression() -> void:")


def test_t211_required_j4_and_legacy_filtering() -> None:
    text = state_text()
    required = function_body(text, "func _required_conversations_for_current_mode(day: int) -> Array:")
    assert "experimental_j1_v2_enabled and day == 4" in required
    for conversation_id in REQUIRED_J4:
        assert f'"{conversation_id}"' in required
    j4_block = required[required.index("experimental_j1_v2_enabled and day == 4"):required.index("return REQUIRED_CONVERSATIONS_BY_DAY")]
    assert '"ines_j4_v2"' not in j4_block
    allowed = function_body(text, "func _conversation_allowed_in_current_mode(id: String, state: Dictionary) -> bool:")
    assert "if day == 4:" in allowed
    assert "return bool(state.get(\"experimental\", false))" in allowed


if __name__ == "__main__":
    test_t211_j4_json_skeletons_exist_and_are_valid()
    test_t211_runtime_declares_j4_conversations()
    test_t211_initial_unlock_and_progression_functions_exist()
    test_t211_j4_progression_chain_and_badges()
    test_t211_required_j4_and_legacy_filtering()
    print("T211 J4 V2 structure tests OK")
