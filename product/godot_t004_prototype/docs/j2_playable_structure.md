# Jour 2 — Structure jouable

## 1. Objectif opérationnel

Le Jour 2 doit être jouable en MVP avec peu de scènes, mais avec des conséquences visibles du Jour 1.

Objectifs :

- faire sentir que le Jour 1 a laissé des traces ;
- utiliser quelques flags et stats structurants ;
- éviter d’ouvrir trop de branches ;
- installer une progression matin → après-midi → soir ;
- préparer le Jour 3.

Le J2 ne doit pas être une expansion incontrôlée du J1. Il doit transformer les intentions de `j2_design_brief.md` et `j2_dynamic_systems.md` en architecture jouable, testable et maintenable.

Principe MVP : peu de conversations, peu de systèmes nouveaux, mais une lecture claire des conséquences.

## 2. Transition J1 → J2

Décision proposée : pour le MVP, le Jour 2 commence via une transition explicite après la fin du J1 V2.

Condition de fin J1 V2 :

- les cinq scènes cœur sont terminées ;
- Sarah repas et Nico respiration sont disponibles ;
- idéalement les deux scènes de respiration sont terminées ou laissées dans un état résolu.

Décision à figer avant implémentation :

- faut-il exiger Sarah repas + Nico respiration pour passer au Jour 2 ?
- ou autoriser le passage J2 dès que les cinq scènes cœur sont terminées ?

Recommandation MVP : exiger les cinq scènes cœur, puis laisser Sarah repas et Nico respiration optionnels mais fortement guidés. Si elles ne sont pas faites, J2 démarre avec un état de distance, dette ou fatigue plus fort.

Conséquence structurelle : le passage J2 ne doit pas effacer les états `left_open`, les flags J1, les variables relationnelles ou l’historique utile.

## 3. Blocs temporels J2

Utiliser trois blocs simples :

- J2 matin ;
- J2 après-midi ;
- J2 soir.

Ne pas créer d’horloge précise.

Chaque conversation J2 doit appartenir à un bloc. Le bloc sert à :

- guider le rythme ;
- rendre les retards et silences lisibles ;
- éviter que toutes les conversations soient disponibles dès le début ;
- préparer les tests de disponibilité.

Le joueur ne gère pas un planning. Il ressent seulement que répondre maintenant ou plus tard change le ton.

## 4. Conversations J2 MVP

Créer à terme cinq conversations principales maximum.

### 1. Sarah J2 matin

Conversation id proposée : `sarah_j2_v2`

Rôle :

- cohérence domestique ;
- conséquence de la version donnée J1 ;
- retour ou non-retour ;
- distance / confiance.

Statut : obligatoire.

Moment : matin.

Débloquée : au début du J2.

Remarque : Sarah doit être le point d’ancrage émotionnel du lendemain. Elle ne doit pas être uniquement accusatrice.

### 2. Nico J2 matin

Conversation id proposée : `nico_j2_v2`

Rôle :

- dette ;
- alibi ;
- version qui tient ou non ;
- limite amicale.

Statut : obligatoire.

Moment : matin.

Débloquée : au début du J2 ou après Sarah selon la structure retenue.

Remarque : Nico J2 est le premier test concret de l’alibi. Il reste drôle, mais son humour peut commencer à coûter.

### 3. Camille J2 après-midi

Conversation id proposée : `camille_j2_v2`

Rôle :

- tension ;
- limite ;
- refus d’être une parenthèse ;
- conséquence du choix Camille J1.

Statut : obligatoire.

Moment : après-midi.

Débloquée : après Sarah ou Nico, selon les flags Camille.

Remarque : Camille ne doit pas être réduite à la tentation. Sa route J2 doit aussi porter le respect, la limite et le refus d’être minimisée.

### 4. Maya J2 après-midi

Conversation id proposée : `maya_j2_v2`

Rôle :

- regard social ;
- photo de groupe ;
- timing ;
- suspicion.

Statut : obligatoire pour MVP si le média Maya a été vu ou si suspicion élevée. Sinon semi-optionnelle.

Moment : après-midi.

Débloquée : après Camille ou après un seuil de suspicion / risque d’exposition.

