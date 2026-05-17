# T032 — Corriger preview dernier message dans Messages

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Objectif

Faire refléter à la liste Messages le dernier message pertinent de chaque conversation.

## Correction appliquée

Fichier modifié :

- `product/godot_t004_prototype/scripts/conversation_state.gd`

La mise à jour de preview est maintenant centralisée dans :

```gdscript
func _preview_for_message(sender: String, text: String) -> String:
```

Règles MVP :

- message contact (`camille`, `sarah`, futur contact) → preview = texte du message ;
- message joueur → preview = `Vous : ...` ;
- message `system` / narration → ignoré pour ne pas polluer la liste Messages ;
- texte vide → ignoré ;
- `has_new` conservé et séparé par conversation ;
- `last_preview` reste stocké séparément pour Camille / Sarah dans `ConversationState.conversations`.

## Pourquoi

Avant T032, `record_current_message()` remplaçait toujours `last_preview` par le texte brut du dernier message affiché, y compris les messages système/narration. Résultat : la liste pouvait rester peu lisible ou afficher une note technique/narrative au lieu du dernier échange utile.

Après T032, la preview suit le dernier message conversationnel pertinent sans modifier la donnée narrative.

## Hors-scope confirmé

- pas de modification JSON ;
- pas de changement du schéma T003 ;
- pas de sauvegarde disque ;
- pas de notification OS ;
- pas de système temps réel ;
- pas de réécriture de la liste Messages.

## Validation statique

Camille :

- fichier : `product/godot_t004_prototype/data/camille_j1_complete.json`
- schema_version : `0.1`
- contact_id : `camille`
- nodes : 45
- choice_nodes : 6
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- sha256 : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Sarah :

- fichier : `product/godot_t004_prototype/data/sarah_j1_placeholder.json`
- schema_version : `0.1`
- contact_id : `sarah`
- nodes : 11
- choice_nodes : 1
- end_nodes : 1
- duplicate_id : 0
- missing_next_target : 0
- sha256 : `604987540aae25eee7a7244cbce3299d92c1cdac5d54e238242b32547dfe21db`

Marqueurs code vérifiés :

- `_preview_for_message`
- `Vous : `
- ignore `sender == "system"`
- `has_new` conservé
- plus de `var state := current()` / `var state := conversation(...)` fragile pour Godot 4.6

## Limite runtime

Godot CLI absent dans l’environnement local : validation runtime à faire côté Ludo sur Godot 4.6.

Checklist runtime proposée :

1. ouvrir Camille ;
2. avancer jusqu’à une réponse joueur ;
3. revenir à Messages ;
4. vérifier preview `Vous : ...` ;
5. avancer jusqu’à un message Camille ;
6. revenir à Messages ;
7. vérifier preview = dernier message Camille ;
8. vérifier que les notes système/narration ne remplacent pas la preview utile ;
9. répéter avec Sarah pour confirmer séparation Camille/Sarah.
