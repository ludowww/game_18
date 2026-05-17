# T077 — Relecture cohérence J3 Camille/Sarah

Thread d’exécution : Dialogues

Statut : DONE

## Périmètre relu

- Camille J3 : `narrative/t075_camille_j3_complete.json`
- Sarah J3 : `narrative/t076_sarah_j3_complete.json`
- Copies prototype :
  - `product/godot_t004_prototype/data/camille_j3_complete.json`
  - `product/godot_t004_prototype/data/sarah_j3_complete.json`

## Verdict

J3 teste bien l’arbitrage d’attention sans déclencher de crise frontale.

- Camille tire vers la disponibilité risquée et la trace émotionnelle.
- Sarah tire vers la présence fiable, le petit rituel et le doute doux.
- Les voix restent distinctes.
- Les fins J3 ouvrent proprement vers J4.
- Le schéma T003 reste inchangé.

## Problèmes trouvés

### 1. Ambiguïté mineure côté Sarah : “photo mentale”

Le texte ne créait pas réellement une image média, mais le mot “photo” pouvait brouiller la contrainte “pas d’image”.

Patch léger appliqué :

- Ancien choix : `Envoie-moi une photo mentale, je veux la voir ce soir.`
- Nouveau choix : `Décris-la-moi. Je veux la voir ce soir.`
- Ancienne réponse Sarah : `Photo mentale envoyée : ...`
- Nouvelle réponse Sarah : `Description mentale : ...`

Objectif : conserver le rituel intime sans suggérer de média/image.

## Points validés

### Camille J3

- Pas de répétition café.
- Pas d’image.
- Pas d’appel.
- Camille reste trouble / disponibilité risquée / sous-texte.
- C3A/C3B/C3C sont clairs pour intégration future.
- Les fins ouvrent J4 : attraction renforcée, limite posée, ou trace gardée.

### Sarah J3

- Pas de dîner.
- Pas de téléphone sur table.
- Pas d’image après patch.
- Pas d’appel.
- Sarah reste intime / quotidienne / soupçon doux.
- Elle n’est pas policière : elle parle de place, geste concret, fatigue émotionnelle.
- S3A/S3B/S3C sont clairs pour intégration future.

### Interaction implicite

- Camille crée une fenêtre courte et capte l’attention.
- Sarah demande une présence fiable via un petit rituel.
- Les deux fils se répondent sans contradiction temporelle.
- Le thème J3 “répondre à l’une commence à coûter à l’autre” est lisible.

## Patchs appliqués

Fichiers patchés :

- `narrative/t076_sarah_j3_complete.json`
- `product/godot_t004_prototype/data/sarah_j3_complete.json`

Fichiers non modifiés :

- `narrative/t075_camille_j3_complete.json`
- `product/godot_t004_prototype/data/camille_j3_complete.json`

Prototype Godot/runtime non modifié.

## Validation post-patch

### Camille J3

- `conversation_id = camille_j3_complete`
- `day = 3`
- `contact_id = camille`
- 46 nodes
- 5 choice nodes
- 3 end nodes
- aucun duplicate ID
- aucun missing target
- aucun unreachable node
- source/copie prototype identiques

### Sarah J3

- `conversation_id = sarah_j3_complete`
- `day = 3`
- `contact_id = sarah`
- 44 nodes
- 5 choice nodes
- 3 end nodes
- aucun duplicate ID
- aucun missing target
- aucun unreachable node
- source/copie prototype identiques

## Recommandation next step

**T078 — Intégrer J3 au prototype via `conversation_blocks.json`**.

Objectif : brancher Camille J3 + Sarah J3 dans le système de jours/blocs externalisés, sans modifier les dialogues JSON.
