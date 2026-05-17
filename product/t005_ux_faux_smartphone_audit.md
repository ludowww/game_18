# T005 — Tester / ajuster l’UX faux smartphone minimal

Statut : DONE

## Contexte testé

Base : prototype T004 dans `/opt/data/profiles/game_18/product/godot_t004_prototype/`.

Godot CLI n’est pas disponible dans l’environnement local : le test est donc une revue statique UX/code du prototype, pas un playtest runtime visuel.

## 1. Problèmes UX constatés

1. **Bulles trop neutres**
   - Avant correction, toutes les bulles occupaient toute la largeur.
   - Camille / joueur n’étaient pas assez différenciés visuellement.
   - Effet “messagerie mobile” faible.

2. **Interface trop debug**
   - Le label `État: {}` était visible en permanence.
   - Utile techniquement, mais il casse l’illusion faux smartphone.

3. **Manque de cadre smartphone**
   - L’écran ressemblait à une liste UI Godot, pas encore à un téléphone.
   - Pas de fond sombre / marge / frame mobile.

4. **Sensation d’attente trop faible**
   - Les délais existaient techniquement.
   - Mais l’utilisateur ne voyait pas assez clairement qu’un message arrivait.

5. **Choix joueur peu incarnés**
   - Les boutons étaient fonctionnels mais trop standards.
   - Risque : le joueur comprend l’action, mais pas encore la sensation “je réponds à un message”.

6. **Confort mobile vertical perfectible**
   - Taille des boutons et respiration améliorables.
   - Besoin de vérifier en vrai dans Godot sur viewport vertical.

## 2. Corrections minimales appliquées

Corrections faites dans :

`/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

### Appliqué

- Ajout d’un fond sombre global.
- Ajout d’un cadre arrondi type faux smartphone.
- Header simplifié : `Camille`.
- Bulles différenciées :
  - Camille à gauche ;
  - joueur à droite ;
  - système centré / neutre.
- Couleurs simples :
  - joueur bleu ;
  - Camille gris sombre ;
  - system gris neutre.
- Ajout d’un indicateur minimal : `Camille écrit…` pendant les délais.
- Boutons de choix agrandis.
- Label debug `État` masqué par défaut via :

```gdscript
const SHOW_DEBUG_STATE := false
```

### Non modifié

- Schéma JSON T003 inchangé.
- Données conversation inchangées.
- Pas de sauvegarde.
- Pas de système de contacts.
- Pas d’animation complexe.

## 3. Corrections minimales proposées ensuite

À traiter seulement si on lance un T006 polish UX :

1. Ajouter marges internes plus propres dans la frame téléphone.
2. Tester les longues réponses sur boutons, car certains choix peuvent dépasser.
3. Ajouter un très léger séparateur visuel entre conversation et choix.
4. Ajouter une zone “répondre…” factice au-dessus des boutons.
5. Vérifier le scroll auto en runtime Godot.
6. Vérifier que les délais plafonnés à 1s restent lisibles.
7. Faire un screenshot / playtest réel dans Godot.

## 4. Décision

**Prototype suffisant pour valider la logique T004/T005**, mais **T006 polish UX léger recommandé** avant d’écrire beaucoup plus de contenu.

Raison : la structure est bonne, le schéma T003 tient, les corrections MVP améliorent l’illusion smartphone, mais il manque encore une validation runtime visuelle dans Godot.

Décision courte : **T006 nécessaire, mais limité à du polish UX court — pas de nouveau système.**
