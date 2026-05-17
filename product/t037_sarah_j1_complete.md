# T037 — Étendre Sarah J1 en contenu complet intégrable

Thread d’exécution : Dialogues

Statut : DONE

## Résultat

Sarah J1 placeholder a été transformée en conversation complète MVP au format JSON plat T003, sans changement de schéma.

Fichier source narratif :

`/opt/data/profiles/game_18/narrative/t037_sarah_j1_complete.json`

Copie prête pour prototype :

`/opt/data/profiles/game_18/product/godot_t004_prototype/data/sarah_j1_complete.json`

## Contenu

- Ton distinct de Camille : domestique, tendre, inquiet, soupçon doux.
- Continuité depuis le placeholder T025A : départ silencieux, café froid, vibrations nocturnes.
- Choix joueur intégrés.
- Branches simples par `next`.
- Conséquences légères via `effects` : `sarah_trust`, `risk`, `guilt`, flags.
- Cliffhanger fin J1 : Sarah formule un soupçon doux sur l’impression que le joueur est ailleurs.

## Validation statique

- JSON valide.
- `schema_version = 0.1`.
- `conversation_id = sarah_j1_complete`.
- 41 nodes.
- 5 nodes de choix.
- 3 fins possibles.
- Senders : `sarah`, `player`, `system`.
- Aucun ID dupliqué.
- Aucun `next` cassé.
- Tous les nodes sont atteignables depuis `start_node`.
- Aucun changement du schéma T003.
