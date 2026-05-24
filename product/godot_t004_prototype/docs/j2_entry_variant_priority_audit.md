# J2 — Audit des priorités d’entry variants

## 1. Problème

Chaque conversation J2 a plusieurs `entry_variants`, mais une seule entrée est affichée. Quand plusieurs flags J1 sont vrais en même temps, l’ordre des variantes décide quelle conséquence est visible et laquelle disparaît.

Le problème n’est pas forcément une incohérence. C’est un risque de **conséquence masquée** : une information reste vraie dans l’état, mais aucun message d’ouverture ne la fait sentir.

Exemple : Sarah peut avoir à la fois :

* `sarah_version_nico`
* `late_reply_sarah_meal_j1`

Si `after_nico_version` est prioritaire, Sarah parle de Nico et ne parle pas du repas. C’est cohérent si la version Nico est l’enjeu principal, mais le retard du repas peut disparaître émotionnellement.

## 2. Objectif de l’audit

Pour chaque personnage, cet audit liste :

* les entry variants actuelles ;
* les flags qui peuvent coexister ;
* si l’ordre actuel est cohérent ;
* les conséquences J1 qui risquent de disparaître ;
* des solutions futures possibles :
  * garder l’ordre actuel ;
  * réordonner les variantes ;
  * créer une variante combinée ;
  * intégrer un rappel dans une réponse ou un end text ;
  * utiliser un message différé futur.

Sources respectées : `docs/j1_to_j2_information_map.md`, `docs/j2_story_reframe.md`, `docs/j2_playable_structure.md`.

## 3. Sarah J2

### Entry variants actuelles

1. `after_nico_version` — flag `sarah_version_nico`
2. `after_camille_minimized` — flag `sarah_version_camille_minimized`
3. `after_domestic_presence` — flag `sarah_j1_domestic_presence`
4. `after_late_meal` — flag `late_reply_sarah_meal_j1`
5. `default`

### Flags Sarah J1 concernés

* `sarah_version_nico` / `used_nico_alibi_sarah`
* `sarah_version_camille_minimized` / `mentioned_camille_to_sarah` / `minimized_camille_to_sarah`
* `sarah_j1_domestic_presence`
* `late_reply_sarah_meal_j1`
* autres flags repas non prioritaires actuellement : `promised_sarah_later_j1`, `sarah_j1_uncertain_return`, `used_work_excuse_sarah_j1`

### Coexistence probable

Oui. La conversation Sarah principale J1 et Sarah repas J1 sont deux moments séparés. Donc :

* `sarah_version_nico` peut coexister avec `late_reply_sarah_meal_j1`.
* `sarah_version_camille_minimized` peut coexister avec `sarah_j1_domestic_presence`.
* `sarah_version_camille_minimized` peut aussi coexister avec `late_reply_sarah_meal_j1`.

### Lecture de l’ordre actuel

L’ordre actuel donne priorité à la **version principale** donnée à Sarah sur le domestique. C’est défendable : Nico ou Camille concernent directement l’explication de la nuit, alors que le repas est une conséquence émotionnelle / domestique.

Risque : `late_reply_sarah_meal_j1` est émotionnellement fort. S’il est masqué par `after_nico_version` ou `after_camille_minimized`, le joueur peut ne pas sentir le coût domestique du silence.

### Recommandation future

Priorité proposée si on décide de corriger plus tard :

1. `after_nico_and_late_meal` futur
2. `after_camille_and_late_meal` futur
3. `after_nico_version`
4. `after_camille_minimized`
5. `after_late_meal`
6. `after_domestic_presence`
7. `default`

Ne pas implémenter maintenant.

Solutions légères possibles :

* ajouter un rappel secondaire du repas dans un end text Sarah ;
* ajouter un message différé domestique après la scène principale ;
* créer seulement deux variantes combinées Sarah si le playtest montre que le repas disparaît trop souvent.

Statut : **ordre actuel acceptable pour MVP, mais risque recommandé à surveiller**.

## 4. Nico J2

### Entry variants actuelles

1. `alibi_used` — flag `used_nico_alibi_sarah`
2. `second_cover` — flag `asked_nico_second_cover_j1`
3. `asked_real_advice` — flag `asked_nico_real_advice_j1`
4. `ignored_respiration` — flag `ignored_nico_respiration_j1`
5. `default`

