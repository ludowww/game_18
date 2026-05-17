# T043 — Sauvegarde persistante minimale

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Objectif

Conserver l’état multi-conversation après fermeture / relance du jeu, sans cloud, sans compte joueur et sans système complexe.

## Implémentation

Fichiers modifiés :

- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/scripts/conversation_list.gd`

Sauvegarde locale Godot :

```gdscript
user://double_vie_save.json
```

Chargement automatique :

```gdscript
func _ready() -> void:
    load_progression()
```

## Données sauvegardées

Par conversation Camille/Sarah :

- messages affichés ;
- `next_node` ;
- `active_choice_node` ;
- choix effectués ;
- `last_preview` ;
- badge `has_new` ;
- `game_state` minimal ;
- statut `started` ;
- statut `done`.

Global :

- `current_conversation_id` ;
- `save_version`.

## Mécanisme de reset

Un bouton discret `Reset` est ajouté dans l’écran Messages, à côté du sous-titre.

Action :

- réinitialise l’état runtime ;
- supprime `user://double_vie_save.json` ;
- recharge la scène courante.

## Conservé

- JSON T003 inchangé ;
- aucun cloud ;
- aucun compte joueur ;
- aucun système complexe ;
- état multi-conversation séparé Camille/Sarah ;
- previews conservées ;
- badges `nouveau` conservés ;
- Sarah complet reste branchée ;
- Camille inchangée.

## Validation statique

### Camille

- fichier : `product/godot_t004_prototype/data/camille_j1_complete.json`
- schema_version : `0.1`
- contact_id : `camille`
- nodes : 45
- choice_nodes : 6
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- unreachable_node : 0
- sha256 : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

### Sarah

- fichier : `product/godot_t004_prototype/data/sarah_j1_complete.json`
- schema_version : `0.1`
- contact_id : `sarah`
- nodes : 41
- choice_nodes : 5
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- unreachable_node : 0
- sha256 : `33512a06b873d4b95638ed1ba07f08ca302d28671a564785ebac9e137d59dd1f`

## Marqueurs code vérifiés

- `SAVE_PATH := "user://double_vie_save.json"`
- `func save_progression()`
- `func load_progression()`
- `func reset_progression()`
- `load_progression()` appelé au démarrage de `ConversationState`
- sauvegarde de `messages`, `next_node`, `active_choice_node`, `choices`, `last_preview`, `has_new`, `game_state`
- bouton `Reset` présent dans `conversation_list.gd`

## Limite runtime

Godot CLI absent dans l’environnement local : validation runtime à faire côté Ludo sur Godot 4.6.

Checklist T044 proposée :

1. lancer le jeu ;
2. avancer Camille ;
3. avancer Sarah ;
4. quitter complètement ;
5. relancer ;
6. vérifier messages affichés, previews, badges, prochain node et choix actifs ;
7. utiliser `Reset` ;
8. relancer ;
9. vérifier retour à l’état initial.
