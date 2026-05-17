# T015 — Repenser interaction choix + timing d’écriture

Statut : DONE

## Objectif

Corriger le modèle UX après T014 non validé : le prototype doit se comporter comme une vraie messagerie, sans modifier le schéma JSON T003 ni le contenu Camille J1.

Fichier modifié :

`/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

## Corrections appliquées

### 1. Délai appliqué avant affichage du message cible

Le modèle a été corrigé : on ne calcule plus l’attente à partir du message déjà affiché.

Ajout du flux :

```gdscript
func _advance_to(node_id: String, immediate: bool = false) -> void
func _wait_before_node(node: Dictionary) -> void
```

Le délai est maintenant appliqué avant l’affichage du node cible.

### 2. `Camille écrit…` uniquement avant Camille

Le typing indicator n’apparaît que si le prochain node à afficher a :

```json
"sender": "camille"
```

Aucun typing indicator avant :

- narration ;
- attente ;
- système ;
- message joueur.

### 3. Réponse joueur immédiate après choix

Au clic sur un choix :

```gdscript
_advance_to(str(choice.get("next", "")), true)
```

Le node cible est affiché immédiatement si nécessaire, ce qui permet à la réponse joueur de s’afficher sans délai artificiel.

### 4. Zone de choix compacte type barre de réponse

Suppression du modèle T013 de zone réservée haute :

- plus de `choice_panel.custom_minimum_size = Vector2(0, 210)` ;
- le panneau de choix est maintenant masqué quand inactif ;
- il redevient visible uniquement quand un choix existe ;
- prompt réduit à `Répondre` ;
- boutons plus compacts.

Objectif : la conversation garde la majorité de l’écran.

### 5. Choix longs gérés sans casser la lecture

Ajout d’un calcul simple de hauteur :

```gdscript
func _choice_button_height(text: String) -> int
```

- choix courts : 40 px ;
- choix longs : 52 px ;
- texte complet disponible en tooltip ;
- texte clipé plutôt que de casser toute la zone de lecture.

### 6. Tempo d’écriture ralenti

Nouveau tempo plus lent :

```gdscript
const DEBUG_DELAY_MIN_SECONDS := 1.1
const DEBUG_DELAY_MAX_SECONDS := 6.5
var length_delay := 1.1 + float(text.length()) / 42.0
```

Les messages longs prennent nettement plus de temps.

### 7. Narration conservée en style éditorial

Le rendu T013 est conservé :

- `RichTextLabel` ;
- italique ;
- centré ;
- taille réduite ;
- encadré distinct ;
- pas une bulle de dialogue.

## Non modifié

- Schéma JSON T003 conservé.
- `camille_j1_complete.json` non modifié.
- Aucun nouveau système lourd.
- Pas de sauvegarde.
- Pas de contacts complets.
- Pas de modification narrative.

## Validation statique

- JSON hash inchangé : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`
- 45 nodes
- 6 choice_nodes
- 3 end_nodes
- aucun duplicate_id
- aucun missing_next_target
- marqueurs script OK : délai avant node cible, typing Camille uniquement, réponse joueur immédiate, barre de choix compacte, choix longs gérés, narration éditoriale.

## Runtime Godot

Godot CLI absent localement : validation runtime impossible ici.

À vérifier au prochain playtest : stabilité visuelle au moment où la barre de réponse apparaît/disparaît, et ressenti du tempo long.
