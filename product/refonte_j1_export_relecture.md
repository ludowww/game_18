# Double Vie — Refonte J1 V2 — Export de relecture

Statut : export consolidé lisible, non intégré runtime.

But : relire la nouvelle journée 1 avant conversion JSON Godot.

Sources : drafts `product/refonte_j1_XX_*_draft.md`.

Runtime Godot actif inchangé.


---

## Instructions de relecture

Pour chaque correction, noter :

```text
Scène :
ID ligne/node :
Problème : incompréhensible / trop long / pas naturel / mauvais ton / effet discutable
Suggestion :
```


Points à surveiller :

- chaque personnage a-t-il une voix reconnaissable ?

- la scène est-elle claire sans être explicative ?

- les choix donnent-ils envie de jouer ?

- Sarah n’est-elle pas trop enquêtrice ?

- Camille reste-t-elle respectée, pas récompense ?

- Maya observe-t-elle sans omniscience ?

- Nico reste-t-il ami, pas bouton alibi ?

- Inès reste-t-elle une fuite douce, pas route complète ?


---


# 00 — Réveil messages


Source : `/opt/data/profiles/game_18/product/refonte_j1_00_reveil_messages_draft.md`


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


---


# 01 — Sarah / absence


Source : `/opt/data/profiles/game_18/product/refonte_j1_01_sarah_absence_draft.md`


# Version draft

## Entrée commune

`j1_01_sarah_001` Sarah :
T’es réveillé ?

`j1_01_sarah_002` Sarah :
Je voulais pas commencer la journée comme ça.

`j1_01_sarah_003` Sarah :
Mais hier, quand t’es revenu, j’ai eu l’impression que t’étais encore dehors.

`j1_01_sarah_004` Sarah :
Je sais pas comment le dire autrement.

`j1_01_sarah_005` Sarah :
Tu étais où, exactement ?

---

## Choix principal

`j1_01_choice_version_sarah` — Que répondre à Sarah ?

---

## Choix A — Besoin d’air

ID : `j1_01_needed_air`

Texte joueur :
J’avais besoin d’air. Je suis sorti un moment, c’est vrai. J’aurais dû te le dire.

Effets :
```json
{
  "confiance_sarah": 1,
  "distance_sarah": -1,
  "coherence": 2,
  "culpabilite": 1,
  "flags": [
    "said_needed_air_to_sarah",
    "sarah_version_needed_air"
  ]
}
```

Suite : `j1_01_needed_air_response`

### Réponse Sarah

`j1_01_player_006a` Joueur :
J’avais besoin d’air. Je suis sorti un moment, c’est vrai. J’aurais dû te le dire.

`j1_01_sarah_007a` Sarah :
D’accord.

`j1_01_sarah_008a` Sarah :
Ça, je peux l’entendre.

`j1_01_sarah_009a` Sarah :
Ce que j’ai moins compris, c’est pourquoi t’es revenu comme si je venais de rater une partie de toi.

`j1_01_sarah_010a` Sarah :
Je te demande pas un rapport minute par minute. Juste de pas me laisser deviner toute seule.

Sortie : `j1_01_exit_fragile_open`

Intention :
Version partielle mais crédible. Sarah reste inquiète, mais ne se ferme pas.

---

## Choix B — Alibi Nico

ID : `j1_01_nico_alibi`

Texte joueur :
J’étais avec Nico une partie du temps. On a parlé dehors, c’est tout.

Effets :
```json
{
  "confiance_sarah": -1,
  "distance_sarah": 1,
  "dette_nico": 3,
  "coherence": -2,
  "risque_exposition": 2,
  "flags": [
    "used_nico_alibi_sarah",
    "sarah_version_nico"
  ]
}
```

Suite : `j1_01_nico_alibi_response`

### Réponse Sarah

`j1_01_player_006b` Joueur :
J’étais avec Nico une partie du temps. On a parlé dehors, c’est tout.

`j1_01_sarah_007b` Sarah :
Nico m’a dit que t’étais sorti deux minutes.

`j1_01_sarah_008b` Sarah :
Là tu me dis “une partie du temps”.

`j1_01_sarah_009b` Sarah :
C’est peut-être rien. Mais ça bouge déjà un peu, ta phrase.

`j1_01_sarah_010b` Sarah :
Je veux pas avoir besoin de comparer ce que les gens me disent.

