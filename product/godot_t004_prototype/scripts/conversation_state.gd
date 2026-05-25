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
const J1_V2_CORE_CONVERSATIONS := ["sarah_j1_v2", "camille_j1_v2", "nico_j1_v2", "maya_j1_v2", "ines_j1_v2"]
const J1_V2_FIRST_OPEN_FLAGS := {
	"sarah_j1_v2": "first_reply_sarah",
	"camille_j1_v2": "first_reply_camille",
	"nico_j1_v2": "first_reply_nico",
	"maya_j1_v2": "first_reply_maya",
	"ines_j1_v2": "first_reply_ines"
}
const J1_V2_DELAYED_REPLY_FLAGS := {
	"sarah_j1_v2": "delayed_reply_sarah_j1",
	"camille_j1_v2": "delayed_reply_camille_j1",
	"nico_j1_v2": "delayed_reply_nico_j1",
	"maya_j1_v2": "delayed_reply_maya_j1",
	"ines_j1_v2": "delayed_reply_ines_j1"
}
const J1_V2_LEFT_OPEN_FLAGS := {
	"sarah_j1_v2": "left_sarah_on_read_j1",
	"camille_j1_v2": "left_camille_on_read_j1",
	"nico_respiration_j1_v2": "ignored_nico_respiration_j1",
	"sarah_meal_j1_v2": "late_reply_sarah_meal_j1"
}
const J1_V2_INITIAL_MESSAGES := {
	"sarah_j1_v2": "T’es réveillé ?",
	"camille_j1_v2": "Je crois qu’on a été moins discrets qu’on pensait.",
	"nico_j1_v2": "T’es rentré comment ?",
	"maya_j1_v2": "tu dors encore ?",
	"ines_j1_v2": "Je peux te parler ?"
}
const J1_V2_INITIAL_PREVIEWS := J1_V2_INITIAL_MESSAGES
const J1_V2_INITIAL_PLAYER_REPLIES := {
	"sarah_j1_v2": "Oui. Je viens de voir ton message.",
	"camille_j1_v2": "Tu crois ?",
	"nico_j1_v2": "À pied. Pourquoi ?",
	"maya_j1_v2": "non. pourquoi ?",
	"ines_j1_v2": "Oui, dis-moi."
}
const J1_V2_FIRST_REPLY_CHOICES := {
	"j1_00_reply_sarah_first": "sarah_j1_v2",
	"j1_00_reply_camille_first": "camille_j1_v2",
	"j1_00_reply_nico_first": "nico_j1_v2",
	"j1_00_reply_maya_first": "maya_j1_v2",
	"j1_00_reply_ines_first": "ines_j1_v2"
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
	if experimental_j1_v2_enabled and current_day == 1:
		_unlock_j1_v2_core_from_messages()
	save_progression()

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

func has_global_flag(flag: String) -> bool:
	return global_game_state.get("flags", []).has(flag)

func global_variable_value(key: String) -> int:
	return int(global_game_state.get("variables", {}).get(key, 0))

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
			false,
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
			false,
			false,
			true,
			"j1_02_camille_001"
		),
		"nico_j1_v2": _new_conversation_state(
			"nico_j1_v2",
			"nico",
			"Nico",
			"J1 V2 — Couverture",
			"res://data/nico_j1_v2_experimental.json",
			1,
			false,
			false,
			true,
			"j1_03_nico_001"
		),
		"maya_j1_v2": _new_conversation_state(
			"maya_j1_v2",
			"maya",
			"Maya",
			"J1 V2 — Timing",
			"res://data/maya_j1_v2_experimental.json",
			1,
			false,
			false,
			true,
			"j1_04_maya_001"
		),
		"ines_j1_v2": _new_conversation_state(
			"ines_j1_v2",
			"ines",
			"Inès",
			"J1 V2 — Faille",
			"res://data/ines_j1_v2_experimental.json",
			1,
			false,
			false,
			true,
			"j1_05_ines_001"
		),
		"sarah_j2_v2": _new_conversation_state(
			"sarah_j2_v2",
			"sarah",
			"Sarah",
			"J2 V2 — Matin",
			"res://data/sarah_j2_v2_experimental.json",
			2,
			false,
			false,
			true,
			"j2_01_sarah_001"
		),
		"nico_j2_v2": _new_conversation_state(
			"nico_j2_v2",
			"nico",
			"Nico",
			"J2 V2 — Alibi",
			"res://data/nico_j2_v2_experimental.json",
			2,
			false,
			false,
			true,
			"j2_02_nico_001"
		),
		"camille_j2_v2": _new_conversation_state(
			"camille_j2_v2",
			"camille",
			"Camille",
			"J2 V2 — Tension",
			"res://data/camille_j2_v2_experimental.json",
			2,
			false,
			false,
			true,
			"j2_03_camille_001"
		),
		"maya_j2_v2": _new_conversation_state(
			"maya_j2_v2",
			"maya",
			"Maya",
			"J2 V2 — Groupe",
			"res://data/maya_j2_v2_experimental.json",
			2,
			false,
			false,
			true,
			"j2_04_maya_001"
		),
		"ines_j2_v2": _new_conversation_state(
			"ines_j2_v2",
			"ines",
			"Inès",
			"J2 V2 — Calme",
			"res://data/ines_j2_v2_experimental.json",
			2,
			false,
			false,
			true,
			"j2_05_ines_001"
		),
		"sarah_j3_v2": _new_conversation_state(
			"sarah_j3_v2",
			"sarah",
			"Sarah",
			"J3 V2 — Matin",
			"res://data/sarah_j3_v2_experimental.json",
			3,
			false,
			false,
			true,
			"j3_01_sarah_001"
		),
		"nico_j3_v2": _new_conversation_state(
			"nico_j3_v2",
			"nico",
			"Nico",
			"J3 V2 — Disponibilité",
			"res://data/nico_j3_v2_experimental.json",
			3,
			false,
			false,
			true,
			"j3_02_nico_001"
		),
		"camille_j3_v2": _new_conversation_state(
			"camille_j3_v2",
			"camille",
			"Camille",
			"J3 V2 — Tension",
			"res://data/camille_j3_v2_experimental.json",
			3,
			false,
			false,
			true,
			"j3_03_camille_001"
		),
		"maya_j3_v2": _new_conversation_state(
			"maya_j3_v2",
			"maya",
			"Maya",
			"J3 V2 — Signaux",
			"res://data/maya_j3_v2_experimental.json",
			3,
			false,
			false,
			true,
			"j3_04_maya_001"
		),
		"ines_j3_v2": _new_conversation_state(
			"ines_j3_v2",
			"ines",
			"Inès",
			"J3 V2 — Calme",
			"res://data/ines_j3_v2_experimental.json",
			3,
			false,
			false,
			true,
			"j3_05_ines_001"
		),
		"sarah_j4_v2": _new_conversation_state(
			"sarah_j4_v2",
			"sarah",
			"Sarah",
			"J4 V2 — Matin",
			"res://data/sarah_j4_v2_experimental.json",
			4,
			false,
			false,
			true,
			"j4_01_sarah_001"
		),
		"nico_j4_v2": _new_conversation_state(
			"nico_j4_v2",
			"nico",
			"Nico",
			"J4 V2 — Consultation",
			"res://data/nico_j4_v2_experimental.json",
			4,
			false,
			false,
			true,
			"j4_02_nico_001"
		),
		"sarah_j4_followup_v2": _new_conversation_state(
			"sarah_j4_followup_v2",
			"sarah",
			"Sarah",
			"J4 V2 — Retour",
			"res://data/sarah_j4_followup_v2_experimental.json",
			4,
			false,
			false,
			true,
			"j4_03_sarah_followup_001"
		),
		"camille_j4_v2": _new_conversation_state(
			"camille_j4_v2",
			"camille",
			"Camille",
			"J4 V2 — Pause",
			"res://data/camille_j4_v2_experimental.json",
			4,
			false,
			false,
			true,
			"j4_04_camille_001"
		),
		"maya_j4_v2": _new_conversation_state(
			"maya_j4_v2",
			"maya",
			"Maya",
			"J4 V2 — Ambiance",
			"res://data/maya_j4_v2_experimental.json",
			4,
			false,
			false,
			true,
			"j4_05_maya_001"
		),
		"ines_j4_v2": _new_conversation_state(
			"ines_j4_v2",
			"ines",
			"Inès",
			"J4 V2 — Soir",
			"res://data/ines_j4_v2_experimental.json",
			4,
			false,
			false,
			true,
			"j4_06_ines_001"
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
		"pending_choice_option_count": 0,
		"next_node": "",
		"done": false,
		"choices": [],
		"left_open": false,
		"left_open_choice_node": "",
		"left_open_count": 0,
		"left_open_flag": "",
		"late_reply_prepared": false,
		"late_reopen_consumed": false,
		"late_reopen_consumed_flag": "",
		"late_reopen_consumed_choice_node": "",
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
	return ["camille", "sarah", "j1_00_reveil_v2", "sarah_j1_v2", "camille_j1_v2", "nico_j1_v2", "maya_j1_v2", "ines_j1_v2", "sarah_j2_v2", "nico_j2_v2", "camille_j2_v2", "maya_j2_v2", "ines_j2_v2", "sarah_j3_v2", "nico_j3_v2", "camille_j3_v2", "maya_j3_v2", "ines_j3_v2", "sarah_j4_v2", "nico_j4_v2", "sarah_j4_followup_v2", "camille_j4_v2", "maya_j4_v2", "ines_j4_v2", "camille_j2", "sarah_j2", "camille_j3", "sarah_j3", "camille_j4", "maya_j4", "ines_j4", "nico_j4", "sarah_j5", "camille_j5", "nico_j5", "maya_j5", "sarah_j6", "camille_j6", "nico_j6", "maya_j6", "ines_j6", "finales_mvp"]

func _conversation_allowed_in_current_mode(id: String, state: Dictionary) -> bool:
	if bool(state.get("experimental", false)) and not experimental_j1_v2_enabled:
		return false
	if experimental_j1_v2_enabled:
		var day: int = int(state.get("day", 1))
		if day == 1:
			return bool(state.get("experimental", false))
		if day == 2:
			return bool(state.get("experimental", false))
		if day == 3:
			return bool(state.get("experimental", false))
		if day == 4:
			return bool(state.get("experimental", false))
	return true

func active_conversation_ids() -> Array:
	var ids: Array = []
	if experimental_j1_v2_enabled and current_day == 1:
		_unlock_j1_v2_core_from_messages()
	var source_ids: Array = _j1_v2_message_list_core_ids() if experimental_j1_v2_enabled and current_day == 1 else conversation_ids()
	for id in source_ids:
		if experimental_j1_v2_enabled and current_day == 1 and id == "j1_00_reveil_v2":
			continue
		var state: Dictionary = conversations[id]
		if not _conversation_allowed_in_current_mode(id, state):
			continue
		var day: int = int(state.get("day", 1))
		if day == current_day and bool(state.get("available", false)):
			ids.append(id)
	return ids

func archived_conversation_ids() -> Array:
	var ids: Array = []
	for id in conversation_ids():
		var state: Dictionary = conversations[id]
		if not _conversation_allowed_in_current_mode(id, state):
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
	# T143: si plusieurs fils non lus existent, revenir à Messages plutôt que choisir à la place du joueur.
	var unread_ids: Array = unread_conversation_ids_except_current()
	if unread_ids.size() == 1:
		return str(unread_ids[0])
	if unread_ids.size() > 1:
		return "__unread_messages__"
	return ""

func unread_conversation_ids_except_current() -> Array:
	var ids: Array = []
	for id in active_conversation_ids():
		if id == current_conversation_id:
			continue
		if not has_new(id):
			continue
		var state: Dictionary = conversations[id]
		if bool(state.get("done", false)):
			continue
		ids.append(id)
	return ids

func set_current_conversation(id: String) -> void:
	if conversations.has(id):
		handle_j1_v2_first_open_from_messages(id)
		current_conversation_id = id
		save_progression()

func handle_j1_v2_first_open_from_messages(conversation_id: String) -> void:
	if not experimental_j1_v2_enabled or current_day != 1:
		return
	if not J1_V2_FIRST_OPEN_FLAGS.has(conversation_id):
		return
	if _j1_v2_first_open_already_chosen():
		return
	var flags: Array = [J1_V2_FIRST_OPEN_FLAGS[conversation_id]]
	for other_id in J1_V2_CORE_CONVERSATIONS:
		if other_id == conversation_id:
			continue
		flags.append(J1_V2_DELAYED_REPLY_FLAGS[other_id])
	apply_global_effects({"flags": flags})

func _j1_v2_first_open_already_chosen() -> bool:
	for flag in J1_V2_FIRST_OPEN_FLAGS.values():
		if has_global_flag(str(flag)):
			return true
	return false

func _unlock_j1_v2_core_from_messages() -> void:
	if conversations.has("sarah_j1_v2"):
		conversations["sarah_j1_v2"]["available"] = true
		if not bool(conversations["sarah_j1_v2"].get("started", false)) and not bool(conversations["sarah_j1_v2"].get("has_new", false)):
			mark_conversation_new("sarah_j1_v2", str(J1_V2_INITIAL_PREVIEWS["sarah_j1_v2"]))
	if conversations.has("camille_j1_v2"):
		conversations["camille_j1_v2"]["available"] = true
		if not bool(conversations["camille_j1_v2"].get("started", false)) and not bool(conversations["camille_j1_v2"].get("has_new", false)):
			mark_conversation_new("camille_j1_v2", str(J1_V2_INITIAL_PREVIEWS["camille_j1_v2"]))
	if conversations.has("nico_j1_v2"):
		conversations["nico_j1_v2"]["available"] = true
		if not bool(conversations["nico_j1_v2"].get("started", false)) and not bool(conversations["nico_j1_v2"].get("has_new", false)):
			mark_conversation_new("nico_j1_v2", str(J1_V2_INITIAL_PREVIEWS["nico_j1_v2"]))
	if conversations.has("maya_j1_v2"):
		conversations["maya_j1_v2"]["available"] = true
		if not bool(conversations["maya_j1_v2"].get("started", false)) and not bool(conversations["maya_j1_v2"].get("has_new", false)):
			mark_conversation_new("maya_j1_v2", str(J1_V2_INITIAL_PREVIEWS["maya_j1_v2"]))
	if conversations.has("ines_j1_v2"):
		conversations["ines_j1_v2"]["available"] = true
		if not bool(conversations["ines_j1_v2"].get("started", false)) and not bool(conversations["ines_j1_v2"].get("has_new", false)):
			mark_conversation_new("ines_j1_v2", str(J1_V2_INITIAL_PREVIEWS["ines_j1_v2"]))

func _j1_v2_message_list_core_ids() -> Array:
	return J1_V2_CORE_CONVERSATIONS.duplicate()

func _j1_v2_forced_first_reply_conversation_id() -> String:
	if not experimental_j1_v2_enabled or current_day != 1:
		return ""
	if not conversations.has("j1_00_reveil_v2"):
		return ""
	var reveil_choices: Array = conversations["j1_00_reveil_v2"].get("choices", [])
	for index in range(reveil_choices.size() - 1, -1, -1):
		var choice_id: String = str(reveil_choices[index])
		if not J1_V2_FIRST_REPLY_CHOICES.has(choice_id):
			continue
		var target_id: String = str(J1_V2_FIRST_REPLY_CHOICES[choice_id])
		if not conversations.has(target_id):
			return ""
		var target_state: Dictionary = conversations[target_id]
		if not bool(target_state.get("available", false)):
			return ""
		if bool(target_state.get("done", false)):
			return ""
		if not bool(target_state.get("started", false)):
			return target_id
	return ""

func j1_v2_initial_message_for(conversation_id: String) -> String:
	if not J1_V2_INITIAL_MESSAGES.has(conversation_id):
		return ""
	return str(J1_V2_INITIAL_MESSAGES[conversation_id])

func j1_v2_initial_player_reply_for(conversation_id: String) -> String:
	if not J1_V2_INITIAL_PLAYER_REPLIES.has(conversation_id):
		return ""
	return str(J1_V2_INITIAL_PLAYER_REPLIES[conversation_id])

func current_has_message_text(text: String) -> bool:
	var clean_text := text.strip_edges()
	for entry in current_messages():
		if str(entry.get("text", "")).strip_edges() == clean_text:
			return true
	return false

func j1_v2_should_show_first_open_note() -> bool:
	return experimental_j1_v2_enabled and current_day == 1 and not _j1_v2_first_open_already_chosen()

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
	record_current_event({"kind": "message", "sender": sender, "text": text})

func record_current_event(event: Dictionary) -> void:
	var state: Dictionary = current()
	state["started"] = true
	var entry: Dictionary = event.duplicate(true)
	if not entry.has("kind"):
		entry["kind"] = "message"
	state["messages"].append(entry)
	var preview: String = _preview_for_event(entry)
	if preview != "":
		state["last_preview"] = preview
	# Le message affiché dans la conversation ouverte est déjà lu.
	# Les badges "nouveau" sont posés uniquement par mark_conversation_new().
	save_progression()

func _preview_for_event(entry: Dictionary) -> String:
	if str(entry.get("kind", "message")) == "media":
		var caption: String = str(entry.get("caption", "")).strip_edges()
		if caption == "":
			caption = "[image envoyée]"
		return _preview_for_message(str(entry.get("sender", "system")), caption)
	return _preview_for_message(str(entry.get("sender", "system")), str(entry.get("text", "")))

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
	state["pending_choice_option_count"] = 0
	save_progression()

func set_current_active_choice(node_id: String, option_count: int = 0) -> void:
	var state: Dictionary = current()
	state["started"] = true
	state["active_choice_node"] = node_id
	state["pending_choice_option_count"] = option_count
	state["next_node"] = ""
	save_progression()

func is_single_reply_choice_node(node_id: String) -> bool:
	return node_id.contains("_single_reply_")

func is_narrative_multiple_choice_pending(conversation_id: String = "") -> bool:
	var id: String = current_conversation_id if conversation_id == "" else conversation_id
	if not conversations.has(id):
		return false
	var state: Dictionary = conversations[id]
	if bool(state.get("done", false)):
		return false
	var active_choice_node: String = str(state.get("active_choice_node", ""))
	if active_choice_node == "":
		return false
	if is_single_reply_choice_node(active_choice_node):
		return false
	return int(state.get("pending_choice_option_count", 0)) > 1

func mark_current_left_open_if_pending_choice() -> bool:
	var state: Dictionary = current()
	if bool(state.get("done", false)):
		return false
	var active_choice_node: String = str(state.get("active_choice_node", ""))
	if active_choice_node == "":
		return false
	if is_single_reply_choice_node(active_choice_node):
		return false
	if int(state.get("pending_choice_option_count", 0)) <= 1:
		return false
	if bool(state.get("left_open", false)):
		return false
	var silence_flag: String = _left_open_flag_for_current_context(active_choice_node)
	var same_late_reopen_already_consumed: bool = (
		bool(state.get("late_reopen_consumed", false))
		and str(state.get("late_reopen_consumed_flag", "")) == silence_flag
		and str(state.get("late_reopen_consumed_choice_node", "")) == active_choice_node
	)
	state["left_open"] = true
	state["left_open_choice_node"] = active_choice_node
	state["left_open_count"] = int(state.get("left_open_count", 0)) + 1
	state["left_open_flag"] = silence_flag
	if same_late_reopen_already_consumed:
		state["late_reply_prepared"] = false
	else:
		state["late_reply_prepared"] = true
		state["late_reopen_consumed"] = false
		state["late_reopen_consumed_flag"] = ""
		state["late_reopen_consumed_choice_node"] = ""
	if silence_flag != "" and not global_game_state["flags"].has(silence_flag):
		global_game_state["flags"].append(silence_flag)
	save_progression()
	return true

func _left_open_flag_for_current_context(active_choice_node: String) -> String:
	var state: Dictionary = current()
	var json_path: String = str(state.get("json_path", ""))
	if json_path.contains("nico_respiration_j1_v2"):
		return str(J1_V2_LEFT_OPEN_FLAGS.get("nico_respiration_j1_v2", ""))
	if json_path.contains("sarah_meal_j1_v2"):
		return str(J1_V2_LEFT_OPEN_FLAGS.get("sarah_meal_j1_v2", ""))
	return str(J1_V2_LEFT_OPEN_FLAGS.get(current_conversation_id, ""))

func current_late_reopen_start_node() -> String:
	var state: Dictionary = current()
	if bool(state.get("done", false)):
		return ""
	if bool(state.get("late_reopen_consumed", false)):
		return ""
	if not bool(state.get("left_open", false)) or not bool(state.get("late_reply_prepared", false)):
		return ""
	var active_choice_node: String = str(state.get("left_open_choice_node", ""))
	var silence_flag: String = str(state.get("left_open_flag", ""))
	var json_path: String = str(state.get("json_path", ""))
	return _late_reopen_start_for_context(silence_flag, active_choice_node, json_path)

func _late_reopen_start_for_context(silence_flag: String, choice_node: String, json_path: String) -> String:
	if silence_flag == "late_reply_sarah_meal_j1" and choice_node == "j1_06_choice_sarah_meal" and json_path.contains("sarah_meal_j1_v2"):
		return "j1_06_sarah_late_reopen_001"
	if silence_flag == "ignored_nico_respiration_j1" and choice_node == "j1_07_choice_nico_respiration" and json_path.contains("nico_respiration_j1_v2"):
		return "j1_07_nico_late_reopen_001"
	return ""

func consume_current_late_reopen(start_node: String) -> void:
	if start_node == "":
		return
	var state: Dictionary = current()
	var consumed_flag: String = str(state.get("left_open_flag", ""))
	var consumed_choice_node: String = str(state.get("left_open_choice_node", ""))
	state["late_reopen_consumed"] = true
	state["late_reopen_consumed_flag"] = consumed_flag
	state["late_reopen_consumed_choice_node"] = consumed_choice_node
	state["late_reply_prepared"] = false
	state["left_open"] = false
	state["active_choice_node"] = ""
	state["pending_choice_option_count"] = 0
	state["next_node"] = start_node
	save_progression()

func record_current_choice(choice_id: String) -> void:
	var state: Dictionary = current()
	state["started"] = true
	state["choices"].append(choice_id)
	state["left_open"] = false
	state["left_open_choice_node"] = ""
	state["left_open_flag"] = ""
	state["late_reply_prepared"] = false
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
	current()["pending_choice_option_count"] = 0
	current()["left_open"] = false
	current()["left_open_choice_node"] = ""
	current()["left_open_flag"] = ""
	current()["late_reply_prepared"] = false
	if current_conversation_id == "j1_00_reveil_v2":
		_unlock_j1_v2_after_priority_choice()
	_unlock_j1_v2_breathing_scenes_if_ready()
	_repair_j2_v2_progression_unlocks()
	_repair_j3_v2_progression_unlocks()
	_repair_j4_v2_progression_unlocks()
	refresh_day_progression()
	save_progression()

func _unlock_j1_v2_after_priority_choice() -> void:
	if conversations.has("sarah_j1_v2"):
		conversations["sarah_j1_v2"]["available"] = true
		mark_conversation_new("sarah_j1_v2", "Sarah attend ta réponse.")
	if conversations.has("camille_j1_v2"):
		conversations["camille_j1_v2"]["available"] = true
		mark_conversation_new("camille_j1_v2", "Camille attend ta réponse.")
	if conversations.has("nico_j1_v2"):
		conversations["nico_j1_v2"]["available"] = true
		mark_conversation_new("nico_j1_v2", "Nico peut couvrir une partie.")
	if conversations.has("maya_j1_v2"):
		conversations["maya_j1_v2"]["available"] = true
		mark_conversation_new("maya_j1_v2", "Maya a noté le timing.")
	if conversations.has("ines_j1_v2"):
		conversations["ines_j1_v2"]["available"] = true
		mark_conversation_new("ines_j1_v2", "Inès ouvre une porte.")
	var forced_j1_v2_id: String = _j1_v2_forced_first_reply_conversation_id()
	if forced_j1_v2_id != "":
		current_conversation_id = forced_j1_v2_id

func _j1_v2_core_conversations_done() -> bool:
	for id in ["sarah_j1_v2", "camille_j1_v2", "nico_j1_v2", "maya_j1_v2", "ines_j1_v2"]:
		if not conversations.has(id):
			return false
		if not bool(conversations[id].get("done", false)):
			return false
	return true

func _unlock_j1_v2_breathing_scenes_if_ready() -> void:
	if not experimental_j1_v2_enabled or current_day != 1:
		return
	if not _j1_v2_core_conversations_done():
		return
	_attach_j1_v2_followup_scene("sarah_j1_v2", "res://data/sarah_meal_j1_v2_experimental.json", "j1_06_sarah_001", "J1 V2 — Rentrer manger", "Sarah parle du repas.")
	_attach_j1_v2_followup_scene("nico_j1_v2", "res://data/nico_respiration_j1_v2_experimental.json", "j1_07_nico_001", "J1 V2 — Respiration", "Nico tente une respiration.")

func _attach_j1_v2_followup_scene(conversation_id: String, json_path: String, start_node: String, title: String, preview: String) -> void:
	if not conversations.has(conversation_id):
		return
	var state: Dictionary = conversations[conversation_id]
	if str(state.get("json_path", "")) == json_path:
		return
	state["json_path"] = json_path
	state["start_node"] = start_node
	state["title"] = title
	state["available"] = true
	state["done"] = false
	state["next_node"] = start_node
	state["active_choice_node"] = ""
	mark_conversation_new(conversation_id, preview)

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
	_repair_j2_v2_progression_unlocks()
	_repair_j3_v2_progression_unlocks()
	_repair_j4_v2_progression_unlocks()
	if current_day >= 6:
		day_transition_available = false
		return
	if _required_conversations_for_current_mode(current_day).is_empty():
		day_transition_available = false
		return
	if completed_days.has(current_day):
		day_transition_available = false
		return
	day_transition_available = _is_day_complete(current_day)

func _required_conversations_for_current_mode(day: int) -> Array:
	if experimental_j1_v2_enabled and day == 1:
		return [
			"j1_00_reveil_v2",
			"sarah_j1_v2",
			"camille_j1_v2",
			"nico_j1_v2",
			"maya_j1_v2",
			"ines_j1_v2"
		]
	if _has_j1_v2_progression() and day == 1:
		return [
			"j1_00_reveil_v2",
			"sarah_j1_v2",
			"camille_j1_v2",
			"nico_j1_v2",
			"maya_j1_v2",
			"ines_j1_v2"
		]
	if experimental_j1_v2_enabled and day == 2:
		return [
			"sarah_j2_v2",
			"nico_j2_v2",
			"camille_j2_v2",
			"maya_j2_v2"
		]
	if experimental_j1_v2_enabled and day == 3:
		return [
			"sarah_j3_v2",
			"nico_j3_v2",
			"camille_j3_v2",
			"maya_j3_v2"
		]
	if experimental_j1_v2_enabled and day == 4:
		return [
			"sarah_j4_v2",
			"nico_j4_v2",
			"sarah_j4_followup_v2",
			"camille_j4_v2",
			"maya_j4_v2"
		]
	return REQUIRED_CONVERSATIONS_BY_DAY.get(day, [])

func _is_day_complete(day: int) -> bool:
	var required_ids: Array = _required_conversations_for_current_mode(day)
	if required_ids.is_empty():
		return false
	for id in required_ids:
		if not _is_required_conversation_complete(id, day):
			return false
	return true

func _is_required_conversation_complete(id: String, day: int) -> bool:
	if not conversations.has(id):
		return false
	var state: Dictionary = conversations[id]
	if str(state.get("active_choice_node", "")) != "":
		return false
	if bool(state.get("done", false)):
		return true
	if day == 1 and _has_j1_v2_progression() and id == "j1_00_reveil_v2" and bool(state.get("available", false)):
		return true
	if (experimental_j1_v2_enabled or _has_j1_v2_progression()) and day == 1:
		var json_path: String = str(state.get("json_path", ""))
		if id == "sarah_j1_v2" and json_path.contains("sarah_meal_j1_v2"):
			return true
		if id == "nico_j1_v2" and json_path.contains("nico_respiration_j1_v2"):
			return true
	return false

func advance_to_next_day() -> void:
	refresh_day_progression()
	if not day_transition_available:
		return
	_advance_day_unchecked()

func force_advance_to_next_day_for_testing() -> void:
	if current_day >= 6:
		return
	if current_day == 1 and _has_j1_v2_progression() and not experimental_j1_v2_enabled:
		experimental_j1_v2_enabled = true
	_advance_day_unchecked()

func _has_j1_v2_progression() -> bool:
	for id in ["j1_00_reveil_v2", "sarah_j1_v2", "camille_j1_v2", "nico_j1_v2", "maya_j1_v2", "ines_j1_v2"]:
		if not conversations.has(id):
			continue
		var state: Dictionary = conversations[id]
		if bool(state.get("started", false)) or bool(state.get("done", false)) or not state.get("messages", []).is_empty():
			return true
	return false

func _advance_day_unchecked() -> void:
	if not completed_days.has(current_day):
		completed_days.append(current_day)
	current_day += 1
	if _has_j1_v2_progression() and current_day == 2 and not experimental_j1_v2_enabled:
		experimental_j1_v2_enabled = true
	if experimental_j1_v2_enabled and current_day == 2:
		_unlock_j2_v2_initial_conversations()
	if experimental_j1_v2_enabled and current_day == 3:
		_unlock_j3_v2_initial_conversations()
	if experimental_j1_v2_enabled and current_day == 4:
		_unlock_j4_v2_initial_conversations()
	day_transition_available = false
	save_progression()

func _unlock_j2_v2_initial_conversations() -> void:
	if conversations.has("sarah_j2_v2") and not bool(conversations["sarah_j2_v2"].get("done", false)):
		conversations["sarah_j2_v2"]["available"] = true
		mark_conversation_new("sarah_j2_v2", "Sarah a écrit ce matin.")
	if conversations.has("nico_j2_v2") and not bool(conversations["nico_j2_v2"].get("done", false)):
		conversations["nico_j2_v2"]["available"] = true
		mark_conversation_new("nico_j2_v2", "Nico vérifie si ça tient encore.")

func _unlock_j3_v2_initial_conversations() -> void:
	if conversations.has("sarah_j3_v2") and not bool(conversations["sarah_j3_v2"].get("done", false)):
		conversations["sarah_j3_v2"]["available"] = true
		mark_conversation_new("sarah_j3_v2", "Sarah observe la journée.")
	if conversations.has("nico_j3_v2") and not bool(conversations["nico_j3_v2"].get("done", false)):
		conversations["nico_j3_v2"]["available"] = true
		mark_conversation_new("nico_j3_v2", "Nico répond plus tard que d’habitude.")

func _unlock_j4_v2_initial_conversations() -> void:
	if not experimental_j1_v2_enabled or current_day != 4:
		return
	if conversations.has("sarah_j4_v2") and not bool(conversations["sarah_j4_v2"].get("done", false)):
		conversations["sarah_j4_v2"]["available"] = true
		mark_conversation_new("sarah_j4_v2", "Sarah a remarqué un détail ce matin.")

func _unlock_j2_v2_after_morning_if_ready() -> void:
	_repair_j2_v2_progression_unlocks()

func _repair_j2_v2_progression_unlocks() -> void:
	if not experimental_j1_v2_enabled or current_day != 2:
		return
	var morning_done := false
	if conversations.has("sarah_j2_v2") and bool(conversations["sarah_j2_v2"].get("done", false)):
		morning_done = true
	if conversations.has("nico_j2_v2") and bool(conversations["nico_j2_v2"].get("done", false)):
		morning_done = true
	if morning_done and conversations.has("camille_j2_v2") and not bool(conversations["camille_j2_v2"].get("done", false)) and not bool(conversations["camille_j2_v2"].get("available", false)):
		conversations["camille_j2_v2"]["available"] = true
		mark_conversation_new("camille_j2_v2", "Camille reprend le fil.")
	if conversations.has("camille_j2_v2") and bool(conversations["camille_j2_v2"].get("done", false)):
		if conversations.has("maya_j2_v2") and not bool(conversations["maya_j2_v2"].get("done", false)) and not bool(conversations["maya_j2_v2"].get("available", false)):
			conversations["maya_j2_v2"]["available"] = true
			mark_conversation_new("maya_j2_v2", "Maya revient sur la photo.")
	if conversations.has("maya_j2_v2") and bool(conversations["maya_j2_v2"].get("done", false)):
		if conversations.has("ines_j2_v2") and not bool(conversations["ines_j2_v2"].get("done", false)) and not bool(conversations["ines_j2_v2"].get("available", false)):
			conversations["ines_j2_v2"]["available"] = true
			mark_conversation_new("ines_j2_v2", "Inès écrit plus tard.")

func _repair_j3_v2_progression_unlocks() -> void:
	if not experimental_j1_v2_enabled or current_day != 3:
		return
	var morning_done := false
	if conversations.has("sarah_j3_v2") and bool(conversations["sarah_j3_v2"].get("done", false)):
		morning_done = true
	if conversations.has("nico_j3_v2") and bool(conversations["nico_j3_v2"].get("done", false)):
		morning_done = true
	if morning_done and conversations.has("camille_j3_v2") and not bool(conversations["camille_j3_v2"].get("done", false)) and not bool(conversations["camille_j3_v2"].get("available", false)):
		conversations["camille_j3_v2"]["available"] = true
		mark_conversation_new("camille_j3_v2", "Camille revient dans l’après-midi.")
	if conversations.has("camille_j3_v2") and bool(conversations["camille_j3_v2"].get("done", false)):
		if conversations.has("maya_j3_v2") and not bool(conversations["maya_j3_v2"].get("done", false)) and not bool(conversations["maya_j3_v2"].get("available", false)):
			conversations["maya_j3_v2"]["available"] = true
			mark_conversation_new("maya_j3_v2", "Maya revient sur l’ambiance.")
	if conversations.has("maya_j3_v2") and bool(conversations["maya_j3_v2"].get("done", false)):
		if conversations.has("ines_j3_v2") and not bool(conversations["ines_j3_v2"].get("done", false)) and not bool(conversations["ines_j3_v2"].get("available", false)):
			conversations["ines_j3_v2"]["available"] = true
			mark_conversation_new("ines_j3_v2", "Inès écrit en soirée.")

func _repair_j4_v2_progression_unlocks() -> void:
	if not experimental_j1_v2_enabled or current_day != 4:
		return
	if conversations.has("sarah_j4_v2") and bool(conversations["sarah_j4_v2"].get("done", false)):
		if conversations.has("nico_j4_v2") and not bool(conversations["nico_j4_v2"].get("done", false)) and not bool(conversations["nico_j4_v2"].get("available", false)):
			conversations["nico_j4_v2"]["available"] = true
			mark_conversation_new("nico_j4_v2", "Nico répond quand il peut.")
	if conversations.has("nico_j4_v2") and bool(conversations["nico_j4_v2"].get("done", false)):
		if conversations.has("sarah_j4_followup_v2") and not bool(conversations["sarah_j4_followup_v2"].get("done", false)) and not bool(conversations["sarah_j4_followup_v2"].get("available", false)):
			conversations["sarah_j4_followup_v2"]["available"] = true
			mark_conversation_new("sarah_j4_followup_v2", "Sarah attend toujours ta réponse.")
	if conversations.has("sarah_j4_followup_v2") and bool(conversations["sarah_j4_followup_v2"].get("done", false)):
		if conversations.has("camille_j4_v2") and not bool(conversations["camille_j4_v2"].get("done", false)) and not bool(conversations["camille_j4_v2"].get("available", false)):
			conversations["camille_j4_v2"]["available"] = true
			mark_conversation_new("camille_j4_v2", "Camille écrit pendant sa pause.")
	if conversations.has("camille_j4_v2") and bool(conversations["camille_j4_v2"].get("done", false)):
		if conversations.has("maya_j4_v2") and not bool(conversations["maya_j4_v2"].get("done", false)) and not bool(conversations["maya_j4_v2"].get("available", false)):
			conversations["maya_j4_v2"]["available"] = true
			mark_conversation_new("maya_j4_v2", "Maya revient sur l’ambiance.")
	if conversations.has("maya_j4_v2") and bool(conversations["maya_j4_v2"].get("done", false)):
		if conversations.has("ines_j4_v2") and not bool(conversations["ines_j4_v2"].get("done", false)) and not bool(conversations["ines_j4_v2"].get("available", false)):
			conversations["ines_j4_v2"]["available"] = true
			mark_conversation_new("ines_j4_v2", "Inès écrit tard.")

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
		"experimental_j1_v2_enabled": experimental_j1_v2_enabled,
		"dynamic_notifications_fired": dynamic_notifications_fired.duplicate(true),
		"global_game_state": global_game_state.duplicate(true),
		"conversation_blocks": conversation_blocks.duplicate(true),
		"conversations": {}
	}
	for id in conversation_ids():
		var state: Dictionary = conversations[id]
		payload["conversations"][id] = {
			"available": bool(state.get("available", false)),
			"title": str(state.get("title", "")),
			"json_path": str(state.get("json_path", "")),
			"start_node": str(state.get("start_node", "")),
			"started": bool(state.get("started", false)),
			"messages": state.get("messages", []).duplicate(true),
			"game_state": state.get("game_state", {}).duplicate(true),
			"active_choice_node": str(state.get("active_choice_node", "")),
			"pending_choice_option_count": int(state.get("pending_choice_option_count", 0)),
			"next_node": str(state.get("next_node", "")),
			"done": bool(state.get("done", false)),
			"choices": state.get("choices", []).duplicate(true),
			"left_open": bool(state.get("left_open", false)),
			"left_open_choice_node": str(state.get("left_open_choice_node", "")),
			"left_open_count": int(state.get("left_open_count", 0)),
			"left_open_flag": str(state.get("left_open_flag", "")),
			"late_reply_prepared": bool(state.get("late_reply_prepared", false)),
			"late_reopen_consumed": bool(state.get("late_reopen_consumed", false)),
			"late_reopen_consumed_flag": str(state.get("late_reopen_consumed_flag", "")),
			"late_reopen_consumed_choice_node": str(state.get("late_reopen_consumed_choice_node", "")),
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
	experimental_j1_v2_enabled = bool(payload.get("experimental_j1_v2_enabled", experimental_j1_v2_enabled))
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
		state["available"] = bool(saved_state.get("available", state.get("available", false)))
		state["title"] = str(saved_state.get("title", state.get("title", "")))
		state["json_path"] = str(saved_state.get("json_path", state.get("json_path", "")))
		state["start_node"] = str(saved_state.get("start_node", state.get("start_node", "")))
		state["started"] = bool(saved_state.get("started", state.get("started", false)))
		state["messages"] = saved_state.get("messages", state.get("messages", [])).duplicate(true)
		state["game_state"] = saved_state.get("game_state", state.get("game_state", {})).duplicate(true)
		state["active_choice_node"] = str(saved_state.get("active_choice_node", state.get("active_choice_node", "")))
		state["pending_choice_option_count"] = int(saved_state.get("pending_choice_option_count", state.get("pending_choice_option_count", 0)))
		state["next_node"] = str(saved_state.get("next_node", state.get("next_node", "")))
		state["done"] = bool(saved_state.get("done", state.get("done", false)))
		state["choices"] = saved_state.get("choices", state.get("choices", [])).duplicate(true)
		state["left_open"] = bool(saved_state.get("left_open", state.get("left_open", false)))
		state["left_open_choice_node"] = str(saved_state.get("left_open_choice_node", state.get("left_open_choice_node", "")))
		state["left_open_count"] = int(saved_state.get("left_open_count", state.get("left_open_count", 0)))
		state["left_open_flag"] = str(saved_state.get("left_open_flag", state.get("left_open_flag", "")))
		state["late_reply_prepared"] = bool(saved_state.get("late_reply_prepared", state.get("late_reply_prepared", false)))
		state["late_reopen_consumed"] = bool(saved_state.get("late_reopen_consumed", state.get("late_reopen_consumed", false)))
		state["late_reopen_consumed_flag"] = str(saved_state.get("late_reopen_consumed_flag", state.get("late_reopen_consumed_flag", "")))
		state["late_reopen_consumed_choice_node"] = str(saved_state.get("late_reopen_consumed_choice_node", state.get("late_reopen_consumed_choice_node", "")))
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
	global_game_state = _default_global_game_state()
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
