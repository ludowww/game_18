# J4 V2 — Matrice arcs/personnages

## 0. Statut et périmètre

Document de design pour le Jour 4 V2. Cette matrice précise, avant toute structure technique ou écriture de dialogues, le rôle de chaque personnage dans J4, ses savoirs, ses limites, ses variables et sa trajectoire long terme.

Contraintes T208 :

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
- `docs/j3_character_voice_and_repetition_audit.md` ;
- `docs/j3_v2_dialogue_audit.md`.

## 1. Rôle de cette matrice

Cette matrice doit empêcher l’écriture “en silo”.

Avant d’écrire J4, on doit savoir pour chaque personnage :

- où il/elle est dans la journée ;
- pourquoi il/elle écrit ;
- ce qu’il/elle sait ;
- ce qu’il/elle ne peut pas savoir ;
- ce que la scène fait avancer ;
- quelle dynamique long terme elle prépare ;
- quelle variable elle met sous pression.

J4 doit être une journée de priorités, de délais et de premiers croisements visibles.

## 2. Tableau synthétique J4

| Personnage | Bloc temporel | Lieu / contexte | Humeur | Rôle J4 | Scène obligatoire ? | Variables clés | Croisement potentiel | Route long terme préparée |
|---|---|---|---|---|---|---|---|---|
| Sarah | Début de matinée + possible écho soirée | Cuisine / table / quotidien | Attentive, fatiguée, prudente | Remarque un détail, teste les gestes | Oui | `confiance_sarah`, `distance_sarah`, `coherence`, `fatigue_emotionnelle` | Sarah ↔ Nico | Réparation lente ou distance |
| Nico | Fin de matinée / consultation + seed soirée | Trajet / réveil tardif / console / vie hors joueur | Drôle, loyal, moins disponible | Ami, alibi possible, limite | Oui | `dette_nico`, `risque_exposition`, `coherence`, `fatigue_emotionnelle` | Sarah ↔ Nico, potentiel Nico ↔ Maya futur | Ami loyal ou ami fatigué |
| Camille | Pause midi / travail | Travail / pause courte | Tendue, troublée, concentrée mais distraite | Tension, limite, désir contenu | Oui | `respect_camille`, `pression_camille`, `tension_camille`, `risque_exposition` | Indirect avec Sarah par disponibilité du joueur | Tension respectée ou fermeture |
| Maya | Fin d’après-midi | Groupe / transport / pause / fil social | Piquante, observatrice, prudente | Ambiance sociale, signaux faibles | Oui | `suspicion_maya`, `risque_exposition`, `coherence`, `fatigue_emotionnelle` | Groupe, futur Nico ↔ Maya | Complice sociale ou suspicion renforcée |
| Inès | Soir tard | Chambre / fenêtre / téléphone repris | Douce, hésitante, prudente | Respiration optionnelle, test de fuite | Non | `fuite_ines`, `coherence`, `culpabilite`, `fatigue_emotionnelle` | Aucun direct ; miroir de fuite | Distance douce ou refuge problématique |

## 3. Sarah J4

### Rôle dans J4

Sarah ouvre la journée. Elle ne vient pas avec une révélation. Elle remarque un détail.

Elle représente :

- le quotidien ;
- les gestes ;
- la cohérence entre paroles et actes ;
- la fatigue d’attendre ;
- la possibilité de réparation ou de distance.

### Bloc temporel

Début de matinée.

### Lieu / contexte

- cuisine ;
- table ;
- tasse ;
- objet domestique ;
- début de journée.

### Humeur

Variable selon J3 :

- attentive si le joueur a promis des gestes ;
- prudente si le joueur a été honnête ;
- distante si le joueur a demandé encore du temps ;
- froide si le joueur s’est défendu.

### Flags J3 à exploiter

- `j3_sarah_promises_actions`
- `j3_sarah_place_named`
- `j3_sarah_honest_uncertainty`
- `j3_sarah_no_false_promise`
- `j3_sarah_more_time`
- `j3_sarah_waiting_continues`
- `j3_sarah_defensive`
- `j3_sarah_feels_unheard`

