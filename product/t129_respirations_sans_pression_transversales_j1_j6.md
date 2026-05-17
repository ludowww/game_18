# T129 — Respirations sans pression transversales J1→J6

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : patch texte transversal, sans modification structurelle ni runtime

## Objectif

Ajouter une passe de **respirations sans pression** après les patchs voix T127/T128.

But : le joueur doit parfois répondre pour créer de la complicité, de l’humour ou une texture de vie, pas seulement pour choisir entre aveu/mensonge/esquive.

## Fichiers modifiés

17 JSON source ont été patchés et synchronisés avec leur copie Godot data :

### Sarah

- `narrative/t037_sarah_j1_complete.json`
- `narrative/t062_sarah_j2_complete.json`
- `narrative/t107_sarah_j5_complete.json`
- `narrative/t120_sarah_j6_complete.json`

### Camille

- `narrative/t007_camille_j1_complete.json`
- `narrative/t061_camille_j2_complete.json`
- `narrative/t075_camille_j3_complete.json`
- `narrative/t120_camille_j6_complete.json`

### Maya

- `narrative/t093_maya_j4_complete.json`
- `narrative/t109_maya_j5_complete.json`
- `narrative/t121_maya_j6_complete.json`

### Nico

- `narrative/t095_nico_j4_complete.json`
- `narrative/t109_nico_j5_complete.json`
- `narrative/t121_nico_j6_complete.json`

### Inès

- `narrative/t094_ines_j4_complete.json`
- `narrative/t121_ines_j6_complete.json`

### Finale

- `narrative/t122_finales_mvp_complete.json`

Copies Godot data correspondantes synchronisées sous `product/godot_t004_prototype/data/`.

## Volume de patch

56 remplacements de texte visible au total.

Remarque : certains choix joueur existent à la fois comme `choice.text` et comme message `player` de confirmation ; ces remplacements comptent donc double quand le même texte visible apparaît aux deux endroits.

Aucun changement de structure : IDs, `next`, choices, effects, flags et schéma T003 conservés.

---

# Respirations par contact

## Sarah — tendresse pratique / maison

Respirations ajoutées ou renforcées :

- boire le café avec Sarah deux minutes ;
- répondre par un vrai message plutôt qu’une défense ;
- commencer avec une phrase qui tient dans la cuisine ;
- reconnaître qu’un mug et une assiette peuvent dire quelque chose ;
- prévenir même par un détail minuscule : “je mets mes chaussures”.

### Exemple avant/après

J1 choix `s1_003_a` :

Avant :
> Désolé, je suis parti tôt. Je voulais pas te réveiller.

Après :
> Désolé, je suis parti tôt. J’aurais dû boire le café avec toi deux minutes.

J6 choix `s6_025_b` :

Avant :
> Je t’écris dès que je pars. Pas une minute floue de plus.

Après :
> Je t’écris dès que je pars. Pas une minute floue de plus, même si c’est juste “je mets mes chaussures”.

## Camille — jeu calme / sous-entendu / café

Respirations ajoutées ou renforcées :

- répondre avant le deuxième café ;
- admettre qu’un café est agaçant parce qu’il rappelle Camille ;
- choisir la table du fond plutôt que “chercher les problèmes” ;
- écouter seulement les vingt premières secondes d’un morceau ;
- répondre à Camille comme à quelqu’un de réel, pas comme à une issue.

### Exemple avant/après

J2 choix `c2_003_a` :

Avant :
> Moi aussi j’y ai repensé.

Après :
> Moi aussi j’y ai repensé. Surtout au café, et c’est agaçant.

J3 choix `c3_007_a` :

Avant :
> Mieux pour qui ?

Après :
> Mieux pour qui ? Pour toi, pour moi, ou pour le café qui nous supporte ?

## Maya — humour social sans tribunal

Respirations ajoutées ou renforcées :

- autodérision sur le timing catastrophique ;
- demander “la scène version Maya, sans tribunal” ;
- “épaule superstar” ;
- calmer le groupe avec une vanne moche ;
- éviter de transformer Maya en vigile.

### Exemple avant/après

J5 choix `m5_003_b` :

Avant :
> Qu’est-ce que tu as vu exactement ?

Après :
> Raconte-moi la scène, version Maya, sans tribunal.

J6 choix `m6_008_b` :

Avant :
> Si tu peux calmer le groupe sans mentir, fais-le.

Après :
> Si tu peux calmer le groupe avec une vanne moche, je prends.

## Nico — pote avant outil

Respirations ajoutées ou renforcées :

- poser le sandwich ;
- manger les frites tranquille ;
- problèmes de sauces ;
- “version pote, pas conférence TED” ;
- hotline émotionnelle refusée avec humour.

### Exemple avant/après

J4 choix `n4_003_a` :

Avant :
> Tu dramatises pour un “je crois”.

Après :
> Tu dramatises pour un “je crois”, ou je dois vraiment poser mon sandwich ?

J5 choix `n5_007_b` :

Avant :
> Je ne veux pas te mettre là-dedans.

Après :
> Je ne veux pas te mettre là-dedans. T’as déjà assez de problèmes avec tes sauces.

## Inès — douceur étrange / espace

Respirations ajoutées ou renforcées :

- remarquer les gens dans les trajets ;
- réagir sans fermer la porte trop fort ;
- reconnaître qu’un message arrive doucement ;
- ne pas ouvrir une autre porte, même calme ;
- laisser la possibilité de répondre plus tard.

### Exemple avant/après

J4 choix `i4_007_a` :

Avant :
> Tu es toujours aussi attentive aux inconnus ?

Après :
> Tu remarques toujours les gens dans les trajets comme ça ?

J6 choix `i6_004_a` :

Avant :
> C’est bizarre, mais je suis content que tu écrives.

Après :
> C’est bizarre, mais ton message arrive doucement. Ça me fait du bien.

## Finale — respiration discrète

La finale reçoit deux micro-ajustements :

- un détail social léger autour d’une photo de dessert moche ;
- une route “équilibre maintenu” formulée moins mécaniquement, avec l’image des verres à ne pas faire tomber.

---

# Contraintes respectées

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

# Validation

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

# Limites

- Patch transversal volontairement limité à des micro-ajustements lisibles.
- Pas de nouvelle branche ni de nouveaux nodes.
- Pas de modification runtime.
- T129 améliore la respiration du run mais ne remplace pas une relecture globale finale.

# Recommandation Roadmap

Prochaine étape : **T130 — Validation cohérence finale voix/personnages + copies Godot**.