### Flags Nico J1 concernés

* Côté Sarah : `used_nico_alibi_sarah`, `sarah_version_nico`
* Côté Nico première scène : `asked_nico_hold_version`, `nico_alibi_requested`, `told_nico_stay_silent`, `confessed_camille_to_nico`, `vulnerable_to_nico`, `dismissed_nico_warning`
* Côté Nico respiration : `asked_nico_second_cover_j1`, `asked_nico_real_advice_j1`, `ignored_nico_respiration_j1`, `nico_j1_respiration_shared`, `joked_to_avoid_nico_j1`

### Coexistence probable

Oui. Les scènes Sarah, Nico et Nico respiration peuvent se cumuler. Cas importants :

* `used_nico_alibi_sarah` peut exister sans `asked_nico_hold_version` : Sarah a reçu Nico comme version, mais Nico n’a pas forcément été préparé.
* `used_nico_alibi_sarah` peut coexister avec `asked_nico_second_cover_j1`.
* `asked_nico_second_cover_j1` peut coexister avec `ignored_nico_respiration_j1` selon le timing de reprise tardive.
* `asked_nico_real_advice_j1` peut coexister avec une implication Nico antérieure dans l’alibi.

### Lecture de l’ordre actuel

`alibi_used` est prioritaire. Après T184, son texte reste hypothétique : Nico ne prétend plus savoir ce que Sarah a entendu. C’est donc acceptable même si Nico n’a pas été préparé.

Risque : `asked_real_advice` donne à Nico un rôle moral plus fort que `second_cover`, mais arrive après. Si les deux coexistent, la couverture peut masquer le fait que le joueur a demandé un vrai conseil.

Risque secondaire : `ignored_respiration` peut être émotionnellement fort, mais il est dernier avant default. L’ignorance peut donc disparaître si un alibi est aussi actif.

### Recommandation future

Variantes futures possibles :

* `alibi_prepared` — `used_nico_alibi_sarah` + `asked_nico_hold_version` ou `asked_nico_second_cover_j1`
* `alibi_unprepared` — `used_nico_alibi_sarah` sans préparation Nico
* `alibi_and_ignored` — alibi + `ignored_nico_respiration_j1`
* `real_advice_after_cover` — conseil moral après demande de couverture

Priorité proposée si correction :

1. `alibi_prepared`
2. `alibi_unprepared`
3. `real_advice_after_cover`
4. `asked_real_advice`
5. `second_cover`
6. `alibi_and_ignored` ou rappel secondaire selon ton choisi
7. `ignored_respiration`
8. `default`

Alternative plus simple : garder l’ordre et ajouter une phrase secondaire si `ignored_nico_respiration_j1` est vrai.

Statut : **acceptable après T184, mais Nico est le meilleur candidat à variantes combinées futures**.

## 5. Camille J2

### Entry variants actuelles

1. `tension_acknowledged` — flag `admitted_tension_to_camille`
2. `boundary_respected` — flag `protected_camille_boundary`
3. `minimized` — flag `minimized_with_camille`
4. `desire_too_early` — flag `early_desire_to_camille`
5. `default`

### Flags Camille J1 concernés

* `admitted_tension_to_camille`, `camille_trouble_acknowledged`
* `protected_camille_boundary`, `camille_boundary_respected`
* `minimized_with_camille`, `camille_minimized_j1`
* `early_desire_to_camille`, `camille_desire_too_early_j1`
* `uncertain_with_camille`, `camille_trouble_acknowledged`

### Coexistence probable

Les choix Camille J1 sont dans une même choice node principale, donc normalement exclusifs dans une partie standard. Le risque de coexistence directe est faible.

À noter : `camille_trouble_acknowledged` peut venir de `j1_02_admit_tension` ou `j1_02_uncertain`, mais J2 ne l’utilise pas directement comme entry variant.

### Lecture de l’ordre actuel

L’ordre actuel est acceptable si les flags sont exclusifs. En revanche, si un futur système pose `early_desire_to_camille` en plus d’un autre flag, `desire_too_early` devrait probablement primer plus haut : c’est une limite forte.

