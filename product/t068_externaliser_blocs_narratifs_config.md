# T068 — Externaliser les blocs narratifs dans une config

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Sortir les frontières et unlocks de blocs du code avant J3, sans modifier les JSON de dialogue.

## Implémentation

### Config blocs ajoutée

Nouveau fichier :

- `product/godot_t004_prototype/data/conversation_blocks.json`

Il contient :

- `schema_version` ;
- `block_order` ;
- `blocks` ;
- blocs J1 ;
- blocs J2 ;
- contact logique ;
- conversation runtime ;
- node de début ;
- nodes de fin ;
- bloc suivant à unlock ;
- cible de notification ;
- texte d’attente.

### Blocs externalisés

J1 :

- `camille_c1a`
- `sarah_s1a`
- `camille_c1b`
- `sarah_s1b`
- `camille_c1c`
- `sarah_s1c`

J2 :

- `camille_c2a`
- `sarah_s2a`
- `camille_c2b`
- `sarah_s2b`
- `camille_c2c`
- `sarah_s2c`

## Changements Godot

`conversation_state.gd` lit maintenant :

```gdscript
res://data/conversation_blocks.json
```

via :

```gdscript
const BLOCKS_CONFIG_PATH := "res://data/conversation_blocks.json"
func _load_conversation_block_defs() -> void
```

Les constantes hardcodées de frontières de blocs ont été retirées du script.

Le runtime conserve :

- `conversation_block_defs` chargé depuis JSON ;
- `conversation_block_order` chargé depuis JSON ;
- `conversation_blocks` pour les statuts sauvegardés.

## Comportement inchangé

Le comportement J1/J2 reste le même :

```text
C1A → S1A → C1B → S1B → C1C → S1C
C2A → S2A → C2B → S2B → C2C → S2C
```

Les états restent :

- `locked` ;
- `available` ;
- `active` ;
- `done`.

Les notifications restent liées à l’unlock réel d’un bloc.

## Sauvegarde

La sauvegarde reste compatible :

- `SAVE_VERSION = 4` conservé ;
- `conversation_blocks` reste le format de sauvegarde ;
- anciennes saves sans certains blocs reçoivent les valeurs par défaut ;
- messages / choix / previews / badges / `current_day` / `completed_days` / `dynamic_notifications_fired` restent conservés.

## Tests adaptés

Tests mis à jour / ajoutés :

- `tests/test_t068_externalized_blocks.py`
- `tests/test_t063_j2_integration.py`
- `tests/test_t057_narrative_blocks.py`

Tests exécutés :

```bash
python3 tests/test_t068_externalized_blocks.py
python3 tests/test_t063_j2_integration.py
python3 tests/test_t057_narrative_blocks.py
python3 tests/test_t053_notification_guards.py
```

Résultat : OK.

## Validation config

Validation statique :

- 12 blocs déclarés ;
- 12 blocs dans `block_order` ;
- tous les `conversation_id` ciblent une conversation existante ;
- tous les `start_node` existent ;
- tous les `end_nodes` existent ;
- tous les `unlock_on_done` ciblent un bloc existant ou vide ;
- toutes les `notification_target` ciblent une conversation existante ou vide.

## Validation JSON dialogues

Aucun JSON de dialogue modifié.

- Camille J1 : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Camille J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.

## Non-changements

- Aucun JSON dialogue modifié.
- Aucun J3 écrit.
- Aucun nouveau système de calendrier.
- Aucun scheduler.
- Aucune horloge réelle.
- Aucun changement gameplay voulu.
- Aucun changement UX voulu.

## Limite restante

Les blocs sont externalisés, mais il n’y a pas encore d’outil d’édition visuel.  
La config JSON est éditable à la main et suffisante pour préparer J3.

Godot CLI absent ici : runtime à valider côté Ludo sur Godot 4.6.
