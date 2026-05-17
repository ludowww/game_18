# T041 — Relecture cohérence dialogues Camille/Sarah J1

Thread d’exécution : Dialogues

Statut : DONE

## Périmètre relu

- Camille J1 complet : `narrative/t007_camille_j1_complete.json`
- Sarah J1 complet : `narrative/t037_sarah_j1_complete.json`
- Copies prototype :
  - `product/godot_t004_prototype/data/camille_j1_complete.json`
  - `product/godot_t004_prototype/data/sarah_j1_complete.json`

## Diagnostic cohérence

### Points validés

- **Voix distinctes** :
  - Camille = tentation, trouble, jeu, attente de notification.
  - Sarah = quotidien, intimité, douceur inquiète, soupçon progressif.
- **Timing J1 cohérent** :
  - Les deux fils peuvent coexister sur la même journée.
  - Camille monte vers le soir puis 23:42.
  - Sarah reste sur une progression matin → journée → fin de journée.
- **Sarah ne sait pas trop tôt** :
  - Elle remarque des indices concrets : départ discret, café froid, vibrations nocturnes, flou sur la soirée.
  - Elle ne nomme jamais Camille et n’accuse pas explicitement.
- **Camille reste dans son rôle** :
  - Elle crée l’appel du risque sans basculer en scène explicite.
  - Le cliffhanger 23:42 conserve la règle “messages d’abord”.
- **Choix joueur plausibles** :
  - Les réponses permettent esquive, demi-vérité, disponibilité, limite ou tentation.
- **Fins compatibles avec suite MVP** :
  - Les fins ouvrent des flags exploitables sans enfermer la route.

## Faiblesses détectées

### 1. Sarah devenait légèrement trop frontale en fin J1

Ancien enchaînement :

- `s1_020` : “Je vais poser une question simple, et tu peux répondre simplement.”
- `s1_021` : “Il y a quelque chose que tu ne me dis pas ?”

Problème : acceptable, mais un peu trop accusatoire pour le brief “soupçon doux” et pour une J1 où Sarah ne doit pas savoir trop tôt.

Correction appliquée :

- `s1_020` : “Je vais poser une question simple, mais je veux pas que ça sonne comme un piège.”
- `s1_021` : “J’ai l’impression que tu es ailleurs depuis ce matin. Je me trompe ?”

Effet : Sarah reste lucide et blessée, mais pas enquêtrice.

### 2. Cohérence implicite Camille/Sarah : tension volontaire, pas contradiction

Camille peut pousser vers le café le soir pendant que Sarah attend le joueur. Ce n’est pas une incohérence : c’est le cœur de la double vie.

Aucune correction nécessaire.

### 3. Effets/jauges

Les conséquences restent légères et exploitables : `risk`, `guilt`, `sarah_trust`, `camille_interest`, flags.

Aucune correction nécessaire.

## Patchs JSON appliqués

Fichiers patchés :

- `narrative/t037_sarah_j1_complete.json`
- `product/godot_t004_prototype/data/sarah_j1_complete.json`

Fichiers non modifiés :

- `narrative/t007_camille_j1_complete.json`
- `product/godot_t004_prototype/data/camille_j1_complete.json`

Schéma T003 conservé.

Prototype Godot non modifié hors fichier JSON Sarah.

## Validation statique après patch

### Camille

- `conversation_id = camille_j1_complete`
- `schema_version = 0.1`
- 45 nodes
- 6 choice nodes
- 3 end nodes
- senders : `camille`, `player`, `system`
- aucun duplicate ID
- aucun missing target
- aucun unreachable node
- source/copie prototype identiques

### Sarah

- `conversation_id = sarah_j1_complete`
- `schema_version = 0.1`
- 41 nodes
- 5 choice nodes
- 3 end nodes
- senders : `sarah`, `player`, `system`
- aucun duplicate ID
- aucun missing target
- aucun unreachable node
- source/copie prototype identiques

## Décision

Les dialogues Camille/Sarah J1 sont cohérents pour le MVP après patch léger de Sarah.

Aucune refonte lourde nécessaire.
