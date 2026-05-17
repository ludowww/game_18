# Double Vie — Source de vérité courte refonte MVP

## Rôle du document

Ce fichier est la base compacte de travail pour réaligner le prototype existant avec la nouvelle vision du MVP.
Il ne remplace pas les documents complets :

- `product/brief_transmission_mvp_jeu_messagerie_godot_4.md`
- `product/jeu_messagerie_mvp_documents_de_conception.md`

Il sert de référence courte pour générer, relire et intégrer les dialogues sans recréer du flou.

---

## Vision courte

Double Vie est une simulation narrative par messagerie.
Le joueur se réveille après une soirée de groupe ambiguë. Plusieurs personnes lui écrivent, chacune avec un morceau différent de ce qui s’est passé ou de ce qu’elle a perçu.

Le joueur choisit :

- à qui répondre en premier ;
- quoi dire ;
- quoi taire ;
- quoi minimiser ;
- qui rassurer ;
- qui utiliser comme alibi ;
- quels messages laisser sans réponse ;
- quelles traces garder ou supprimer plus tard.

Le cœur du jeu n’est pas de “gagner” une route romantique. Le cœur du jeu est de révéler comment le joueur aime, évite, ment, assume ou fuit.

---

## Thème central

Le jeu parle de :

- demi-vérités ;
- culpabilité ;
- désir ;
- évitement du choix ;
- loyauté émotionnelle ;
- tension entre version intime et version sociale ;
- conséquences relationnelles des silences.

Le vrai danger n’est pas seulement ce qui s’est passé. Le vrai danger est que le joueur tente de maintenir plusieurs versions incompatibles.

---

## Vérité canonique de départ

La veille du Jour 1, le joueur était à une soirée de groupe avec :

- Sarah, sa compagne ;
- Camille, collègue avec qui une complicité trouble existe déjà ;
- Maya, meilleure amie de Sarah et amie du joueur ;
- Nico, confident du joueur ;
- Inès, amie plus discrète et observatrice.

Pendant la soirée, le joueur est sorti prendre l’air. Camille l’a rejoint. Ils sont restés absents environ vingt minutes.

Il ne s’est pas forcément passé un acte physique irréversible :

- pas forcément de baiser ;
- pas forcément de sexe ;
- pas de preuve claire à ce stade.

Mais il y a eu un moment émotionnellement trop intime :

- proximité ;
- silence trop long ;
- phrase qui franchit une limite ;
- contact possible mais volontairement ambigu ;
- trouble que le joueur n’a pas vraiment interrompu.

Le joueur est revenu auprès de Sarah avec quelque chose de déplacé intérieurement.

---

## Carte de connaissance J1

### Sarah

Sarah sait :

- que le joueur était moins présent pendant la soirée ;
- qu’il a disparu ou s’est absenté ;
- que Camille était aussi absente à un moment proche ;
- que Nico a donné une explication qui semblait improvisée ;
- que le joueur est revenu différent.

Sarah ignore :

- ce qui s’est dit dehors ;
- s’il y a eu contact physique ;
- ce que le joueur dit aux autres ;
- jusqu’où Camille compte vraiment.

Fonction : la maison, la présence, la confiance installée, la peur de devenir une façade.

À éviter : Sarah détective, Sarah omnisciente, Sarah simple culpabilité.

### Camille

Camille sait :

- qu’elle a rejoint le joueur dehors ;
- que le moment n’était pas neutre ;
- que le joueur peut avoir envie de minimiser ;
- qu’il était troublé.

Camille ignore :

- ce que Sarah sait exactement ;
- ce que le joueur a dit à Sarah ;
- ce que Nico ou Maya ont vu ;
- si le joueur est prêt à clarifier quoi que ce soit.

Fonction : lucidité, trouble, désir relationnel, limite de dignité.

À éviter : Camille récompense sexy automatique, Camille jalouse caricaturale, Camille refuge pratique.

### Maya

Maya sait :

- que le joueur et Camille ont été absents ou difficiles à situer ;
- que Sarah a senti quelque chose ;
- que Nico a couvert ou simplifié ;
- que certains timings sont suspects.

Maya ignore :

- ce qui s’est réellement passé dehors ;
- la vérité intime du joueur ;
- ce que Sarah sait déjà ;
- ce que Camille cherche.

Fonction : regard social, timing, photo, conflit de loyauté.

À éviter : Maya policière, Maya omnisciente, Maya outil d’exposition.

### Nico

