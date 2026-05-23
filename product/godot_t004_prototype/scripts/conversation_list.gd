extends Control

const CHAT_SCENE := "res://scenes/conversation_screen.tscn"
const CAMILLE_COLOR := Color("46345f")
const SARAH_COLOR := Color("a96d2a")
const MAYA_COLOR := Color("2f6f73")
const INES_COLOR := Color("7b3f67")
const NICO_COLOR := Color("426c2f")
const SYSTEM_COLOR := Color("2d2d35")

var archives_expanded: bool = false

func _ready() -> void:
	ConversationState.repair_available_block_notifications()
	_build_ui()

func _rebuild_ui() -> void:
	for child in get_children():
		remove_child(child)
		child.queue_free()
	_build_ui()

func _build_ui() -> void:
	var background := ColorRect.new()
	background.color = Color("0f0f14")
	background.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(background)

	var outer := MarginContainer.new()
	outer.set_anchors_preset(Control.PRESET_FULL_RECT)
	outer.add_theme_constant_override("margin_left", 12)
	outer.add_theme_constant_override("margin_right", 12)
	outer.add_theme_constant_override("margin_top", 16)
	outer.add_theme_constant_override("margin_bottom", 16)
	add_child(outer)

	var phone_frame := PanelContainer.new()
	phone_frame.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	phone_frame.size_flags_vertical = Control.SIZE_EXPAND_FILL
	var phone_style := StyleBoxFlat.new()
	phone_style.bg_color = Color("181820")
	phone_style.corner_radius_top_left = 30
	phone_style.corner_radius_top_right = 30
	phone_style.corner_radius_bottom_left = 30
	phone_style.corner_radius_bottom_right = 30
	phone_style.border_color = Color("3a3a46")
	phone_style.set_border_width_all(2)
	phone_frame.add_theme_stylebox_override("panel", phone_style)
	outer.add_child(phone_frame)

	var phone_margin := MarginContainer.new()
	phone_margin.add_theme_constant_override("margin_left", 12)
	phone_margin.add_theme_constant_override("margin_right", 12)
	phone_margin.add_theme_constant_override("margin_top", 14)
	phone_margin.add_theme_constant_override("margin_bottom", 14)
	phone_frame.add_child(phone_margin)

	var root := VBoxContainer.new()
	root.add_theme_constant_override("separation", 12)
	phone_margin.add_child(root)

	var title := Label.new()
	title.text = "Messages"
	title.add_theme_font_size_override("font_size", 26)
	root.add_child(title)

	var header_stack := VBoxContainer.new()
	header_stack.add_theme_constant_override("separation", 6)
	header_stack.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	root.add_child(header_stack)

	var subtitle_row := HBoxContainer.new()
	subtitle_row.add_theme_constant_override("separation", 8)
	subtitle_row.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	header_stack.add_child(subtitle_row)

	var subtitle := Label.new()
	subtitle.text = "Prototype MVP — conversations · " + ConversationState.day_label()
	subtitle.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	subtitle.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	subtitle.clip_text = false
	subtitle.add_theme_font_size_override("font_size", 13)
	subtitle.add_theme_color_override("font_color", Color("9b9baa"))
	subtitle_row.add_child(subtitle)

	header_stack.add_child(_make_header_debug_controls())

	if ConversationState.j1_v2_should_show_first_open_note():
		root.add_child(_make_j1_v2_first_open_note())

	if ConversationState.is_day_transition_available():
		root.add_child(_make_day_transition_button())

	var scroll := ScrollContainer.new()
	scroll.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	root.add_child(scroll)

	var list := VBoxContainer.new()
	list.custom_minimum_size = Vector2(0, 0)
	list.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	list.size_flags_vertical = Control.SIZE_EXPAND_FILL
	list.add_theme_constant_override("separation", 10)
	scroll.add_child(list)

	for conversation_id in ConversationState.active_conversation_ids():
		var state: Dictionary = ConversationState.conversation(conversation_id)
		list.add_child(_make_conversation_entry(
			conversation_id,
			str(state.get("display_name", conversation_id)),
			str(state.get("title", "")),
			ConversationState.preview_text(conversation_id),
			bool(state.get("available", false)),
			ConversationState.has_new(conversation_id)
		))

	var archived_ids: Array = ConversationState.archived_conversation_ids()
	if not archived_ids.is_empty():
		list.add_child(_make_archives_toggle(archived_ids.size()))
		if archives_expanded:
			for conversation_id in archived_ids:
				var state: Dictionary = ConversationState.conversation(conversation_id)
				list.add_child(_make_archived_conversation_entry(
					conversation_id,
					str(state.get("display_name", conversation_id)),
					str(state.get("title", "")),
					ConversationState.archived_preview_text(conversation_id),
					bool(state.get("available", false))
				))

