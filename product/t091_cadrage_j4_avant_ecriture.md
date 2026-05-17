# T091 — Cadrer J4 avant écriture

Statut : DONE
Thread : Narration jours

## Décision narrative

J4 doit élargir la pression après le socle J1→J3 sans déclencher encore la crise finale. J3 testait l’arbitrage d’attention entre Camille et Sarah ; J4 teste maintenant la **multiplication des fronts** : le joueur commence à gérer non seulement deux intimités, mais des traces sociales, des occasions concrètes, et des tiers qui rendent le mensonge plus coûteux.

Objectif J4 : faire sentir que la double vie devient un système instable, tout en restant jouable en messagerie MVP.

## Portée MVP retenue

J4 reste une journée de messages, sans ajout technique lourd :

- pas d’image obligatoire ;
- pas d’appel ;
- pas de galerie ;
- pas de temps réel / scheduler ;
- pas de calendrier complexe ;
- pas de nouveau schéma T003 ;
- pas de refonte Godot/runtime dans ce ticket ;
- pas de crise totale ou révélation finale prématurée.

Les conséquences J1→J3 doivent rester légères : flags et jauges modulent le ton, les relances et quelques variantes, sans explosion combinatoire.

## Contacts actifs J4

### Camille — tentation plus concrète

Rôle J4 : tirer le joueur vers une disponibilité risquée, plus difficile à justifier.

Évolution :
- elle n’est plus seulement trouble / sous-texte ;
- elle teste si le joueur assume un vrai créneau, une vraie trace, un vrai déplacement ;
- elle doit rester séduisante et ambiguë, pas trop directe ni explicite.

Risque à éviter : répéter le café ou devenir une caricature de tentatrice.

### Maya — miroir social / regard extérieur

Rôle J4 : créer une pression sociale légère, ni amante centrale ni simple outil d’exposition.

Évolution :
- elle peut remarquer des absences, contradictions ou micro-traces ;
- elle peut être complice, ironique, curieuse, ou protectrice selon le ton retenu ;
- elle sert à rendre la double vie visible par le réseau social, pas seulement par les partenaires.

Risque à éviter : transformer Maya en enquêteuse omnisciente.

### Inès — trouble neuf / perturbation

Rôle J4 : ouvrir une nouvelle tension sans voler tout l’espace narratif.

Évolution :
- elle peut être une présence plus directe, une opportunité ou un contact qui déstabilise l’équilibre ;
- son intérêt doit rester encore partiel / ambigu ;
- elle donne au joueur l’impression que la double vie peut s’étendre au-delà de Camille/Sarah.

Risque à éviter : ajouter une troisième romance complète trop tôt ou rendre J4 ingérable.

### Nico — confident / miroir masculin / risque de fuite

Rôle J4 : matérialiser le risque de parler, minimiser, se vanter ou chercher conseil.

Évolution :
- il peut encourager, taquiner, alerter ou couvrir le joueur ;
- il transforme certains choix en traces sociales ;
- il peut ouvrir des flags utiles pour J5 : silence, couverture, malaise, fanfaronnade.

Risque à éviter : faire de Nico un simple tutoriel ou un donneur de leçon.

### Sarah — présence indirecte plutôt qu’active J4

Sarah a porté J1→J3. En J4, elle peut rester visible comme poids émotionnel/historique via archives, souvenirs, flags ou conséquences indirectes, mais le cadrage MVP ne force pas un nouveau dialogue actif Sarah J4 si la structure 5 jours la réserve à J1→J3.

Décision : ne pas écrire Sarah J4 par défaut dans la première vague J4, sauf décision Roadmap contraire.

## Structure de blocs proposée

J4 doit conserver le modèle validé : blocs courts, alternance forcée, attente lisible, notifications neutres.

Proposition de blocs :

- `c4_block_a` — Camille : reprise risquée / disponibilité concrète
- `m4_block_a` — Maya : regard social / remarque légère
- `i4_block_a` — Inès : entrée trouble / perturbation
- `n4_block_a` — Nico : confident ou couverture
- `c4_block_b` — Camille : proposition plus coûteuse
- `m4_block_b` — Maya : pression par incohérence ou observation
- `i4_block_b` — Inès : intérêt ambigu, pas encore romance pleine
- `n4_block_b` — Nico : conseil, provocation ou avertissement
- `c4_block_c` — Camille : trace émotionnelle / point de bascule vers J5
- `i4_block_c` — Inès ou Nico selon priorité Roadmap : clôture de tension J4

