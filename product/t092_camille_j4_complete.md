# T092 — Camille J4 complet intégrable

Statut : DONE
Thread : Dialogues

## Livrables

- Source narrative : `narrative/t092_camille_j4_complete.json`
- Copie prototype : `product/godot_t004_prototype/data/camille_j4_complete.json`

## Intention narrative

Camille J4 pousse la tension vers une disponibilité concrète sans crise finale : une fenêtre de quarante minutes, un lieu banal mais traçable, puis une trace émotionnelle laissée pour J5. Le dialogue évite de répéter le motif café et maintient Camille dans un registre séduisant, trouble et prudent plutôt qu’explicite.

## Structure

- `c4_block_a` — reprise risquée / disponibilité concrète
- `c4_block_b` — proposition plus coûteuse / adresse ou non-adresse
- `c4_block_c` — trace émotionnelle / point de bascule vers J5

## Validation statique

```json
{
  "schema_version": "0.1",
  "conversation_id": "camille_j4_complete",
  "day": 4,
  "contact_id": "camille",
  "nodes": 54,
  "choice_nodes": 6,
  "end_nodes": 3,
  "block_markers": ["c4_block_a", "c4_block_b", "c4_block_c"],
  "source_copy_sha256": "6114ed9aac6de3e2afa0d85e4dffdb39f20c295bfb3ef0022fb67ef6a57f9de3",
  "schema_t003_changed": false
}
```

## Notes

- Aucun script Godot modifié.
- Aucun changement de schéma T003.
- Intégration runtime/blocs J4 réservée à un ticket ultérieur après Maya/Inès/Nico J4 + cohérence J1→J4.

## Next step recommandé

**T093 — Écrire Maya J4 complet intégrable**.