Remarque : Maya peut observer et interpréter, mais ne doit pas prouver.

### 5. Inès J2 soir

Conversation id proposée : `ines_j2_v2`

Rôle :

- espace calme ;
- fuite émotionnelle ;
- conséquence de l’ouverture ou maladresse J1.

Statut : optionnelle ou semi-optionnelle.

Moment : soir.

Débloquée : selon flags Inès ou fatigue émotionnelle.

Remarque : Inès J2 peut offrir une respiration, mais ne doit pas devenir romance explicite trop tôt.

## 5. Disponibilité initiale

Au début du J2 :

- Sarah disponible ;
- Nico disponible.

Ne pas rendre toutes les conversations disponibles immédiatement.

Après Sarah/Nico :

- Camille devient disponible ;
- Maya devient disponible ensuite ;
- Inès arrive plus tard si conditions remplies ou si besoin de respiration.

Recommandation de déblocage MVP :

1. J2 démarre avec Sarah + Nico.
2. Après au moins une des deux scènes matin, Camille peut apparaître.
3. Après Camille ou après un marqueur social, Maya peut apparaître.
4. Inès apparaît en soirée si ses flags J1 ou la fatigue émotionnelle le justifient.

Cette structure garde une sensation de téléphone vivant sans ouvrir cinq fils simultanés.

## 6. Scènes obligatoires pour terminer J2 MVP

Obligatoires :

- Sarah J2 ;
- Nico J2 ;
- Camille J2 ;
- Maya J2.

Optionnelle :

- Inès J2.

Le J2 peut se terminer même sans Inès, mais Inès doit être disponible si les flags J1 la rendent pertinente.

Condition de fin MVP : les quatre scènes obligatoires sont terminées. Ensuite, un bouton ou événement de transition peut proposer de passer au Jour 3.

## 7. Flags J1 structurants par scène

### Sarah J2

Utiliser prioritairement :

- `sarah_version_needed_air` ;
- `sarah_version_nico` ;
- `sarah_version_camille_minimized` ;
- `sarah_version_emotional_confusion` ;
- `late_reply_sarah_meal_j1` ;
- `sarah_j1_domestic_presence` ;
- `used_work_excuse_sarah_j1`.

Variables :

- `confiance_sarah` ;
- `distance_sarah` ;
- `intimite_sarah` ;
- `coherence` ;
- `culpabilite`.

### Nico J2

Utiliser prioritairement :

- `used_nico_alibi_sarah` ;
- `nico_alibi_requested` ;
- `asked_nico_second_cover_j1` ;
- `asked_nico_real_advice_j1` ;
- `ignored_nico_respiration_j1` ;
- `nico_j1_respiration_shared`.

Variables :

- `dette_nico` ;
- `coherence` ;
- `risque_exposition` ;
- `fatigue_emotionnelle`.

### Camille J2

Utiliser prioritairement :

- `admitted_tension_to_camille` ;
- `protected_camille_boundary` ;
- `minimized_with_camille` ;
- `early_desire_to_camille` ;
- `uncertain_with_camille`.

Variables :

- `tension_camille` ;
- `respect_camille` ;
- `pression_camille` ;
- `intimite_camille` ;
- `culpabilite`.

### Maya J2

Utiliser prioritairement :

- `maya_photo_possible` ;
- `asked_maya_what_she_saw` ;
- `played_dumb_with_maya` ;
- `told_maya_not_involve`.

Variables :

- `suspicion_maya` ;
- `coherence` ;
- `risque_exposition`.

### Inès J2

Utiliser prioritairement :

- `opened_to_ines` ;
- `kept_ines_at_distance` ;
- `ines_fuite_seed` ;
- `sexualized_ines_too_early`.

Variables :

- `fuite_ines` ;
- `fatigue_emotionnelle` ;
- `culpabilite`.

## 8. Entry variants J2

Chaque conversation J2 doit avoir des `entry_variants`, mais en nombre limité.

Recommandation :

- 3 à 5 variantes par conversation maximum ;
- une variante `default` ;
- une variante forte basée sur flags ;
- une variante basée sur stats ;
- une variante tardive / `left_open` seulement si utile.

