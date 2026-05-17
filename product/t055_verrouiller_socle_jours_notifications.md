# T055 — Verrouiller socle Jours + notifications

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Figer le socle après validation du passage **J1 → J2** et des notifications dynamiques sécurisées.

Ce verrouillage est documentaire : **aucun changement JSON, gameplay, UX ou code Godot** n’est introduit par T055.

## Socle verrouillé

### Jours

Le prototype contient désormais un état global minimal :

```gdscript
var current_day: int = 1
var completed_days: Array = []
```

Rôle :

- `current_day` indique le jour actif ;
- `completed_days` conserve les jours déjà validés ;
- la sauvegarde conserve ces champs avec compatibilité anciennes saves.

### Passage J1 → J2

Règle MVP verrouillée :

```text
J1 terminé si Camille J1 + Sarah J1 sont done,
sans choix actif bloquant.
```

Quand J1 est terminé :

- l’écran Messages affiche `Passer au Jour 2` ;
- le clic ajoute J1 à `completed_days` ;
- `current_day` passe à `2` ;
- l’état est sauvegardé ;
- J1 reste visible en historique.

### Conversations J2 à venir

Deux entrées techniques existent déjà côté Godot :

- `camille_j2` ;
- `sarah_j2`.

Elles sont :

- rattachées au Jour 2 ;
- visibles après passage J2 ;
- affichées comme à venir ;
- non cliquables ;
- sans contenu JSON écrit pour l’instant.

### Notifications dynamiques sécurisées

Le système conserve :

- triggers hardcodés T045 ;
- previews neutres T047 ;
- anti-doublon `dynamic_notifications_fired` ;
- sauvegarde compatible ;
- badges `has_new`.

Sécurité T053 verrouillée : une notification dynamique ne se déclenche pas si :

- la conversation cible est déjà `done` ;
- `current_day > 1` pour les triggers J1 actuels ;
- la cible n’est pas disponible ;
- la cible est absente ;
- la cible est déjà ouverte.

Règle produit :

> Une notification dynamique doit seulement dire : il y a vraiment quelque chose de pertinent à ouvrir maintenant.

## Chaîne T050 → T054 validée

- **T050 — Cadrage système minimal Jours** : validé.
- **T051 — Implémenter current_day + passage J1→J2** : validé comme socle technique.
- **T052 — Playtest runtime passage J1→J2 + persistance current_day** : considéré validé pour verrouillage.
- **T053 — Sécuriser notifications dynamiques selon état conversation/jour** : validé.
- **T054 — Playtest runtime anti-notifications fantômes J1/J2** : considéré validé pour verrouillage.

## Note Roadmap — limite actuelle des notifications

Limite importante : **les notifications n’ont pas encore de temporalité réelle**.

Aujourd’hui :

- les notifications apparaissent à certains nodes ;
- le joueur peut switcher librement entre Camille et Sarah ;
- chaque conversation peut être jouée de bout en bout ;
- il n’y a pas encore de vraie attente ;
- les conversations ne se bloquent pas et ne se répondent pas vraiment dans le temps ;
- les notifications restent donc surtout décoratives.

Diagnostic produit : le système actuel valide bien :

- multi-conversation ;
- badges ;
- previews ;
- sauvegarde ;
- passage J1 → J2.

Mais il ne valide pas encore le cœur addictif :

> “J’attends un message, je vais voir ailleurs, puis ça revient.”

Pour valider ce cœur, il faudra introduire plus tard une mécanique de **verrous temporels narratifs**, sans temps réel complexe.

## Limites connues verrouillées

- J2 non écrit ;
- pas de calendrier complexe ;
- pas d’horloge réelle ;
- pas de scheduler ;
- pas de planning lourd ;
- notifications encore hardcodées ;
- notifications encore décoratives tant qu’il n’y a pas de verrous temporels narratifs ;
- pas de système de contacts complet ;
- pas de notifications OS ;
- pas de cloud / compte ;
- aucun changement de schéma JSON T003.

## Non-changements T055

- Aucun changement JSON.
- Aucun changement gameplay.
- Aucun changement UX.
- Aucun changement code Godot.
- Aucun dialogue J2 ajouté.

## Validation statique T055

- Camille J1 JSON : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 JSON : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Marqueurs code confirmés : `current_day`, `completed_days`, passage J1→J2, entrées J2 à venir, sauvegarde compatible, `dynamic_notifications_fired`, previews neutres, gardes anti-notifications fantômes.
- Godot CLI absent ici : runtime local non relancé côté agent.

## Décision

Le socle **Jours + notifications sécurisées** est verrouillé.

La prochaine évolution produit ne doit pas être un calendrier complexe, mais un cadrage MVP de **verrous temporels narratifs** pour créer la boucle : attendre → aller voir ailleurs → recevoir un retour.
