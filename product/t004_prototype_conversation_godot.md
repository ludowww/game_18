# T004 — Prototype conversation Godot

Statut : DONE

## Résultat

Prototype Godot 4 minimal créé dans :

`/opt/data/profiles/game_18/product/godot_t004_prototype/`

Il lit le JSON plat T003 et affiche une conversation type messagerie avec Camille J1.

## Fichiers

- `project.godot` : projet Godot 4 minimal.
- `scenes/conversation_screen.tscn` : scène principale.
- `scripts/conversation_screen.gd` : logique conversation.
- `data/camille_j1_intro.json` : dialogue J1 Camille issu de T002 converti au schéma T003.
- `README_T004.md` : note de lancement et limite constatée.

## Fonctionnel

- Lecture du JSON T003 sans modification du schéma.
- Affichage des messages dans l’ordre via `start_node` + `next`.
- Délais simples via `delay` en secondes.
- Choix joueur cliquables.
- Branche simple fonctionnelle.
- Effets appliqués dans un `game_state` minimal : jauges numériques + flags.
- Dialogue J1 Camille inclus : 17 nodes, 2 choix, branches flirt / soft / ignore / disponibilité.

## Validation

Validation statique effectuée :

- JSON valide.
- `schema_version = 0.1`.
- 17 nodes.
- 2 nodes de choix.
- aucun ID dupliqué.
- aucun `next` cassé.
- senders présents : `camille`, `player`, `system`.

Godot CLI n’est pas installé dans l’environnement local, donc le lancement runtime n’a pas pu être vérifié ici.

## Limite du schéma constatée

Aucun blocage réel du schéma T003.

Note pratique : pour tester vite, le script plafonne les délais longs côté affichage avec :

```gdscript
const DEBUG_DELAY_CAP_SECONDS := 1.0
```

Le JSON conserve bien les délais en secondes comme prévu par T003.
