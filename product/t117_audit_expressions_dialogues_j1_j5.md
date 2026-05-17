# T117 — Audit expressions bizarres / dialogues trop conceptuels J1→J5

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : audit texte uniquement, sans patch JSON/Godot

## Objectif

Auditer les dialogues actifs J1→J5 après T116 pour repérer :

- les expressions trop conceptuelles ;
- les lignes qui sonnent comme des notes d’auteur ;
- les choix trop mécaniques ou trop dramatiques ;
- les endroits où les personnages perdent leur voix propre ;
- les blocs où la pression dramatique écrase les respirations.

T117 ne modifie pas les JSON. Il prépare le polish T118.

## Corpus audité

Dialogues actifs :

- Camille J1 : `narrative/t007_camille_j1_complete.json`
- Sarah J1 : `narrative/t037_sarah_j1_complete.json`
- Camille J2 : `narrative/t061_camille_j2_complete.json`
- Sarah J2 : `narrative/t062_sarah_j2_complete.json`
- Camille J3 : `narrative/t075_camille_j3_complete.json`
- Sarah J3 : `narrative/t076_sarah_j3_complete.json`
- Camille J4 : `narrative/t092_camille_j4_complete.json`
- Maya J4 : `narrative/t093_maya_j4_complete.json`
- Inès J4 : `narrative/t094_ines_j4_complete.json`
- Nico J4 : `narrative/t095_nico_j4_complete.json`
- Sarah J5 : `narrative/t107_sarah_j5_complete.json`
- Camille J5 : `narrative/t108_camille_j5_complete.json`
- Nico J5 : `narrative/t109_nico_j5_complete.json`
- Maya J5 : `narrative/t109_maya_j5_complete.json`

Total actuel validateur : 14 dialogues actifs, 38 blocs.

## Synthèse Roadmap

Le contenu J1→J5 est cohérent et intégrable, mais l’audit confirme le ressenti produit : certains dialogues parlent parfois comme le **concept du jeu** plutôt que comme des personnes.

Le problème n’est pas bloquant pour le prototype, mais il limite l’attachement :

- les mots `trace`, `preuve`, `dette`, `coût`, `absence`, `mensonge`, `disponibilité` reviennent souvent ;
- certains titres de blocs sont explicitement conceptuels, ce qui est acceptable côté outil, mais dangereux si la formulation glisse dans les messages ;
- Camille, Maya et Nico utilisent parfois un vocabulaire très méta sur les traces, preuves, dettes ;
- Sarah reste globalement la plus naturelle, mais certains choix peuvent encore être adoucis ;
- Inès J4 a plusieurs formulations intéressantes, mais elle parle parfois trop frontalement en “preuve/mensonge/disponibilité” pour un personnage censé être flottant et hésitant.

Priorité T118 : ne pas réécrire toute la structure, mais remplacer les lignes les plus conceptuelles par des formulations concrètes, situées, humaines.

## Comptage indicatif des signaux conceptuels

Audit automatique sur mots à surveiller issus de T116 : `trace`, `preuve`, `dette`, `coût`, `double vie`, `disponibilité`, `incohérence`, `conséquence`, `fuite`, `risque`, `mensonge`, `présence`, `absence`.

Résultat indicatif par contact :

| Contact | Messages actifs audités | Choix audités | Hits conceptuels | Remarque |
|---|---:|---:|---:|---|
| Camille | 216 | 28 | 32 | Voix forte, mais trop souvent conceptualisée en trace/coût/dette. |
| Sarah | 163 | 21 | 11 | Globalement naturelle ; garder concret/domestique. |
| Maya | 76 | 10 | 14 | Bon piquant social, mais attention à `trace`/`incohérence`. |
| Nico | 77 | 10 | 18 | Très bon oral/humour ; quelques phrases trop explicatives. |
| Inès | 48 | 6 | 13 | Doit devenir plus rare/flottante, moins “preuve/mensonge”. |

