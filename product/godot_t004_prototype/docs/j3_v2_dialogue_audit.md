# J3 V2 — Audit de cohérence complet

## 1. Résumé global

Le Jour 3 V2 remplit globalement le rôle défini dans `docs/j3_design_brief.md` : ce n’est pas encore le jour de la vérité, mais le jour où le joueur comprend qu’il n’est plus seul à gérer les versions.

Les cinq conversations J3 V2 sont désormais écrites : Sarah, Nico, Camille, Maya et Inès. L’axe **contradictions contrôlées** est respecté : Sarah observe les gestes, Nico reprend sa disponibilité, Camille protège son vécu, Maya lit les signaux sociaux sans preuve, et Inès reste dans le calme / distance / fuite.

Aucun dialogue J3 ne contient de preuve absolue ou de révélation globale. Les personnages ne deviennent pas omniscients. La progression émotionnelle reste cohérente avec J1 → J2 → J3.

Le principal problème restant n’est pas textuel : il est **runtime / progression**. T190 avait gardé un MVP J3 court avec Sarah/Nico required et seulement Camille débloquée ensuite. Maintenant que Camille, Maya et Inès sont écrites, le runtime ne reflète plus totalement le contenu disponible : Maya et Inès peuvent rester inaccessibles dans un flux normal, et le Jour 3 peut être considéré comme terminé après Sarah + Nico seulement.

Conclusion globale :

- Dialogues J3 : **validés MVP**.
- Effets / flags : **globalement cohérents**, avec quelques noms à surveiller.
- Runtime J3 : **à corriger avant playtest complet J3**.

## 2. Audit Sarah J3

Fichier : `data/sarah_j3_v2_experimental.json`

### Entry variants

1. `after_concrete` — `j2_sarah_try_concrete`
2. `after_delay` — `j2_sarah_asked_time`
3. `after_minimized` — `j2_sarah_minimized_again`
4. `after_fragile_incoherence` — `j2_sarah_admitted_incoherence` + `j2_sarah_version_fragile_named`
5. `default`

### Cohérence des savoirs

Sarah parle uniquement depuis ce qu’elle a vécu avec le joueur : ses phrases, son délai, sa minimisation, sa version fragile, sa place dans la journée. Elle ne mentionne pas Nico, Camille, Maya ou Inès. Elle ne déduit pas de faits hors écran.

Le choix de centrer la scène sur les gestes plutôt que les promesses est cohérent avec J3 : Sarah ne réclame pas la vérité complète, mais une présence lisible.

### Choix et effets

| Choix | Effet narratif | Cohérence |
|---|---|---|
| `j3_01_sarah_show_with_actions` | confiance + cohérence, distance réduite | OK |
| `j3_01_sarah_honest_uncertainty` | confiance modérée + cohérence, culpabilité | OK |
| `j3_01_sarah_ask_more_time` | distance + fatigue | OK |
| `j3_01_sarah_defensive` | confiance baisse, distance monte | OK |

### Risques

- Le thème des “gestes” peut devenir une dette narrative si J4 ne l’exploite pas.
- `after_fragile_incoherence` utilise deux flags requis ensemble. C’est cohérent avec la branche J2 actuelle, mais si un futur choix pose un seul des deux flags, la variante ne se déclenchera pas.

### Recommandation

Sarah J3 est validée. À surveiller pour J4 : exploiter les gestes promis ou l’absence de gestes.

## 3. Audit Nico J3

Fichier : `data/nico_j3_v2_experimental.json`

### Entry variants

1. `after_hold_line` — `j2_nico_hold_line`
2. `after_released` — `j2_nico_released_from_alibi`
3. `after_partial_truth` — `j2_nico_partial_truth_camille`
4. `after_joke_escape` — `j2_nico_joke_escape`
5. `default`

### Cohérence des savoirs

Nico parle depuis son rôle d’ami / alibi / confident limité. Il ne rapporte pas de conversation Sarah, ne nomme pas Maya, et ne trahit pas le joueur. Le teaser “quelqu’un m’a écrit” reste assez flou pour préparer une vie sociale hors joueur sans basculer dans une révélation.

La branche `j3_02_nico_sarah_observes` est cohérente parce que c’est le joueur qui parle de Sarah à Nico. Nico réagit à la perception du joueur, pas à un savoir direct.

