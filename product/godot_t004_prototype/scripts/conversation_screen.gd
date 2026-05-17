extends Control

const JSON_PATH := "res://data/camille_j1_complete.json"
const DEBUG_DELAY_MIN_SECONDS := 1.1
const DEBUG_DELAY_MAX_SECONDS := 6.5
const PRE_CHOICE_DELAY_SECONDS := 0.8
const NARRATION_READ_SECONDS := 1.6
const MIN_BETWEEN_MESSAGES_SECONDS := 0.6
const FAST_TYPING_DELAY_MAX_SECONDS := 0.35
const FAST_PRE_CHOICE_DELAY_SECONDS := 0.1
const FAST_NARRATION_READ_SECONDS := 0.2
const FAST_MIN_BETWEEN_MESSAGES_SECONDS := 0.1
const SHOW_DEBUG_STATE := false
const CHOICE_PANEL_MAX_HEIGHT := 260.0
const BUBBLE_WIDTH := 284.0
const PLAYER_COLOR := Color("2f73e0")
const CAMILLE_COLOR := Color("46345f")
const SARAH_COLOR := Color("a96d2a")
const MAYA_COLOR := Color("2f6f73")
const INES_COLOR := Color("7b3f67")
const NICO_COLOR := Color("426c2f")
const SYSTEM_COLOR := Color("2d2d35")
const WAIT_COLOR := Color("3a3130")
const INTROSPECTION_COLOR := Color("26333b")

var conversation: Dictionary = {}
var nodes_by_id: Dictionary = {}
var game_state: Dictionary = {}
var current_contact_id := "camille"
var current_display_name := "Camille"
var current_json_path := JSON_PATH

var phone_frame: PanelContainer
var root_container: VBoxContainer
var scroll: ScrollContainer
var message_list: VBoxContainer
var choice_panel: PanelContainer
var choice_scroll: ScrollContainer
var choice_box: VBoxContainer
var state_label: Label
var typing_row: HBoxContainer
var typing_bubble: PanelContainer
var typing_label: Label
var typing_indicator_active: bool = false
var typing_dot_count: int = 0
var quick_switch_target_id: String = ""
var quick_switch_button: Button

func _ready() -> void:
	current_contact_id = ConversationState.current_contact_id()
	current_display_name = ConversationState.current_display_name()
	current_json_path = ConversationState.current_json_path()
	_build_ui()
	_load_conversation(current_json_path)
	ConversationState.mark_current_opened()
	if ConversationState.has_current_state():
		game_state = ConversationState.current_game_state()
		await _restore_current_messages()
	if not ConversationState.can_current_block_play():
		_show_waiting_state()
		return
	ConversationState.mark_current_block_active()
	if ConversationState.has_current_state():
		if ConversationState.current_active_choice_node() != "":
			_show_choice(nodes_by_id[ConversationState.current_active_choice_node()])
		elif ConversationState.current_next_node() != "" and not ConversationState.current_done():
			_advance_to(ConversationState.current_next_node())
	else:
		ConversationState.current()["started"] = true
		_advance_to(ConversationState.current_block_start_node(), true)

