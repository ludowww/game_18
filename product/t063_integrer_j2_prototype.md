# T063 — Intégrer J2 dans le prototype

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Brancher **Camille J2** + **Sarah J2** dans le socle Jours / blocs existant, sans modifier les dialogues ni le schéma JSON T003.

## Intégration réalisée

### Conversations J2 branchées

Les entrées J2 existantes du prototype pointent maintenant vers les fichiers complets :

- `camille_j2` → `res://data/camille_j2_complete.json`
- `sarah_j2` → `res://data/sarah_j2_complete.json`

Titres :

- `Jour 2 — conversation complète MVP`

Les conversations J2 sont disponibles quand `current_day = 2`.

### J1 reste visible

Les conversations J1 restent présentes dans la liste Messages comme historique :

- Camille J1 ;
- Sarah J1.

Aucun reset / masquage de J1 n’est appliqué.

## Blocs runtime J2 ajoutés

### Camille J2

- `camille_c2a` — C2A : reprise après 23:42
  - start : `c2_block_a`
  - fin de bloc : `c2_009_a` / `c2_009_b` / `c2_009_c`
  - unlock : `sarah_s2a`
- `camille_c2b` — C2B : proposition ambiguë
  - start : `c2_block_b`
  - fin de bloc : `c2_020_a` / `c2_020_b` / `c2_020_c`
  - unlock : `sarah_s2b`
- `camille_c2c` — C2C : point de bascule J2
  - start : `c2_block_c`
  - fin : `c2_end_boundary` / `c2_end_stay` / `c2_end_thread`
  - unlock : `sarah_s2c`

### Sarah J2

- `sarah_s2a` — S2A : matin après malaise
  - start : `s2_block_a`
  - fin de bloc : `s2_009_a` / `s2_009_b` / `s2_009_c`
  - unlock : `camille_c2b`
- `sarah_s2b` — S2B : demande de présence
  - start : `s2_block_b`
  - fin de bloc : `s2_019_a` / `s2_019_b` / `s2_019_c`
  - unlock : `camille_c2c`
- `sarah_s2c` — S2C : doute formulé doucement
  - start : `s2_block_c`
  - fin : `s2_end_presence` / `s2_end_fragile` / `s2_end_distance`
  - unlock : aucun, fin Sarah J2

## Rythme J2 intégré

Rythme T060 appliqué côté runtime :

```text
C2A → S2A → C2B → S2B → C2C → S2C
```

Comme pour J1 :

- fin de bloc = attente claire ;
- bloc suivant débloqué ;
- notification seulement si un bloc est réellement disponible.

## Notifications liées aux blocs J2

Les notifications J2 passent par le même mécanisme que J1 :

```text
unlock bloc → mark_conversation_new(target)
```

Previews neutres conservées :

- `Nouveau message de Camille`
- `Nouveau message de Sarah`

Les gardes T053 restent en place :

- pas de notification si cible done ;
- pas de notification si cible indisponible ;
- pas de notification si cible déjà ouverte ;
- notification uniquement si un bloc est ouvrable.

## Sauvegarde

La sauvegarde passe à `SAVE_VERSION = 4`.

`conversation_blocks` conserve maintenant les blocs J1 + J2 :

```json
{
  "conversation_blocks": {
    "camille_c2a": { "status": "available" },
    "sarah_s2a": { "status": "locked" }
  }
}
```

Compatibilité :

- anciennes saves sans blocs J2 gardent leurs données ;
- les nouveaux blocs J2 sont créés par défaut ;
- `current_day`, `completed_days`, messages, choix, previews, badges et `dynamic_notifications_fired` restent conservés.

## Fichiers modifiés

- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/tests/test_t063_j2_integration.py`

## Non-changements

- Aucun changement JSON T003.
- Aucun dialogue modifié.
- Aucun contenu J2 réécrit.
- Aucun scheduler.
- Aucune horloge réelle.
- Aucun nouveau système complexe.

## Validation statique

Tests exécutés :

```bash
python3 tests/test_t063_j2_integration.py
python3 tests/test_t057_narrative_blocks.py
python3 tests/test_t053_notification_guards.py
```

Résultat : OK.

JSON validés :

- Camille J1 : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Camille J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.

Copies J2 source/prototype : hash identique pour Camille et Sarah.

Godot CLI absent ici : runtime à valider côté Ludo sur Godot 4.6.

## Checklist runtime recommandée

1. Terminer J1 et passer à `current_day = 2`.
2. Vérifier que Camille J2 et Sarah J2 apparaissent dans Messages.
3. Ouvrir Camille J2 : C2A doit démarrer.
4. Fin C2A : Camille attend, Sarah J2 reçoit une notification.
5. Jouer S2A → C2B → S2B → C2C → S2C.
6. Quitter / relancer : vérifier que `conversation_blocks` J2 persiste.
