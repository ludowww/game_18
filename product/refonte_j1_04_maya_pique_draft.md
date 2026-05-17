# Double Vie — Refonte J1 — Draft lisible

## Scène : `j1_04_maya_pique`

Statut : draft narratif lisible, non intégré runtime.

Objectif : poser Maya comme regard social : elle voit des timings et des attitudes, pas la vérité complète.

---

## Fonction de la scène

Maya écrit avec une pique. Elle n’accuse pas frontalement. Elle signale qu’elle a remarqué une incohérence : absence, photo, timing, retour bizarre, énergie entre le joueur et Camille.

Elle est la meilleure amie de Sarah, mais pas l’ennemie du joueur.

---

## Connaissances de Maya

Maya sait :

- le joueur et Camille ont été absents ou difficiles à situer ;
- Sarah a senti quelque chose ;
- Nico a donné une explication fragile ;
- le timing est suspect ;
- elle a peut-être une photo ou un souvenir de groupe où il manque deux personnes.

Maya ignore :

- ce qui s’est dit dehors ;
- s’il y a eu contact physique ;
- la version donnée à Sarah ;
- ce que Camille attend vraiment.

---

## Version draft

`j1_04_maya_001` Maya :
je pose ça là : vous êtes fatigants.

`j1_04_maya_002` Maya :
et par “vous” je veux dire “les gens qui disparaissent pile quand je veux faire une photo de groupe”.

`j1_04_maya_003` Maya :
coïncidence sûrement.

`j1_04_maya_004` Maya :
très artistique comme timing.

---

## Choix principal

`j1_04_choice_maya_pique` — Que répondre à Maya ?

---

## Choix A — Jouer l’innocence

ID : `j1_04_play_dumb`

Texte joueur :
Je vois pas de quoi tu parles. J’ai juste dû sortir deux minutes.

Effets :
```json
{
  "suspicion_maya": 2,
  "coherence": -1,
  "risque_exposition": 1,
  "flags": [
    "played_dumb_with_maya",
    "maya_suspicion_seeded_j1"
  ]
}
```

### Réponse Maya

`j1_04_player_005a` Joueur :
Je vois pas de quoi tu parles. J’ai juste dû sortir deux minutes.

`j1_04_maya_006a` Maya :
“deux minutes”, j’adore.

`j1_04_maya_007a` Maya :
les minutes masculines ont vraiment une fiscalité particulière.

`j1_04_maya_008a` Maya :
je vais faire semblant de ne pas avoir noté.

`j1_04_maya_009a` Maya :
mais je note.

Sortie : `j1_04_exit_maya_suspicious`

---

## Choix B — Dire besoin d’air

ID : `j1_04_needed_air`

Texte joueur :
J’avais besoin d’air. J’ai pas géré le timing, c’est vrai.

Effets :
```json
{
  "suspicion_maya": -1,
  "coherence": 1,
  "fatigue_emotionnelle": 1,
  "flags": [
    "told_maya_needed_air",
    "maya_timing_noted"
  ]
}
```

### Réponse Maya

`j1_04_player_005b` Joueur :
J’avais besoin d’air. J’ai pas géré le timing, c’est vrai.

`j1_04_maya_006b` Maya :
ok. ça, c’est une phrase qui ressemble presque à une vraie phrase.

`j1_04_maya_007b` Maya :
je peux entendre “j’avais besoin d’air”.

`j1_04_maya_008b` Maya :
je peux moins entendre les gens qui essayent ensuite de faire croire que personne n’a vu la porte s’ouvrir.

Sortie : `j1_04_exit_maya_prudent`

---

## Choix C — Demander ce qu’elle a vu

ID : `j1_04_ask_what_saw`

Texte joueur :
Qu’est-ce que t’as vu exactement ?

Effets :
```json
{
  "suspicion_maya": 1,
  "risque_exposition": 1,
  "fatigue_emotionnelle": 1,
  "flags": [
    "asked_maya_what_she_saw",
    "maya_photo_possible"
  ]
}
```

