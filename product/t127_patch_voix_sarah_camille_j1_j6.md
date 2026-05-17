# T127 — Patch voix Sarah/Camille J1→J6

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : patch texte ciblé fort sur Sarah/Camille, sans modification structurelle ni runtime

## Objectif

Appliquer la première passe de refonte voix issue de T126A/T126B sur les deux axes émotionnels principaux :

- **Sarah** : maison, routine, confiance abîmée, chaleur fatiguée.
- **Camille** : lieux, musique, silences, lucidité oblique, trouble magnétique.

Le patch vise un ressenti plus identifiable en jeu sans modifier les branches ni la logique.

## Fichiers modifiés

### Sarah

Sources :

- `narrative/t037_sarah_j1_complete.json`
- `narrative/t062_sarah_j2_complete.json`
- `narrative/t107_sarah_j5_complete.json`
- `narrative/t120_sarah_j6_complete.json`

Copies Godot synchronisées :

- `product/godot_t004_prototype/data/sarah_j1_complete.json`
- `product/godot_t004_prototype/data/sarah_j2_complete.json`
- `product/godot_t004_prototype/data/sarah_j5_complete.json`
- `product/godot_t004_prototype/data/sarah_j6_complete.json`

### Camille

Sources :

- `narrative/t007_camille_j1_complete.json`
- `narrative/t075_camille_j3_complete.json`
- `narrative/t092_camille_j4_complete.json`
- `narrative/t120_camille_j6_complete.json`

Copies Godot synchronisées :

- `product/godot_t004_prototype/data/camille_j1_complete.json`
- `product/godot_t004_prototype/data/camille_j3_complete.json`
- `product/godot_t004_prototype/data/camille_j4_complete.json`
- `product/godot_t004_prototype/data/camille_j6_complete.json`

## Résumé des patchs

Chaque conversation ciblée a reçu environ 6 remplacements de texte visible, sans changer IDs, `next`, choices, effects, flags, day/contact/conversation IDs.

### Sarah — refonte ressentie

Axes ajoutés/renforcés :

- café froid ;
- clés ;
- chargeur côté canapé ;
- épisode commencé sans le joueur ;
- pull/canapé ;
- lumière cuisine ;
- assiette/frigo/courses ;
- téléphone écran vers le haut.

Sarah devient plus domestique et intime avant de devenir douloureuse.

#### Exemples avant/après

J1 `s1_002` :

Avant :
> J’ai laissé ton café sur le plan de travail. Il doit être froid maintenant.

Après :
> J’ai laissé ton café sur le plan de travail. Il doit être froid maintenant. J’ai même remis ta clé sous le bol, comme une personne très organisée et pas du tout inquiète.

J2 `s2_002` :

Avant :
> Je ne te reproche rien. Je me suis juste réveillée avec l’impression qu’on avait laissé une phrase en suspens hier.

Après :
> Je ne te reproche rien. J’ai lancé l’épisode sans toi hier. J’ai tenu huit minutes, exploit. Après j’ai surtout eu l’impression qu’on avait laissé une phrase en suspens.

J5 `s5_001` :

Avant :
> Je sais que tu as beaucoup de choses en ce moment. Je ne veux pas ajouter du bruit.

Après :
> J’ai laissé la petite lumière de la cuisine. Je sais pas pourquoi. Ça faisait moins vide.

J6 `s6_011` :

Avant :
> J’ai gardé une assiette hier. Puis je l’ai mise au frigo. Puis je l’ai jetée ce matin. Ça m’a énervée d’être triste pour une assiette.

Après :
> J’ai gardé une assiette hier. Puis je l’ai mise au frigo. Puis je l’ai jetée ce matin, entre le café et les courses. Ça m’a énervée d’être triste pour une assiette.

### Camille — refonte ressentie

Axes ajoutés/renforcés :

- café du coin ;
- morceau trop dramatique ;
- serviette en papier ;
- silence bien habillé ;
- marche/vitrines/pluie ;
- téléphone retourné ;
- table du fond / table bancale ;
- regard vers la porte ;
- café trop fort.

Camille devient plus située, moins abstraite : elle parle par lieux, musique, objets et silences.

#### Exemples avant/après

J1 `c1_001` :

Avant :
> Alors… tu fais toujours semblant d’être sérieux le matin ?

Après :
> Alors… tu fais toujours semblant d’être sérieux le matin ? Le café du coin passe un morceau beaucoup trop dramatique pour 9h, ça aide peut-être.

J3 `c3_001` :

Avant :
> Je me demandais si aujourd’hui tu allais faire comme si hier n’avait pas existé.

Après :
> Je marche depuis dix minutes. Même rue, mêmes vitrines. Je me demandais si aujourd’hui tu allais faire comme si hier n’avait pas existé.

J4 `c4_001` :

Avant :
> Je viens de passer devant un endroit où on ne se croise jamais par hasard.

Après :
> Je viens de passer devant le café aux tables bancales. Celui où on ne se croise jamais par hasard.

J6 `c6_001` :

Avant :
> J’ai remis le même morceau qu’hier.

Après :
> J’ai remis le même morceau qu’hier. Le café du fond l’a adopté, mauvaise nouvelle pour moi.

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

- Patch volontairement limité à Sarah/Camille.
- Pas de nouvelle branche, pas de nouveau système, pas de modification runtime.
- Maya/Nico/Inès restent à traiter dans T128.
- Les respirations transversales plus larges restent à traiter dans T129.

## Recommandation Roadmap

Prochaine étape : **T128 — Patch voix Maya/Nico/Inès J4→J6**.
