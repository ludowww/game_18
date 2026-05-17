extends Node

const SAVE_PATH := "user://double_vie_save.json"
const SAVE_VERSION := 4
const REQUIRED_CONVERSATIONS_BY_DAY := {
	1: ["camille", "sarah"],
	2: ["camille_j2", "sarah_j2"],
	3: ["camille_j3", "sarah_j3"],
	4: ["camille_j4", "maya_j4", "ines_j4", "nico_j4"],
	5: ["sarah_j5", "camille_j5", "nico_j5", "maya_j5"],
	6: ["sarah_j6", "camille_j6", "nico_j6", "maya_j6", "ines_j6", "finales_mvp"]
}
const BLOCK_STATUS_LOCKED := "locked"
const BLOCK_STATUS_AVAILABLE := "available"
const BLOCK_STATUS_ACTIVE := "active"
const BLOCK_STATUS_DONE := "done"
const BLOCKS_CONFIG_PATH := "res://data/conversation_blocks.json"
const V2_VARIABLE_DEFAULTS := {
	"confiance_sarah": 55,
	"distance_sarah": 35,
	"tension_camille": 55,
	"respect_camille": 50,
	"pression_camille": 30,
	"intimite_sarah": 45,
	"intimite_camille": 45,
	"attente_image_camille": 0,
	"suspicion_maya": 40,
	"dette_nico": 20,
	"fuite_ines": 10,
	"coherence": 60,
	"culpabilite": 35,
	"risque_exposition": 25,
	"fatigue_emotionnelle": 20
}

var current_conversation_id: String = "camille"
var current_day: int = 1
var completed_days: Array = []
var day_transition_available: bool = false
var test_fast_mode_enabled: bool = false
var experimental_j1_v2_enabled: bool = false

var conversations: Dictionary = _default_conversations()
var conversation_block_defs: Dictionary = {}
var conversation_block_order: Array = []
var conversation_blocks: Dictionary = {}
var dynamic_notifications_fired: Array = []
var global_game_state: Dictionary = _default_global_game_state()

func set_test_fast_mode_enabled(enabled: bool) -> void:
	test_fast_mode_enabled = enabled

func set_experimental_j1_v2_enabled(enabled: bool) -> void:
	experimental_j1_v2_enabled = enabled

func _default_global_game_state() -> Dictionary:
	var state: Dictionary = {
		"variables": {},
		"flags": []
	}
	for key in V2_VARIABLE_DEFAULTS.keys():
		state["variables"][key] = int(V2_VARIABLE_DEFAULTS[key])
	return state

func global_state() -> Dictionary:
	return global_game_state.duplicate(true)

func apply_global_effects(effects_value) -> Dictionary:
	if typeof(effects_value) != TYPE_DICTIONARY:
		return global_state()
	var effects: Dictionary = effects_value
	for key in effects.keys():
		if key == "flags":
			if typeof(effects[key]) != TYPE_ARRAY:
				continue
			for flag in effects["flags"]:
				if not global_game_state["flags"].has(flag):
					global_game_state["flags"].append(flag)
		elif V2_VARIABLE_DEFAULTS.has(key) and (typeof(effects[key]) == TYPE_INT or typeof(effects[key]) == TYPE_FLOAT):
			var current_value: int = int(global_game_state["variables"].get(key, V2_VARIABLE_DEFAULTS[key]))
			global_game_state["variables"][key] = int(clamp(current_value + int(effects[key]), 0, 100))
	save_progression()
	return global_state()

func _ready() -> void:
	_load_conversation_block_defs()
	conversation_blocks = _default_conversation_blocks()
	load_progression()
	repair_available_block_notifications()
	refresh_day_progression()

