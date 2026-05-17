# T004 — Prototype conversation Godot

Prototype minimal Godot 4 qui lit le JSON plat T003 et affiche une conversation J1 Camille.

## Contenu

- `project.godot` : projet Godot 4 minimal.
- `scenes/conversation_screen.tscn` : écran conversation.
- `scripts/conversation_screen.gd` : chargement JSON, affichage messages, choix, effets, branches.
- `data/camille_j1_intro.json` : dialogue J1 Camille issu de T002, converti au schéma T003.

## Fonctionnel MVP

- Lecture de `schema_version`, `conversation_id`, `start_node`, `nodes`.
- Affichage séquentiel des messages Camille / joueur / system.
- Délais simples via `delay` en secondes.
- Choix cliquables.
- Branche simple via `next`.
- Effets simples cumulés dans `game_state` : jauges + flags.

## Lancer

Ouvrir le dossier `godot_t004_prototype` dans Godot 4, puis lancer la scène principale.

Si Godot CLI est installé :

```bash
godot4 --path /opt/data/profiles/game_18/product/godot_t004_prototype
```

## Limite constatée du schéma

Aucun blocage réel. Pour un prototype rapide, les délais longs du JSON sont plafonnés côté affichage par `DEBUG_DELAY_CAP_SECONDS = 1.0` dans le script, sans modifier le schéma T003.
