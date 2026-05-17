# T121 — Écrire Nico/Maya/Inès J6 pression finale courte

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : création des dialogues J6 secondaires pré-intégration, sans modification Godot runtime ni `conversation_blocks.json`

## Objectif

Compléter la pression finale J6 autour du duo Sarah/Camille déjà écrit en T120 :

- Nico : ami loyal, limite d’alibi, humour + fatigue.
- Maya : détail social concret, pas omniscience.
- Inès : porte latérale / tentation de fuite, rare et hésitante.

T121 prépare les seeds relationnels pour T122 sans écrire les fins MVP finales.

## Fichiers créés

Sources narratives :

- `narrative/t121_nico_j6_complete.json`
- `narrative/t121_maya_j6_complete.json`
- `narrative/t121_ines_j6_complete.json`

Copies Godot data synchronisées :

- `product/godot_t004_prototype/data/nico_j6_complete.json`
- `product/godot_t004_prototype/data/maya_j6_complete.json`
- `product/godot_t004_prototype/data/ines_j6_complete.json`

Note produit :

- `product/t121_nico_maya_ines_j6_pression_finale.md`

## Nico J6 — `nico_j6_complete`

Identité JSON :

- `conversation_id`: `nico_j6_complete`
- `day`: 6
- `contact_id`: `nico`
- `start_node`: `n6_block_a`
- bloc : `n6_block_a`
- volume : 32 nodes, 4 choice nodes, 3 end nodes

### Bloc N6A — dernier service, vraie limite

Fonction : Nico refuse de devenir un standard téléphonique ou un outil d’alibi permanent.

Ancrages :

- frites commandées en trop ;
- Maya qui lui écrit avec “trois points” ;
- réponse propre possible, mais pas héroïque ;
- amitié encore là si le joueur respecte la limite.

End seeds pour T122 :

- `n6_end_loyal_limit` : Nico aide une dernière fois avec limite.
- `n6_end_steps_back` : Nico sort du rôle de tampon social.
- `n6_end_friend_hurt` : Nico recule, blessé d’être traité comme outil.

## Maya J6 — `maya_j6_complete`

Identité JSON :

- `conversation_id`: `maya_j6_complete`
- `day`: 6
- `contact_id`: `maya`
- `start_node`: `m6_block_a`
- bloc : `m6_block_a`
- volume : 32 nodes, 4 choice nodes, 3 end nodes

### Bloc M6A — une photo, pas une enquête

Fonction : Maya relève un détail social concret sans tout savoir ni mener d’enquête.

Ancrages :

- photo du groupe ;
- épaule reconnaissable ;
- “il était pas ailleurs lui ?” ;
- groupe qui peut écrire le résumé à la place du joueur.

End seeds pour T122 :

- `m6_end_warned` : Maya prévient, le joueur doit parler avant le groupe.
- `m6_end_soft_cover` : Maya amortit sans inventer.
- `m6_end_minimized` : le joueur minimise, Maya se retire.

## Inès J6 — `ines_j6_complete`

Identité JSON :

- `conversation_id`: `ines_j6_complete`
- `day`: 6
- `contact_id`: `ines`
- `start_node`: `i6_block_a`
- bloc : `i6_block_a`
- volume : 25 nodes, 3 choice nodes, 3 end nodes

### Bloc I6A — porte latérale à contretemps

Fonction : Inès revient brièvement comme signe de fuite possible, pas comme troisième route complète.

Ancrages :

- trois versions d’un message ;
- arrêt où elle avait vu le joueur marcher trop vite ;
- ticket de trajet gardé dans une poche ;
- seuil / porte / endroit où ça fait moins de bruit.

End seeds pour T122 :

- `i6_end_boundary` : le joueur ferme la porte latérale pour répondre aux liens déjà ouverts.
- `i6_end_ambiguous` : Inès reste une phrase en suspens.
- `i6_end_flight` : la fuite s’ouvre, pas comme romance bonus mais comme échappatoire dangereuse.

## Garde-fous T116/T118 appliqués

- Nico reste oral : vannes courtes, frites, ponctuation de guerre, limite claire.
- Maya reste sociale : photo, groupe, phrase entendue, pas de rôle policier.
- Inès reste rare et flottante : message hésité, seuil, ticket de trajet, tentation douce.
- Aucun hit visible sur les mots surveillés : `trace`, `preuve`, `dette`, `coût`, `double vie`, `conséquence`, `incohérence`, `mensonge`.
- Les endings sont des seeds pour T122, pas des fins MVP finales.

## Contraintes respectées

Non modifié :

- `conversation_blocks.json`
- scripts Godot
- runtime/save/UX
- intégration Day 6
- schéma T003

Conservé :

- format JSON plat T003 ;
- IDs/nodes/choices/end nodes autonomes ;
- `flags` sous forme de tableaux de chaînes ;
- gauges sous forme d’entiers ;
- source narrative et copie Godot synchronisées.

## Validation

Validation locale T121 :

```txt
narrative/t121_nico_j6_complete.json
- 32 nodes
- 4 choice nodes
- 3 end nodes
- marker n6_block_a présent
- senders autorisés : nico, player, system
- SHA source/copie Godot OK

narrative/t121_maya_j6_complete.json
- 32 nodes
- 4 choice nodes
- 3 end nodes
- marker m6_block_a présent
- senders autorisés : maya, player, system
- SHA source/copie Godot OK

narrative/t121_ines_j6_complete.json
- 25 nodes
- 3 choice nodes
- 3 end nodes
- marker i6_block_a présent
- senders autorisés : ines, player, system
- SHA source/copie Godot OK
```

Contrôles OK :

- JSON parsés ;
- `schema_version = 0.1` ;
- identités `conversation_id`, `day`, `contact_id` conformes ;
- aucun ID dupliqué ;
- aucun `next` ou choice target manquant ;
- tous les nodes atteignables depuis `start_node` ;
- effets valides ;
- copies Godot synchronisées ;
- lexique conceptuel surveillé absent des textes visibles.

## Limites

- J6 n’est pas intégré au prototype dans T121.
- `conversation_blocks.json` n’est pas modifié.
- Les fins MVP finales restent à écrire en T122.
- Pas de playtest Godot runtime côté VPS.

## Recommandation Roadmap

Prochaine étape : **T122 — Écrire fins MVP / conversation finale**.
