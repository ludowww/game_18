# T108 — Camille J5 complet intégrable

Statut : DONE
Thread : Dialogues

## Livrables

- Source narrative : `narrative/t108_camille_j5_complete.json`
- Copie prototype : `product/godot_t004_prototype/data/camille_j5_complete.json`

## Intention narrative

Camille J5 transforme la tension J4 en coût affectif visible : elle ne formule pas d’ultimatum brutal, mais demande au joueur une preuve de disponibilité, de courage ou de vérité partielle. Sarah reste présente en creux par les effets et les formulations : répondre à Camille coûte ailleurs.

## Structure

- `c5_block_a` — risque affectif plus coûteux
- `c5_block_b` — preuve de courage / vérité partielle
- `c5_block_c` — dette affective / conséquence J6

## Validation statique

```json
{
  "schema_version": "0.1",
  "conversation_id": "camille_j5_complete",
  "day": 5,
  "contact_id": "camille",
  "nodes": 54,
  "choice_nodes": 6,
  "end_nodes": 3,
  "block_markers": ["c5_block_a", "c5_block_b", "c5_block_c"],
  "source_copy_sha256": "de7b0e0dbd0e1a1b71c64f5b9a04811cc45888e5d1cfaeb85c0727035fe880d8",
  "schema_t003_changed": false
}
```

## Notes

- Aucun script Godot modifié.
- Aucun changement de schéma T003.
- Camille reste lucide/exigeante, sans révélation finale ni ultimatum brutal.
- J5 non intégré : intégration réservée au ticket Scope dédié après contenus/relecture.

## Next step recommandé

**T109 — Écrire Nico/Maya J5 pression sociale MVP**.
