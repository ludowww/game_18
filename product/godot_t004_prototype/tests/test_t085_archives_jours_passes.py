from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIST = ROOT / "scripts" / "conversation_list.gd"
STATE = ROOT / "scripts" / "conversation_state.gd"
DATA_DIR = ROOT / "data"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_messages_active_filter_and_archives_are_code_side_only():
    listing = read(LIST)
    state = read(STATE)

    # Messages active must be current-day only, not all past visible ids.
    assert "func active_conversation_ids() -> Array:" in state
    active_body = state.split("func active_conversation_ids() -> Array:", 1)[1].split("func archived_conversation_ids()", 1)[0]
    assert "day == current_day" in active_body
    assert "day <= current_day" not in active_body
    assert "ConversationState.active_conversation_ids()" in listing
    assert "ConversationState.visible_conversation_ids()" not in listing

    # Past days remain readable via a discreet, collapsed Archives / Jours précédents UI.
    assert "func archived_conversation_ids() -> Array:" in state
    archive_body = state.split("func archived_conversation_ids() -> Array:", 1)[1].split("func set_current_conversation", 1)[0]
    assert "day < current_day" in archive_body
    assert "Archives" in listing or "Jours précédents" in listing
    assert "archives_expanded: bool = false" in listing
    assert "_make_archives_toggle" in listing
    assert "_make_archived_conversation_entry" in listing
    assert "ConversationState.archived_conversation_ids()" in listing

    # Archived entries are openable but visually secondary and never show active badges/previews.
    archived_entry_body = listing.split("func _make_archived_conversation_entry", 1)[1].split("func _make_day_transition_button", 1)[0]
    assert "ConversationState.set_current_conversation(conversation_id)" in archived_entry_body or "_make_conversation_entry" in archived_entry_body
    assert "change_scene_to_file(CHAT_SCENE)" in archived_entry_body or "_make_conversation_entry" in archived_entry_body
    assert "false" in archived_entry_body  # has_new forced off for archive cards
    assert "archived_preview_text" in state

    # No dialogue JSON / block config changes are needed for this UI behavior.
    assert '"day"' not in listing  # day metadata is read via state helpers, not hardcoded in UI loop
    assert (DATA_DIR / "conversation_blocks.json").exists()


if __name__ == "__main__":
    test_messages_active_filter_and_archives_are_code_side_only()
    print("T085 archives jours passés static checks OK")
