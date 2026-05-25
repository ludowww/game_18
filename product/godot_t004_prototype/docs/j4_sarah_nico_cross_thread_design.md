# J4 — Design du croisement Sarah ↔ Nico

## 0. Statut et périmètre

Document de design pour le premier croisement dynamique J4 : Sarah ↔ Nico.

Ce document ne crée pas J4. Il définit la structure cible, les conversations futures, les flags, les effets narratifs et les garde-fous avant toute création JSON ou runtime.

Contraintes T209 :

- aucun JSON modifié ;
- aucun script modifié ;
- aucune conversation J4 créée ;
- aucun dialogue complet écrit ;
- aucun asset ajouté ;
- aucun test modifié ;
- documentation uniquement.

Documents respectés :

- `docs/narrative_production_bible_j4_plus.md` ;
- `docs/j4_macro_brief.md` ;
- `docs/j4_temporality_and_availability.md` ;
- `docs/j4_character_arc_matrix.md`.

## 1. Rôle du croisement

Le croisement Sarah ↔ Nico est le premier moment où le joueur ne gère plus les conversations comme des fils totalement séparés.

But :

- Sarah remarque un détail faible ;
- le joueur peut répondre directement ou temporiser ;
- le joueur peut consulter Nico avant de répondre ;
- Nico peut aider, refuser ou alerter sur le délai ;
- Sarah peut ensuite sentir la réponse ou le délai.

Le croisement ne doit pas être une explosion.

Il doit faire sentir :

- le coût du temps ;
- le coût de l’alibi ;
- la différence entre sincérité et version préparée ;
- la dette envers Nico ;
- la fragilité du quotidien avec Sarah.

Phrase directrice :

> Le joueur peut chercher une réponse plus propre, mais le temps pris pour la fabriquer devient lui-même visible.

## 2. Décision de design T209

Décision recommandée : implémenter J4 avec un **croisement réel mais runtime-light**, en trois conversations.

1. `sarah_j4_v2`
   - Sarah ouvre le matin avec un détail.
   - Le joueur choisit une posture.
   - Si le joueur veut consulter Nico, Sarah reste en attente.

2. `nico_j4_v2`
   - Nico est débloqué après Sarah.
   - Il réagit selon le choix fait avec Sarah.
   - Il peut aider, refuser, conseiller ou rappeler le coût.

3. `sarah_j4_followup_v2`
   - Sarah revient après Nico.
   - Elle réagit au délai, au ton ou à la réponse préparée.
   - Cette conversation ferme le mini-croisement Sarah ↔ Nico.

Pourquoi ajouter `sarah_j4_followup_v2` ?

- Sans retour Sarah, le croisement reste abstrait.
- Le joueur doit voir l’effet de son délai.
- J4 doit donner une impression de fil vivant.
- Ce follow-up permet de sentir que consulter Nico a un effet immédiat, sans système multi-fil complexe.

Cette conversation de retour doit rester courte.

## 3. Structure temporelle recommandée

### Bloc 1 — Sarah matin

Conversation : `sarah_j4_v2`

Moment : début de matinée.

Fonction : Sarah remarque un détail.

Sorties possibles :

- réponse directe ;
- vérité prudente ;
- temporisation ;
- défense ;
- “je vérifie avant de répondre” / contact Nico.

### Bloc 2 — Nico consultation

Conversation : `nico_j4_v2`

Moment : fin de matinée.

Fonction : le joueur consulte Nico ou parle à Nico après le message Sarah.

Nico n’est pas un bouton magique. Il peut :

- aider ;
- refuser ;
- dire que le délai va se voir ;
- conseiller de répondre plus simplement ;
- rappeler qu’il n’est pas un service de maintenance des versions.

### Bloc 3 — Sarah retour

Conversation : `sarah_j4_followup_v2`

Moment : fin de matinée / avant midi.

Fonction : Sarah reçoit la réponse ou perçoit le délai.

Elle ne sait pas que Nico a été consulté. Elle peut seulement sentir :

- que le joueur a répondu vite ;
- qu’il a mis du temps ;
- qu’il répond trop proprement ;
- qu’il se défend ;
- qu’il revient avec une formulation plus stable mais moins spontanée.

Après ce follow-up : Camille peut se débloquer pour le bloc midi.

## 4. Pourquoi ne pas faire un système runtime multi-fil complet maintenant

À éviter pour le MVP J4 :

- interruption d’une conversation active ;
- retour dynamique dans le même fil après une autre conversation ;
- required conditionnels complexes ;
- choix qui ouvre un autre chat sans fermer proprement le premier ;
- logique de scheduler ou temps réel.