Sortie : `j1_01_exit_version_fragile`

Intention :
Le joueur cherche à stabiliser par Nico, mais crée une première contradiction exploitable plus tard.

---

## Choix C — Camille minimisée

ID : `j1_01_camille_minimized`

Texte joueur :
J’ai croisé Camille dehors, oui. Mais c’était juste une discussion, rien de plus.

Effets :
```json
{
  "confiance_sarah": -2,
  "distance_sarah": 2,
  "coherence": -1,
  "culpabilite": 2,
  "risque_exposition": 1,
  "flags": [
    "mentioned_camille_to_sarah",
    "minimized_camille_to_sarah",
    "sarah_version_camille_minimized"
  ]
}
```

Suite : `j1_01_camille_minimized_response`

### Réponse Sarah

`j1_01_player_006c` Joueur :
J’ai croisé Camille dehors, oui. Mais c’était juste une discussion, rien de plus.

`j1_01_sarah_007c` Sarah :
Je crois que c’est le “juste” qui me fatigue.

`j1_01_sarah_008c` Sarah :
Pas parce que j’ai une preuve ou je sais pas quoi.

`j1_01_sarah_009c` Sarah :
Parce que tu l’as dit comme quand tu veux poser un couvercle sur quelque chose qui déborde.

`j1_01_sarah_010c` Sarah :
Si c’était rien, pourquoi j’ai eu l’impression que tu faisais attention à chaque mot ?

Sortie : `j1_01_exit_sarah_doubts`

Intention :
Le joueur donne une information importante, mais en la minimisant. Sarah ne sait pas plus, mais elle sent l’esquive.

---

## Choix D — Vulnérabilité partielle

ID : `j1_01_vulnerable`

Texte joueur :
Je sais pas bien. Je suis sorti parce que j’étais pas bien. Et quand je suis revenu, j’ai pas réussi à revenir vraiment.

Effets :
```json
{
  "confiance_sarah": 2,
  "distance_sarah": -1,
  "coherence": 1,
  "culpabilite": 2,
  "fatigue_emotionnelle": 1,
  "flags": [
    "vulnerable_to_sarah",
    "sarah_version_emotional_confusion"
  ]
}
```

Suite : `j1_01_vulnerable_response`

### Réponse Sarah

`j1_01_player_006d` Joueur :
Je sais pas bien. Je suis sorti parce que j’étais pas bien. Et quand je suis revenu, j’ai pas réussi à revenir vraiment.

`j1_01_sarah_007d` Sarah :
Merci de le dire comme ça.

`j1_01_sarah_008d` Sarah :
Ça me rassure pas complètement.

`j1_01_sarah_009d` Sarah :
Mais au moins j’ai pas l’impression que tu me demandes de faire semblant de rien sentir.

`j1_01_sarah_010d` Sarah :
Je peux entendre que tu sois perdu. Je peux moins entendre que tu me laisses seule avec ça.

Sortie : `j1_01_exit_fragile_open`

Intention :
Le joueur ne dit pas tout, mais reconnaît un état intérieur. Sarah reste blessée mais dans l’échange.

---

## Choix E — Silence / réponse tardive

ID : `j1_01_silence`

Texte joueur :
Ne pas répondre maintenant.

Effets :
```json
{
  "confiance_sarah": -2,
  "distance_sarah": 3,
  "fatigue_emotionnelle": 1,
  "culpabilite": 1,
  "flags": [
    "ignored_sarah_j1",
    "sarah_no_clear_version_j1"
  ]
}
```

Suite : `j1_01_silence_response`

### Réponse Sarah

`j1_01_sys_006e` Système :
Tu laisses le message ouvert.

`j1_01_sys_007e` Système :
La bulle ne bouge plus. Mais la conversation, elle, continue ailleurs.

`j1_01_sarah_008e` Sarah :
Ok.

`j1_01_sarah_009e` Sarah :
Je vais prendre ça comme une réponse pour l’instant.

Sortie : `j1_01_exit_no_clear_version`

Intention :
Le silence pose une première absence de version. Ce n’est pas neutre et doit peser sur la suite.

---

# Sorties communes possibles

## `j1_01_exit_fragile_open`

Sarah reste inquiète mais ouverte.
Peut débloquer plus facilement `j1_06_sarah_rentrer_manger` avec une tonalité douce.