Ce comptage n’est pas un jugement mécanique : certains mots sont justifiés. Il sert à prioriser le polish.

## Audit prioritaire — lignes à corriger en T118

### 1. Camille J4 — formulation trop “système de traces”

Fichier : `narrative/t092_camille_j4_complete.json`  
Node : `c4_006`

Actuel :

> Quarante minutes. Fin d’après-midi. Un endroit banal, mais assez loin de tes habitudes pour devenir une trace si quelqu’un demande.

Problème : Camille parle presque comme le système de risque du jeu. Le mot `trace` est trop frontal.

Direction T118 : rendre ça plus incarné.

Proposition :

> Quarante minutes. Fin d’après-midi. Un endroit banal. Juste assez loin de tes habitudes pour que tu hésites déjà.

---

### 2. Camille J4 — choix trop mécanique

Fichier : `narrative/t092_camille_j4_complete.json`  
Node : `c4_007` / `c4_008_b`

Actuel :

> Je ne veux pas créer une trace de plus.

Problème : choix très fonctionnel, peu naturel en messagerie.

Proposition :

> J’ai pas envie de laisser encore un détail derrière moi.

ou, plus Camille :

> Je sais déjà que je vais regarder derrière mon épaule.

---

### 3. Camille J5 — `coût` et `dette` trop explicites

Fichier : `narrative/t108_camille_j5_complete.json`  
Nodes : `c5_006`, `c5_007_a`, `c5_019`, `c5_020_a`, `c5_021_a`

Actuels :

> Je garde un fil avec toi, même si ça me coûte ailleurs.

> Je sais. Et je suis en train de créer une dette avec toi.

> Alors n’oublie pas que les dettes affectives ne se règlent pas avec des messages plus beaux.

Problème : Camille peut être lucide, mais la répétition `coût/dette` fait note d’auteur.

Propositions :

> Je garde un fil avec toi, même quand je devrais lâcher mon téléphone.

> Je sais. Et je suis en train de t’accorder une place que je ne sais pas ranger.

> Alors ne fais pas comme si une belle réponse suffisait à remettre les choses droites.

---

### 4. Maya J4 — formulation trop analytique

Fichier : `narrative/t093_maya_j4_complete.json`  
Node : `m4_018_c`

Actuel :

> Ça se voit rarement par une grosse preuve. Ça se voit par trois petits détails que personne ne regarde au même moment.

Problème : bonne idée, mais le mot `preuve` et la structure sonnent très auteur.

Proposition :

> En général c’est pas le gros truc qui grille quelqu’un. C’est trois petits détails que personne ne devait additionner.

---

### 5. Maya J5 — ligne trop conceptuelle

Fichier : `narrative/t109_maya_j5_complete.json`  
Node : `m5_011`

Actuel :

> C’est souvent là que les petites incohérences deviennent plus lourdes que les grandes déclarations.

Problème : Maya explique le thème. Elle doit piquer avec un détail social.

Proposition :

> C’est souvent là que les petits “ah oui c’est vrai” commencent à peser plus lourd que les grands discours.

ou plus naturel :

> C’est fou comme un mini détail peut ruiner un grand discours.

---

### 6. Maya J5 — fin trop “radar/trace”

Fichier : `narrative/t109_maya_j5_complete.json`  
Nodes : `m5_end_watch`, `m5_end_minimized`

Actuels :

> Fin Maya J5 — Maya devient témoin/radar léger : elle voit la trace, sans tout savoir.

> Fin Maya J5 — le joueur minimise ; la trace sociale reste visible et moins maîtrisée.

Problème : textes de fin système acceptables si non visibles au joueur ; si affichés, trop méta.

Direction : si ces fins sont visibles, les réécrire en narration plus incarnée. Si non visibles, moins prioritaire.

Propositions visibles :