func _default_conversations() -> Dictionary:
	return {
		"camille": _new_conversation_state(
			"camille",
			"camille",
			"Camille",
			"Jour 1 — conversation complète MVP",
			"res://data/camille_j1_complete.json",
			1,
			true,
			false
		),
		"sarah": _new_conversation_state(
			"sarah",
			"sarah",
			"Sarah",
			"Jour 1 — conversation complète MVP",
			"res://data/sarah_j1_complete.json",
			1,
			true,
			false
		),
		"j1_00_reveil_v2": _new_conversation_state(
			"j1_00_reveil_v2",
			"system",
			"J1 V2",
			"Réveil — cinq messages",
			"res://data/j1_00_reveil_messages_v2_experimental.json",
			1,
			true,
			true,
			true,
			"j1_00_sys_001"
		),
		"sarah_j1_v2": _new_conversation_state(
			"sarah_j1_v2",
			"sarah",
			"Sarah",
			"J1 V2 — Où tu étais ?",
			"res://data/sarah_j1_v2_experimental.json",
			1,
			true,
			false,
			true,
			"j1_01_sarah_001"
		),
		"camille_j1_v2": _new_conversation_state(
			"camille_j1_v2",
			"camille",
			"Camille",
			"J1 V2 — Dehors",
			"res://data/camille_j1_v2_experimental.json",
			1,
			true,
			false,
			true,
			"j1_02_camille_001"
		),
		"camille_j2": _new_conversation_state(
			"camille_j2",
			"camille",
			"Camille",
			"Jour 2 — conversation complète MVP",
			"res://data/camille_j2_complete.json",
			2,
			true,
			false
		),
		"sarah_j2": _new_conversation_state(
			"sarah_j2",
			"sarah",
			"Sarah",
			"Jour 2 — conversation complète MVP",
			"res://data/sarah_j2_complete.json",
			2,
			true,
			false
		),
		"camille_j3": _new_conversation_state(
			"camille_j3",
			"camille",
			"Camille",
			"Jour 3 — conversation complète MVP",
			"res://data/camille_j3_complete.json",
			3,
			true,
			false
		),
		"sarah_j3": _new_conversation_state(
			"sarah_j3",
			"sarah",
			"Sarah",
			"Jour 3 — conversation complète MVP",
			"res://data/sarah_j3_complete.json",
			3,
			true,
			false
		),
		"camille_j4": _new_conversation_state(
			"camille_j4",
			"camille",
			"Camille",
			"Jour 4 — conversation complète MVP",
			"res://data/camille_j4_complete.json",
			4,
			true,
			false
		),
		"maya_j4": _new_conversation_state(
			"maya_j4",
			"maya",
			"Maya",
			"Jour 4 — conversation complète MVP",
			"res://data/maya_j4_complete.json",
			4,
			true,
			false
		),
		"ines_j4": _new_conversation_state(
			"ines_j4",
			"ines",
			"Inès",
			"Jour 4 — conversation complète MVP",
			"res://data/ines_j4_complete.json",
			4,
			true,
			false
		),
		"nico_j4": _new_conversation_state(
			"nico_j4",
			"nico",
			"Nico",
			"Jour 4 — conversation complète MVP",
			"res://data/nico_j4_complete.json",
			4,
			true,
			false
		),
		"sarah_j5": _new_conversation_state(
			"sarah_j5",
			"sarah",
			"Sarah",
			"Jour 5 — conversation complète MVP",
			"res://data/sarah_j5_complete.json",
			5,
			true,
			false
		),
		"camille_j5": _new_conversation_state(
			"camille_j5",
			"camille",
			"Camille",
			"Jour 5 — conversation complète MVP",
			"res://data/camille_j5_complete.json",
			5,
			true,
			false
		),
		"nico_j5": _new_conversation_state(
			"nico_j5",
			"nico",
			"Nico",
			"Jour 5 — conversation complète MVP",
			"res://data/nico_j5_complete.json",
			5,
			true,
			false
		),
		"maya_j5": _new_conversation_state(
			"maya_j5",
			"maya",
			"Maya",
			"Jour 5 — conversation complète MVP",
			"res://data/maya_j5_complete.json",
			5,
			true,
			false
		),
		"sarah_j6": _new_conversation_state(
			"sarah_j6",
			"sarah",
			"Sarah",
			"Jour 6 — conversation complète MVP",
			"res://data/sarah_j6_complete.json",
			6,
			true,
			false
		),
		"camille_j6": _new_conversation_state(
			"camille_j6",
			"camille",
			"Camille",
			"Jour 6 — conversation complète MVP",
			"res://data/camille_j6_complete.json",
			6,
			true,
			false
		),
		"nico_j6": _new_conversation_state(
			"nico_j6",
			"nico",
			"Nico",
			"Jour 6 — conversation complète MVP",
			"res://data/nico_j6_complete.json",
			6,
			true,
			false
		),
		"maya_j6": _new_conversation_state(
			"maya_j6",
			"maya",
			"Maya",
			"Jour 6 — conversation complète MVP",
			"res://data/maya_j6_complete.json",
			6,
			true,
			false
		),
		"ines_j6": _new_conversation_state(
			"ines_j6",
			"ines",
			"Inès",
			"Jour 6 — conversation complète MVP",
			"res://data/ines_j6_complete.json",
			6,
			true,
			false
		),
		"finales_mvp": _new_conversation_state(
			"finales_mvp",
			"system",
			"Finale",
			"Jour 6 — fins MVP",
			"res://data/finales_mvp_complete.json",
			6,
			true,
			false
		)
	}