Raison : ce serait coûteux, fragile et risquerait de ralentir la production.

Solution MVP : créer un cross-thread narratif lisible avec :

- flags ;
- unlock progressif ;
- une conversation Sarah follow-up dédiée ;
- entry variants selon les flags posés.

Cela donne l’effet de croisement sans sur-développer le runtime.

## 5. Conversations J4 à prévoir

### Obligatoires recommandées

- `sarah_j4_v2`
- `nico_j4_v2`
- `sarah_j4_followup_v2`
- `camille_j4_v2`
- `maya_j4_v2`

### Optionnelle recommandée

- `ines_j4_v2`

Différence avec T208 : T208 proposait Sarah/Nico/Camille/Maya required. T209 recommande d’ajouter `sarah_j4_followup_v2` comme required, car le croisement Sarah ↔ Nico doit avoir un vrai retour dans la journée.

Inès reste optionnelle.

## 6. Déblocage recommandé

Début J4 :

- `sarah_j4_v2` disponible.

Après `sarah_j4_v2` terminée :

- `nico_j4_v2` disponible.

Après `nico_j4_v2` terminée :

- `sarah_j4_followup_v2` disponible.

Après `sarah_j4_followup_v2` terminée :

- `camille_j4_v2` disponible.

Après `camille_j4_v2` terminée :

- `maya_j4_v2` disponible.

Après `maya_j4_v2` terminée :

- `ines_j4_v2` disponible, optionnelle.

Required J4 :

- Sarah matin ;
- Nico ;
- Sarah follow-up ;
- Camille ;
- Maya.

Non required :

- Inès.

## 7. Sarah matin — design

### Rôle

Sarah ouvre avec un détail faible. Elle ne sait rien de Nico. Elle ne doit pas accuser frontalement.

### Exemple de situation

Sarah remarque :

- un geste attendu qui n’est pas venu ;
- une réponse trop tardive ;
- une phrase qui ne colle pas avec les actes ;
- un petit détail domestique.

Elle peut dire des choses comme :

- `Je ne sais pas si c’est important, mais j’ai remarqué un détail.`
- `Ce matin, je me suis demandé si tu allais y penser.`
- `Je crois que je regarde trop les petits trucs maintenant.`
- `Il y a un truc qui colle pas. Pas énorme. Mais je l’ai vu.`

### Entry variants Sarah matin

Utiliser les flags J3 Sarah.

Propositions :

1. `after_actions_promised`
   - flag : `j3_sarah_promises_actions`
   - Sarah attend un geste.

2. `after_honest_uncertainty`
   - flag : `j3_sarah_honest_uncertainty`
   - Sarah reste prudente mais accessible.

3. `after_more_time`
   - flag : `j3_sarah_more_time`
   - Sarah est plus distante.

4. `after_defensive`
   - flag : `j3_sarah_defensive` ou `j3_sarah_feels_unheard`
   - Sarah écrit plus court.

5. `default`

### Choix central Sarah matin

Node futur : `j4_01_choice_sarah_morning_detail`

#### Choix 1 — répondre directement

Texte intentionnel :

`Tu as raison de le remarquer. Je vais te répondre directement, sans chercher une version parfaite.`

Effets :

- `confiance_sarah` +1
- `coherence` +2
- `risque_exposition` 0

Flags :

- `j4_player_given_direct_sarah_answer`
- `j4_sarah_morning_detail_answered`

#### Choix 2 — vérité prudente

Texte intentionnel :

`Je peux t’expliquer, mais je préfère le faire sans tout lisser.`

Effets :

- `confiance_sarah` +1
- `coherence` +1
- `fatigue_emotionnelle` +1

Flags :

- `j4_player_chose_prudent_truth`
- `j4_sarah_detail_acknowledged`

#### Choix 3 — temporiser

Texte intentionnel :

`Je veux te répondre, mais pas n’importe comment. Laisse-moi un peu de temps.`

Effets :

- `distance_sarah` +1
- `fatigue_emotionnelle` +1
- `risque_exposition` +1

Flags :

- `j4_player_delayed_sarah_answer`
- `j4_sarah_delay_possible`

#### Choix 4 — vérifier avec Nico

Texte intentionnel :

`Je vais vérifier un truc avant de te répondre, parce que je ne veux pas te dire n’importe quoi.`

Effets :

- `distance_sarah` +1
- `risque_exposition` +1
- `dette_nico` +1

Flags :

- `j4_sarah_answer_pending_nico_check`
- `j4_player_checked_with_nico`
- `j4_player_delayed_sarah_answer`

Attention : Sarah ne sait pas que c’est Nico. Le texte doit rester vague : “vérifier un truc”, pas “je vais demander à Nico”.

