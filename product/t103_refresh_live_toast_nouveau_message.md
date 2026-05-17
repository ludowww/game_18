# T103 — Corriger toast accès rapide : refresh immédiat après unlock

Statut : DONE  
Thread : Scope MVP / technique  
Portée : correction runtime T102

## Problème

Après T102, le toast `Nouveau message de X · Ouvrir` était calculé seulement au chargement de `conversation_screen.gd`.

Conséquence runtime : quand un bloc débloquait une autre conversation pendant la lecture, `has_new` était bien posé, mais le toast n’apparaissait pas immédiatement. Il devenait visible seulement après un aller-retour Messages → conversation.

## Correction

### `conversation_screen.gd`

Ajout d’un état UI réutilisable :

- `root_container: VBoxContainer`
- `quick_switch_button: Button`
- `quick_switch_target_id: String`

Ajout du helper :

- `_refresh_quick_switch_notification()`

Comportement :

1. Recalcule `ConversationState.quick_switch_new_conversation_id()`.
2. Retire l’ancien bouton si la cible change ou disparaît.
3. Crée le toast via `_make_quick_switch_notification(target_id)` si une cible existe.
4. Le place immédiatement sous le header avec `root_container.move_child(quick_switch_button, 1)`.

### Points de refresh ajoutés

Le helper est appelé :

- à la construction UI initiale ;
- après `ConversationState.handle_dynamic_notification(current_contact_id, node_id)` ;
- après `ConversationState.complete_current_block(next_id)` avant l’état d’attente ;
- après `ConversationState.complete_current_block("")` pour les fins de bloc/conversation.

Ainsi, si un unlock pose `has_new` pendant la lecture, le toast est rafraîchi dans la scène courante sans attendre un reload.

## Comportement préservé

- Texte discret inchangé : `Nouveau message de X · Ouvrir`.
- Clic inchangé :
  - `ConversationState.set_current_conversation(target_id)` ;
  - `ConversationState.mark_conversation_read(target_id)` ;
  - `change_scene_to_file("res://scenes/conversation_screen.tscn")`.
- Filtre T102 conservé : conversation active du jour courant, hors conversation ouverte, avec `has_new`, non `done`.
- Archives / jours passés exclus via `active_conversation_ids()`.

## Non-changements

- Aucun JSON dialogue modifié.
- Aucun changement au schéma T003.
- Aucun changement à `conversation_blocks.json`.
- Aucun changement de save payload.
- Aucune notification OS.
- Aucun scheduler / temps réel.
- Aucun changement de rythme narratif ou typing bubble.

## Validation statique

Test ajouté :

- `product/godot_t004_prototype/tests/test_t103_quick_switch_live_refresh.py`

Test T102 adapté pour accepter le nouveau chemin via refresh helper :

- `product/godot_t004_prototype/tests/test_t102_quick_switch_new_message.py`

Vérifications T103 :

- présence de `_refresh_quick_switch_notification()` ;
- toast plus limité à `_ready()` / build initial ;
- suppression/recréation propre de l’ancien bouton ;
- placement sous le header via `move_child(..., 1)` ;
- refresh après dynamic notification et après fin de bloc/unlock ;
- T102 conservé : open action + current-day filter ;
- hashes inchangés pour dialogues actifs J1→J4, `conversation_blocks.json` et T003.

## Validation exécutée

Régressions lancées :

- `test_t103_quick_switch_live_refresh.py`
- `test_t102_quick_switch_new_message.py`
- `test_t101_typing_bubble_scroll_friendly.py`
- `test_t100_typing_bubble_in_thread.py`
- `test_t099_contact_colors_typing_indicator.py`
- `test_t097_j4_integration.py`
- `test_t090_dialogue_block_validator.py`
- `test_t087_messages_horizontal_overflow.py`
- `test_t085_archives_jours_passes.py`
- `test_t083_mode_test_accelere.py`
- `test_t080_day_transition_button_label.py`
- `test_t078_j3_integration.py`
- `test_t072_repair_existing_save_badges.py`
- `test_t068_externalized_blocks.py`
- `test_t063_j2_integration.py`
- `test_t057_narrative_blocks.py`
- `test_t053_notification_guards.py`

Résultat obtenu : tous OK en validation statique Python.

Godot CLI : `godot_cli_absent` sur VPS.

## Validation runtime attendue côté Ludo

1. Reprendre une conversation J4.
2. Atteindre une fin de bloc qui débloque une autre conversation.
3. Vérifier que le toast `Nouveau message de X · Ouvrir` apparaît immédiatement dans la conversation courante.
4. Cliquer `Ouvrir`.
5. Vérifier que la cible s’ouvre, que son badge est marqué lu, et que la conversation quittée conserve son état.
