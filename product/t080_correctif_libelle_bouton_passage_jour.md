# T080 — Correctif libellé bouton passage de jour

Statut : DONE

## Contexte

Lors du playtest runtime T079, le bouton de transition affichait encore `Passer au Jour 2` au moment où le prototype devait proposer le passage vers le Jour 3.

Cause : le libellé et le tooltip de `_make_day_transition_button()` étaient hardcodés pour J1→J2 dans `conversation_list.gd`.

## Correctif appliqué

Fichier modifié :
- `product/godot_t004_prototype/scripts/conversation_list.gd`

Changement :
- calcul du jour cible via `ConversationState.current_day + 1` ;
- libellé dynamique : `Passer au Jour X` ;
- tooltip générique : `Passer au jour suivant`.

Comportement attendu :
- si `current_day = 1` : bouton `Passer au Jour 2` ;
- si `current_day = 2` : bouton `Passer au Jour 3`.

## Non-changements

- Aucun changement JSON.
- Aucun changement gameplay.
- Aucun changement de sauvegarde.
- Aucun changement de schéma T003.
- Aucun changement UX autre que le libellé et le tooltip du bouton.

## Test ajouté

- `product/godot_t004_prototype/tests/test_t080_day_transition_button_label.py`

Le test vérifie :
- absence du hardcode `Passer au Jour 2` dans `_make_day_transition_button()` ;
- absence du tooltip hardcodé `Camille J1 et Sarah J1 sont terminés` ;
- présence du calcul `ConversationState.current_day + 1` ;
- présence du libellé dynamique `Passer au Jour " + str(next_day)` ;
- présence d’un tooltip générique.

## Validation

Commande lancée depuis `product/godot_t004_prototype/` :

```bash
python3 tests/test_t080_day_transition_button_label.py \
  && python3 tests/test_t078_j3_integration.py \
  && python3 tests/test_t072_repair_existing_save_badges.py \
  && python3 tests/test_t068_externalized_blocks.py \
  && python3 tests/test_t063_j2_integration.py \
  && python3 tests/test_t057_narrative_blocks.py \
  && python3 tests/test_t053_notification_guards.py
```

Résultat : OK.

Sortie :

```txt
T080 day transition button label tests OK
T078 J3 integration tests OK
T072 repair existing save badge tests OK
T068 externalized block config tests OK
T063 J2 integration tests OK
T057 narrative block lock tests OK
T053 notification guard tests OK
```

## Limite

Validation runtime locale non faite : Godot CLI absent sur le VPS (`godot_cli_absent`).

## Next step

Reprendre le playtest runtime T079/T081 côté Godot 4.6 : vérifier que le bouton affiche bien `Passer au Jour 3` après fin J2, puis continuer le contrôle progression J3 / badges / sauvegarde.
