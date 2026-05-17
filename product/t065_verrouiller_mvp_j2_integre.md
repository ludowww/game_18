# T065 — Verrouiller MVP J2 intégré

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Figer **J2 intégré** comme tranche MVP validée avant d’ajouter J3, de nouveaux contacts ou de nouveaux systèmes.

Ce verrouillage est documentaire : **aucun changement JSON, code, gameplay ou UX** n’est introduit par T065.

## Socle J2 verrouillé

### Camille J2

Camille J2 est intégrée au prototype :

- fichier : `product/godot_t004_prototype/data/camille_j2_complete.json` ;
- conversation runtime : `camille_j2` ;
- jour : `2` ;
- contact : `camille` ;
- statut : disponible à `current_day = 2`.

Validation statique :

- 45 nodes ;
- 5 choice nodes ;
- 3 end nodes ;
- 0 duplicate ID ;
- 0 lien cassé.

### Sarah J2

Sarah J2 est intégrée au prototype :

- fichier : `product/godot_t004_prototype/data/sarah_j2_complete.json` ;
- conversation runtime : `sarah_j2` ;
- jour : `2` ;
- contact : `sarah` ;
- statut : disponible à `current_day = 2`.

Validation statique :

- 45 nodes ;
- 5 choice nodes ;
- 3 end nodes ;
- 0 duplicate ID ;
- 0 lien cassé.

## Blocs J2 verrouillés

### Camille J2

- `camille_c2a` — C2A : reprise après 23:42 ;
- `camille_c2b` — C2B : proposition ambiguë ;
- `camille_c2c` — C2C : point de bascule J2.

### Sarah J2

- `sarah_s2a` — S2A : matin après malaise ;
- `sarah_s2b` — S2B : demande de présence ;
- `sarah_s2c` — S2C : doute formulé doucement.

Statuts runtime conservés :

- `locked` ;
- `available` ;
- `active` ;
- `done`.

## Unlocks J2 verrouillés

Rythme J2 validé :

```text
C2A → S2A → C2B → S2B → C2C → S2C
```

Règle :

- fin de bloc = attente claire ;
- bloc suivant débloqué ;
- notification posée uniquement si un bloc est réellement disponible ;
- pas de notification décorative.

## Sauvegarde

La sauvegarde est verrouillée en :

```gdscript
SAVE_VERSION = 4
```

Elle conserve :

- `current_day` ;
- `completed_days` ;
- `conversation_blocks` J1 + J2 ;
- messages affichés ;
- choix ;
- previews ;
- badges `has_new` ;
- `dynamic_notifications_fired`.

Compatibilité :

- anciennes saves J1 compatibles ;
- anciennes saves sans blocs J2 reçoivent les blocs par défaut ;
- J1 reste visible en historique ;
- pas de reset forcé.

## Compatibilité J1 / J2

J1 reste disponible comme historique :

- `camille` ;
- `sarah`.

J2 apparaît à `current_day = 2` :

- `camille_j2` ;
- `sarah_j2`.

La progression J1 n’est pas effacée par J2.

## Validations runtime côté Ludo

Pour ce verrouillage, la chaîne est considérée validée côté runtime après T064 :

- passage vers J2 ;
- affichage Camille J2 / Sarah J2 ;
- alternance blocs J2 ;
- unlocks croisés ;
- notifications liées aux blocs ;
- sauvegarde / reprise de `conversation_blocks` ;
- J1 conservé en historique.

Note : Godot CLI est absent côté agent, donc la validation runtime locale reste portée par Ludo sur Godot 4.6.

## Chaîne T060 → T064 validée

- **T060 — Cadrage narratif et technique J2** : validé.
- **T061 — Écrire Camille J2 complet** : validé.
- **T062 — Écrire Sarah J2 complet** : validé.
- **T063 — Intégrer J2 dans le prototype** : validé.
- **T064 — Playtest runtime J2 blocs/unlocks/sauvegarde** : validé côté Ludo pour verrouillage.

## Limites connues verrouillées

- pas de J3 ;
- frontières de blocs encore hardcodées côté Godot ;
- pas d’outil d’édition de blocs ;
- pas de calendrier complexe ;
- pas de vraie horloge ;
- pas de scheduler ;
- pas de notifications OS ;
- pas de nouveaux contacts ;
- pas de médias/images ;
- pas de migration du schéma JSON T003.

## Non-changements T065

- Aucun changement JSON.
- Aucun changement code.
- Aucun changement gameplay.
- Aucun changement UX.
- Aucun dialogue modifié.

## Validation statique T065

- Camille J1 : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Camille J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Marqueurs code confirmés : `SAVE_VERSION = 4`, blocs J1/J2, `conversation_blocks`, compatibilité saves, conversations J2 à `current_day = 2`.

## Décision

Le MVP **J1 + J2 intégré** est verrouillé comme tranche stable.

Prochaine évolution recommandée : cadrer la suite avant d’écrire J3 ou d’ajouter de nouveaux systèmes.
