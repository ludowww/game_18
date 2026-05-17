# T050 — Cadrage système minimal Jours

Thread : Scope MVP / technique + Roadmap  
Statut : DONE  
Date : 2026-05-15

## Objectif

Définir le fonctionnement minimal du passage **J1 → J2** avant d’écrire Camille/Sarah J2.

Ce ticket est un cadrage : **aucun changement JSON, gameplay, UX ou code Godot n’est appliqué ici**.

## Décision MVP

Le MVP utilise un système de jours très simple :

- un état global `current_day` indique le jour actif ;
- les conversations sont rattachées à un jour via leur `day` JSON et/ou leur configuration Godot ;
- J1 reste lisible après passage à J2 ;
- J2 apparaît uniquement quand J1 est terminé ;
- le passage de jour est déclenché par le jeu, pas par une horloge réelle.

## Règle de passage J1 → J2

### Règle principale

Le joueur peut passer à J2 quand toutes les conversations obligatoires de J1 sont terminées.

Pour le socle actuel :

```text
J1 terminé si :
- Camille J1 est done ;
- Sarah J1 est done ;
- aucun choix bloquant J1 n’est encore actif.
```

### Déclenchement MVP recommandé

Quand ces conditions sont vraies :

1. l’écran Messages peut afficher une action discrète du type `Passer au J2` ;
2. au clic, le jeu met `current_day = 2` ;
3. les conversations J2 deviennent disponibles ;
4. la sauvegarde est mise à jour.

Alternative acceptable pour le prototype : passage automatique après fin de la dernière conversation J1 obligatoire.  
Décision recommandée : **bouton/action explicite**, car plus lisible pour playtest et debug.

## État global minimal

Ajouter plus tard dans l’autoload `ConversationState` ou équivalent :

```gdscript
var current_day: int = 1
var completed_days: Array[int] = []
```

Option utile mais non obligatoire :

```gdscript
var day_transition_available: bool = false
```

Rôle :

- `current_day` filtre ce qui est actif dans Messages ;
- `completed_days` évite de rejouer une transition déjà faite ;
- l’état reste global, pas stocké dans les JSON narratifs.

## Conditions de fin J1

Pour le MVP, une conversation J1 est considérée finie quand son état runtime a :

```text
done = true
```

J1 est considéré fini quand :

```text
required_conversations_by_day[1] = ["camille", "sarah"]
```

et que chaque conversation requise est `done`.

Règle importante : une conversation avec un choix actif non résolu ne doit pas compter comme terminée.

## Apparition des conversations J2

### Recommandation technique simple

Conserver une liste de conversations configurée côté Godot, avec disponibilité par jour :

```gdscript
"camille_j2": {
  "contact_id": "camille",
  "display_name": "Camille",
  "title": "J2 — Camille",
  "json_path": "res://data/camille_j2.json",
  "day": 2,
  "available_from_day": 2
}
```

Même principe pour Sarah :

```gdscript
"sarah_j2": {
  "contact_id": "sarah",
  "display_name": "Sarah",
  "title": "J2 — Sarah",
  "json_path": "res://data/sarah_j2.json",
  "day": 2,
  "available_from_day": 2
}
```

La liste Messages affiche :

- les conversations du jour courant ;
- les conversations passées déjà commencées/terminées, si on veut garder l’historique visible.

## Ce qui reste visible de J1

Après passage à J2 :

- Camille J1 reste consultable ;
- Sarah J1 reste consultable ;
- leurs messages affichés restent dans la sauvegarde ;
- leurs previews peuvent rester comme dernier message réel ou être marquées discrètement comme terminées ;
- aucun reset automatique de J1 ;
- aucun replay forcé de J1.

Décision MVP : **J1 reste visible en lecture / historique**, mais ne doit pas bloquer l’apparition de J2 une fois validé.

## Impact sur sauvegarde

La sauvegarde T043 devra être étendue plus tard avec :

```json
{
  "current_day": 2,
  "completed_days": [1]
}
```

À conserver :

- états séparés par conversation ;
- messages affichés ;
- `done` ;
- choix ;
- previews ;
- badges `has_new` ;
- `dynamic_notifications_fired`.

Compatibilité :

- si une ancienne sauvegarde n’a pas `current_day`, valeur par défaut = `1` ;
- si une ancienne sauvegarde n’a pas `completed_days`, valeur par défaut = `[]` ;
- ne pas casser les saves T043 existantes.

## Hors-scope clair

Explicitement hors-scope pour le MVP :

- pas de calendrier complexe ;
- pas d’horloge réelle ;
- pas de système de planning lourd ;
- pas de date/heure système ;
- pas de timers multi-heures ;
- pas de notifications OS ;
- pas de scheduler global ;
- pas de simulation de semaine ;
- pas de règles avancées par personnage ;
- pas de migration du schéma JSON T003 ;
- pas de J2 écrit dans T050.

## Décision finale

Le système minimal Jours repose sur :

1. `current_day` global ;
2. conversations requises par jour ;
3. passage explicite J1 → J2 quand Camille J1 + Sarah J1 sont terminés ;
4. apparition des conversations J2 via configuration Godot ;
5. historique J1 conservé ;
6. sauvegarde étendue avec défauts compatibles.

Prochaine étape recommandée : **T051 — Implémenter current_day + passage J1 → J2 sans écrire encore les dialogues J2**.