#### Choix 5 — se défendre

Texte intentionnel :

`J’ai l’impression que le moindre détail devient un procès.`

Effets :

- `confiance_sarah` -1
- `distance_sarah` +2
- `coherence` -1

Flags :

- `j4_player_defensive_with_sarah`
- `j4_sarah_feels_pushed_away`

## 8. Nico consultation — design

### Rôle

Nico vient après Sarah matin. Il reflète la posture choisie :

- si le joueur a demandé à vérifier, Nico comprend qu’on lui demande quelque chose ;
- si le joueur a répondu directement, Nico peut être une respiration ;
- si le joueur a temporisé, Nico peut alerter sur le délai ;
- si le joueur s’est défendu, Nico peut se moquer doucement de la défense.

### Entry variants Nico

1. `after_sarah_pending_check`
   - flag : `j4_sarah_answer_pending_nico_check`
   - Nico réagit à une demande de vérification.

2. `after_direct_sarah_answer`
   - flag : `j4_player_given_direct_sarah_answer`
   - Nico est moins alibi, plus ami.

3. `after_sarah_delay`
   - flag : `j4_player_delayed_sarah_answer`
   - Nico signale que le délai peut se voir.

4. `after_sarah_defensive`
   - flag : `j4_player_defensive_with_sarah`
   - Nico peut se moquer doucement de la défense.

5. `default`

### Ce que Nico peut savoir

Nico sait seulement ce que le joueur lui dit.

Si le joueur dit : `Sarah a remarqué un truc`, alors Nico peut réagir à cette phrase.

Nico ne sait pas :

- le détail exact, sauf si le joueur le dit ;
- ce que Sarah ressent vraiment ;
- ce que Sarah a compris ;
- ce que Camille/Maya/Inès savent.

### Choix central Nico

Node futur : `j4_02_choice_nico_consultation`

#### Choix 1 — demander conseil

Texte intentionnel :

`J’ai besoin d’un avis, pas d’un alibi. Juste savoir comment ne pas empirer.`

Effets :

- `coherence` +1
- `dette_nico` +1
- `fatigue_emotionnelle` +1

Flags :

- `j4_nico_advice_requested`
- `j4_nico_warned_about_delay`

#### Choix 2 — demander couverture

Texte intentionnel :

`J’ai besoin que tu tiennes la même ligne que moi, au moins pour aujourd’hui.`

Effets :

- `dette_nico` +2
- `risque_exposition` +2
- `coherence` -1

Flags :

- `j4_nico_cover_requested`
- `j4_nico_pressure_increases`

#### Choix 3 — libérer Nico

Texte intentionnel :

`Non, laisse. Je ne veux pas te remettre là-dedans.`

Effets :

- `dette_nico` -1
- `coherence` +1
- `risque_exposition` 0

Flags :

- `j4_nico_released_again`
- `j4_player_chooses_own_answer`

#### Choix 4 — plaisanter / esquiver

Texte intentionnel :

`C’était une question théorique. Comme tous les incendies que je déclenche.`

Effets :

- `dette_nico` +1
- `fatigue_emotionnelle` -1
- `risque_exposition` +1

Flags :

- `j4_nico_joke_escape`
- `j4_nico_not_a_service`

#### Choix 5 — parler soirée jeux vidéo

Texte intentionnel :

`Et sinon, ta soirée console tient toujours ? J’ai peut-être besoin de penser à autre chose.`

Effets :

- `fatigue_emotionnelle` -1
- `dette_nico` 0

Flags :

- `j4_nico_game_evening_seed`
- `j4_player_considers_game_evening`

## 9. Nico — résultats possibles

Selon le choix, Nico doit poser un flag exploitable par Sarah follow-up.

### Si conseil

Flags :

- `j4_nico_advised_direct_answer`
- `j4_nico_warned_about_delay`

Conséquence Sarah follow-up : Sarah sent peut-être le délai, mais la réponse peut être plus cohérente.

### Si couverture

Flags :

- `j4_nico_helped_version`
- `j4_nico_cover_requested`

Conséquence Sarah follow-up : réponse plus “propre” mais plus risquée / moins spontanée.

### Si Nico libéré

Flags :

- `j4_nico_released_again`
- `j4_player_chooses_own_answer`

Conséquence Sarah follow-up : réponse plus personnelle, moins préparée.

### Si plaisanterie

Flags :

- `j4_nico_joke_escape`
- `j4_nico_not_a_service`

Conséquence Sarah follow-up : le joueur reste flou ; Sarah peut sentir l’évitement.

### Si soirée console

Flags :

