# T082 — Verrouiller MVP J3 intégré

Statut : DONE  
Thread : Scope MVP / technique  
Date : 2026-05-15

## Objectif

Figer J3 intégré comme tranche MVP validée avant J4 ou nouveaux systèmes.

Ce ticket est un verrouillage documentaire/status. Il ne modifie pas le prototype, les JSON narratifs, le gameplay, la sauvegarde ou l'UX.

## Périmètre verrouillé

### Contenus J3

- Camille J3 complet produit et intégré comme `camille_j3`.
- Sarah J3 complet produit et intégré comme `sarah_j3`.
- Schéma narratif T003 conservé (`schema_version: 0.1`).
- Aucun changement de dialogue dans ce verrouillage.

### Blocs J3

Les blocs J3 sont externalisés dans :

`product/godot_t004_prototype/data/conversation_blocks.json`

Rythme validé :

```text
C3A → S3A → C3B → S3B → C3C → S3C
```

Blocs verrouillés :

- `camille_c3a`
- `sarah_s3a`
- `camille_c3b`
- `sarah_s3b`
- `camille_c3c`
- `sarah_s3c`

Les unlocks, badges et previews J3 restent pilotés par la configuration de blocs, sans migration du schéma JSON de dialogue.

### Passage de jour

Le bouton de passage de jour est verrouillé après correctif T080 :

- Jour 1 → `Passer au Jour 2`
- Jour 2 → `Passer au Jour 3`
- libellé calculé via `ConversationState.current_day + 1`
- tooltip générique : `Passer au jour suivant`

### Sauvegarde et historique

Verrouillé en l'état :

- J1 et J2 restent visibles comme historique après progression.
- La progression J3 s'inscrit dans le système de sauvegarde existant.
- Les blocs, badges/previews et notifications restent compatibles avec les sauvegardes existantes.
- Aucun changement de `SAVE_VERSION` dans T082.

## Validations actées

À marquer validés dans la Roadmap :

- T075 — Camille J3 complet produit.
- T076 — Sarah J3 complet produit.
- T077 — cohérence J3 Camille/Sarah validée.
- T078 — J3 intégré au prototype via `conversation_blocks.json`.
- T079 — playtest runtime J3 avec retour bouton.
- T080 — correctif bouton passage de jour dynamique.
- T081 — runtime J3 validé côté Ludo après correctif.

Validation runtime T081 actée côté Ludo :

- passage J2 → J3 vérifié après T080 ;
- J3 visible/disponible ;
- alternance J3 validée ;
- badges/previews J3 validés ;
- sauvegarde/reload au milieu de J3 validés ;
- J1/J2 restent visibles en historique ;
- pas de notification fantôme bloquante signalée.

## Non-changements T082

T082 ne change pas :

- les JSON narratifs ;
- le schéma T003 ;
- `conversation_blocks.json` ;
- les scripts Godot ;
- le gameplay ;
- l'UX ;
- la sauvegarde ;
- les notifications.

## Limites connues MVP

Restent hors-scope / non verrouillés :

- pas de J4 ;
- frontières/config blocs encore manuelles ;
- pas d'éditeur de blocs ;
- pas de calendrier complexe ;
- pas de vraie horloge ;
- pas de scheduler ;
- pas de notifications OS ;
- pas de système de contacts complet ;
- pas de médias/images dans ce verrouillage.

## Décision

MVP J3 intégré verrouillé.

La base jouable couvre maintenant :

- J1 complet Camille/Sarah ;
- J2 complet Camille/Sarah ;
- J3 complet Camille/Sarah ;
- progression de jour J1 → J2 → J3 ;
- blocs narratifs externalisés ;
- alternance contrôlée par blocs ;
- badges/previews ;
- sauvegarde locale ;
- historique J1/J2 ;
- bouton de passage de jour dynamique.

## Next step recommandé

Décider la suite Roadmap avant d'implémenter :

- soit **cadrage J4** ;
- soit **polish UX / lisibilité / rythme** sur le MVP J1-J3 ;
- soit **outil de production blocs/dialogues** pour réduire le manuel avant expansion.