Flags possibles en aval :
- `sarah_open_to_domestic_scene_j1`

## `j1_01_exit_version_fragile`

Sarah ne se ferme pas totalement, mais une incohérence existe déjà.
Nico devient plus exposé.

Flags possibles en aval :
- `sarah_noted_nico_inconsistency_j1`

## `j1_01_exit_sarah_doubts`

Sarah sait que Camille est dans la version, mais sent que le joueur réduit quelque chose.
Camille pourra réagir plus fort si le joueur minimise aussi auprès d’elle.

Flags possibles en aval :
- `sarah_knows_camille_was_outside_j1`

## `j1_01_exit_no_clear_version`

Sarah n’a aucune réponse claire.
La distance augmente et les scènes domestiques doivent devenir plus froides.

Flags possibles en aval :
- `sarah_waits_without_answer_j1`

---

# Notes de validation

- Sarah ne sait pas ce qui s’est passé dehors.
- Elle ne formule jamais d’accusation d’infidélité ou équivalent.
- Elle part de son ressenti concret : retour, absence, phrase qui bouge, impression d’être seule avec son malaise.
- Les choix fixent bien des versions différentes.
- Le silence est traité comme une action.
- La scène peut nourrir J2 : versions, Nico, Camille, cohérence.

---

# Notes pour conversion JSON Godot

Format recommandé : nodes plats.

Start node : `j1_01_sarah_001`

Choice node : `j1_01_choice_version_sarah`

End nodes possibles :

- `j1_01_end_fragile_open`
- `j1_01_end_version_fragile`
- `j1_01_end_sarah_doubts`
- `j1_01_end_no_clear_version`

À la conversion, chaque sortie peut être un node `end` avec un court message système ou un `next` vers une attente de bloc.


---


# 02 — Camille / dehors


Source : `/opt/data/profiles/game_18/product/refonte_j1_02_camille_dehors_draft.md`


# Version draft

## Entrée commune

`j1_02_camille_001` Camille :
Je crois qu’on a été moins discrets qu’on pensait.

`j1_02_camille_002` Camille :
Ou alors tout le monde a poliment décidé de devenir aveugle pendant vingt minutes.

`j1_02_camille_003` Camille :
Je ne sais pas quelle option est la plus confortable.

`j1_02_camille_004` Camille :
Tu vas faire comme si c’était juste une discussion dehors ?

---

## Choix principal

`j1_02_choice_camille_dehors` — Que répondre à Camille ?

---

## Choix A — Assumer le trouble

ID : `j1_02_admit_tension`

Texte joueur :
Non. C’était pas juste une discussion. Je sais pas encore quoi en faire, mais je vais pas te dire que c’était rien.

Effets :
```json
{
  "tension_camille": 2,
  "respect_camille": 1,
  "coherence": 1,
  "culpabilite": 2,
  "flags": [
    "admitted_tension_to_camille",
    "camille_trouble_acknowledged"
  ]
}
```

Suite : `j1_02_admit_tension_response`

### Réponse Camille

`j1_02_player_005a` Joueur :
Non. C’était pas juste une discussion. Je sais pas encore quoi en faire, mais je vais pas te dire que c’était rien.

`j1_02_camille_006a` Camille :
C’est déjà plus honnête que “on prenait l’air”.

`j1_02_camille_007a` Camille :
Je ne te demande pas de savoir quoi en faire ce matin.

`j1_02_camille_008a` Camille :
Je te demande juste de ne pas me laisser seule avec la version exacte de ce qui s’est passé.

`j1_02_camille_009a` Camille :
Même si cette version tient mal debout.

Sortie : `j1_02_exit_trouble_acknowledged`

Intention :
Le joueur reconnaît le trouble sans promettre une route. Camille reste prudente mais ouverte.

---

## Choix B — Poser une limite respectueuse

ID : `j1_02_respect_boundary`

Texte joueur :
Je veux pas faire comme si c’était rien. Mais je peux pas te demander de porter ça pendant que je ne suis pas clair avec Sarah.

Effets :
```json
{
  "tension_camille": -1,
  "respect_camille": 3,
  "pression_camille": -2,
  "coherence": 2,
  "culpabilite": 1,
  "flags": [
    "protected_camille_boundary",
    "camille_boundary_respected"
  ]
}
```

Suite : `j1_02_respect_boundary_response`

### Réponse Camille

