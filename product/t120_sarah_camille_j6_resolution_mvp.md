# T120 — Écrire Sarah/Camille J6 résolution MVP

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : création des dialogues J6 Sarah/Camille pré-intégration, sans modification Godot runtime ni `conversation_blocks.json`

## Objectif

Écrire les deux conversations principales de résolution MVP pour J6 :

- Sarah : vérité intime, relation officielle, quotidien qui ne tient plus.
- Camille : position claire, refus d’être une parenthèse ou un refuge.

T120 prépare la fin MVP sans intégrer J6 dans le prototype et sans écrire encore Nico/Maya/Inès ni les fins finales T122.

## Fichiers créés

Sources narratives :

- `narrative/t120_sarah_j6_complete.json`
- `narrative/t120_camille_j6_complete.json`

Copies Godot data synchronisées :

- `product/godot_t004_prototype/data/sarah_j6_complete.json`
- `product/godot_t004_prototype/data/camille_j6_complete.json`

Note produit :

- `product/t120_sarah_camille_j6_resolution_mvp.md`

## Sarah J6 — `sarah_j6_complete`

Identité JSON :

- `conversation_id`: `sarah_j6_complete`
- `day`: 6
- `contact_id`: `sarah`
- `start_node`: `s6_block_a`
- blocs : `s6_block_a`, `s6_block_b`
- volume : 50 nodes, 6 choice nodes, 3 end nodes

### Bloc S6A — le quotidien ne tient plus

Fonction : Sarah ouvre par des détails domestiques, sans posture d’enquête.

Ancrages :

- mug laissé dans l’évier ;
- assiette gardée puis jetée ;
- téléphone posé face contre table ;
- fatigue de devoir attendre et deviner.

Sarah ne cherche pas une preuve. Elle dit que le quotidien commence à parler à la place du joueur.

### Bloc S6B — rester ou seulement faire tenir

Fonction : Sarah formule la question émotionnelle simple de J6 :

> Tu veux encore être là avec moi, ou tu veux juste que ça ne casse pas ce soir ?

Les choix ouvrent trois couleurs pour T122 :

- réparation fragile : `s6_end_repair`
- maintien incertain / contrôle fragile : `s6_end_uncertain`
- distance Sarah : `s6_end_distance`

Ces fins ne sont pas les fins MVP finales : elles préparent les graines relationnelles pour T122.

## Camille J6 — `camille_j6_complete`

Identité JSON :

- `conversation_id`: `camille_j6_complete`
- `day`: 6
- `contact_id`: `camille`
- `start_node`: `c6_block_a`
- blocs : `c6_block_a`, `c6_block_b`
- volume : 50 nodes, 6 choice nodes, 3 end nodes

### Bloc C6A — le téléphone encore allumé

Fonction : Camille revient par un morceau de musique, un café banal, le téléphone encore consulté.

Ancrages :

- même morceau qu’hier ;
- café regardé comme une porte de secours ;
- phrase qui tient dans un coin d’écran ;
- refus de servir seulement d’endroit où respirer.

Camille reste lucide et oblique : elle ne lance pas un ultimatum caricatural.

### Bloc C6B — ne plus être une parenthèse

Fonction : Camille demande du respect et une position plus claire.

Formule centrale :

> Je ne veux pas être l’endroit où tu respires quand tu n’arrives plus à parler ailleurs.

Les choix ouvrent trois couleurs pour T122 :

- Camille assumée : `c6_end_chosen_seed`
- distance honnête / vérité avant Camille : `c6_end_respect_distance`
- Camille coupe court : `c6_end_cuts_short`

Ces fins préparent T122 sans résoudre tout le MVP dans T120.

## Garde-fous T116/T118 appliqués

- Sarah part de détails domestiques et fatigue douce, pas d’interrogatoire.
- Camille utilise musique, lieu, téléphone, silence, pas de jalousie frontale.
- Aucun hit visible sur les mots surveillés : `trace`, `preuve`, `dette`, `coût`, `double vie`, `conséquence`, `incohérence`, `mensonge`.
- Pression présente, mais respiration conservée : thé, mug, assiette, morceau, café.

## Contraintes respectées

Non modifié :

- `conversation_blocks.json`
- scripts Godot
- runtime/save/UX
- intégration Day 6
- schéma T003

Conservé :

- format JSON plat T003 ;
- nodes avec `id`, `type`, `sender`, `text`, `delay`, `next` si applicable ;
- choices avec `id`, `text`, `next`, `effects` ;
- `flags` sous forme de tableau de chaînes ;
- gauges sous forme d’entiers.

## Validation

Validation locale T120 :

```txt
narrative/t120_sarah_j6_complete.json
- 50 nodes
- 6 choice nodes
- 3 end nodes
- markers s6_block_a / s6_block_b présents
- senders autorisés : sarah, player, system
- SHA source/copie Godot OK

narrative/t120_camille_j6_complete.json
- 50 nodes
- 6 choice nodes
- 3 end nodes
- markers c6_block_a / c6_block_b présents
- senders autorisés : camille, player, system
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
- copies Godot synchronisées.

## Limites

- J6 n’est pas intégré au prototype dans T120.
- `conversation_blocks.json` n’est pas modifié.
- Nico, Maya, Inès J6 restent à écrire en T121.
- Les fins MVP finales restent à écrire en T122.
- Pas de playtest Godot runtime côté VPS.

## Recommandation Roadmap

Prochaine étape : **T121 — Écrire Nico/Maya/Inès J6 pression finale courte**.
