# T030 — Notifications simples / nouveaux messages entre conversations

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Objectif

Tester l’intérêt multi-contact : une conversation peut signaler qu’elle attend l’attention du joueur depuis la liste Messages.

## Décision MVP

Implémentation runtime-only dans `ConversationState` : chaque conversation garde son propre `has_new` et son propre `last_preview`.

Aucun changement de schéma JSON T003, aucun système OS, aucun temps réel complexe, aucune sauvegarde disque.

## Ce qui est ajouté

### État par conversation

Dans `scripts/conversation_state.gd` :

- `has_new` reste séparé par conversation ;
- `last_preview` reste séparé par conversation ;
- `mark_conversation_new(id, preview)` permet de poser un badge simple ;
- `mark_conversation_read(id)` permet de retirer le badge ;
- `mark_current_opened()` marque la conversation ouverte comme lue ;
- les messages affichés dans la conversation ouverte ne recréent pas automatiquement un badge “nouveau”.

### Liste Messages

Dans `scripts/conversation_list.gd` :

- badge visuel `nouveau` sur les conversations qui ont `has_new = true` ;
- preview par conversation via `ConversationState.preview_text(id)` ;
- couleur de preview renforcée si la conversation est nouvelle ;
- Camille et Sarah restent indépendantes.

### État initial de test MVP

Sarah démarre avec `has_new = true` et preview `Nouveau message` pour rendre le badge testable immédiatement depuis l’écran Messages.

À l’ouverture de Sarah, `mark_current_opened()` retire le badge. Camille garde son état séparé.

## Hors-scope confirmé

- pas de notifications OS ;
- pas de push ;
- pas de timers temps réel ;
- pas de sauvegarde disque ;
- pas de logique de disponibilité complexe ;
- pas de modification des JSON narratifs ;
- pas de modification du schéma T003.

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

- `func mark_conversation_new`
- `func mark_conversation_read`
- `func has_new`
- `func _make_new_badge`
- appel liste : `ConversationState.has_new(conversation_id)`

## Limite runtime

Godot CLI absent dans l’environnement local : validation runtime à faire côté Ludo sur Godot 4.6.

Checklist runtime proposée :

1. ouvrir l’écran Messages ;
2. vérifier que Sarah affiche le badge `nouveau` ;
3. ouvrir Sarah ;
4. revenir à Messages ;
5. vérifier que le badge Sarah disparaît ;
6. ouvrir Camille / revenir Messages ;
7. vérifier que les previews restent séparées Camille/Sarah.
