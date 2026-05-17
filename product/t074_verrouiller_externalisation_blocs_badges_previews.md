# T074 — Verrouiller externalisation blocs + badges/previews

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Figer l’externalisation des blocs narratifs comme socle stable avant reprise J3.

Ce verrouillage est documentaire : **aucun changement JSON, code, gameplay ou UX** n’est introduit par T074.

## Socle verrouillé

### Source des blocs

La source des blocs narratifs est désormais :

```text
product/godot_t004_prototype/data/conversation_blocks.json
```

Cette config contient :

- blocs J1 ;
- blocs J2 ;
- ordre des blocs ;
- contact logique ;
- conversation runtime ;
- node de début ;
- nodes de fin ;
- unlock suivant ;
- cible de notification ;
- texte d’attente.

Validation config :

- 12 blocs déclarés ;
- 12 entrées dans `block_order` ;
- aucune référence cassée connue.

## Unlocks / notifications depuis config

Les unlocks ne sont plus codés comme frontières hardcodées principales dans `conversation_state.gd`.

Le runtime lit la config et utilise :

- `unlock_on_done` pour débloquer le bloc suivant ;
- `notification_target` pour savoir quelle conversation notifier ;
- `waiting_text` pour afficher l’état d’attente.

Règle verrouillée :

```text
notification = bloc réellement débloqué + conversation pertinente à ouvrir maintenant
```

## Badges / previews

Le comportement attendu est verrouillé :

- `has_new = true` quand un bloc pertinent devient disponible ;
- preview neutre : `Nouveau message de Camille` / `Nouveau message de Sarah` ;
- ouverture d’une conversation = badge de cette conversation seulement effacé ;
- dernier vrai message non écrasé si le joueur a déjà commencé un bloc.

## Réparation saves existantes — T072

T072 ajoute :

```gdscript
repair_available_block_notifications()
```

Cette réparation est appelée :

- après chargement de sauvegarde ;
- au refresh de l’écran Messages.

Elle restaure les badges/previews des blocs `available` non ouverts pour les saves existantes après externalisation.

Elle évite :

- conversation déjà `done` ;
- conversation courante ;
- conversation indisponible ;
- bloc déjà commencé.

## Sauvegarde

La sauvegarde reste en :

```gdscript
SAVE_VERSION = 4
```

Champs conservés :

- `current_day` ;
- `completed_days` ;
- `conversation_blocks` ;
- messages affichés ;
- choix ;
- previews ;
- badges `has_new` ;
- `dynamic_notifications_fired`.

Compatibilité :

- saves avant externalisation compatibles ;
- saves existantes réparées sans reset ;
- pas de migration destructrice ;
- J1/J2 restent lisibles.

## Chaîne validée

- **T068 — Externaliser les blocs narratifs dans une config** : validé.
- **T069 — Playtest runtime non-régression après externalisation** : validé avec réserve corrigée ensuite.
- **T070 — Corriger badges/previews après externalisation des blocs** : validé.
- **T071 — Correctif runtime badge nouveau après unlock bloc** : validé.
- **T072 — Réparer badges/previews pour saves existantes après externalisation** : validé.
- **T073 — Playtest runtime badges/previews sur save existante** : validé côté Ludo.

## Validations runtime T073

T073 valide côté Ludo :

- badges `nouveau` restaurés ;
- previews visibles ;
- comportement OK sur save existante sans reset ;
- externalisation des blocs conservée ;
- pas de régression J1/J2 signalée.

## Validation statique T074

- Config blocs : 12 blocs, 12 entrées d’ordre.
- Camille J1 : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Camille J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J2 : 45 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Marqueurs code confirmés : lecture `conversation_blocks.json`, repair T072, sauvegarde `conversation_blocks`, unlocks/notifications via config.

Godot CLI absent ici : runtime local non relancé côté agent.

## Limites connues

- pas encore d’éditeur de blocs ;
- config manuelle ;
- J3 pas encore intégré ;
- pas de calendrier complexe ;
- pas de vraie horloge ;
- pas de scheduler ;
- pas de notifications OS.

## Non-changements T074

- Aucun changement JSON dialogue.
- Aucun changement code runtime.
- Aucun changement gameplay.
- Aucun changement UX.
- Aucun contenu J3 ajouté.

## Décision

L’externalisation des blocs + badges/previews est verrouillée comme socle stable.

La reprise J3 peut partir de cette base, en ajoutant les futurs blocs dans `conversation_blocks.json` plutôt que dans le code.
