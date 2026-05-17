# T059 — Verrouiller rythme narratif J1 segmenté

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Figer le fonctionnement actuel comme **rythme MVP J1 validé** avant d’écrire J2.

Ce verrouillage est documentaire : **aucun changement JSON, code, gameplay ou UX** n’est introduit par T059.

## Socle verrouillé

Le J1 n’est plus pensé comme deux conversations jouables librement de bout en bout.

Le rythme MVP retenu est :

```text
Camille début → attente → Sarah → notification Camille → alternance contrôlée → fin J1
```

But produit : valider la boucle addictive minimale :

```text
j’attends un message → je vais voir ailleurs → ça revient
```

sans temps réel complexe.

## Blocs Camille/Sarah J1

### Camille

- `camille_c1a` — accroche / tentation légère ;
- `camille_c1b` — relance / café / montée du risque ;
- `camille_c1c` — café / cliffhanger J1.

### Sarah

- `sarah_s1a` — domestique / manque du matin ;
- `sarah_s1b` — engagement / soirée / malaise doux ;
- `sarah_s1c` — question / cliffhanger J1.

## Statuts runtime verrouillés

Chaque bloc utilise un statut simple :

- `locked` : bloc non disponible ;
- `available` : bloc ouvrable ;
- `active` : bloc en cours ;
- `done` : bloc terminé.

Décision : ces statuts suffisent pour le MVP. Pas de système de planning plus lourd.

## Règles d’unlock croisé

Ordre MVP verrouillé :

```text
camille_c1a → sarah_s1a
sarah_s1a → camille_c1b
camille_c1b → sarah_s1b
sarah_s1b → camille_c1c
camille_c1c → sarah_s1c
sarah_s1c → fin J1 complète
```

Règle : quand un bloc se termine, la conversation courante se met en attente et le bloc suivant de l’autre conversation devient disponible.

## États d’attente

États d’attente validés pour le MVP :

- `Plus rien pour le moment` ;
- `Camille ne répond plus pour l’instant` ;
- `Sarah ne répond plus pour l’instant`.

Règle UX : l’attente doit être claire mais légère. Le joueur doit comprendre qu’il y a autre chose à ouvrir, pas qu’il est bloqué par un bug.

## Notifications liées aux blocs

Les notifications ne sont plus seulement décoratives.

Règle verrouillée :

```text
notification = bloc réellement débloqué + conversation pertinente à ouvrir maintenant
```

Conséquences :

- pas de badge si le bloc cible n’est pas disponible ;
- pas de badge si la conversation cible est `done` ;
- pas de badge si la conversation cible n’est pas disponible ;
- pas de badge J1 si `current_day > 1` ;
- previews neutres conservées : `Nouveau message de Sarah` / `Nouveau message de Camille`.

## Sauvegarde

L’état des blocs est persisté via :

```json
{
  "conversation_blocks": {
    "camille_c1a": { "status": "done" },
    "sarah_s1a": { "status": "available" }
  }
}
```

Compatibilité :

- anciennes saves sans `conversation_blocks` migrées avec défauts ;
- messages, choix, previews, `has_new`, `current_day`, `completed_days`, `dynamic_notifications_fired` conservés ;
- aucun reset forcé de progression existante.

## Chaîne T056 → T058 validée

- **T056 — Segmentation narrative J1** : blocs Camille/Sarah définis, rythme MVP posé.
- **T057 — Implémenter verrous narratifs de blocs J1** : blocs runtime, attente, unlocks croisés, notifications liées aux blocs et sauvegarde ajoutés.
- **T058 — Playtest runtime alternance blocs J1** : considéré validé pour ce verrouillage.

## Limites connues verrouillées

- frontières de blocs encore hardcodées côté Godot ;
- pas d’outil d’édition de blocs ;
- pas de J2 ;
- pas de scheduler ;
- pas de temps réel ;
- pas d’horloge système ;
- pas de calendrier complexe ;
- pas de système avancé de priorités d’événements ;
- pas de migration du schéma JSON T003.

## Non-changements T059

- Aucun changement JSON.
- Aucun changement code.
- Aucun changement UX.
- Aucun changement gameplay.
- Aucun contenu J2 ajouté.

## Validation statique T059

- Camille J1 JSON : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 JSON : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Marqueurs code confirmés : `CONVERSATION_BLOCKS`, statuts `locked/available/active/done`, unlock croisé, états d’attente, notifications liées aux blocs, `conversation_blocks` sauvegardé.
- Godot CLI absent ici : runtime local non relancé côté agent.

## Décision

Le rythme narratif J1 segmenté est **verrouillé comme socle MVP**.

La prochaine étape peut être l’écriture de J2 ou le cadrage de la continuité J2 à partir des conséquences J1, sans remettre en cause ce socle sauf bug bloquant.