func _build_ui() -> void:
	var background := ColorRect.new()
	background.color = Color("0f0f14")
	background.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(background)

	var outer := MarginContainer.new()
	outer.set_anchors_preset(Control.PRESET_FULL_RECT)
	outer.add_theme_constant_override("margin_left", 14)
	outer.add_theme_constant_override("margin_right", 14)
	outer.add_theme_constant_override("margin_top", 18)
	outer.add_theme_constant_override("margin_bottom", 18)
	add_child(outer)

	phone_frame = PanelContainer.new()
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
	phone_margin.add_theme_constant_override("margin_top", 12)
	phone_margin.add_theme_constant_override("margin_bottom", 12)
	phone_frame.add_child(phone_margin)

	root_container = VBoxContainer.new()
	root_container.add_theme_constant_override("separation", 8)
	phone_margin.add_child(root_container)

	root_container.add_child(_make_header())
	_refresh_quick_switch_notification()

	scroll = ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	root_container.add_child(scroll)

	message_list = VBoxContainer.new()
	message_list.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	message_list.add_theme_constant_override("separation", 10)
	scroll.add_child(message_list)

	choice_panel = PanelContainer.new()
	var choice_style := StyleBoxFlat.new()
	choice_style.bg_color = Color("20202a")
	choice_style.border_color = _contact_color(current_contact_id)
	choice_style.set_border_width_all(1)
	choice_style.corner_radius_top_left = 14
	choice_style.corner_radius_top_right = 14
	choice_style.corner_radius_bottom_left = 14
	choice_style.corner_radius_bottom_right = 14
	choice_style.content_margin_left = 8
	choice_style.content_margin_right = 8
	choice_style.content_margin_top = 8
	choice_style.content_margin_bottom = 8
	choice_panel.add_theme_stylebox_override("panel", choice_style)
	choice_panel.visible = false
	root_container.add_child(choice_panel)

	choice_scroll = ScrollContainer.new()
	choice_scroll.custom_minimum_size = Vector2(0, CHOICE_PANEL_MAX_HEIGHT)
	choice_scroll.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	choice_scroll.size_flags_vertical = Control.SIZE_SHRINK_END
	choice_scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	choice_scroll.vertical_scroll_mode = ScrollContainer.SCROLL_MODE_AUTO
	choice_panel.add_child(choice_scroll)

	choice_box = VBoxContainer.new()
	choice_box.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	choice_box.size_flags_vertical = Control.SIZE_SHRINK_BEGIN
	choice_box.add_theme_constant_override("separation", 6)
	choice_scroll.add_child(choice_box)

	state_label = Label.new()
	state_label.text = "État: {}"
	state_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	state_label.visible = SHOW_DEBUG_STATE
	root_container.add_child(state_label)

func _make_header() -> Control:
	var header_panel := PanelContainer.new()
	header_panel.custom_minimum_size = Vector2(0, 58)
	var header_style := StyleBoxFlat.new()
	header_style.bg_color = Color("22222c")
	header_style.corner_radius_top_left = 20
	header_style.corner_radius_top_right = 20
	header_style.corner_radius_bottom_left = 20
	header_style.corner_radius_bottom_right = 20
	header_style.content_margin_left = 12
	header_style.content_margin_right = 12
	header_style.content_margin_top = 8
	header_style.content_margin_bottom = 8
	header_style.border_color = _contact_color(current_contact_id)
	header_style.set_border_width_all(1)
	header_panel.add_theme_stylebox_override("panel", header_style)

	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 10)
	header_panel.add_child(row)

	var back := Button.new()
	back.text = "‹"
	back.add_theme_font_size_override("font_size", 22)
	back.custom_minimum_size = Vector2(34, 34)
	back.tooltip_text = "Retour conversations"
	back.pressed.connect(func() -> void:
		get_tree().change_scene_to_file("res://scenes/conversation_list.tscn")
	)
	row.add_child(back)

	var avatar := Label.new()
	avatar.text = current_display_name.substr(0, 1).to_upper()
	avatar.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	avatar.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	avatar.custom_minimum_size = Vector2(34, 34)
	avatar.add_theme_font_size_override("font_size", 18)
	avatar.add_theme_color_override("font_color", _contact_color(current_contact_id).lightened(0.45))
	row.add_child(avatar)

	var info := VBoxContainer.new()
	info.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	row.add_child(info)

	var header_name_label := Label.new()
	header_name_label.text = current_display_name
	header_name_label.add_theme_font_size_override("font_size", 18)
	info.add_child(header_name_label)

	var status := Label.new()
	status.text = "en ligne · " + ConversationState.day_label_for_conversation(ConversationState.current_conversation_id)
	status.add_theme_font_size_override("font_size", 12)
	status.add_theme_color_override("font_color", Color("8bd99a"))
	info.add_child(status)

	return header_panel

func _refresh_quick_switch_notification() -> void:
	var next_target_id: String = ConversationState.quick_switch_new_conversation_id()
	if next_target_id == quick_switch_target_id and quick_switch_button != null:
		return
	if quick_switch_button != null:
		root_container.remove_child(quick_switch_button)
		quick_switch_button.queue_free()
		quick_switch_button = null
	quick_switch_target_id = next_target_id
	if quick_switch_target_id == "":
		return
	quick_switch_button = _make_quick_switch_notification(quick_switch_target_id)
	root_container.add_child(quick_switch_button)
	root_container.move_child(quick_switch_button, 1)