`j1_02_player_005b` Joueur :
Je veux pas faire comme si c’était rien. Mais je peux pas te demander de porter ça pendant que je ne suis pas clair avec Sarah.

`j1_02_camille_006b` Camille :
Je ne sais pas si c’est lâche ou prudent.

`j1_02_camille_007b` Camille :
Mais au moins tu ne me déguises pas en pause dans ta journée.

`j1_02_camille_008b` Camille :
Ça ne rend pas hier plus simple.

`j1_02_camille_009b` Camille :
Ça le rend juste un peu moins sale.

Sortie : `j1_02_exit_boundary_respected`

Intention :
Le joueur baisse la tension immédiate mais augmente le respect. Camille n’est pas utilisée comme refuge.

---

## Choix C — Minimiser

ID : `j1_02_minimize`

Texte joueur :
Camille, on a parlé dehors. C’est tout. On va pas transformer ça en drame.

Effets :
```json
{
  "tension_camille": -1,
  "respect_camille": -3,
  "pression_camille": 1,
  "coherence": -1,
  "culpabilite": 1,
  "flags": [
    "minimized_with_camille",
    "camille_minimized_j1"
  ]
}
```

Suite : `j1_02_minimize_response`

### Réponse Camille

`j1_02_player_005c` Joueur :
Camille, on a parlé dehors. C’est tout. On va pas transformer ça en drame.

`j1_02_camille_006c` Camille :
Je note le détour.

`j1_02_camille_007c` Camille :
Et le “on”, très généreux.

`j1_02_camille_008c` Camille :
Tu peux appeler ça une discussion si ça t’aide à dormir.

`j1_02_camille_009c` Camille :
Ne me demande juste pas de jouer dans la même version.

Sortie : `j1_02_exit_camille_cold`

Intention :
Le joueur tente de réduire le moment. Camille se ferme sans exploser.

---

## Choix D — Désir trop direct

ID : `j1_02_early_desire`

Texte joueur :
Je pensais surtout à toi ce matin. Au moment dehors. À ce que j’aurais peut-être dû faire.

Effets :
```json
{
  "tension_camille": 2,
  "respect_camille": -3,
  "pression_camille": 3,
  "culpabilite": 2,
  "fatigue_emotionnelle": 1,
  "flags": [
    "early_desire_to_camille",
    "camille_desire_too_early_j1"
  ]
}
```

Suite : `j1_02_early_desire_response`

### Réponse Camille

`j1_02_player_005d` Joueur :
Je pensais surtout à toi ce matin. Au moment dehors. À ce que j’aurais peut-être dû faire.

`j1_02_camille_006d` Camille :
Tu vois, c’est exactement là que ça devient pratique pour toi.

`j1_02_camille_007d` Camille :
Tu sautes la partie où tu regardes ce que ça abîme.

`j1_02_camille_008d` Camille :
Et tu arrives directement à celle où je deviens une idée agréable.

`j1_02_camille_009d` Camille :
Je ne veux pas être ton endroit où respirer quand le reste t’étouffe.

Sortie : `j1_02_exit_pressure_too_high`

Intention :
Le désir augmente la tension mais abîme le respect. Camille pose une limite forte.

---

## Choix E — Incertitude honnête

ID : `j1_02_uncertain`

Texte joueur :
Je sais pas ce que c’était. Je sais juste que ça m’a déplacé. Et que j’ai peur de répondre à côté.

Effets :
```json
{
  "tension_camille": 1,
  "respect_camille": 1,
  "coherence": 1,
  "culpabilite": 2,
  "fatigue_emotionnelle": 1,
  "flags": [
    "uncertain_with_camille",
    "camille_trouble_acknowledged"
  ]
}
```

Suite : `j1_02_uncertain_response`

### Réponse Camille

`j1_02_player_005e` Joueur :
Je sais pas ce que c’était. Je sais juste que ça m’a déplacé. Et que j’ai peur de répondre à côté.

`j1_02_camille_006e` Camille :
Ça sonnait presque vrai.

`j1_02_camille_007e` Camille :
Je dis presque parce que tu as cette façon de garder une porte ouverte derrière chaque phrase.

`j1_02_camille_008e` Camille :
Mais je préfère ça à quelqu’un qui me raconte qu’il faisait juste frais dehors.

Sortie : `j1_02_exit_uncertain_open`

