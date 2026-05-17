# T128 — Patch voix Maya/Nico/Inès J4→J6

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : patch texte ciblé fort sur Maya/Nico/Inès, sans modification structurelle ni runtime

## Objectif

Appliquer la deuxième passe de refonte voix issue de T126A/T126B sur les contacts secondaires :

- **Maya** : social, piquant, détails publics, groupe/photo/story.
- **Nico** : ami oral, humour, bouffe, limite d’alibi.
- **Inès** : rareté, trajet, nuit, message hésité, porte latérale.

Le patch vise des voix plus reconnaissables immédiatement, sans changer la logique narrative ni technique.

## Fichiers modifiés

### Maya

Sources :

- `narrative/t093_maya_j4_complete.json`
- `narrative/t109_maya_j5_complete.json`
- `narrative/t121_maya_j6_complete.json`

Copies Godot synchronisées :

- `product/godot_t004_prototype/data/maya_j4_complete.json`
- `product/godot_t004_prototype/data/maya_j5_complete.json`
- `product/godot_t004_prototype/data/maya_j6_complete.json`

### Nico

Sources :

- `narrative/t095_nico_j4_complete.json`
- `narrative/t109_nico_j5_complete.json`
- `narrative/t121_nico_j6_complete.json`

Copies Godot synchronisées :

- `product/godot_t004_prototype/data/nico_j4_complete.json`
- `product/godot_t004_prototype/data/nico_j5_complete.json`
- `product/godot_t004_prototype/data/nico_j6_complete.json`

### Inès

Sources :

- `narrative/t094_ines_j4_complete.json`
- `narrative/t121_ines_j6_complete.json`
- `narrative/t122_finales_mvp_complete.json`

Copies Godot synchronisées :

- `product/godot_t004_prototype/data/ines_j4_complete.json`
- `product/godot_t004_prototype/data/ines_j6_complete.json`
- `product/godot_t004_prototype/data/finales_mvp_complete.json`

## Résumé des patchs

53 remplacements de texte visible au total :

- Maya : 18 remplacements ;
- Nico : 18 remplacements ;
- Inès : 12 remplacements ;
- Finale : 5 micro-ajustements sur retombées Nico/Maya/Inès.

Aucun changement de structure : IDs, `next`, choices, effects, flags et schéma T003 conservés.

---

# Maya — social/piquant/détails publics

## Axes renforcés

- photo de groupe ;
- épaule floue ;
- story mal cadrée ;
- groupe qui regarde la porte ;
- “je pose ça là” ;
- visage neutre / neutralité ratée ;
- social drôle mais pas omniscient.

Maya devient moins “analyse de l’intrigue” et plus “commentatrice sociale mordante qui a vu un détail public”.

## Exemples avant/après

J4 `m4_001` :

Avant :
> Je viens de comprendre un truc : tu es devenu très fort pour être “pas loin” sans être vraiment là.

Après :
> Je pose ça là : sur la photo de groupe, tu es techniquement “pas là”, mais ton épaule fait une carrière solo.

J5 `m5_002` :

Avant :
> Rassure-moi : tu n’es pas devenu une sorte d’événement local ?

Après :
> Rassure-moi : tu n’es pas devenu une sorte d’événement local ? Parce que j’ai pas prévu de faire l’accueil presse.

J6 `m6_003` :

Avant :
> Je précise : je n’ai pas un mur avec des fils rouges chez moi. J’ai juste des yeux et un dimanche trop calme.

Après :
> Je précise : je n’ai pas un mur avec des fils rouges chez moi. J’ai juste des yeux, un dimanche trop calme, et une story mal cadrée.

---

# Nico — oralité/humour/limite

## Axes renforcés

- sandwich ;
- frites ;
- sauce sur les doigts ;
- résumé de match ;
- franchise d’excuses claquées ;
- justificatif EDF ;
- standard de crise ;
- Google Traduction du chaos.

Nico gagne davantage de sas comique avant de poser sa limite. Il reste loyal, mais moins fonctionnel et moins “outil d’alibi”.

## Exemples avant/après

J4 `n4_001` :

