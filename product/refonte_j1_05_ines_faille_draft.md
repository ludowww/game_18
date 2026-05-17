# Double Vie — Refonte J1 — Draft lisible

## Scène : `j1_05_ines_faille`

Statut : draft narratif lisible, non intégré runtime.

Objectif : poser Inès comme porte latérale et miroir de fuite, pas comme romance complète.

---

## Fonction de la scène

Inès écrit parce qu’elle a perçu un état chez le joueur. Elle n’a pas de preuve et ne cherche pas à obtenir une confession. Elle offre un espace doux, presque en marge, qui peut devenir une fuite si le joueur s’y accroche.

---

## Connaissances d’Inès

Inès sait :

- le joueur avait l’air ailleurs ;
- il semblait triste ou déplacé ;
- il cherchait peut-être une sortie.

Inès ignore :

- la tension avec Camille ;
- l’état réel du couple avec Sarah ;
- le rôle de Nico ;
- ce que Maya a vu.

---

## Version draft

`j1_05_ines_001` Inès :
C’est peut-être pas mes affaires.

`j1_05_ines_002` Inès :
Mais tu avais l’air triste hier.

`j1_05_ines_003` Inès :
Enfin pas triste exactement.

`j1_05_ines_004` Inès :
Plutôt comme quelqu’un qui cherchait une sortie sans vouloir bouger.

`j1_05_ines_005` Inès :
Oublie si c’est bizarre.

---

## Choix principal

`j1_05_choice_ines_faille` — Que répondre à Inès ?

---

## Choix A — S’ouvrir doucement

ID : `j1_05_open_softly`

Texte joueur :
Non, c’est pas bizarre. Je crois que t’as vu juste. Je sais pas trop où j’étais dans ma tête hier.

Effets :
```json
{
  "fuite_ines": 1,
  "fatigue_emotionnelle": -1,
  "culpabilite": 1,
  "flags": [
    "opened_to_ines"
  ]
}
```

### Réponse Inès

`j1_05_player_006a` Joueur :
Non, c’est pas bizarre. Je crois que t’as vu juste. Je sais pas trop où j’étais dans ma tête hier.

`j1_05_ines_007a` Inès :
Je me demandais si j’avais inventé.

`j1_05_ines_008a` Inès :
Tu avais l’air là, mais pas vraiment dans la pièce.

`j1_05_ines_009a` Inès :
Pas besoin d’expliquer si t’as pas les mots.

`j1_05_ines_010a` Inès :
Je voulais juste vérifier que tu étais rentré entier. Enfin, à peu près.

Sortie : `j1_05_exit_soft_opening`

---

## Choix B — Garder une distance respectueuse

ID : `j1_05_keep_distance`

Texte joueur :
Merci d’avoir écrit. Je suis un peu emmêlé, mais je préfère pas te mettre là-dedans.

Effets :
```json
{
  "fuite_ines": -1,
  "coherence": 1,
  "respect_camille": 0,
  "flags": [
    "kept_ines_at_distance"
  ]
}
```

### Réponse Inès

`j1_05_player_006b` Joueur :
Merci d’avoir écrit. Je suis un peu emmêlé, mais je préfère pas te mettre là-dedans.

`j1_05_ines_007b` Inès :
C’est peut-être mieux.

`j1_05_ines_008b` Inès :
Je voulais pas entrer dans une pièce où je ne vois pas les meubles.

`j1_05_ines_009b` Inès :
Mais je suis contente que tu aies répondu.

Sortie : `j1_05_exit_distance_respected`

---

## Choix C — Demander pourquoi elle écrit

ID : `j1_05_ask_why_write`

Texte joueur :
Pourquoi tu m’écris ça ? T’as vu quelque chose ?

Effets :
```json
{
  "fuite_ines": 1,
  "fatigue_emotionnelle": 1,
  "risque_exposition": 1,
  "flags": [
    "asked_ines_why_write"
  ]
}
```

