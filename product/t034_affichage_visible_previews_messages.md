# T034 — Corriger affichage visible des previews dans Messages

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Objectif

Rendre la preview réellement visible dans chaque carte conversation de l’écran Messages.

## Correction appliquée

Fichier modifié :

- `product/godot_t004_prototype/scripts/conversation_list.gd`

La carte conversation est maintenant dimensionnée pour afficher clairement 3 niveaux :

1. nom du contact ;
2. titre de conversation ;
3. preview visible.

## Changements UI

- hauteur carte augmentée : `Vector2(0, 132)` ;
- marge verticale augmentée ;
- séparation interne explicite dans le bloc texte ;
- preview avec hauteur minimale dédiée : `Vector2(0, 38)` ;
- preview en `autowrap` ;
- suppression du clipping sur preview : `preview.clip_text = false` ;
- couleur preview rendue plus lisible ;
- scroll horizontal désactivé pour éviter une carte trop large ou décalée ;
- liste en `SIZE_EXPAND_FILL` horizontal et vertical.

## Règles conservées

La logique de preview reste celle de T032 dans `ConversationState` :

- aucun message encore affiché : `Démarrer Camille` / `Démarrer Sarah` ;
- conversation avec `has_new` : preview existante, ex. `Nouveau message` ;
- dernier message joueur : `Vous : ...` ;
- dernier message contact : texte du contact ;
- message `system` / narration : ne remplace pas la preview ;
- previews séparées Camille / Sarah ;
- `has_new` conservé.

## Hors-scope confirmé

- aucun JSON modifié ;
- aucun changement de schéma T003 ;
- aucune sauvegarde disque ;
- aucune notification OS ;
- pas de refonte complète de la liste Messages.

## Validation statique

Marqueurs UI vérifiés :

- `button.custom_minimum_size = Vector2(0, 132)` ;
- `preview.custom_minimum_size = Vector2(0, 38)` ;
- `preview.clip_text = false` ;
- `ConversationState.preview_text(conversation_id)` ;
- `line.text = title` ;
- `preview.text = _short_preview(meta)`.

Marqueurs logique preview conservés :

- `Démarrer ...` ;
- `Vous : ...` ;
- ignore `sender == "system"` ;
- `has_new` conservé ;
- plus de `var state := ...` fragile côté Godot 4.6.

Camille :

- fichier : `product/godot_t004_prototype/data/camille_j1_complete.json`
- schema_version : `0.1`
- contact_id : `camille`
- nodes : 45
- choice_nodes : 6
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- sha256 : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Sarah :

- fichier : `product/godot_t004_prototype/data/sarah_j1_placeholder.json`
- schema_version : `0.1`
- contact_id : `sarah`
- nodes : 11
- choice_nodes : 1
- end_nodes : 1
- duplicate_id : 0
- missing_next_target : 0
- sha256 : `604987540aae25eee7a7244cbce3299d92c1cdac5d54e238242b32547dfe21db`

## Limite runtime

Godot CLI absent dans l’environnement local : validation runtime à faire côté Ludo sur Godot 4.6.

Checklist runtime T034 :

- écran Messages : Camille affiche 3 niveaux visibles ;
- écran Messages : Sarah affiche 3 niveaux visibles ;
- Camille avant démarrage : `Démarrer Camille` ;
- Sarah avant démarrage ou notification : `Nouveau message` / `Démarrer Sarah` ;
- après réponse joueur : `Vous : ...` visible ;
- après message contact : dernier message contact visible ;
- narration/système ne remplace pas la preview.