func _make_j1_v2_first_open_note() -> PanelContainer:
	var card := PanelContainer.new()
	var style := StyleBoxFlat.new()
	style.bg_color = Color("24202a")
	style.border_color = Color("d58a35")
	style.set_border_width_all(1)
	style.corner_radius_top_left = 12
	style.corner_radius_top_right = 12
	style.corner_radius_bottom_left = 12
	style.corner_radius_bottom_right = 12
	style.content_margin_left = 12
	style.content_margin_right = 12
	style.content_margin_top = 10
	style.content_margin_bottom = 10
	card.add_theme_stylebox_override("panel", style)

	var label := Label.new()
	label.text = "Ton téléphone s’allume. Plusieurs conversations attendent. La première que tu ouvres donnera le ton de la journée."
	label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	label.add_theme_font_size_override("font_size", 13)
	label.add_theme_color_override("font_color", Color("f1d6a8"))
	card.add_child(label)
	return card

func _make_archives_toggle(count: int) -> Button:
	var button := Button.new()
	button.text = ("Archives" if not archives_expanded else "Archives ouvertes") + " — Jours précédents (" + str(count) + ")"
	button.tooltip_text = "Afficher ou masquer les conversations des jours passés"
	button.custom_minimum_size = Vector2(0, 34)
	button.add_theme_font_size_override("font_size", 12)
	button.pressed.connect(func() -> void:
		archives_expanded = not archives_expanded
		_rebuild_ui()
	)
	return button

func _make_archived_conversation_entry(conversation_id: String, contact_name: String, title: String, meta: String, available: bool) -> Button:
	return _make_conversation_entry(
		conversation_id,
		contact_name,
		title,
		meta,
		available,
		false
	)

func _make_day_transition_button() -> Button:
	var button := Button.new()
	var next_day: int = ConversationState.current_day + 1
	button.text = "Passer au Jour " + str(next_day)
	button.tooltip_text = "Passer au jour suivant"
	button.custom_minimum_size = Vector2(0, 40)
	button.add_theme_font_size_override("font_size", 14)
	button.pressed.connect(func() -> void:
		ConversationState.advance_to_next_day()
		get_tree().reload_current_scene()
	)
	return button

func _make_header_debug_controls() -> HBoxContainer:
	var debug_row := HBoxContainer.new()
	debug_row.alignment = BoxContainer.ALIGNMENT_END
	debug_row.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	debug_row.add_theme_constant_override("separation", 6)

	var reset_button := Button.new()
	reset_button.text = "Reset"
	reset_button.tooltip_text = "Debug: effacer la progression locale"
	reset_button.custom_minimum_size = Vector2(0, 28)
	reset_button.add_theme_font_size_override("font_size", 11)
	reset_button.pressed.connect(func() -> void:
		ConversationState.reset_progression()
		get_tree().reload_current_scene()
	)
	debug_row.add_child(reset_button)
	debug_row.add_child(_make_test_fast_mode_button())
	debug_row.add_child(_make_force_day_button())
	debug_row.add_child(_make_experimental_j1_v2_button())
	return debug_row

