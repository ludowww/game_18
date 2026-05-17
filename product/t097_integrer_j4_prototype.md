# T097 — Intégrer J4 Godot blocs/unlocks

Statut : DONE
Thread : Scope MVP / technique

## Décision

J4 est intégré statiquement dans le prototype Godot : 4 conversations Jour 4, progression J1→J2→J3→J4, 12 blocs/unlocks J4, validateur T090 étendu à J1→J4.

Rythme intégré :

```txt
C4A → M4A → I4A → N4A → C4B → M4B → I4B → N4B → C4C → M4C → I4C → N4C
```

## Fichiers créés / modifiés

- `product/godot_t004_prototype/scripts/conversation_state.gd`
  - conversations `camille_j4`, `maya_j4`, `ines_j4`, `nico_j4` ajoutées ;
  - chemins `res://data/*_j4_complete.json` ;
  - map `REQUIRED_CONVERSATIONS_BY_DAY` étendue au jour 4 ;
  - `conversation_ids()` étendu ;
  - transition explicite jusqu’à J4 ;
  - `camille_c4a` ajouté comme bloc initial disponible côté config runtime.
- `product/godot_t004_prototype/data/conversation_blocks.json`
  - 12 blocs J4 ajoutés ;
  - ordre/unlocks J4 ajoutés ;
  - `start_node`, `end_nodes`, `unlock_on_done`, `notification_target`, `waiting_text` renseignés.
- `product/godot_t004_prototype/tests/test_t097_j4_integration.py`
  - nouveau test statique J4.
- `product/godot_t004_prototype/tools/validate_dialogues_and_blocks.py`
  - validateur T090 étendu de J1→J3 à J1→J4 ;
  - contacts J4 `maya`, `ines`, `nico` acceptés ;
  - ordre de blocs attendu porté à 30 blocs.
- `product/godot_t004_prototype/tests/test_t090_dialogue_block_validator.py`
  - attente mise à jour : 10 dialogues actifs, 30 blocs.
- `product/godot_t004_prototype/tests/test_t078_j3_integration.py`
  - régression J3 adaptée pour rester valide après ajout J4 : J3 doit rester présent à sa position, sans supposer qu’il est le dernier jour.
- JSON J4 source + copies prototype : correction technique minimale des nodes de fin `*_end_*`, passés de `type: "message"` à `type: "end"` pour respecter T003 et permettre `mark_current_done()` runtime.
  - `narrative/t092_camille_j4_complete.json`
  - `narrative/t093_maya_j4_complete.json`
  - `narrative/t094_ines_j4_complete.json`
  - `narrative/t095_nico_j4_complete.json`
  - `product/godot_t004_prototype/data/camille_j4_complete.json`
  - `product/godot_t004_prototype/data/maya_j4_complete.json`
  - `product/godot_t004_prototype/data/ines_j4_complete.json`
  - `product/godot_t004_prototype/data/nico_j4_complete.json`
- `product/t097_integrer_j4_prototype.md`
- `roadmap_double_vie_discord.txt`
- `discord_blocks/bloc_04.txt`

## Conversations ajoutées

| Runtime ID | Contact | JSON | Jour | Nodes | Choices | End |
|---|---|---|---:|---:|---:|---:|
| `camille_j4` | Camille | `camille_j4_complete.json` | 4 | 54 | 6 | 3 |
| `maya_j4` | Maya | `maya_j4_complete.json` | 4 | 54 | 6 | 3 |
| `ines_j4` | Inès | `ines_j4_complete.json` | 4 | 54 | 6 | 3 |
| `nico_j4` | Nico | `nico_j4_complete.json` | 4 | 54 | 6 | 3 |

## Blocs ajoutés

