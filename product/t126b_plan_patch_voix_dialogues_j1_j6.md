# T126B — Préparer refonte voix dialogues J1→J6 / patch ciblé fort

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : plan de patch dialogue uniquement, sans modification JSON/Godot

## Objectif

Préparer la refonte de voix en jeu après le retour runtime : le run fonctionne, mais les personnages doivent devenir plus reconnaissables dans la messagerie minute par minute.

T126B ne patche rien. Il transforme T126A en plan opérationnel : où intervenir, dans quel ordre, avec quel niveau de risque, et comment découper les tickets suivants sans réécriture dangereuse.

## Sources utilisées

- T126A : `product/t126a_refonte_identite_personnages_bible_jouable.md`
- T116 : `product/t116_bible_personnages_voix_messagerie.md`
- Dialogues actifs J1→J6 + finale : `narrative/*.json`
- Copies Godot data correspondantes : `product/godot_t004_prototype/data/*.json`

## Décision de méthode

Le patch suivant doit être **fort en ressenti**, mais **faible en risque technique** :

- patch texte uniquement ;
- préserver IDs, `next`, choices, flags, gauges, `conversation_id`, `day`, `contact_id`, schéma T003 ;
- synchroniser chaque JSON source modifié avec sa copie Godot data ;
- ne pas toucher `conversation_blocks.json`, scripts Godot, save/runtime/UX ;
- valider parse, duplicate IDs, missing targets, reachability, effects, SHA source/copie.

Ratio cible par bloc patché :

- 50 % lignes de texture / respiration ;
- 30 % pression douce ;
- 20 % pression forte.

Le but n’est pas d’ajouter de longues scènes : il faut remplacer ou injecter quelques lignes très visibles, surtout au début des conversations et avant les choix clés.

---

# Plan par contact

## Sarah — maison, routine, confiance abîmée

### Fichiers prioritaires

| Priorité | Fichier source | Copie Godot | Scènes/nodes à viser | Type de refonte | Risque technique |
|---:|---|---|---|---|---|
| P0 | `narrative/t037_sarah_j1_complete.json` | `data/sarah_j1_complete.json` | `s1_001`, `s1_002`, `s1_006`, premiers choix | Renforcer histoire commune dès l’ouverture : café, départ, au revoir, objet vu sans accusation | Faible si remplacement texte uniquement |
| P0 | `narrative/t062_sarah_j2_complete.json` | `data/sarah_j2_complete.json` | `s2_001`, `s2_002`, `s2_006`, `s2_019_c` | Plus de routine concrète : assiette, canapé, film commencé, message attendu | Faible |
| P1 | `narrative/t107_sarah_j5_complete.json` | `data/sarah_j5_complete.json` | `s5_001`, `s5_002`, `s5_006`, blocs B/C | Remplacer fatigue abstraite par gestes domestiques, attente du message, lumière cuisine | Faible |
| P1 | `narrative/t120_sarah_j6_complete.json` | `data/sarah_j6_complete.json` | `s6_001`→`s6_011`, endings Sarah | Déjà fort ; ajouter juste 1–2 rappels récurrents J1/J2 pour boucler mug/assiette/film | Faible |
| P2 | `narrative/t122_finales_mvp_complete.json` | `data/finales_mvp_complete.json` | route `final_repair_*`, `final_fracture_*` | Harmoniser avec objets récurrents créés en J1/J2 | Faible |

### Intention de patch

Sarah doit être attachante avant d’être douloureuse. Le joueur doit sentir qu’il existe déjà une maison : café froid, assiette, film, chargeur, clé, lumière cuisine.

### Exemples d’injections ciblées

- J1 après `s1_002` : “J’ai aussi trouvé ta clé sous le coussin. Classique toi.”
- J2 autour `s2_002` : “J’ai lancé l’épisode sans toi hier. J’ai tenu huit minutes, exploit.”
- J5 autour `s5_001` : “J’ai laissé la petite lumière de la cuisine. Ça faisait moins vide.”

---

## Camille — lieux, musique, silences, lucidité oblique

### Fichiers prioritaires

| Priorité | Fichier source | Copie Godot | Scènes/nodes à viser | Type de refonte | Risque technique |
|---:|---|---|---|---|---|
| P0 | `narrative/t007_camille_j1_complete.json` | `data/camille_j1_complete.json` | `c1_001`, `c1_004_*`, `c1_007_*` | Première apparition plus spécifique : café, morceau, remarque oblique, silence choisi | Faible |
| P0 | `narrative/t075_camille_j3_complete.json` | `data/camille_j3_complete.json` | `c3_001`, `c3_002`, `c3_006`, bloc C | Ajouter musique/lieu avant la tension ; rendre le “fil” plus sensoriel | Faible |
| P1 | `narrative/t092_camille_j4_complete.json` | `data/camille_j4_complete.json` | `c4_001`→`c4_006`, choix de fenêtre | Déjà mieux après T118 ; renforcer lieu précis, téléphone retourné, regard vers porte | Faible |
| P1 | `narrative/t120_camille_j6_complete.json` | `data/camille_j6_complete.json` | `c6_001`→`c6_012`, route C6B | Déjà fort ; relier au motif musique/café dès J1/J3 | Faible |
| P2 | `narrative/t122_finales_mvp_complete.json` | `data/finales_mvp_complete.json` | route `final_camille_*` | Vérifier que Camille ne devient pas récompense automatique | Faible |