func _make_test_fast_mode_button() -> Button:
	var button := Button.new()
	if ConversationState.test_fast_mode_enabled:
		button.text = "Mode test rapide : ON"
	else:
		button.text = "Mode test rapide : OFF"
	button.tooltip_text = "Debug: accélère les délais de lecture pour rejouer J1-J3"
	button.custom_minimum_size = Vector2(0, 28)
	button.add_theme_font_size_override("font_size", 11)
	button.pressed.connect(_on_test_fast_mode_pressed)
	return button

func _on_test_fast_mode_pressed() -> void:
	ConversationState.set_test_fast_mode_enabled(not ConversationState.test_fast_mode_enabled)
	get_tree().reload_current_scene()

func _make_force_day_button() -> Button:
	var button := Button.new()
	var next_day: int = ConversationState.current_day + 1
	button.text = "Debug Jour " + str(next_day)
	button.tooltip_text = "Debug: forcer la bascule au jour suivant pour les playtests"
	button.custom_minimum_size = Vector2(0, 28)
	button.add_theme_font_size_override("font_size", 11)
	button.disabled = ConversationState.current_day >= 6
	button.pressed.connect(_on_force_day_pressed)
	return button

func _on_force_day_pressed() -> void:
	ConversationState.force_advance_to_next_day_for_testing()
	get_tree().reload_current_scene()

func _make_experimental_j1_v2_button() -> Button:
	var button := Button.new()
	if ConversationState.experimental_j1_v2_enabled:
		button.text = "Mode J1 V2 : ON"
	else:
		button.text = "Mode J1 V2 : OFF"
	button.tooltip_text = "Debug: affiche les conversations expérimentales de refonte J1 V2"
	button.custom_minimum_size = Vector2(0, 28)
	button.add_theme_font_size_override("font_size", 11)
	button.pressed.connect(_on_experimental_j1_v2_pressed)
	return button

func _on_experimental_j1_v2_pressed() -> void:
	ConversationState.set_experimental_j1_v2_enabled(not ConversationState.experimental_j1_v2_enabled)
	get_tree().reload_current_scene()

func _make_conversation_entry(conversation_id: String, contact_name: String, title: String, meta: String, available: bool, has_new: bool) -> Button:
	var button := Button.new()
	button.text = ""
	button.custom_minimum_size = Vector2(0, 140)
	button.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	button.disabled = not available
	button.focus_mode = Control.FOCUS_ALL
	button.tooltip_text = "Conversation prête" if available else "Branchement prévu, contenu à fournir plus tard"
	button.add_theme_stylebox_override("normal", _entry_style(_contact_color(conversation_id), false))
	button.add_theme_stylebox_override("hover", _entry_style(_contact_color(conversation_id), true))
	button.add_theme_stylebox_override("focus", _entry_style(_contact_color(conversation_id), true))
	button.add_theme_stylebox_override("disabled", _entry_style(Color("44444c"), false))

	var margin := MarginContainer.new()
	margin.set_anchors_preset(Control.PRESET_FULL_RECT)
	margin.mouse_filter = Control.MOUSE_FILTER_IGNORE
	margin.add_theme_constant_override("margin_left", 12)
	margin.add_theme_constant_override("margin_right", 12)
	margin.add_theme_constant_override("margin_top", 10)
	margin.add_theme_constant_override("margin_bottom", 10)
	button.add_child(margin)

	var row := HBoxContainer.new()
	row.mouse_filter = Control.MOUSE_FILTER_IGNORE
	row.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	row.custom_minimum_size = Vector2(0, 0)
	row.add_theme_constant_override("separation", 8)
	margin.add_child(row)

	var accent := ColorRect.new()
	accent.color = _contact_color(conversation_id)
	accent.custom_minimum_size = Vector2(4, 0)
	accent.mouse_filter = Control.MOUSE_FILTER_IGNORE
	row.add_child(accent)

	var text_box := VBoxContainer.new()
	text_box.mouse_filter = Control.MOUSE_FILTER_IGNORE
	text_box.custom_minimum_size = Vector2(0, 0)
	text_box.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	text_box.add_theme_constant_override("separation", 4)
	row.add_child(text_box)

	var top_row := HBoxContainer.new()
	top_row.mouse_filter = Control.MOUSE_FILTER_IGNORE
	top_row.add_theme_constant_override("separation", 8)
	text_box.add_child(top_row)

	var contact_name_label := Label.new()
	contact_name_label.text = contact_name
	contact_name_label.add_theme_font_size_override("font_size", 17)
	contact_name_label.mouse_filter = Control.MOUSE_FILTER_IGNORE
	contact_name_label.clip_text = true
	contact_name_label.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top_row.add_child(contact_name_label)

	if has_new:
		top_row.add_child(_make_new_badge())

	var line := Label.new()
	line.text = title
	line.custom_minimum_size = Vector2(0, 20)
	line.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	line.add_theme_font_size_override("font_size", 13)
	line.add_theme_color_override("font_color", Color("b8b8c6"))
	line.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	line.text_overrun_behavior = TextServer.OVERRUN_TRIM_ELLIPSIS
	line.clip_text = false
	line.mouse_filter = Control.MOUSE_FILTER_IGNORE
	text_box.add_child(line)

	var preview := Label.new()
	preview.text = _short_preview(meta)
	preview.custom_minimum_size = Vector2(0, 44)
	preview.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	preview.size_flags_vertical = Control.SIZE_EXPAND_FILL
	preview.add_theme_font_size_override("font_size", 13)
	preview.add_theme_color_override("font_color", Color("f1d6a8") if has_new else Color("c4c4cf"))
	preview.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	preview.text_overrun_behavior = TextServer.OVERRUN_TRIM_ELLIPSIS
	preview.clip_text = false
	preview.mouse_filter = Control.MOUSE_FILTER_IGNORE
	text_box.add_child(preview)

	button.pressed.connect(func() -> void:
		ConversationState.set_current_conversation(conversation_id)
		get_tree().change_scene_to_file(CHAT_SCENE)
	)
	return button

