# Double Vie — Refonte J1 — Structure fonctionnelle des scènes

## Rôle du document

Ce document prépare la génération des dialogues du Jour 1 sans flou.
Il définit la fonction de chaque scène, les informations disponibles pour chaque personnage, les choix joueur attendus, les variables touchées, les flags à poser et l’état de sortie.

Source courte associée : `product/mvp_refonte_source_verite.md`

Règle : aucune scène ne doit être générée en dialogue complet tant que sa fonction n’est pas claire ici.

---

## Variables disponibles J1

- `confiance_sarah`
- `distance_sarah`
- `tension_camille`
- `respect_camille`
- `pression_camille`
- `intimite_sarah`
- `intimite_camille`
- `attente_image_camille`
- `suspicion_maya`
- `dette_nico`
- `fuite_ines`
- `coherence`
- `culpabilite`
- `risque_exposition`
- `fatigue_emotionnelle`

Toutes les valeurs sont entre 0 et 100. Les effets des choix sont relatifs.

---

# J1 — Fonction globale

## Question du jour

À qui réponds-tu en premier quand chaque personne détient un morceau différent de la soirée ?

## Objectifs J1

- Installer la situation sans exposition lourde.
- Faire comprendre que chaque contact possède une vérité partielle.
- Enregistrer la première priorité du joueur.
- Poser la première version donnée à Sarah.
- Poser le statut du moment avec Camille : assumé, minimisé, repoussé ou désiré trop vite.
- Introduire la dette envers Nico.
- Introduire le regard social de Maya.
- Introduire Inès comme miroir de fuite, pas comme route complète.
- Garder des respirations banales.

## Contraintes J1

- Pas de personnage omniscient.
- Pas d’accusation frontale trop tôt.
- Pas d’explosion sociale dès J1.
- Pas de sexualisation de Maya ou Nico.
- Pas de route sexuelle Inès.
- Pas d’image NSFW.
- Camille peut porter du trouble, mais doit garder une limite.
- Sarah doit exister comme relation domestique, pas seulement comme culpabilité.

---

# Scène `j1_00_reveil_messages`

## Fonction

Ouverture du jeu.
Le joueur se réveille avec cinq messages entrants. Il doit choisir à qui répondre en premier.

La scène ne doit pas résoudre le conflit. Elle doit créer la tension de priorité.

## Contact actif

Système / liste de conversations.
Les cinq contacts apparaissent.

## Messages entrants recommandés

Sarah :
> “T’es réveillé ? Faut qu’on parle d’hier.”

Nico :
> “frérot j’ai fait ce que j’ai pu mais ton histoire sent le plan claqué”

Camille :
> “Je crois qu’on a été moins discrets qu’on pensait.”

Maya :
> “je pose ça là : vous êtes fatigants.”

Inès :
> “C’est peut-être pas mes affaires. Mais tu avais l’air triste hier.”

## Choix joueur

Choix principal : ouvrir/répondre en premier à un contact.

Options :

1. Répondre d’abord à Sarah.
2. Répondre d’abord à Camille.
3. Répondre d’abord à Nico.
4. Répondre d’abord à Maya.
5. Répondre d’abord à Inès.

## Effets recommandés

Répondre d’abord à Sarah :
- `confiance_sarah`: +2
- `distance_sarah`: -1
- `tension_camille`: -1
- flag `first_reply_sarah`

Répondre d’abord à Camille :
- `tension_camille`: +2
- `confiance_sarah`: -1
- `culpabilite`: +1
- flag `first_reply_camille`

Répondre d’abord à Nico :
- `dette_nico`: +1
- `coherence`: +1 ou -1 selon choix suivant
- flag `first_reply_nico`

Répondre d’abord à Maya :
- `suspicion_maya`: +1
- `risque_exposition`: +1
- flag `first_reply_maya`

Répondre d’abord à Inès :
- `fuite_ines`: +2
- `fatigue_emotionnelle`: +1
- flag `first_reply_ines`

## Flags de silence implicites à prévoir plus tard

Selon l’ordre et les retards :

