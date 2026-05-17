# T057 — Implémenter verrous narratifs de blocs J1

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Appliquer la segmentation T056 dans le prototype, sans réécrire les dialogues J1 et sans créer de contenu J2.

## Implémentation

### Table hardcodée MVP côté Godot

Comme prévu par le point de vigilance, le JSON T003 n’est pas modifié. Les frontières de blocs sont définies côté Godot dans `ConversationState` via une table hardcodée MVP :

- `camille_c1a` → C1A ;
- `camille_c1b` → C1B ;
- `camille_c1c` → C1C ;
- `sarah_s1a` → S1A ;
- `sarah_s1b` → S1B ;
- `sarah_s1c` → S1C.

Statuts runtime :

- `locked` ;
- `available` ;
- `active` ;
- `done`.

### Bloc initial

Au reset / nouvelle partie :

```text
camille_c1a = available
sarah_s1a / autres blocs = locked
```

Sarah ne commence donc plus avec un badge initial décoratif : elle devient pertinente après le premier verrou Camille.

## Frontières de blocs J1

### Camille

- C1A : `c1_001` → `c1_009_pause`
  - puis lock Camille ;
  - unlock Sarah S1A ;
  - notification Sarah.
- C1B : `c1_010` → `c1_018_wait`
  - puis lock Camille ;
  - unlock Sarah S1B ;
  - notification Sarah.
- C1C : `c1_019` → fins `c1_end_go` / `c1_end_resist` / `c1_end_seen`
  - Camille J1 done ;
  - unlock Sarah S1C.

### Sarah

- S1A : `s1_001` → `s1_010`
  - puis lock Sarah ;
  - unlock Camille C1B ;
  - notification Camille.
- S1B : `s1_011` → `s1_019_a` / `s1_019_b` / `s1_019_c`
  - puis lock Sarah ;
  - unlock Camille C1C ;
  - notification Camille.
- S1C : `s1_020` → fins `s1_end_deny` / `s1_end_delay` / `s1_end_confess_hint`
  - Sarah J1 done.

## Comportement runtime

Quand le joueur atteint la fin d’un bloc :

1. le prochain node est gardé en `next_node` ;
2. le bloc courant passe `done` ;
3. le bloc suivant prévu est `available` ;
4. la conversation courante affiche un état d’attente ;
5. l’autre conversation reçoit une notification seulement si un vrai bloc est débloqué.

États d’attente affichés :

- `Plus rien pour le moment` ;
- `Camille ne répond plus pour l’instant` ;
- `Sarah ne répond plus pour l’instant`.

## Notifications

Les notifications dynamiques ne servent plus seulement de décor.

Elles sont maintenant liées à un bloc réellement disponible :

```text
notification = bloc unlocké + conversation pertinente à ouvrir maintenant
```

La garde T053 est conservée :

- pas de notification si cible `done` ;
- pas de notification J1 si `current_day > 1` ;
- pas de notification si cible indisponible ;
- pas de notification si cible déjà ouverte ;
- anti-doublon `dynamic_notifications_fired` conservé.

## Sauvegarde

La sauvegarde passe à `SAVE_VERSION = 3` et ajoute :

```json
{
  "conversation_blocks": {
    "camille_c1a": { "status": "done" },
    "sarah_s1a": { "status": "available" }
  }
}
```

Compatibilité anciennes saves :

- si `conversation_blocks` est absent, une migration légère initialise les blocs ;
- si Camille / Sarah sont déjà `done`, leurs blocs J1 sont marqués `done` ;
- les champs existants restent conservés : messages, choices, previews, `has_new`, `current_day`, `completed_days`, `dynamic_notifications_fired`.

## Fichiers modifiés

- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/scripts/conversation_screen.gd`
- `product/godot_t004_prototype/tests/test_t057_narrative_blocks.py`

## Non-changements

- Aucun JSON T003 modifié.
- Aucun dialogue J1 réécrit.
- Aucun contenu J2 ajouté.
- Aucun scheduler.
- Aucune horloge réelle.
- Aucun calendrier complexe.

## Tests / validation statique

Tests ajoutés / exécutés :

```bash
python3 tests/test_t057_narrative_blocks.py
python3 tests/test_t053_notification_guards.py
```

Résultat : OK.

Validation JSON :

- Camille J1 : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.

Godot CLI absent ici : runtime à valider côté Ludo sur Godot 4.6.

## Checklist runtime recommandée

1. Reset.
2. Vérifier que Camille démarre, Sarah n’a pas encore de vraie relance utile.
3. Jouer Camille jusqu’à `c1_009_pause`.
4. Vérifier : Camille affiche attente, Sarah reçoit une notification.
5. Jouer Sarah jusqu’à `s1_010`.
6. Vérifier : Sarah affiche attente, Camille reçoit une notification.
7. Continuer alternance C1B → S1B → C1C → S1C.
8. Vérifier que le passage J2 n’apparaît qu’après Camille J1 done + Sarah J1 done.
9. Quitter / relancer : vérifier que les statuts de blocs persistent.
