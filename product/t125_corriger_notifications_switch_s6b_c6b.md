# T125 — Corriger notifications switch vers S6B / C6B

Statut : DONE  
Thread : Scope MVP / Roadmap  
Portée : bugfix runtime quick-switch J6, sans réécriture dialogue

## Retour runtime Ludo

Pendant le playtest J6/finale après T124 :

> vers S6B et vers C6B : pas de notif pour switch de conversation. Le reste semble ok

Interprétation :

- progression générale J6/finale OK ;
- problème ciblé sur le toast de switch rapide `Nouveau message de X · Ouvrir` ;
- cas touchés :
  - déverrouillage de `sarah_s6b` après `maya_m6a` ;
  - déverrouillage de `camille_c6b` après `sarah_s6b`.

## Diagnostic

Les blocs `S6B` et `C6B` sont des deuxièmes blocs dans des conversations déjà commencées (`sarah_j6` et `camille_j6`).

Après `S6A` / `C6A`, l’état de conversation conserve un `next_node` de transition :

- Sarah : `s6_014_a/b/c` → puis `s6_block_b` ;
- Camille : `c6_014_a/b/c` → puis `c6_block_b`.

La réparation live des notifications (`repair_available_block_notifications`) vérifie qu’un bloc disponible n’a pas déjà été commencé. Elle considérait tout `next_node` différent du `start_node` du bloc comme “déjà commencé”.

Pour `S6B` / `C6B`, c’était faux : ces nodes `s6_014_*` / `c6_014_*` sont des ponts de reprise avant le vrai début du bloc B, pas un bloc B déjà commencé.

Résultat possible : si le bloc B était déjà `available` sans badge dans la save/runtime, la réparation live ne posait pas `has_new`, donc pas de toast quick-switch.

## Correction

Correction data-driven : ajout d’un champ optionnel `pre_start_nodes` dans `conversation_blocks.json` pour les blocs J6 concernés.

```json
"sarah_s6b": {
  "start_node": "s6_block_b",
  "pre_start_nodes": ["s6_014_a", "s6_014_b", "s6_014_c"]
}
```

```json
"camille_c6b": {
  "start_node": "c6_block_b",
  "pre_start_nodes": ["c6_014_a", "c6_014_b", "c6_014_c"]
}
```

Puis `conversation_state.gd` utilise ce champ dans `_has_started_available_block(...)` :

- si `next_node` est dans `pre_start_nodes`, le bloc disponible n’est pas considéré comme commencé ;
- la réparation live peut donc poser `has_new` et permettre le toast quick-switch ;
- les vrais blocs déjà ouverts restent protégés par le statut `active` et les autres checks existants.

## Fichiers modifiés

- `product/godot_t004_prototype/data/conversation_blocks.json`
- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/tests/test_t125_j6_second_block_quick_switch.py`
- tests de régression quick-switch/typing ajustés au nouveau hash de `conversation_blocks.json` :
  - `test_t104_quick_switch_repair_available_live.py`
  - `test_t103_quick_switch_live_refresh.py`
  - `test_t102_quick_switch_new_message.py`
  - `test_t101_typing_bubble_scroll_friendly.py`
  - `test_t100_typing_bubble_in_thread.py`
  - `test_t099_contact_colors_typing_indicator.py`

## Non modifié

- Aucun JSON dialogue J6/finale.
- Aucun texte narratif.
- Aucun schéma T003.
- Aucun script UI hors `conversation_state.gd`.
- Aucun changement save payload.
- Aucun nouveau système lourd de fins/notifications.

## Validation

Tests directs OK :

```txt
python3 tests/test_t125_j6_second_block_quick_switch.py
python3 tests/test_t124_j6_fins_integration.py
python3 tests/test_t104_quick_switch_repair_available_live.py
python3 tests/test_t103_quick_switch_live_refresh.py
python3 tests/test_t102_quick_switch_new_message.py
python3 tests/test_t101_typing_bubble_scroll_friendly.py
python3 tests/test_t100_typing_bubble_in_thread.py
python3 tests/test_t099_contact_colors_typing_indicator.py
python3 tests/test_t097_j4_integration.py
python3 tests/test_t090_dialogue_block_validator.py
python3 tests/test_t112_j5_integration.py
python3 tests/test_t078_j3_integration.py
python3 tests/test_t063_j2_integration.py
python3 tests/test_t053_notification_guards.py
```

Validateur :

```txt
T090 dialogue/block validation: OK
Active dialogues: 20
Blocks: 46
Errors: 0
Warnings: 5
```

Nouveau SHA `conversation_blocks.json` :

```txt
5bee89f1e5d8422a8d368f2afda4071b3a05aea6011e60708dcd1a34c7d6f6b0
```

Godot CLI absent sur VPS : runtime à valider côté Ludo.

## Checklist playtest Ludo

Reprendre un run J6/finale et vérifier :

1. Finir `M6A` depuis Maya.
2. Vérifier apparition du toast : `Nouveau message de Sarah · Ouvrir`.
3. Ouvrir Sarah via toast, vérifier que `S6B` reprend correctement.
4. Finir `S6B`.
5. Vérifier apparition du toast : `Nouveau message de Camille · Ouvrir`.
6. Ouvrir Camille via toast, vérifier que `C6B` reprend correctement.
7. Continuer vers `I6A`, puis `FIN`.
8. Faire un save/reload rapide après `M6A` ou avant `S6B` si possible pour vérifier la réparation live/save.