- `delayed_reply_sarah_j1`
- `delayed_reply_camille_j1`
- `delayed_reply_nico_j1`
- `delayed_reply_maya_j1`
- `delayed_reply_ines_j1`

## État de sortie

Le contact choisi devient la première scène active.
Les autres conversations restent disponibles ou reçoivent une marque de retard.

## Risque à éviter

Ne pas transformer cette scène en exposition complète de la soirée. Le joueur doit sentir qu’il manque des morceaux.

---

# Scène `j1_01_sarah_absence`

## Fonction

Sarah demande où le joueur était et pourquoi il est revenu différent.
La scène fixe la première version donnée à Sarah.

Sarah ne cherche pas à piéger le joueur. Elle veut savoir si elle invente son malaise.

## Sarah sait

- Le joueur était moins présent.
- Il s’est absenté.
- Camille était absente à un moment proche.
- Nico a donné une explication floue.
- Le joueur est revenu changé.

## Sarah ignore

- Ce qui s’est dit dehors.
- S’il y a eu contact physique.
- Ce que Camille pense du moment.
- Ce que le joueur a dit ou dira aux autres.

## Ton

Concret, doux, blessé, pas policier.
Partir d’un détail : café, clés, retour, fatigue, téléphone, silence.

## Choix joueur principaux

1. Dire qu’il avait besoin d’air.
2. Dire qu’il était avec Nico / utiliser l’alibi.
3. Dire qu’il a parlé avec Camille mais minimiser.
4. Avouer qu’il était perdu / troublé sans tout détailler.
5. Ne pas répondre ou répondre trop tard.

## Effets recommandés

Besoin d’air :
- `confiance_sarah`: +1
- `coherence`: +2
- `culpabilite`: +1
- flag `said_needed_air_to_sarah`

Alibi Nico :
- `confiance_sarah`: -1
- `dette_nico`: +3
- `coherence`: -2
- `risque_exposition`: +2
- flags `used_nico_alibi_sarah`, `version_sarah_nico`

Camille minimisée :
- `confiance_sarah`: -2
- `distance_sarah`: +2
- `coherence`: -1
- `culpabilite`: +2
- flags `mentioned_camille_to_sarah`, `minimized_camille_to_sarah`

Vulnérabilité partielle :
- `confiance_sarah`: +2
- `distance_sarah`: -1
- `culpabilite`: +2
- `coherence`: +1
- flag `vulnerable_to_sarah`

Silence / retard :
- `confiance_sarah`: -2
- `distance_sarah`: +3
- `fatigue_emotionnelle`: +1
- flag `ignored_sarah_j1`

## État de sortie

La première version à Sarah doit être enregistrée.
Cette version servira aux incohérences J2/J3.

Flags structurants possibles :

- `sarah_version_needed_air`
- `sarah_version_nico`
- `sarah_version_camille_minimized`
- `sarah_version_emotional_confusion`
- `sarah_no_clear_version_j1`

## Risque à éviter

Sarah ne doit pas dire “je sais ce que tu as fait avec Camille”. Elle peut soupçonner ou sentir, pas savoir.

---

# Scène `j1_02_camille_dehors`

## Fonction

Camille demande si le joueur va faire comme si le moment dehors était banal.
La scène définit si le joueur reconnaît le trouble, le minimise, pose une limite ou cherche le désir trop vite.

## Camille sait

- Elle était dehors avec lui.
- Le moment n’était pas neutre.
- Une limite émotionnelle a été touchée.
- Le joueur peut minimiser par confort ou peur.

## Camille ignore

- Ce que Sarah sait.
- Ce que le joueur a dit à Sarah.
- Ce que Maya a vu.
- Jusqu’où Nico est impliqué.

## Ton

Précis, oblique, lucide.
Camille doit être attirante par sa lucidité, pas uniquement par la séduction.

## Choix joueur principaux

1. Assumer que ce n’était pas neutre.
2. Poser une limite respectueuse.
3. Minimiser le moment.
4. Répondre par désir trop direct.
5. Laisser le message sans réponse.

## Effets recommandés

