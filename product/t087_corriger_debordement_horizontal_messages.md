# T087 — Corriger débordement horizontal écran Messages

## Décision

Correction UI Godot uniquement sur l’écran `Messages` : les cartes et le header sont contraints à la largeur disponible, sans toucher aux JSON de dialogues, au schéma T003, à `conversation_blocks.json` ni à la sauvegarde.

## Corrections appliquées

- Header rendu responsive : sous-titre séparé des contrôles debug dans un `header_stack`, puis `Reset` / `Mode test rapide` déplacés sur une deuxième ligne compacte alignée à droite.
- Suppression des minimums horizontaux fixes côté contrôles debug : les boutons gardent une hauteur minimale mais n’imposent plus de largeur `x`.
- Liste Messages explicitement contrainte : scroll horizontal désactivé et conteneur liste à largeur minimale `0`.
- Cartes de conversation contraintes : carte `Vector2(0, 140)`, row interne et text box en `SIZE_EXPAND_FILL` + minimum horizontal `0`.
- Titres/previews : wrap intelligent conservé, ellipsis volontaire ajouté en sécurité (`TextServer.OVERRUN_TRIM_ELLIPSIS`), preview légèrement plus haute pour éviter les coupes.

## Non-changements

- Aucun changement JSON de dialogues.
- Aucun changement schéma T003.
- Aucun changement `data/conversation_blocks.json`.
- Aucun changement sauvegarde / payload / day-state.
- Aucun changement gameplay ou contenu narratif.

## Validation statique

Commandes exécutées depuis `product/godot_t004_prototype/` :

```bash
python3 tests/test_t087_messages_horizontal_overflow.py
for f in tests/test_t087_messages_horizontal_overflow.py tests/test_t085_archives_jours_passes.py tests/test_t083_mode_test_accelere.py tests/test_t080_day_transition_button_label.py tests/test_t078_j3_integration.py tests/test_t072_repair_existing_save_badges.py tests/test_t068_externalized_blocks.py tests/test_t063_j2_integration.py tests/test_t057_narrative_blocks.py tests/test_t053_notification_guards.py; do python3 "$f" || exit 1; done
```

Résultat : OK.

Godot CLI absent sur le VPS (`godot_cli_absent`) : validation runtime à faire côté Ludo dans Godot 4.6.

## Checklist runtime recommandée

1. Ouvrir Messages en largeur normale puis étroite.
2. Vérifier que les cartes Camille/Sarah restent dans le cadre.
3. Vérifier que previews ne sont plus coupées horizontalement.
4. Vérifier que `Reset` et `Mode test rapide` restent visibles sur une deuxième ligne, sans sortir du bord droit.
5. Ouvrir/fermer Archives pour vérifier qu’aucune carte archivée ne déborde.
