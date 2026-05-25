# J4 V2 — Temporalité et disponibilités

## 0. Statut et périmètre

Document de design pour le Jour 4 V2. Il précise la temporalité, les disponibilités, l’ordre recommandé des conversations et les règles de progression à prévoir avant toute création de JSON J4.

Ce document ne crée pas J4.

Contraintes T207 :

- aucun JSON modifié ;
- aucun script modifié ;
- aucune conversation J4 créée ;
- aucun dialogue complet écrit ;
- aucun asset ajouté ;
- aucun test modifié ;
- documentation uniquement.

Documents de référence :

- `docs/narrative_production_bible_j4_plus.md` ;
- `docs/j4_macro_brief.md` ;
- `docs/j3_character_voice_and_repetition_audit.md` ;
- `docs/j3_v2_dialogue_audit.md`.

## 1. Rôle de ce document

J4 ne doit pas être une simple liste de conversations. Il doit donner l’impression d’une journée qui avance.

Le joueur doit sentir :

- que le matin n’a pas la même humeur que le soir ;
- que chaque personnage a une activité ;
- que tout le monde n’est pas disponible au même moment ;
- qu’attendre a un coût ;
- qu’une conversation peut en retarder une autre ;
- que répondre, c’est choisir une priorité.

Ce document fixe donc :

- les blocs temporels ;
- les disponibilités par personnage ;
- les rythmes de déblocage ;
- les croisements possibles ;
- les flags de temporalité à prévoir ;
- les limites MVP.

## 2. Principe général

J4 est structuré autour de six blocs narratifs :

1. Début de matinée — Sarah / détail du quotidien.
2. Fin de matinée — Nico / consultation possible.
3. Pause midi — Camille / travail et tension.
4. Fin d’après-midi — Maya / social et ambiance.
5. Soirée — Nico ou Sarah / priorité de présence.
6. Soir tard — Inès optionnelle / calme ou fuite.

Chaque bloc doit avoir :

- une humeur ;
- un ou plusieurs personnages actifs ;
- des personnages indisponibles ou partiellement disponibles ;
- une raison d’écriture ;
- un risque narratif ;
- des flags possibles ;
- un rôle dans la journée.

Le découpage temporel doit d’abord être rendu par les dialogues, pas par une UI lourde.

## 3. Bloc 1 — Début de matinée

### Humeur

- fatigue ;
- prudence ;
- observation ;
- petits gestes ;
- détails domestiques ;
- tension basse mais persistante.

### Personnage principal

Sarah.

### Personnage secondaire possible

Nico, mais seulement indirectement ou via un choix de consultation ultérieur.

### Fonction narrative

Sarah ouvre J4. Elle ne vient pas avec une révélation. Elle vient avec un détail.

Ce détail peut être :

- un geste attendu mais absent ;
- un geste tenu mais fragile ;
- une phrase qui ne s’accorde pas avec les actes ;
- un délai ;
- une petite incohérence ;
- un objet du quotidien.

Sarah ne doit pas savoir ce que Nico, Camille, Maya ou Inès ont dit. Elle remarque seulement ce qu’elle peut remarquer dans le quotidien.

### Disponibilité Sarah

Sarah est disponible, mais son ouverture dépend de J3.

#### Si `j3_sarah_promises_actions`

- Sarah attend des gestes concrets.
- Elle observe les détails.
- Elle peut être sensible aux petites absences.

#### Si `j3_sarah_honest_uncertainty`

- Sarah reste prudente.
- Elle accepte l’incertitude, mais pas l’évitement.
- Elle peut être accessible si le joueur reste direct.

#### Si `j3_sarah_more_time`

- Sarah est plus distante.
- Elle accepte moins facilement un nouveau délai.
- Elle peut écrire plus court.

#### Si `j3_sarah_defensive` ou `j3_sarah_feels_unheard`

- Sarah se protège.
- Elle est moins tendre.
- Elle attend un changement de posture, pas une explication brillante.