Assumer :
- `tension_camille`: +2
- `respect_camille`: +1
- `culpabilite`: +2
- `coherence`: +1
- flag `admitted_tension_to_camille`

Limite respectueuse :
- `tension_camille`: -1
- `respect_camille`: +3
- `pression_camille`: -2
- `coherence`: +2
- flag `protected_camille_boundary`

Minimiser :
- `tension_camille`: -1
- `respect_camille`: -3
- `pression_camille`: +1
- `coherence`: -1
- flag `minimized_with_camille`

Désir trop direct :
- `tension_camille`: +2
- `respect_camille`: -3
- `pression_camille`: +3
- `culpabilite`: +2
- flag `early_desire_to_camille`

Silence :
- `tension_camille`: -2
- `respect_camille`: -1
- `fatigue_emotionnelle`: +1
- flag `ignored_camille_j1`

## État de sortie

Camille doit comprendre si le joueur la reconnaît comme personne ou s’il cherche une échappatoire.

Flags structurants possibles :

- `camille_trouble_acknowledged`
- `camille_boundary_respected`
- `camille_minimized_j1`
- `camille_desire_too_early_j1`
- `camille_left_on_read_j1`

## Risque à éviter

Camille ne doit pas devenir immédiatement disponible ou explicitement sexuelle. Le désir existe, mais sous condition de respect.

---

# Scène `j1_03_nico_couverture`

## Fonction

Nico rappelle qu’il a couvert ou simplifié l’absence du joueur.
Il peut aider, mais il ne veut pas devenir un alibi permanent.

## Nico sait

- Il a donné une explication improvisée.
- Le joueur est troublé par Camille.
- Sarah ou Maya pourraient lui poser des questions.
- Son explication peut devenir fragile.

## Nico ignore

- Ce qui s’est réellement passé dehors.
- Ce que le joueur a dit à Sarah.
- Ce que Camille attend.
- Ce que Maya a vu.

## Ton

Oral, drôle, familier, avec une limite sérieuse.

## Choix joueur principaux

1. Demander à Nico de tenir une version.
2. Lui dire de rester vague / silencieux.
3. Avouer qu’il s’est passé un moment avec Camille.
4. Plaisanter pour éviter.
5. Le rembarrer / minimiser son inquiétude.

## Effets recommandés

Tenir une version :
- `dette_nico`: +4
- `coherence`: -1
- `risque_exposition`: +2
- flags `asked_nico_hold_version`, `nico_alibi_requested`

Rester vague :
- `dette_nico`: +1
- `coherence`: +1
- `fatigue_emotionnelle`: +1
- flag `told_nico_stay_silent`

Confession :
- `dette_nico`: -1
- `coherence`: +2
- `culpabilite`: +1
- flag `confessed_camille_to_nico`

Humour d’évitement :
- `dette_nico`: +1
- `fatigue_emotionnelle`: +1
- flag `joked_with_nico_to_avoid`

Rembarrer :
- `dette_nico`: +2
- `coherence`: -1
- `fatigue_emotionnelle`: +2
- flag `dismissed_nico_warning`

## État de sortie

Le jeu doit savoir si Nico devient :

- soutien lucide ;
- alibi fragile ;
- ami agacé ;
- détente comique mais inquiet.

## Risque à éviter

Nico ne doit pas résoudre les conséquences. Il ne peut couvrir qu’un blanc, pas toute la vie du joueur.

---

# Scène `j1_04_maya_pique`

## Fonction

Maya signale une incohérence sociale : timing, absence, photo, comportement du joueur ou de Camille.
Elle ne sait pas tout, mais elle voit assez pour gêner.

## Maya sait

- Le joueur et Camille ont été absents ou difficiles à situer.
- Sarah a senti quelque chose.
- Nico a donné une explication pas totalement solide.
- Le timing est suspect.

## Maya ignore

- Le contenu du moment dehors.
- La vérité émotionnelle complète.
- La version donnée à Sarah.
- L’intention de Camille.

## Ton

Court, piquant, social, rapide.
Humour comme pression légère.

## Choix joueur principaux

