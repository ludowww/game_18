# T072 — Réparer badges/previews pour saves existantes après externalisation

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Ajouter une réparation légère pour les anciennes sauvegardes après externalisation des blocs narratifs, afin de restaurer les badges / previews quand un bloc est disponible mais que la save ne contient pas le bon `has_new`.

## Problème ciblé

Après T068, les frontières / unlocks de blocs sont lues depuis :

```text
res://data/conversation_blocks.json
```

Certaines saves existantes peuvent avoir :

- un bloc `available` ;
- une conversation pertinente à ouvrir ;
- mais pas de badge `has_new` ;
- ou une preview non remise à jour.

Résultat : le joueur peut ne pas voir qu’un bloc est réellement disponible.

## Réparation ajoutée

Ajout dans `ConversationState` :

```gdscript
func repair_available_block_notifications() -> void
```

Cette réparation est appelée :

- après `load_progression()` dans `_ready()` ;
- au refresh de l’écran Messages dans `conversation_list.gd`.

## Règles de réparation

La réparation parcourt les blocs et restaure un badge uniquement si :

- le bloc est `available` ;
- la conversation cible existe ;
- la conversation cible est disponible ;
- la conversation cible n’est pas `done` ;
- la conversation cible n’est pas la conversation courante ;
- le bloc disponible n’a pas déjà commencé à être lu.

Si ces conditions sont remplies :

```gdscript
state["has_new"] = true
state["last_preview"] = "Nouveau message de Camille/Sarah"
```

## Protection previews

La réparation évite d’écraser un vrai dernier message si le joueur a déjà commencé à lire le bloc.

Helper ajouté :

```gdscript
func _has_started_available_block(conversation_id: String, block_def: Dictionary) -> bool
```

Un bloc est considéré commencé si :

- un choix actif existe ;
- `next_node` existe et ne correspond plus au `start_node` du bloc.

Donc :

- bloc available non ouvert → badge restauré ;
- bloc déjà commencé → preview conservée.

## Sauvegarde

La sauvegarde reste compatible :

- pas de changement de format ;
- `SAVE_VERSION = 4` conservé ;
- `conversation_blocks` inchangé ;
- messages / choix / previews / badges existants conservés ;
- réparation sauvegardée uniquement si elle modifie vraiment un badge.

## Non-changements

- Aucun JSON dialogue modifié.
- Aucun J3 écrit.
- Aucun changement de schéma T003.
- Aucun scheduler.
- Aucune horloge réelle.
- Aucun changement UX volontaire.

## Tests

Test ajouté :

- `product/godot_t004_prototype/tests/test_t072_repair_existing_save_badges.py`

Tests exécutés :

```bash
python3 tests/test_t072_repair_existing_save_badges.py
python3 tests/test_t068_externalized_blocks.py
python3 tests/test_t063_j2_integration.py
python3 tests/test_t057_narrative_blocks.py
python3 tests/test_t053_notification_guards.py
```

Résultat : OK.

## Validation JSON dialogues

Aucun JSON dialogue modifié.

- Camille J1 : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Camille J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.

Godot CLI absent ici : runtime à valider côté Ludo sur Godot 4.6.
