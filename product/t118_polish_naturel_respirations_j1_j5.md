# T118 — Polish naturel + respirations J1→J5

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : polish texte ciblé des JSON actifs J1→J5, sans changement de schéma ni runtime

## Objectif

Appliquer les corrections prioritaires issues de T117 pour rendre les dialogues J1→J5 moins conceptuels et plus incarnés : moins de vocabulaire auteur (`trace`, `preuve`, `dette`, `coût`, `double vie`, `disponibilité`, `incohérence`, `absence`) dans les messages visibles ; plus de détails concrets, d’oralité et de respirations.

## Corpus modifié

10 dialogues source ont été patchés puis synchronisés avec leur copie Godot `product/godot_t004_prototype/data/` :

- `narrative/t075_camille_j3_complete.json` → `data/camille_j3_complete.json`
- `narrative/t092_camille_j4_complete.json` → `data/camille_j4_complete.json`
- `narrative/t108_camille_j5_complete.json` → `data/camille_j5_complete.json`
- `narrative/t093_maya_j4_complete.json` → `data/maya_j4_complete.json`
- `narrative/t109_maya_j5_complete.json` → `data/maya_j5_complete.json`
- `narrative/t094_ines_j4_complete.json` → `data/ines_j4_complete.json`
- `narrative/t095_nico_j4_complete.json` → `data/nico_j4_complete.json`
- `narrative/t109_nico_j5_complete.json` → `data/nico_j5_complete.json`
- `narrative/t062_sarah_j2_complete.json` → `data/sarah_j2_complete.json`
- `narrative/t107_sarah_j5_complete.json` → `data/sarah_j5_complete.json`

Aucun changement dans :

- `conversation_blocks.json`
- scripts Godot/runtime/save/UX
- structure T003
- IDs de nodes, branches, flags, effets et compteurs

## Changements principaux

### Camille — moins `trace/coût/dette`, plus lieu, téléphone, hésitation

- J4 `c4_006` :
  - avant : “devenir une trace si quelqu’un demande”
  - après : “Juste assez loin de tes habitudes pour que tu hésites déjà.”
- J4 choix/refus `c4_007_b` / `c4_008_b` :
  - avant : “Je ne veux pas créer une trace de plus.”
  - après : “J’ai pas envie de passer ma soirée à regarder derrière moi.”
- J5 `c5_006_a` / `c5_007_a` :
  - avant : “même si ça me coûte ailleurs”
  - après : “même quand je devrais lâcher mon téléphone”
- J5 `c5_019_a` / `c5_020_a` :
  - avant : “créer une dette avec toi”
  - après : “t’accorder une place que je ne sais pas ranger”
- J5 `c5_021_a` :
  - avant : “les dettes affectives…”
  - après : “une belle réponse [ne suffit pas] à remettre les choses droites”

Quelques textes internes de blocs/fins Camille ont aussi été adoucis quand ils étaient potentiellement visibles.

### Inès — moins accusation/preuve, plus version/signe/question

- J4 `i4_001` :
  - avant : “un de tes mensonges innocents”
  - après : “une version un peu arrangée de toi”
- J4 `i4_005_a` :
  - avant : “Un mensonge…”
  - après : “Elle tient debout, ta version…”
- J4 `i4_015` :
  - avant : “une micro-preuve”
  - après : “un signe”
- J4 choix/refus et réponses associées : `preuve` devient `signe` ou `dossier`, pour garder la voix flottante sans posture d’enquête.

### Maya — moins analyse, plus détail social concret

- J4 `m4_018_c` :
  - avant : “une grosse preuve… trois petits détails”
  - après : “le gros truc qui grille quelqu’un… trois petits détails que personne ne devait additionner”
- J5 `m5_005_b` :
  - avant : “une absence commentée…”
  - après : “un ‘il est où ?’ lancé un peu trop vite…”
- J5 `m5_011` :
  - avant : “petites incohérences…”
  - après : “un mini détail peut ruiner un grand discours”
- Fins Maya J5 réécrites de façon moins méta si elles apparaissent au joueur.

### Nico — oralité et limite amicale plus simple

- J4 `n4_006` :
  - avant : “pas une double vie entière… personnage secondaire dans tes mensonges”
  - après : “pas devenir ton standard téléphonique… oublier quelle version je suis censé raconter”
- J4 `n4_023_b` :
  - avant : “risque zéro… distribuer des rôles…”
  - après : “zéro embrouille… filer des rôles…”
- J5 : plusieurs lignes `mensonge/coût/absence` ont été rendues plus orales : excuse qui “porte des chaussures”, Nico qui “lève les yeux au ciel”, “porter le sac”.

### Sarah — ancrage quotidien léger

- J2 `s2_019_c` :
  - avant : “demander ta présence”
  - après : “attendre ton message”
- J5 `s5_007_c` / `s5_008_c` :
  - avant : “chaque absence”
  - après : “un soir où je rentre tard”

## Validation

Validation locale effectuée sur les 14 dialogues actifs J1→J5 :

- JSON parsés avec succès ;
- `schema_version = 0.1` ;
- aucun ID dupliqué ;
- aucun `next` manquant ;
- tous les nodes atteignables depuis `start_node` ;
- effets conformes : flags en chaînes, gauges en entiers ;
- SHA source/copie Godot identiques pour les 14 dialogues actifs.

Tests Python directs exécutés, `pytest` absent sur la machine :

```txt
python3 tests/test_t112_j5_integration.py  OK
python3 tests/test_t097_j4_integration.py  OK
python3 tests/test_t090_dialogue_block_validator.py  OK
python3 tests/test_t078_j3_integration.py  OK
python3 tests/test_t063_j2_integration.py  OK
```

## Limites

- Pas de playtest Godot runtime côté VPS.
- Les textes de blocs système ont été adoucis uniquement dans les JSON quand ils semblaient potentiellement visibles ; `conversation_blocks.json` n’a pas été touché.
- Les flags internes gardent parfois les anciens mots (`trace`, `debt`, etc.) pour préserver compatibilité et logique existante ; le polish vise les textes joueurs.

## Recommandation Roadmap

T118 clôt la séquence Bible → Audit → Polish. Prochaine étape recommandée : reprendre la suite produit avec **T119 — Cadrage J6 / fin MVP après polish**, sans rouvrir J1→J5 sauf retour playtest ciblé.