func _make_quick_switch_notification(target_id: String) -> Button:
	var button := Button.new()
	var target_state: Dictionary = ConversationState.conversation(target_id)
	var display_name: String = str(target_state.get("display_name", target_id))
	button.text = "Nouveau message de " + display_name + " · Ouvrir"
	button.tooltip_text = "Ouvrir cette conversation sans repasser par Messages"
	button.custom_minimum_size = Vector2(0, 40)
	button.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	button.focus_mode = Control.FOCUS_ALL
	button.add_theme_font_size_override("font_size", 13)
	button.add_theme_color_override("font_color", Color("f8eddc"))
	button.add_theme_stylebox_override("normal", _quick_switch_style(false))
	button.add_theme_stylebox_override("hover", _quick_switch_style(true))
	button.add_theme_stylebox_override("focus", _quick_switch_style(true))
	button.pressed.connect(_open_quick_switch_conversation.bind(target_id))
	return button

func _quick_switch_style(highlighted: bool) -> StyleBoxFlat:
	var style := StyleBoxFlat.new()
	style.bg_color = Color("33271f") if highlighted else Color("28232a")
	style.border_color = Color("d58a35")
	style.set_border_width_all(1)
	style.corner_radius_top_left = 12
	style.corner_radius_top_right = 12
	style.corner_radius_bottom_left = 12
	style.corner_radius_bottom_right = 12
	style.content_margin_left = 12
	style.content_margin_right = 12
	style.content_margin_top = 6
	style.content_margin_bottom = 6
	return style

func _open_quick_switch_conversation(target_id: String) -> void:
	if target_id == "" or not ConversationState.conversations.has(target_id):
		return
	ConversationState.set_current_conversation(target_id)
	ConversationState.mark_conversation_read(target_id)
	get_tree().change_scene_to_file("res://scenes/conversation_screen.tscn")

func _load_conversation(path: String) -> void:
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		_add_bubble("system", "Erreur: JSON introuvable: " + path)
		return

	var parsed = JSON.parse_string(file.get_as_text())
	if typeof(parsed) != TYPE_DICTIONARY:
		_add_bubble("system", "Erreur: JSON invalide")
		return

	conversation = parsed
	nodes_by_id.clear()
	for node in conversation.get("nodes", []):
		nodes_by_id[str(node.get("id", ""))] = node

func _restore_current_messages() -> void:
	for entry in ConversationState.current_messages():
		await _add_bubble(str(entry.get("sender", "system")), str(entry.get("text", "")), false)
	_update_state_label()

func _show_waiting_state() -> void:
	_clear_choices()
	_hide_typing_indicator()
	await _add_system_note(ConversationState.current_waiting_text(), false)

func _advance_to(node_id: String, immediate: bool = false) -> void:
	if not nodes_by_id.has(node_id):
		_add_bubble("system", "Erreur: node introuvable: " + node_id)
		return

	var node: Dictionary = nodes_by_id[node_id]
	var node_type := str(node.get("type", "message"))

	if node_type == "choice":
		ConversationState.set_current_active_choice(node_id)
		if not immediate:
			await get_tree().create_timer(_pre_choice_delay_seconds()).timeout
		_show_choice(node)
		return

	if not immediate:
		await _wait_before_node(node)

	var sender := str(node.get("sender", "system"))
	_add_bubble(sender, str(node.get("text", "")))
	_apply_effects(node.get("effects", {}))
	ConversationState.handle_dynamic_notification(current_contact_id, node_id)
	_refresh_quick_switch_notification()

	if node_type == "end":
		ConversationState.complete_current_block("")
		ConversationState.repair_available_block_notifications()
		_refresh_quick_switch_notification()
		ConversationState.mark_current_done()
		return

	var next_id := str(node.get("next", ""))
	if next_id != "":
		ConversationState.set_current_next_node(next_id)
		if ConversationState.is_current_block_end_node(node_id):
			ConversationState.complete_current_block(next_id)
			ConversationState.repair_available_block_notifications()
			_refresh_quick_switch_notification()
			_show_waiting_state()
			return
		if sender == "system":
			await get_tree().create_timer(_narration_read_seconds()).timeout
		else:
			await get_tree().create_timer(_between_messages_delay_seconds()).timeout
		_advance_to(next_id)

