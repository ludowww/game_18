# J4 V2 — Brief macro

## 0. Statut et périmètre

Document de cadrage macro pour le Jour 4 V2.

Ce document ne crée pas J4. Il définit le rôle dramatique, les blocs temporels, les dynamiques relationnelles, les modules narratifs à utiliser, les limites du MVP et les questions ouvertes avant la structure technique.

Contraintes T206 :

- aucun JSON modifié ;
- aucun script modifié ;
- aucune conversation J4 créée ;
- aucun dialogue complet écrit ;
- aucun asset ajouté ;
- aucun test modifié ;
- documentation uniquement.

Documents de référence :

- `docs/narrative_production_bible_j4_plus.md` ;
- `docs/j3_design_brief.md` ;
- `docs/j3_v2_dialogue_audit.md` ;
- `docs/j3_character_voice_and_repetition_audit.md` ;
- `docs/j3_media_and_intimacy_design.md`.

## 1. Rôle narratif du Jour 4

J4 doit être le premier jour où les fils de conversation commencent à se croiser de manière plus visible.

Rappel de progression :

- J1 : versions initiales, premiers mensonges ou aveux partiels ;
- J2 : conséquences individuelles de ces versions ;
- J3 : quotidien, temporalité, premiers signaux, personnages plus incarnés ;
- J4 : début des croisements dynamiques et des priorités conflictuelles.

Phrase directrice :

> Le J4 est le jour où le joueur commence à ne plus pouvoir gérer les conversations comme des fils séparés.

J4 ne doit pas encore être :

- la révélation totale ;
- la confrontation Sarah/Camille ;
- l’explosion du groupe ;
- la bascule sexuelle explicite ;
- une journée de résolution.

J4 doit faire sentir :

- les délais ;
- les choix de priorité ;
- les contradictions faibles ;
- la disponibilité limitée des personnages ;
- le coût de consulter quelqu’un avant de répondre à quelqu’un d’autre ;
- le fait que le quotidien continue pendant que le joueur essaie de gérer ses versions.

## 2. Axe dramatique principal

Axe proposé : **priorités et délais**.

Le joueur doit devoir choisir :

- répondre maintenant ou attendre ;
- dire la vérité ou vérifier une version ;
- tenir un geste Sarah ou fuir chez Nico ;
- répondre à Camille pendant le travail ou laisser la tension redescendre ;
- demander de l’aide à Nico ou le laisser respirer ;
- garder Maya à distance ou accepter son regard social ;
- chercher Inès le soir ou rester seul avec les conséquences.

Le cœur de J4 :

> Le téléphone devient un espace de gestion du temps et des priorités, pas seulement de réponses.

## 3. Pression cible

Niveau de pression : **moyenne → forte**.

J4 doit être plus tendu que J3, mais pas encore explosif.

Signes de pression attendus :

- Sarah remarque un détail ou l’absence d’un geste ;
- Nico est moins immédiatement disponible ;
- Camille écrit dans un moment contraint ;
- Maya sent que l’ambiance circule ;
- Inès peut apparaître comme refuge, mais ce refuge devient plus coûteux ;
- les réponses tardives ont un poids.

La pression doit venir du rythme, pas d’un grand twist.

## 4. Modules narratifs à utiliser

### 4.1 Module temporalité

J4 doit être explicitement découpé en blocs narratifs :

- début de matinée ;
- pause midi / travail ;
- fin d’après-midi ;
- soirée ;
- éventuellement tard le soir.

Les repères doivent d’abord être intégrés aux messages, pas forcément via UI.

Exemples :

- `je viens de voir ta tasse.`
- `pause de trois minutes.`
- `je peux pas trop écrire, je suis au boulot.`
- `ce soir je lance la console.`
- `j’ai écrit et effacé trois fois.`

### 4.2 Module disponibilité

Chaque personnage doit avoir une disponibilité située :

- Sarah : matin / quotidien / attente ;
- Nico : disponibilité limitée, soirée possible ;
- Camille : pause travail / réponse contrainte ;
- Maya : social / groupe / fin d’après-midi ;
- Inès : soir / douceur / distance.

La disponibilité n’est pas un décor. Elle doit influencer la forme de la conversation : messages courts, délais, refus, invitations, fatigue.

### 4.3 Module croisements

J4 doit introduire au moins un croisement MVP.

Croisement prioritaire : **Sarah ↔ Nico**.

Principe : Sarah remarque un détail qui ne colle pas. Le joueur peut répondre directement, temporiser, ou contacter Nico avant de répondre.

Ce croisement ne doit pas rendre Sarah ou Nico omniscients. Tout doit passer par :

