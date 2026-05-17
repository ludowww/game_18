# T115 — Cadrer J6 / fin MVP avant écriture

Statut : DONE
Thread : Roadmap / Narration jours

## Décision Roadmap

Après verrouillage J5, la suite retenue est **cadrage J6 / fin MVP**.

J6 doit transformer le coût visible de J5 en **résolution MVP testable** : le joueur arrive au point où il ne peut plus seulement temporiser, couvrir ou séduire. Il doit choisir ce qu’il assume, ce qu’il cache encore, et ce qu’il accepte de perdre.

Objectif : obtenir une fin courte, rejouable, lisible, sans révélation totale unique obligatoire et sans explosion de branches.

## Fonction dramatique de J6

J6 teste : **que reste-t-il quand la double vie a cessé d’être invisible ?**

J1→J3 installaient l’attention et l’alternance Sarah/Camille.  
J4 élargissait le réseau social avec Maya/Inès/Nico.  
J5 rendait les coûts visibles : absence, trace, couverture fragile, doute doux.  
J6 doit convertir ces coûts en choix final MVP.

Le joueur doit sentir :

- qu’il y a encore plusieurs sorties possibles ;
- qu’aucune sortie n’efface tout gratuitement ;
- que les flags/jauges accumulés colorent la fin ;
- que le prototype 0.1 a une vraie clôture jouable, même courte.

## Portée MVP retenue

J6 reste dans le cadre messages :

- pas d’image obligatoire ;
- pas d’appel ;
- pas de média ;
- pas de scheduler temps réel ;
- pas de nouveau schéma T003 ;
- pas de système de fins complexe séparé dans un premier temps ;
- pas de révélation totale obligatoire commune à toutes les routes ;
- pas de branche combinatoire contact × contact.

Principe : les flags/jauges orientent le ton et le choix de fin, mais J6 doit rester intégrable en blocs courts.

## Rôles contacts J6

### Sarah — vérité intime / confiance / rupture possible

Sarah porte le cœur domestique de la fin.

Rôle J6 : demander une vérité émotionnelle, pas mener une enquête.

Elle doit pouvoir mener vers :

- une réparation fragile si le joueur choisit la présence et limite le mensonge ;
- une confession partielle qui ne règle pas tout mais ouvre une suite ;
- une rupture ou distance froide si le joueur continue à esquiver ;
- une solitude finale si le joueur a trop instrumentalisé tout le monde.

À éviter : Sarah détective, accusation mécanique, procès final trop long.

### Camille — choix de courage ou retrait

Camille porte le risque affectif.

Rôle J6 : demander une position claire : être choisie, être respectée, ou se retirer.

Elle ne doit pas forcer une fin “Camille gagne” par défaut. Elle doit tester si le joueur assume une relation, reconnaît le déséquilibre, ou continue à la garder comme échappatoire.

À éviter : ultimatum brutal unique, scène de jalousie caricaturale, récompense automatique si le joueur ment bien.

### Nico — miroir social / couverture qui coûte

Nico ne résout rien.

Rôle J6 : rappeler ce que le joueur lui a demandé ou laissé entendre, et rendre visible le coût d’une couverture fragile.

Il peut :

- aider à maintenir une sortie propre si la confiance existe ;
- lâcher une phrase qui complique la situation si le joueur l’a trop impliqué ;
- refuser d’être l’alibi final.

À éviter : tutoriel moral, deus ex machina, ami qui sauve toutes les routes.

### Maya — témoin social / trace visible

Maya sert de pression externe légère.

Rôle J6 : matérialiser la trace sociale : un détail vu, une incohérence, un “je ne veux pas me mêler de ça mais…”.

Elle peut pousser vers une fin plus exposée si le joueur a minimisé les traces, ou rester en retrait si le joueur a été prudent.

À éviter : omniscience, révélation policière, rôle trop central dans la fin romantique.

### Inès — retour dosé après réserve J5

Inès revient comme perturbation contrôlée, pas comme troisième romance complète.

Rôle J6 : agir comme révélateur ou tentation de fuite. Elle rappelle qu’une autre porte existe, mais la prendre a un coût : ambiguïté, solitude, ou fuite en avant.