func _wait_before_node(node: Dictionary) -> void:
	var delay_seconds := float(node.get("delay", 0))
	if delay_seconds <= 0.0:
		return

	var sender := str(node.get("sender", "system"))
	if sender == current_contact_id:
		await _show_typing_indicator(sender)
		await get_tree().create_timer(_display_delay_for_text(str(node.get("text", "")), delay_seconds)).timeout
		_hide_typing_indicator()
	elif sender == "player":
		return
	else:
		_hide_typing_indicator()
		await get_tree().create_timer(_display_delay_for_text(str(node.get("text", "")), delay_seconds) * 0.65).timeout

func _show_choice(node: Dictionary) -> void:
	choice_panel.visible = true

	var prompt := Label.new()
	prompt.text = "Répondre"
	prompt.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	prompt.add_theme_font_size_override("font_size", 12)
	prompt.add_theme_color_override("font_color", Color("b8b8c6"))
	choice_box.add_child(prompt)

	for choice in node.get("choices", []):
		var choice_text := str(choice.get("text", "..."))
		var button := Button.new()
		button.text = ""
		button.custom_minimum_size = Vector2(0, _choice_button_height(choice_text))
		button.focus_mode = Control.FOCUS_ALL
		button.add_theme_stylebox_override("normal", _choice_button_style(false))
		button.add_theme_stylebox_override("hover", _choice_button_style(true))
		button.add_theme_stylebox_override("focus", _choice_button_style(true))

		var margin := MarginContainer.new()
		margin.set_anchors_preset(Control.PRESET_FULL_RECT)
		margin.mouse_filter = Control.MOUSE_FILTER_IGNORE
		margin.add_theme_constant_override("margin_left", 10)
		margin.add_theme_constant_override("margin_right", 10)
		margin.add_theme_constant_override("margin_top", 6)
		margin.add_theme_constant_override("margin_bottom", 6)
		button.add_child(margin)

		var label := Label.new()
		label.text = choice_text
		label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		label.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
		label.add_theme_font_size_override("font_size", 14)
		label.add_theme_color_override("font_color", Color("f1f1f5"))
		label.mouse_filter = Control.MOUSE_FILTER_IGNORE
		margin.add_child(label)

		button.pressed.connect(_on_choice_pressed.bind(choice))
		choice_box.add_child(button)

	await get_tree().process_frame
	choice_scroll.scroll_vertical = 0
	_ensure_last_message_visible()

func _choice_button_height(text: String) -> int:
	if text.length() > 96:
		return 92
	if text.length() > 58:
		return 74
	if text.length() > 32:
		return 58
	return 46

func _choice_button_style(highlighted: bool) -> StyleBoxFlat:
	var style := StyleBoxFlat.new()
	style.bg_color = Color("2c2c38") if highlighted else Color("24242e")
	style.border_color = _contact_color(current_contact_id)
	style.set_border_width_all(1)
	style.corner_radius_top_left = 10
	style.corner_radius_top_right = 10
	style.corner_radius_bottom_left = 10
	style.corner_radius_bottom_right = 10
	return style

func _on_choice_pressed(choice: Dictionary) -> void:
	_lock_choice_buttons()
	ConversationState.record_current_choice(str(choice.get("id", "")))
	_apply_effects(choice.get("effects", {}))
	_clear_choices()
	_advance_to(str(choice.get("next", "")), true)

func _lock_choice_buttons() -> void:
	for child in choice_box.get_children():
		if child is Button:
			child.disabled = true

func _apply_effects(effects_value) -> void:
	if typeof(effects_value) != TYPE_DICTIONARY:
		return
	var effects: Dictionary = effects_value
	for key in effects.keys():
		if key == "flags":
			if not game_state.has("flags"):
				game_state["flags"] = []
			for flag in effects["flags"]:
				if not game_state["flags"].has(flag):
					game_state["flags"].append(flag)
		elif typeof(effects[key]) == TYPE_INT or typeof(effects[key]) == TYPE_FLOAT:
			game_state[key] = game_state.get(key, 0) + effects[key]
	_update_state_label()
	ConversationState.set_current_game_state(game_state)

