from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "conversation_state.gd"
BLOCKS = ROOT / "data" / "conversation_blocks.json"
SCREEN = ROOT / "scripts" / "conversation_screen.gd"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(source: str, start: str, end: str) -> str:
    return source.split(start, 1)[1].split(end, 1)[0]


def test_t125_j6_second_blocks_declare_pre_start_bridge_nodes_for_notification_repair() -> None:
    config = json.loads(read(BLOCKS))
    blocks = config["blocks"]
    assert blocks["sarah_s6b"]["pre_start_nodes"] == ["s6_014_a", "s6_014_b", "s6_014_c"]
    assert blocks["camille_c6b"]["pre_start_nodes"] == ["c6_014_a", "c6_014_b", "c6_014_c"]


def test_t125_repair_does_not_treat_j6_bridge_nodes_as_started_available_blocks() -> None:
    state = read(STATE)
    helper = section(state, "func _has_started_available_block", "func current_done")
    assert "pre_start_nodes" in helper
    assert "pre_start_nodes.has(next_node)" in helper
    assert helper.index("pre_start_nodes.has(next_node)") < helper.index("next_node != \"\" and next_node != start_node")


def test_t125_conversation_screen_still_repairs_before_refresh_after_unlock() -> None:
    screen = read(SCREEN)
    advance = section(screen, "func _advance_to", "func _wait_before_node")
    for boundary in ["ConversationState.complete_current_block(next_id)", "ConversationState.complete_current_block(\"\")"]:
        assert boundary in advance
        after = advance[advance.index(boundary):]
        assert "ConversationState.repair_available_block_notifications()" in after
        assert "_refresh_quick_switch_notification()" in after
        assert after.index("ConversationState.repair_available_block_notifications()") < after.index("_refresh_quick_switch_notification()")


if __name__ == "__main__":
    test_t125_j6_second_blocks_declare_pre_start_bridge_nodes_for_notification_repair()
    test_t125_repair_does_not_treat_j6_bridge_nodes_as_started_available_blocks()
    test_t125_conversation_screen_still_repairs_before_refresh_after_unlock()
    print("T125 J6 second-block quick-switch tests OK")