### Réponse Maya

`j1_04_player_005c` Joueur :
Qu’est-ce que t’as vu exactement ?

`j1_04_maya_006c` Maya :
intéressant comme première question.

`j1_04_maya_007c` Maya :
pas “ça va Sarah ?”, pas “j’ai été bizarre ?”.

`j1_04_maya_008c` Maya :
mais “quel est le périmètre des dégâts visibles ?”.

`j1_04_maya_009c` Maya :
j’ai une photo où il manque deux personnes. pour commencer.

Sortie : `j1_04_exit_photo_seeded`

---

## Choix D — Lui dire de ne pas s’en mêler

ID : `j1_04_not_involve`

Texte joueur :
Maya, te mêle pas de ça. S’il y a un truc à dire à Sarah, je le ferai.

Effets :
```json
{
  "suspicion_maya": 3,
  "risque_exposition": 2,
  "coherence": -1,
  "flags": [
    "told_maya_not_involve"
  ]
}
```

### Réponse Maya

`j1_04_player_005d` Joueur :
Maya, te mêle pas de ça. S’il y a un truc à dire à Sarah, je le ferai.

`j1_04_maya_006d` Maya :
ah.

`j1_04_maya_007d` Maya :
le fameux “ne t’en mêle pas” adressé à la meilleure amie de la personne qui a mal dormi à côté de toi.

`j1_04_maya_008d` Maya :
je veux pas être mêlée.

`j1_04_maya_009d` Maya :
mais j’ai des yeux. et Sarah aussi, accessoirement.

Sortie : `j1_04_exit_maya_defensive`

---

## Choix E — Répondre par humour

ID : `j1_04_joke`

Texte joueur :
Tu surveilles les photos de groupe comme une gardienne de musée, c’est inquiétant.

Effets :
```json
{
  "suspicion_maya": 1,
  "fatigue_emotionnelle": -1,
  "flags": [
    "joked_with_maya_j1"
  ]
}
```

### Réponse Maya

`j1_04_player_005e` Joueur :
Tu surveilles les photos de groupe comme une gardienne de musée, c’est inquiétant.

`j1_04_maya_006e` Maya :
je protège le patrimoine national : mes soirées ratées.

`j1_04_maya_007e` Maya :
mais joli détour.

`j1_04_maya_008e` Maya :
je te donne 6/10 pour l’humour et 2/10 pour la discrétion.

Sortie : `j1_04_exit_joke_noted`

---

## Choix F — Silence

ID : `j1_04_silence`

Texte joueur :
Ne pas répondre.

Effets :
```json
{
  "suspicion_maya": 2,
  "risque_exposition": 1,
  "flags": [
    "ignored_maya_j1",
    "maya_suspicion_seeded_j1"
  ]
}
```

### Réponse Maya

`j1_04_sys_005f` Système :
Tu laisses Maya en vu.

`j1_04_maya_006f` Maya :
vu.

`j1_04_maya_007f` Maya :
littéralement et conceptuellement, du coup.

Sortie : `j1_04_exit_silence_noted`

---

# Sorties communes possibles

- `j1_04_exit_maya_suspicious` : Maya augmente son niveau d’alerte.
- `j1_04_exit_maya_prudent` : Maya reste piquante mais moins hostile.
- `j1_04_exit_photo_seeded` : la photo devient une trace possible.
- `j1_04_exit_maya_defensive` : Maya se rapproche de Sarah par protection.
- `j1_04_exit_joke_noted` : l’humour respire mais ne masque pas tout.
- `j1_04_exit_silence_noted` : Maya enregistre l’évitement.

---

# Notes de validation

- Maya n’est pas omnisciente.
- Elle voit des traces sociales, pas l’intimité.
- Elle protège Sarah sans être ennemie du joueur.
- Les réponses trop défensives augmentent `suspicion_maya` et `risque_exposition`.
- La photo reste une possibilité, pas une preuve totale.
