# T039 — Intégrer Sarah J1 complet dans le prototype

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Objectif

Remplacer le placeholder Sarah par le contenu complet T037 dans le socle multi-conversation verrouillé.

## Changement appliqué

Fichier modifié :

- `product/godot_t004_prototype/scripts/conversation_state.gd`

Sarah pointe maintenant vers :

```gdscript
res://data/sarah_j1_complete.json
```

Titre liste mis à jour :

```gdscript
Jour 1 — conversation complète MVP
```

## Conservé

- Sarah reste active dans la liste Messages.
- État runtime Sarah séparé conservé.
- `last_preview` conservé.
- `has_new` / badge `nouveau` conservé.
- Camille inchangée.
- JSON T003 inchangé.
- Aucun contenu JSON modifié.
- Aucun système de sauvegarde ajouté.

## Validation statique Sarah complet

Fichier : `product/godot_t004_prototype/data/sarah_j1_complete.json`

- schema_version : `0.1`
- contact_id : `sarah`
- nodes : 41
- 41 nodes
- choice_nodes : 5
- 5 choice nodes
- end_nodes : 3
- 3 end nodes
- duplicate_id : 0
- missing_next_target : 0
- unreachable_node : 0
- sha256 : `bd3aa7c5c8bc92afeaad78cb28459e38a87b37f5b5244c0cd87405664aad71ba`

## Validation Camille inchangée

Fichier : `product/godot_t004_prototype/data/camille_j1_complete.json`

- schema_version : `0.1`
- contact_id : `camille`
- nodes : 45
- choice_nodes : 6
- end_nodes : 3
- 3 end nodes
- duplicate_id : 0
- missing_next_target : 0
- unreachable_node : 0
- sha256 : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

## Marqueurs code vérifiés

Dans `conversation_state.gd` :

- `res://data/sarah_j1_complete.json` présent ;
- `res://data/sarah_j1_placeholder.json` absent ;
- Sarah `available = true` ;
- `has_new` conservé ;
- `last_preview` conservé ;
- dictionnaire `conversations` séparé Camille/Sarah conservé.

## Limite runtime

Godot CLI absent dans l’environnement local : validation runtime à faire côté Ludo sur Godot 4.6.

Checklist runtime T040 proposée :

1. ouvrir Messages ;
2. vérifier Sarah active ;
3. ouvrir Sarah ;
4. vérifier que le contenu complet T037 démarre ;
5. tester les 5 choix ;
6. vérifier les 3 fins ;
7. revenir Messages ;
8. vérifier previews/badge/état séparé ;
9. vérifier que Camille reste inchangée.
