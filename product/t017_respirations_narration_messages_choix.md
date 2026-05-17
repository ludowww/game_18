# T017 — Ajuster respirations entre narration, messages et choix

Statut : DONE

## Objectif

Rendre le rythme de lecture naturel sans modifier le JSON T003 ni le contenu Camille J1.

Fichier modifié :

`/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

## Corrections appliquées

### 1. Court délai avant affichage des choix

Ajout d’un délai avant l’apparition d’un node `choice` :

```gdscript
const PRE_CHOICE_DELAY_SECONDS := 0.8
```

Dans `_advance_to`, si le node cible est un choix et qu’il n’est pas appelé en immédiat, le prototype attend avant d’afficher la barre de réponse.

Effet attendu : éviter que message Camille + choix apparaissent simultanément.

### 2. Temps de lecture après narration / système / introspection

Ajout d’un temps de lecture dédié :

```gdscript
const NARRATION_READ_SECONDS := 1.6
```

Après affichage d’un message `system`, le prototype attend avant de passer au node suivant.

Effet attendu : éviter que narration + message Camille apparaissent simultanément.

### 3. Typing indicator après la respiration narrative

Le flux est maintenant :

1. afficher narration / système / introspection ;
2. attendre `NARRATION_READ_SECONDS` ;
3. avancer vers le node suivant ;
4. afficher `Camille écrit…` uniquement si ce node suivant est de Camille.

Le typing indicator reste limité à :

```gdscript
sender == "camille"
```

### 4. Temps minimum entre deux messages

Ajout d’une respiration courte entre messages non-système :

```gdscript
const MIN_BETWEEN_MESSAGES_SECONDS := 0.6
```

Effet attendu : éviter les enchaînements trop secs entre deux bulles ou entre une bulle et un choix.

### 5. Modèle T015 conservé

Le modèle T015 reste en place :

- délai appliqué avant node cible ;
- réponse joueur immédiate après choix via `immediate = true` ;
- barre de choix compacte ;
- choix longs gérés sans casser la lecture ;
- narration en style éditorial.

## Non modifié

- Schéma JSON T003 conservé.
- `camille_j1_complete.json` non modifié.
- Aucun nouveau système.
- Pas de modification narrative.

## Validation statique

- JSON hash inchangé : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`
- 45 nodes
- 6 choice_nodes
- 3 end_nodes
- aucun duplicate_id
- aucun missing_next_target
- marqueurs script OK : délai avant choix, temps lecture narration, typing Camille uniquement, temps minimum entre messages, modèle T015 conservé.

## Runtime Godot

Godot CLI absent localement : validation runtime impossible ici.

À valider en playtest : rythme ressenti entre narration → Camille, Camille → choix, et message → message.