- ce que Sarah observe ;
- ce que le joueur dit à Nico ;
- le délai visible ;
- la cohérence ou fragilité de la réponse.

### 4.4 Module médias

Pas de média obligatoire dans le brief macro J4.

Si un média J4 est ajouté plus tard :

- il doit avoir une réaction joueur ;
- il doit avoir un commentaire personnage ;
- il ne doit pas prouver ;
- il ne doit pas révéler une conversation privée ;
- il ne doit pas sexualiser trop tôt.

### 4.5 Module intimité progressive

J4 peut commencer à nommer davantage le désir avec Camille, mais sans média suggestif explicite.

Niveau autorisé :

- émotionnel ;
- trouble ;
- allusion ;
- désir verbal contrôlé ;
- tension dans une pause ou un délai.

Niveau interdit :

- contenu sexuel explicite ;
- photo sexy ;
- récompense de route ;
- bascule intime si pression haute ou respect bas.

## 5. Blocs temporels J4 proposés

### Bloc 1 — Début de matinée

Personnages : Sarah, avec présence indirecte possible de Nico.

Fonction : Sarah observe un détail du quotidien ou une absence de geste.

Situation possible :

- Sarah remarque que quelque chose ne colle pas avec ce qui a été promis ;
- elle ne sait rien d’une autre conversation ;
- elle parle depuis le matin, la table, un objet, un geste attendu.

Déclencheurs J3 possibles :

- `j3_sarah_promises_actions` : Sarah attend un geste ;
- `j3_sarah_more_time` : Sarah est plus distante ;
- `j3_sarah_defensive` : Sarah écrit froidement ;
- `j3_sarah_honest_uncertainty` : Sarah reste prudente mais accessible ;
- `j3_sarah_feels_unheard` : Sarah est plus sensible aux réponses défensives.

Choix possibles :

- répondre directement ;
- reconnaître le détail ;
- temporiser ;
- préparer une réponse en contactant Nico ;
- se défendre.

Attention : Sarah ne doit pas savoir ce que Nico a dit. Elle remarque un détail, pas une vérité.

### Bloc 2 — Réaction / consultation Nico

Personnage : Nico.

Fonction : premier vrai croisement dynamique.

Si Sarah soulève un détail, le joueur peut contacter Nico avant de répondre ou après avoir répondu.

Nico peut :

- aider brièvement ;
- refuser de porter encore une version ;
- rappeler qu’il a une soirée / une vie ;
- proposer de parler plus tard ou de jouer ce soir ;
- signaler que le délai va se voir.

Effets possibles :

- `dette_nico` +1/+2 si on demande une couverture ;
- `risque_exposition` +1 si délai ou version fragile ;
- `coherence` +1 si le joueur choisit la vérité ;
- `fatigue_emotionnelle` +1 si le joueur temporise ;
- `distance_sarah` +1 si le délai devient visible.

Nico ne doit pas :

- trahir ;
- parler au nom de Sarah ;
- être disponible sans coût ;
- devenir un bouton “réparer l’alibi”.

### Bloc 3 — Pause midi / Camille au travail

Personnage : Camille.

Fonction : faire exister Camille dans son quotidien et installer une tension dans une fenêtre courte.

Contexte :

- pause de travail ;
- message envoyé alors qu’elle devrait bosser ;
- sous-entendu ;
- tension contrôlée ;
- disponibilité courte.

Selon J3 :

- si `j3_camille_boundary_kept` : elle teste si la limite tient ;
- si `j3_camille_recognized_without_using` : proximité prudente ;
- si `j3_camille_pressure_rises` : elle est plus méfiante ;
- si `j3_camille_minimized_again` : froideur / distance ;
- si `j3_camille_closes_badly` : elle répond plus court ou plus froidement.

Choix possibles :

- taquiner légèrement ;
- respecter la pause ;
- nommer le trouble ;
- forcer / relancer trop fort ;
- couper court.

Effets possibles :

- `respect_camille` ;
- `pression_camille` ;
- `tension_camille` ;
- `risque_exposition` ;
- `coherence`.

J4 peut préparer la tension sexuelle future par :

- sous-entendu ;
- limite ;
- pause qui dure trop ;
- désir évoqué sans image ;
- contradiction entre travail et envie de répondre.

Interdit :

- photo suggestive ;
- contenu explicite ;
- Camille récompense ;
- pression récompensée.

### Bloc 4 — Fin d’après-midi / Maya social

Personnage : Maya.

Fonction : montrer que le social commence à absorber les contradictions.

Contexte :

