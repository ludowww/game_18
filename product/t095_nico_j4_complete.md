# T095 — Nico J4 complet intégrable

Statut : DONE
Thread : Dialogues

## Livrables

- Source narrative : `narrative/t095_nico_j4_complete.json`
- Copie prototype : `product/godot_t004_prototype/data/nico_j4_complete.json`

## Intention narrative

Nico J4 matérialise le risque de parler : il chambre, couvre un peu, avertit sans devenir moralisateur. Le dialogue transforme la couverture amicale en dette sociale fragile et prépare J5 par des flags de silence, couverture, malaise ou clarification.

## Structure

- `n4_block_a` — confident ou couverture
- `n4_block_b` — conseil / provocation / avertissement
- `n4_block_c` — clôture sociale / dette de couverture

## Validation statique

```json
{
  "schema_version": "0.1",
  "conversation_id": "nico_j4_complete",
  "day": 4,
  "contact_id": "nico",
  "nodes": 54,
  "choice_nodes": 6,
  "end_nodes": 3,
  "block_markers": ["n4_block_a", "n4_block_b", "n4_block_c"],
  "source_copy_sha256": "cd0e0fdfe961bd6a0a5df74828e16d97769c355d1e729431e8e85d46bf6dd858",
  "schema_t003_changed": false
}
```

## Notes

- Aucun script Godot modifié.
- Aucun changement de schéma T003.
- Nico reste confident/miroir/couverture fragile, pas tutoriel ni donneur de leçon.
- Intégration runtime/blocs J4 réservée à T097 après relecture cohérence T096.

## Next step recommandé

**T096 — Relecture cohérence J4 / J1→J4**.