func _new_conversation_state(id: String, contact_id: String, display_name: String, title: String, json_path: String, day: int, available: bool, initial_has_new: bool = false, experimental: bool = false, start_node: String = "") -> Dictionary:
	return {
		"id": id,
		"contact_id": contact_id,
		"display_name": display_name,
		"title": title,
		"json_path": json_path,
		"day": day,
		"available": available,
		"experimental": experimental,
		"start_node": start_node,
		"started": false,
		"messages": [],
		"game_state": {},
		"active_choice_node": "",
		"next_node": "",
		"done": false,
		"choices": [],
		"last_preview": "Nouveau message" if initial_has_new else display_name + " — " + title,
		"has_new": initial_has_new
	}

func _load_conversation_block_defs() -> void:
	conversation_block_defs = {}
	conversation_block_order = []
	var file: FileAccess = FileAccess.open(BLOCKS_CONFIG_PATH, FileAccess.READ)
	if file == null:
		push_warning("Config blocs introuvable: " + BLOCKS_CONFIG_PATH)
		return
	var parsed = JSON.parse_string(file.get_as_text())
	if typeof(parsed) != TYPE_DICTIONARY:
		push_warning("Config blocs invalide: " + BLOCKS_CONFIG_PATH)
		return
	var data: Dictionary = parsed
	var parsed_blocks = data.get("blocks", {})
	if typeof(parsed_blocks) == TYPE_DICTIONARY:
		conversation_block_defs = parsed_blocks
	var parsed_order = data.get("block_order", [])
	if typeof(parsed_order) == TYPE_ARRAY:
		conversation_block_order = parsed_order.duplicate(true)

func _default_conversation_blocks() -> Dictionary:
	var blocks: Dictionary = {}
	for block_id in conversation_block_order:
		blocks[block_id] = {
			"status": BLOCK_STATUS_AVAILABLE if block_id == "camille_c1a" or block_id == "camille_c2a" or block_id == "camille_c3a" or block_id == "camille_c4a" or block_id == "sarah_s5a" or block_id == "sarah_s6a" else BLOCK_STATUS_LOCKED
		}
	return blocks

func conversation_ids() -> Array:
	return ["camille", "sarah", "j1_00_reveil_v2", "sarah_j1_v2", "camille_j1_v2", "camille_j2", "sarah_j2", "camille_j3", "sarah_j3", "camille_j4", "maya_j4", "ines_j4", "nico_j4", "sarah_j5", "camille_j5", "nico_j5", "maya_j5", "sarah_j6", "camille_j6", "nico_j6", "maya_j6", "ines_j6", "finales_mvp"]

func active_conversation_ids() -> Array:
	var ids: Array = []
	for id in conversation_ids():
		var state: Dictionary = conversations[id]
		if experimental_j1_v2_enabled and current_day == 1 and not bool(state.get("experimental", false)):
			continue
		if bool(state.get("experimental", false)) and not experimental_j1_v2_enabled:
			continue
		var day: int = int(state.get("day", 1))
		if day == current_day and bool(state.get("available", false)):
			ids.append(id)
	return ids

func archived_conversation_ids() -> Array:
	var ids: Array = []
	for id in conversation_ids():
		var state: Dictionary = conversations[id]
		if experimental_j1_v2_enabled and current_day == 1 and not bool(state.get("experimental", false)):
			continue
		if bool(state.get("experimental", false)) and not experimental_j1_v2_enabled:
			continue
		var day: int = int(state.get("day", 1))
		var started: bool = bool(state.get("started", false))
		var done: bool = bool(state.get("done", false))
		if day < current_day and (bool(state.get("available", false)) or started or done):
			ids.append(id)
	return ids

func visible_conversation_ids() -> Array:
	# Compatibilité interne : l'écran Messages actif ne doit plus exposer les jours passés.
	return active_conversation_ids()

func quick_switch_new_conversation_id() -> String:
	# T102 MVP: proposer une seule conversation active du jour courant, jamais une archive.
	for id in active_conversation_ids():
		if id == current_conversation_id:
			continue
		if not has_new(id):
			continue
		var state: Dictionary = conversations[id]
		if bool(state.get("done", false)):
			continue
		return id
	return ""

func set_current_conversation(id: String) -> void:
	if conversations.has(id):
		current_conversation_id = id
		save_progression()

func current() -> Dictionary:
	return conversations[current_conversation_id]

func conversation(id: String) -> Dictionary:
	return conversations[id]

func current_display_name() -> String:
	return str(current().get("display_name", "Conversation"))

func current_json_path() -> String:
	return str(current().get("json_path", ""))

