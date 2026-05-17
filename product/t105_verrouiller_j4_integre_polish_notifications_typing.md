# T105 — Verrouiller J4 intégré + polish notifications/typing validé

Statut : DONE
Thread : Roadmap / Scope MVP / technique

## Décision Roadmap

La tranche **J4 intégré + polish notifications/typing** est verrouillée côté MVP après validation runtime Ludo.

Ce verrou couvre :

- intégration J4 dans Godot ;
- conversations J4 actives : Camille, Maya, Inès, Nico ;
- 12 blocs J4 et rythme d’unlocks ;
- bulles typing `...` intégrées au flux scrollable ;
- couleurs distinctes pour Maya/Inès/Nico ;
- toast d’accès rapide `Nouveau message de X · Ouvrir` ;
- correction live du toast sans aller-retour Messages ;
- nettoyage warnings Godot `var name`.

## Chaîne validée

- **T097** — J4 intégré Godot : conversations `camille_j4`, `maya_j4`, `ines_j4`, `nico_j4`, progression Jour 4, 12 blocs J4.
- **T099** — Couleurs contacts + indicateur d’écriture.
- **T100** — Indicateur `...` transformé en bulle typing dans le fil.
- **T101** — Bulle typing plus friendly + intégrée au scroll, validée côté Ludo.
- **T102** — Accès rapide nouvelle conversation.
- **T103** — Première tentative de refresh live, non suffisante en runtime.
- **T104** — Réparation live des notifications de blocs déjà disponibles + warnings Godot corrigés, validé côté Ludo.

## Ce qui est verrouillé

### J4 contenu / conversations

- Camille J4 : `camille_j4_complete.json`.
- Maya J4 : `maya_j4_complete.json`.
- Inès J4 : `ines_j4_complete.json`.
- Nico J4 : `nico_j4_complete.json`.

Chaque conversation J4 reste au schéma T003 plat, intégrée au prototype via `ConversationState`.

### Rythme J4

Rythme verrouillé :

```txt
C4A → M4A → I4A → N4A → C4B → M4B → I4B → N4B → C4C → M4C → I4C → N4C
```

Blocs J4 verrouillés dans `data/conversation_blocks.json` :

- `camille_c4a`, `camille_c4b`, `camille_c4c`
- `maya_m4a`, `maya_m4b`, `maya_m4c`
- `ines_i4a`, `ines_i4b`, `ines_i4c`
- `nico_n4a`, `nico_n4b`, `nico_n4c`

### UX notifications / typing

Verrouillé après corrections runtime :

- bulles typing temporaires dans le flux `message_list` ;
- taille des `...` plus friendly ;
- auto-scroll de la bulle typing dans les conversations longues ;
- disparition de la bulle avant le vrai message ;
- toast in-app discret `Nouveau message de X · Ouvrir` ;
- toast affiché live après fin de bloc sans retour obligatoire par Messages ;
- ouverture rapide vers la conversation cible, avec lecture ciblée uniquement ;
- archives/jours passés exclus des notifications actives ;
- couleurs contacts distinctes pour Camille/Sarah/Maya/Inès/Nico.

## Validation runtime

Validation runtime déclarée côté Ludo :

- T101 validée : bulle typing friendly + scroll OK.
- T104 validée : toast accès rapide live OK après correction du cas bloc disponible sans badge.
- Les warnings Godot `SHADOWED_VARIABLE_BASE_CLASS` liés à `var name` ont été corrigés dans les scripts concernés.

Le VPS n’a pas de Godot CLI (`godot_cli_absent`) : la validation runtime locale reste côté Ludo.

## Validation statique à conserver

Régressions garde-fous :

```bash
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
```

Le validateur T090 doit rester vert sur J1→J4 :

```bash
python3 tools/validate_dialogues_and_blocks.py --json
```

## Non-changements

Ce verrou ne modifie pas :

- dialogues JSON ;
- schéma T003 ;
- `conversation_blocks.json` ;
- save payload ;
- rythme narratif ;
- OS notifications ;
- temps réel / scheduler ;
- médias/images/appels.

## Limites MVP assumées

- Pas de J5 cadré/écrit/intégré.
- Pas d’OS notifications.
- Pas de scheduler / temps réel.
- Pas de vraie file multi-notifications complexe : accès rapide MVP vers une conversation pertinente.
- Pas de système contacts complet.
- Pas de média/images.

## Next step recommandé

Décision Roadmap avant expansion :

1. **T106 — Cadrer J5** si l’objectif est de continuer la progression narrative.
2. **T106 — Polish rythme J1→J4** si l’objectif est de lisser tempo, notifications et transitions avant plus de contenu.
3. **T106 — Outillage auteur J5/blocs** si l’objectif est de sécuriser la production de jours supplémentaires.

Recommandation : **cadrer J5** maintenant que J4 + notifications/typing sont validés, sauf si Ludo veut d’abord une passe confort globale J1→J4.
