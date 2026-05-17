# T099 — Corriger lisibilité J4 : couleurs contacts + indicateur d’écriture

Statut : DONE
Thread : Scope MVP / technique

## Décision

Correction UX runtime ciblée après playtest J4 : les nouveaux contacts J4 ont désormais des couleurs distinctes, et l’indicateur d’écriture est replacé juste sous le flux de conversation avec une animation légère de points/alpha.

## Fichiers créés / modifiés

- `product/godot_t004_prototype/scripts/conversation_screen.gd`
  - couleurs distinctes ajoutées : Maya, Inès, Nico ;
  - helper `_contact_color(contact_id)` étendu ;
  - bulles, choix, header et indicateur d’écriture utilisent la couleur du contact courant ;
  - indicateur d’écriture replacé entre le flux messages et le panneau de réponses ;
  - animation légère par points `.` / `..` / `...` + variation alpha.
- `product/godot_t004_prototype/scripts/conversation_list.gd`
  - couleurs contacts centralisées côté liste Messages ;
  - cartes, accents et bordures différencient Maya / Inès / Nico.
- `product/godot_t004_prototype/tests/test_t099_contact_colors_typing_indicator.py`
  - nouveau test statique T099.
- `product/t099_couleurs_contacts_indicateur_ecriture.md`
  - présent artefact produit.
- `roadmap_double_vie_discord.txt`
- `discord_blocks/bloc_04.txt`

## Palette MVP

| Contact | Couleur | Intention |
|---|---|---|
| Camille | `#46345f` | violet / risque affectif |
| Sarah | `#a96d2a` | amber-caramel / domestique |
| Maya | `#2f6f73` | bleu-vert social / observation |
| Inès | `#7b3f67` | magenta discret / perturbation ambiguë |
| Nico | `#426c2f` | vert sourd / confident-cover |

## Indicateur d’écriture

Avant : label statique `Personnage écrit…`, peu vivant.

Après :
- conteneur dédié `typing_container` juste après le `ScrollContainer` des messages et avant les choix ;
- texte `Nom écrit.` / `Nom écrit..` / `Nom écrit...` ;
- boucle légère `_animate_typing_indicator()` avec `0.32s` entre états ;
- variation alpha subtile ;
- couleur alignée sur le contact actif.

## Non-changements

- Aucun dialogue JSON modifié.
- Aucun changement du schéma T003.
- Aucun changement de `conversation_blocks.json`.
- Aucun changement de save/payload.
- Aucun changement de delays narratifs ou de rythme de lecture.
- Pas d’accès rapide aux conversations avec nouveau message dans T099 : sujet réservé pour T100.

## Validation

```json
{
  "t099": "OK",
  "validator_ok": true,
  "active_dialogues": 10,
  "blocks": 30,
  "json_and_blocks_unchanged": true,
  "regressions": {
    "test_t099_contact_colors_typing_indicator.py": "OK",
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
python3 tests/test_t099_contact_colors_typing_indicator.py \
  && python3 tests/test_t097_j4_integration.py \
  && python3 tests/test_t090_dialogue_block_validator.py \
  && python3 tests/test_t087_messages_horizontal_overflow.py \
  && python3 tests/test_t085_archives_jours_passes.py \
  && python3 tests/test_t083_mode_test_accelere.py \
  && python3 tests/test_t080_day_transition_button_label.py \
  && python3 tests/test_t078_j3_integration.py \
  && python3 tests/test_t072_repair_existing_save_badges.py \
  && python3 tests/test_t068_externalized_blocks.py \
  && python3 tests/test_t063_j2_integration.py \
  && python3 tests/test_t057_narrative_blocks.py \
  && python3 tests/test_t053_notification_guards.py
```

## Limites / runtime

Godot CLI absent sur VPS : validation runtime à reprendre côté Ludo dans Godot 4.6.

Checklist runtime rapide :
1. Ouvrir J4 en mode test rapide.
2. Vérifier cartes Messages : Maya, Inès, Nico ont trois accents distincts.
3. Ouvrir chaque conversation J4 : header, bulles et choix utilisent la bonne couleur.
4. Observer un délai de réponse contact : indicateur visible juste sous le flux, animé, puis masqué à l’arrivée du message.
5. Vérifier que le rythme/delays ne semble pas accéléré ou ralenti hors mode test.

## Backlog recommandé

**T100 — Accès rapide à une conversation avec nouveau message** : permettre de basculer vers la conversation nouvellement déverrouillée sans repasser systématiquement par Messages, sans perturber la structure actuelle.

## Next step recommandé

**T098 reprise playtest après correctif T099**, puis décision Roadmap sur **T100 — Accès rapide nouvelle conversation**.