Nico sait :

- qu’il a couvert ou simplifié l’absence du joueur ;
- que le joueur est troublé par Camille ;
- que son explication peut devenir fragile ;
- que Sarah ou Maya pourraient lui poser des questions.

Nico ignore :

- le contenu exact du moment dehors ;
- le niveau d’intimité avec Camille ;
- la version donnée à Sarah ;
- ce que Maya a vu.

Fonction : amitié, humour, alibi, limite.

À éviter : Nico sauveur magique, Nico simple distributeur d’alibis, Nico moraliste permanent.

### Inès

Inès sait :

- que le joueur avait l’air ailleurs ;
- qu’il semblait chercher une sortie ;
- que quelque chose sonnait faux dans son état.

Inès ignore :

- la tension exacte avec Camille ;
- l’état réel du couple avec Sarah ;
- le rôle de Nico ;
- les observations de Maya.

Fonction : porte latérale, douceur, fuite, miroir de l’évitement.

À éviter : route sexuelle/romantique complète dans le MVP, nouvelle option disponible, fuite récompensée.

---

## Signatures vocales rapides

Sarah : maison, concret, présence. Messages simples, détails domestiques, douleur contenue.
Exemple : “Je t’ai gardé une assiette.”

Camille : lucidité, détour, trouble. Messages précis, incisifs, rarement gratuits.
Exemple : “Je note le détour.”

Maya : social, timing, pique. Messages courts, rapides, observation publique.
Exemple : “je pose ça là.”

Nico : pote, vanne, limite. Oralité forte, humour, sérieux soudain.
Exemple : “frérot, ça sent le plan claqué.”

Inès : marge, hésitation, étrangeté douce. Messages rares, flottants, non intrusifs.
Exemple : “c’est bizarre à dire.”

Règle de relecture : si une phrase pourrait être dite par deux personnages, elle doit être réécrite.

---

## Variables officielles V2

Toutes les variables sont bornées entre 0 et 100.
Les effets de choix sont relatifs et doivent être clampés.

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

---

## Règles d’écriture J1

- Personne ne doit être omniscient.
- Les soupçons doivent venir du banal : horaire, absence, téléphone, photo, ton, retour étrange.
- Le silence est une action.
- Répondre tard est une action.
- L’ordre des réponses est une action.
- Une scène doit avoir une fonction jouable, pas seulement une ambiance.
- Les choix ne doivent pas être “gentil / méchant”.
- Chaque choix important doit poser au moins un flag ou modifier au moins une variable.
- Les conversations banales doivent exister : le drame devient crédible parce qu’il repose sur du quotidien.
- Le désir doit rester relationnel : il dépend du respect, du timing et de la clarté.

---

## Structure J1 cible

1. `j1_00_reveil_messages` — cinq messages au réveil, choix de priorité.
2. `j1_01_sarah_absence` — première version donnée à Sarah.
3. `j1_02_camille_dehors` — reconnaissance ou minimisation du moment dehors.
4. `j1_03_nico_couverture` — alibi, dette et limite de Nico.
5. `j1_04_maya_pique` — incohérence sociale, photo/timing, loyauté Sarah.
6. `j1_05_ines_faille` — porte latérale, perception de fuite.
7. `j1_06_sarah_rentrer_manger` — respiration domestique.
8. `j1_07_nico_vanne_soiree` — respiration amicale et rappel du danger.

---

## Intégration technique recommandée

Ne pas casser l’existant.

Court terme :

- garder le format JSON plat actuellement compatible Godot ;
- créer les scènes J1 V2 en fichiers séparés ;
- ajouter le schéma variables/flags V2 ;
- préserver les anciens dialogues tant que la V2 n’est pas branchée ;
- valider les dialogues avant intégration runtime.

Moyen terme :

- adapter `ConversationState` pour initialiser les variables V2 ;
- adapter `_apply_effects` pour clamp 0–100 ;
- migrer ou mapper progressivement les anciennes variables ;
- créer une boucle J1 V2 jouable avec les cinq contacts dès le départ.

---

## Priorité immédiate

Ne pas générer tout J1 immédiatement.

Ordre :

1. cadrer les scènes J1 ;
2. créer le schéma variables/flags ;
3. générer `j1_00_reveil_messages` en version lisible ;
4. relire voix et clarté ;
5. convertir en JSON Godot ;
6. intégrer runtime ;
7. seulement ensuite générer Sarah/Camille/Nico/Maya/Inès J1.