- `j4_nico_game_evening_seed`
- `j4_player_considers_game_evening`

Conséquence Sarah follow-up : prépare le conflit du soir : vraie respiration ou fuite.

## 10. Sarah follow-up — design

### Rôle

Sarah follow-up ferme le croisement. Elle ne sait pas ce qui s’est passé avec Nico. Elle réagit au délai, au ton, à la réponse.

Conversation future : `sarah_j4_followup_v2`

### Entry variants Sarah follow-up

1. `after_nico_helped_version`
   - flag : `j4_nico_helped_version`
   - Sarah sent une réponse trop propre.

2. `after_nico_advice`
   - flag : `j4_nico_advised_direct_answer`
   - Sarah peut sentir une réponse plus simple mais tardive.

3. `after_nico_refused_or_released`
   - flags : `j4_nico_released_again` ou `j4_player_chooses_own_answer`
   - Sarah reçoit une réponse plus personnelle.

4. `after_delay_only`
   - flag : `j4_player_delayed_sarah_answer`
   - Sarah réagit au délai.

5. `after_defensive`
   - flag : `j4_player_defensive_with_sarah`
   - Sarah se protège.

6. `default`

### Ce que Sarah peut dire

Sarah peut dire :

- `Tu as mis du temps.`
- `Je ne sais pas si tu cherchais tes mots ou autre chose.`
- `Ta réponse est plus claire. Je ne sais pas si elle est plus simple.`
- `J’aurais préféré que tu me dises que tu ne savais pas répondre.`
- `Là, j’ai l’impression que tu me réponds depuis toi. C’est déjà différent.`

Sarah ne doit pas dire :

- `Tu as demandé à Nico.`
- `Nico t’a aidé.`
- `Vous vous êtes mis d’accord.`
- `Je sais que tu as vérifié une version.`

### Choix central Sarah follow-up

Node futur : `j4_03_choice_sarah_followup`

#### Choix 1 — assumer le délai

Texte intentionnel :

`Oui, j’ai pris du temps. Je ne voulais pas répondre juste pour me protéger.`

Effets :

- `confiance_sarah` +1
- `coherence` +1
- `fatigue_emotionnelle` +1

Flags :

- `j4_sarah_delay_admitted`
- `j4_player_owns_delay`

#### Choix 2 — donner une réponse simple

Texte intentionnel :

`Tu as raison. Je vais faire simple : ce détail compte, et je ne veux pas le balayer.`

Effets :

- `confiance_sarah` +2
- `distance_sarah` -1
- `coherence` +2

Flags :

- `j4_sarah_detail_validated`
- `j4_player_simple_answer`

#### Choix 3 — rester flou

Texte intentionnel :

`Je crois que tu donnes beaucoup de poids à quelque chose de petit.`

Effets :

- `confiance_sarah` -1
- `distance_sarah` +1
- `coherence` -1

Flags :

- `j4_sarah_detail_minimized`
- `j4_sarah_trust_strains`

#### Choix 4 — avouer qu’on a cherché ses mots

Texte intentionnel :

`J’ai cherché mes mots, oui. Pas pour inventer, mais parce que je sentais que ça pouvait abîmer plus.`

Effets :

- `confiance_sarah` +1
- `coherence` +1
- `fatigue_emotionnelle` +1

Flags :

- `j4_player_searched_words`
- `j4_sarah_hears_effort`

#### Choix 5 — se défendre

Texte intentionnel :

`Je ne peux pas être suspect à chaque fois que je ne réponds pas assez vite.`

Effets :

- `confiance_sarah` -2
- `distance_sarah` +2
- `coherence` -1

Flags :

- `j4_player_defensive_followup`
- `j4_sarah_closes_after_defense`

## 11. Effets croisés globaux

### Répondre directement à Sarah

Effet :

- cohérence plus haute ;
- moins de dette Nico ;
- risque de maladresse.

Variables :

- `coherence` +2
- `dette_nico` 0
- `confiance_sarah` +1 selon ton

### Consulter Nico

Effet :

- réponse potentiellement plus propre ;
- délai visible ;
- dette Nico ;
- risque exposition.

Variables :

- `dette_nico` +1/+2
- `risque_exposition` +1/+2
- `distance_sarah` +1
- `coherence` variable

### Temporiser sans Nico

Effet :

- moins de dette ;
- mais Sarah sent le délai ;
- flou plus lourd.

Variables :

- `distance_sarah` +1
- `fatigue_emotionnelle` +1
- `coherence` 0/-1

### Se défendre

Effet :

- Sarah se ferme ;
- Nico peut éventuellement recadrer si consulté ensuite.

Variables :