| Bloc | Conversation | Start | End nodes | Unlock | Notification |
|---|---|---|---|---|---|
| `camille_c4a` | `camille_j4` | `c4_block_a` | `c4_009_a/b/c` | `maya_m4a` | `maya_j4` |
| `maya_m4a` | `maya_j4` | `m4_block_a` | `m4_009_a/b/c` | `ines_i4a` | `ines_j4` |
| `ines_i4a` | `ines_j4` | `i4_block_a` | `i4_009_a/b/c` | `nico_n4a` | `nico_j4` |
| `nico_n4a` | `nico_j4` | `n4_block_a` | `n4_009_a/b/c` | `camille_c4b` | `camille_j4` |
| `camille_c4b` | `camille_j4` | `c4_block_b` | `c4_018_a/b/c` | `maya_m4b` | `maya_j4` |
| `maya_m4b` | `maya_j4` | `m4_block_b` | `m4_018_a/b/c` | `ines_i4b` | `ines_j4` |
| `ines_i4b` | `ines_j4` | `i4_block_b` | `i4_018_a/b/c` | `nico_n4b` | `nico_j4` |
| `nico_n4b` | `nico_j4` | `n4_block_b` | `n4_018_a/b/c` | `camille_c4c` | `camille_j4` |
| `camille_c4c` | `camille_j4` | `c4_block_c` | `c4_end_window/trace/retreat` | `maya_m4c` | `maya_j4` |
| `maya_m4c` | `maya_j4` | `m4_block_c` | `m4_end_gratitude/cover/distance` | `ines_i4c` | `ines_j4` |
| `ines_i4c` | `ines_j4` | `i4_block_c` | `i4_end_open/boundary/complication` | `nico_n4c` | `nico_j4` |
| `nico_n4c` | `nico_j4` | `n4_block_c` | `n4_end_clarify/cloud/silence` | vide | vide |

## Validation

```json
{
  "validator_ok": true,
  "active_dialogues": 10,
  "blocks": 30,
  "errors": 0,
  "warnings": 5,
  "j4_dialogues": {
    "camille_j4_complete": {"nodes": 54, "choices": 6, "end_nodes": 3, "source_copy_match": true},
    "maya_j4_complete": {"nodes": 54, "choices": 6, "end_nodes": 3, "source_copy_match": true},
    "ines_j4_complete": {"nodes": 54, "choices": 6, "end_nodes": 3, "source_copy_match": true},
    "nico_j4_complete": {"nodes": 54, "choices": 6, "end_nodes": 3, "source_copy_match": true}
  },
  "regressions": {
    "test_t097_j4_integration.py": "OK",
    "test_t090_dialogue_block_validator.py": "OK",
    "test_t087_messages_horizontal_overflow.py": "OK",
    "test_t085_archives_jours_passes.py": "OK",
    "test_t083_mode_test_accelere.py": "OK",
    "test_t080_day_transition_button_label.py": "OK",
    "test_t078_j3_integration.py": "OK",
    "test_t072_repair_existing_save_badges.py": "OK",
    "test_t068_externalized_blocks.py": "OK",
    "test_t063_j2_integration.py": "OK",
    "test_t057_narrative_blocks.py": "OK",
    "test_t053_notification_guards.py": "OK"
  },
  "godot_cli": "absent"
}
```

Commande exécutée :

```bash
cd product/godot_t004_prototype
python3 tools/validate_dialogues_and_blocks.py --json
python3 tests/test_t087_messages_horizontal_overflow.py \
  && python3 tests/test_t085_archives_jours_passes.py \
  && python3 tests/test_t083_mode_test_accelere.py \
  && python3 tests/test_t080_day_transition_button_label.py \
  && python3 tests/test_t078_j3_integration.py \
  && python3 tests/test_t072_repair_existing_save_badges.py \
  && python3 tests/test_t068_externalized_blocks.py \
  && python3 tests/test_t063_j2_integration.py \
  && python3 tests/test_t057_narrative_blocks.py \
  && python3 tests/test_t053_notification_guards.py \
  && python3 tests/test_t090_dialogue_block_validator.py \
  && python3 tests/test_t097_j4_integration.py
```

## Notes / limites

- Aucun ajout images, appels, scheduler, temps réel, contacts complets ou UX lourde.
- Schéma T003 préservé ; correction JSON limitée à restaurer les vrais nodes `end` J4.
- Les warnings du validateur restent les placeholders/anciens artefacts non actifs déjà connus depuis T090.
- Godot CLI absent sur VPS : validation runtime à faire côté Ludo.

## Checklist runtime T098 pour Ludo

1. Ouvrir `product/godot_t004_prototype/` dans Godot 4.6.
2. En mode test rapide ON, terminer J3 puis vérifier que le bouton affiche `Passer au Jour 4`.
3. Passer J4 : vérifier que les conversations actives sont Camille, Maya, Inès, Nico.
4. Jouer l’ordre attendu : C4A → M4A → I4A → N4A → C4B → M4B → I4B → N4B → C4C → M4C → I4C → N4C.
5. Vérifier badges/previews entre chaque unlock.
6. Sauvegarder/recharger en milieu de J4 : reprise du bon bloc et archives J1/J2/J3 toujours relisibles.
7. Terminer les 4 conversations J4 : vérifier que la fin de journée ne casse pas l’écran Messages.

## Next step recommandé

**T098 — Playtest runtime J4** côté Godot 4.6.
