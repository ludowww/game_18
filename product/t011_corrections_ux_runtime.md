# T011 — Corrections UX runtime après playtest

Statut : DONE

## Objectif

Corriger les problèmes observés en runtime sans créer de nouveau système lourd.

Fichier modifié :

`/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

## Corrections appliquées

### 1. Couleur dédiée pour Camille

Ajout d’une couleur dédiée :

```gdscript
const CAMILLE_COLOR := Color("46345f")
```

Les bulles Camille utilisent maintenant `CAMILLE_COLOR`, distincte du gris système et du bleu joueur.

### 2. Styles distincts pour système / attente / introspection

Ajout de styles séparés :

```gdscript
const SYSTEM_COLOR := Color("2d2d35")
const WAIT_COLOR := Color("3a3130")
const INTROSPECTION_COLOR := Color("26333b")
```

Ajout d’un classifieur léger côté UI :

```gdscript
func _system_variant(text: String) -> String
```

Règles MVP :

- fins `Fin J1...` → style système ;
- textes avec `attente`, `notification`, `écran`, `calme` → style attente ;
- autres messages système → style introspection.

Le JSON n’est pas modifié.

### 3. Panneau de choix qui ne masque pas les derniers messages

Ajout d’un spacer dynamique dans la liste des messages :

```gdscript
var choice_padding: Control
func _set_choice_padding(choice_count: int) -> void
```

Quand un choix apparaît, le scroll reçoit une marge basse estimée selon le nombre de choix. Les derniers messages restent lisibles au-dessus du panneau.

Quand le choix disparaît, le padding est remis à zéro.

### 4. Auto-scroll corrigé quand un choix apparaît

Ajout d’une fonction centralisée :

```gdscript
func _scroll_to_bottom() -> void
```

Elle est appelée après :

- ajout d’un message ;
- affichage d’un choix ;
- recalcul du padding bas.

### 5. Délai d’affichage ajusté selon longueur du texte

Remplacement du cap fixe par un délai calculé :

```gdscript
const DEBUG_DELAY_MIN_SECONDS := 0.35
const DEBUG_DELAY_MAX_SECONDS := 2.2

func _display_delay_for_text(text: String, source_delay: float) -> float:
    var length_delay := 0.35 + float(text.length()) / 75.0
    return clamp(length_delay, DEBUG_DELAY_MIN_SECONDS, DEBUG_DELAY_MAX_SECONDS)
```

Le champ JSON `delay` reste utilisé comme signal d’attente, mais l’affichage runtime est adapté à la longueur du texte pour le confort de test.

## Non modifié

- Schéma JSON T003 conservé.
- `camille_j1_complete.json` non modifié.
- Aucun nouveau système ajouté.
- Pas de sauvegarde.
- Pas de contacts complets.
- Pas d’animations complexes.

## Validation statique

- JSON chargé : `product/godot_t004_prototype/data/camille_j1_complete.json`.
- Hash JSON inchangé : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`.
- 45 nodes.
- 6 choice_nodes.
- 3 end_nodes.
- aucun duplicate_id.
- aucun missing_next_target.
- script contient les marqueurs attendus : couleur Camille, styles système/attente/introspection, padding choix, auto-scroll, délai calculé.

## Runtime Godot

Godot CLI reste absent dans l’environnement local.

La correction est donc validée statiquement ici, mais doit être confirmée en runtime dans Godot côté machine de playtest.