### Savoirs Sarah

Sarah sait :

- ce que le joueur lui a dit ;
- si elle a eu des promesses ;
- si le joueur a demandé du temps ;
- si le joueur a minimisé ou s’est défendu ;
- ce qu’elle observe dans le quotidien.

Sarah soupçonne :

- qu’il y a peut-être un écart entre les mots et les gestes ;
- que le joueur peut attendre avant de répondre ;
- que certains détails ne collent pas.

Sarah ignore :

- ce que Nico a dit ;
- ce que Camille a dit ;
- ce que Maya a vu ou pensé ;
- ce qu’Inès représente pour le joueur ;
- toute vérité privée hors de son fil.

### Objectif de scène

Créer une tension douce :

- Sarah remarque quelque chose ;
- le joueur doit choisir s’il répond directement ou temporise ;
- possibilité de préparer le croisement Sarah ↔ Nico.

### Postures de choix possibles

1. Répondre directement et reconnaître le détail.
2. Dire une vérité prudente.
3. Temporiser.
4. Se défendre.
5. Préparer une réponse via Nico.

### Variables concernées

- `confiance_sarah`
- `distance_sarah`
- `coherence`
- `risque_exposition`
- `fatigue_emotionnelle`
- `culpabilite`

### Flags J4 possibles

- `j4_sarah_morning_detail_noted`
- `j4_sarah_waits_for_action`
- `j4_sarah_small_incoherence`
- `j4_player_given_direct_sarah_answer`
- `j4_player_delayed_sarah_answer`
- `j4_sarah_answer_pending_nico_check`
- `j4_sarah_delay_noticed`

### Risques d’écriture

À éviter :

- Sarah omnisciente ;
- Sarah détective ;
- Sarah trop juge ;
- Sarah qui sait que Nico a été contacté ;
- Sarah qui parle trop comme une thérapeute.

### Voix attendue

Sarah doit sonner :

- intime ;
- quotidienne ;
- fatiguée ;
- précise sur les petits gestes ;
- blessée mais pas explosive.

Exemples de direction :

- `Je ne sais pas si c’est important, mais j’ai remarqué un détail.`
- `Ce matin, j’ai attendu un peu avant de t’écrire.`
- `Je crois que je regarde trop les petits trucs maintenant.`

### Trajectoire long terme préparée

- Réparation si gestes tenus.
- Distance si délais répétés.
- Perte de confiance si défense/minimisation.
- Intimité domestique future seulement si confiance haute et distance basse.

## 4. Nico J4

### Rôle dans J4

Nico est le premier vrai croisement dynamique. Il peut aider, mais il n’est pas disponible gratuitement.

Il représente :

- l’amitié ;
- l’alibi ;
- le délai ;
- le coût de demander de l’aide ;
- la vie hors joueur.

### Bloc temporel

Fin de matinée / début de midi. Seed soirée jeux vidéo dans la même conversation MVP.

### Lieu / contexte

- réveil tardif ;
- trajet ;
- canapé ;
- préparation d’une soirée console ;
- disponibilité entre deux choses.

### Humeur

- drôle ;
- loyal ;
- un peu fatigué ;
- moins disponible ;
- direct.

### Flags J3 à exploiter

- `j3_nico_limit_respected`
- `j3_nico_no_longer_tool`
- `j3_nico_more_help_requested`
- `j3_nico_pressure_continues`
- `j3_nico_knows_sarah_observes` ou futur renommage
- `j3_sarah_gestures_pressure_named` ou futur renommage
- `j3_nico_life_outside_player_teased`
- `j3_nico_maya_thread_possible`

Note : si les flags ambigus autour de Sarah observatrice n’ont pas encore été renommés, les utiliser prudemment ou prévoir un ticket séparé de renommage avant J4.

### Savoirs Nico

Nico sait :

- ce que le joueur lui dit ;
- si le joueur l’a utilisé comme alibi ;
- si le joueur lui a demandé de l’aide ;
- si le joueur l’a libéré d’un rôle ;
- si le joueur lui parle de pression Sarah.