### Rôle du joueur

Le joueur doit choisir entre :

- répondre directement ;
- reconnaître le détail ;
- temporiser ;
- se défendre ;
- préparer une réponse en contactant Nico.

### Croisement possible

Préparer ici le croisement Sarah ↔ Nico.

Sarah peut dire :

```text
Il y a un truc qui colle pas.
```

ou :

```text
Je ne sais pas si c’est important, mais j’ai remarqué un détail.
```

Mais elle ne doit pas dire :

```text
Nico m’a dit...
```

### Flags possibles

- `j4_sarah_morning_detail_noted`
- `j4_sarah_waits_for_action`
- `j4_sarah_notices_delay`
- `j4_sarah_small_incoherence`
- `j4_player_given_direct_sarah_answer`
- `j4_player_delayed_sarah_answer`
- `j4_sarah_answer_pending_nico_check`

### Notes design

Ce bloc ne doit pas exploser. Il doit créer une urgence douce :

> Si je réponds trop vite, je risque de dire n’importe quoi. Si j’attends, elle va sentir que j’attends.

## 4. Bloc 2 — Fin de matinée / consultation Nico

### Humeur

- retard ;
- humour ;
- disponibilité partielle ;
- fatigue amicale ;
- coût de l’alibi ;
- tension cachée sous la vanne.

### Personnage principal

Nico.

### Moment

Fin de matinée ou début de midi.

Nico ne doit pas être disponible comme un bouton magique. Il peut répondre avec un délai, ou indiquer qu’il ne peut pas entrer dans un nouveau mensonge tout de suite.

### Fonction narrative

Tester le premier croisement dynamique de J4.

Le joueur peut :

- contacter Nico pour vérifier une version ;
- demander une couverture ;
- lui dire que Sarah a remarqué un détail ;
- chercher une formulation ;
- renoncer à l’utiliser.

### Disponibilité Nico

Nico est moins disponible qu’avant.

Raisons possibles :

- il se réveille tard ;
- il travaille ;
- il est en trajet ;
- il prépare sa soirée jeux vidéo ;
- il répond entre deux choses ;
- il refuse de redevenir un pare-feu.

### Ton Nico

Nico doit rester :

- drôle ;
- direct ;
- un peu agacé ;
- loyal ;
- limité.

Exemples de ton :

```text
tu me demandes ça avant ou après avoir allumé l’incendie ?
```

```text
je peux t’aider à pas empirer. pas à réécrire la journée.
```

```text
je suis là, mais pas en service illimité.
```

### Choix possibles

1. demander une aide claire ;
2. demander seulement un avis ;
3. libérer Nico ;
4. plaisanter / esquiver ;
5. demander une couverture malgré sa limite.

### Effets possibles

Demander couverture :

- `dette_nico` +2 ;
- `risque_exposition` +1 ;
- `fatigue_emotionnelle` +1 ;
- `coherence` -1 si formulation fragile.

Demander conseil :

- `coherence` +1 ;
- `dette_nico` +1 ;
- `fatigue_emotionnelle` +1.

Libérer Nico :

- `dette_nico` -1 ;
- `coherence` +1 ;
- `risque_exposition` 0 ou -1.

Plaisanter :

- `dette_nico` +1 ;
- `risque_exposition` +1 ;
- `fatigue_emotionnelle` -1 ou +1 selon contexte.

### Flags possibles

- `j4_player_checked_with_nico`
- `j4_nico_warned_about_delay`
- `j4_nico_helped_version`
- `j4_nico_refused_more_alibi`
- `j4_nico_available_later`
- `j4_nico_game_evening_seed`
- `j4_nico_not_a_service`

### Rôle long terme

Nico doit devenir un personnage avec une disponibilité propre.

Ce bloc prépare :

- la soirée jeux vidéo ;
- l’alibi coûteux ;
- le refus futur ;
- la fatigue de l’amitié ;
- une dynamique sociale future hors joueur.

