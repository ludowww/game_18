# Double Vie — Refonte J1 — Draft lisible

## Scène : `j1_07_nico_vanne_soiree`

Statut : draft narratif lisible, non intégré runtime.

Objectif : respiration amicale avec Nico, sans annuler le danger. Nico fait rire, puis rappelle la limite.

---

## Fonction de la scène

Nico envoie une vanne ou un prétexte léger en fin de journée. La scène permet de respirer après les tensions Sarah/Camille/Maya/Inès, mais elle garde le thème de l’alibi et de l’amitié sous pression.

---

## Version draft

`j1_07_nico_001` Nico :
je t’ai envoyé un meme.

`j1_07_nico_002` Nico :
c’est thérapeutique, dis merci.

`j1_07_nico_003` Nico :
aussi j’ai faim, mais je refuse de commander seul comme un homme abandonné par la République.

`j1_07_nico_004` Nico :
pizza ou tu continues ton régime “angoisse et mauvaises décisions” ?

---

## Choix principal

`j1_07_choice_nico_respiration` — Que répondre à Nico ?

---

## Choix A — Accepter la respiration

ID : `j1_07_share_joke`

Texte joueur :
Pizza. Et ton meme est nul, donc oui, il m’a aidé.

Effets :
```json
{
  "fatigue_emotionnelle": -1,
  "dette_nico": -1,
  "flags": [
    "nico_j1_respiration_shared"
  ]
}
```

### Réponse Nico

`j1_07_player_005a` Joueur :
Pizza. Et ton meme est nul, donc oui, il m’a aidé.

`j1_07_nico_006a` Nico :
mes memes sont un service public.

`j1_07_nico_007a` Nico :
je note que monsieur revient parmi les vivants.

`j1_07_nico_008a` Nico :
ça règle rien, mais ça évite que tu deviennes une plante verte coupable.

Sortie : `j1_07_exit_friendship_breathes`

---

## Choix B — Demander conseil sincèrement

ID : `j1_07_ask_real_advice`

Texte joueur :
J’ai besoin d’un vrai conseil, sans vanne deux secondes. Je fais quoi si je sais même pas quelle vérité dire ?

Effets :
```json
{
  "coherence": 1,
  "dette_nico": -1,
  "fatigue_emotionnelle": -1,
  "flags": [
    "asked_nico_real_advice_j1"
  ]
}
```

### Réponse Nico

`j1_07_player_005b` Joueur :
J’ai besoin d’un vrai conseil, sans vanne deux secondes. Je fais quoi si je sais même pas quelle vérité dire ?

`j1_07_nico_006b` Nico :
Ok. Sans vanne deux secondes, ce qui me coûte personnellement.

`j1_07_nico_007b` Nico :
Tu commences par dire ce que tu sais sûr.

`j1_07_nico_008b` Nico :
Pas ce qui t’arrange. Pas ce qui minimise. Ce que tu sais sûr.

`j1_07_nico_009b` Nico :
Après tu dis que le reste est flou. Mais tu vends pas le flou comme une vérité.

Sortie : `j1_07_exit_real_advice`

---

## Choix C — Redemander une couverture

ID : `j1_07_second_cover`

Texte joueur :
Si jamais Sarah ou Maya te relance, tu peux juste rester sur la même version ?

Effets :
```json
{
  "dette_nico": 3,
  "risque_exposition": 1,
  "fatigue_emotionnelle": 1,
  "flags": [
    "asked_nico_second_cover_j1"
  ]
}
```

### Réponse Nico

`j1_07_player_005c` Joueur :
Si jamais Sarah ou Maya te relance, tu peux juste rester sur la même version ?

`j1_07_nico_006c` Nico :
et voilà, la pizza du mensonge revient sur la table.

`j1_07_nico_007c` Nico :
Je vais pas changer ce que j’ai déjà dit.

`j1_07_nico_008c` Nico :
Mais je vais pas ajouter des DLC à ton alibi non plus.

`j1_07_nico_009c` Nico :
Tu m’as demandé un pansement. Là tu me demandes une mutuelle.

Sortie : `j1_07_exit_debt_grows`

---

## Choix D — Éviter par humour

ID : `j1_07_joke_avoid`

Texte joueur :
Le régime angoisse fonctionne très bien, j’ai déjà perdu deux ans d’espérance de vie.

Effets :
```json
{
  "fatigue_emotionnelle": 1,
  "flags": [
    "joked_to_avoid_nico_j1"
  ]
}
```

### Réponse Nico

`j1_07_player_005d` Joueur :
Le régime angoisse fonctionne très bien, j’ai déjà perdu deux ans d’espérance de vie.

`j1_07_nico_006d` Nico :
bon score, mais peut mieux faire.

`j1_07_nico_007d` Nico :
Je te connais : quand tu fais trop de blagues, c’est que tu caches les vraies dans un placard.

`j1_07_nico_008d` Nico :
Mange un truc. Et arrête de transformer ton téléphone en tribunal portable.

Sortie : `j1_07_exit_joke_soft_warning`

---

## Choix E — Silence

ID : `j1_07_silence`

Texte joueur :
Ne pas répondre.

Effets :
```json
{
  "dette_nico": 1,
  "fatigue_emotionnelle": 1,
  "flags": [
    "ignored_nico_respiration_j1"
  ]
}
```

### Réponse Nico

`j1_07_sys_005e` Système :
Tu ne réponds pas.

`j1_07_nico_006e` Nico :
ok donc même mon meme est en attente de procès

`j1_07_nico_007e` Nico :
respire quand même, idiot.

Sortie : `j1_07_exit_friend_waits`

---

# Notes de validation

- Nico sert de respiration sans effacer les conséquences.
- Les demandes répétées d’alibi augmentent `dette_nico`.
- Le conseil sincère améliore `coherence`.
- Le ton reste amical/oral.
- Nico ne devient pas un tutoriel pur : il parle comme un ami.