Nico soupçonne :

- que le joueur peut encore chercher une version ;
- que Sarah peut sentir les délais ;
- que son aide devient coûteuse.

Nico ignore :

- ce que Sarah a réellement écrit ;
- ce que Camille ressent précisément ;
- ce que Maya sait ;
- ce qu’Inès représente.

### Objectif de scène

Faire sentir que consulter Nico a un coût :

- délai ;
- dette ;
- risque ;
- fatigue ;
- mais aussi vraie amitié possible.

### Postures de choix possibles

1. Demander conseil sans demander alibi.
2. Demander couverture.
3. Libérer Nico.
4. Plaisanter pour esquiver.
5. Parler de la soirée jeux vidéo.

### Variables concernées

- `dette_nico`
- `risque_exposition`
- `coherence`
- `fatigue_emotionnelle`
- `distance_sarah`

### Flags J4 possibles

- `j4_player_checked_with_nico`
- `j4_nico_helped_version`
- `j4_nico_refused_more_alibi`
- `j4_nico_warned_about_delay`
- `j4_nico_not_a_service`
- `j4_nico_game_evening_seed`
- `j4_nico_available_later`

### Risques d’écriture

À éviter :

- Nico bouton magique ;
- Nico trahit le joueur ;
- Nico devient conseiller conjugal ;
- Nico sait ce que Sarah pense ;
- Nico clown permanent.

### Voix attendue

Nico doit sonner :

- pote ;
- drôle ;
- un peu sec quand il faut ;
- loyal mais pas corvéable.

Exemples de direction :

- `je peux t’aider à pas empirer. pas à réécrire la journée.`
- `je suis là, mais pas en service illimité.`
- `ce soir je lance la console. si tu viens, tu mens pas à ma manette.`

### Trajectoire long terme préparée

- Amitié renforcée si respectée.
- Dette lourde si utilisée.
- Refus futur si pression continue.
- Soirée jeux vidéo comme vraie respiration ou alibi risqué.
- Dynamique sociale Nico ↔ Maya possible plus tard.

## 5. Camille J4

### Rôle dans J4

Camille apporte la tension du midi / travail. Elle n’est pas seulement un fil de désir : elle a une journée, une pause, une limite.

Elle représente :

- tension ;
- désir contenu ;
- limites ;
- respect ;
- risque de pression.

### Bloc temporel

Pause midi / début d’après-midi.

### Lieu / contexte

- travail ;
- pause courte ;
- téléphone consulté vite ;
- obligation de retourner à autre chose.

### Humeur

Selon J3 :

- ouverte mais prudente ;
- frustrée mais respectueuse ;
- méfiante si pression haute ;
- froide si minimisée.

### Flags J3 à exploiter

- `j3_camille_recognized_without_using`
- `j3_camille_not_escape_route`
- `j3_camille_boundary_kept`
- `j3_camille_confusion_not_shifted`
- `j3_camille_tension_reopened`
- `j3_camille_pressure_rises`
- `j3_camille_minimized_again`
- `j3_camille_closes_badly`

### Savoirs Camille

Camille sait :

- ce qu’elle a vécu avec le joueur ;
- si le joueur a reconnu la tension ;
- si le joueur a posé une limite ;
- si le joueur a minimisé ;
- si le joueur a cherché refuge ;
- si le joueur a rouvert la tension.

Camille soupçonne :

- que le joueur peut la chercher comme sortie ;
- que la tension peut devenir plus forte ;
- que le joueur n’est pas toujours clair.

Camille ignore :

- les détails Sarah ;
- les échanges Nico ;
- le regard Maya ;
- Inès.

### Objectif de scène

Faire sentir une tension dans un temps contraint :

- Camille écrit alors qu’elle devrait travailler ;
- elle teste le joueur ;
- elle peut ouvrir une ambiguïté sans devenir une récompense.

### Postures de choix possibles

1. Taquiner légèrement.
2. Respecter sa pause.
3. Nommer le trouble.
4. Forcer / relancer trop fort.
5. Couper court proprement.