Intention :
Le joueur reconnaît une confusion sans clarifier. Camille reste lucide, ni dupe ni fermée.

---

## Choix F — Silence / vu

ID : `j1_02_silence`

Texte joueur :
Laisser le message ouvert sans répondre.

Effets :
```json
{
  "tension_camille": -2,
  "respect_camille": -1,
  "fatigue_emotionnelle": 1,
  "culpabilite": 1,
  "flags": [
    "ignored_camille_j1",
    "camille_left_on_read_j1"
  ]
}
```

Suite : `j1_02_silence_response`

### Réponse Camille

`j1_02_sys_005f` Système :
Le message reste ouvert.

`j1_02_sys_006f` Système :
Camille écrit. S’arrête. Réécrit.

`j1_02_camille_007f` Camille :
D’accord.

`j1_02_camille_008f` Camille :
Je vais prendre ton silence pour ce qu’il est, alors.

Sortie : `j1_02_exit_camille_left_on_read`

Intention :
Le silence devient un choix actif. Camille n’a pas besoin d’une dispute pour comprendre l’évitement.

---

# Sorties communes possibles

## `j1_02_exit_trouble_acknowledged`

Camille reste prudente mais disponible à une parole plus honnête.
La tension existe, avec un minimum de respect.

Flags possibles en aval :
- `camille_available_if_coherent_j1`

## `j1_02_exit_boundary_respected`

Camille respecte la limite, même si elle peut être frustrée.
Le joueur n’utilise pas Camille comme refuge immédiat.

Flags possibles en aval :
- `camille_respects_player_boundary_j1`

## `j1_02_exit_camille_cold`

Camille détecte la minimisation.
Elle ne se retire pas forcément du jeu, mais elle devient plus coupante.

Flags possibles en aval :
- `camille_not_duped_by_minimization_j1`

## `j1_02_exit_pressure_too_high`

Camille sent qu’elle devient une échappatoire désirante.
Cela prépare une limite forte si le comportement se répète.

Flags possibles en aval :
- `camille_refuge_warning_j1`

## `j1_02_exit_uncertain_open`

Camille accepte l’incertitude, mais surveille les détours.

Flags possibles en aval :
- `camille_accepts_uncertainty_j1`

## `j1_02_exit_camille_left_on_read`

Camille est laissée seule avec la version du moment dehors.
La confiance relationnelle baisse.

Flags possibles en aval :
- `camille_silence_registered_j1`

---

# Notes de validation

- Camille sait uniquement ce qu’elle a vécu avec le joueur dehors.
- Elle ne sait pas ce que Sarah sait ou a dit.
- Elle n’est pas jalouse de Sarah : elle refuse surtout d’être utilisée.
- La scène sépare correctement tension, respect et pression.
- Le désir direct n’est pas récompensé mécaniquement.
- Le silence est traité comme une action.
- Les choix préparent des conséquences futures sans ouvrir une route romantique complète dès J1.

---

# Notes pour conversion JSON Godot

Format recommandé : nodes plats.

Start node : `j1_02_camille_001`

Choice node : `j1_02_choice_camille_dehors`

End nodes possibles :

- `j1_02_end_trouble_acknowledged`
- `j1_02_end_boundary_respected`
- `j1_02_end_camille_cold`
- `j1_02_end_pressure_too_high`
- `j1_02_end_uncertain_open`
- `j1_02_end_camille_left_on_read`

À la conversion, certaines sorties pourront être regroupées si on veut éviter trop de branches runtime.


---


# 03 — Nico / couverture


Source : `/opt/data/profiles/game_18/product/refonte_j1_03_nico_couverture_draft.md`


# Version draft

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


---


# 04 — Maya / pique


Source : `/opt/data/profiles/game_18/product/refonte_j1_04_maya_pique_draft.md`


# Version draft

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


---


# 05 — Inès / faille


Source : `/opt/data/profiles/game_18/product/refonte_j1_05_ines_faille_draft.md`


# Version draft

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


---


# 06 — Sarah / rentrer manger


Source : `/opt/data/profiles/game_18/product/refonte_j1_06_sarah_rentrer_manger_draft.md`


# Version draft

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


---


# 07 — Nico / vanne soirée


Source : `/opt/data/profiles/game_18/product/refonte_j1_07_nico_vanne_soiree_draft.md`


# Version draft

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


---