## 5. Bloc 3 — Pause midi / Camille au travail

### Humeur

- tension ;
- contrainte ;
- pause courte ;
- sous-entendu ;
- désir contenu ;
- concentration perturbée.

### Personnage principal

Camille.

### Moment

Pause midi ou début d’après-midi.

Camille ne doit pas écrire comme si elle attendait le joueur dans le vide. Elle doit être située :

- au travail ;
- en pause ;
- en déplacement ;
- entre deux obligations.

### Fonction narrative

Montrer que Camille a une vie et que la tension s’insère dans une journée réelle.

La scène doit permettre :

- de taquiner Camille ;
- de respecter sa pause ;
- de nommer un trouble ;
- de poser une limite ;
- de mettre trop de pression.

### Disponibilité Camille

Camille a peu de temps.

Ses messages peuvent être :

- plus courts ;
- plus tendus ;
- interrompus ;
- plus concrets ;
- moins analytiques.

Exemples de repères :

```text
pause de trois minutes.
```

```text
je suis censée bosser.
```

```text
je peux pas écrire longtemps.
```

```text
je te réponds vite avant de regretter.
```

### Selon J3

Si `j3_camille_recognized_without_using` :

- elle reste ouverte mais prudente ;
- elle teste si le joueur garde cette position.

Si `j3_camille_boundary_kept` :

- elle teste la limite ;
- elle peut être frustrée mais respectueuse.

Si `j3_camille_tension_reopened` ou `j3_camille_pressure_rises` :

- elle est plus méfiante ;
- elle peut répondre avec attirance et défense.

Si `j3_camille_minimized_again` ou `j3_camille_closes_badly` :

- elle est froide ;
- elle ne veut pas rouvrir facilement.

### Choix possibles

1. taquiner légèrement ;
2. respecter la pause ;
3. nommer le trouble ;
4. forcer / relancer trop fort ;
5. couper court proprement.

### Effets possibles

Taquiner :

- `tension_camille` +1 ;
- `respect_camille` 0/+1 ;
- `pression_camille` +1 si trop appuyé.

Respecter :

- `respect_camille` +2 ;
- `pression_camille` -1 ;
- `coherence` +1.

Nommer trouble :

- `tension_camille` +2 ;
- `risque_exposition` +1 ;
- `pression_camille` +1.

Forcer :

- `pression_camille` +2 ;
- `respect_camille` -1 ;
- `tension_camille` peut monter ou chuter selon branche.

Couper court proprement :

- `respect_camille` +1 ;
- `tension_camille` -1 ;
- `coherence` +1.

### Flags possibles

- `j4_camille_work_pause`
- `j4_camille_limit_tested`
- `j4_camille_teased_during_work`
- `j4_camille_trouble_named`
- `j4_camille_pressure_too_high`
- `j4_camille_boundary_respected`
- `j4_camille_pause_cut_short`

### Tension sexuelle

J4 peut augmenter la tension avec Camille, mais seulement verbalement.

Autorisé :

- sous-entendu ;
- trouble ;
- limite testée ;
- pause qui dure trop ;
- désir évoqué mais retenu.

Interdit :

- média suggestif ;
- contenu explicite ;
- Camille qui récompense la pression ;
- route intime si pression haute.

## 6. Bloc 4 — Fin d’après-midi / Maya social

### Humeur

- observation ;
- rythme social ;
- piques ;
- prudence ;
- ambiance de groupe ;
- fausse légèreté.

### Personnage principal

Maya.

### Moment

Fin d’après-midi.

Le joueur a déjà géré Sarah, Nico, Camille. Maya arrive comme signe que le monde social continue.

### Fonction narrative

Montrer que les contradictions commencent à être visibles dans l’ambiance.

Maya ne doit pas apporter de preuve. Elle apporte :

