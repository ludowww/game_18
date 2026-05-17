# T036 — Verrouiller socle multi-conversation MVP

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Décision

Le socle multi-conversation actuel est verrouillé comme **base MVP validée** avant ajout de contenu narratif supplémentaire.

Aucun changement gameplay, JSON ou UX n’a été appliqué dans T036 : tâche de documentation/verrouillage uniquement.

## Socle validé

### Liste Messages

Écran d’entrée du prototype Godot :

- liste des conversations ;
- cartes structurées en 3 niveaux visibles :
  1. contact ;
  2. titre ;
  3. preview ;
- cartes non clippées après T034 ;
- navigation vers conversation au clic.

### Conversations disponibles

#### Camille

- conversation active ;
- contenu complet MVP J1 ;
- fichier : `product/godot_t004_prototype/data/camille_j1_complete.json` ;
- contact_id : `camille`.

#### Sarah

- conversation active techniquement ;
- placeholder J1 uniquement ;
- fichier : `product/godot_t004_prototype/data/sarah_j1_placeholder.json` ;
- contact_id : `sarah`.

### États runtime séparés

Dans `ConversationState`, Camille et Sarah ont chacune leur état séparé :

- `messages` ;
- `game_state` ;
- `active_choice_node` ;
- `next_node` ;
- `done` ;
- `choices` ;
- `last_preview` ;
- `has_new`.

Le socle reste **runtime-only** : l’état existe pendant la session Godot, sans sauvegarde disque.

### Previews

Règles validées :

- preview séparée Camille / Sarah ;
- preview visible dans la liste Messages ;
- si aucun message : `Démarrer Camille` / `Démarrer Sarah` ;
- si dernier message joueur : `Vous : ...` ;
- si dernier message contact : texte du contact ;
- système / narration : n’écrase pas la preview utile.

### Badges nouveau

Règles validées :

- `has_new` séparé par conversation ;
- badge `nouveau` affiché dans la liste Messages ;
- ouverture d’une conversation = badge retiré pour cette conversation seulement ;
- pas de notification OS ;
- pas de temps réel complexe.

### Navigation aller/retour

Flux validé :

1. Liste Messages ;
2. ouvrir Camille ou Sarah ;
3. conversation ;
4. retour à la liste ;
5. état runtime conservé pendant la session.

## Statut T030 → T035

- **T030 — Notifications simples / nouveaux messages entre conversations** : validé.
- **T031 — Playtest runtime notifications simples multi-conversations** : validé globalement, avec retour sur preview à traiter ensuite.
- **T032 — Corriger preview dernier message dans Messages** : validé statiquement, correction logique appliquée.
- **T033 — Playtest runtime previews Messages + badges has_new** : non validé tel quel, a produit le besoin T034 sur visibilité UI.
- **T034 — Corriger affichage visible des previews dans Messages** : validé statiquement, correction layout appliquée.
- **T035 — Playtest runtime visibilité previews Messages** : validé côté Ludo ; previews visibles, cartes 3 niveaux OK, règles `Vous : ...` / système ignoré / badges conservés.

Conclusion : malgré T033 non validé isolément, le cycle T030→T035 est clos par T034/T035. Le socle est verrouillé.

## Limites connues verrouillées

- pas de sauvegarde disque ;
- pas de notifications OS ;
- pas de temps réel ;
- pas de scheduler d’événements ;
- pas de système complet de contacts ;
- Sarah reste placeholder ;
- pas de multi-jour complet ;
- pas d’images/médias dans ce socle ;
- pas de modification du schéma T003 ;
- pas de modification gameplay dans T036.

## Fichiers de socle

Godot :

- `product/godot_t004_prototype/project.godot`
- `product/godot_t004_prototype/scenes/conversation_list.tscn`
- `product/godot_t004_prototype/scenes/conversation_screen.tscn`
- `product/godot_t004_prototype/scripts/conversation_state.gd`
- `product/godot_t004_prototype/scripts/conversation_list.gd`
- `product/godot_t004_prototype/scripts/conversation_screen.gd`

Données :

- `product/godot_t004_prototype/data/camille_j1_complete.json`
- `product/godot_t004_prototype/data/sarah_j1_placeholder.json`

Documents liés :

- `product/t030_notifications_simples_nouveaux_messages.md`
- `product/t032_corriger_preview_dernier_message_messages.md`
- `product/t034_affichage_visible_previews_messages.md`

## Validation statique JSON

Camille :

- schema_version : `0.1`
- contact_id : `camille`
- nodes : 45
- choice_nodes : 6
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- sha256 : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Sarah :

- schema_version : `0.1`
- contact_id : `sarah`
- nodes : 11
- choice_nodes : 1
- end_nodes : 1
- duplicate_id : 0
- missing_next_target : 0
- sha256 : `604987540aae25eee7a7244cbce3299d92c1cdac5d54e238242b32547dfe21db`

## Runtime

Godot CLI absent dans l’environnement local.

Le verrouillage s’appuie sur :

- validations statiques locales ;
- retours runtime côté Ludo, notamment T035 validé.

## Prochaine étape recommandée

Ajouter du contenu sur ce socle verrouillé, sans toucher au framework multi-conversation sauf bug bloquant.
