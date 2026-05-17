# Double Vie — Refonte J1 — Draft lisible

## Scène : `j1_03_nico_couverture`

Statut : draft narratif lisible, non intégré runtime.

Objectif : poser Nico comme ami loyal, drôle, mais limité. Il a couvert un blanc, pas signé pour porter une double vie.

---

## Fonction de la scène

Nico rappelle qu’il a improvisé une explication pendant la soirée. Il veut savoir s’il doit tenir une version, rester vague, ou si le joueur va enfin lui dire ce qu’il couvre vraiment.

Nico n’est pas un outil. Il peut aider, mais chaque demande crée une dette.

---

## Connaissances de Nico

Nico sait :

- qu’il a donné une explication floue pendant la soirée ;
- que le joueur était troublé par Camille ;
- que Sarah ou Maya pourraient lui poser des questions ;
- que son explication peut devenir fragile.

Nico ignore :

- ce qui s’est réellement passé dehors ;
- ce que le joueur a dit à Sarah ;
- ce que Camille attend ;
- ce que Maya a vu précisément.

---

## Version draft

`j1_03_nico_001` Nico :
frérot j’ai fait ce que j’ai pu mais ton histoire sent le plan claqué

`j1_03_nico_002` Nico :
Et je dis ça avec amour.

`j1_03_nico_003` Nico :
Enfin avec amour et une petite envie de changer d’identité si Sarah me demande des détails.

`j1_03_nico_004` Nico :
Tu veux que je sache quelle version, exactement ?

---

## Choix principal

`j1_03_choice_nico_version` — Que demander à Nico ?

---

## Choix A — Demander de tenir une version

ID : `j1_03_hold_version`

Texte joueur :
Si on te demande, dis juste qu’on était ensemble dehors un moment. Rien de plus.

Effets :
```json
{
  "dette_nico": 4,
  "coherence": -1,
  "risque_exposition": 2,
  "fatigue_emotionnelle": 1,
  "flags": [
    "asked_nico_hold_version",
    "nico_alibi_requested"
  ]
}
```

### Réponse Nico

`j1_03_player_005a` Joueur :
Si on te demande, dis juste qu’on était ensemble dehors un moment. Rien de plus.

`j1_03_nico_006a` Nico :
Ah oui. Donc je passe de figurant inquiet à coproducteur du mensonge.

`j1_03_nico_007a` Nico :
Je peux dire que t’étais sorti prendre l’air.

`j1_03_nico_008a` Nico :
Mais “ensemble un moment”, ça commence à mettre mes chaussures dans ta boue.

`j1_03_nico_009a` Nico :
Je te couvre pour un blanc. Pas pour une saison complète.

Sortie : `j1_03_exit_alibi_debt`

---

## Choix B — Lui dire de rester vague

ID : `j1_03_stay_silent`

Texte joueur :
Dis rien de plus. Si on te demande, reste vague. Je vais gérer.

Effets :
```json
{
  "dette_nico": 1,
  "coherence": 1,
  "fatigue_emotionnelle": 1,
  "flags": [
    "told_nico_stay_silent"
  ]
}
```

### Réponse Nico

`j1_03_player_005b` Joueur :
Dis rien de plus. Si on te demande, reste vague. Je vais gérer.

`j1_03_nico_006b` Nico :
“Je vais gérer”, phrase préférée des gens qui ne gèrent absolument pas.

`j1_03_nico_007b` Nico :
Mais ok.

`j1_03_nico_008b` Nico :
Je brode pas. Je rajoute pas de décoration. Je fais le mur blanc.

`j1_03_nico_009b` Nico :
Par contre faudra vraiment que tu gères, du coup. Concept audacieux.

Sortie : `j1_03_exit_vague_support`

---

## Choix C — Avouer le trouble avec Camille

ID : `j1_03_confess_camille`

Texte joueur :
Camille m’a rejoint dehors. Il s’est rien passé de clair, mais c’était pas neutre. Je sais pas quoi faire de ça.

