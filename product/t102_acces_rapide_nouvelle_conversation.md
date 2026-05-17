# T102 — Accès rapide à une conversation avec nouveau message

Statut : DONE  
Thread : Scope MVP / technique  
Portée : polish UX navigation / notifications in-app J4

## Objectif

Permettre au joueur qui lit déjà une conversation de basculer rapidement vers une autre conversation active qui vient de recevoir un badge `has_new`, sans devoir revenir manuellement à l’écran Messages.

## Implémentation

### `ConversationState`

Ajout du helper :

- `quick_switch_new_conversation_id()`

Règles MVP :

- parcourt uniquement `active_conversation_ids()` ;
- ignore la conversation actuellement ouverte ;
- ne retourne que les conversations avec `has_new == true` ;
- ignore les conversations `done` ;
- ne parcourt pas les archives / jours passés.

Choix MVP si plusieurs conversations ont `has_new` :

- afficher la première conversation pertinente dans l’ordre de l’inbox active du jour courant ;
- pas de file complexe, pas de centre de notifications.

### `conversation_screen.gd`

Ajout d’une barre/toast in-app discrète sous le header de conversation :

- texte : `Nouveau message de Maya · Ouvrir`, `Nouveau message de Inès · Ouvrir`, etc. ;
- affichée seulement si `ConversationState.quick_switch_new_conversation_id()` retourne une cible ;
- aucun changement automatique de conversation ;
- clic sur la barre = ouverture de la conversation cible.

Action d’ouverture :

- `ConversationState.set_current_conversation(target_id)` ;
- `ConversationState.mark_conversation_read(target_id)` ;
- `get_tree().change_scene_to_file("res://scenes/conversation_screen.tscn")`.

Cette action réutilise donc le même chemin de scène que l’ouverture depuis Messages, tout en ne marquant comme lue que la cible.

## Non-changements

- Aucun JSON dialogue modifié.
- Aucun changement au schéma T003.
- Aucun changement à `conversation_blocks.json`.
- Aucun scheduler / temps réel.
- Aucune notification OS.
- Aucun changement de save payload.
- Aucun changement de rythme narratif ou typing bubble.

## Validation statique

Test ajouté :

- `product/godot_t004_prototype/tests/test_t102_quick_switch_new_message.py`

Le test vérifie :

- présence du helper `quick_switch_new_conversation_id()` ;
- filtrage sur `active_conversation_ids()` et exclusion de la conversation courante ;
- absence d’usage des archives dans le helper ;
- présence d’une notification in-app côté `conversation_screen.gd` ;
- texte neutre `Nouveau message de ... · Ouvrir` ;
- action d’ouverture vers `conversation_screen.tscn` ;
- usage de `set_current_conversation(target_id)` et `mark_conversation_read(target_id)` ;
- non-modification de `conversation_blocks.json`, des dialogues actifs J1→J4 et du schéma T003 par hash.

## Validation exécutée

Régressions lancées :

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

## Limite

Godot CLI est absent sur le VPS si `godot4` / `godot` ne sont pas disponibles. Validation runtime à faire côté Ludo dans Godot 4.6 :

1. Se mettre en J4 avec plusieurs conversations actives.
2. Ouvrir une conversation.
3. Déclencher un unlock/badge `has_new` vers une autre conversation.
4. Vérifier la barre `Nouveau message de X · Ouvrir`.
5. Cliquer dessus.
6. Vérifier que la cible s’ouvre directement, que son badge disparaît, et que la conversation quittée conserve son état.