> Maya n’a pas tout compris. Mais elle a vu assez pour ne plus regarder pareil.

> Tu minimises. Maya sourit, mais elle garde le détail en tête.

---

### 7. Inès J4 — trop “preuve/mensonge” pour une voix flottante

Fichier : `narrative/t094_ines_j4_complete.json`  
Nodes : `i4_001`, `i4_005_a`, `i4_015`, `i4_016`, `i4_018_a`, `i4_020`

Actuels :

> Je crois que je viens de tomber sur un de tes mensonges innocents.

> Un mensonge qui garde encore une bonne posture. Le tien n’est pas mal, mais il penche un peu.

> Je ne te demande rien de compromettant. Juste une micro-preuve que je n’ai pas inventé ton air pressé.

Problème : Inès devrait être plus hésitante, moins catégorique. Elle nomme trop directement `mensonge` et `preuve`.

Propositions :

> Je crois que je viens de tomber sur une version un peu arrangée de toi.

> Elle tient debout, ta version. Elle penche juste un peu quand on la regarde de côté.

> Je ne te demande rien de compromettant. Juste un signe que je n’ai pas inventé ton air pressé.

---

### 8. Nico J4 — ligne trop méta malgré bon ton

Fichier : `narrative/t095_nico_j4_complete.json`  
Node : `n4_006`

Actuel :

> Je peux couvrir un retard, pas une double vie entière. Enfin, je peux essayer, mais après je deviens un personnage secondaire dans tes mensonges et ça ne me va pas.

Problème : drôle et utile, mais `double vie entière` + `personnage secondaire` casse un peu l’immersion.

Proposition :

> Je peux couvrir un retard, pas devenir ton standard téléphonique. À un moment je vais finir par oublier quelle version je suis censé raconter.

---

### 9. Nico J4 — explication trop morale

Fichier : `narrative/t095_nico_j4_complete.json`  
Node : `n4_023_b`

Actuel :

> Trop tard pour le risque zéro, mais pas trop tard pour arrêter de distribuer des rôles aux gens sans leur demander.

Problème : idée juste, mais phrase trop dissertation. Nico doit rester oral.

Proposition :

> Trop tard pour le zéro embrouille. Mais évite de filer des rôles aux gens sans les prévenir, quand même.

---

### 10. Sarah J2/J5 — présence/absence à concrétiser

Fichiers :

- `narrative/t062_sarah_j2_complete.json`, node `s2_019_c`
- `narrative/t107_sarah_j5_complete.json`, nodes `s5_007`, `s5_008_c`

Actuels :

> Je n’essaye pas de gagner un débat. J’essaye de ne pas me sentir bête de demander ta présence.

> Je ne veux pas qu’on transforme chaque absence en problème.

Problème : moins grave que les autres, mais `présence/absence` peut rester conceptuel. Sarah gagne quand elle part d’un détail quotidien.

Propositions :

> Je n’essaye pas de gagner un débat. J’aimerais juste ne pas me sentir idiote d’attendre ton message.

> Je ne veux pas qu’un soir où je rentre tard devienne forcément un sujet.

## Voix par personnage — diagnostic

### Sarah

État : la voix est la plus proche du naturel. Elle a déjà un bon socle domestique/tendre.

À renforcer :

- plus de détails maison ;
- moins de `présence/absence` abstraits ;
- davantage de phrases simples qui ne cherchent pas à formuler le thème.

Priorité T118 : légère.

### Camille

État : voix forte, magnétique, mais parfois trop écrite. Elle utilise beaucoup de concepts affectifs.

À renforcer :

- remplacer `trace/coût/dette` par images concrètes ;
- garder ses silences et détours ;
- ajouter quelques moments de complicité non dramatique : musique, marche, lieu, blague sèche.

Priorité T118 : forte.

### Maya

État : bonne énergie sociale, piquante, mais parfois trop analytique.

À renforcer :

