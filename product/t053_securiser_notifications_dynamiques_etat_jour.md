# T053 — Sécuriser notifications dynamiques selon état conversation/jour

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Empêcher les notifications fantômes quand une conversation cible n’a plus rien de pertinent à ouvrir maintenant.

Règle MVP retenue :

> Une notification dynamique doit seulement dire : il y a vraiment quelque chose de pertinent à ouvrir maintenant.

## Implémentation

### Garde centralisé

Ajout d’un helper dans `ConversationState` :

```gdscript
func _can_emit_dynamic_notification(target_id: String) -> bool:
```

La notification dynamique est maintenant bloquée si :

- `current_day > 1` pour les triggers J1 actuels ;
- la cible est la conversation déjà ouverte ;
- la cible n’existe pas ;
- la cible n’est pas disponible ;
- la cible est déjà `done`.

### Ordre sécurisé

Avant T053, le flux était :

```text
trouver target → append dynamic_notifications_fired → mark_conversation_new
```

Après T053 :

```text
trouver target → vérifier pertinence → append dynamic_notifications_fired → mark_conversation_new
```

Donc un événement non pertinent ne pose pas de badge et n’est pas enregistré comme notification émise.

## Conservé

- `dynamic_notifications_fired` conservé ;
- sauvegarde conservée ;
- previews neutres conservées :
  - `Nouveau message de Sarah` ;
  - `Nouveau message de Camille` ;
- triggers T045 conservés ;
- `has_new` conservé ;
- badges Messages conservés.

## Non-changements

- Aucun JSON modifié.
- Aucun scheduler complexe.
- Aucune notification OS.
- Aucun calendrier complexe.
- Aucun contenu J2 ajouté.

## Tests / validation

Test statique ajouté :

- `product/godot_t004_prototype/tests/test_t053_notification_guards.py`

Validation :

```bash
python3 tests/test_t053_notification_guards.py
```

Résultat : OK.

Validation JSON :

- Camille J1 : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.

Godot CLI absent ici : runtime à valider côté Ludo.

## Checklist runtime recommandée

1. Sur J1, déclencher un événement dynamique vers une conversation encore ouverte/pertinente : badge attendu.
2. Terminer Sarah J1, puis déclencher un ancien trigger Camille → Sarah : aucun badge Sarah attendu.
3. Passer à J2, puis rejouer/rouvrir un état qui traite un node J1 trigger : aucun badge J1 attendu.
4. Vérifier que les previews restent neutres si une vraie notification est posée.
5. Quitter / relancer : vérifier que sauvegarde et anti-doublon restent stables.
