# T045 — Notifications dynamiques simples

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Objectif

Faire apparaître de nouveaux messages/badges entre conversations de manière simple, sans temps réel complexe.

## Décision MVP

Déclenchement **hardcodé léger côté Godot**.

Raison :

- ne pas modifier le JSON T003 ;
- ne pas créer de scheduler ;
- tester rapidement le gain gameplay : une conversation se réveille après progression dans une autre.

On décidera plus tard si ces déclencheurs doivent devenir des `effects.flags` ou un format dédié.

## Implémentation

Fichiers modifiés :

- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/scripts/conversation_screen.gd`

Ajout principal :

```gdscript
func handle_dynamic_notification(source_conversation_id: String, node_id: String) -> void:
```

Appelé depuis `conversation_screen.gd` après affichage d’un node :

```gdscript
ConversationState.handle_dynamic_notification(current_contact_id, node_id)
```

## Déclencheurs T045

### Camille → Sarah

- Après `c1_010` :
  - Sarah reçoit `has_new = true`
  - preview : `Tu sais déjà si tu rentres pour manger ?`

- Après `c1_020` :
  - Sarah reçoit `has_new = true`
  - preview : `Tu es encore dehors ?`

### Sarah → Camille

- Après `s1_006` :
  - Camille reçoit `has_new = true`
  - preview : `Tu réponds quand tu peux ?`

- Après `s1_020` :
  - Camille reçoit `has_new = true`
  - preview : `Je crois que j’ai pensé à toi au mauvais moment.`

## Anti-doublon

Ajout d’un état runtime sauvegardé :

```gdscript
dynamic_notifications_fired
```

Chaque événement est identifié par :

```gdscript
source_conversation_id + ":" + node_id
```

Un événement déjà déclenché ne se redéclenche pas après retour liste, sauvegarde ou relance.

## Persistance

Les notifications dynamiques utilisent `mark_conversation_new()`, donc elles conservent :

- `has_new` ;
- `last_preview` ;
- sauvegarde dans `user://double_vie_save.json` ;
- restauration après relance.

Le reset T043 remet aussi `dynamic_notifications_fired` à zéro.

## Hors-scope confirmé

- pas de notification OS ;
- pas de temps réel ;
- pas de scheduler ;
- pas de compte joueur ;
- pas de cloud ;
- pas de modification JSON T003 ;
- JSON T003 inchangé ;
- pas de format d’événement narratif dans le JSON pour l’instant.

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
- sha256 : `33512a06b873d4b95638ed1ba07f08ca302d28671a564785ebac9e137d59dd1f`

## Marqueurs code vérifiés

- `func handle_dynamic_notification`
- triggers `c1_010`, `c1_020`, `s1_006`, `s1_020`
- `mark_conversation_new(target_id, preview)`
- `dynamic_notifications_fired`
- appel depuis `conversation_screen.gd`
- sauvegarde locale T043 conservée

## Limite runtime

Godot CLI absent dans l’environnement local : validation runtime à faire côté Ludo sur Godot 4.6.

Checklist T046 proposée :

1. reset progression ;
2. avancer Camille jusqu’à `c1_010` ;
3. revenir Messages ;
4. vérifier badge Sarah + preview ;
5. ouvrir Sarah puis revenir ;
6. avancer Sarah jusqu’à `s1_006` ;
7. revenir Messages ;
8. vérifier badge Camille + preview ;
9. quitter / relancer ;
10. vérifier que badge/preview/anti-doublon persistent.