### Choix et effets

| Choix | Effet narratif | Cohérence |
|---|---|---|
| `j3_02_nico_respect_limit` | dette Nico baisse, cohérence monte | OK |
| `j3_02_nico_ask_more_help` | dette + risque + fatigue | OK |
| `j3_02_nico_sarah_observes` | pression Sarah racontée à Nico, risque/fatigue | OK avec réserve de nommage |
| `j3_02_nico_deflect_to_his_life` | dette/fatigue baissent, vie propre teasée | OK |

### Risques

- `j3_nico_knows_sarah_observes` est ambigu : Nico ne sait pas objectivement que Sarah observe ; il sait que le joueur le lui raconte.
- `j3_sarah_gestures_pressure_named` est aussi ambigu : cette pression est nommée par le joueur à Nico, pas par Sarah elle-même.

### Recommandation

Corriger les noms de flags dans une tâche dédiée, sans changer le dialogue :

- `j3_nico_knows_sarah_observes` → `j3_player_told_nico_sarah_observes`
- `j3_sarah_gestures_pressure_named` → `j3_player_named_sarah_gestures_pressure`

Priorité : **recommandé**, avant que ces flags soient utilisés en J4.

## 4. Audit Camille J3

Fichier : `data/camille_j3_v2_experimental.json`

### Entry variants

1. `after_assumed_tension` — `j2_camille_assumed_tension`
2. `after_clear_boundary` — `j2_camille_clear_boundary`
3. `after_minimized_again` — `j2_camille_minimized_again`
4. `after_refuge_attempt` — `j2_camille_refuge_attempt`
5. `default`

### Cohérence des savoirs

Camille parle uniquement depuis ce qu’elle a vécu avec le joueur. Elle ne nomme pas Sarah, Nico, Maya ou Inès. Elle parle de “ailleurs”, de “confusion”, de “sortie”, de “poids”, mais sans savoir ce qui se passe dans les autres conversations.

C’est cohérent avec son rôle : elle protège son propre vécu et refuse d’être minimisée ou utilisée comme refuge.

### Choix et effets

| Choix | Effet narratif | Cohérence |
|---|---|---|
| `j3_03_camille_recognize_without_using` | respect +, pression - | OK |
| `j3_03_camille_keep_boundary` | respect +, pression --, tension - | OK |
| `j3_03_camille_reopen_tension` | tension +++, pression ++, risque + | OK |
| `j3_03_camille_close_down` | respect baisse, tension baisse, pression monte | OK |

### Risques

- Camille peut parfois être très analytique, mais cela reste acceptable parce qu’elle parle depuis son ressenti.
- Le choix `reopen_tension` augmente pression et risque : c’est essentiel pour éviter une lecture “récompense Camille”.

### Recommandation

Camille J3 est validée. Aucun correctif prioritaire.

## 5. Audit Maya J3

Fichier : `data/maya_j3_v2_experimental.json`

### Entry variants

1. `after_social_read_opened` — `j2_maya_social_read_opened`
2. `after_malaise_admitted` — `j2_maya_malaise_admitted`
3. `after_defensive` — `j2_maya_defensive`
4. `after_discretion` — `j2_maya_discretion_requested`
5. `default`

### Cohérence des savoirs

Maya reste dans le registre social : ambiance, détails, flou, signaux, groupe, absence de preuve. Elle ne nomme aucun autre personnage. Elle ne donne aucun fait privé. Les phrases “sentir, ce n’est pas savoir” et “je ne vais pas te donner des noms” respectent très bien le cadrage.

La scène réussit à rendre le monde plus vivant sans transformer Maya en détective.

### Choix et effets

| Choix | Effet narratif | Cohérence |
|---|---|---|
| `j3_04_maya_ask_what_changed` | ouvre les signaux, risque léger | OK |
| `j3_04_maya_keep_group_boundary` | suspicion/risk baisse, canal direct demandé | OK |
| `j3_04_maya_minimize_signals` | suspicion/risk montent | OK |
| `j3_04_maya_ask_if_others_notice` | risque social fort, sans noms | OK |

### Risques

- Le choix `ask_if_others_notice` ouvre un vrai fil J4 : si le joueur choisit cette option, J4 devrait pouvoir faire exister un malaise social plus fort.
- Le flag `j3_maya_social_thread_possible` prépare bien ce risque.

