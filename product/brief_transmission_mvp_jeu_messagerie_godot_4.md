# BRIEF DE TRANSMISSION — MVP Jeu de messagerie Godot 4

## Objectif du brief

Ce document sert à transmettre clairement le projet à une IA, un développeur, ou à une nouvelle conversation ChatGPT/Hermes IA.

Le but est de transformer un MVP commencé sous Godot 4 en jeu narratif de messagerie structuré, sans réinventer le scénario ni perdre les choix de conception déjà validés.

---

# 1. Pitch du jeu

Le jeu est une simulation narrative par messagerie.

Le joueur incarne une personne en couple avec Sarah. Après une soirée de groupe ambiguë, il se réveille avec plusieurs messages. Chaque personnage possède un morceau différent de ce qui s’est passé ou de ce qu’il a perçu.

Le joueur doit répondre aux messages, choisir qui prioriser, quoi dire, quoi cacher, quoi assumer, quoi ignorer, quoi supprimer ou garder. Ses choix modifient les relations, la cohérence de ses versions, le risque d’exposition, la culpabilité, le désir, la confiance et les fins possibles.

Le thème central n’est pas seulement l’infidélité ou la séduction, mais :

> l’évitement du choix, les demi-vérités, la culpabilité, le désir, la fuite et les conséquences relationnelles.

Le jeu ne doit pas être un dating sim classique où le joueur “gagne” un personnage. Il doit être un jeu de tension relationnelle où chaque choix révèle une manière d’aimer, d’éviter, de mentir ou d’assumer.

---

# 2. Format du MVP

Le MVP couvre 6 jours.

Structure :

```text
Jour 1 — Le lendemain
Jour 2 — Les versions
Jour 3 — Les liens ordinaires
Jour 4 — L’intimité / l’image
Jour 5 — Les limites
Jour 6 — La conséquence
```

Le MVP doit être conçu comme un épisode pilote complet : il raconte une crise entière, mais laisse des états narratifs exploitables pour une suite.

---

# 3. Situation de départ

La veille du Jour 1, le joueur était à une soirée de groupe.

Personnages présents :

- Sarah : compagne du joueur ;
- Camille : collègue de travail du joueur ;
- Maya : meilleure amie de Sarah, aussi amie avec le joueur ;
- Nico : confident du joueur ;
- Inès : amie du groupe, plus discrète et énigmatique.

Pendant la soirée, le joueur sort prendre l’air. Camille le rejoint. Ils restent absents environ vingt minutes.

Il ne s’est pas forcément passé quelque chose de physiquement irréversible : pas forcément de baiser, pas forcément de sexe. Mais il y a eu un moment émotionnellement trop intime : une conversation chargée, une proximité, un silence, peut-être un contact physique ambigu.

Le vrai problème n’est pas seulement ce qui a été fait. Le vrai problème est que le joueur revient auprès de Sarah avec quelque chose de déplacé intérieurement.

---

# 4. Ce que chaque personnage sait

## Sarah

Sarah sait que le joueur a disparu pendant la soirée, qu’il est revenu différent, et que Camille était absente à un moment proche. Elle ne sait pas ce qui s’est passé dehors.

Elle veut une présence réelle et une vérité qui ne la fasse pas douter d’elle-même.

Elle ne doit pas être écrite comme une enquêtrice.

## Camille

Camille sait que le moment dehors n’était pas neutre. Elle sait que le joueur peut être tenté de minimiser.

Elle veut être reconnue comme une personne, pas comme une échappatoire émotionnelle ou sexuelle.

Elle accepte le trouble, mais refuse d’être utilisée comme refuge.

## Maya

Maya ne sait pas tout, mais elle voit les micro-incohérences : absences, timing, photos, comportement du joueur.

Elle est la meilleure amie de Sarah, mais pas l’ennemie du joueur.

Elle refuse de mentir pour protéger une version fausse.

## Nico

Nico sait qu’il a couvert l’absence du joueur, mais il ne sait pas forcément ce qui s’est passé avec Camille.

Il est loyal et drôle, mais il ne peut pas devenir un alibi permanent.

## Inès

Inès ne connaît presque rien des faits. Elle a surtout perçu l’état intérieur du joueur : il avait l’air ailleurs, comme s’il cherchait une sortie.

Elle représente une porte latérale, une fuite douce, mais pas une vraie route romantique complète dans le MVP.

---

# 5. Signatures vocales

Les personnages doivent être immédiatement différenciables dans les messages.

## Sarah — Ancrage

- Monde : maison, couple, quotidien.
- Ton : simple, concret, doux, parfois blessé.
- Exemples :
  - “Tu rentres manger ?”
  - “Je t’ai gardé une assiette.”
  - “Je veux pas te faire un procès.”
  - “Dis-moi juste si je me trompe.”

