# T028 — Lisibilité choix longs + couleurs contacts + layout Messages

Statut : DONE

## Objectif

Corriger les problèmes UI révélés par le playtest multi-conversation, sans modifier les JSON Camille/Sarah ni le schéma T003.

## Fichiers modifiés

- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`
- `/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_list.gd`

## Choix longs

Corrections appliquées :

- texte complet visible dans les boutons ;
- retour à la ligne automatique via `Label.autowrap_mode` ;
- suppression de la dépendance au tooltip pour lire un choix ;
- hauteur de bouton adaptée à la longueur :
  - court : 46 px ;
  - moyen : 58 px ;
  - long : 74 px ;
  - très long : 92 px.

Le bouton contient maintenant un label interne en autowrap au lieu de clipper le texte du bouton.

## Zone de choix

Corrections appliquées :

- bordure légère ;
- couleur d’accent basée sur le contact courant ;
- style `hover` / `focus` lisible ;
- fond légèrement différent au survol ;
- marges internes plus propres.

## Couleurs contacts

Couleurs stabilisées :

- Joueur : bleu ;
- Camille : violet ;
- Sarah : ambre / caramel sombre ;
- Système : neutre ;
- Narration : style éditorial distinct conservé.

Ajout côté chat :

```gdscript
const SARAH_COLOR := Color("a96d2a")
func _contact_color(contact_id: String) -> Color
```

Le système est prêt pour une couleur par contact.

## Écran Messages

Corrections appliquées :

- liste placée dans un `ScrollContainer` ;
- entrées conversation en largeur `SIZE_EXPAND_FILL` ;
- structure interne en `HBox/VBox` plutôt que texte brut dans un bouton ;
- preview avec autowrap ;
- preview longue raccourcie proprement avec ellipsis ;
- suppression du footer/hint qui risquait d’être coupé ;
- marges réduites pour éviter la troncature à droite.

## JSON conservés

### Camille

Hash inchangé :

`fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Validation : 45 nodes, 6 choice_nodes, 3 end_nodes, aucun duplicate_id, aucun missing_next_target.

### Sarah

Hash inchangé :

`604987540aae25eee7a7244cbce3299d92c1cdac5d54e238242b32547dfe21db`

Validation : 11 nodes, 1 choice_node, 1 end_node, aucun duplicate_id, aucun missing_next_target.

## Runtime Godot

Godot CLI absent localement : validation runtime impossible ici.

À vérifier côté Ludo sur Godot 4.6 : choix longs visibles sans tooltip, Sarah ambre, Camille violet, liste Messages sans troncature droite.