### Recommandation

Maya J3 est validée. À exploiter plus tard en J4 si besoin.

## 6. Audit Inès J3

Fichier : `data/ines_j3_v2_experimental.json`

### Entry variants

1. `after_careful_opening` — `j2_ines_careful_opening`
2. `after_boundary` — `j2_ines_boundary_kept`
3. `after_refuge` — `j2_ines_refuge_attempt`
4. `after_repair` — `j2_ines_repair_misstep`
5. `default`

### Cohérence des savoirs

Inès reste complètement isolée des faits centraux. Elle ne mentionne pas le groupe, les photos ou les autres personnages. Elle parle de calme, de distance, de présence, de bruit, de fuite et de limite. C’est cohérent avec son rôle.

Elle ne devient pas une récompense romantique : même quand elle accepte une présence claire, elle la conditionne au fait de ne pas être utilisée comme échappatoire.

### Choix et effets

| Choix | Effet narratif | Cohérence |
|---|---|---|
| `j3_05_ines_clear_presence` | fuite baisse fortement, cohérence monte | OK |
| `j3_05_ines_keep_soft_distance` | fuite baisse, cohérence monte | OK |
| `j3_05_ines_seek_refuge_again` | fuite monte fortement, cohérence baisse | OK |
| `j3_05_ines_step_back` | fuite baisse, fatigue/culpabilité montent | OK |

### Risques

- Inès reste très lucide. Le risque de “thérapeute parfaite” existe légèrement, mais ses phrases restent suffisamment personnelles et prudentes.
- Le thème “je ne veux pas être un endroit” revient depuis J2 ; la répétition est cohérente, mais à ne pas surutiliser en J4.

### Recommandation

Inès J3 est validée. Aucun correctif prioritaire.

## 7. Audit des variables et effets J3

| Conversation | Choix | Variables modifiées | Effet narratif attendu | Cohérent ? | Risque |
|---|---|---|---|---|---|
| Sarah | gestes visibles | confiance +2, distance -1, coherence +2, culpabilite +1 | réparation par actions | Oui | dette J4 sur les gestes |
| Sarah | incertitude honnête | confiance +1, coherence +2, culpabilite +2, fatigue +1 | honnêteté non magique | Oui | fatigue augmente malgré amélioration, cohérent |
| Sarah | plus de temps | confiance -1, distance +2, fatigue +1, culpabilite +1 | attente prolongée | Oui | à exploiter J4 |
| Sarah | défensive | confiance -2, distance +2, coherence -1, fatigue +1 | fermeture | Oui | aucun |
| Nico | respecter limite | dette -2, coherence +2, fatigue -1, risque -1 | ami libéré | Oui | aucun |
| Nico | aide encore | dette +2, coherence -1, risque +1, fatigue +1 | alibi prolongé | Oui | aucun |
| Nico | Sarah observe | coherence +1, risque +1, fatigue +1 | pression racontée à Nico | Oui | flags à renommer |
| Nico | vie propre | dette -1, fatigue -1 | sortie du rôle d’outil | Oui | prépare J4 Nico/Maya |
| Camille | reconnaître sans utiliser | tension +1, respect +2, pression -1, coherence +1 | tension tenue proprement | Oui | aucun |
| Camille | garder limite | tension -1, respect +2, pression -2, coherence +2 | limite saine | Oui | aucun |
| Camille | rouvrir tension | tension +3, pression +2, respect -1, risque +1 | désir risqué | Oui | ne pas traiter comme récompense |
| Camille | refermer | tension -2, respect -2, pression +1, coherence -1 | minimisation froide | Oui | aucun |
| Maya | demander signaux | suspicion +1, coherence +1, risque +1 | flou ouvert | Oui | aucun |
| Maya | limite groupe | suspicion -1, coherence +1, risque -1 | canal direct | Oui | aucun |
| Maya | minimiser | suspicion +2, coherence -1, risque +1 | défense suspecte | Oui | aucun |
| Maya | autres remarquent | suspicion +1, risque +2, fatigue +1 | risque social | Oui | à exploiter J4 |
| Inès | présence claire | fuite -2, coherence +2, fatigue -1, culpabilite +1 | présence non-fuite | Oui | aucun |
| Inès | distance douce | fuite -1, coherence +2, fatigue -1 | limite saine | Oui | aucun |
| Inès | refuge encore | fuite +3, fatigue -1, culpabilite +1, coherence -1 | fuite coûteuse | Oui | aucun |
| Inès | recul | fuite -2, coherence +1, fatigue +1, culpabilite +1 | recul propre mais coûteux | Oui | aucun |