- un ressenti social ;
- une remarque sur le ton ;
- un timing bizarre ;
- une impression de groupe ;
- une pique ;
- un doute qu’elle n’affirme pas.

### Disponibilité Maya

Maya est disponible mais pas solennelle.

Elle peut écrire depuis :

- un transport ;
- une pause ;
- un groupe ;
- une conversation collective ;
- une notification sociale.

### Selon J3

Si `j3_maya_social_thread_possible` :

- elle peut suggérer qu’elle n’est pas la seule à sentir quelque chose.

Si `j3_maya_group_boundary_requested` :

- elle respecte la limite, mais garde un œil.

Si `j3_maya_suspicion_reinforced` :

- elle est plus piquante.

Si `j3_maya_direct_channel_requested` :

- elle parle directement, sans passer par le groupe.

Si `j3_maya_defensive_again` :

- elle perçoit la défense comme un signal.

### Choix possibles

1. accepter son regard ;
2. demander du direct ;
3. minimiser ;
4. demander si d’autres ont remarqué ;
5. plaisanter.

### Effets possibles

Accepter :

- `suspicion_maya` 0/+1 ;
- `coherence` +1.

Demander direct :

- `suspicion_maya` -1 ;
- `coherence` +1.

Minimiser :

- `suspicion_maya` +2 ;
- `risque_exposition` +1.

Demander qui d’autre :

- `risque_exposition` +2 ;
- `fatigue_emotionnelle` +1.

Plaisanter :

- peut réduire la fatigue ;
- peut augmenter la suspicion si trop défensif.

### Flags possibles

- `j4_maya_group_mood_noted`
- `j4_maya_tone_shift_seen`
- `j4_maya_direct_channel_kept`
- `j4_maya_suspicion_pushed`
- `j4_maya_others_possibly_noticed`
- `j4_maya_social_delay_seen`

### Garde-fous

Maya ne doit pas :

- nommer Sarah comme source ;
- dire qu’elle sait ;
- donner une preuve ;
- devenir détective ;
- agir comme porte-parole du groupe.

## 7. Bloc 5 — Soirée / priorités Sarah-Nico

### Humeur

- choix de disponibilité ;
- respiration ;
- fatigue ;
- amitié ;
- risque de fuite ;
- soirée qui peut devenir alibi.

### Personnages

Nico et Sarah.

### Fonction narrative

Le soir doit tester ce que le joueur fait de sa disponibilité.

Situation possible :

- Nico propose une soirée jeux vidéo ;
- Sarah attend un geste ou une présence ;
- le joueur ne peut pas tout faire parfaitement.

### Disponibilité Nico

Nico devient disponible pour une vraie respiration, pas forcément pour un alibi.

Exemples :

```text
je lance la console vers 21h.
```

```text
si tu viens, tu parles pas de tes versions pendant la première game.
```

```text
si c’est pour respirer, viens. si c’est pour te cacher, préviens avant.
```

### Disponibilité Sarah

Sarah n’a pas forcément besoin d’écrire beaucoup.
Elle peut :

- attendre ;
- envoyer un message bref ;
- remarquer une présence ou une absence ;
- réagir au délai.

Selon J4 matin :

- si le joueur a répondu directement : Sarah peut être plus calme ;
- si le joueur a temporisé : Sarah est plus distante ;
- si le joueur a contacté Nico : Sarah peut remarquer le délai ;
- si le joueur s’est défendu : Sarah se ferme.

### Choix possibles

1. rester disponible pour Sarah ;
2. aller chez Nico pour respirer vraiment ;
3. utiliser Nico comme alibi ;
4. reporter Nico ;
5. mentir / temporiser.

### Effets possibles

Rester disponible Sarah :

- `confiance_sarah` +1/+2 ;
- `distance_sarah` -1 ;
- `dette_nico` 0/-1.

Aller chez Nico honnêtement :