func _add_bubble(sender: String, text: String, record_state: bool = true) -> void:
	if sender == "system":
		_add_system_note(text, record_state)
		return

	var row := HBoxContainer.new()
	row.size_flags_horizontal = Control.SIZE_EXPAND_FILL

	var left_spacer := Control.new()
	var right_spacer := Control.new()
	left_spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	right_spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL

	var bubble := PanelContainer.new()
	bubble.custom_minimum_size = Vector2(BUBBLE_WIDTH, 42)
	var style := StyleBoxFlat.new()
	style.corner_radius_top_left = 16
	style.corner_radius_top_right = 16
	style.corner_radius_bottom_left = 16
	style.corner_radius_bottom_right = 16
	style.content_margin_left = 12
	style.content_margin_right = 12
	style.content_margin_top = 9
	style.content_margin_bottom = 9

	if sender == "player":
		style.bg_color = PLAYER_COLOR
		style.corner_radius_bottom_right = 5
		row.add_child(left_spacer)
		row.add_child(bubble)
	else:
		style.bg_color = _contact_color(sender)
		style.corner_radius_bottom_left = 5
		row.add_child(bubble)
		row.add_child(right_spacer)

	bubble.add_theme_stylebox_override("panel", style)

	var label := Label.new()
	label.text = _display_sender(sender) + text
	label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	label.add_theme_font_size_override("font_size", 16)
	label.add_theme_color_override("font_color", Color("f1f1f5"))
	bubble.add_child(label)

	message_list.add_child(row)
	if record_state:
		ConversationState.record_current_message(sender, text)
	await get_tree().process_frame
	_ensure_last_message_visible()

func _add_system_note(text: String, record_state: bool = true) -> void:
	var row := HBoxContainer.new()
	row.size_flags_horizontal = Control.SIZE_EXPAND_FILL

	var left_spacer := Control.new()
	var right_spacer := Control.new()
	left_spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	right_spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	row.add_child(left_spacer)

	var card := PanelContainer.new()
	card.custom_minimum_size = Vector2(250, 0)
	var style := StyleBoxFlat.new()
	style.corner_radius_top_left = 10
	style.corner_radius_top_right = 10
	style.corner_radius_bottom_left = 10
	style.corner_radius_bottom_right = 10
	style.content_margin_left = 14
	style.content_margin_right = 14
	style.content_margin_top = 10
	style.content_margin_bottom = 10

	var variant := _system_variant(text)
	if variant == "wait":
		style.bg_color = WAIT_COLOR
	elif variant == "introspection":
		style.bg_color = INTROSPECTION_COLOR
	else:
		style.bg_color = SYSTEM_COLOR
	card.add_theme_stylebox_override("panel", style)

	var label := RichTextLabel.new()
	label.bbcode_enabled = true
	label.fit_content = true
	label.scroll_active = false
	label.custom_minimum_size = Vector2(250, 0)
	label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	label.add_theme_font_size_override("normal_font_size", 14)
	label.add_theme_color_override("default_color", Color("c8c8d2"))
	label.bbcode_text = "[center][i]" + _escape_bbcode(text) + "[/i][/center]"
	card.add_child(label)

	row.add_child(card)
	row.add_child(right_spacer)
	message_list.add_child(row)
	if record_state:
		ConversationState.record_current_message("system", text)
	await get_tree().process_frame
	_ensure_last_message_visible()

func _escape_bbcode(text: String) -> String:
	return text.replace("[", "［").replace("]", "］")

func _display_sender(sender: String) -> String:
	if sender == "player":
		return ""
	return current_display_name + " · "

func _contact_color(contact_id: String) -> Color:
	if contact_id == "sarah":
		return SARAH_COLOR
	if contact_id == "camille":
		return CAMILLE_COLOR
	if contact_id == "maya":
		return MAYA_COLOR
	if contact_id == "ines":
		return INES_COLOR
	if contact_id == "nico":
		return NICO_COLOR
	return SYSTEM_COLOR

func _system_variant(text: String) -> String:
	var lower := text.to_lower()
	if lower.begins_with("fin j1"):
		return "system"
	if lower.contains("attente") or lower.contains("notification") or lower.contains("écran") or lower.contains("calme"):
		return "wait"
	return "introspection"

