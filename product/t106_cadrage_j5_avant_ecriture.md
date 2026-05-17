# T106 — Cadrer J5 avant écriture

Statut : DONE
Thread : Roadmap / Narration jours

## Décision Roadmap

Après verrouillage J4, la suite retenue est **cadrage J5** plutôt qu’un polish supplémentaire immédiat.

J5 doit transformer la multiplication des fronts de J4 en **coût visible** : le joueur ne gère plus seulement des conversations qui s’ouvrent, mais les premières conséquences concrètes de ses absences, couvertures et ambiguïtés.

Intention J5 : **premier point de pression sérieux**, sans final game-over ni révélation totale obligatoire.

## Test narratif principal

J5 teste : **tenir une double vie quand les témoins commencent à se parler indirectement**.

J1→J3 testait l’attention entre Camille et Sarah.  
J4 testait l’expansion sociale : Maya, Inès, Nico.  
J5 doit tester la **cohérence du mensonge dans un réseau** : ce que le joueur a laissé comme trace commence à peser.

Le joueur doit sentir :

- qu’il peut encore s’en sortir ;
- mais qu’il doit choisir ce qu’il protège ;
- et qu’un mensonge confortable dans une conversation devient coûteux ailleurs.

## Portée MVP retenue

J5 reste une journée de messages, sans nouveau système lourd :

- pas d’image obligatoire ;
- pas d’appel ;
- pas de temps réel / scheduler ;
- pas de calendrier complexe ;
- pas de nouveau schéma T003 ;
- pas de média/gallerie ;
- pas de crise finale définitive ;
- pas de branche combinatoire massive.

Les flags/jauges J1→J4 doivent moduler le ton, certains rappels et quelques choix, pas créer quatre routes séparées.

## Contacts actifs J5

### Sarah — retour du poids intime

Sarah doit redevenir active en J5.

Rôle : rappeler que la double vie n’est pas seulement un jeu de messages séduisants ou sociaux, mais une intimité domestique qui commence à sentir le vide.

Évolution :

- elle ne devient pas policière ;
- elle formule un besoin de présence, une gêne douce, une demande concrète ;
- elle peut mentionner une incohérence sans tout savoir ;
- elle fait peser la culpabilité sans transformer J5 en interrogatoire.

Risque à éviter : Sarah accusatrice ou détective.

### Camille — risque affectif plus coûteux

Camille reste moteur de tentation, mais J5 doit la rendre plus difficile à compartimenter.

Évolution :

- elle ne se contente plus d’une tension abstraite ;
- elle demande une preuve de disponibilité, de courage ou de vérité partielle ;
- elle peut sentir que le joueur hésite ou gère d’autres fronts ;
- elle prépare une vraie conséquence J6/Jfin sans forcer encore la révélation.

Risque à éviter : Camille trop explicite ou ultimatum brutal.

### Maya — témoin social / relais de rumeur

Maya ne doit pas forcément avoir une grosse conversation J5, mais elle doit garder son rôle de témoin social.

Deux options MVP :

- conversation courte active en J5 si on veut tester le réseau social ;
- ou présence via notification/relance légère si on veut limiter la charge.

Rôle : rendre une trace visible, rappeler une absence, offrir/couper une couverture.

Risque à éviter : Maya omnisciente.

### Nico — couverture fragile

Nico peut servir de miroir : il sait assez pour aider ou rendre le joueur imprudent.

Rôle :

- couvrir si le joueur a construit ce lien ;
- alerter si le joueur fanfaronne ;
- créer un coût social si le joueur l’a trop impliqué.

Risque à éviter : Nico qui résout le problème à la place du joueur.

### Inès — perturbation à doser

Inès doit rester une perturbation, pas devenir l’axe central J5 sauf décision Roadmap contraire.

Rôle : rappeler qu’une nouvelle possibilité existe et complique l’équilibre, mais ne pas voler la journée à Sarah/Camille.

Risque à éviter : troisième romance complète trop vite.

## Structure de blocs recommandée

Pour éviter l’explosion J5, Roadmap recommande **6 à 8 blocs**, pas 12 par défaut.

### Version MVP recommandée — 8 blocs

```txt
S5A → C5A → N5A → S5B → C5B → M5A → S5C → C5C
```

Lecture :

- Sarah ouvre la journée par le poids intime ;
- Camille remet la tentation en face ;
- Nico matérialise la couverture/risque social ;
- Sarah revient avec une demande de présence ;
- Camille pousse vers un choix plus coûteux ;
- Maya rappelle qu’il y a des témoins ;
- Sarah et Camille ferment la journée sur deux tensions incompatibles.

### Variante plus sociale — 10 blocs