Aucune variable n’est manifestement mal ciblée. Les effets sur personnages absents sont évités. Le principal point est le nommage des flags Nico autour de Sarah.

## 8. Audit des flags J3

### Sarah

- `j3_sarah_promises_actions` : promesse d’agir, utile J4.
- `j3_sarah_place_named` : place Sarah nommée, utile J4.
- `j3_sarah_honest_uncertainty` : incertitude assumée, utile.
- `j3_sarah_no_false_promise` : très bon flag de garde-fou.
- `j3_sarah_more_time` : attente prolongée, utile.
- `j3_sarah_waiting_continues` : conséquence émotionnelle claire.
- `j3_sarah_defensive` : défense, utile.
- `j3_sarah_feels_unheard` : ressenti Sarah, utile.

Statut : OK.

### Nico

- `j3_nico_limit_respected` : OK.
- `j3_nico_no_longer_tool` : OK.
- `j3_nico_more_help_requested` : OK.
- `j3_nico_pressure_continues` : OK.
- `j3_nico_knows_sarah_observes` : ambigu.
- `j3_sarah_gestures_pressure_named` : ambigu.
- `j3_nico_life_outside_player_teased` : OK.
- `j3_nico_maya_thread_possible` : OK, même si Maya n’est pas nommée dans le dialogue.

Renommage recommandé :

- `j3_nico_knows_sarah_observes` → `j3_player_told_nico_sarah_observes`
- `j3_sarah_gestures_pressure_named` → `j3_player_named_sarah_gestures_pressure`

### Camille

- `j3_camille_recognized_without_using` : OK.
- `j3_camille_not_escape_route` : OK.
- `j3_camille_boundary_kept` : OK.
- `j3_camille_confusion_not_shifted` : OK.
- `j3_camille_tension_reopened` : OK.
- `j3_camille_pressure_rises` : OK.
- `j3_camille_minimized_again` : OK.
- `j3_camille_closes_badly` : OK.

Statut : OK.

### Maya

- `j3_maya_asked_for_signals` : OK.
- `j3_maya_social_signals_opened` : OK.
- `j3_maya_group_boundary_requested` : OK.
- `j3_maya_direct_channel_requested` : OK.
- `j3_maya_defensive_again` : OK.
- `j3_maya_suspicion_reinforced` : OK.
- `j3_maya_others_may_notice` : OK.
- `j3_maya_social_thread_possible` : OK.

Statut : OK.

### Inès

- `j3_ines_clear_presence` : OK.
- `j3_ines_not_used_as_escape` : OK.
- `j3_ines_soft_distance` : OK.
- `j3_ines_boundary_respected` : OK.
- `j3_ines_refuge_again` : OK.
- `j3_ines_escape_risk_high` : OK.
- `j3_ines_step_back` : OK.
- `j3_ines_not_pulled_in` : OK.

Statut : OK.

## 9. Audit des entry variants J3

Les entry variants J3 correspondent bien aux flags J2 attendus.

### Sarah

OK. Risque mineur : `after_fragile_incoherence` exige deux flags. Acceptable car la branche J2 pose ces deux flags ensemble.

### Nico

OK. Les variantes couvrent : alibi prolongé, alibi libéré, vérité partielle Camille, fuite par la vanne.

### Camille

OK. Les variantes couvrent les quatre postures J2 majeures : tension, limite, minimisation, refuge.

### Maya

OK. Les variantes couvrent : lecture sociale ouverte, malaise admis, défense, discrétion.

### Inès

OK. Les variantes couvrent : ouverture prudente, limite, refuge, réparation.

Aucune entry variant ne crée une information impossible.

## 10. Audit runtime / progression J3

Fichier : `scripts/conversation_state.gd`

### État actuel

Le runtime actuel fait :

- passage au Jour 3 expérimental : débloque `sarah_j3_v2` et `nico_j3_v2` ;
- required J3 expérimental : `sarah_j3_v2`, `nico_j3_v2` uniquement ;
- après Sarah ou Nico terminé : débloque `camille_j3_v2` ;
- pas de déblocage Maya après Camille ;
- pas de déblocage Inès après Maya.

