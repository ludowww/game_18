#!/usr/bin/env python3
"""T166: media bubbles use captions as fallback and images can zoom."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "conversation_screen.gd"


def source() -> str:
    return SCRIPT.read_text(encoding="utf-8")


def media_bubble_body() -> str:
    text = source()
    start = text.index("func _add_media_bubble")
    end = text.index("func _add_system_note", start)
    return text[start:end]


def test_placeholder_caption_helper_exists():
    text = source()
    assert "func _is_placeholder_caption(caption: String) -> bool:" in text
    assert "begins_with(\"[\")" in text
    assert "ends_with(\"]\")" in text


def test_loaded_image_suppresses_placeholder_caption_but_fallback_still_displays():
    body = media_bubble_body()
    assert "var image_loaded := false" in body
    assert "image_loaded = true" in body
    assert "var should_show_caption := true" in body
    assert "image_loaded and _is_placeholder_caption(caption)" in body
    assert "should_show_caption = false" in body
    assert "if should_show_caption:" in body
    assert "caption = \"[image envoyée]\"" in body


def test_media_image_is_clickable_and_opens_overlay():
    body = media_bubble_body()
    assert "gui_input.connect" in body
    assert "InputEventMouseButton" in body
    assert "MOUSE_BUTTON_LEFT" in body
    assert "_show_media_overlay" in body


def test_media_overlay_exists_and_can_close_without_scene_change():
    text = source()
    assert "func _show_media_overlay(texture: Texture2D, caption: String = \"\") -> void:" in text
    overlay_start = text.index("func _show_media_overlay")
    overlay_end = text.index("func _add_system_note", overlay_start)
    overlay = text[overlay_start:overlay_end]
    assert "ColorRect.new()" in overlay
    assert "PanelContainer.new()" in overlay
    assert "TextureRect.new()" in overlay
    assert "STRETCH_KEEP_ASPECT_CENTERED" in overlay
    assert "Fermer" in overlay
    assert "queue_free" in overlay
    assert "change_scene_to_file" not in overlay


def test_media_history_record_keeps_t162_shape():
    body = media_bubble_body()
    assert '"kind": "media"' in body
    assert '"sender": sender' in body
    assert '"media_type": media_type' in body
    assert '"asset": asset' in body
    assert '"caption": caption' in body


if __name__ == "__main__":
    test_placeholder_caption_helper_exists()
    test_loaded_image_suppresses_placeholder_caption_but_fallback_still_displays()
    test_media_image_is_clickable_and_opens_overlay()
    test_media_overlay_exists_and_can_close_without_scene_change()
    test_media_history_record_keeps_t162_shape()
    print("T166 media caption and zoom tests OK")