Avant :
> Question simple : tu es en train de gérer ta journée ou de la perdre avec panache ?

Après :
> Question simple : tu es en train de gérer ta journée ou de la perdre avec panache ? Je pose mon sandwich pour suivre, c’est dire.

J5 `n5_005_b` :

Avant :
> Occupé à quoi ? Respirer avec mystère ? Il faut au moins une excuse qui porte des chaussures, sinon ça ne marche pas.

Après :
> Occupé à quoi ? Respirer avec mystère ? Ton excuse a besoin de chaussures et d’un justificatif EDF, sinon ça ne marche pas.

J6 `n6_007` :

Avant :
> Maya m’a écrit “il fait quoi exactement ?” avec trois points. Trois points, frérot. Elle a sorti la ponctuation de guerre.

Après :
> Maya m’a écrit “il fait quoi exactement ?” avec trois points. Trois points, frérot. Elle a sorti la ponctuation de guerre et moi j’avais de la sauce sur les doigts.

---

# Inès — rareté/hésitation/trajet/nuit

## Axes renforcés

- message écrit puis effacé ;
- trajet ;
- bus / arrêt ;
- reflet/vitrine de nuit ;
- ticket froissé ;
- seuil ;
- réponse plus tard ;
- porte latérale douce, pas romance bonus.

Inès devient plus flottante et mémorable par peu de détails, sans grossir son rôle.

## Exemples avant/après

J4 `i4_001` :

Avant :
> Je crois que je viens de tomber sur une version un peu arrangée de toi.

Après :
> J’ai hésité avant d’envoyer. Du coup j’envoie avant de re-hésiter : je crois que je viens de tomber sur une version un peu arrangée de toi.

J4 `i4_005_b` :

Avant :
> Près d’un passage où les gens pressés regardent leurs chaussures. Toi, tu regardais ton écran comme s’il contenait une issue de secours.

Après :
> Près d’un passage où les gens pressés regardent leurs chaussures. Le bus a raté mon arrêt, ou moi le sien, et toi tu regardais ton écran comme s’il contenait une sortie.

J6 `i6_002` :

Avant :
> Celle-ci est la moins étrange. Je crois.

Après :
> Celle-ci est la moins étrange. Je crois. Oublie si c’est déjà trop.

---

# Finale — micro-ajustements retombées

La finale a reçu 5 micro-ajustements pour harmoniser les retombées sociales :

- Nico devient plus personnel : “pas un plan claqué”, “Google Traduction du chaos”.
- Maya devient plus sociale : “PowerPoint de ton épaule”, “visage neutre demande des congés”.
- Inès reste une porte douce : “pas grave si tu réponds plus tard. Peut-être même mieux.”

## Contraintes respectées

Non modifié :

- `conversation_blocks.json`
- scripts Godot
- runtime/save/UX
- schéma T003
- IDs de nodes
- IDs de choices
- `next`
- effects/gauges/flags
- `conversation_id`, `day`, `contact_id`

## Validation

Validation locale :

- 20 dialogues actifs J1→J6/finale parsés ;
- `schema_version = 0.1` ;
- aucun ID dupliqué ;
- aucun `next` ou choice target manquant ;
- tous les nodes atteignables depuis `start_node` ;
- effects valides : flags string arrays, gauges entiers ;
- SHA source/copie Godot identiques.

Tests directs exécutés avec succès :

```txt
tests/test_t124_j6_fins_integration.py OK
tests/test_t125_j6_second_block_quick_switch.py OK
tests/test_t112_j5_integration.py OK
tests/test_t097_j4_integration.py OK
tests/test_t090_dialogue_block_validator.py OK
tests/test_t078_j3_integration.py OK
tests/test_t063_j2_integration.py OK
```

`pytest` reste absent sur la machine, donc exécution directe `python3`.

## Limites

- Patch volontairement limité à Maya/Nico/Inès + 5 retombées finale.
- Pas de nouvelle branche, pas de nouveau système, pas de modification runtime.
- Les respirations transversales plus larges restent à traiter dans T129.

## Recommandation Roadmap

Prochaine étape : **T129 — Respirations sans pression transversales**.