Exemple Sarah :

- `default` ;
- `after_nico_version` ;
- `after_camille_minimized` ;
- `after_domestic_presence` ;
- `low_trust`.

Exemple Nico :

- `default` ;
- `alibi_used` ;
- `debt_high` ;
- `asked_real_advice` ;
- `ignored_respiration`.

Les variantes doivent changer le raccord d’ouverture, pas multiplier les scènes complètes. Elles doivent toujours converger vers un choix lisible.

## 9. Choix J2

Chaque scène J2 doit viser :

- 2 à 3 choix uniques avant choix multiple ;
- 3 à 4 choix multiples maximum.

Les choix multiples doivent représenter des postures :

- clarifier ;
- esquiver ;
- demander du temps ;
- poser une limite ;
- utiliser ou libérer quelqu’un ;
- chercher une fuite.

Pas de choix visible “ne pas répondre” si `left_open` peut le porter.

Les choix uniques doivent respecter la convention `_single_reply_` documentée dans `j1_v2_mvp_conventions.md`.

## 10. Médias J2

MVP : un seul média J2 au départ.

Recommandation : Maya J2 peut réutiliser la photo de groupe ou en envoyer une variation. Le média doit rester ambigu. Il ne doit pas prouver.

Possibilité future : Camille peut avoir un média symbolique si respect / tension / intimité le justifient, mais pas dans la première passe J2.

Règles :

- pas de média récompense ;
- pas de preuve absolue ;
- pas de média explicite dans le MVP ;
- conserver fallback caption + zoom ;
- réutiliser les conventions `type: "media"` existantes.

## 11. Dynamique alibi J2

Nico J2 doit être le premier test concret du système d’alibi.

États à documenter :

- pas d’alibi Nico ;
- alibi demandé mais fragile ;
- alibi renforcé ;
- alibi coûteux ;
- alibi refusé.

Ne pas encore créer un système complexe.

Commencer par flags + variables existantes :

- `used_nico_alibi_sarah` ;
- `asked_nico_second_cover_j1` ;
- `dette_nico` ;
- `coherence`.

Usage attendu : Nico peut encore aider, mais le coût doit devenir lisible. L’alibi peut tenir sans être confortable.

## 12. Fin J2 MVP

Le Jour 2 se termine quand les scènes obligatoires sont terminées :

- Sarah ;
- Nico ;
- Camille ;
- Maya.

Fin possible : débloquer un bouton “Passer au Jour 3”.

Préparation J3 : le dernier choix J2 peut poser un flag de priorité :

- `j2_priority_sarah` ;
- `j2_priority_camille` ;
- `j2_priority_nico` ;
- `j2_priority_escape`.

Ne pas implémenter ces flags dans T172 : ils sont seulement documentés ici comme pistes de sortie J2.

## 13. Tests futurs à prévoir

Quand l’implémentation commencera :

- test structure J2 conversations déclarées ;
- test disponibilité initiale Sarah/Nico ;
- test déblocage Camille/Maya ;
- test scènes obligatoires J2 ;
- test flags J1 référencés existants ;
- test entry variants J2 ;
- test `_single_reply_` ;
- test absence d’omniscience ;
- test transition J1 → J2 ;
- test J1 V2 non régressé.

Le premier test J2 doit vérifier la structure et la disponibilité avant d’écrire les dialogues complets.

## 14. Décisions ouvertes

Décisions encore ouvertes :

- Sarah repas / Nico respiration obligatoires ou optionnels avant J2 ?
- Inès J2 optionnelle ou obligatoire ?
- Maya J2 conditionnelle ou obligatoire ?
- Un média J2 dès la première version ou plus tard ?
- Bouton Jour 2 visible dès fin des scènes cœur ou après respirations ?
- Affichage du bloc temporel dans l’UI maintenant ou plus tard ?
- Sarah et Nico disponibles simultanément au matin, ou Sarah d’abord ?
- La priorité J2 → J3 doit-elle être un choix explicite ou une conséquence calculée ?

Ces décisions doivent être tranchées avant les premiers JSON J2 jouables.
