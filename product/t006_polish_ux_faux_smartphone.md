# T006 — Polish UX faux smartphone court

Statut : DONE

## Base

Prototype modifié :

`/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

Le schéma JSON T003 et le fichier Camille J1 n’ont pas été modifiés.

Validation statique :

- JSON valide.
- 17 nodes.
- aucun ID dupliqué.
- aucun `next` cassé.
- Godot CLI absent localement : pas de playtest runtime dans cet environnement.

## 1. Polish appliqués

### Espacement / confort vertical

- Ajout d’un `phone_margin` interne dans le faux téléphone.
- Espacement vertical des bulles augmenté : `separation = 10`.
- Marges internes des bulles ajustées : texte plus respirant.

### Taille max / lisibilité des bulles

- Ajout d’une largeur fixe MVP :

```gdscript
const BUBBLE_WIDTH := 284.0
```

- Les bulles ne prennent plus toute la largeur.
- Lecture plus proche d’une messagerie mobile.

### Alignement mobile

- Camille reste à gauche.
- Joueur reste à droite.
- Messages système centrés.
- Coins des bulles asymétriques pour renforcer l’effet conversation :
  - bulle joueur avec coin bas droit réduit ;
  - bulle Camille avec coin bas gauche réduit.

### Header plus crédible

- Header remplacé par une barre type messagerie :
  - chevron retour `‹` ;
  - avatar textuel `C` ;
  - nom `Camille` ;
  - statut discret `en ligne · J1`.

### Zone de choix plus intégrée

- Les choix sont maintenant contenus dans un panneau bas dédié.
- Panneau visible seulement quand un choix est actif.
- Prompt de choix plus discret.
- Boutons agrandis : hauteur minimale `48`.

### Feedback visuel léger au clic

- Au clic, les boutons de choix sont désactivés immédiatement.
- Petit délai `0.12s` avant d’afficher la suite, pour éviter l’impression de disparition brutale.
- Le message joueur apparaît ensuite via la branche JSON, sans ajouter de système.

### Indication discrète d’attente / écriture

- `Camille écrit…` conservé et légèrement indenté.
- Couleur plus discrète.
- Toujours basé sur le champ `delay` existant.

### Debug masqué

- Debug state toujours masqué par défaut :

```gdscript
const SHOW_DEBUG_STATE := false
```

## 2. Éléments volontairement non traités

- Pas de refonte UI complète.
- Pas de système de contacts.
- Pas de sauvegarde.
- Pas d’écran liste conversations.
- Pas de notifications système OS.
- Pas d’animations avancées.
- Pas de sons / vibrations.
- Pas de thème complet.
- Pas de gestion responsive avancée multi-résolutions.
- Pas de modification du schéma JSON T003.
- Pas d’ajout de contenu hors Camille J1.

## 3. Décision

Le prototype est **prêt pour écrire / intégrer le contenu J1 complet côté structure**, mais il faut prévoir un **playtest runtime externe dans Godot** avant de figer l’UX.

Décision courte :

**OK pour passer à J1 complet, avec un checkpoint playtest runtime dès que Godot est disponible.**

Pas besoin d’un T007 polish avant contenu, sauf si le playtest visuel révèle un problème majeur de lecture ou de scroll.