### Variables concernées

- `respect_camille`
- `pression_camille`
- `tension_camille`
- `risque_exposition`
- `coherence`

### Flags J4 possibles

- `j4_camille_work_pause`
- `j4_camille_limit_tested`
- `j4_camille_teased_during_work`
- `j4_camille_trouble_named`
- `j4_camille_pressure_too_high`
- `j4_camille_boundary_respected`
- `j4_camille_pause_cut_short`

### Risques d’écriture

À éviter :

- Camille récompense sexuelle ;
- Camille trop théorique ;
- Camille trop disponible ;
- Camille qui ignore son travail ;
- tension trop explicite ;
- photo suggestive trop tôt.

### Voix attendue

Camille doit sonner :

- précise ;
- légèrement provocante ;
- contrainte par le temps ;
- troublée mais pas offerte ;
- capable de couper court.

Exemples de direction :

- `pause de trois minutes.`
- `je suis censée bosser, donc évidemment je t’écris.`
- `tu joues avec la limite ou tu la tiens ?`

### Trajectoire long terme préparée

- Route désir progressif si respect haut / pression basse.
- Fermeture si pression haute.
- Tension sexuelle future préparée verbalement.
- Pas de média suggestif J4.

## 6. Maya J4

### Rôle dans J4

Maya montre que les contradictions commencent à avoir une odeur sociale. Elle n’apporte pas de preuve. Elle rend le monde vivant.

Elle représente :

- groupe ;
- ambiance ;
- signaux faibles ;
- ironie ;
- regard social.

### Bloc temporel

Fin d’après-midi.

### Lieu / contexte

- transport ;
- pause ;
- fil de groupe ;
- interaction sociale ;
- ambiance collective.

### Humeur

- piquante ;
- prudente ;
- un peu amusée ;
- pas dupe ;
- pas encore accusatrice.

### Flags J3 à exploiter

- `j3_maya_asked_for_signals`
- `j3_maya_social_signals_opened`
- `j3_maya_group_boundary_requested`
- `j3_maya_direct_channel_requested`
- `j3_maya_defensive_again`
- `j3_maya_suspicion_reinforced`
- `j3_maya_others_may_notice`
- `j3_maya_social_thread_possible`

### Savoirs Maya

Maya sait :

- ce que le joueur lui a dit ;
- si le joueur lui a demandé de rester discrète ;
- si le joueur a admis un malaise ;
- si le joueur s’est défendu ;
- ce qu’elle peut observer socialement.

Maya soupçonne :

- que le joueur ajuste son ton selon les personnes ;
- que l’ambiance n’est pas neutre ;
- que d’autres peuvent sentir un décalage.

Maya ignore :

- les détails Sarah ;
- les échanges Nico ;
- ce que Camille ressent ;
- Inès.

### Objectif de scène

Faire sentir que le social continue :

- les délais se voient ;
- les tons changent ;
- le groupe respire autour du joueur ;
- Maya est un thermomètre, pas une preuve.

### Postures de choix possibles

1. Accepter son regard.
2. Demander du direct.
3. Minimiser.
4. Demander qui d’autre remarque.
5. Plaisanter.

### Variables concernées

- `suspicion_maya`
- `risque_exposition`
- `coherence`
- `fatigue_emotionnelle`

### Flags J4 possibles

- `j4_maya_group_mood_noted`
- `j4_maya_tone_shift_seen`
- `j4_maya_direct_channel_kept`
- `j4_maya_suspicion_pushed`
- `j4_maya_others_possibly_noticed`
- `j4_maya_social_delay_seen`

### Risques d’écriture

À éviter :

- Maya détective ;
- Maya donne des noms ;
- Maya prouve ;
- Maya parle pour Sarah ;
- Maya devient omnisciente.

### Voix attendue

Maya doit sonner :

- vive ;
- sociale ;
- ironique ;
- pas solennelle ;
- capable de dire “je peux me tromper” sans lâcher le sujet.

Exemples de direction :

