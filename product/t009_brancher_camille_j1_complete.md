# T009 — Brancher Camille J1 complet dans le prototype

Statut : DONE

## Résultat

Le prototype T004/T006 charge maintenant le fichier complet :

`res://data/camille_j1_complete.json`

Fichier modifié :

`/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

Changement appliqué :

```gdscript
const JSON_PATH := "res://data/camille_j1_complete.json"
```

## Validation statique

Fichier chargé par le prototype :

`/opt/data/profiles/game_18/product/godot_t004_prototype/data/camille_j1_complete.json`

Résultats :

- JSON valide.
- `schema_version = 0.1`.
- 45 nodes.
- 6 choice_nodes.
- 3 end_nodes.
- aucun duplicate_id.
- aucun missing_next_target.
- aucun node unreachable depuis `start_node`.
- les 6 choice nodes sont atteignables.
- les 3 fins sont atteignables :
  - `c1_end_go`
  - `c1_end_resist`
  - `c1_end_seen`

Choice nodes vérifiés :

- `c1_002` : 3 choix OK.
- `c1_005_ignore_choice` : 2 choix OK.
- `c1_006` : 3 choix OK.
- `c1_011` : 3 choix OK.
- `c1_015` : 3 choix OK.
- `c1_021` : 3 choix OK.

## Intégrité JSON

Aucune modification du schéma T003.

Aucune modification du contenu JSON complet Camille J1.

Hash identique entre source narrative et copie prototype :

`fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Fichiers identiques :

- `narrative/t007_camille_j1_complete.json`
- `product/godot_t004_prototype/data/camille_j1_complete.json`

## Runtime Godot

Godot CLI toujours absent dans l’environnement local.

Donc validation runtime/visuelle impossible ici. La validation faite est une validation statique complète du graphe JSON + branchement prototype.
