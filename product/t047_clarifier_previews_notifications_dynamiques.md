# T047 — Clarifier previews notifications dynamiques

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Objectif

Éviter qu’une notification dynamique ressemble à un vrai dernier message absent du dialogue JSON.

## Décision MVP

Les previews dynamiques ne doivent pas simuler une phrase de dialogue.

Elles affichent désormais un libellé neutre :

- `Nouveau message de Sarah`
- `Nouveau message de Camille`

Cela distingue clairement :

- un vrai dernier message issu du JSON ;
- une notification d’appel générée par le prototype.

## Changement appliqué

Fichier modifié :

- `product/godot_t004_prototype/scripts/conversation_state.gd`

Les déclencheurs T045 sont conservés :

- `c1_010` ;
- `c1_020` ;
- `s1_006` ;
- `s1_020`.

Mais les previews hardcodées changent.

### Avant

Exemples de previews ambiguës :

- `Tu sais déjà si tu rentres pour manger ?`
- `Tu es encore dehors ?`
- `Tu réponds quand tu peux ?`
- `Je crois que j’ai pensé à toi au mauvais moment.`

Problème : ces phrases pouvaient sembler être des messages réels alors qu’elles n’existent pas forcément comme nodes dans le JSON.

### Après

- Camille déclenche Sarah → `Nouveau message de Sarah`
- Sarah déclenche Camille → `Nouveau message de Camille`

## Conservé

- déclencheurs T045 ;
- `has_new` ;
- badge `nouveau` ;
- preview sauvegardée ;
- anti-doublon `dynamic_notifications_fired` ;
- sauvegarde locale T043 ;
- JSON T003 inchangé ;
- aucun JSON modifié ;
- pas de notification OS ;
- pas de temps réel ;
- pas de scheduler.

## Validation statique

### Camille

- fichier : `product/godot_t004_prototype/data/camille_j1_complete.json`
- schema_version : `0.1`
- contact_id : `camille`
- nodes : 45
- choice_nodes : 6
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- sha256 : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

### Sarah

- fichier : `product/godot_t004_prototype/data/sarah_j1_complete.json`
- schema_version : `0.1`
- contact_id : `sarah`
- nodes : 41
- choice_nodes : 5
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- sha256 : `33512a06b873d4b95638ed1ba07f08ca302d28671a564785ebac9e137d59dd1f`

## Marqueurs code vérifiés

- `Nouveau message de Sarah`
- `Nouveau message de Camille`
- anciens textes ambigus absents ;
- triggers `c1_010`, `c1_020`, `s1_006`, `s1_020` présents ;
- `mark_conversation_new(target_id, preview)` conservé ;
- `dynamic_notifications_fired` conservé ;
- sauvegarde locale conservée.

## Limite runtime

Godot CLI absent dans l’environnement local : validation runtime à faire côté Ludo sur Godot 4.6.
