# Double Vie — Refonte J1 — Draft lisible

## Scène : `j1_06_sarah_rentrer_manger`

Statut : draft narratif lisible, non intégré runtime.

Objectif : respiration domestique avec Sarah. Rappeler que Sarah est une relation vivante, pas seulement une source de reproche.

---

## Fonction de la scène

Sarah écrit plus tard dans la journée. Elle parle de repas, de retour, de présence concrète. La scène ne doit pas relancer l’interrogatoire sur Camille. Elle doit montrer ce que le joueur risque de perdre : une intimité ordinaire.

---

## Version draft

`j1_06_sarah_001` Sarah :
Tu rentres manger ce soir ?

`j1_06_sarah_002` Sarah :
J’ai sorti ce qu’il restait de pâtes.

`j1_06_sarah_003` Sarah :
Et j’ai retrouvé ton pull sur la chaise, donc techniquement tu es déjà un peu là.

`j1_06_sarah_004` Sarah :
Je sais pas si ça compte.

---

## Choix principal

`j1_06_choice_sarah_meal` — Que répondre à Sarah ?

---

## Choix A — Être présent

ID : `j1_06_come_home`

Texte joueur :
Oui. Je rentre. Et je veux être vraiment là, pas juste poser mon sac.

Effets :
```json
{
  "confiance_sarah": 2,
  "distance_sarah": -2,
  "intimite_sarah": 2,
  "fatigue_emotionnelle": -1,
  "flags": [
    "sarah_j1_domestic_presence"
  ]
}
```

### Réponse Sarah

`j1_06_player_005a` Joueur :
Oui. Je rentre. Et je veux être vraiment là, pas juste poser mon sac.

`j1_06_sarah_006a` Sarah :
D’accord.

`j1_06_sarah_007a` Sarah :
Je vais réchauffer doucement alors.

`j1_06_sarah_008a` Sarah :
Les pâtes. Pas nous. Enfin, je sais pas. Peut-être un peu les deux.

Sortie : `j1_06_exit_domestic_warmth`

---

## Choix B — Promettre plus tard

ID : `j1_06_later`

Texte joueur :
Je passe plus tard. Je veux pas te laisser sans réponse, mais j’ai besoin d’un peu de temps.

Effets :
```json
{
  "confiance_sarah": 1,
  "distance_sarah": 1,
  "fatigue_emotionnelle": 1,
  "flags": [
    "promised_sarah_later_j1"
  ]
}
```

### Réponse Sarah

`j1_06_player_005b` Joueur :
Je passe plus tard. Je veux pas te laisser sans réponse, mais j’ai besoin d’un peu de temps.

`j1_06_sarah_006b` Sarah :
Merci de prévenir.

`j1_06_sarah_007b` Sarah :
Je vais pas faire comme si ça me faisait plaisir.

`j1_06_sarah_008b` Sarah :
Mais c’est mieux que de regarder l’heure en inventant des raisons à ta place.

Sortie : `j1_06_exit_later_fragile`

---

## Choix C — Incertitude

ID : `j1_06_uncertain`

Texte joueur :
Je sais pas encore. Je suis désolé, je suis un peu partout aujourd’hui.

Effets :
```json
{
  "distance_sarah": 1,
  "culpabilite": 1,
  "fatigue_emotionnelle": 1,
  "flags": [
    "sarah_j1_uncertain_return"
  ]
}
```

### Réponse Sarah

`j1_06_player_005c` Joueur :
Je sais pas encore. Je suis désolé, je suis un peu partout aujourd’hui.

`j1_06_sarah_006c` Sarah :
Oui.

`j1_06_sarah_007c` Sarah :
Je le vois bien.

`j1_06_sarah_008c` Sarah :
C’est juste que moi je suis ici, du coup.

Sortie : `j1_06_exit_sarah_waits`

---

## Choix D — Prétexte travail

ID : `j1_06_work_excuse`

Texte joueur :
Je vais sûrement finir tard avec le boulot. Mange sans moi.

Effets :
```json
{
  "confiance_sarah": -1,
  "distance_sarah": 2,
  "coherence": -1,
  "culpabilite": 1,
  "flags": [
    "used_work_excuse_sarah_j1"
  ]
}
```

### Réponse Sarah

`j1_06_player_005d` Joueur :
Je vais sûrement finir tard avec le boulot. Mange sans moi.

`j1_06_sarah_006d` Sarah :
D’accord.

`j1_06_sarah_007d` Sarah :
Je vais arrêter de garder une assiette “au cas où”, alors.

`j1_06_sarah_008d` Sarah :
C’est pas grave. Enfin. C’est une phrase pratique.

Sortie : `j1_06_exit_domestic_distance`

---

## Choix E — Répondre trop tard

ID : `j1_06_late_reply`

Texte joueur :
Répondre plus tard : Désolé, j’ai pas vu. Tu as mangé ?

Effets :
```json
{
  "distance_sarah": 2,
  "intimite_sarah": -1,
  "culpabilite": 1,
  "flags": [
    "late_reply_sarah_meal_j1"
  ]
}
```

### Réponse Sarah

`j1_06_sys_005e` Système :
Tu réponds plus tard.

`j1_06_player_006e` Joueur :
Désolé, j’ai pas vu. Tu as mangé ?

`j1_06_sarah_007e` Sarah :
Oui.

`j1_06_sarah_008e` Sarah :
J’ai mangé.

`j1_06_sarah_009e` Sarah :
Ton assiette est dans le frigo.

Sortie : `j1_06_exit_late_cold`

---

# Notes de validation

- La scène parle du quotidien, pas d’une enquête.
- Sarah a une présence affective propre.
- Les choix modifient `intimite_sarah`, `distance_sarah`, `confiance_sarah`.
- Le retard est une action.