Le média Camille ajouté en T187 existe uniquement dans `tension_acknowledged`. Il peut rendre cette branche plus attractive au joueur, mais narrativement c’est cadré : le média est une trace de lieu, pas une récompense sexuelle, et il n’apparaît pas en cas de minimisation ou désir trop tôt.

### Recommandation future

* Si exclusivité confirmée : garder l’ordre actuel.
* Si non exclusif dans de futurs ajouts : remonter `desire_too_early` avant `tension_acknowledged`.
* Ne pas ajouter de média dans `desire_too_early`, `minimized` ou `default`.

Priorité future conditionnelle :

1. `desire_too_early` si coexistence possible
2. `tension_acknowledged`
3. `boundary_respected`
4. `minimized`
5. `default`

Statut : **validé pour MVP si les choix restent exclusifs**.

## 6. Maya J2

### Entry variants actuelles

1. `photo_possible` — flag `maya_photo_possible`
2. `played_dumb` — flag `played_dumb_with_maya`
3. `not_involve` — flag `told_maya_not_involve`
4. `timing_noted` — flag `maya_timing_noted`
5. `default`

### Flags Maya J1 concernés

* `played_dumb_with_maya`, `maya_suspicion_seeded_j1`
* `told_maya_needed_air`, `maya_timing_noted`
* `asked_maya_what_she_saw`, `maya_photo_possible`
* `told_maya_not_involve`

### Coexistence probable

Les choix Maya J1 sont normalement exclusifs, mais certains états sociaux peuvent s’additionner plus tard. `maya_photo_possible` est particulièrement fort parce qu’il active déjà un média. `told_maya_not_involve` est fort émotionnellement parce qu’il repousse Maya et justifie sa protection de Sarah.

### Lecture de l’ordre actuel

`photo_possible` prime actuellement sur `not_involve`. C’est acceptable si les choix J1 sont exclusifs. Si un futur système peut cumuler photo et rejet, l’ordre deviendrait discutable : dire à Maya de ne pas s’en mêler est socialement plus fort que la simple existence d’une trace photo.

Le média Maya photo groupe existe déjà. Il ne prouve rien, mais rend `photo_possible` visible et potentiellement dominant.

### Recommandation future

Si coexistence possible, priorité recommandée :

1. `not_involve`
2. `photo_possible`
3. `played_dumb`
4. `timing_noted`
5. `default`

Variante combinée possible : `not_involve_with_photo`.

Ne pas implémenter maintenant.

Statut : **ordre actuel acceptable pour MVP, mais à réévaluer si Maya cumule plusieurs signaux**.

## 7. Inès J2

### Entry variants actuelles

1. `opened_softly` — flag `opened_to_ines`
2. `kept_distance` — flag `kept_ines_at_distance`
3. `fuite_seed` — flag `ines_fuite_seed`
4. `too_direct` — flag `sexualized_ines_too_early`
5. `default`

### Flags Inès J1 concernés

* `opened_to_ines`
* `kept_ines_at_distance`
* `ines_fuite_seed`
* `sexualized_ines_too_early`

### Coexistence probable

Les choix Inès J1 sont normalement exclusifs. Le risque de coexistence est donc faible dans l’état actuel.

### Lecture de l’ordre actuel

Si les flags sont exclusifs, l’ordre est non bloquant. Si un futur système rend les flags cumulables, `sexualized_ines_too_early` devrait primer : c’est une limite de consentement forte. `ines_fuite_seed` devrait aussi être haut car il définit le danger principal d’Inès : devenir un refuge.

Le média Inès calme ajouté en T187 existe seulement dans `opened_softly`. Il rend cette branche plus attractive, mais reste cohérent : image calme, non corporelle, non romantique, non explicite. Il ne doit pas être copié vers `fuite_seed` ou `too_direct`.

### Recommandation future

Si non exclusif un jour :

1. `too_direct`
2. `fuite_seed`
3. `opened_softly`
4. `kept_distance`
5. `default`

Statut : **validé pour MVP si les choix restent exclusifs**.

## 8. Risques liés aux médias

### Camille média dehors

