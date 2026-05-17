# T071 — Correctif runtime badge nouveau après unlock bloc

## Contexte

Après T068/T070, le playtest runtime montrait que les blocs/unlocks fonctionnaient, mais que le badge `nouveau` n’apparaissait toujours pas de manière fiable dans l’écran Messages.

Symptôme côté Ludo :
- Camille/Sarah alternent correctement ;
- les previews existent ;
- mais le badge `nouveau` n’est pas visible lors d’un unlock de bloc.

## Cause probable

Le guard `_can_emit_block_unlock_notification()` dépendait encore de :

```gdscript
has_available_block_for_conversation(target_id)
```

au moment exact de l’unlock.

Ce test est fragile car le bloc vient justement d’être rendu `available`. La décision de poser le badge doit être basée sur le bloc débloqué, pas sur une requête globale qui peut dépendre de l’état courant, de la migration ou du contexte runtime.

## Correction appliquée

Fichier modifié :

```txt
product/godot_t004_prototype/scripts/conversation_state.gd
```

Changements :

```gdscript
_can_emit_block_unlock_notification(target_id, block_id)
```

remplace l’ancien guard basé uniquement sur `target_id`.

Le guard vérifie maintenant :
- cible non vide ;
- cible différente de la conversation courante ;
- cible existante ;
- bloc débloqué connu dans `conversation_block_defs` ;
- le bloc débloqué appartient bien à la conversation cible ;
- conversation cible disponible ;
- conversation cible non terminée.

Il ne re-query plus `has_available_block_for_conversation(target_id)`.

## Comportement attendu

Quand un bloc est débloqué pour une autre conversation :

```txt
has_new = true
last_preview = Nouveau message de Camille/Sarah
```

La sauvegarde reste immédiate via `mark_conversation_new()`.

## Tests

Fichier modifié :

```txt
product/godot_t004_prototype/tests/test_t070_block_unlock_badges_previews.py
```

Ajout :

```python
test_t071_unlock_badge_guard_does_not_requery_available_block_after_unlock
```

Le test vérifie que le guard ne dépend plus de `has_available_block_for_conversation()` et prend en compte `unlocked_block_id`.

## Validation

Commandes exécutées :

```bash
python3 product/godot_t004_prototype/tests/test_t070_block_unlock_badges_previews.py
```

Résultat : OK.

Suite complète :

```bash
for f in product/godot_t004_prototype/tests/test_*.py; do python3 "$f" || exit 1; done
```

Résultat : OK.

Tests validés :
- T053 ;
- T057 ;
- T063 ;
- T068 ;
- T070/T071.

Validation JSON :
- Camille J1 : 45 nodes, 6 choix, 3 fins, 0 lien cassé ;
- Sarah J1 : 41 nodes, 5 choix, 3 fins, 0 lien cassé ;
- Camille J2 : 45 nodes, 5 choix, 3 fins, 0 lien cassé ;
- Sarah J2 : 45 nodes, 5 choix, 3 fins, 0 lien cassé.

## Non modifié

- JSON dialogues ;
- schéma T003 ;
- config `conversation_blocks.json` ;
- UX ;
- contenu J3.

## Limite

Godot CLI absent sur le VPS : runtime à valider côté Ludo.

## Next step

T072 — Playtest runtime badges/previews après correctif T071.
