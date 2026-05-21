from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
SCREEN = ROOT / "scripts" / "conversation_screen.gd"


def source(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def function_body(text: str, name: str) -> str:
    start = text.index(f"func {name}")
    rest = text[start + 5:]
    next_func = rest.find("\nfunc ")
    if next_func == -1:
        return text[start:]
    return text[start:start + 5 + next_func]


def test_t136_conversation_state_exposes_global_flag_and_variable_helpers() -> None:
    text = source(STATE)
    assert "func has_global_flag(flag: String) -> bool:" in text
    assert "return global_game_state.get(\"flags\", []).has(flag)" in function_body(text, "has_global_flag")
    assert "func global_variable_value(key: String) -> int:" in text
    assert "return int(global_game_state.get(\"variables\", {}).get(key, 0))" in function_body(text, "global_variable_value")


def test_t136_new_conversation_uses_resolved_entry_variant_start_node() -> None:
    text = source(SCREEN)
    ready = function_body(text, "_ready")
    assert "var start_node := _resolved_start_node()" in ready
    assert "_advance_to(start_node, true)" in ready
    assert "_advance_to(ConversationState.current_block_start_node(), true)" not in ready


def test_t136_resolved_start_node_checks_entry_variants_in_order_before_fallback() -> None:
    text = source(SCREEN)
    assert "func _resolved_start_node() -> String:" in text
    body = function_body(text, "_resolved_start_node")
    assert 'var variants = conversation.get("entry_variants", [])' in body
    assert "for variant in variants:" in body
    assert "if _entry_variant_matches(variant):" in body
    assert 'return str(variant.get("start_node", conversation.get("start_node", "")))' in body
    assert "return ConversationState.current_block_start_node()" in body
    assert body.index("for variant in variants:") < body.index("return ConversationState.current_block_start_node()")


def test_t136_entry_variant_matcher_supports_only_flags_and_not_flags() -> None:
    text = source(SCREEN)
    assert "func _entry_variant_matches(variant: Dictionary) -> bool:" in text
    body = function_body(text, "_entry_variant_matches")
    assert 'var conditions: Dictionary = variant.get("conditions", {})' in body
    assert 'var flags: Array = conditions.get("flags", [])' in body
    assert "if not ConversationState.has_global_flag(str(flag)):" in body
    assert 'var not_flags: Array = conditions.get("not_flags", [])' in body
    assert "if ConversationState.has_global_flag(str(flag)):" in body
    assert "return true" in body
    assert "global_variable_value" not in body


if __name__ == "__main__":
    test_t136_conversation_state_exposes_global_flag_and_variable_helpers()
    test_t136_new_conversation_uses_resolved_entry_variant_start_node()
    test_t136_resolved_start_node_checks_entry_variants_in_order_before_fallback()
    test_t136_entry_variant_matcher_supports_only_flags_and_not_flags()
    print("T136 entry variants runtime tests OK")
