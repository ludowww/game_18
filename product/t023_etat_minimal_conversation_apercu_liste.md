# T023 — État minimal conversation + aperçu liste

Statut : DONE

## Résultat

Ajout d’un état runtime minimal pour Camille J1.

Flow attendu :

**Je quitte Camille → je reviens → je retrouve l’état courant.**

La liste affiche maintenant un aperçu utile basé sur le dernier message connu ou un texte `Nouveau message — ...`.

## Fichiers créés / modifiés

### Créé

- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_state.gd`

### Modifiés

- `/opt/data/profiles/game_18/product/godot_t004_prototype/project.godot`
- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_list.gd`
- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

## Implémentation MVP

### Runtime state en mémoire

Ajout d’un autoload Godot :

```ini
[autoload]
ConversationState="*res://scripts/conversation_state.gd"
```

Cet état reste en mémoire pendant l’exécution du prototype.

Pas de sauvegarde disque.

### Données mémorisées

Pour Camille J1 :

- messages déjà affichés ;
- état minimal `game_state` ;
- node suivant à jouer ;
- node de choix actif ;
- choix déjà effectués ;
- dernier aperçu texte ;
- badge simple `Nouveau message` si le dernier message vient de Camille.

### Retour dans Camille

Au retour dans `conversation_screen.gd` :

- les messages déjà affichés sont restaurés ;
- le choix actif est réaffiché si on avait quitté sur un choix ;
- sinon le prototype reprend depuis le prochain node connu ;
- si la conversation est terminée, elle reste dans son état terminé.

### Aperçu liste

`conversation_list.gd` affiche maintenant :

```gdscript
ConversationState.camille_preview_text()
```

Donc la ligne Camille montre :

- `Démarrer Camille J1` si rien n’a commencé ;
- le dernier message connu ;
- ou `Nouveau message — ...` si un message Camille est arrivé depuis l’ouverture.

## Hors-scope respecté

Non ajouté :

- vraie sauvegarde persistante ;
- historique multi-jours complet ;
- notifications dynamiques avancées ;
- système lu/non-lu complet ;
- contacts complets ;
- contenu narratif nouveau.

## JSON Camille J1

Aucune modification du JSON T003 ni du contenu Camille J1.

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

À vérifier côté Ludo sur Godot 4.6 : quitter Camille pendant un choix / après un message / en fin de conversation, puis revenir depuis la liste.
