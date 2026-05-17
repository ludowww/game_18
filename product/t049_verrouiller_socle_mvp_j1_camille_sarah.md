# T049 — Verrouiller socle MVP J1 Camille/Sarah

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Figer l’état actuel comme **socle MVP J1 validé** avant d’ajouter du J2, de nouveaux contacts ou des systèmes plus complexes.

Ce verrouillage est documentaire : **aucun changement JSON, gameplay, code ou UX** n’est introduit par T049.

## Socle validé

### Contenus J1

- **Camille J1 complet** intégré au prototype.
  - Fichier prototype : `product/godot_t004_prototype/data/camille_j1_complete.json`
  - Validation statique : 45 nodes, 6 choice nodes, 3 end nodes, aucun duplicate ID, aucun lien cassé.
- **Sarah J1 complet** intégré au prototype.
  - Fichier prototype : `product/godot_t004_prototype/data/sarah_j1_complete.json`
  - Validation statique : 41 nodes, 5 choice nodes, 3 end nodes, aucun duplicate ID, aucun lien cassé.

### Prototype MVP

Le socle technique actuel comprend :

- écran **Messages** minimal ;
- navigation **liste Messages → conversation → retour Messages** ;
- conversations Camille / Sarah actives ;
- états séparés par conversation ;
- progression conversation conservée ;
- choix joueur cliquables ;
- branches simples fonctionnelles ;
- previews Messages par conversation ;
- badges `nouveau` ;
- sauvegarde locale minimale via `user://double_vie_save.json` ;
- bouton debug discret `Reset` ;
- notifications dynamiques simples hardcodées côté Godot ;
- previews de notifications neutres : `Nouveau message de Sarah` / `Nouveau message de Camille`.

## Chaîne T043 → T048 validée

- **T043 — Sauvegarde persistante minimale** : validé comme socle local MVP.
- **T044 / T046 / T048 — checkpoints runtime/playtest autour sauvegarde + notifications** : considérés validés pour le verrouillage du socle J1.
- **T045 — Notifications dynamiques simples** : validé comme système prototype hardcodé léger.
- **T047 — Clarifier previews notifications dynamiques** : validé avec previews neutres, sans phrases de dialogue inventées.

Décision : la tranche **J1 Camille/Sarah + Messages + sauvegarde + previews + badges + notifications dynamiques simples** est verrouillée comme base MVP avant extension J2.

## Limites connues verrouillées

Explicitement hors-scope à ce stade :

- pas de notifications OS ;
- pas de temps réel ;
- pas de scheduler ;
- notifications dynamiques encore hardcodées côté Godot ;
- pas encore de J2 ;
- pas encore de vraie gestion calendrier / jours ;
- pas de système complet de contacts ;
- pas de compte/cloud ;
- pas de média/images dans ce verrouillage ;
- pas de migration du schéma JSON ;
- pas de nouvel événement complexe.

## Non-changements T049

- Aucun changement JSON.
- Aucun changement gameplay.
- Aucun changement UX.
- Aucun changement de contenu narratif.
- Aucun changement de code Godot.

## Validation statique T049

- Camille JSON : OK — 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah JSON : OK — 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Marqueurs code confirmés : sauvegarde, previews, badges `has_new`, notifications dynamiques, anti-doublon `dynamic_notifications_fired`, previews neutres.
- Godot CLI absent ici : runtime local non relancé côté agent.

## Décision

Le socle MVP J1 Camille/Sarah est **figé**.  
La prochaine évolution doit être une nouvelle tranche explicite, probablement **J2** ou cadrage calendrier/jours, sans modifier rétroactivement le socle J1 sauf bug bloquant.
