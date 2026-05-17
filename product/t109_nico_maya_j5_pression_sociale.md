# T109 — Nico/Maya J5 pression sociale MVP

Statut : DONE
Thread : Dialogues

## Livrables

- Source narrative Nico : `narrative/t109_nico_j5_complete.json`
- Copie prototype Nico : `product/godot_t004_prototype/data/nico_j5_complete.json`
- Source narrative Maya : `narrative/t109_maya_j5_complete.json`
- Copie prototype Maya : `product/godot_t004_prototype/data/maya_j5_complete.json`

## Intention narrative

T109 ajoute deux conversations J5 plus courtes pour matérialiser la pression sociale sans ouvrir une nouvelle crise majeure.

- **Nico J5** : couverture fragile / miroir social. Nico peut aider sur un blanc précis, mais refuse de devenir complice ou solutionner la double vie.
- **Maya J5** : témoin social / trace visible. Maya voit une absence et peut relayer une alerte légère, sans devenir détective ni omnisciente.

## Structure

- `n5_block_a` — Nico : couverture fragile / pression sociale
- `m5_block_a` — Maya : trace visible / témoin social léger

## Validation statique attendue

```json
{
  "nico": {
    "schema_version": "0.1",
    "conversation_id": "nico_j5_complete",
    "day": 5,
    "contact_id": "nico",
    "nodes": 33,
    "choice_nodes": 4,
    "end_nodes": 3,
    "block_markers": ["n5_block_a"],
    "source_copy_sha256": "ad3a51adc584128d87c59948f1202205d44904fe95a36aaee19273ecdc060c86"
  },
  "maya": {
    "schema_version": "0.1",
    "conversation_id": "maya_j5_complete",
    "day": 5,
    "contact_id": "maya",
    "nodes": 32,
    "choice_nodes": 4,
    "end_nodes": 3,
    "block_markers": ["m5_block_a"],
    "source_copy_sha256": "ae6828fb1003fc155caa422087a72b1c6e33eb74e06268d2b4b85bcc49d9a784"
  },
  "schema_t003_changed": false
}
```

## Notes

- Aucun script Godot modifié.
- Aucun changement de schéma T003.
- Aucun changement de `conversation_blocks.json`.
- Nico/Maya restent des relais sociaux limités : pas de solution magique, pas de morale plate, pas d’enquête omnisciente.
- J5 non intégré : intégration réservée au ticket Scope dédié après contenus/relecture.

## Next step recommandé

**T110 — Décider Inès J5 : réserve ou micro-bloc**.
