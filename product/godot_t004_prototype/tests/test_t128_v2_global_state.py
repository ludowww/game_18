from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
SCREEN = ROOT / "scripts" / "conversation_screen.gd"


def state_text() -> str:
    return STATE.read_text(encoding="utf-8")


def screen_text() -> str:
    return SCREEN.read_text(encoding="utf-8")


def test_t128_declares_global_v2_state_and_initial_variables() -> None:
    source = state_text()
    assert "const V2_VARIABLE_DEFAULTS :=" in source
    for variable in [
        "confiance_sarah",
        "distance_sarah",
        "tension_camille",
        "respect_camille",
        "pression_camille",
        "intimite_sarah",
        "intimite_camille",
        "attente_image_camille",
        "suspicion_maya",
        "dette_nico",
        "fuite_ines",
        "coherence",
        "culpabilite",
        "risque_exposition",
        "fatigue_emotionnelle",
    ]:
        assert f'"{variable}"' in source
    assert "var global_game_state: Dictionary = _default_global_game_state()" in source
    assert "func _default_global_game_state() -> Dictionary:" in source
    assert '"flags": []' in source


def test_t128_global_apply_effects_clamps_variables_and_merges_unique_flags() -> None:
    source = state_text()
    assert "func apply_global_effects(effects_value) -> Dictionary:" in source
    assert "clamp(" in source
    assert "V2_VARIABLE_DEFAULTS.has(key)" in source
    assert 'global_game_state["variables"][key]' in source
    assert 'global_game_state["flags"].append(flag)' in source
    assert 'if not global_game_state["flags"].has(flag):' in source
    assert "save_progression()" in source.split("func apply_global_effects", 1)[1].split("func ", 1)[0]


def test_t128_global_state_is_saved_and_loaded() -> None:
    source = state_text()
    assert '"global_game_state": global_game_state.duplicate(true)' in source
    assert 'var saved_global_game_state = payload.get("global_game_state", {})' in source
    assert "_merge_saved_global_game_state(saved_global_game_state)" in source
    assert "func _merge_saved_global_game_state(saved_global_game_state) -> void:" in source


def test_t128_screen_applies_effects_to_global_state_not_per_conversation_state() -> None:
    source = screen_text()
    assert "ConversationState.apply_global_effects(effects_value)" in source
    assert "game_state = ConversationState.global_state()" in source
    apply_body = source.split("func _apply_effects(effects_value) -> void:", 1)[1].split("func ", 1)[0]
    assert "for key in effects.keys()" not in apply_body
    assert "ConversationState.set_current_game_state" not in apply_body


if __name__ == "__main__":
    test_t128_declares_global_v2_state_and_initial_variables()
    test_t128_global_apply_effects_clamps_variables_and_merges_unique_flags()
    test_t128_global_state_is_saved_and_loaded()
    test_t128_screen_applies_effects_to_global_state_not_per_conversation_state()
    print("T128 V2 global state tests OK")