## Camille — Lucidité

- Monde : travail, détour, tension, désir, précision.
- Ton : incisif, oblique, lucide, rarement gratuit.
- Exemples :
  - “Je note le détour.”
  - “Tu vas faire comme si c’était juste une discussion dehors ?”
  - “Tu réponds à côté.”
  - “Je ne veux pas être ton endroit où respirer quand le reste t’étouffe.”

## Maya — Observation

- Monde : groupe social, timing, photos, absences.
- Ton : court, piquant, rapide, social.
- Exemples :
  - “je pose ça là”
  - “je note”
  - “ton timing est une œuvre d’art”
  - “si Sarah me demande directement, je mens pas.”

## Nico — Oralité

- Monde : amitié, vanne, alibi, limite.
- Ton : oral, drôle, familier, direct.
- Exemples :
  - “frérot”
  - “plan claqué”
  - “t’as besoin d’un alibi ou d’un psy ?”
  - “je peux couvrir un blanc. pas toute ta vie.”

## Inès — Flottement

- Monde : marge, nuit, perception, hésitation.
- Ton : doux, étrange, rare, légèrement flottant.
- Exemples :
  - “j’ai hésité avant d’écrire”
  - “c’est bizarre à dire”
  - “pas grave si tu réponds plus tard”
  - “tu avais l’air ailleurs, mais pas absent.”

---

# 6. Variables principales

Toutes les variables sont sur 0–100.

Variables à conserver :

```text
confiance_sarah
mesure si Sarah peut croire que le joueur lui parle vraiment

distance_sarah
mesure l’éloignement ressenti par Sarah

tension_camille
mesure la charge affective et désirante avec Camille

respect_camille
mesure si Camille se sent respectée et non utilisée

pression_camille
mesure si Camille sent que le joueur pousse trop

intimite_sarah
mesure la chaleur domestique avec Sarah

intimite_camille
mesure la proximité avec Camille au-delà du désir

attente_image_camille
mesure l’attente, l’imaginaire et le fantasme autour d’une image possible de Camille

suspicion_maya
mesure le niveau d’alerte sociale de Maya

dette_nico
mesure le poids que le joueur fait porter à Nico

fuite_ines
mesure la tentation de chercher une porte latérale

coherence
mesure si les versions données par le joueur tiennent ensemble

culpabilite
mesure la charge intérieure du joueur

risque_exposition
mesure le risque que les traces deviennent visibles

fatigue_emotionnelle
mesure le coût psychique des mensonges, silences et tensions
```

Valeurs initiales recommandées :

```json
{
  "confiance_sarah": 55,
  "distance_sarah": 35,
  "tension_camille": 55,
  "respect_camille": 50,
  "pression_camille": 30,
  "intimite_sarah": 45,
  "intimite_camille": 45,
  "attente_image_camille": 0,
  "suspicion_maya": 40,
  "dette_nico": 20,
  "fuite_ines": 10,
  "coherence": 60,
  "culpabilite": 35,
  "risque_exposition": 25,
  "fatigue_emotionnelle": 20
}
```

Règle : les effets de scène sont relatifs. Exemple :

```json
"effects": {
  "confiance_sarah": 5,
  "distance_sarah": -3
}
```

signifie :

```gdscript
confiance_sarah += 5
distance_sarah -= 3
```

Puis clamp entre 0 et 100.

---

# 7. Système de timing

Le jeu ne doit pas nécessairement utiliser du temps réel. Il utilise un temps narratif contrôlé.

Blocs de temps :

```text
morning
midday
afternoon
evening
night
```

Le joueur peut :

- répondre immédiatement ;
- répondre tard ;
- lire sans répondre ;
- ignorer ;
- ouvrir une conversation avant une autre ;
- ouvrir ou non une image ;
- garder, supprimer ou revoir une image.

Dans ce jeu, ne pas répondre est une action.

Répondre à Camille pendant que Sarah attend doit produire une conséquence. Répondre à Nico seulement quand il faut mentir doit produire une conséquence. Ouvrir une image au mauvais moment doit produire une conséquence.

---

# 8. Images, désir et contenu adulte

Les images ne sont pas de simples récompenses. Elles sont des objets relationnels.

Une image peut :

- nourrir l’attente ;
- nourrir l’imaginaire ;
- créer du fantasme ;
- augmenter le désir ;
- augmenter la culpabilité ;
- devenir une trace ;
- être supprimée ;
- être gardée ;
- être revue ;
- être découverte.

Camille est le cœur du système intime du MVP.

Sarah peut avoir une intimité de couple plus douce et domestique.

Inès ne doit pas devenir une route sexuelle dans le MVP.

Maya et Nico ne doivent pas être sexualisés.

Niveaux d’image possibles :

