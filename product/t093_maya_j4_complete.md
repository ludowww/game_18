# T093 — Maya J4 complet intégrable

Statut : DONE
Thread : Dialogues

## Livrables

- Source narrative : `narrative/t093_maya_j4_complete.json`
- Copie prototype : `product/godot_t004_prototype/data/maya_j4_complete.json`

## Intention narrative

Maya J4 transforme la double vie en pression sociale légère : absences visibles, micro-contradictions, couverture fragile. Elle n’enquête pas et ne remplace pas Sarah dans le soupçon intime ; elle observe, pique, protège un peu, puis pose une limite.

## Structure

- `m4_block_a` — regard social / remarque légère
- `m4_block_b` — pression par observation / micro-trace
- `m4_block_c` — couverture fragile / dette sociale

## Validation statique

```json
{
  "schema_version": "0.1",
  "conversation_id": "maya_j4_complete",
  "day": 4,
  "contact_id": "maya",
  "nodes": 54,
  "choice_nodes": 6,
  "end_nodes": 3,
  "block_markers": ["m4_block_a", "m4_block_b", "m4_block_c"],
  "source_copy_sha256": "5edfdabb5f79042bd600ea555d09cd2dd44e891406d472b924b092db3e629293",
  "schema_t003_changed": false
}
```

## Notes

- Aucun script Godot modifié.
- Aucun changement de schéma T003.
- Maya reste miroir social / couverture fragile, pas enquêtrice omnisciente.
- Intégration runtime/blocs J4 réservée à T097 après Inès/Nico et relecture cohérence.

## Next step recommandé

**T094 — Écrire Inès J4 complet intégrable**.