```txt
S5A → C5A → M5A → N5A → I5A → S5B → C5B → M5B → S5C → C5C
```

À utiliser seulement si Roadmap veut donner à Inès/Maya/Nico plus de place dès J5.

### Variante ultra-MVP — 6 blocs

```txt
S5A → C5A → N5A → S5B → C5B → S5C/C5C
```

À utiliser si on veut d’abord sécuriser Sarah/Camille avant d’étendre le réseau.

## Décision recommandée

Retenir la **version MVP 8 blocs**.

Elle réactive Sarah, garde Camille au centre du risque, conserve Nico/Maya comme pression sociale, et garde Inès en réserve pour éviter surcharge.

## Conséquences légères à porter

Flags/gauges à exploiter légèrement :

- `camille_window_accepted`
- `camille_emotional_debt`
- `j4_social_trace`
- `maya_cover_possible`
- `maya_suspicion_seeded`
- `nico_cover_possible`
- `nico_knows_too_much`
- `player_boasted_nico`
- `ines_interest_seeded`
- `player_kept_distance_ines`
- `sarah_trust`
- `sarah_doubt`
- `player_presence`
- `player_evasion`

Usage recommandé :

- changer une phrase d’ouverture ;
- activer une relance plus sèche ou plus tendre ;
- modifier une option de réponse ;
- préparer J6/Jfin.

Ne pas faire :

- routes entièrement séparées ;
- verrouillage dur incompréhensible ;
- accumulation de checks invisibles.

## Ton J5

J5 doit être plus tendu que J4, mais encore jouable.

À privilégier :

- malaise doux ;
- messages qui forcent à répondre maintenant ;
- couverture sociale fragile ;
- contradiction qui peut encore être rattrapée ;
- choix où protéger Sarah fragilise Camille, ou répondre à Camille rend Sarah plus distante ;
- sentiment que chaque réponse laisse une trace.

À éviter :

- révélation finale ;
- Sarah policière ;
- Camille ultimatum explicite ;
- Maya/Nico qui savent tout ;
- Inès trop centrale ;
- médias/images/appels comme béquille de tension ;
- explosion combinatoire.

## Implications système

T106 ne demande aucun nouveau système.

T117/Tintégration pourra réutiliser :

- `current_day = 5` ;
- `conversation_blocks.json` externalisé ;
- notifications de blocs ;
- toast accès rapide ;
- archives jours précédents ;
- validateur T090.

Aucune migration T003 nécessaire.

## Découpage tickets recommandé

Pour éviter un gros ticket fragile :

1. **T107 — Écrire Sarah J5 complet intégrable**  
   Thread : Dialogues  
   Rôle : retour du poids intime, demande de présence, doute doux.

2. **T108 — Écrire Camille J5 complet intégrable**  
   Thread : Dialogues  
   Rôle : risque affectif plus coûteux, disponibilité/projection.

3. **T109 — Écrire Nico/Maya J5 pression sociale MVP**  
   Thread : Dialogues  
   Rôle : couverture, trace sociale, relais léger.  
   Option : produire deux conversations courtes ou une paire de JSON complets selon charge Roadmap.

4. **T110 — Décider Inès J5 : réserve ou micro-bloc**  
   Thread : Roadmap / Narration jours  
   Décision avant écriture : garder Inès en réserve ou l’intégrer en un bloc court.

5. **T111 — Relecture cohérence J5 / J1→J5**  
   Thread : Dialogues / Narration jours  
   Vérifier Sarah/Camille, traces sociales, Inès dosée, pas de crise finale.

6. **T112 — Intégrer J5 Godot blocs/unlocks**  
   Thread : Scope MVP / technique  
   Ajouter day 5, conversations J5, blocs J5, tests et validateur.

7. **T113 — Playtest runtime J5**  
   Thread : Scope MVP / Roadmap  
   Validation côté Ludo Godot 4.6.

8. **T114 — Verrouiller J5 intégré**  
   Thread : Roadmap  
   Documentation/status lock si runtime validé.

## Ordre conseillé

Commencer par **T107 — Sarah J5**, car J5 doit réactiver le poids intime avant de relancer la tentation Camille.

Puis :

```txt
T107 Sarah → T108 Camille → T109 Nico/Maya → T110 décision Inès → T111 cohérence → T112 intégration
```

## Non-changements

T106 ne modifie pas :

- dialogue JSON ;
- copies prototype ;
- Godot scripts ;
- `conversation_blocks.json` ;
- sauvegarde ;
- UX ;
- schéma T003.

## Next step recommandé

**T107 — Écrire Sarah J5 complet intégrable** dans le thread Dialogues, avec marqueurs de blocs `s5_block_a`, `s5_block_b`, `s5_block_c` si la version 8 blocs est confirmée.