func _display_delay_for_text(text: String, source_delay: float) -> float:
	if source_delay <= 0.0:
		return 0.0
	if ConversationState.test_fast_mode_enabled:
		return min(source_delay, FAST_TYPING_DELAY_MAX_SECONDS)
	var length_delay := 1.1 + float(text.length()) / 42.0
	return clamp(length_delay, DEBUG_DELAY_MIN_SECONDS, DEBUG_DELAY_MAX_SECONDS)

func _pre_choice_delay_seconds() -> float:
	if ConversationState.test_fast_mode_enabled:
		return FAST_PRE_CHOICE_DELAY_SECONDS
	return PRE_CHOICE_DELAY_SECONDS

func _narration_read_seconds() -> float:
	if ConversationState.test_fast_mode_enabled:
		return FAST_NARRATION_READ_SECONDS
	return NARRATION_READ_SECONDS

func _between_messages_delay_seconds() -> float:
	if ConversationState.test_fast_mode_enabled:
		return FAST_MIN_BETWEEN_MESSAGES_SECONDS
	return MIN_BETWEEN_MESSAGES_SECONDS

func _ensure_last_message_visible() -> void:
	var max_scroll := int(scroll.get_v_scroll_bar().max_value)
	if scroll.scroll_vertical < max_scroll:
		scroll.scroll_vertical = max_scroll

func _add_typing_bubble() -> void:
	_remove_typing_bubble()
	typing_row = HBoxContainer.new()
	typing_row.size_flags_horizontal = Control.SIZE_EXPAND_FILL

	var right_spacer := Control.new()
	right_spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL

	typing_bubble = PanelContainer.new()
	typing_bubble.custom_minimum_size = Vector2(96, 44)
	var style := StyleBoxFlat.new()
	style.bg_color = _contact_color(current_contact_id).lightened(0.08)
	style.border_color = _contact_color(current_contact_id).lightened(0.32)
	style.set_border_width_all(1)
	style.corner_radius_top_left = 17
	style.corner_radius_top_right = 17
	style.corner_radius_bottom_left = 5
	style.corner_radius_bottom_right = 17
	style.content_margin_left = 18
	style.content_margin_right = 18
	style.content_margin_top = 9
	style.content_margin_bottom = 9
	typing_bubble.add_theme_stylebox_override("panel", style)

	typing_label = Label.new()
	typing_label.text = "..."
	typing_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	typing_label.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	typing_label.add_theme_font_size_override("font_size", 24)
	typing_label.add_theme_color_override("font_color", Color("f7f7fb"))
	typing_bubble.add_child(typing_label)

	typing_row.add_child(typing_bubble)
	typing_row.add_child(right_spacer)
	message_list.add_child(typing_row)
	await get_tree().process_frame
	_ensure_last_message_visible()

func _remove_typing_bubble() -> void:
	if typing_row != null:
		message_list.remove_child(typing_row)
		typing_row.queue_free()
	typing_row = null
	typing_bubble = null
	typing_label = null

func _show_typing_indicator(sender: String) -> void:
	if sender != current_contact_id:
		_hide_typing_indicator()
		return
	typing_dot_count = 1
	typing_indicator_active = true
	await _add_typing_bubble()
	if typing_label != null:
		typing_label.modulate.a = 0.72
		typing_label.text = _typing_indicator_text()
	_animate_typing_indicator()

func _typing_indicator_text() -> String:
	return ".".repeat(typing_dot_count)

func _animate_typing_indicator() -> void:
	while typing_indicator_active and typing_row != null:
		typing_dot_count = (typing_dot_count % 3) + 1
		if typing_label != null:
			typing_label.text = _typing_indicator_text()
			typing_label.modulate.a = 0.55 + 0.15 * float(typing_dot_count)
		await get_tree().create_timer(0.32).timeout

func _hide_typing_indicator() -> void:
	typing_indicator_active = false
	typing_dot_count = 0
	_remove_typing_bubble()

func _clear_choices() -> void:
	for child in choice_box.get_children():
		child.queue_free()
	choice_panel.visible = false

func _update_state_label() -> void:
	state_label.text = "État: " + JSON.stringify(game_state)