func current_contact_id() -> String:
	return str(current().get("contact_id", current().get("id", current_conversation_id)))

func day_label() -> String:
	return "Jour " + str(current_day)

func has_current_state() -> bool:
	return bool(current().get("started", false)) and current()["messages"].size() > 0

func mark_current_opened() -> void:
	mark_conversation_read(current_conversation_id)

func mark_conversation_read(id: String) -> void:
	if conversations.has(id):
		conversations[id]["has_new"] = false
		save_progression()

func mark_conversation_new(id: String, preview: String = "Nouveau message") -> void:
	if not conversations.has(id):
		return
	var state: Dictionary = conversations[id]
	if not bool(state.get("available", false)):
		return
	state["has_new"] = true
	if preview != "":
		state["last_preview"] = preview
	save_progression()

func record_current_message(sender: String, text: String) -> void:
	var state: Dictionary = current()
	state["started"] = true
	state["messages"].append({"sender": sender, "text": text})
	var preview: String = _preview_for_message(sender, text)
	if preview != "":
		state["last_preview"] = preview
	# Le message affiché dans la conversation ouverte est déjà lu.
	# Les badges "nouveau" sont posés uniquement par mark_conversation_new().
	save_progression()

func _preview_for_message(sender: String, text: String) -> String:
	var clean_text: String = text.strip_edges()
	if clean_text == "":
		return ""
	if sender == "system":
		return ""
	if sender == "player":
		return "Vous : " + clean_text
	return clean_text

func set_current_next_node(node_id: String) -> void:
	var state: Dictionary = current()
	state["started"] = true
	state["next_node"] = node_id
	state["active_choice_node"] = ""
	save_progression()

func set_current_active_choice(node_id: String) -> void:
	var state: Dictionary = current()
	state["started"] = true
	state["active_choice_node"] = node_id
	state["next_node"] = ""
	save_progression()

func record_current_choice(choice_id: String) -> void:
	var state: Dictionary = current()
	state["started"] = true
	state["choices"].append(choice_id)
	save_progression()

func set_current_game_state(game_state: Dictionary) -> void:
	current()["game_state"] = game_state.duplicate(true)
	save_progression()

func current_game_state() -> Dictionary:
	return current()["game_state"].duplicate(true)

func current_messages() -> Array:
	return current()["messages"]

func current_active_choice_node() -> String:
	return str(current().get("active_choice_node", ""))

func current_next_node() -> String:
	return str(current().get("next_node", ""))

func active_block_for_conversation(conversation_id: String) -> String:
	for block_id in conversation_block_order:
		var block_def: Dictionary = conversation_block_defs[block_id]
		if str(block_def.get("conversation_id", "")) != conversation_id:
			continue
		var block_state: Dictionary = conversation_blocks.get(block_id, {})
		var status: String = str(block_state.get("status", BLOCK_STATUS_LOCKED))
		if status == BLOCK_STATUS_AVAILABLE or status == BLOCK_STATUS_ACTIVE:
			return block_id
	return ""

func current_block_id() -> String:
	return active_block_for_conversation(current_conversation_id)

func current_block_start_node() -> String:
	var state: Dictionary = current()
	if bool(state.get("experimental", false)):
		return str(state.get("start_node", ""))
	var block_id: String = current_block_id()
	if block_id == "":
		return ""
	var block_def: Dictionary = conversation_block_defs[block_id]
	return str(block_def.get("start_node", ""))

func can_current_block_play() -> bool:
	var state: Dictionary = current()
	if current_day < int(state.get("day", 1)):
		return false
	if not bool(state.get("available", false)):
		return false
	if bool(state.get("experimental", false)):
		return current_block_id() != "" or str(state.get("start_node", "")) != ""
	return current_block_id() != ""

func current_waiting_text() -> String:
	var block_id: String = current_block_id()
	if block_id != "":
		var block_def: Dictionary = conversation_block_defs[block_id]
		return str(block_def.get("waiting_text", "Plus rien pour le moment"))
	var display_name: String = current_display_name()
	if current_conversation_id == "camille":
		return "Camille ne répond plus pour l’instant."
	if current_conversation_id == "sarah":
		return "Sarah ne répond plus pour l’instant."
	return display_name + " — Plus rien pour le moment."

func mark_current_block_active() -> void:
	var block_id: String = current_block_id()
	if block_id == "":
		return
	var block_state: Dictionary = conversation_blocks[block_id]
	if str(block_state.get("status", BLOCK_STATUS_LOCKED)) == BLOCK_STATUS_AVAILABLE:
		block_state["status"] = BLOCK_STATUS_ACTIVE
		save_progression()

