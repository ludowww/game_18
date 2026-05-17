# T013 — Stabiliser lecture choix + tempo écriture + style narration

Statut : DONE

## Objectif

Corriger les problèmes runtime T012 sans modifier le JSON T003 ni le contenu Camille J1.

Fichier modifié :

`/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

## Corrections appliquées

### 1. Padding artificiel supprimé

Supprimé :

- `choice_padding`
- `_set_choice_padding()`
- déplacement du padding dans `message_list`

Raison : ce padding créait un gros espace vide et cassait la ligne de vue quand un choix apparaissait.

### 2. Zone de choix stabilisée

Le panneau de choix reste maintenant dans une zone basse réservée et stable :

```gdscript
choice_panel.custom_minimum_size = Vector2(0, 210)
choice_panel.visible = true
```

Quand aucun choix n’est actif, le panneau reste en mode discret/inactif. Quand un choix apparaît, seuls ses contenus changent : la hauteur de lecture ne saute plus brutalement.

### 3. Scroll moins brutal

Remplacement du scroll forcé par une fonction de maintien lisible :

```gdscript
func _ensure_last_message_visible() -> void
```

Objectif : garder le dernier message lisible sans provoquer un saut violent à l’apparition/disparition du choix.

### 4. Tempo d’écriture ralenti

Ancien tempo trop agressif remplacé par une plage plus lente :

```gdscript
const DEBUG_DELAY_MIN_SECONDS := 0.9
const DEBUG_DELAY_MAX_SECONDS := 4.8
```

Le délai dépend davantage de la longueur du texte :

```gdscript
var length_delay := 0.9 + float(text.length()) / 48.0
```

Le champ JSON `delay` reste utilisé comme signal d’attente ; le calcul runtime ajuste seulement le confort de lecture.

### 5. Narration / attente / introspection vraiment différenciées

Les messages `system` ne sont plus affichés comme des bulles de dialogue.

Ajout d’un rendu éditorial :

- `RichTextLabel`
- texte centré
- italique via BBCode
- police légèrement réduite
- encadré distinct
- couleurs différentes selon variante

Styles :

```gdscript
const SYSTEM_COLOR := Color("2d2d35")
const WAIT_COLOR := Color("3a3130")
const INTROSPECTION_COLOR := Color("26333b")
```

Classification MVP conservée côté UI :

- `Fin J1...` → système
- `attente`, `notification`, `écran`, `calme` → attente
- reste → introspection

Aucun champ ajouté au JSON.

## Non modifié

- Schéma JSON T003 conservé.
- `camille_j1_complete.json` non modifié.
- Aucun nouveau système lourd.
- Pas de sauvegarde.
- Pas de contacts complets.
- Pas de refonte.

## Validation statique

- JSON hash inchangé : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`
- 45 nodes
- 6 choice_nodes
- 3 end_nodes
- aucun duplicate_id
- aucun missing_next_target
- marqueurs script OK : suppression padding, zone choix stable, tempo ralenti, narration éditoriale, styles système/attente/introspection.

## Runtime Godot

Godot CLI absent dans l’environnement local.

La correction doit être validée par un nouveau playtest runtime externe, mais elle répond directement aux retours T012 : stabilité de lecture d’abord, pas polish.
