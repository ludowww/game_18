# T112 — Intégrer J5 Godot blocs/unlocks

## Statut

Exécuté ✅

## Objectif

Intégrer le Jour 5 dans le prototype Godot en branchant les conversations J5 existantes et la progression de blocs/unlocks correspondante, sans modifier les dialogues JSON ni le schéma T003.

## Conversations J5 intégrées

Ajout runtime dans `product/godot_t004_prototype/scripts/conversation_state.gd` :

- `sarah_j5` → `res://data/sarah_j5_complete.json`
- `camille_j5` → `res://data/camille_j5_complete.json`
- `nico_j5` → `res://data/nico_j5_complete.json`
- `maya_j5` → `res://data/maya_j5_complete.json`

Aucune conversation Inès J5 n’a été ajoutée.

## Blocs J5 intégrés

`product/godot_t004_prototype/data/conversation_blocks.json` passe à 38 blocs actifs, avec 8 blocs J5 ajoutés après J4 :

1. `sarah_s5a` — `sarah_j5`, `s5_block_a` → unlock `camille_c5a`, notification `camille_j5`
2. `camille_c5a` — `camille_j5`, `c5_block_a` → unlock `nico_n5a`, notification `nico_j5`
3. `nico_n5a` — `nico_j5`, `n5_block_a` → unlock `sarah_s5b`, notification `sarah_j5`
4. `sarah_s5b` — `sarah_j5`, `s5_block_b` → unlock `camille_c5b`, notification `camille_j5`
5. `camille_c5b` — `camille_j5`, `c5_block_b` → unlock `maya_m5a`, notification `maya_j5`
6. `maya_m5a` — `maya_j5`, `m5_block_a` → unlock `sarah_s5c`, notification `sarah_j5`
7. `sarah_s5c` — `sarah_j5`, `s5_block_c` → unlock `camille_c5c`, notification `camille_j5`
8. `camille_c5c` — `camille_j5`, `c5_block_c` → fin de chaîne J5 MVP

Ordre validé : `S5A → C5A → N5A → S5B → C5B → M5A → S5C → C5C`.

## Validator / tests

- `tools/validate_dialogues_and_blocks.py` étendu à J1→J5.
- Couverture active : 14 dialogues, 38 blocs.
- Nouveau test statique : `tests/test_t112_j5_integration.py`.
- Tests historiques ajustés pour préserver J1→J4 tout en acceptant l’extension J5.

## Contraintes vérifiées

- JSON dialogues J5 non modifiés.
- Schéma `product/t003_mini_schema_json_godot.md` non modifié.
- Pas de `ines_j5`.
- Pas de `i5_block_a`.
- Archives / jours précédents conservés dans l’ordre de blocs.
- Pas de scheduler, temps réel ou notification OS ajouté.

## Validation

Commandes passées :

```bash
python3 tests/test_t112_j5_integration.py
python3 tests/test_t104_quick_switch_repair_available_live.py
python3 tests/test_t103_quick_switch_live_refresh.py
python3 tests/test_t102_quick_switch_new_message.py
python3 tests/test_t101_typing_bubble_scroll_friendly.py
python3 tests/test_t100_typing_bubble_in_thread.py
python3 tests/test_t099_contact_colors_typing_indicator.py
python3 tests/test_t097_j4_integration.py
python3 tests/test_t090_dialogue_block_validator.py
python3 tests/test_t087_messages_horizontal_overflow.py
python3 tests/test_t085_archives_jours_passes.py
python3 tests/test_t083_mode_test_accelere.py
python3 tests/test_t080_day_transition_button_label.py
python3 tests/test_t078_j3_integration.py
python3 tests/test_t072_repair_existing_save_badges.py
python3 tests/test_t068_externalized_blocks.py
python3 tests/test_t063_j2_integration.py
python3 tests/test_t057_narrative_blocks.py
python3 tests/test_t053_notification_guards.py
python3 tools/validate_dialogues_and_blocks.py --json
```

Résultat : OK.

Validator :

```json
{
  "ok": true,
  "counts": {
    "dialogues": 14,
    "blocks": 38,
    "errors": 0,
    "warnings": 5
  }
}
```

Les 5 warnings sont les placeholders/non-active dialogues déjà non bloquants du validateur.

## Limites

Godot CLI absent sur la machine d’exécution (`godot_cli_absent`) : validation runtime à faire côté Ludo.