func is_current_block_end_node(node_id: String) -> bool:
	var block_id: String = current_block_id()
	if block_id == "":
		return false
	var block_def: Dictionary = conversation_block_defs[block_id]
	var end_nodes: Array = block_def.get("end_nodes", [])
	return end_nodes.has(node_id)

func complete_current_block(next_node_after_block: String = "") -> void:
	var block_id: String = current_block_id()
	if block_id == "":
		return
	var block_state: Dictionary = conversation_blocks[block_id]
	block_state["status"] = BLOCK_STATUS_DONE
	var block_def: Dictionary = conversation_block_defs[block_id]
	var unlock_id: String = str(block_def.get("unlock_on_done", ""))
	if unlock_id != "":
		_unlock_block(unlock_id)
	if next_node_after_block != "":
		current()["next_node"] = next_node_after_block
		current()["active_choice_node"] = ""
	save_progression()

func _unlock_block(block_id: String) -> void:
	if not conversation_blocks.has(block_id):
		return
	var block_state: Dictionary = conversation_blocks[block_id]
	if str(block_state.get("status", BLOCK_STATUS_LOCKED)) != BLOCK_STATUS_LOCKED:
		return
	block_state["status"] = BLOCK_STATUS_AVAILABLE
	var block_def: Dictionary = conversation_block_defs[block_id]
	var target_id: String = str(block_def.get("notification_target", block_def.get("conversation_id", "")))
	if _can_emit_block_unlock_notification(target_id, block_id):
		mark_conversation_new(target_id, _notification_preview_for_target(target_id))
	else:
		save_progression()

func _notification_preview_for_target(target_id: String) -> String:
	if not conversations.has(target_id):
		return "Nouveau message"
	return "Nouveau message de " + str(conversations[target_id].get("display_name", target_id))

func _can_emit_block_unlock_notification(target_id: String, unlocked_block_id: String) -> bool:
	if target_id == "" or target_id == current_conversation_id:
		return false
	if not conversations.has(target_id):
		return false
	if not conversation_block_defs.has(unlocked_block_id):
		return false
	var unlocked_block_def: Dictionary = conversation_block_defs[unlocked_block_id]
	if str(unlocked_block_def.get("conversation_id", "")) != target_id:
		return false
	var target_state: Dictionary = conversations[target_id]
	if not bool(target_state.get("available", false)):
		return false
	if bool(target_state.get("done", false)):
		return false
	return true

func has_available_block_for_conversation(conversation_id: String) -> bool:
	return active_block_for_conversation(conversation_id) != ""

func repair_available_block_notifications() -> void:
	var changed: bool = false
	for block_id in conversation_block_order:
		if not conversation_blocks.has(block_id) or not conversation_block_defs.has(block_id):
			continue
		var block_state: Dictionary = conversation_blocks[block_id]
		var status: String = str(block_state.get("status", BLOCK_STATUS_LOCKED))
		if status != BLOCK_STATUS_AVAILABLE:
			continue
		var block_def: Dictionary = conversation_block_defs[block_id]
		var conversation_id: String = str(block_def.get("conversation_id", ""))
		if conversation_id == "" or conversation_id == current_conversation_id:
			continue
		if not conversations.has(conversation_id):
			continue
		var state: Dictionary = conversations[conversation_id]
		if int(state.get("day", 1)) != current_day:
			continue
		if not bool(state.get("available", false)):
			continue
		if bool(state.get("done", false)):
			continue
		if bool(state.get("has_new", false)):
			continue
		if _has_started_available_block(conversation_id, block_def):
			continue
		state["has_new"] = true
		state["last_preview"] = _notification_preview_for_target(conversation_id)
		changed = true
	if changed:
		save_progression()

func _has_started_available_block(conversation_id: String, block_def: Dictionary) -> bool:
	var state: Dictionary = conversations[conversation_id]
	var start_node: String = str(block_def.get("start_node", ""))
	var next_node: String = str(state.get("next_node", ""))
	var active_choice_node: String = str(state.get("active_choice_node", ""))
	if active_choice_node != "":
		return true
	var pre_start_nodes: Array = block_def.get("pre_start_nodes", [])
	if pre_start_nodes.has(next_node):
		return false
	if next_node != "" and next_node != start_node:
		return true
	if next_node == start_node:
		return false
	return false

func current_done() -> bool:
	return bool(current().get("done", false))

func mark_current_done() -> void:
	current()["done"] = true
	current()["next_node"] = ""
	current()["active_choice_node"] = ""
	refresh_day_progression()
	save_progression()

func has_new(id: String) -> bool:
	if not conversations.has(id):
		return false
	return bool(conversations[id].get("has_new", false))