```text
Niveau 0 — banal / quotidien
Niveau 1 — ambigu / suggestif léger
Niveau 2 — sexy assumé non explicite
Niveau 3 — intime NSFW optionnel pour version future
Niveau 4 — adulte premium optionnel pour version future
```

Le contenu NSFW/premium est une idée pour plus tard, pas pour le MVP. Il doit rester optionnel, clairement adulte, lié au consentement, et ne pas bloquer la compréhension du récit principal.

Principe important :

> Le contenu adulte enrichit une relation déjà écrite. Il ne remplace pas la relation.

---

# 9. Fins du MVP

Le MVP a 6 fins principales :

## FIN_SARAH_REPARATION_FRAGILE

Le joueur a parlé suffisamment clairement pour que Sarah ne se sente pas folle ou humiliée. La réparation est possible, mais fragile.

## FIN_SARAH_FACADE

Le couple continue, mais sur un silence. Rien n’explose, mais rien n’est vraiment réparé.

## FIN_CAMILLE_REFUSE_REFUGE

Camille comprend qu’elle est devenue une échappatoire. Elle refuse d’être utilisée comme refuge.

## FIN_CAMILLE_SUITE_PRUDENTE

Camille accepte une possibilité, mais sous conditions. Ce n’est pas une récompense romantique, c’est une ouverture fragile.

## FIN_EFFONDREMENT_SOCIAL

Les contradictions parlent à la place du joueur. Sarah, Camille, Nico et Maya se croisent dans les conséquences. Le joueur perd le contrôle de sa version.

## FIN_FUITE_INES

Le joueur ne choisit pas vraiment. Il part vers Inès comme vers une parenthèse. C’est doux en surface, inquiétant en profondeur.

Priorité de sélection des fins :

```text
1. FIN_EFFONDREMENT_SOCIAL
2. FIN_FUITE_INES
3. FIN_CAMILLE_REFUSE_REFUGE
4. FIN_CAMILLE_SUITE_PRUDENTE
5. FIN_SARAH_REPARATION_FRAGILE
6. FIN_SARAH_FACADE
```

---

# 10. Scènes du Jour 1 déjà structurées

Le Jour 1 est la première boucle narrative complète.

Fichiers prévus :

```text
j1_00_reveil_messages.json
j1_01_sarah_absence.json
j1_02_camille_dehors.json
j1_03_nico_couverture.json
j1_04_maya_pique.json
j1_05_ines_faille.json
j1_06_sarah_rentrer_manger.json
j1_07_nico_vanne_soiree.json
```

Rôle de chaque scène :

## j1_00_reveil_messages.json

Scène d’ouverture. Cinq messages arrivent. Le joueur choisit à qui répondre en premier.

Messages :

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

## j1_01_sarah_absence.json

Sarah demande où le joueur était pendant la soirée. La scène fixe la première version donnée à Sarah.

Flags importants :

```text
used_nico_alibi_sarah
mentioned_camille_to_sarah
minimized_camille_to_sarah
vulnerable_to_sarah
ignored_sarah_j1
```

## j1_02_camille_dehors.json

Camille demande si le joueur va faire comme si le moment dehors était banal.

Flags importants :

```text
admitted_tension_to_camille
protected_camille_boundary
minimized_with_camille
uncertain_with_camille
early_desire_to_camille
ignored_camille_j1
```

## j1_03_nico_couverture.json

Nico demande quelle version il doit connaître ou tenir. Il peut aider, mais pas devenir un outil.

Flags importants :

```text
asked_nico_hold_version
told_nico_stay_silent
confessed_camille_to_nico
vulnerable_to_nico
dismissed_nico_warning
nico_full_alibi
```

## j1_04_maya_pique.json

Maya signale une incohérence sociale. Elle voit le timing, pas toute la vérité.

Flags importants :

```text
played_dumb_with_maya
info_maya_photo_possible
told_maya_needed_air
told_maya_not_involve
joked_with_maya_j1
asked_maya_if_sarah_talked
ignored_maya_j1
```

## j1_05_ines_faille.json

Inès perçoit l’état intérieur du joueur. Elle ouvre une porte latérale, pas une romance complète.

Flags importants :

```text
opened_to_ines
ines_fuite_seed
asked_ines_why_write
kept_ines_at_distance
sexualized_ines_too_early
ignored_ines_j1
```

## j1_06_sarah_rentrer_manger.json

Respiration domestique avec Sarah. Repas, assiette gardée, présence.

## j1_07_nico_vanne_soiree.json

Respiration avec Nico. Meme, humour, mais rappel du danger.

---

# 11. Structure JSON recommandée pour une scène

Chaque scène peut suivre ce modèle :

