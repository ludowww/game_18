# Double Vie — J1 V2 expérimental — Point test Godot

## Statut

Première conversion JSON expérimentale effectuée pour préparer une future boucle runtime J1 V2.

Ces fichiers ne sont pas encore branchés dans `conversation_blocks.json` et ne remplacent aucun dialogue actif.

## Fichiers créés

- `product/godot_t004_prototype/data/j1_00_reveil_messages_v2_experimental.json`
- `product/godot_t004_prototype/data/sarah_j1_v2_experimental.json`
- `product/godot_t004_prototype/data/camille_j1_v2_experimental.json`
- `product/godot_t004_prototype/tools/validate_j1_v2_experimental.py`

## Contenu converti

### j1_00

- 14 nodes
- 1 node de choix
- 5 fins de priorité : Sarah, Camille, Nico, Maya, Inès

### Sarah J1 V2

- 34 nodes
- 1 node de choix
- 4 fins : ouverture fragile, version fragile, doute Sarah, absence de version claire

### Camille J1 V2

- 39 nodes
- 1 node de choix
- 6 fins : trouble reconnu, limite respectée, Camille froide, pression trop haute, incertitude ouverte, silence

## Validation

Commandes :

```bash
cd /opt/data/profiles/game_18/product/godot_t004_prototype
python3 tools/validate_j1_v2_experimental.py
python3 tools/validate_dialogues_and_blocks.py
```

Résultat :

- J1 V2 experimental validation: OK
- Runtime actif : OK
- Active dialogues: 20
- Blocks: 46
- Errors: 0

## Pas encore besoin de test Godot

Le test local Godot n’est pas encore utile tant que ces fichiers ne sont pas branchés.

## Quand demander un test à Ludo

Demander un test Godot après une prochaine tâche qui :

1. ajoute ces conversations expérimentales à `ConversationState` ;
2. ajoute des blocs expérimentaux dans `conversation_blocks.json` ou un fichier de blocs V2 séparé ;
3. permet d’ouvrir `j1_00_reveil_messages_v2_experimental.json` depuis la liste ;
4. vérifie que les effets V2 s’affichent/sauvegardent correctement ;
5. garde une voie de retour/reset sans casser la progression existante.

Premier test demandé à Ludo devra vérifier :

- lisibilité des 5 messages d’ouverture ;
- confort des choix longs ;
- rythme typing/scroll ;
- sensation de priorité entre contacts ;
- Sarah et Camille V2 dans l’interface ;
- absence de régression sur l’ancien contenu.