func preview_text(id: String) -> String:
	var state: Dictionary = conversation(id)
	if not bool(state.get("available", false)):
		return "À venir — " + day_label_for_conversation(id)
	if bool(state.get("has_new", false)):
		return str(state.get("last_preview", "Nouveau message"))
	if not has_available_block_for_conversation(id) and not bool(state.get("done", false)):
		return "Plus rien pour le moment"
	if state["messages"].is_empty():
		return "Démarrer " + str(state.get("display_name", id))
	return str(state.get("last_preview", ""))

func archived_preview_text(id: String) -> String:
	if not conversations.has(id):
		return "Archivé"
	var state: Dictionary = conversation(id)
	if bool(state.get("done", false)):
		return "Archivé — terminé"
	if state["messages"].is_empty():
		return "Archivé — non lu"
	return "Archivé — relire"

func day_label_for_conversation(id: String) -> String:
	if not conversations.has(id):
		return "Jour ?"
	var state: Dictionary = conversations[id]
	return "Jour " + str(int(state.get("day", 1)))

func is_day_transition_available() -> bool:
	return day_transition_available

func refresh_day_progression() -> void:
	# MVP actuel : transitions explicites J1 → J2 → J3 → J4 → J5 → J6, sans calendrier ni scheduler.
	if current_day >= 6:
		day_transition_available = false
		return
	if not REQUIRED_CONVERSATIONS_BY_DAY.has(current_day):
		day_transition_available = false
		return
	if completed_days.has(current_day):
		day_transition_available = false
		return
	day_transition_available = _is_day_complete(current_day)

func _is_day_complete(day: int) -> bool:
	if not REQUIRED_CONVERSATIONS_BY_DAY.has(day):
		return false
	var required_ids: Array = REQUIRED_CONVERSATIONS_BY_DAY[day]
	for id in required_ids:
		if not conversations.has(id):
			return false
		var state: Dictionary = conversations[id]
		if not bool(state.get("done", false)):
			return false
		if str(state.get("active_choice_node", "")) != "":
			return false
	return true

func advance_to_next_day() -> void:
	refresh_day_progression()
	if not day_transition_available:
		return
	if not completed_days.has(current_day):
		completed_days.append(current_day)
	current_day += 1
	day_transition_available = false
	save_progression()

func handle_dynamic_notification(source_conversation_id: String, node_id: String) -> void:
	var event_id: String = source_conversation_id + ":" + node_id
	if dynamic_notifications_fired.has(event_id):
		return

	var target_id: String = ""
	var preview: String = ""
	if source_conversation_id == "camille":
		if node_id == "c1_010":
			target_id = "sarah"
			preview = "Nouveau message de Sarah"
		elif node_id == "c1_020":
			target_id = "sarah"
			preview = "Nouveau message de Sarah"
	elif source_conversation_id == "sarah":
		if node_id == "s1_006":
			target_id = "camille"
			preview = "Nouveau message de Camille"
		elif node_id == "s1_020":
			target_id = "camille"
			preview = "Nouveau message de Camille"

	if target_id == "" or preview == "":
		return
	if not _can_emit_dynamic_notification(target_id):
		return
	dynamic_notifications_fired.append(event_id)
	mark_conversation_new(target_id, preview)

func _can_emit_dynamic_notification(target_id: String) -> bool:
	if current_day > 1:
		return false
	if target_id == current_conversation_id:
		return false
	if not conversations.has(target_id):
		return false
	var target_state: Dictionary = conversations[target_id]
	if not bool(target_state.get("available", false)):
		return false
	if bool(target_state.get("done", false)):
		return false
	if not has_available_block_for_conversation(target_id):
		return false
	return true

func save_progression() -> void:
	var payload: Dictionary = {
		"save_version": SAVE_VERSION,
		"current_conversation_id": current_conversation_id,
		"current_day": current_day,
		"completed_days": completed_days.duplicate(true),
		"day_transition_available": day_transition_available,
		"dynamic_notifications_fired": dynamic_notifications_fired.duplicate(true),
		"global_game_state": global_game_state.duplicate(true),
		"conversation_blocks": conversation_blocks.duplicate(true),
		"conversations": {}
	}
	for id in conversation_ids():
		var state: Dictionary = conversations[id]
		payload["conversations"][id] = {
			"started": bool(state.get("started", false)),
			"messages": state.get("messages", []).duplicate(true),
			"game_state": state.get("game_state", {}).duplicate(true),
			"active_choice_node": str(state.get("active_choice_node", "")),
			"next_node": str(state.get("next_node", "")),
			"done": bool(state.get("done", false)),
			"choices": state.get("choices", []).duplicate(true),
			"last_preview": str(state.get("last_preview", "")),
			"has_new": bool(state.get("has_new", false))
		}

	var file: FileAccess = FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	if file == null:
		push_warning("Sauvegarde impossible: " + SAVE_PATH)
		return
	file.store_string(JSON.stringify(payload))