### Intention de patch

Camille doit être reconnaissable par ce qu’elle remarque : le café, la rue, un morceau, une phrase trop prudente, un silence qui dit plus qu’un aveu.

### Exemples d’injections ciblées

- J1 : “Le café du coin passe un morceau beaucoup trop dramatique pour 9h.”
- J3 : “Je marche un peu. C’est plus simple que d’attendre un message.”
- J4 : “Tu regardes déjà la porte dans ta tête, non ?”

---

## Maya — social, piquant, détails publics

### Fichiers prioritaires

| Priorité | Fichier source | Copie Godot | Scènes/nodes à viser | Type de refonte | Risque technique |
|---:|---|---|---|---|---|
| P0 | `narrative/t093_maya_j4_complete.json` | `data/maya_j4_complete.json` | `m4_001`→`m4_006`, `m4_018_c` | Première apparition plus sociale : groupe, story, phrase entendue ; réduire ton “analyse” | Faible |
| P0 | `narrative/t109_maya_j5_complete.json` | `data/maya_j5_complete.json` | `m5_001`→`m5_006`, `m5_011`, `m5_015` | Ajouter 1 respiration piquante sans conséquence ; montrer qu’elle suppose, pas qu’elle sait | Faible |
| P1 | `narrative/t121_maya_j6_complete.json` | `data/maya_j6_complete.json` | `m6_001`→`m6_012` | Déjà très aligné photo/groupe ; préserver, ajouter éventuellement une micro-story | Faible |
| P2 | `narrative/t122_finales_mvp_complete.json` | `data/finales_mvp_complete.json` | `final_repair_007`, `final_control_005`, `final_fracture_006` | Retombées sociales plus Maya, moins système | Faible |

### Intention de patch

Maya ne doit pas être “celle qui sait”. Elle doit être celle qui a vu un détail drôle/gênant et qui le formule vite.

### Exemples d’injections ciblées

- J4 : “Je pose ça là : ta tête sur la photo de groupe = niveau amateur.”
- J5 : “Le ‘il est où ?’ est parti trop vite. Trois têtes se sont tournées. Ambiance.”
- J6 : “Je suis pas mêlée, officiellement. Officieusement, ton épaule floue travaille contre moi.”

---

## Nico — oralité, humour, limite d’ami

### Fichiers prioritaires

| Priorité | Fichier source | Copie Godot | Scènes/nodes à viser | Type de refonte | Risque technique |
|---:|---|---|---|---|---|
| P0 | `narrative/t095_nico_j4_complete.json` | `data/nico_j4_complete.json` | `n4_001`→`n4_006`, bloc C, `n4_023_b` | Ajouter bouffe/meme/match avant limite ; remplacer morale restante par oralité | Faible |
| P0 | `narrative/t109_nico_j5_complete.json` | `data/nico_j5_complete.json` | `n5_001`→`n5_006`, `n5_015`, endings | Plus de sas comique sans pression ; garder limite claire | Faible |
| P1 | `narrative/t121_nico_j6_complete.json` | `data/nico_j6_complete.json` | `n6_001`→`n6_016` | Déjà fort ; préserver frites/service client, éventuellement renforcer amitié hors crise | Faible |
| P2 | `narrative/t122_finales_mvp_complete.json` | `data/finales_mvp_complete.json` | `final_repair_006`, `final_camille_006`, `final_fracture_005` | Retombées Nico plus personnelles, moins fonctionnelles | Faible |

### Intention de patch

Nico doit faire respirer le jeu. Une vanne doit arriver avant la phrase sérieuse. Il n’est pas un didacticiel moral ni un bouton d’alibi.

### Exemples d’injections ciblées

- J4 : “Je pose mon sandwich pour te dire ça : calme-toi.”
- J5 : “Ton excuse a besoin de chaussures et d’un justificatif EDF.”
- J6 : “Je suis ton pote, pas ton standard de crise.”

---

## Inès — rareté, hésitation, trajet, porte latérale

### Fichiers prioritaires

| Priorité | Fichier source | Copie Godot | Scènes/nodes à viser | Type de refonte | Risque technique |
|---:|---|---|---|---|---|
| P0 | `narrative/t094_ines_j4_complete.json` | `data/ines_j4_complete.json` | `i4_001`→`i4_006`, `i4_015`→`i4_020` | Rendre l’entrée moins explicative, plus trajet/vitrine/message effacé | Faible |
| P0 | `narrative/t121_ines_j6_complete.json` | `data/ines_j6_complete.json` | `i6_001`→`i6_012` | Déjà aligné ; vérifier qu’elle ne nomme pas trop son rôle de sortie/porte | Faible |
| P1 | `narrative/t122_finales_mvp_complete.json` | `data/finales_mvp_complete.json` | route `final_flight_*` | Préserver fuite comme solitude, pas romance bonus ; renforcer étrangeté douce | Faible |