1. Jouer l’innocence.
2. Dire qu’il avait besoin d’air.
3. Demander ce qu’elle a vu.
4. Lui dire de ne pas s’en mêler.
5. Répondre par humour.
6. Ne pas répondre.

## Effets recommandés

Innocence :
- `suspicion_maya`: +2
- `coherence`: -1
- flag `played_dumb_with_maya`

Besoin d’air :
- `suspicion_maya`: -1
- `coherence`: +1
- flag `told_maya_needed_air`

Demander ce qu’elle a vu :
- `suspicion_maya`: +1
- `risque_exposition`: +1
- flag `asked_maya_what_she_saw`

Ne pas s’en mêler :
- `suspicion_maya`: +3
- `risque_exposition`: +2
- flag `told_maya_not_involve`

Humour :
- `suspicion_maya`: +1 ou -1 selon qualité
- flag `joked_with_maya_j1`

Silence :
- `suspicion_maya`: +2
- `risque_exposition`: +1
- flag `ignored_maya_j1`

## État de sortie

Maya doit rester dans une zone de soupçon, pas de certitude.
Elle peut devenir alliée prudente ou risque social selon le ton du joueur.

Flags structurants possibles :

- `maya_photo_possible`
- `maya_timing_noted`
- `maya_warned_no_lie`
- `maya_suspicion_seeded_j1`

## Risque à éviter

Maya ne doit pas être une enquêtrice ni faire chanter le joueur. Elle observe, pique, protège Sarah.

---

# Scène `j1_05_ines_faille`

## Fonction

Inès écrit peu mais remarque l’état intérieur du joueur.
Elle ouvre une porte latérale, sans route romantique complète.

## Inès sait

- Le joueur avait l’air ailleurs.
- Il semblait triste ou déplacé.
- Il cherchait peut-être une sortie.

## Inès ignore

- La tension avec Camille.
- L’état du couple avec Sarah.
- Le rôle de Nico.
- Les observations de Maya.

## Ton

Doux, hésitant, légèrement étrange.
Elle laisse de la place.

## Choix joueur principaux

1. S’ouvrir doucement.
2. Garder une distance respectueuse.
3. Demander pourquoi elle écrit.
4. Utiliser Inès comme fuite émotionnelle.
5. Sexualiser ou forcer trop tôt.
6. Ne pas répondre.

## Effets recommandés

S’ouvrir :
- `fuite_ines`: +1
- `fatigue_emotionnelle`: -1
- `culpabilite`: +1
- flag `opened_to_ines`

Distance respectueuse :
- `fuite_ines`: -1
- `coherence`: +1
- flag `kept_ines_at_distance`

Pourquoi écrire :
- `fuite_ines`: +1
- flag `asked_ines_why_write`

Fuite émotionnelle :
- `fuite_ines`: +3
- `fatigue_emotionnelle`: +1
- flag `ines_fuite_seed`

Sexualisation trop tôt :
- `fuite_ines`: -2
- `fatigue_emotionnelle`: +2
- flag `sexualized_ines_too_early`

Silence :
- `fuite_ines`: -1
- flag `ignored_ines_j1`

## État de sortie

Inès doit pouvoir disparaître presque complètement si le joueur ne nourrit pas cette porte.
Si le joueur s’y engouffre, elle devient un marqueur de fuite, pas une solution romantique.

## Risque à éviter

Inès ne doit pas devenir une “nouvelle fille disponible”. Elle est un miroir de l’évitement.

---

# Scène `j1_06_sarah_rentrer_manger`

## Fonction

Respiration domestique avec Sarah.
La scène rappelle que Sarah n’est pas seulement une source de reproche : elle est une relation installée, concrète, désirable par le quotidien.

## Déclenchement recommandé

Après `j1_01_sarah_absence`, ou plus tard dans la journée si Sarah n’a pas été complètement ignorée.

## Sarah sait

Elle sait seulement ce qui a déjà été dit dans `j1_01` et son propre malaise.

## Ton

Maison, repas, assiette, café, retour, fatigue.
Simple et humain.

## Choix joueur principaux

