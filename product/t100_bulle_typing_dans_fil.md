# T100 — Bulle typing dans le fil

Statut : DONE
Thread : Scope MVP / technique

## Décision

L’indicateur d’écriture n’est plus un label séparé sous le fil : il devient une bulle temporaire intégrée à `message_list`, alignée côté contact, avec animation légère des points.

## Fichiers créés / modifiés

- `product/godot_t004_prototype/scripts/conversation_screen.gd`
  - suppression de l’élément UI séparé `typing_container` ajouté en T099 ;
  - ajout d’une bulle temporaire via `_add_typing_bubble()` ;
  - suppression propre via `_remove_typing_bubble()` avant l’arrivée du vrai message ;
  - style aligné côté contact : même couleur que le contact courant, bulle à gauche, rayon façon bulle contact ;
  - animation `.` / `..` / `...` + alpha léger, timing inchangé.
- `product/godot_t004_prototype/tests/test_t100_typing_bubble_in_thread.py`
  - nouveau test statique T100.
- `product/godot_t004_prototype/tests/test_t099_contact_colors_typing_indicator.py`
  - régression T099 adaptée : elle vérifie désormais que le typing reste animé et dans le flux, sans imposer l’ancien conteneur séparé.
- `product/t100_bulle_typing_dans_fil.md`
  - présent artefact produit.
- `roadmap_double_vie_discord.txt`
- `discord_blocks/bloc_04.txt`

## Comportement attendu

Quand un message contact a un délai :

1. `_show_typing_indicator(sender)` crée une bulle temporaire dans `message_list`.
2. La bulle est alignée à gauche, comme un message contact.
3. Le contenu anime les points : `.`, `..`, `...`.
4. `_hide_typing_indicator()` appelle `_remove_typing_bubble()` avant l’ajout du vrai message.
5. Le vrai message arrive ensuite comme bulle normale.

## Non-changements

- Aucun JSON dialogue modifié.
- Aucun changement du schéma T003.
- Aucun changement de `conversation_blocks.json`.
- Aucun changement de save/payload.
- Aucun changement de délais narratifs ou mode test rapide.
- Aucun ajout d’accès rapide vers conversation nouvellement déverrouillée ; ce backlog devient **T101** si Roadmap le priorise.

## Validation

```json
{
  "t100": "OK",
  "validator_ok": true,
  "active_dialogues": 10,
  "blocks": 30,
  "json_and_blocks_unchanged": true,
  "regressions": {
    "test_t100_typing_bubble_in_thread.py": "OK",
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
python3 tests/test_t100_typing_bubble_in_thread.py \
  && python3 tests/test_t099_contact_colors_typing_indicator.py \
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

Godot CLI absent sur VPS : validation runtime à faire côté Ludo dans Godot 4.6.

Checklist runtime :
1. Ouvrir une conversation avec délai contact.
2. Vérifier que les `...` apparaissent comme une bulle contact à gauche dans le fil.
3. Vérifier que la bulle disparaît avant l’arrivée du message réel.
4. Vérifier que l’animation est lisible mais discrète.
5. Tester sur Camille/Maya/Inès/Nico pour confirmer couleur contact.

## Next step recommandé

Reprise playtest **T098/T100** côté Godot. Backlog possible ensuite : **T101 — Accès rapide à une conversation avec nouveau message**.