- `fatigue_emotionnelle` -1 ;
- `dette_nico` 0 ;
- `confiance_sarah` dépend de ce qui est dit ;
- `coherence` +1 si le joueur est clair.

Utiliser Nico comme alibi :

- `dette_nico` +2 ;
- `risque_exposition` +2 ;
- `coherence` -1 ;
- `distance_sarah` +1.

Reporter Nico :

- `dette_nico` -1 ;
- `confiance_sarah` +1 si cohérent ;
- `fatigue_emotionnelle` +1.

Mentir :

- `risque_exposition` +2 ;
- `coherence` -2 ;
- `distance_sarah` +1.

### Flags possibles

- `j4_nico_game_invite`
- `j4_player_chose_sarah_evening`
- `j4_player_chose_nico_evening`
- `j4_player_used_game_as_alibi`
- `j4_sarah_evening_presence_kept`
- `j4_sarah_evening_presence_failed`
- `j4_evening_delay_cost`

## 8. Bloc 6 — Soir tard / Inès optionnelle

### Humeur

- calme ;
- fatigue ;
- hésitation ;
- tentation de fuite ;
- douceur prudente.

### Personnage

Inès.

### Fonction narrative

Inès reste optionnelle.

Elle sert à tester si le joueur cherche :

- une vraie présence calme ;
- ou une échappatoire après une journée tendue.

### Disponibilité Inès

Inès répond tard.

Elle ne doit pas être disponible toute la journée. Elle peut écrire :

- après que les autres fils se soient tendus ;
- après un choix de fuite ;
- après une soirée agitée ;
- si le joueur l’a préservée en J3.

### Selon J3

Si `j3_ines_clear_presence` :

- Inès peut rester douce mais pas naïve.

Si `j3_ines_soft_distance` :

- elle reste présente à distance.

Si `j3_ines_refuge_again` ou `j3_ines_escape_risk_high` :

- elle est plus prudente ;
- elle peut poser une limite plus tôt.

Si `j3_ines_step_back` :

- elle peut rester distante.

### Choix possibles

1. chercher du calme ;
2. dire clairement qu’on ne veut pas l’utiliser ;
3. se retirer ;
4. prolonger trop ;
5. répondre tardivement.

### Effets possibles

Calme clair :

- `fuite_ines` -1 ;
- `coherence` +1.

Refuge :

- `fuite_ines` +2 ;
- `coherence` -1 ;
- `culpabilite` +1.

Retrait :

- `fuite_ines` -1 ;
- `fatigue_emotionnelle` +1.

Prolonger :

- `fuite_ines` +1/+2 ;
- `culpabilite` +1.

### Flags possibles

- `j4_ines_late_reply`
- `j4_ines_refuge_risk`
- `j4_ines_clear_distance`
- `j4_ines_soft_presence`
- `j4_player_avoids_using_ines`
- `j4_ines_keeps_distance`

## 9. Ordre de déblocage recommandé

### Début J4

Disponible :

- Sarah J4.

Verrouillé :

- Nico J4 ;
- Camille J4 ;
- Maya J4 ;
- Inès J4.

Raison : Sarah ouvre la journée avec le détail.

### Après Sarah J4 première scène

Débloquer :

- Nico J4.

Raison : le joueur peut avoir besoin de consulter Nico ou gérer son alibi.

### Après Nico J4 ou après résolution du bloc Sarah/Nico

Débloquer :

- Camille J4.

Raison : passage vers midi / travail.

### Après Camille J4

Débloquer :

- Maya J4.

Raison : passage fin d’après-midi / social.

### Après Maya J4

Débloquer :

- Inès J4 optionnelle.

Raison : soir tard / respiration.

## 10. Nico : une ou deux conversations J4 ?

Deux options existent.

### Option A — une seule conversation Nico J4

Nico couvre :

- consultation matin / midi ;
- seed soirée jeux vidéo ;
- limite d’alibi.

Avantages :

- runtime simple ;
- MVP plus rapide ;
- moins de doublons ;
- moins de tests.