1. Rentrer manger / être présent.
2. Promettre de passer plus tard.
3. Dire qu’il ne sait pas encore.
4. Éviter / prétexter le travail.
5. Répondre trop tard.

## Effets recommandés

Présence :
- `confiance_sarah`: +2
- `distance_sarah`: -2
- `intimite_sarah`: +2
- flag `sarah_j1_domestic_presence`

Plus tard :
- `confiance_sarah`: +1
- `fatigue_emotionnelle`: +1
- flag `promised_sarah_later_j1`

Incertitude :
- `distance_sarah`: +1
- `culpabilite`: +1
- flag `sarah_j1_uncertain_return`

Prétexte travail :
- `confiance_sarah`: -1
- `distance_sarah`: +2
- `coherence`: -1
- flag `used_work_excuse_sarah_j1`

Retard :
- `distance_sarah`: +2
- `intimite_sarah`: -1
- flag `late_reply_sarah_meal_j1`

## État de sortie

Sarah peut rester ouverte, fragile ou plus distante.
Cette scène doit donner au joueur une raison émotionnelle de ne pas réduire Sarah au conflit.

## Risque à éviter

Ne pas faire de cette scène une deuxième interrogation sur Camille. Elle doit respirer.

---

# Scène `j1_07_nico_vanne_soiree`

## Fonction

Respiration amicale avec Nico.
Humour, meme, pizza, soirée, puis rappel léger du danger.

## Déclenchement recommandé

Après `j1_03_nico_couverture`, ou en fin de journée pour alléger sans annuler la tension.

## Ton

Oral, drôle, direct.
Une phrase sérieuse peut tomber après une vanne.

## Choix joueur principaux

1. Accepter la respiration / répondre à la vanne.
2. Demander conseil sincèrement.
3. Redemander une couverture.
4. Éviter par humour.
5. Ne pas répondre.

## Effets recommandés

Respiration :
- `fatigue_emotionnelle`: -1
- flag `nico_j1_respiration_shared`

Conseil sincère :
- `coherence`: +1
- `dette_nico`: -1
- flag `asked_nico_real_advice_j1`

Redemander couverture :
- `dette_nico`: +3
- `risque_exposition`: +1
- flag `asked_nico_second_cover_j1`

Humour évitement :
- `fatigue_emotionnelle`: +1
- flag `joked_to_avoid_nico_j1`

Silence :
- `dette_nico`: +1
- flag `ignored_nico_respiration_j1`

## État de sortie

Nico peut rester pote disponible, pote inquiet ou pote déjà utilisé.

## Risque à éviter

Ne pas faire de Nico un tutoriel ou un juge moral. Il aide par amitié, pas par fonction système.

---

# Priorité de génération des dialogues

1. `j1_00_reveil_messages`
2. `j1_01_sarah_absence`
3. `j1_02_camille_dehors`
4. `j1_03_nico_couverture`
5. `j1_04_maya_pique`
6. `j1_05_ines_faille`
7. `j1_06_sarah_rentrer_manger`
8. `j1_07_nico_vanne_soiree`

Chaque scène doit être produite d’abord en version lisible avant conversion JSON Godot.

---

# Format cible pour génération lisible

Pour chaque scène générée en draft :

```text
SCENE_ID:
CONTACT:
FONCTION:
CONNAISSANCES DU CONTACT:
IGNORANCES DU CONTACT:
TON:

MESSAGES:
[ID] Contact : texte
[ID] Joueur : texte

CHOIX:
- [choice_id] Texte joueur
  Effets : {...}
  Flags : [...]
  Suite : ...

SORTIES POSSIBLES:
- ...
```

Une fois validée, la scène peut être convertie en JSON plat compatible Godot.

---

# Critères de validation avant intégration

Une scène J1 est validable si :

- elle a une fonction claire ;
- elle ne donne pas au personnage plus d’informations qu’il n’en possède ;
- elle propose des choix compréhensibles ;
- chaque choix important a effets + flags ;
- la voix du personnage est reconnaissable ;
- les messages sont naturels en messagerie ;
- la scène peut être résumée en une phrase ;
- elle prépare une conséquence future sans tout résoudre immédiatement.