func load_progression() -> void:
	if not FileAccess.file_exists(SAVE_PATH):
		return
	var file: FileAccess = FileAccess.open(SAVE_PATH, FileAccess.READ)
	if file == null:
		return
	var parsed = JSON.parse_string(file.get_as_text())
	if typeof(parsed) != TYPE_DICTIONARY:
		return
	var payload: Dictionary = parsed
	current_day = int(payload.get("current_day", 1))
	var saved_completed_days = payload.get("completed_days", [])
	if typeof(saved_completed_days) == TYPE_ARRAY:
		completed_days = saved_completed_days.duplicate(true)
	day_transition_available = bool(payload.get("day_transition_available", false))
	var saved_fired = payload.get("dynamic_notifications_fired", [])
	if typeof(saved_fired) == TYPE_ARRAY:
		dynamic_notifications_fired = saved_fired.duplicate(true)
	var saved_global_game_state = payload.get("global_game_state", {})
	_merge_saved_global_game_state(saved_global_game_state)
	var saved_blocks = payload.get("conversation_blocks", {})
	var has_saved_blocks: bool = typeof(saved_blocks) == TYPE_DICTIONARY and not saved_blocks.is_empty()
	if has_saved_blocks:
		for block_id in conversation_block_order:
			if not saved_blocks.has(block_id):
				continue
			var saved_block_value = saved_blocks[block_id]
			if typeof(saved_block_value) != TYPE_DICTIONARY:
				continue
			var saved_block: Dictionary = saved_block_value
			conversation_blocks[block_id]["status"] = str(saved_block.get("status", conversation_blocks[block_id].get("status", BLOCK_STATUS_LOCKED)))
	var saved_conversations = payload.get("conversations", {})
	if typeof(saved_conversations) != TYPE_DICTIONARY:
		return

	for id in conversation_ids():
		if not saved_conversations.has(id):
			continue
		var saved_state_value = saved_conversations[id]
		if typeof(saved_state_value) != TYPE_DICTIONARY:
			continue
		var saved_state: Dictionary = saved_state_value
		var state: Dictionary = conversations[id]
		state["started"] = bool(saved_state.get("started", state.get("started", false)))
		state["messages"] = saved_state.get("messages", state.get("messages", [])).duplicate(true)
		state["game_state"] = saved_state.get("game_state", state.get("game_state", {})).duplicate(true)
		state["active_choice_node"] = str(saved_state.get("active_choice_node", state.get("active_choice_node", "")))
		state["next_node"] = str(saved_state.get("next_node", state.get("next_node", "")))
		state["done"] = bool(saved_state.get("done", state.get("done", false)))
		state["choices"] = saved_state.get("choices", state.get("choices", [])).duplicate(true)
		state["last_preview"] = str(saved_state.get("last_preview", state.get("last_preview", "")))
		state["has_new"] = bool(saved_state.get("has_new", state.get("has_new", false)))

	var saved_current: String = str(payload.get("current_conversation_id", current_conversation_id))
	if conversations.has(saved_current):
		current_conversation_id = saved_current
	if not has_saved_blocks:
		_migrate_blocks_from_existing_save()
	refresh_day_progression()

func _merge_saved_global_game_state(saved_global_game_state) -> void:
	global_game_state = _default_global_game_state()
	if typeof(saved_global_game_state) != TYPE_DICTIONARY:
		return
	var saved_variables = saved_global_game_state.get("variables", {})
	if typeof(saved_variables) == TYPE_DICTIONARY:
		for key in V2_VARIABLE_DEFAULTS.keys():
			if saved_variables.has(key) and (typeof(saved_variables[key]) == TYPE_INT or typeof(saved_variables[key]) == TYPE_FLOAT):
				global_game_state["variables"][key] = int(clamp(int(saved_variables[key]), 0, 100))
	var saved_flags = saved_global_game_state.get("flags", [])
	if typeof(saved_flags) == TYPE_ARRAY:
		for flag in saved_flags:
			if not global_game_state["flags"].has(flag):
				global_game_state["flags"].append(flag)