- faire parler Maya par détails publics concrets ;
- garder `je note`, `je pose ça là`, mais éviter d’expliquer le thème ;
- moins de `trace/incohérence`, plus de “j’ai vu X / quelqu’un a dit Y”.

Priorité T118 : moyenne.

### Nico

État : très utile pour respirations et humour. Certaines lignes sont excellentes, mais il a parfois des phrases trop conscientes de l’intrigue.

À renforcer :

- oralité ;
- vannes courtes ;
- limite amicale dite simplement ;
- moins de phrases méta.

Priorité T118 : moyenne.

### Inès

État : bon potentiel de perturbation douce, mais elle est parfois trop frontale pour son rôle.

À renforcer :

- hésitation ;
- rareté ;
- messages qui semblent presque effacés ;
- remplacer `preuve/mensonge/disponibilité` par signe, version, impression, détail.

Priorité T118 : forte pour J4 et avant retour J6.

## Choix joueur — diagnostic

Plusieurs choix restent trop mécaniques dans leur fonction dramatique :

- “je ne veux pas créer une trace” ;
- “je risque…” ;
- “je ne suis pas disponible…” ;
- “je sais que je crée une dette…” ;
- “je ne veux pas qu’on transforme chaque absence…”

Direction T118 : transformer davantage les choix en **tons de réponse** :

- rassurer maladroitement ;
- faire une blague ;
- donner un détail concret ;
- esquiver sans employer le mot esquive ;
- ouvrir une porte sans promettre ;
- poser une limite humaine plutôt qu’un choix méta.

Exemple :

Au lieu de :

> Je ne veux pas créer une trace de plus.

Préférer :

> J’ai pas envie de passer ma soirée à surveiller mon téléphone.

## Blocs/titres internes

Plusieurs nodes de type bloc portent volontairement des noms très conceptuels :

- `C3C — Trace émotionnelle`
- `C4B — Camille : proposition plus coûteuse`
- `M4B — Maya : pression par observation / micro-trace`
- `M4C — Maya : couverture fragile / dette sociale`
- `C5B — Camille : preuve de courage / vérité partielle`
- `C5C — Camille : dette affective / conséquence J6`
- `M5A — Maya : trace visible / témoin social léger`

Si ces nodes sont visibles au joueur, il faut les polisher.  
Si ces nodes servent uniquement d’organisation interne/système, priorité basse.

Décision recommandée T118 : vérifier si les `block_*` messages sont affichés dans le fil. S’ils apparaissent, les remplacer par des transitions naturelles ou invisibles.

## Recommandations T118

T118 doit être un polish ciblé, pas une réécriture totale.

Priorité 1 — Corriger les lignes les plus conceptuelles :

- Camille J4/J5 : trace/coût/dette.
- Inès J4 : preuve/mensonge/disponibilité.
- Maya J5 : incohérence/trace.
- Nico J4 : double vie/personnage secondaire.

Priorité 2 — Ajouter respirations sans pression :

- Sarah : quotidien maison.
- Camille : musique/lieu/marche.
- Maya : détail social drôle.
- Nico : vanne + bouffe/soirée/meme textuel.
- Inès : pensée nocturne ou message hésité.

Priorité 3 — Préserver structure technique :

- conserver autant que possible IDs, branches, effets ;
- ne pas changer le schéma T003 ;
- ne pas changer `conversation_blocks.json` ;
- valider duplicate/missing/unreachable et source/copie après patch.

## Validation T117

T117 est un audit uniquement.

Modifications autorisées :

- création du présent fichier produit ;
- mise à jour roadmap locale ;
- mise à jour bloc Discord local.

Modifications interdites dans T117 :

- patch JSON dialogues ;
- modification Godot ;
- modification `conversation_blocks.json` ;
- modification schéma T003 ;
- modification save/runtime/UX.

Résultat : audit prêt pour T118 — Polish naturel + respirations J1→J5.