* Seulement dans `tension_acknowledged`.
* Risque : cette variante devient plus “récompensante”.
* Garde-fou actuel : pas de média si minimisation, désir trop tôt, boundary, default.
* Conclusion : acceptable. À surveiller en playtest pour vérifier que le média est perçu comme trace / climat, pas comme récompense.

### Inès média calme

* Seulement dans `opened_softly`.
* Risque : la branche d’ouverture douce devient plus attractive.
* Garde-fou actuel : pas de média si fuite, too_direct, kept_distance, default.
* Conclusion : acceptable. À surveiller pour éviter que le joueur lise Inès comme échappatoire visuelle.

## 9. Synthèse des risques

### Bloquant

* Une entry variant qui fait apparaître une information impossible.
* Nico qui saurait factuellement ce que Sarah a entendu sans préparation ou scène explicite.
* Camille/Maya/Inès qui parleraient depuis une information reçue dans une autre conversation.

État actuel : pas de bloquant identifié après T183/T184.

### Recommandé

* Sarah : le repas tardif peut être masqué par une version Nico/Camille.
* Nico : l’ignorance de respiration ou le vrai conseil peut être masqué par l’alibi.
* Maya : si coexistence future, `not_involve` devrait probablement primer sur `photo_possible`.

### Optionnel

* Variantes combinées Sarah pour repas + version principale.
* Variantes combinées Nico pour alibi préparé / non préparé / ignoré.
* Réordonnancement Inès/Camille seulement si les flags cessent d’être exclusifs.

## 10. Recommandations pour T189 ou T190

### Option A — ne rien modifier avant playtest

Recommandé à court terme. Le J2 est jouable, cohérent et les risques restants sont surtout des conséquences masquées, pas des incohérences manifestes.

### Option B — créer seulement 2 variantes combinées

Cible minimale si le playtest confirme une perte de conséquence :

* Sarah `after_nico_and_late_meal`
* Nico `alibi_and_ignored`

### Option C — réordonner certaines entry variants

À envisager seulement si les flags peuvent coexister :

* Maya `not_involve` avant `photo_possible`
* Inès `too_direct` avant `opened_softly`
* Camille `desire_too_early` avant `tension_acknowledged`

### Option D — ajouter des rappels secondaires

Sans créer de nouvelle branche :

* une phrase dans une réponse ;
* un end text ;
* une notification différée ;
* un message de retour après la scène principale.

Cette option est probablement la moins risquée pour Sarah repas et Nico respiration.

## 11. Sortie attendue

### Priorité actuelle validée ou non par personnage

* Sarah : **partiellement validée**. Priorité version principale OK, mais repas tardif à surveiller.
* Nico : **partiellement validée**. Texte désormais hypothétique OK, mais rôle conseil / alibi / silence peut mériter variantes combinées.
* Camille : **validée MVP** si choix exclusifs.
* Maya : **validée MVP** si choix exclusifs ; sinon `not_involve` devrait monter.
* Inès : **validée MVP** si choix exclusifs ; sinon `too_direct` et `fuite_seed` devraient monter.

### Recommandations concrètes

1. Ne rien modifier avant un playtest J2 complet.
2. Pendant le playtest, noter les runs où :
   * Sarah ne mentionne jamais le repas malgré `late_reply_sarah_meal_j1` ;
   * Nico ne mentionne jamais l’ignorance malgré `ignored_nico_respiration_j1` ;
   * Maya photo masque un rejet explicite ;
   * Inès ouverture douce masque une limite plus importante.
3. Si correction nécessaire, privilégier deux variantes combinées maximum avant J3.

### Ce qu’il ne faut pas faire maintenant

* Ne pas multiplier toutes les combinaisons possibles.
* Ne pas ajouter de nouvelles branches sans preuve playtest.
* Ne pas réordonner Camille/Inès tant que leurs choix J1 restent exclusifs.
* Ne pas ajouter de média pour compenser une conséquence masquée.
* Ne pas faire d’une photo une preuve ou une récompense.

### Décision proposée avant J3

Décision recommandée : **playtest d’abord, corrections combinées ensuite seulement si nécessaire**.

Le J2 V2 est suffisamment stable pour être joué. Les priorités actuelles ne bloquent pas le MVP, mais Sarah et Nico sont les deux axes à observer avant de passer à J3.
