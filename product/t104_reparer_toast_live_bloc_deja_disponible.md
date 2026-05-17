# T104 — Réparer toast live : bloc déjà disponible sans badge

Statut : DONE  
Thread : Scope MVP / technique  
Portée : correction runtime T102/T103 + addendum warnings Godot

## Problème

Après T103, le toast `Nouveau message de X · Ouvrir` était bien rafraîchi après fin de bloc, mais le retour runtime Ludo montrait encore le même symptôme :

- pas de toast au bout de la conversation ;
- toast visible seulement après retour Messages puis réouverture.

Diagnostic Roadmap : l’écran Messages appelle déjà `ConversationState.repair_available_block_notifications()` à son chargement. Le fait que le toast apparaisse après passage par Messages indique que le bloc cible peut être `available` mais sans `has_new` dans la save / l’état runtime courant. T103 rafraîchissait donc l’UI, mais sur un état non réparé.

## Correction principale

### `conversation_screen.gd`

Avant chaque refresh toast consécutif à une fin de bloc, appel live de :

- `ConversationState.repair_available_block_notifications()`

Ajout aux deux chemins critiques :

1. `ConversationState.complete_current_block("")`
2. `ConversationState.complete_current_block(next_id)`

Ordre appliqué :

```gdscript
ConversationState.complete_current_block(...)
ConversationState.repair_available_block_notifications()
_refresh_quick_switch_notification()
```

Cela reproduit en live la réparation qui n’était jusque-là déclenchée qu’en revenant sur Messages.

### `conversation_state.gd`

Renforcement de `repair_available_block_notifications()` :

- ne traite que les blocs `BLOCK_STATUS_AVAILABLE` ;
- ignore la conversation courante ;
- ignore les conversations absentes, indisponibles ou `done` ;
- ignore les conversations hors `current_day` ;
- ignore les conversations qui ont déjà `has_new == true` ;
- ignore les blocs déjà commencés via `_has_started_available_block(...)` ;
- pose `has_new = true` + preview neutre seulement pour un bloc disponible, courant, pertinent et non ouvert.

Cela couvre le cas critique : bloc déjà `available` mais badge absent.

## Addendum warnings Godot

Warnings corrigés :

- `conversation_screen.gd` : `var name := Label.new()` renommé en `header_name_label`.
- `conversation_list.gd` : `var name := Label.new()` renommé en `contact_name_label`.

Ces warnings n’étaient pas la cause probable du bug toast, mais ils polluaient le debugger Godot et sont supprimés dans T104.

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

- `product/godot_t004_prototype/tests/test_t104_quick_switch_repair_available_live.py`

Vérifications T104 :

- réparation live appelée avant `_refresh_quick_switch_notification()` après fin de bloc ;
- cas `BLOCK_STATUS_AVAILABLE` sans badge couvert ;
- réparation plus limitée au cycle de vie de `conversation_list.gd` ;
- filtre `current_day` présent ;
- pas de doublon si `has_new` est déjà true ;
- warnings `var name :=` supprimés des scripts Godot ;
- T102/T103 conservés ;
- hashes inchangés pour dialogues actifs J1→J4, `conversation_blocks.json` et T003.

## Validation exécutée

Régressions lancées :

- `test_t104_quick_switch_repair_available_live.py`
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

1. Reprendre la save/état qui reproduisait le bug T103.
2. Arriver en fin de bloc/conversation qui débloque l’autre conversation.
3. Vérifier que le toast `Nouveau message de X · Ouvrir` apparaît immédiatement, sans retour Messages.
4. Cliquer `Ouvrir`.
5. Vérifier que la cible s’ouvre, que son badge est lu, et que la conversation quittée conserve son état.

## Limite / décision si échec

Si T104 échoue encore côté runtime, ne pas empiler de micro-correctifs. Prochaine étape recommandée : ticket d’architecture notification/state avec signal explicite depuis `ConversationState.mark_conversation_new()` vers `conversation_screen.gd`.
