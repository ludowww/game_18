# T025B — Préparation multi-conversation prototype

Statut : DONE

## Objectif

Préparer le prototype à recevoir Sarah comme deuxième conversation, sans inventer son contenu et sans modifier le JSON Camille.

## Fichiers modifiés

- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_state.gd`
- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_list.gd`
- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

## Structure multi-conversation simple

`ConversationState` contient maintenant une table `conversations` :

- `camille`
- `sarah`

Chaque conversation possède son état séparé :

- `id`
- `display_name`
- `title`
- `json_path`
- `available`
- `started`
- `messages`
- `game_state`
- `active_choice_node`
- `next_node`
- `done`
- `choices`
- `last_preview`
- `has_new`

## Camille

Camille reste la seule conversation jouable.

Branchement conservé :

```gdscript
res://data/camille_j1_complete.json
```

Le comportement T023 est conservé : état runtime, aperçu liste, retour conversation sans restart.

## Sarah

Sarah est préparée techniquement mais non jouable tant que son contenu n’existe pas.

Branchement prévu :

```gdscript
res://data/sarah_j1_complete.json
```

Important : aucun contenu Sarah n’a été inventé.

Dans la liste, Sarah apparaît comme entrée préparée / à venir, désactivée tant que `available = false`.

## Liste conversations

La liste ne hardcode plus uniquement Camille.

Elle boucle sur :

```gdscript
ConversationState.conversation_ids()
```

Elle affiche :

- Camille jouable ;
- Sarah préparée mais désactivée ;
- aperçu par conversation via `ConversationState.preview_text(conversation_id)`.

## Conversation screen

Le chat utilise maintenant la conversation courante :

```gdscript
current_contact_id = ConversationState.current_contact_id()
current_display_name = ConversationState.current_display_name()
current_json_path = ConversationState.current_json_path()
```

Le header, le typing indicator et le chemin JSON sont donc prêts pour une autre conversation.

## Hors-scope respecté

Non ajouté :

- contenu Sarah ;
- contacts complets ;
- avatars avancés ;
- notifications dynamiques ;
- sauvegarde persistante ;
- historique multi-jours ;
- système de statut complexe.

## JSON Camille

Aucune modification du JSON Camille J1.

Hash inchangé :

`fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Validation statique :

- 45 nodes
- 6 choice_nodes
- 3 end_nodes
- aucun duplicate_id
- aucun missing_next_target

## Runtime Godot

Godot CLI absent localement : validation runtime impossible ici.

À vérifier côté Ludo sur Godot 4.6 : liste affiche Camille + Sarah, Camille reste jouable, Sarah reste désactivée / à venir.
