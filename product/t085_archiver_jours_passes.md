# T085 — Archiver les jours passés hors liste Messages active

Statut : DONE
Thread : Scope MVP / technique

## Objectif

Garder l'écran Messages lisible en affichant par défaut uniquement les conversations du jour courant, tout en laissant les jours passés relisibles dans une zone secondaire.

## Décision MVP

- `Messages` = conversations actives du `current_day` uniquement.
- `Archives / Jours précédents` = conversations des jours passés, repliées par défaut.
- Les conversations archivées restent ouvrables et lisibles.
- Les badges/previews actifs ne polluent plus la boîte de réception du jour courant.

## Implémentation

Fichiers modifiés :

- `product/godot_t004_prototype/scripts/conversation_state.gd`
  - ajout de helpers jour courant / jours passés ;
  - `active_conversation_ids()` filtre les conversations du `current_day` ;
  - helpers d'archives pour regrouper les anciennes conversations ;
  - preview day-aware sans modifier les données narratives.

- `product/godot_t004_prototype/scripts/conversation_list.gd`
  - la liste principale utilise maintenant `ConversationState.active_conversation_ids()` ;
  - ajout d'une section discrète `Archives / Jours précédents`, repliée par défaut ;
  - les entrées archivées réutilisent `_make_conversation_entry(...)`, donc restent ouvrables ;
  - refresh UI corrigé pour reconstruire proprement après ouverture/fermeture des archives.

- `product/godot_t004_prototype/tests/test_t085_archives_jours_passes.py`
  - test statique ajouté pour verrouiller le comportement attendu.

## Non-changements

- Aucun JSON dialogue modifié.
- Aucun changement du schéma T003.
- Aucun changement de `data/conversation_blocks.json`.
- Aucun bump de sauvegarde : `archives_expanded` est un état UI/runtime local non persisté.
- Pas de système complexe de calendrier, corbeille, recherche ou filtres avancés.

## Validation

Cycle TDD :

- test T085 créé puis lancé avant implémentation : échec attendu RED ;
- implémentation minimale ;
- test T085 puis régressions : OK.

Commande finale :

```bash
python3 tests/test_t085_archives_jours_passes.py \
  && python3 tests/test_t083_mode_test_accelere.py \
  && python3 tests/test_t080_day_transition_button_label.py \
  && python3 tests/test_t078_j3_integration.py \
  && python3 tests/test_t072_repair_existing_save_badges.py \
  && python3 tests/test_t068_externalized_blocks.py \
  && python3 tests/test_t063_j2_integration.py \
  && python3 tests/test_t057_narrative_blocks.py \
  && python3 tests/test_t053_notification_guards.py
```

Sortie :

```text
T085 archives jours passés static checks OK
T083 fast test mode static checks OK
T080 day transition button label tests OK
T078 J3 integration tests OK
T072 repair existing save badge tests OK
T068 externalized block config tests OK
T063 J2 integration tests OK
T057 narrative block lock tests OK
T053 notification guard tests OK
```

Check Godot CLI :

```text
godot_cli_absent
```

## Limite

Validation runtime impossible sur ce VPS car Godot CLI est absent. À vérifier côté Godot 4.6 :

1. lancer le prototype ;
2. progresser J1 → J2 → J3 ;
3. vérifier que la liste active affiche seulement le jour courant ;
4. ouvrir/fermer `Archives / Jours précédents` ;
5. relire J1/J2 depuis les archives ;
6. vérifier qu'aucun ancien badge/preview ne donne l'impression d'un message actif du jour.

## Prochaine étape recommandée

T086 — Playtest runtime archives Messages J1→J3 côté Godot 4.6.
