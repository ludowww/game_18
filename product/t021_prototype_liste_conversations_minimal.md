# T021 — Prototype liste de conversations minimal

Statut : DONE

## Résultat

Ajout d’un écran minimal de liste de conversations avant l’entrée dans le chat.

Flow MVP obtenu :

**Liste conversations → Camille → Chat → Retour liste**

## Fichiers modifiés / créés

### Créés

- `/opt/data/profiles/game_18/product/godot_t004_prototype/scenes/conversation_list.tscn`
- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_list.gd`

### Modifiés

- `/opt/data/profiles/game_18/product/godot_t004_prototype/project.godot`
- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

## Détail implémentation

### Écran liste conversations

Nouvelle scène principale :

```ini
run/main_scene="res://scenes/conversation_list.tscn"
```

L’écran affiche :

- titre `Messages` ;
- sous-titre prototype ;
- une entrée conversation : `Camille` ;
- indication que la structure pourra accueillir Sarah / autres contacts plus tard.

### Clic Camille → chat existant

L’entrée Camille appelle :

```gdscript
get_tree().change_scene_to_file("res://scenes/conversation_screen.tscn")
```

La conversation existante reste branchée sur :

```gdscript
const JSON_PATH := "res://data/camille_j1_complete.json"
```

### Retour chat → liste

Le chevron retour du header conversation est devenu un bouton :

```gdscript
get_tree().change_scene_to_file("res://scenes/conversation_list.tscn")
```

## Structure prête pour plus tard

La liste est volontairement simple, mais prête à ajouter ensuite :

- Sarah ;
- autres contacts ;
- autres conversations ;
- autres scènes JSON.

Sans système de contacts complet pour l’instant.

## Hors-scope respecté

Non ajouté :

- contacts complets ;
- avatars avancés ;
- historique multi-jours ;
- notifications dynamiques ;
- système de statut complexe ;
- sauvegarde ;
- nouveau contenu narratif.

## JSON Camille J1

Aucune modification du JSON Camille J1.

Hash inchangé :

`fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Validation statique :

- 45 nodes
- 6 choice_nodes
- 3 end_nodes
- aucun duplicate_id
- aucun missing_next_target

## Runtime Godot

Godot CLI absent localement : validation runtime impossible ici.

À vérifier côté Ludo : navigation liste → Camille → retour liste dans Godot 4.6.