Elle peut être :

- un micro-bloc actif ;
- ou un déclencheur/écho dans la fin selon scope intégration.

Décision recommandée : **micro-bloc Inès J6 court**, car elle a été réservée en J5 et peut maintenant servir de révélateur final sans surcharger la journée.

À éviter : route Inès complète, nouveau triangle majeur, romance forcée.

## Structure J6 recommandée

### Version MVP recommandée — 8 blocs + fins

```txt
S6A → C6A → N6A → M6A → S6B → C6B → I6A → FIN
```

Lecture :

- `S6A` : Sarah ouvre la journée par une demande claire de présence/vérité.
- `C6A` : Camille demande une position, sans ultimatum brutal.
- `N6A` : Nico rappelle la fragilité de la couverture.
- `M6A` : Maya pose la trace sociale visible.
- `S6B` : Sarah devient le point de vérité intime.
- `C6B` : Camille force le choix affectif ou le retrait.
- `I6A` : Inès agit comme tentation/révélateur final court.
- `FIN` : bloc/choix final de résolution MVP.

### Variante plus serrée — 6 blocs

```txt
S6A → C6A → N6A/M6A → S6B → C6B → FIN
```

À utiliser seulement si la charge de contenu devient trop forte. Dans cette variante, Inès reste en écho final plutôt qu’en bloc.

### Variante plus dense — 10 blocs

Non recommandée pour le MVP 0.1. Elle risquerait de reproduire la charge J4 au moment où le prototype doit se clôturer proprement.

## Fins MVP recommandées

Objectif : **4 fins courtes** pour rester dans la promesse 3 à 5 fins.

### Fin A — Réparation fragile

Le joueur choisit Sarah / présence / vérité partielle et limite la fuite.

Résultat : Sarah ne pardonne pas tout, mais accepte une reconstruction prudente. Camille prend de la distance ou reste comme blessure non résolue.

Condition narrative indicative : confiance Sarah suffisante, mensonges non maximaux, choix final orienté présence.

### Fin B — Camille assumée

Le joueur assume Camille comme risque affectif réel et cesse de la maintenir dans l’ombre.

Résultat : Camille accepte une vérité imparfaite, mais la fin reste coûteuse : Sarah s’éloigne ou comprend qu’il y a une fracture.

Condition narrative indicative : intimité Camille haute, courage/vérité partielle activés, choix final orienté Camille.

### Fin C — Double vie maintenue / mensonge propre

Le joueur réussit à compartimenter assez pour finir sans explosion immédiate.

Résultat : personne ne sait tout, mais la dernière bulle doit montrer que le coût revient bientôt. Fin volontairement inconfortable, pas victoire parfaite.

Condition narrative indicative : couvertures Nico/Maya possibles, suspicion Sarah/Camille contenue, choix final orienté contrôle.

### Fin D — Tout se fissure

Le joueur a trop esquivé, trop impliqué Nico/Maya, trop minimisé Sarah/Camille.

Résultat : pas forcément grande scène publique, mais perte de confiance généralisée. Sarah se ferme, Camille se retire, Nico/Maya ne couvrent plus.

Condition narrative indicative : suspicion forte, flags de mensonge/trace cumulés, choix final esquive.

### Fin E — Fuite en avant / solitude

Optionnelle si l’intégration peut porter 5 fins.

Le joueur refuse de choisir et se raccroche à l’ambiguïté Inès ou au silence.

Résultat : fin plus froide, ouverte, où la double vie devient surtout évitement. Bonne fin “chaos doux” pour rejouabilité.

Condition narrative indicative : choix final fuite, Inès activée comme révélateur, liens principaux fragilisés.

Décision recommandée : intégrer **4 fins obligatoires** A-D, garder **Fin E** comme bonus si le coût d’écriture/intégration reste bas.

## Flags / jauges à exploiter sans nouveau système lourd

Réutiliser ou prolonger légèrement les effets existants :