- `confiance_sarah` -1/-2
- `distance_sarah` +2
- `coherence` -1

## 12. Garde-fous anti-omniscience

### Sarah

Ne doit jamais savoir :

- que Nico a été contacté ;
- ce que Nico a conseillé ;
- si Nico a aidé ou refusé ;
- une vérité issue d’un autre fil.

Elle peut seulement percevoir :

- délai ;
- ton ;
- formulation trop préparée ;
- évitement ;
- cohérence.

### Nico

Ne doit jamais savoir :

- ce que Sarah pense vraiment ;
- ce qu’elle a compris ;
- le détail exact si le joueur ne le lui donne pas ;
- les émotions exactes de Sarah.

Il peut seulement savoir :

- ce que le joueur lui dit ;
- l’historique de son rôle d’alibi ;
- sa propre fatigue.

## 13. Flags J4 retenus pour MVP

### Sarah matin

- `j4_sarah_morning_detail_noted`
- `j4_player_given_direct_sarah_answer`
- `j4_player_chose_prudent_truth`
- `j4_player_delayed_sarah_answer`
- `j4_sarah_answer_pending_nico_check`
- `j4_player_defensive_with_sarah`

### Nico

- `j4_player_checked_with_nico`
- `j4_nico_advice_requested`
- `j4_nico_advised_direct_answer`
- `j4_nico_cover_requested`
- `j4_nico_helped_version`
- `j4_nico_released_again`
- `j4_player_chooses_own_answer`
- `j4_nico_joke_escape`
- `j4_nico_not_a_service`
- `j4_nico_game_evening_seed`

### Sarah follow-up

- `j4_sarah_delay_admitted`
- `j4_player_owns_delay`
- `j4_sarah_detail_validated`
- `j4_player_simple_answer`
- `j4_sarah_detail_minimized`
- `j4_sarah_trust_strains`
- `j4_player_searched_words`
- `j4_sarah_hears_effort`
- `j4_player_defensive_followup`
- `j4_sarah_closes_after_defense`

## 14. Required conversations révisées J4

À partir de ce design, required J4 recommandé :

- `sarah_j4_v2`
- `nico_j4_v2`
- `sarah_j4_followup_v2`
- `camille_j4_v2`
- `maya_j4_v2`

Optionnelle :

- `ines_j4_v2`

Justification : le follow-up Sarah est nécessaire pour donner un effet réel au croisement.

## 15. Déblocage recommandé révisé

Début J4 :

- Sarah J4 disponible.

Après Sarah J4 :

- Nico J4 disponible.

Après Nico J4 :

- Sarah J4 follow-up disponible.

Après Sarah follow-up :

- Camille J4 disponible.

Après Camille J4 :

- Maya J4 disponible.

Après Maya J4 :

- Inès J4 optionnelle disponible.

## 16. Ce qu’il ne faut pas faire dans T210/T211

Ne pas :

- créer un runtime complexe multi-fil ;
- faire revenir Sarah dans la même conversation après Nico si le moteur ne le supporte pas proprement ;
- faire dire à Sarah qu’elle sait que Nico a été consulté ;
- faire trahir Nico ;
- rendre le délai trop explosif ;
- faire de ce croisement une révélation totale ;
- ajouter des médias ;
- ajouter une confrontation Sarah/Camille.

## 17. Tests futurs à prévoir

Quand la structure J4 sera créée, prévoir des tests pour vérifier :

- les six conversations J4 attendues existent ;
- Sarah follow-up existe ;
- required J4 inclut Sarah follow-up ;
- Inès reste optionnelle ;
- Sarah follow-up se débloque après Nico ;
- Camille se débloque après Sarah follow-up ;
- aucun legacy J4 n’apparaît en mode expérimental ;
- flags de croisement existent dans les JSON écrits ;
- Sarah ne contient pas les chaînes interdites :
  - `Nico m’a dit`
  - `tu as demandé à Nico`
  - `vous vous êtes mis d’accord`
- Nico ne contient pas de savoir direct sur Sarah.

## 18. Conclusion

Le croisement Sarah ↔ Nico doit être réel mais simple.

Décision T209 :

- pas de runtime multi-fil complexe ;
- ajout d’une conversation courte `sarah_j4_followup_v2` ;
- progression Sarah → Nico → Sarah follow-up ;
- Camille seulement après fermeture du croisement ;
- required J4 ajusté pour inclure Sarah follow-up.

Prochaine tâche recommandée :
`T210 — Effets/routes et structure cible J4`

Validation :

- créer uniquement cette doc ;
- lancer :
  `python3 tools/validate_j1_v2_experimental.py`
- git status propre.