Inconvénients :

- la soirée jeux vidéo reste surtout évoquée ;
- moins de sensation de retour en soirée.

### Option B — deux conversations Nico J4

- `nico_j4_v2` : consultation / alibi.
- `nico_evening_j4_v2` : soirée jeux vidéo / respiration / alibi possible.

Avantages :

- temporalité plus forte ;
- vraie sensation de soirée ;
- meilleure mise en scène des priorités Sarah/Nico.

Inconvénients :

- plus de runtime ;
- plus de tests ;
- plus de risques de doublons ;
- plus long à implémenter.

### Recommandation T207

Pour le MVP J4 : option A.

Garder une seule conversation Nico J4, mais y intégrer clairement :

- disponibilité limitée ;
- consultation possible ;
- seed soirée jeux vidéo ;
- choix ou fin qui prépare la soirée.

Reporter une vraie conversation `nico_evening_j4_v2` à J5 ou à une extension J4 ultérieure.

## 11. Required conversations J4 MVP

Recommandé :

Required :

- Sarah J4 ;
- Nico J4 ;
- Camille J4 ;
- Maya J4.

Optionnelle :

- Inès J4.

Même logique que J3.

## 12. Repères temporels visibles

### Pour le MVP

Utiliser des repères intégrés aux messages :

- `ce matin` ;
- `pause de trois minutes` ;
- `je suis censée bosser` ;
- `fin de journée` ;
- `ce soir` ;
- `tard`.

### À éviter pour le moment

Éviter un système UI lourd de cartes temporelles dans T207/T208.

### À préparer plus tard

Possibilité de nodes système sobres :

- `— Début de matinée —`
- `— Pause midi —`
- `— Fin d’après-midi —`
- `— Soirée —`

Mais ne pas implémenter avant décision UI.

## 13. Médias J4

Aucun média J4 obligatoire à ce stade.

Possibles plus tard :

- Nico setup console ;
- Camille lieu de travail / pause ;
- Sarah trace domestique ;
- Maya social flou ;
- Inès coin calme.

Recommandation T207 :

- pas de média dans la première structure J4 ;
- décider les médias après stabilisation des scènes ;
- toujours prévoir réaction joueur + commentaire personnage.

## 14. Décisions à prendre avant T208

T208 devra décider :

1. Une seule conversation Nico J4 ou deux ?
2. Le croisement Sarah ↔ Nico est-il réel dans le runtime ou narratif dans les dialogues ?
3. Sarah J4 doit-elle être scindée en matin + retour après Nico ?
4. Les blocs temporels sont-ils représentés par des messages système ou seulement par les dialogues ?
5. Inès J4 est-elle débloquée après Maya comme J3 ?
6. Les required J4 restent-ils Sarah/Nico/Camille/Maya ?
7. Faut-il préparer des flags J4 dès la structure skeleton ?
8. Faut-il prévoir un second passage Sarah le soir ou le réserver à J5 ?

## 15. Recommandation finale T207

Pour rester efficace :

- J4 doit être construit avec une progression simple ;
- pas de runtime complexe multi-fil dans la première implémentation ;
- le croisement Sarah ↔ Nico doit être préparé mais pas surconçu ;
- les repères temporels doivent d’abord être textuels ;
- la soirée jeux vidéo Nico doit être un élément narratif fort mais pas forcément une deuxième conversation ;
- Inès doit rester optionnelle.

Prochaine tâche recommandée :

`T208 — Matrice arcs/personnages J4`

Ce document devra préciser pour chaque personnage :

- humeur ;
- lieu ;
- objectif ;
- savoirs ;
- flags J3 utilisés ;
- flags J4 à créer ;
- risques ;
- voix attendue.

## 16. Validation

Validation attendue pour T207 :

```bash
python3 tools/validate_j1_v2_experimental.py
git status
```

Commit attendu :

`docs: define J4 temporality and availability`