- ambiance de groupe ;
- remarque sur le fait que le joueur répond différemment ;
- signe faible ;
- timing étrange ;
- pas de preuve.

Selon J3 :

- si `j3_maya_social_thread_possible` : elle sent que d’autres remarquent ;
- si `j3_maya_group_boundary_requested` : elle respecte mais surveille ;
- si `j3_maya_suspicion_reinforced` : elle est plus piquante ;
- si `j3_maya_direct_channel_requested` : elle parle au joueur directement ;
- si `j3_maya_defensive_again` : elle perçoit la défense comme un signal.

Choix possibles :

- accepter son regard ;
- lui demander de rester directe ;
- minimiser ;
- demander qui d’autre a remarqué ;
- détourner par l’humour.

Effets possibles :

- `suspicion_maya` ;
- `risque_exposition` ;
- `coherence` ;
- `fatigue_emotionnelle`.

Maya ne doit pas :

- donner des noms trop tôt ;
- prouver ;
- devenir détective ;
- parler à la place de Sarah.

### Bloc 5 — Soirée / Nico ou Sarah

Personnages : Nico, Sarah.

Fonction : faire jouer les priorités du soir.

Situation possible :

- Nico propose une soirée jeux vidéo ;
- Sarah attend un geste ou une présence ;
- le joueur doit choisir ce que “respirer” veut dire.

Choix possibles :

- rejoindre Nico pour respirer vraiment ;
- utiliser Nico comme alibi ;
- rester disponible pour Sarah ;
- mentir / temporiser ;
- reporter Nico.

Effets possibles :

- `confiance_sarah` ;
- `distance_sarah` ;
- `dette_nico` ;
- `coherence` ;
- `fatigue_emotionnelle` ;
- `risque_exposition`.

C’est un bon lieu de tension :

- amitié réelle vs fuite ;
- geste Sarah vs alibi ;
- vraie pause vs évitement ;
- soirée comme respiration ou comme mensonge.

### Bloc 6 — Soir tard / Inès optionnelle

Personnage : Inès.

Fonction : respiration optionnelle, mais coûteuse si utilisée comme fuite.

Selon J3 :

- si `j3_ines_clear_presence` : Inès peut rester douce ;
- si `j3_ines_refuge_again` : elle est plus prudente ;
- si `j3_ines_step_back` : distance ;
- si `j3_ines_soft_distance` : présence calme mais bornée ;
- si `j3_ines_escape_risk_high` : refuge à traiter avec prudence.

Choix possibles :

- dire qu’on cherche du calme ;
- dire qu’on ne veut pas l’utiliser ;
- se retirer ;
- tenter de prolonger trop ;
- répondre très tard.

Effets possibles :

- `fuite_ines` ;
- `coherence` ;
- `fatigue_emotionnelle` ;
- `culpabilite`.

Inès ne doit pas :

- connaître les autres fils ;
- sauver le joueur ;
- devenir romance automatique ;
- devenir thérapeute.

## 6. Personnages actifs J4 MVP

### Obligatoires recommandés

- Sarah ;
- Nico ;
- Camille ;
- Maya.

### Optionnelle recommandée

- Inès.

Même logique que J3 : Inès doit pouvoir être disponible en soirée mais ne pas bloquer la progression.

## 7. Croisement MVP prioritaire : Sarah ↔ Nico

But : tester la première vraie mécanique de croisement sans explosion.

Situation design : Sarah remarque un détail faible. Le joueur peut contacter Nico pour préparer ou vérifier une version.

Structure possible :

1. Sarah envoie un message de doute.
2. Choix joueur :
   - répondre maintenant ;
   - demander un peu de temps ;
   - contacter Nico.
3. Si contacter Nico :
   - Nico répond avec délai ou limite ;
   - il peut aider ou refuser ;
   - cela pose un flag.
4. Retour Sarah :
   - la réponse arrive plus tard ;
   - Sarah peut sentir le délai ;
   - la version peut être plus cohérente mais moins spontanée.

Flags possibles :

- `j4_sarah_detail_noted` ;
- `j4_player_delayed_sarah_reply` ;
- `j4_player_checked_with_nico` ;
- `j4_nico_helped_version` ;
- `j4_nico_refused_more_alibi` ;
- `j4_sarah_delay_noticed`.

Effets possibles :

- `risque_exposition` ;
- `dette_nico` ;
- `confiance_sarah` ;
- `distance_sarah` ;
- `coherence` ;
- `fatigue_emotionnelle`.

Important : ne pas forcément implémenter tout en J4 MVP. Mais J4 doit au moins préparer cette dynamique.

## 8. Routes intimes et tension sexuelle J4

