# Double Vie — Refonte J1 — Draft lisible

## Scène : `j1_01_sarah_absence`

Statut : draft narratif lisible, non intégré runtime.
Source :
- `product/mvp_refonte_source_verite.md`
- `product/refonte_j1_structure_scenes.md`
- `product/godot_t004_prototype/data/schema/variables_and_flags_schema.json`

Objectif : poser la première vraie conversation avec Sarah et enregistrer la première version donnée par le joueur.

---

## Fonction de la scène

Sarah demande où le joueur était pendant la soirée, mais elle ne mène pas une enquête.
Elle part d’un détail concret : son retour, son silence, le fait qu’il était là sans vraiment être là.

Elle ne sait pas ce qui s’est passé dehors avec Camille. Elle sait seulement que quelque chose a changé.

Cette scène doit fixer une première version :

- besoin d’air ;
- alibi Nico ;
- Camille mentionnée mais minimisée ;
- vulnérabilité partielle ;
- absence de réponse claire.

---

## Connaissances de Sarah

Sarah sait :

- le joueur s’est absenté pendant la soirée ;
- il est revenu différent ;
- Camille était absente à un moment proche ;
- Nico a donné une explication floue ;
- le joueur semble plus distant depuis quelque temps.

Sarah ignore :

- ce qui s’est dit dehors ;
- s’il y a eu contact physique ;
- ce que Camille pense de ce moment ;
- ce que le joueur a dit ou dira aux autres.

---

## Ton attendu

Sarah parle depuis la maison et le concret.
Elle n’est pas brillante ou coupante. Elle est simple, contenue, blessée sans chercher à piéger.

À éviter :

- accusation frontale ;
- phrase trop littéraire ;
- omniscience ;
- ultimatum prématuré ;
- Sarah réduite à la culpabilité.

---

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
