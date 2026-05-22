#!/usr/bin/env python3
"""T162: media node support foundation for conversations."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SCREEN = (ROOT / "scripts" / "conversation_screen.gd").read_text(encoding="utf-8")
TEST_MEDIA = DATA / "test_media_conversation.json"


def function_body(name: str) -> str:
    marker = f"func {name}"
    assert marker in SCREEN, marker
    body = SCREEN[SCREEN.index(marker):]
    return body.split("\nfunc ", 1)[0]


def test_advance_to_recognizes_media_nodes():
    body = function_body("_advance_to")
    assert 'node_type == "media"' in body
    assert "_add_media_bubble" in body
    assert "_wait_before_node(node)" in body


def test_media_bubble_function_supports_image_and_caption_fallback():
    body = function_body("_add_media_bubble")
    assert "media_type" in body
    assert '"image"' in body
    assert "asset" in body
    assert "caption" in body
    assert "[image envoyée]" in body
    assert "ResourceLoader.exists" in body
    assert "TextureRect" in body


def test_history_restore_keeps_legacy_messages_and_media_entries():
    restore_body = function_body("_restore_current_messages")
    assert 'entry.get("kind", "message")' in restore_body
    assert '== "media"' in restore_body
    assert "_add_media_bubble" in restore_body
    assert "_add_bubble" in restore_body
    media_body = function_body("_add_media_bubble")
    assert '"kind": "media"' in media_body
    assert "record_current_event" in media_body
    assert "record_current_message" in SCREEN


def test_test_media_conversation_exists_and_contains_valid_media_node():
    assert TEST_MEDIA.exists()
    data = json.loads(TEST_MEDIA.read_text(encoding="utf-8"))
    nodes = {node["id"]: node for node in data["nodes"]}
    media = nodes["test_media_002"]
    assert media["type"] == "media"
    assert media["sender"] == "maya"
    assert media["media_type"] == "image"
    assert "asset" in media
    assert media["caption"] == "[photo de groupe envoyée]"
    assert media["next"] == "test_media_003"


if __name__ == "__main__":
    test_advance_to_recognizes_media_nodes()
    test_media_bubble_function_supports_image_and_caption_fallback()
    test_history_restore_keeps_legacy_messages_and_media_entries()
    test_test_media_conversation_exists_and_contains_valid_media_node()
    print("T162 media node support tests OK")