### Réponse Inès

`j1_05_player_006c` Joueur :
Pourquoi tu m’écris ça ? T’as vu quelque chose ?

`j1_05_ines_007c` Inès :
Pas “quelque chose” comme ça.

`j1_05_ines_008c` Inès :
Je suis pas très douée pour les preuves.

`j1_05_ines_009c` Inès :
J’ai surtout vu ton visage quand tu pensais que personne ne regardait.

`j1_05_ines_010c` Inès :
C’est peut-être rien. Je sais pas.

Sortie : `j1_05_exit_perception_only`

---

## Choix D — Utiliser Inès comme fuite

ID : `j1_05_fuite_seed`

Texte joueur :
J’aurais peut-être préféré rester avec quelqu’un qui ne me demandait rien.

Effets :
```json
{
  "fuite_ines": 3,
  "fatigue_emotionnelle": 1,
  "culpabilite": 1,
  "flags": [
    "ines_fuite_seed"
  ]
}
```

### Réponse Inès

`j1_05_player_006d` Joueur :
J’aurais peut-être préféré rester avec quelqu’un qui ne me demandait rien.

`j1_05_ines_007d` Inès :
Je comprends l’envie.

`j1_05_ines_008d` Inès :
Mais je suis pas sûre d’aimer la place que ça me donne.

`j1_05_ines_009d` Inès :
Une parenthèse, peut-être.

`j1_05_ines_010d` Inès :
Pas un trou dans le mur.

Sortie : `j1_05_exit_fuite_warning`

---

## Choix E — Forcer trop tôt

ID : `j1_05_too_direct`

Texte joueur :
Tu m’as regardé longtemps, alors ? J’aurais dû venir te parler plutôt.

Effets :
```json
{
  "fuite_ines": -2,
  "fatigue_emotionnelle": 2,
  "culpabilite": 1,
  "flags": [
    "sexualized_ines_too_early"
  ]
}
```

### Réponse Inès

`j1_05_player_006e` Joueur :
Tu m’as regardé longtemps, alors ? J’aurais dû venir te parler plutôt.

`j1_05_ines_007e` Inès :
Ah.

`j1_05_ines_008e` Inès :
Je crois que mon message est arrivé au mauvais endroit.

`j1_05_ines_009e` Inès :
Je voulais pas ouvrir cette porte-là.

`j1_05_ines_010e` Inès :
Pas maintenant.

Sortie : `j1_05_exit_ines_closes`

---

## Choix F — Silence

ID : `j1_05_silence`

Texte joueur :
Ne pas répondre.

Effets :
```json
{
  "fuite_ines": -1,
  "flags": [
    "ignored_ines_j1"
  ]
}
```

### Réponse Inès

`j1_05_sys_006f` Système :
Tu ne réponds pas.

`j1_05_ines_007f` Inès :
Pas grave si tu réponds plus tard.

`j1_05_ines_008f` Inès :
Ou pas.

Sortie : `j1_05_exit_ines_fades`

---

# Sorties communes possibles

- `j1_05_exit_soft_opening` : Inès reste une présence douce.
- `j1_05_exit_distance_respected` : la porte reste fermée proprement.
- `j1_05_exit_perception_only` : Inès confirme qu’elle n’a pas de preuve.
- `j1_05_exit_fuite_warning` : Inès perçoit qu’elle peut être utilisée comme fuite.
- `j1_05_exit_ines_closes` : Inès se ferme face à une intimité forcée.
- `j1_05_exit_ines_fades` : Inès peut disparaître du MVP si non nourrie.

---

# Notes de validation

- Inès ne sait rien des faits Camille/Sarah.
- Elle parle depuis la perception, pas depuis l’enquête.
- Elle ne devient pas une route romantique complète.
- La fuite augmente `fuite_ines`, mais n’est pas récompensée sans ambiguïté.
- La sexualisation trop tôt ferme la scène.