```json
{
  "scene_id": "j1_01_sarah_absence",
  "title": "Où tu étais ?",
  "day": 1,
  "time_block": "morning",
  "time_index": 2,
  "scene_type": "conversation",
  "contact": "sarah",
  "description": "Description courte de la scène.",
  "conditions": {},
  "entry_variants": [],
  "player_prompt": "Que répondre ?",
  "choice_mode": "single_reply",
  "choices": [
    {
      "choice_id": "needed_air",
      "label": "Dire que tu avais besoin d’air",
      "player_text": "J’avais besoin d’air.",
      "effects": {
        "coherence": 2,
        "confiance_sarah": 1
      },
      "flags_set": ["said_needed_air_to_sarah"],
      "unlock_scenes": [],
      "time_advance": "short"
    }
  ],
  "completion_flags": ["completed_j1_01_sarah_absence"],
  "default_return_to": "conversation_list"
}
```

---

# 12. Structure Godot recommandée

Arborescence conseillée :

```text
res://data/
  schema/
    variables_and_flags_schema.json

  scenes/
    day_1/
      j1_00_reveil_messages.json
      j1_01_sarah_absence.json
      j1_02_camille_dehors.json
      j1_03_nico_couverture.json
      j1_04_maya_pique.json
      j1_05_ines_faille.json
      j1_06_sarah_rentrer_manger.json
      j1_07_nico_vanne_soiree.json

    day_2/
      j2_01_nico_version.json
      j2_02_maya_photo.json
      j2_03_sarah_quotidien.json
      j2_04_camille_detour.json
      j2_05_priorite_soir.json

  media/
    images/
      sarah/
      camille/
      maya/
      nico/
      ines/
```

Autoloads recommandés :

## NarrativeState.gd

Gère :

- variables ;
- flags ;
- états de contacts ;
- états de médias ;
- sauvegarde / chargement ;
- application des effets.

## DialogueLoader.gd

Gère :

- chargement JSON ;
- validation des conditions ;
- récupération des scènes disponibles.

## DialogueRunner.gd

Gère :

- affichage des messages ;
- choix du joueur ;
- application des effets ;
- progression du temps ;
- scènes débloquées.

---

# 13. Boucle minimale à tester

La première boucle jouable doit faire :

```text
1. Charger variables_and_flags_schema.json
2. Initialiser les variables
3. Charger j1_00_reveil_messages.json
4. Afficher les 5 messages entrants
5. Choisir à qui répondre en premier
6. Appliquer les effets et flags
7. Débloquer les conversations du Jour 1
8. Jouer une conversation individuelle
9. Revenir à la liste de conversations
10. Continuer jusqu’à completed_day_1_core
```

---

# 14. Ce qu’il faut demander à Hermes IA ou à une nouvelle IA

Instruction recommandée :

```text
Je développe un jeu narratif de messagerie sous Godot 4. Voici le brief complet du MVP.

Je veux que tu m’aides à transformer mon prototype existant pour l’adapter à cette structure.

Ne réinvente pas le scénario.
Respecte les personnages, les voix, les variables et le format JSON.
Commence par analyser l’architecture actuelle du projet, puis propose les modifications nécessaires.
Ensuite, aide-moi à implémenter progressivement :

1. variables_and_flags_schema.json
2. NarrativeState.gd
3. DialogueLoader.gd
4. DialogueRunner.gd
5. la scène j1_00_reveil_messages.json
6. la boucle de conversation du Jour 1
```

---

# 15. Priorité de développement conseillée

Ne pas écrire tout le jeu immédiatement.

Priorité :

```text
1. Faire fonctionner le schéma variables/flags
2. Charger une scène JSON
3. Afficher des messages
4. Proposer des choix
5. Appliquer les effets
6. Débloquer une autre scène
7. Sauvegarder l’état
8. Tester tout le Jour 1
9. Seulement ensuite écrire le Jour 2
```

Le Jour 1 suffit à valider toute l’architecture du MVP.

---

# 16. Règles à ne pas oublier

- Personne ne doit être omniscient.
- Les conversations banales doivent exister.
- Le silence est un choix.
- Répondre tard est un choix.
- L’ordre des réponses est un choix.
- Les images sont des objets narratifs, pas seulement des récompenses.
- Le désir et le respect sont séparés.
- Nico peut aider, mais pas sauver.
- Maya observe, mais ne sait pas tout.
- Inès ouvre une fuite, pas une solution.
- Sarah ne doit pas être seulement la culpabilité.
- Camille ne doit pas être seulement la récompense sexy.
- Les fins dépendent de la manière d’agir, pas seulement de “qui choisir”.

---

# 17. Résumé en une phrase

Le jeu est une simulation de messagerie où le joueur tente de maintenir plusieurs liens après une soirée ambiguë, mais chaque réponse, silence, image, retard et demi-vérité modifie la manière dont les autres le voient — jusqu’à une fin qui révèle moins qui il choisit que la manière dont il a traité les personnes autour de lui.