func _make_new_badge() -> PanelContainer:
	var badge := PanelContainer.new()
	badge.mouse_filter = Control.MOUSE_FILTER_IGNORE
	var style := StyleBoxFlat.new()
	style.bg_color = Color("d58a35")
	style.corner_radius_top_left = 8
	style.corner_radius_top_right = 8
	style.corner_radius_bottom_left = 8
	style.corner_radius_bottom_right = 8
	style.content_margin_left = 7
	style.content_margin_right = 7
	style.content_margin_top = 3
	style.content_margin_bottom = 3
	badge.add_theme_stylebox_override("panel", style)
	var label := Label.new()
	label.text = "nouveau"
	label.add_theme_font_size_override("font_size", 11)
	label.add_theme_color_override("font_color", Color("17130f"))
	label.mouse_filter = Control.MOUSE_FILTER_IGNORE
	badge.add_child(label)
	return badge

func _short_preview(text: String) -> String:
	if text.length() <= 96:
		return text
	return text.substr(0, 93) + "…"

func _contact_color(conversation_id: String) -> Color:
	if conversation_id.begins_with("sarah"):
		return SARAH_COLOR
	if conversation_id.begins_with("camille"):
		return CAMILLE_COLOR
	if conversation_id.begins_with("maya"):
		return MAYA_COLOR
	if conversation_id.begins_with("ines"):
		return INES_COLOR
	if conversation_id.begins_with("nico"):
		return NICO_COLOR
	return SYSTEM_COLOR

func _entry_style(accent: Color, highlighted: bool) -> StyleBoxFlat:
	var style := StyleBoxFlat.new()
	style.bg_color = Color("24242e") if highlighted else Color("202028")
	style.border_color = accent
	style.set_border_width_all(1)
	style.corner_radius_top_left = 14
	style.corner_radius_top_right = 14
	style.corner_radius_bottom_left = 14
	style.corner_radius_bottom_right = 14
	style.content_margin_left = 8
	style.content_margin_right = 8
	style.content_margin_top = 6
	style.content_margin_bottom = 6
	return style
