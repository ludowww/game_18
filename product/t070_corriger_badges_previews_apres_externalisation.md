# T070 — Corriger badges/previews après externalisation des blocs

Thread : Scope MVP / technique

Statut : DONE

## Contexte

T069 runtime a validé le flux principal après T068 :

- blocs / unlocks OK ;
- alternance J1/J2 OK ;
- mais perte ou fragilité des badges `nouveau` et des previews Messages après passage aux blocs externalisés.

T070 corrige donc la jonction :

```txt
conversation_blocks.json → _unlock_block() → mark_conversation_new() → has_new / last_preview → Messages list
```

## Correction appliquée

Fichier modifié :

- `product/godot_t004_prototype/scripts/conversation_state.gd`

Changements :

- `_unlock_block()` ne réouvre plus un bloc déjà `available`, `active` ou `done` : seul un bloc `locked` peut être débloqué.
- Ajout de `_can_emit_block_unlock_notification(target_id)` pour sécuriser les badges issus des unlocks de blocs.
- Ajout de `_notification_preview_for_target(target_id)` pour garder une preview neutre et centralisée :
  - `Nouveau message de Sarah`
  - `Nouveau message de Camille`
- Les unlocks de blocs repassent explicitement par `mark_conversation_new(target_id, preview)`.
- Si aucun badge ne doit être posé, l’état de bloc est quand même sauvegardé via `save_progression()`.

## Non-changements

- Aucun JSON dialogue modifié.
- Aucun changement de schéma T003.
- Aucun changement de `conversation_blocks.json`.
- Aucun ajout OS notification / scheduler / temps réel.
- Aucun contenu J3 écrit ou intégré.

## Validation statique

Tests exécutés :

```txt
product/godot_t004_prototype/tests/test_t070_block_unlock_badges_previews.py OK
product/godot_t004_prototype/tests/test_t068_externalized_blocks.py OK
product/godot_t004_prototype/tests/test_t063_j2_integration.py OK
product/godot_t004_prototype/tests/test_t057_narrative_blocks.py OK
product/godot_t004_prototype/tests/test_t053_notification_guards.py OK
```

JSON inchangés / liens OK :

```txt
camille_j1_complete.json : 45 nodes, 6 choice nodes, 3 end nodes, duplicate_id=0, missing=0, sha=fba4627bd236
sarah_j1_complete.json   : 41 nodes, 5 choice nodes, 3 end nodes, duplicate_id=0, missing=0, sha=33512a06b873
camille_j2_complete.json : 45 nodes, 5 choice nodes, 3 end nodes, duplicate_id=0, missing=0, sha=c9e0993c7ed5
sarah_j2_complete.json   : 45 nodes, 5 choice nodes, 3 end nodes, duplicate_id=0, missing=0, sha=f19e87f45c0c
conversation_blocks.json : 12 blocks, 12 order entries, sha=0d4dd12aa8c5
```

Godot CLI local VPS : absent. Runtime à valider côté Ludo Godot 4.6.

## Checklist runtime T071

1. Reset save.
2. Jouer Camille jusqu’à fin C1A.
3. Retour Messages : Sarah doit avoir badge `nouveau` + preview `Nouveau message de Sarah`.
4. Ouvrir Sarah : seul le badge Sarah disparaît.
5. Jouer Sarah jusqu’à unlock Camille : Camille doit récupérer badge + preview neutre.
6. Refaire sur J2 après passage Jour 2.
7. Quitter/relaunch : badges/previews doivent survivre via save.

## Décision

T070 verrouille la correction technique avant de reprendre l’intégration/écriture J3. Si T071 runtime valide, la Roadmap peut repasser à la production J3.