from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIST_SCRIPT = ROOT / "scripts" / "conversation_list.gd"


def test_t080_day_transition_button_uses_current_day_plus_one() -> None:
    source = LIST_SCRIPT.read_text(encoding="utf-8")
    assert 'var next_day: int = ConversationState.current_day + 1' in source
    assert 'button.text = "Passer au Jour " + str(next_day)' in source


def test_t080_day_transition_button_has_no_j1_j2_hardcoded_copy() -> None:
    source = LIST_SCRIPT.read_text(encoding="utf-8")
    day_button_section = source.split("func _make_day_transition_button() -> Button:", 1)[1].split("func _make_conversation_entry", 1)[0]
    assert 'button.text = "Passer au Jour 2"' not in day_button_section
    assert "Camille J1 et Sarah J1 sont terminés" not in day_button_section
    assert 'button.tooltip_text = "Passer au jour suivant"' in day_button_section


if __name__ == "__main__":
    test_t080_day_transition_button_uses_current_day_plus_one()
    test_t080_day_transition_button_has_no_j1_j2_hardcoded_copy()
    print("T080 day transition button label tests OK")