Option plus légère si Roadmap veut limiter la charge : 2 blocs par nouveau contact et 3 blocs pour Camille.

## Rythme d’unlocks recommandé

Rythme principal :

```txt
C4A → M4A → I4A → N4A → C4B → M4B → I4B → N4B → C4C → I4C/N4C
```

Intention :
- Camille reste le moteur de risque affectif ;
- Maya et Nico transforment le secret en risque social ;
- Inès ouvre la sensation d’expansion sans devenir tout de suite un troisième arc complet ;
- l’alternance évite les longs tunnels d’un seul contact.

## Conséquences légères à porter depuis J1→J3

À prévoir dans les dialogues J4, sans refonte système :

- `camille_complice` / `camille_distance` : ton plus joueur ou plus prudent ;
- `sarah_trust` / `sarah_doubt` : poids moral, hésitations, phrases d’évitement ;
- `player_presence` / `player_evasion` : cohérence des réponses ;
- nouveaux flags possibles :
  - `maya_noticed_absence`
  - `ines_interest_seeded`
  - `nico_cover_possible`
  - `camille_window_accepted`
  - `j4_social_trace`

Ces flags doivent moduler quelques formulations et préparer J5, pas créer des routes totalement séparées.

## Ton J4

J4 doit être plus nerveux que J3, mais pas explosif.

À privilégier :
- petites contradictions ;
- messages qui arrivent au mauvais moment ;
- silences qui coûtent ;
- phrases à double lecture ;
- choix où répondre à l’un rend l’autre plus risqué ;
- sentiment que le joueur contrôle encore, mais de moins en moins.

À éviter :
- confrontation finale ;
- Sarah policière ;
- Camille trop explicite ;
- Maya omnisciente ;
- Inès déjà trop investie ;
- Nico réduit à un panneau d’explication ;
- répétition des motifs café / dîner / téléphone sur table.

## Découpage tickets recommandé

Pour éviter un gros ticket fragile, J4 doit être découpé en contenu puis intégration :

1. **T092 — Écrire Camille J4 complet intégrable**  
   Thread : Dialogues  
   Livrable : `narrative/t092_camille_j4_complete.json` + copie prototype.

2. **T093 — Écrire Maya J4 complet intégrable**  
   Thread : Dialogues  
   Rôle : pression sociale / regard extérieur.

3. **T094 — Écrire Inès J4 complet intégrable**  
   Thread : Dialogues  
   Rôle : trouble neuf / perturbation.

4. **T095 — Écrire Nico J4 complet intégrable**  
   Thread : Dialogues  
   Rôle : confident / couverture / risque de fuite.

5. **T096 — Relecture cohérence J1→J4**  
   Thread : Dialogues / Narration jours  
   Vérifier voix, timing, contradictions, flags, et absence de crise prématurée.

6. **T097 — Intégrer J4 Godot blocs/unlocks**  
   Thread : Scope MVP / technique  
   Ajouter conversations J4, blocs J4 dans `conversation_blocks.json`, progression Jour 4, tests statiques.

7. **T098 — Playtest runtime J4**  
   Thread : Scope MVP / technique / Roadmap  
   Validation côté Ludo Godot 4.6.

## Ordre conseillé

Commencer par **T092 — Camille J4**, car Camille reste le moteur émotionnel et donne le niveau de pression de la journée. Ensuite écrire Maya/Nico/Inès selon la priorité Roadmap :

- si priorité lisibilité sociale : Maya puis Nico puis Inès ;
- si priorité tension séduisante : Inès puis Maya puis Nico ;
- recommandation actuelle : **Camille → Maya → Inès → Nico**, pour construire d’abord le risque, puis l’expansion, puis la couverture.

## Non-changements

T091 ne modifie pas :

- dialogue JSON ;
- copies prototype ;
- Godot scripts ;
- `conversation_blocks.json` ;
- sauvegarde ;
- UX ;
- schéma T003.

## Next step recommandé

**T092 — Écrire Camille J4 complet intégrable** dans le thread Dialogues, en gardant T003 inchangé et en prévoyant les marqueurs de blocs `c4_block_a`, `c4_block_b`, `c4_block_c`.