Effets :
```json
{
  "dette_nico": -1,
  "coherence": 2,
  "culpabilite": 1,
  "fatigue_emotionnelle": -1,
  "flags": [
    "confessed_camille_to_nico",
    "vulnerable_to_nico"
  ]
}
```

### Réponse Nico

`j1_03_player_005c` Joueur :
Camille m’a rejoint dehors. Il s’est rien passé de clair, mais c’était pas neutre. Je sais pas quoi faire de ça.

`j1_03_nico_006c` Nico :
Ok.

`j1_03_nico_007c` Nico :
Déjà merci de pas me faire jouer à devine-la-catastrophe.

`j1_03_nico_008c` Nico :
Là t’as pas besoin d’un alibi, t’as besoin d’arrêter de faire comme si le flou allait t’élever tout seul.

`j1_03_nico_009c` Nico :
Je peux t’aider à respirer. Pas à mentir mieux.

Sortie : `j1_03_exit_confession_support`

---

## Choix D — Éviter par humour

ID : `j1_03_joke_avoid`

Texte joueur :
Tu dramatises. T’as toujours rêvé d’être personnage secondaire dans une série nulle.

Effets :
```json
{
  "dette_nico": 1,
  "fatigue_emotionnelle": 1,
  "coherence": -1,
  "flags": [
    "joked_with_nico_to_avoid"
  ]
}
```

### Réponse Nico

`j1_03_player_005d` Joueur :
Tu dramatises. T’as toujours rêvé d’être personnage secondaire dans une série nulle.

`j1_03_nico_006d` Nico :
Oui mais dans mes rêves j’avais de meilleures fringues et moins de culpabilité par association.

`j1_03_nico_007d` Nico :
Je rigole, mais fais pas le magicien avec moi.

`j1_03_nico_008d` Nico :
Si tu veux pas me dire, dis-le.

`j1_03_nico_009d` Nico :
Mais me fais pas couvrir un truc que tu refuses même de nommer.

Sortie : `j1_03_exit_joke_warning`

---

## Choix E — Rembarrer Nico

ID : `j1_03_dismiss_warning`

Texte joueur :
Laisse tomber. T’en fais trop. Si quelqu’un demande, dis juste que tu sais pas.

Effets :
```json
{
  "dette_nico": 2,
  "coherence": -1,
  "fatigue_emotionnelle": 2,
  "risque_exposition": 1,
  "flags": [
    "dismissed_nico_warning"
  ]
}
```

### Réponse Nico

`j1_03_player_005e` Joueur :
Laisse tomber. T’en fais trop. Si quelqu’un demande, dis juste que tu sais pas.

`j1_03_nico_006e` Nico :
Ah, parfait. Je suis donc assez impliqué pour servir, mais pas assez pour comprendre.

`j1_03_nico_007e` Nico :
Je vais faire simple alors.

`j1_03_nico_008e` Nico :
Si on me demande un truc précis, je vais pas inventer.

`j1_03_nico_009e` Nico :
Je peux pas te sauver de toi-même si tu m’envoies aussi balader.

Sortie : `j1_03_exit_nico_hurt`

---

# Sorties communes possibles

- `j1_03_exit_alibi_debt` : Nico accepte partiellement, mais dette forte.
- `j1_03_exit_vague_support` : Nico reste allié prudent.
- `j1_03_exit_confession_support` : Nico soutient sans mentir davantage.
- `j1_03_exit_joke_warning` : Nico voit l’esquive.
- `j1_03_exit_nico_hurt` : Nico pose une limite plus froide.

---

# Notes de validation

- Nico ne sait pas exactement ce qui s’est passé dehors sauf si le joueur lui dit.
- Nico reste drôle, mais pas disponible à l’infini.
- Demander un alibi augmente bien `dette_nico`.
- La confession réduit la dette et augmente la cohérence.
- Nico n’est ni tutoriel ni sauveur magique.