- `j’ai réussi à ne pas faire de commentaire pendant presque toute la journée.`
- `l’ambiance a changé de température. oui, c’est scientifique.`
- `je dis pas que ça prouve quelque chose. je dis que ça se voit un peu.`

### Trajectoire long terme préparée

- Suspicion sociale progressive.
- Possibilité d’un groupe plus vivant.
- Potentiel Nico ↔ Maya futur.
- Pas de preuve sociale immédiate.

## 7. Inès J4

### Rôle dans J4

Inès est optionnelle. Elle arrive tard, comme respiration ou risque de fuite.

Elle représente :

- calme ;
- hésitation ;
- distance ;
- douceur ;
- question : présence ou refuge ?

### Bloc temporel

Soir tard.

### Lieu / contexte

- chambre ;
- fenêtre ;
- silence ;
- téléphone repris plusieurs fois ;
- message tardif.

### Humeur

Selon J3 :

- douce mais prudente ;
- distante si recul ;
- plus méfiante si le joueur l’a utilisée comme refuge ;
- ouverte si présence claire.

### Flags J3 à exploiter

- `j3_ines_clear_presence`
- `j3_ines_not_used_as_escape`
- `j3_ines_soft_distance`
- `j3_ines_boundary_respected`
- `j3_ines_refuge_again`
- `j3_ines_escape_risk_high`
- `j3_ines_step_back`
- `j3_ines_not_pulled_in`

### Savoirs Inès

Inès sait :

- ce que le joueur lui a dit ;
- si le joueur a cherché du calme ;
- si le joueur a posé une limite ;
- si le joueur a essayé de ne pas l’utiliser.

Inès soupçonne :

- qu’elle peut être utilisée comme refuge ;
- que le joueur arrive tard quand il est fatigué ;
- que le calme peut devenir une fuite.

Inès ignore :

- Sarah ;
- Nico ;
- Camille ;
- Maya ;
- le groupe ;
- les versions.

### Objectif de scène

Tester la fuite :

- le joueur vient-il vers elle comme personne ?
- ou comme cachette ?

### Postures de choix possibles

1. Chercher du calme.
2. Dire clairement qu’on ne veut pas l’utiliser.
3. Se retirer.
4. Prolonger trop.
5. Répondre tardivement.

### Variables concernées

- `fuite_ines`
- `coherence`
- `culpabilite`
- `fatigue_emotionnelle`

### Flags J4 possibles

- `j4_ines_late_reply`
- `j4_ines_refuge_risk`
- `j4_ines_clear_distance`
- `j4_ines_soft_presence`
- `j4_player_avoids_using_ines`
- `j4_ines_keeps_distance`

### Risques d’écriture

À éviter :

- Inès thérapeute ;
- Inès récompense de calme ;
- Inès omnisciente ;
- Inès sexualisée trop tôt ;
- Inès trop parfaite.

### Voix attendue

Inès doit sonner :

- douce ;
- lente ;
- hésitante ;
- pas trop explicative ;
- capable de poser une limite avec peu de mots.

Exemples de direction :

- `j’ai écrit, effacé, réécrit.`
- `je réponds tard parce que je ne voulais pas répondre vite.`
- `si tu viens juste chercher du silence, je crois que je vais le sentir.`

### Trajectoire long terme préparée

- Présence douce si fuite basse.
- Distance si refuge répété.
- Intimité très lente possible seulement si elle sort du rôle d’échappatoire.

## 8. Matrice des croisements J4

### Sarah ↔ Nico

Type : croisement principal.

Déclencheur : Sarah remarque un détail ou une incohérence faible.

Possibilité joueur : contacter Nico avant de répondre.

Risques :

- délai visible ;
- dette Nico ;
- version plus propre mais moins spontanée ;
- Sarah remarque que le joueur temporise.

Flags :

- `j4_player_checked_with_nico`
- `j4_sarah_answer_pending_nico_check`
- `j4_nico_helped_version`
- `j4_nico_refused_more_alibi`
- `j4_sarah_delay_noticed`

### Sarah ↔ Camille

Type : croisement indirect.

Déclencheur : le joueur répond à Camille pendant qu’un geste Sarah est attendu.