### Intention de patch

Inès doit être mémorable avec peu de lignes. Elle doit donner l’impression d’un message presque effacé, pas d’une troisième romance qui réclame sa route.

### Exemples d’injections ciblées

- J4 : “J’ai hésité avant d’envoyer. Du coup j’envoie avant de re-hésiter.”
- J4/J6 : “Le bus a raté mon arrêt. Ou moi le sien.”
- Finale : “Pas grave si tu réponds plus tard. Peut-être même mieux.”

---

# Découpage recommandé

## T127 — Patch voix Sarah/Camille J1→J6

Objectif : renforcer les deux axes émotionnels principaux avant tout le reste.

Fichiers :

- Sarah : `t037`, `t062`, `t107`, `t120`, finale route Sarah.
- Camille : `t007`, `t075`, `t092`, `t120`, finale route Camille.

Livrable : JSON patchés + copies Godot + note avant/après.

Pourquoi d’abord : ce sont les deux routes principales. Si elles ne deviennent pas attachantes/spécifiques, les retombées sociales ne suffiront pas.

## T128 — Patch voix Maya/Nico/Inès J4→J6

Objectif : rendre les contacts secondaires mémorables sans les transformer en routes lourdes.

Fichiers :

- Maya : `t093`, `t109`, `t121`, finale retombées.
- Nico : `t095`, `t109`, `t121`, finale retombées.
- Inès : `t094`, `t121`, finale fuite.

Livrable : JSON patchés + copies Godot + note avant/après.

Pourquoi ensuite : ils doivent soutenir la pression finale, mais aussi donner envie d’ouvrir leurs messages.

## T129 — Respirations sans pression transversales

Objectif : ajouter ou remplacer quelques lignes de respiration partout où le run ressemble trop à un questionnaire dramatique.

Cibles :

- J1/J2 : chaleur et attachement.
- J4/J5 : nouveaux contacts pas uniquement “problèmes”.
- J6/finale : éviter le tunnel de procès.

Méthode : patch visible texte uniquement, 1 à 3 lignes par bloc max, sans branch explosion.

## T130 — Validation cohérence + intégration copies

Objectif : audit final après patchs T127/T128/T129.

Checks :

- voix reconnaissables sans nom ;
- ratio respiration/pression ;
- lexique auteur absent ou très rare ;
- JSON T003 valides ;
- copies Godot synchronisées ;
- tests directs Python si disponibles ;
- pas de modification runtime involontaire.

---

# Ordre de priorité détaillé

1. **Début J1/J2 Sarah/Camille** : première impression du jeu. Le joueur doit accrocher avant les choix lourds.
2. **Premières apparitions Maya/Nico/Inès** : chaque nouveau contact doit avoir une couleur immédiate.
3. **J5/J6 résolution** : garder la tension, mais ajouter des respirations qui montrent les gens derrière les fonctions narratives.
4. **Finale T122** : harmoniser les motifs récurrents créés par T127/T128 sans changer les routes.

# Risques et garde-fous

## Risque : patch trop vaste

Garde-fou : ne pas réécrire tous les messages. Viser les nodes de première impression, les transitions de blocs, et 1–2 lignes avant/après choix clés.

## Risque : casser la structure

Garde-fou : pas d’ajout de branches, pas de suppression de nodes, pas de changement de `next` sauf nécessité exceptionnelle. Préférer remplacer le `text` d’un node existant.

## Risque : surcharger les personnages de tics

Garde-fou : 2–3 marqueurs récurrents par contact suffisent. Les tics doivent rester naturels, pas devenir slogans.

## Risque : Inès devient trop importante

Garde-fou : ne patcher que J4/J6/finale, garder sa rareté et son ambiguïté.

# Validation attendue après futurs patchs

Pour T127/T128/T129 :

```txt
- JSON parse OK
- schema_version = 0.1
- conversation_id/day/contact_id inchangés
- aucun duplicate ID
- aucun next/choice target manquant
- tous les nodes atteignables depuis start_node
- effects valides : flags string arrays, gauges entiers
- SHA source/copie Godot identiques
- conversation_blocks.json inchangé
- scripts/runtime/save/UX inchangés
```

# Validation T126B

T126B est un plan uniquement.

Modifié :

- `product/t126b_plan_patch_voix_dialogues_j1_j6.md`
- roadmap locale / bloc 04 de suivi

Non modifié :

- aucun JSON dialogue ;
- aucune copie Godot data ;
- aucun script Godot ;
- aucun `conversation_blocks.json` ;
- aucun schéma T003 ;
- aucun save/runtime/UX.
