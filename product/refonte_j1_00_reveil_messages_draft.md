# Double Vie — Refonte J1 — Draft lisible

## Scène : `j1_00_reveil_messages`

Statut : draft narratif lisible, non intégré runtime.
Source : `product/refonte_j1_structure_scenes.md`
Objectif : tester l’ouverture V2 avec cinq messages entrants et choix de priorité.

---

## Fonction de la scène

Le joueur se réveille après la soirée.
Son téléphone contient cinq messages non lus.
Chaque contact arrive avec une tension différente : Sarah cherche une présence, Camille sait que le moment dehors n’était pas neutre, Nico rappelle l’alibi fragile, Maya observe le timing social, Inès perçoit une faille intérieure.

La scène ne révèle pas toute la soirée. Elle force seulement le premier choix : à qui répondre en premier ?

---

## Contraintes de voix

Sarah : concrète, inquiète, pas enquêtrice.
Camille : précise, lucide, trouble.
Nico : oral, drôle, alerte.
Maya : court, social, piquant.
Inès : doux, hésitant, flottant.

---

## Messages entrants

`j1_00_sys_001` Système :
L’écran s’allume avant toi.

`j1_00_sys_002` Système :
Cinq conversations attendent. Pas dans le même silence.

`j1_00_sarah_001` Sarah :
T’es réveillé ? Faut qu’on parle d’hier.

`j1_00_nico_001` Nico :
frérot j’ai fait ce que j’ai pu mais ton histoire sent le plan claqué

`j1_00_camille_001` Camille :
Je crois qu’on a été moins discrets qu’on pensait.

`j1_00_maya_001` Maya :
je pose ça là : vous êtes fatigants.

`j1_00_ines_001` Inès :
C’est peut-être pas mes affaires. Mais tu avais l’air triste hier.

`j1_00_sys_003` Système :
Tu peux répondre à tout le monde. Pas en premier.

---

## Choix principal

`j1_00_choice_priority` — À qui répondre en premier ?

### Choix A — Sarah

ID : `j1_00_reply_sarah_first`

Texte joueur affiché :
Ouvrir Sarah.

Effets :
```json
{
  "confiance_sarah": 2,
  "distance_sarah": -1,
  "tension_camille": -1,
  "flags": ["first_reply_sarah"]
}
```

Suite : `j1_01_sarah_absence`

Intention :
Le joueur choisit la relation officielle et la présence immédiate. Camille peut ressentir le délai plus tard.

---

### Choix B — Camille

ID : `j1_00_reply_camille_first`

Texte joueur affiché :
Ouvrir Camille.

Effets :
```json
{
  "tension_camille": 2,
  "confiance_sarah": -1,
  "culpabilite": 1,
  "flags": ["first_reply_camille", "delayed_reply_sarah_j1"]
}
```

Suite : `j1_02_camille_dehors`

Intention :
Le joueur suit le trouble avant de rassurer Sarah. Ce n’est pas encore une faute irréversible, mais c’est déjà un ordre de priorité.

---

### Choix C — Nico

ID : `j1_00_reply_nico_first`

Texte joueur affiché :
Ouvrir Nico.

Effets :
```json
{
  "dette_nico": 1,
  "fatigue_emotionnelle": 1,
  "flags": ["first_reply_nico", "delayed_reply_sarah_j1", "delayed_reply_camille_j1"]
}
```

Suite : `j1_03_nico_couverture`

Intention :
Le joueur cherche à stabiliser la version avant de parler aux personnes directement concernées.

---

### Choix D — Maya

ID : `j1_00_reply_maya_first`

Texte joueur affiché :
Ouvrir Maya.

Effets :
```json
{
  "suspicion_maya": 1,
  "risque_exposition": 1,
  "flags": ["first_reply_maya", "delayed_reply_sarah_j1", "delayed_reply_camille_j1"]
}
```

Suite : `j1_04_maya_pique`

Intention :
Le joueur veut savoir ce qui est visible socialement. Ce choix peut paraître défensif.

---

### Choix E — Inès

ID : `j1_00_reply_ines_first`

Texte joueur affiché :
Ouvrir Inès.

Effets :
```json
{
  "fuite_ines": 2,
  "fatigue_emotionnelle": 1,
  "culpabilite": 1,
  "flags": ["first_reply_ines", "delayed_reply_sarah_j1", "delayed_reply_camille_j1"]
}
```

Suite : `j1_05_ines_faille`

Intention :
Le joueur choisit la conversation qui demande le moins de comptes. Doux en surface, inquiétant pour la suite.

---

## Sorties possibles

- Si Sarah est ouverte en premier : le jeu démarre sur la présence et la première version officielle.
- Si Camille est ouverte en premier : le jeu démarre sur le trouble et la culpabilité.
- Si Nico est ouvert en premier : le jeu démarre sur l’alibi et la dette.
- Si Maya est ouverte en premier : le jeu démarre sur la peur d’être vu.
- Si Inès est ouverte en premier : le jeu démarre sur la fuite latérale.

---

## Notes pour conversion JSON Godot

Le runtime actuel ne gère pas encore naturellement un écran d’ouverture multi-conversations comme scène unique.
Deux options techniques seront possibles plus tard :

1. créer une conversation système `j1_00_reveil_messages` dont le choix renvoie vers la conversation sélectionnée ;
2. simuler l’ouverture dans la liste de conversations via badges `has_new` sur les cinq contacts et enregistrer `first_reply_*` au premier contact ouvert.

Recommandation pour prototype V2 : commencer par option 1, plus simple à valider en JSON plat.

---

## Critères de validation narrative

Cette scène est acceptable si :

- les cinq voix sont différenciées ;
- le joueur comprend immédiatement que l’ordre compte ;
- aucun personnage n’explique toute la soirée ;
- le choix d’Inès ressemble bien à une fuite, pas à une romance ;
- le choix de Nico ressemble à une gestion de version, pas à un bouton solution ;
- Sarah n’est pas réduite à un reproche ;
- Camille n’est pas réduite à une récompense.
