# T051 — Implémenter current_day + passage J1→J2

Thread : Scope MVP / technique  
Statut : DONE  
Date : 2026-05-15

## Objectif

Ajouter la mécanique minimale de jour définie en T050, sans écrire Camille J2 / Sarah J2 et sans modifier les JSON J1.

## Implémentation

### État global Jour

Ajout dans `ConversationState` :

```gdscript
var current_day: int = 1
var completed_days: Array = []
var day_transition_available: bool = false
```

Rôle :

- `current_day` indique le jour actif ;
- `completed_days` mémorise les jours déjà validés ;
- `day_transition_available` permet d’afficher une action discrète dans Messages quand J1 est terminé.

### Conditions de fin J1

Ajout d’une règle minimale :

```gdscript
const REQUIRED_CONVERSATIONS_BY_DAY := {
  1: ["camille", "sarah"]
}
```

J1 est considéré terminé si :

- `camille.done == true` ;
- `sarah.done == true` ;
- aucun choix actif bloquant n’est présent sur ces conversations.

La vérification est relancée quand une conversation est marquée `done`.

### Passage J1 → J2

Quand J1 est terminé :

- l’écran Messages affiche un bouton discret `Passer au Jour 2` ;
- au clic :
  - J1 est ajouté à `completed_days` ;
  - `current_day` passe de `1` à `2` ;
  - la scène Messages est rechargée ;
  - la sauvegarde est mise à jour.

Décision conservée depuis T050 : passage explicite, pas automatique.

### Conversations J2 préparées

Deux entrées techniques sont ajoutées côté Godot :

- `camille_j2` ;
- `sarah_j2`.

Elles sont :

- rattachées au jour 2 ;
- visibles après passage à J2 ;
- affichées comme `À venir — Jour 2` ;
- désactivées / non cliquables ;
- branchées vers des chemins prévus mais non encore créés :
  - `res://data/camille_j2.json` ;
  - `res://data/sarah_j2.json`.

Aucun contenu J2 n’est écrit dans T051.

### J1 reste visible

Après passage à J2 :

- Camille J1 reste dans Messages ;
- Sarah J1 reste dans Messages ;
- leurs messages, choix, previews et badges restent conservés par la sauvegarde ;
- aucun reset ou replay forcé de J1.

### Affichage discret du jour

L’écran Messages affiche maintenant le jour courant dans le sous-titre :

```text
Prototype MVP — conversations · Jour 1
```

puis :

```text
Prototype MVP — conversations · Jour 2
```

Le header d’une conversation utilise aussi le jour de cette conversation au lieu d’un `J1` hardcodé.

## Sauvegarde

La sauvegarde passe à `SAVE_VERSION = 2` et conserve :

```json
{
  "current_day": 2,
  "completed_days": [1],
  "day_transition_available": false
}
```

Compatibilité anciennes saves :

- absence de `current_day` → valeur par défaut `1` ;
- absence de `completed_days` → valeur par défaut `[]` ;
- absence de `day_transition_available` → valeur recalculée au chargement ;
- les états T043/T045 existants restent conservés : conversations, messages, choices, previews, `has_new`, `dynamic_notifications_fired`.

## Fichiers modifiés

- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/scripts/conversation_list.gd`
- `product/godot_t004_prototype/scripts/conversation_screen.gd`

## Non-changements

- Aucun JSON J1 modifié.
- Aucun dialogue J2 écrit.
- Aucun calendrier complexe.
- Aucune horloge réelle.
- Aucun planning lourd.
- Aucune notification OS.
- Aucun scheduler.

## Validation statique

- Camille J1 JSON : 45 nodes, 6 choice nodes, 3 end nodes, 0 lien cassé.
- Sarah J1 JSON : 41 nodes, 5 choice nodes, 3 end nodes, 0 lien cassé.
- Marqueurs code confirmés : `current_day`, `completed_days`, `REQUIRED_CONVERSATIONS_BY_DAY`, `advance_to_next_day`, bouton `Passer au Jour 2`, entrées `camille_j2` / `sarah_j2`, save/load compatible.
- Godot CLI absent ici : validation runtime à faire côté Ludo sur Godot 4.6.

## Checklist runtime recommandée

1. Charger une save neuve ou reset.
2. Terminer Camille J1.
3. Terminer Sarah J1.
4. Retourner dans Messages.
5. Vérifier apparition du bouton `Passer au Jour 2`.
6. Cliquer dessus.
7. Vérifier le sous-titre `Jour 2`.
8. Vérifier que Camille J1 et Sarah J1 restent visibles.
9. Vérifier que Camille J2 / Sarah J2 apparaissent comme à venir et non cliquables.
10. Quitter / relancer : vérifier que `current_day = 2` persiste.
