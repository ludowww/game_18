# T078 — Intégrer J3 au prototype via `conversation_blocks.json`

Statut : DONE

## Objectif

Intégrer les conversations J3 déjà produites (`camille_j3_complete.json`, `sarah_j3_complete.json`) dans le prototype Godot sans modifier le schéma T003 ni réécrire les dialogues.

## Modifications réalisées

- Ajout des conversations runtime :
  - `camille_j3` → `res://data/camille_j3_complete.json`
  - `sarah_j3` → `res://data/sarah_j3_complete.json`
- Extension de `REQUIRED_CONVERSATIONS_BY_DAY` avec le Jour 3.
- Extension de `conversation_ids()` pour inclure J3.
- Adaptation de la progression J1 → J2 → J3.
- Ajout des blocs J3 dans `data/conversation_blocks.json` :
  - `camille_c3a`
  - `sarah_s3a`
  - `camille_c3b`
  - `sarah_s3b`
  - `camille_c3c`
  - `sarah_s3c`
- Rythme configuré : `C3A → S3A → C3B → S3B → C3C → S3C`.
- Ajout du test statique `tests/test_t078_j3_integration.py`.

## Fichiers modifiés / créés

- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/data/conversation_blocks.json`
- `product/godot_t004_prototype/tests/test_t078_j3_integration.py`
- `product/t078_integrer_j3_prototype.md`

## Validation statique dialogues

| Fichier | Jour | Contact | Nodes | Choix | Fins | Duplicates | Liens cassés | SHA-256 |
|---|---:|---|---:|---:|---:|---:|---:|---|
| `camille_j1_complete.json` | 1 | Camille | 45 | 6 | 3 | 0 | 0 | `fba4627bd236` |
| `sarah_j1_complete.json` | 1 | Sarah | 41 | 5 | 3 | 0 | 0 | `33512a06b873` |
| `camille_j2_complete.json` | 2 | Camille | 45 | 5 | 3 | 0 | 0 | `c9e0993c7ed5` |
| `sarah_j2_complete.json` | 2 | Sarah | 45 | 5 | 3 | 0 | 0 | `f19e87f45c0c` |
| `camille_j3_complete.json` | 3 | Camille | 46 | 5 | 3 | 0 | 0 | `ae009e1bb743` |
| `sarah_j3_complete.json` | 3 | Sarah | 44 | 5 | 3 | 0 | 0 | `6c0992a9ac09` |

## Validation blocs

- `conversation_blocks.json` : 18 entrées dans `block_order`, 18 définitions dans `blocks`.
- J3 ajouté sans toucher aux dialogues : `camille_c3a`, `sarah_s3a`, `camille_c3b`, `sarah_s3b`, `camille_c3c`, `sarah_s3c`.
- Les `start_node` / `end_nodes` J3 pointent vers des IDs existants dans les JSON J3.
- Les unlocks J3 pointent vers des blocs existants.
- Les notifications restent des previews neutres via le pipeline existant.

## Tests exécutés

Depuis `product/godot_t004_prototype/` :

```bash
python3 tests/test_t078_j3_integration.py \
  && python3 tests/test_t072_repair_existing_save_badges.py \
  && python3 tests/test_t068_externalized_blocks.py \
  && python3 tests/test_t063_j2_integration.py \
  && python3 tests/test_t057_narrative_blocks.py \
  && python3 tests/test_t053_notification_guards.py
```

Résultat : OK.

## Limites connues

- Validation runtime Godot non faite localement : le CLI Godot n’est pas disponible sur ce VPS.
- Le test final doit être fait côté Ludo dans Godot 4.6.
- Aucun système complexe ajouté : pas de scheduler temps réel, pas de notifications OS, pas de contacts complets, pas de migration du schéma T003.
- `SAVE_VERSION` reste compatible : les nouveaux blocs/conversations sont ajoutés par défaut sans casser les anciennes sauvegardes.

## Next step recommandé

**T079 — Playtest runtime J3 : progression J2→J3, alternance C3/S3, badges/previews, sauvegarde/reload.**
