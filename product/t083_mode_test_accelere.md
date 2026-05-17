# T083 — Mode test accéléré

Statut : DONE

## Objectif

Ajouter un outil discret de test pour rejouer rapidement J1→J3 dans le prototype Godot, sans modifier le rythme normal ni les JSON narratifs.

## Implémentation

- Toggle ajouté sur l’écran Messages : `Mode test rapide : ON/OFF`.
- Valeur par défaut : OFF.
- Le mode est porté par `ConversationState.test_fast_mode_enabled`.
- Le bouton appelle `ConversationState.set_test_fast_mode_enabled(...)` puis rafraîchit l’écran Messages.
- Aucun changement dans `conversation_blocks.json` ni dans les JSON de dialogues T003.
- Pas de changement de version de sauvegarde : c’est un état runtime/debug simple.

## Délais en mode test rapide

Quand le toggle est ON :

- délai d’écriture plafonné à `0.35s` ;
- délai avant choix : `0.1s` ;
- lecture narration/système : `0.2s` ;
- respiration entre messages : `0.1s`.

Quand le toggle est OFF, les constantes normales restent inchangées :

- `DEBUG_DELAY_MIN_SECONDS := 1.1` ;
- `DEBUG_DELAY_MAX_SECONDS := 6.5` ;
- `PRE_CHOICE_DELAY_SECONDS := 0.8` ;
- `NARRATION_READ_SECONDS := 1.6` ;
- `MIN_BETWEEN_MESSAGES_SECONDS := 0.6`.

## Fichiers modifiés

- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/scripts/conversation_screen.gd`
- `product/godot_t004_prototype/scripts/conversation_list.gd`
- `product/godot_t004_prototype/tests/test_t083_mode_test_accelere.py`

## Validation statique

Commande exécutée :

```bash
python3 tests/test_t083_mode_test_accelere.py   && python3 tests/test_t080_day_transition_button_label.py   && python3 tests/test_t078_j3_integration.py   && python3 tests/test_t072_repair_existing_save_badges.py   && python3 tests/test_t068_externalized_blocks.py   && python3 tests/test_t063_j2_integration.py   && python3 tests/test_t057_narrative_blocks.py   && python3 tests/test_t053_notification_guards.py
```

Résultat : OK.

```text
T083 fast test mode static checks OK
T080 day transition button label tests OK
T078 J3 integration tests OK
T072 repair existing save badge tests OK
T068 externalized block config tests OK
T063 J2 integration tests OK
T057 narrative block lock tests OK
T053 notification guard tests OK
```

## Limite

Godot CLI absent sur le VPS : `godot_cli_absent`.
La validation runtime doit donc être faite côté Ludo dans Godot 4.6.

## Checklist runtime recommandée

1. Lancer le prototype normalement : vérifier que le rythme OFF est inchangé.
2. Activer `Mode test rapide : ON` depuis Messages.
3. Rejouer Camille/Sarah J1→J3 : vérifier que les délais sont fortement réduits.
4. Désactiver le mode : vérifier retour au rythme normal.
5. Utiliser Reset : vérifier que le prototype reste stable et que le toggle ne casse pas la progression.

## Décision MVP

Le mode test rapide est un outil debug discret, non player-facing. Il sert à accélérer les playtests sans complexifier le schéma T003 ni le système narratif.