J4 peut monter légèrement la tension, surtout avec Camille.

### Camille

Autorisé :

- sous-entendus ;
- “tu joues avec la limite ?” ;
- tension qui dure dans une pause ;
- désir évoqué mais retenu ;
- trouble assumé si respect haut.

Interdit :

- photo suggestive ;
- explicite ;
- récompense ;
- désir forcé si pression haute.

Variables importantes :

- `respect_camille` ;
- `pression_camille` ;
- `tension_camille` ;
- `coherence`.

### Sarah

Autorisé :

- intimité domestique ;
- gestes ;
- présence ;
- proximité prudente.

Interdit :

- sexualité comme réparation ;
- photo intime ;
- bascule rapide si confiance basse.

### Inès

Autorisé :

- douceur ;
- présence ;
- hésitation.

Interdit :

- refuge sexualisé ;
- intimité si `fuite_ines` haute.

### Maya

Pas de route intime J4 recommandée. Garder flirt verbal éventuel pour plus tard.

### Nico

Vie sentimentale hors joueur possible, mais sans média intime ni personne identifiable.

## 9. Médias J4

Pas de média obligatoire dans ce brief macro.

Médias possibles à envisager plus tard :

- Sarah : trace domestique si geste tenu/non tenu ;
- Camille : lieu ou pause travail, non suggestif ;
- Nico : console / setup / soirée ;
- Maya : capture sociale non probante, à manier avec prudence ;
- Inès : pas prioritaire.

Règle : aucun média sans mini-discussion.

## 10. Variables clés J4

Variables principales :

- `confiance_sarah` ;
- `distance_sarah` ;
- `dette_nico` ;
- `risque_exposition` ;
- `coherence` ;
- `fatigue_emotionnelle` ;
- `respect_camille` ;
- `pression_camille` ;
- `tension_camille` ;
- `suspicion_maya` ;
- `fuite_ines` ;
- `culpabilite`.

Nouvelles variables non nécessaires pour MVP. Préférer flags J4 + variables existantes.

## 11. Ce que J4 ne doit pas faire

J4 ne doit pas :

- révéler toute la vérité ;
- confronter Sarah et Camille directement ;
- transformer Maya en détective ;
- faire trahir Nico ;
- sexualiser Camille trop vite ;
- rendre Inès centrale ;
- multiplier les médias ;
- ajouter trop de nouveaux systèmes runtime d’un coup ;
- devenir une journée énorme impossible à tester.

## 12. MVP J4 recommandé

### MVP narratif

- Sarah matin : détail / geste / doute léger.
- Nico matin ou soirée : disponibilité limitée / alibi possible.
- Camille pause midi : tension dans le travail.
- Maya fin d’après-midi : ambiance sociale.
- Inès soir optionnelle : calme ou fuite.

### MVP mécanique

- structure J4 skeleton ;
- progression temporelle simple ;
- Sarah/Nico/Camille/Maya required ;
- Inès optionnelle ;
- au moins un flag préparant le croisement Sarah ↔ Nico ;
- pas encore de runtime complexe multi-fil si trop coûteux.

## 13. Questions ouvertes avant T207

À trancher dans les prochaines tâches :

1. J4 doit-il implémenter immédiatement le choix “contacter Nico avant Sarah” ?
2. Ou doit-il seulement le préparer par flags ?
3. Faut-il introduire des nodes système de transition temporelle ?
4. Faut-il garder les repères uniquement dans les textes ?
5. Nico soirée jeux vidéo doit-il être obligatoire ou optionnel ?
6. Camille doit-elle être au midi ou après-midi ?
7. Inès doit-elle être débloquée après Maya comme J3 ?
8. J4 doit-il avoir un média ou attendre la stabilité des scènes ?
9. Le croisement Sarah ↔ Nico doit-il être dans le runtime dès J4 ou simulé narrativement dans les JSON ?
10. Faut-il réserver la première vraie mécanique multi-fil à J5 pour éviter de surcharger J4 ?

## 14. Conclusion

J4 doit être une journée de priorités.

Le joueur commence à comprendre que répondre est aussi choisir :

- un moment ;
- une personne ;
- une version ;
- un risque ;
- une absence ailleurs.

Ce brief ne lance pas encore l’écriture. La prochaine tâche doit préciser la temporalité et les disponibilités.

Prochaine tâche recommandée :

`T207 — Temporalité et disponibilités J4`

## 15. Validation

Validation attendue pour T206 :

```bash
python3 tools/validate_j1_v2_experimental.py
git status
```

Commit attendu :

`docs: add J4 macro brief`