Risques :

- Sarah sent une absence ;
- Camille sent qu’elle devient une sortie ;
- tension augmente sans preuve.

Flags possibles :

- `j4_player_prioritized_camille_over_sarah`
- `j4_sarah_evening_presence_failed`
- `j4_camille_pressure_too_high`

À ne pas implémenter fortement en J4 MVP sauf préparation.

### Nico ↔ Maya

Type : préparation future.

Déclencheur : Nico évoque une vie sociale ; Maya évoque une ambiance.

Risque : le joueur comprend que le groupe bouge sans lui.

Flags possibles :

- `j4_nico_social_life_visible`
- `j4_maya_social_thread_possible`

Ne pas révéler de romance ou de relation identifiable.

### Inès ↔ autres

Type : miroir de fuite.

Déclencheur : le joueur va vers Inès après tensions Sarah/Nico/Camille/Maya.

Risque : Inès devient cachette.

Flags possibles :

- `j4_ines_refuge_risk`
- `j4_player_avoids_using_ines`

Inès ne doit pas connaître les autres fils.

## 9. Required / optionnel recommandé

Required J4 :

- Sarah J4
- Nico J4
- Camille J4
- Maya J4

Optionnel :

- Inès J4

Justification : même logique que J3, mais avec une progression plus tendue.

Sarah ouvre la journée. Nico permet le croisement. Camille installe le midi/tension. Maya donne le social/fin d’après-midi. Inès offre une respiration tardive, non bloquante.

## 10. Flags J4 à réserver

Liste initiale à utiliser plus tard en structure/écriture.

### Sarah

- `j4_sarah_morning_detail_noted`
- `j4_sarah_waits_for_action`
- `j4_sarah_small_incoherence`
- `j4_player_given_direct_sarah_answer`
- `j4_player_delayed_sarah_answer`
- `j4_sarah_answer_pending_nico_check`
- `j4_sarah_delay_noticed`

### Nico

- `j4_player_checked_with_nico`
- `j4_nico_helped_version`
- `j4_nico_refused_more_alibi`
- `j4_nico_warned_about_delay`
- `j4_nico_not_a_service`
- `j4_nico_game_evening_seed`
- `j4_nico_available_later`

### Camille

- `j4_camille_work_pause`
- `j4_camille_limit_tested`
- `j4_camille_teased_during_work`
- `j4_camille_trouble_named`
- `j4_camille_pressure_too_high`
- `j4_camille_boundary_respected`
- `j4_camille_pause_cut_short`

### Maya

- `j4_maya_group_mood_noted`
- `j4_maya_tone_shift_seen`
- `j4_maya_direct_channel_kept`
- `j4_maya_suspicion_pushed`
- `j4_maya_others_possibly_noticed`
- `j4_maya_social_delay_seen`

### Inès

- `j4_ines_late_reply`
- `j4_ines_refuge_risk`
- `j4_ines_clear_distance`
- `j4_ines_soft_presence`
- `j4_player_avoids_using_ines`
- `j4_ines_keeps_distance`

## 11. Décisions pour T209

T209 devra maintenant décider :

1. le design précis du croisement Sarah ↔ Nico ;
2. si ce croisement est seulement narratif ou soutenu par runtime ;
3. les choix concrets Sarah du matin ;
4. les choix Nico de consultation ;
5. les flags réellement conservés ;
6. les effets exacts ;
7. les garde-fous anti-omniscience ;
8. la forme MVP de l’alibi J4.

## 12. Conclusion

Cette matrice permet de passer à la prochaine étape sans écrire encore les dialogues.

J4 doit être conçu autour de :

- Sarah : détail du matin ;
- Nico : consultation et disponibilité limitée ;
- Camille : pause travail et tension ;
- Maya : social de fin d’après-midi ;
- Inès : soir tard optionnel.

Prochaine tâche recommandée :
`T209 — Design du croisement Sarah ↔ Nico J4`

Validation :

- créer uniquement cette doc ;
- lancer :
  `python3 tools/validate_j1_v2_experimental.py`
- git status propre.
