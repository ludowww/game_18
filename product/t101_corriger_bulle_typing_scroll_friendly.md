# T101 — Corriger bulle typing : taille friendly + intégration scroll

Statut : DONE

## Décision

Correction UI-only du bug remonté après T100 : la bulle `...` est traitée comme un message temporaire du flux scrollable, avec auto-scroll après layout, puis suppression avant le vrai message. Le réglage visuel est rendu plus friendly : `...` plus grands, bulle légèrement plus lisible, toujours discrète.

## Fichiers créés / modifiés

- `product/godot_t004_prototype/scripts/conversation_screen.gd`
  - `_wait_before_node()` attend maintenant `_show_typing_indicator(sender)` pour laisser la bulle être insérée/scrollee avant le délai d’écriture ;
  - `_add_typing_bubble()` ajoute toujours `typing_row` dans `message_list`, attend une frame (`await get_tree().process_frame`) puis appelle `_ensure_last_message_visible()` ;
  - `_remove_typing_bubble()` retire `typing_row` de `message_list` et le `queue_free()` avant l’arrivée du vrai message ;
  - style friendly : bulle `Vector2(96, 44)`, bordure discrète, marges élargies, `font_size = 24`, alignement vertical centré.
- `product/godot_t004_prototype/tests/test_t101_typing_bubble_scroll_friendly.py`
  - nouveau test statique T101 : intégration dans `message_list`, scroll après frame layout, suppression avant vrai message, réglage friendly, hashes JSON/config inchangés.
- `product/godot_t004_prototype/tests/test_t100_typing_bubble_in_thread.py`
  - adaptation mineure de la régression T100 pour accepter la couleur contact légèrement éclaircie de T101.
- `product/t101_corriger_bulle_typing_scroll_friendly.md`
  - présent artefact produit.
- `roadmap_double_vie_discord.txt`
- `discord_blocks/bloc_04.txt`

## Validation

```json
{
  "t101_typing_bubble_scroll_friendly": "OK",
  "regressions": {
    "T100": "OK",
    "T099": "OK",
    "T097": "OK",
    "T090": "OK",
    "T087": "OK",
    "T085": "OK",
    "T083": "OK",
    "T080": "OK",
    "T078": "OK",
    "T072": "OK",
    "T068": "OK",
    "T063": "OK",
    "T057": "OK",
    "T053": "OK"
  },
  "json_dialogues_unchanged": true,
  "conversation_blocks_unchanged": true,
  "save_payload_unchanged": true,
  "t003_schema_unchanged": true,
  "godot_cli": "absent"
}
```

Commandes lancées depuis `product/godot_t004_prototype/` :

```bash
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

## Notes / limites

- Aucun dialogue JSON modifié.
- Aucun changement T003.
- Aucun changement `conversation_blocks.json`.
- Aucun changement save/payload.
- Aucun changement de rythme narratif/delays : seule l’insertion/scroll de la bulle typing et son style changent.
- Runtime Godot non exécuté localement : CLI Godot absent sur VPS.

## Checklist runtime Ludo

1. Ouvrir une conversation avec message contact retardé.
2. Vérifier que `...` apparaît comme une petite bulle dans le fil scrollable, sous les messages déjà visibles.
3. Vérifier que le scroll descend quand la bulle apparaît.
4. Vérifier que la bulle disparaît avant le vrai message.
5. Vérifier que les points sont lisibles/friendly sans prendre trop de place.