- `sarah_trust`, `sarah_suspicion`, `sarah_distance` ;
- `camille_intimacy`, `camille_pressure`, `camille_truth_seeded` ;
- `nico_cover_possible`, `player_asked_nico_cover_j5`, `nico_knows_too_much` ;
- `maya_trace_seen_j5`, `maya_suspicion_seeded`, `player_minimized_maya_j5` ;
- `ines_reserve_j5`, `ines_ambiguity_seeded` ou équivalent léger ;
- `j5_social_pressure` ;
- un flag final simple : `j6_final_choice_sarah`, `j6_final_choice_camille`, `j6_final_choice_control`, `j6_final_choice_escape`.

Garde-fou : ne pas créer un moteur de scoring final complet avant d’avoir écrit les blocs. Les conditions peuvent rester simples et lisibles dans les dialogues/fins.

## Découpage tickets recommandé

### T116 — Écrire Sarah/Camille J6 résolution MVP

Thread : Dialogues

Créer :

- `narrative/t116_sarah_j6_complete.json`
- `product/godot_t004_prototype/data/sarah_j6_complete.json`
- `narrative/t116_camille_j6_complete.json`
- `product/godot_t004_prototype/data/camille_j6_complete.json`
- `product/t116_sarah_camille_j6_resolution.md`

Cible : Sarah 2 blocs, Camille 2 blocs, fin émotionnelle préparée mais pas encore intégration finale complexe.

### T117 — Écrire Nico/Maya/Inès J6 pression finale courte

Thread : Dialogues

Créer :

- `narrative/t117_nico_j6_complete.json`
- `product/godot_t004_prototype/data/nico_j6_complete.json`
- `narrative/t117_maya_j6_complete.json`
- `product/godot_t004_prototype/data/maya_j6_complete.json`
- `narrative/t117_ines_j6_complete.json` si micro-bloc retenu
- `product/godot_t004_prototype/data/ines_j6_complete.json` si micro-bloc retenu
- `product/t117_nico_maya_ines_j6_pression_finale.md`

Cible : blocs courts, pas de routes longues.

### T118 — Écrire fins MVP

Thread : Dialogues / Routes fins

Créer les fins textuelles/message finales sous forme intégrable T003 ou note de mapping selon décision technique.

Décision à prendre en T118 : fins comme conversation dédiée `finales_mvp_complete.json` ou fins portées par derniers nodes Sarah/Camille/Inès.

Recommandation actuelle : commencer simple avec **une conversation finale dédiée** si l’intégration T003 le permet proprement, sinon rattacher les end nodes aux dernières conversations J6.

### T119 — Relecture cohérence J6 / fins MVP

Thread : Dialogues / Roadmap

Vérifier :

- pas de révélation totale obligatoire ;
- Sarah pas détective ;
- Camille pas ultimatum brutal ;
- Nico/Maya pas omniscients/solution magique ;
- Inès révélateur dosé ;
- fins 3 à 5, lisibles, non combinatoires ;
- continuité J1→J6.

### T120 — Intégrer J6 + fins MVP dans Godot

Thread : Scope MVP / technique

Ajouter day 6, blocs J6, fins, validation J1→J6, tests et playtest runtime Ludo.

## Limites assumées

- T115 ne crée aucun JSON dialogue.
- T115 ne modifie pas Godot.
- Les fins sont cadrées narrativement, pas encore implémentées techniquement.
- Les conditions exactes de fins devront être ajustées après écriture T116–T118.
- La fin E est optionnelle pour ne pas dépasser la charge MVP.

## Décision à demander à Roadmap

Valider le découpage suivant :

1. **T116 — Écrire Sarah/Camille J6 résolution MVP**
2. **T117 — Écrire Nico/Maya/Inès J6 pression finale courte**
3. **T118 — Écrire fins MVP**
4. **T119 — Relecture cohérence J6 / fins MVP**
5. **T120 — Intégrer J6 + fins MVP dans Godot**

Décision clé : retenir **Inès micro-bloc J6** ou la garder uniquement en écho/final.

Recommandation : **Inès micro-bloc J6 court**, car J5 l’a volontairement mise en réserve et J6 doit utiliser cette tension sans ouvrir une troisième romance complète.
