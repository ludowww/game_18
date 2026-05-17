# T019 — Verrouiller Camille J1 MVP

Statut : DONE

## Décision

**Camille J1 est verrouillé comme première tranche MVP validée runtime.**

Validation runtime déclarée côté Ludo sur **Godot 4.6**.

Aucune modification gameplay, contenu ou UX n’a été effectuée pour T019 : uniquement documentation / verrouillage roadmap.

## État verrouillé

### Schéma JSON utilisé

Schéma : **T003 — Mini-schéma JSON stable Godot**

Fichier de référence :

`/opt/data/profiles/game_18/product/t003_mini_schema_json_godot.md`

Version utilisée dans les données :

```json
"schema_version": "0.1"
```

### Contenu complet verrouillé

Source narrative :

`/opt/data/profiles/game_18/narrative/t007_camille_j1_complete.json`

Copie prototype :

`/opt/data/profiles/game_18/product/godot_t004_prototype/data/camille_j1_complete.json`

Hash identique source/copie :

`fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

Validation statique :

- 45 nodes
- 6 choice_nodes
- 3 end_nodes
- aucun duplicate_id
- aucun missing_next_target

### Prototype Godot branché

Projet :

`/opt/data/profiles/game_18/product/godot_t004_prototype/`

Script principal :

`/opt/data/profiles/game_18/product/godot_t004_prototype/scripts/conversation_screen.gd`

Le prototype charge :

```gdscript
const JSON_PATH := "res://data/camille_j1_complete.json"
```

Version Godot validée côté Ludo : **Godot 4.6**.

## Limites connues acceptées MVP

- Une seule conversation verrouillée : Camille J1.
- Pas encore de liste complète de contacts.
- Pas de sauvegarde.
- Pas de galerie.
- Pas de sons / vibrations.
- Pas d’animations avancées.
- Pas de responsive multi-résolutions final.
- Rythme et UX validés pour cette tranche, mais à retester si on ajoute plusieurs conversations.
- Les jauges/flags sont appliqués en mémoire prototype, sans système global final.
- Le schéma T003 reste volontairement plat et minimal.

## Hors changement T019

- Aucun changement JSON.
- Aucun changement gameplay.
- Aucun changement UX.
- Aucun changement de contenu narratif.
- Aucun nouveau système.

## Conclusion

Camille J1 devient la **référence MVP runtime** pour la suite :

- structure JSON ;
- rythme de messagerie ;
- rendu narration / attente / introspection ;
- interaction choix joueur ;
- branchement Godot minimal.

La suite doit s’appuyer sur cette tranche sans rouvrir le schéma T003 sauf blocage réel.
