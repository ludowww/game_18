# T026 — Intégrer Sarah J1 placeholder dans le prototype

Statut : DONE

## Objectif

Brancher le contenu Sarah produit en T025A dans la structure multi-conversation T025B, sans modifier le JSON Camille et sans inventer de contenu Sarah.

## Fichiers modifiés

- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_state.gd`
- `/opt/data/profiles/game_18/product/t026_integrer_sarah_j1_placeholder.md`

## Branchement Sarah

Sarah est maintenant activée dans la liste conversations.

Branchement utilisé :

```gdscript
"sarah": _new_conversation_state(
    "sarah",
    "Sarah",
    "Jour 1 — placeholder technique",
    "res://data/sarah_j1_placeholder.json",
    true
)
```

Fichier utilisé :

`/opt/data/profiles/game_18/product/godot_t004_prototype/data/sarah_j1_placeholder.json`

## Fonctionnel attendu

- Liste conversations affiche Camille + Sarah.
- Clic Sarah définit la conversation courante sur `sarah`.
- Le chat charge `res://data/sarah_j1_placeholder.json` via le modèle dynamique T025B.
- Camille et Sarah ont des états runtime séparés dans `ConversationState.conversations`.
- Les previews sont séparées par conversation via `ConversationState.preview_text(conversation_id)`.
- Le choix Sarah est branché via le JSON T003 et validé statiquement.

## JSON conservés

### Camille

Aucune modification.

Hash :

`fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Validation :

- 45 nodes
- 6 choice_nodes
- 3 end_nodes
- aucun duplicate_id
- aucun missing_next_target

### Sarah

Aucune modification du contenu Sarah existant.

Hash :

`604987540aae25eee7a7244cbce3299d92c1cdac5d54e238242b32547dfe21db`

Validation :

- schema_version : `0.1`
- contact_id : `sarah`
- 11 nodes
- 1 choice_node
- 1 end_node
- aucun duplicate_id
- aucun missing_next_target

## Hors-scope respecté

Non ajouté :

- contenu Sarah inventé ;
- sauvegarde persistante ;
- notifications dynamiques ;
- système de contacts complet ;
- historique multi-jours.

## Runtime Godot

Godot CLI absent localement : validation runtime impossible ici.

À vérifier côté Ludo sur Godot 4.6 : liste → Sarah → choix Sarah → retour liste, puis Camille et Sarah gardent des états séparés.
