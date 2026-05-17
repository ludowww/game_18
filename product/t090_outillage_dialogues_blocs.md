# T090 — Outillage dialogues/blocs avant J4

Statut : DONE
Thread : Scope MVP / technique

## Décision

Avant d’ouvrir J4, l’outillage existant a été consolidé en un validateur standalone réutilisable :

```bash
cd product/godot_t004_prototype
python3 tools/validate_dialogues_and_blocks.py
python3 tools/validate_dialogues_and_blocks.py --json
```

Le script centralise les validations techniques auparavant éparpillées dans les tests T078/T068 et ajoute le contrôle source `narrative/` ↔ copie prototype `data/`.

## Fichiers créés / modifiés

- `product/godot_t004_prototype/tools/validate_dialogues_and_blocks.py`
  - validateur standalone CLI texte/JSON ;
  - valide dialogues actifs J1→J3 ;
  - compare les sources narratives et copies prototype ;
  - valide `data/conversation_blocks.json` contre les vrais IDs de dialogues.
- `product/godot_t004_prototype/tests/test_t090_dialogue_block_validator.py`
  - test de régression direct `python3` ;
  - vérifie que le validateur couvre les 6 dialogues actifs, les 18 blocs, l’ordre J1→J3, et expose `--json`/`--help`.
- `product/t090_outillage_dialogues_blocs.md`
  - présent artefact produit.
- `roadmap_double_vie_discord.txt`
- `discord_blocks/bloc_04.txt`

## Couverture validateur

### Dialogues actifs couverts

| Conversation | Fichier source | Copie prototype | Nodes | Choices | End |
|---|---|---|---:|---:|---:|
| Camille J1 | `narrative/t007_camille_j1_complete.json` | `data/camille_j1_complete.json` | 45 | 6 | 3 |
| Sarah J1 | `narrative/t037_sarah_j1_complete.json` | `data/sarah_j1_complete.json` | 41 | 5 | 3 |
| Camille J2 | `narrative/t061_camille_j2_complete.json` | `data/camille_j2_complete.json` | 45 | 5 | 3 |
| Sarah J2 | `narrative/t062_sarah_j2_complete.json` | `data/sarah_j2_complete.json` | 45 | 5 | 3 |
| Camille J3 | `narrative/t075_camille_j3_complete.json` | `data/camille_j3_complete.json` | 46 | 5 | 3 |
| Sarah J3 | `narrative/t076_sarah_j3_complete.json` | `data/sarah_j3_complete.json` | 44 | 5 | 3 |

### Contrôles centralisés

- JSON parseable.
- Schéma T003 inchangé : `schema_version = "0.1"`, structure flat `nodes`, types `message` / `choice` / `end`.
- IDs dupliqués.
- Cibles cassées : `next` des nodes et `next` des choices.
- Reachability depuis `start_node`.
- Counts nodes / choices / endings.
- Senders attendus : `player`, `system`, contact actif (`camille` ou `sarah`).
- Effects valides : `flags` array de strings ; jauges numériques en `int`.
- Hash source/prototype identique pour les paires officielles.
- `conversation_blocks.json` :
  - `conversation_id` connu ;
  - `start_node` existant ;
  - chaque `end_nodes` existant ;
  - `unlock_on_done` référence un bloc existant ou vide ;
  - `notification_target` connu ou vide ;
  - ordre J1→J3 exact, 18 blocs.

## Validation

```json
{
  "validator_ok": true,
  "active_dialogues": 6,
  "blocks": 18,
  "errors": 0,
  "warnings": 5,
  "source_copy_match_all_active": true,
  "tests": {
    "test_t078_j3_integration.py": "OK",
    "test_t068_externalized_blocks.py": "OK",
    "test_t090_dialogue_block_validator.py": "OK"
  },
  "godot_cli": "absent"
}
```

Commande exécutée :

```bash
cd product/godot_t004_prototype
python3 tools/validate_dialogues_and_blocks.py --json
python3 tests/test_t078_j3_integration.py \
  && python3 tests/test_t068_externalized_blocks.py \
  && python3 tests/test_t090_dialogue_block_validator.py
```

## Warnings non bloquants

Les fichiers suivants sont détectés comme placeholders/anciens artefacts non actifs et ne bloquent pas J1→J3 :

- `product/godot_t004_prototype/data/camille_j1_intro.json`
- `product/godot_t004_prototype/data/sarah_j1_placeholder.json`
- `narrative/t002_dialogue_camille_j1_structured.json`
- `narrative/t025a_sarah_j1_placeholder.json`
- `narrative/jour_1_mvp.json`

## Limites

- Le validateur est technique, pas un outil auteur visuel.
- Il ne réécrit pas les dialogues et ne modifie pas le schéma T003.
- Il couvre explicitement les conversations actives J1→J3 ; J4 devra être ajouté au mapping `ACTIVE_DIALOGUES` après création/validation de contenu.
- Godot CLI absent sur ce VPS : pas de validation runtime locale, uniquement statique.

## Next step recommandé

Décision Roadmap : choisir entre **cadrage J4** ou **polish UX/rythme J1→J3**. Grâce à T090, l’expansion J4 peut maintenant s’appuyer sur une commande de sécurité centralisée.
