# T056 — Segmentation narrative J1

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Découper **Camille J1** et **Sarah J1** en blocs narratifs courts pour préparer une future mécanique de verrous / unlocks sans temps réel.

But produit : créer le rythme minimal :

```text
Camille début → attente → Sarah → notification Camille → attente → Sarah/Camille → fin J1
```

Sans :

- temps réel ;
- sans scheduler ;
- horloge système ;
- calendrier complexe ;
- modification JSON immédiate.

## Décision MVP

On ne joue plus forcément chaque conversation J1 de bout en bout librement.

Le rythme J1 doit devenir :

1. un bloc Camille est disponible ;
2. Camille se verrouille narrativement ;
3. Sarah devient pertinente ;
4. une notification Camille rouvre Camille ;
5. Camille / Sarah alternent par blocs ;
6. le J1 se termine quand les blocs requis sont finis.

Les verrous sont **narratifs**, pas temporels réels.

## Segmentation proposée — Camille J1

### Camille J1 — Bloc C1A — Accroche / tentation légère

Entrée : début J1.  
Nodes concernés :

- `c1_001` ;
- `c1_002` ;
- branches de réponse `c1_003_*` / `c1_004_*` ;
- si silence : `c1_005_ignore_choice` puis résolution courte ;
- convergence vers `c1_005` / `c1_006`.

Fonction :

- poser Camille ;
- tester ton joueur ;
- donner une première micro-dose de flirt ;
- créer une attente.

Sortie de bloc :

```text
lock Camille
unlock Sarah bloc S1A
```

### Camille J1 — Bloc C1B — Relance / café / montée du risque

Déclencheur : après Sarah S1A, via notification Camille.  
Nodes concernés :

- `c1_010` ;
- `c1_011` ;
- suites jusqu’à `c1_015`.

Fonction :

- reprendre Camille après un détour Sarah ;
- faire sentir que le téléphone revient réclamer l’attention ;
- augmenter risque / intérêt.

Sortie de bloc :

```text
lock Camille
unlock Sarah bloc S1B
```

### Camille J1 — Bloc C1C — Café / cliffhanger J1

Déclencheur : après Sarah S1B ou fin de boucle J1.  
Nodes concernés :

- `c1_020` ;
- `c1_021` ;
- fins `c1_end_go` / `c1_end_resist` / `c1_end_seen`.

Fonction :

- poser le choix de limite / bascule ;
- terminer l’arc Camille J1 ;
- alimenter les conséquences J2.

Sortie de bloc :

```text
Camille J1 done
```

## Segmentation proposée — Sarah J1

### Sarah J1 — Bloc S1A — Domestique / manque du matin

Déclencheur : Camille C1A verrouillé.  
Nodes concernés :

- `s1_001` ;
- `s1_002` ;
- `s1_003` ;
- branches `s1_004_*` / `s1_005_*` ;
- `s1_006` ;
- `s1_007`.

Fonction :

- ramener le joueur au foyer ;
- contraster Sarah avec Camille ;
- introduire le téléphone comme objet suspect.

Sortie de bloc :

```text
lock Sarah
unlock Camille bloc C1B
notification Camille
```

### Sarah J1 — Bloc S1B — Engagement / soirée / malaise doux

Déclencheur : Camille C1B verrouillé.  
Nodes concernés :

- `s1_011` ;
- suites jusqu’à `s1_017`.

Fonction :

- poser une promesse domestique ;
- mettre en conflit le désir de Camille et l’attachement Sarah ;
- préparer le cliffhanger Sarah.

Sortie de bloc :

```text
lock Sarah
unlock Camille bloc C1C ou Sarah bloc S1C selon ordre retenu
```

### Sarah J1 — Bloc S1C — Question / cliffhanger J1

Déclencheur : fin de boucle J1.  
Nodes concernés :

- `s1_020` ;
- `s1_021` si présent dans le flux ;
- `s1_022` ;
- fins `s1_end_deny` / `s1_end_delay` / `s1_end_confess_hint`.

Fonction :

- transformer le soupçon en question ;
- finir Sarah J1 ;
- préparer J2.

Sortie de bloc :

```text
Sarah J1 done
```

## Rythme J1 recommandé

Ordre MVP recommandé :

```text
1. Camille C1A disponible au lancement
2. Camille C1A terminé → Camille locked, Sarah S1A unlocked
3. Sarah S1A terminé → Sarah locked, notification Camille, Camille C1B unlocked
4. Camille C1B terminé → Camille locked, Sarah S1B unlocked
5. Sarah S1B terminé → Sarah locked, Camille C1C unlocked
6. Camille C1C terminé → Camille J1 done, Sarah S1C unlocked
7. Sarah S1C terminé → Sarah J1 done
8. Si Camille J1 done + Sarah J1 done → passage J2 disponible
```

Ce rythme crée la boucle :

```text
j’attends → je vais voir ailleurs → ça revient
```

sans temps réel.

## États / unlocks minimaux proposés

À implémenter plus tard côté Godot, pas dans T056 :

```gdscript
var conversation_blocks := {
  "camille_c1a": {"conversation": "camille", "status": "available"},
  "sarah_s1a": {"conversation": "sarah", "status": "locked"}
}
```

Statuts possibles :

- `locked` : pas encore disponible ;
- `available` : bloc ouvrable ;
- `active` : bloc en cours ;
- `done` : bloc terminé.

Un bloc terminé peut déclencher :

```text
unlock_block(next_block_id)
mark_conversation_new(contact, preview_neutre)
lock_current_block()
```

## Ce qui reste visible

Même si une conversation est locked :

- les messages déjà lus restent visibles ;
- la conversation reste dans Messages ;
- le joueur comprend qu’il attend une réponse ;
- le lock doit être narratif : `En attente d’un nouveau message`, pas punitif.

## Règle produit

Une notification ne doit plus simplement décorer.

Elle doit correspondre à :

```text
un bloc réellement unlocké,
pertinent,
ouvrable maintenant.
```

## Hors-scope T056

- pas d’écriture Camille J2 ;
- pas d’écriture Sarah J2 ;
- pas de modification JSON J1 ;
- pas de refactor Godot immédiat ;
- pas de scheduler ;
- pas d’horloge réelle ;
- pas de calendrier complexe ;
- pas de temps d’attente en minutes/heures ;
- pas de système avancé de priorité d’événements.

## Décision finale

J1 doit être découpé en **3 blocs Camille** et **3 blocs Sarah** pour créer une alternance contrôlée.

T056 ne modifie pas le prototype : il définit le découpage et la logique produit.  
La prochaine étape technique doit implémenter ces verrous narratifs de blocs sans toucher au contenu J1.