func _migrate_blocks_from_existing_save() -> void:
	if current_day > 1 or bool(conversations["camille"].get("done", false)):
		conversation_blocks["camille_c1a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c1b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c1c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 1 or bool(conversations["sarah"].get("done", false)):
		conversation_blocks["sarah_s1a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["sarah_s1b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["sarah_s1c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 2 or bool(conversations["camille_j2"].get("done", false)):
		conversation_blocks["camille_c2a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c2b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c2c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 2 or bool(conversations["sarah_j2"].get("done", false)):
		conversation_blocks["sarah_s2a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["sarah_s2b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["sarah_s2c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 3 or bool(conversations["camille_j3"].get("done", false)):
		conversation_blocks["camille_c3a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c3b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c3c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 3 or bool(conversations["sarah_j3"].get("done", false)):
		conversation_blocks["sarah_s3a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["sarah_s3b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["sarah_s3c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 4 or bool(conversations["camille_j4"].get("done", false)):
		conversation_blocks["camille_c4a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c4b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c4c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 4 or bool(conversations["maya_j4"].get("done", false)):
		conversation_blocks["maya_m4a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["maya_m4b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["maya_m4c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 4 or bool(conversations["ines_j4"].get("done", false)):
		conversation_blocks["ines_i4a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["ines_i4b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["ines_i4c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 4 or bool(conversations["nico_j4"].get("done", false)):
		conversation_blocks["nico_n4a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["nico_n4b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["nico_n4c"]["status"] = BLOCK_STATUS_DONE
	if current_day <= 1 and not bool(conversations["camille"].get("done", false)) and not bool(conversations["sarah"].get("done", false)):
		conversation_blocks["camille_c1a"]["status"] = BLOCK_STATUS_AVAILABLE
	if current_day == 2 and not bool(conversations["camille_j2"].get("done", false)) and not bool(conversations["sarah_j2"].get("done", false)):
		conversation_blocks["camille_c2a"]["status"] = BLOCK_STATUS_AVAILABLE
	if current_day == 3 and not bool(conversations["camille_j3"].get("done", false)) and not bool(conversations["sarah_j3"].get("done", false)):
		conversation_blocks["camille_c3a"]["status"] = BLOCK_STATUS_AVAILABLE
	if current_day == 4 and not bool(conversations["camille_j4"].get("done", false)) and not bool(conversations["maya_j4"].get("done", false)) and not bool(conversations["ines_j4"].get("done", false)) and not bool(conversations["nico_j4"].get("done", false)):
		conversation_blocks["camille_c4a"]["status"] = BLOCK_STATUS_AVAILABLE
	if current_day > 5 or bool(conversations["sarah_j5"].get("done", false)):
		conversation_blocks["sarah_s5a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["sarah_s5b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["sarah_s5c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 5 or bool(conversations["camille_j5"].get("done", false)):
		conversation_blocks["camille_c5a"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c5b"]["status"] = BLOCK_STATUS_DONE
		conversation_blocks["camille_c5c"]["status"] = BLOCK_STATUS_DONE
	if current_day > 5 or bool(conversations["nico_j5"].get("done", false)):
		conversation_blocks["nico_n5a"]["status"] = BLOCK_STATUS_DONE
	if current_day > 5 or bool(conversations["maya_j5"].get("done", false)):
		conversation_blocks["maya_m5a"]["status"] = BLOCK_STATUS_DONE
	if current_day == 5 and not bool(conversations["sarah_j5"].get("done", false)) and not bool(conversations["camille_j5"].get("done", false)) and not bool(conversations["nico_j5"].get("done", false)) and not bool(conversations["maya_j5"].get("done", false)):
		conversation_blocks["sarah_s5a"]["status"] = BLOCK_STATUS_AVAILABLE
	if current_day == 6 and not bool(conversations["sarah_j6"].get("done", false)) and not bool(conversations["camille_j6"].get("done", false)) and not bool(conversations["nico_j6"].get("done", false)) and not bool(conversations["maya_j6"].get("done", false)) and not bool(conversations["ines_j6"].get("done", false)) and not bool(conversations["finales_mvp"].get("done", false)):
		conversation_blocks["sarah_s6a"]["status"] = BLOCK_STATUS_AVAILABLE

func reset_progression() -> void:
	current_conversation_id = "camille"
	current_day = 1
	completed_days = []
	day_transition_available = false
	conversation_blocks = _default_conversation_blocks()
	dynamic_notifications_fired = []
	conversations = _default_conversations()
	if FileAccess.file_exists(SAVE_PATH):
		var dir: DirAccess = DirAccess.open("user://")
		if dir != null:
			dir.remove("double_vie_save.json")

# Compatibilité Camille existante si un ancien script l'appelle encore.
func has_camille_state() -> bool:
	return bool(conversations["camille"].get("started", false)) and conversations["camille"]["messages"].size() > 0

func camille_preview_text() -> String:
	return preview_text("camille")
