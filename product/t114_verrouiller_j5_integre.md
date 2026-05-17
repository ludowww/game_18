# T114 — Verrouiller J5 intégré

Statut : DONE
Thread : Roadmap / Scope MVP / technique

## Décision Roadmap

La tranche **J5 intégré** est verrouillée côté MVP après validation runtime Ludo : “J5 fonctionne”.

Ce verrou couvre :

- contenu Sarah J5, Camille J5, Nico J5, Maya J5 ;
- décision Inès J5 en réserve ;
- intégration Godot Jour 5 ;
- 8 blocs J5 ;
- validation runtime côté Ludo ;
- non-régression des systèmes J1→J5 : archives, save, blocs, notifications, typing bubble, accès rapide.

## Chaîne validée

- **T106** — Cadrage J5 : coût visible de la double vie.
- **T107** — Sarah J5 complet : poids intime, besoin de présence, doute doux.
- **T108** — Camille J5 complet : risque affectif plus coûteux, vérité partielle, conséquence J6.
- **T109** — Nico/Maya J5 : pression sociale, couverture fragile, trace visible.
- **T110** — Inès J5 en réserve : pas de JSON ni bloc actif.
- **T111** — Relecture cohérence J5 / J1→J5 : J5 prêt pour intégration, aucun patch JSON nécessaire.
- **T112** — Intégration Godot J5 : conversations, day 5, blocs/unlocks, validateur J1→J5.
- **T113** — Playtest runtime J5 : validé côté Ludo.

## Ce qui est verrouillé

### Conversations J5

Conversations intégrées :

- `sarah_j5` → `res://data/sarah_j5_complete.json`
- `camille_j5` → `res://data/camille_j5_complete.json`
- `nico_j5` → `res://data/nico_j5_complete.json`
- `maya_j5` → `res://data/maya_j5_complete.json`

Inès reste en réserve :

- pas de `ines_j5` ;
- pas de `ines_j5_complete.json` ;
- pas de `i5_block_a`.

### Rythme J5

Rythme verrouillé :

```txt
S5A → C5A → N5A → S5B → C5B → M5A → S5C → C5C
```

Blocs verrouillés :

- `sarah_s5a`
- `camille_c5a`
- `nico_n5a`
- `sarah_s5b`
- `camille_c5b`
- `maya_m5a`
- `sarah_s5c`
- `camille_c5c`

## Validation runtime

Validation runtime déclarée côté Ludo :

- **J5 fonctionne** dans Godot local.

Le VPS n’a pas de Godot CLI (`godot_cli_absent`) : la validation runtime locale reste côté Ludo.

## Validation statique à conserver

Garde-fous principaux :

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

Attendu validateur T090 après T112 :

```json
{
  "ok": true,
  "dialogues": 14,
  "blocks": 38,
  "errors": 0,
  "warnings": 5
}
```

Les 5 warnings sont les placeholders/non-active dialogues déjà connus et non bloquants.

## Non-changements

T114 ne modifie pas :

- dialogues JSON ;
- schéma T003 ;
- `conversation_blocks.json` ;
- scripts Godot ;
- save payload ;
- UX ;
- notifications ;
- typing bubble ;
- OS notifications / scheduler / temps réel.

## Limites MVP assumées

- J6 non cadré / non écrit / non intégré.
- Pas de vraie fin ou révélation finale verrouillée.
- Pas d’Inès J5 active.
- Pas d’OS notifications.
- Pas de scheduler / temps réel.
- Pas de médias/images/appels.
- Pas de système contacts complet.

## Next step recommandé

Décision Roadmap avant suite :

1. **T115 — Cadrer J6 / fin MVP** : continuer vers la résolution / point de rupture.
2. **T115 — Polish rythme J1→J5** : relire tempo global, longueur, transitions et charge UX avant contenu final.
3. **T115 — Outillage auteur / regression pack J1→J5** : sécuriser la production avant fin.

Recommandation : **cadrer J6 / fin MVP**, maintenant que J1→J5 sont jouables/intégrés.
