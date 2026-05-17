# Double Vie — Refonte J1 — Draft lisible

## Scène : `j1_02_camille_dehors`

Statut : draft narratif lisible, non intégré runtime.
Source :
- `product/mvp_refonte_source_verite.md`
- `product/refonte_j1_structure_scenes.md`
- `product/godot_t004_prototype/data/schema/variables_and_flags_schema.json`

Objectif : poser la première vraie conversation avec Camille et définir si le joueur reconnaît, minimise, respecte ou instrumentalise le moment dehors.

---

## Fonction de la scène

Camille écrit parce qu’elle sait que le moment dehors n’était pas neutre.
Elle ne demande pas une déclaration. Elle veut surtout savoir si le joueur va ranger ce moment dans la catégorie “rien”.

La scène doit séparer clairement :

- tension avec Camille ;
- respect de Camille ;
- pression exercée sur Camille ;
- culpabilité du joueur ;
- cohérence des versions.

Camille n’est pas une récompense. Elle est lucide, attirante, mais elle garde sa dignité et ses limites.

---

## Connaissances de Camille

Camille sait :

- elle a rejoint le joueur dehors ;
- ils sont restés absents assez longtemps pour que ce soit visible ;
- le moment était émotionnellement chargé ;
- le joueur n’a pas vraiment interrompu le trouble ;
- il pourrait minimiser par peur ou confort.

Camille ignore :

- ce que Sarah sait ;
- ce que le joueur a dit à Sarah ;
- ce que Maya a vu ;
- jusqu’où Nico est impliqué ;
- si le joueur est prêt à perdre quelque chose pour être cohérent.

---

## Ton attendu

Camille écrit avec précision.
Elle formule les choses par détour, mais elle touche juste.
Elle peut être joueuse, mais son jeu n’est pas gratuit.
Elle ne supplie pas. Elle ne se donne pas comme une issue facile.

À éviter :

- Camille jalouse ;
- Camille disponible immédiatement ;
- Camille qui explique tout le thème du jeu ;
- Camille omnisciente sur Sarah ;
- Camille réduite à une tentation sexy.

---

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