### Problème

Maintenant que les cinq conversations J3 sont écrites, le runtime est devenu incomplet :

- `maya_j3_v2` et `ines_j3_v2` peuvent rester inaccessibles dans un parcours normal ;
- le Jour 3 peut devenir transitionnable après Sarah + Nico seulement, donc avant Camille / Maya / Inès ;
- Camille peut être débloquée mais non required, donc elle peut aussi être ignorée si la transition est disponible.

Ce n’était pas bloquant au moment de T190, mais ça le devient maintenant que les cinq scènes existent.

### Recommandation runtime

Créer T198 pour aligner le runtime J3 sur le contenu écrit :

- début J3 : Sarah + Nico ;
- Sarah ou Nico terminé → Camille ;
- Camille terminée → Maya ;
- Maya terminée → Inès optionnelle ;
- required J3 recommandé : Sarah, Nico, Camille, Maya ;
- Inès optionnelle, comme en J2.

Cette logique reflète le J2 V2 et permet de jouer tout le contenu écrit sans rendre Inès bloquante.

### Priorité

**Bloquant avant playtest complet J3.**

## 11. Cohérence globale J3

J3 produit bien une montée de pression par circulation indirecte :

- Sarah demande des gestes ;
- Nico refuse de porter les phrases du joueur ;
- Camille refuse d’être une sortie ;
- Maya signale que l’ambiance devient perceptible ;
- Inès refuse d’être un refuge.

Il existe une répétition volontaire autour de “ne pas porter / ne pas être utilisé / ne pas être une sortie”. Elle est thématique et cohérente, mais à surveiller en J4 pour éviter que tous les personnages parlent avec la même structure morale.

La variation actuelle reste suffisante :

- Sarah = place / gestes / attente ;
- Nico = disponibilité / dette / vie propre ;
- Camille = tension / limite / refuge ;
- Maya = signaux sociaux / groupe / flou ;
- Inès = calme / distance / fuite.

## 12. Problèmes classés

### Bloquant

1. Runtime J3 incomplet : Maya et Inès peuvent rester inaccessibles.
2. Required J3 encore limité à Sarah/Nico alors que Camille/Maya sont écrites et structurantes.
3. Transition J3 potentiellement disponible avant le contenu J3 complet.

### Recommandé

1. Renommer deux flags Nico autour de Sarah observatrice.
2. Surveiller la répétition thématique “je ne veux pas porter / être utilisé”.
3. J4 devra exploiter certains flags J3 forts : gestes Sarah, dette Nico, tension Camille, social Maya, fuite Inès.

### Optionnel

1. Polir légèrement certaines formulations très analytiques si le playtest les fait sonner trop écrites.
2. Ajouter plus tard une doc de transition J3 → J4.

## 13. Recommandations pour T198 / T199 / T200

### T198 — Runtime J3 complet

Priorité immédiate.

Objectif :

- étendre `_repair_j3_v2_progression_unlocks()` ;
- débloquer Maya après Camille ;
- débloquer Inès après Maya ;
- rendre Sarah/Nico/Camille/Maya required pour J3 expérimental ;
- garder Inès optionnelle ;
- empêcher la transition J3 avant Camille/Maya.

Commit attendu possible :
`feat: complete J3 V2 progressive unlocks`

### T199 — Polish cohérence J3

À faire seulement après T198 ou playtest.

Cibles possibles :

- renommage flags Nico ;
- léger polish si certains dialogues sonnent trop analytiques ;
- ajustement des effets si playtest montre un ressenti incohérent.

### T200 — Préparation J4

À faire une fois J3 runtime + playtest validés.

Objectif :

- définir J4 comme première vraie journée de conséquences croisées plus fortes ;
- décider si Nico ↔ Maya devient visible ;
- décider si Sarah observe les gestes promis ;
- décider si Camille/Inès restent des routes distinctes ou des miroirs.

## 14. Décision proposée

Décision recommandée : **corriger le runtime J3 avant tout nouveau contenu**.

Le contenu J3 est suffisamment cohérent pour être testé, mais le flux actuel ne permet pas encore de le jouer proprement de bout en bout. T198 doit donc précéder tout polish ou toute préparation J4.

