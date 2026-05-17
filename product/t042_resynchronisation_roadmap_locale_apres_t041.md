# T042 — Resynchroniser roadmap locale après T041

Thread d’exécution : Scope MVP / technique  
Statut : DONE

## Objectif

Corriger la roadmap locale après T041, sans toucher au gameplay, aux JSON ni au prototype Godot.

## Décision Roadmap

L’ancien intitulé local `T041 — Ajouter sauvegarde` est obsolète pour la roadmap MVP actuelle.

Le T041 correct est :

**T041 — Relecture cohérence dialogues Camille/Sarah J1**  
Statut : **DONE**

## Résumé T041

- Relecture cohérence Camille/Sarah J1 effectuée.
- Résultat : cohérent MVP.
- Patch Sarah doux appliqué : soupçon plus doux, moins accusatoire.
- Camille inchangée.
- Schéma T003 inchangé.
- Pas de refonte lourde.

## Fichiers T041 concernés

Fichiers mis à jour pendant T041, avant T042 :

- `product/t041_relecture_coherence_dialogues_camille_sarah_j1.md`
- `narrative/t037_sarah_j1_complete.json`
- `product/godot_t004_prototype/data/sarah_j1_complete.json`
- `product/t037_sarah_j1_complete.md`

Fichiers Camille non modifiés :

- `narrative/t007_camille_j1_complete.json`
- `product/godot_t004_prototype/data/camille_j1_complete.json`

## Validation post-patch

### Camille

- schema_version : `0.1`
- conversation_id : `camille_j1_complete`
- contact_id : `camille`
- nodes : 45
- choice_nodes : 6
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- unreachable_node : 0
- senders : `camille`, `player`, `system`
- source/copie prototype identiques : oui
- sha256 : `fba4627bd236d49364e7dc5a06ffa4764b842cfdf0514977f1820d6679ae916e`

### Sarah

- schema_version : `0.1`
- conversation_id : `sarah_j1_complete`
- contact_id : `sarah`
- nodes : 41
- choice_nodes : 5
- end_nodes : 3
- duplicate_id : 0
- missing_next_target : 0
- unreachable_node : 0
- senders : `sarah`, `player`, `system`
- source/copie prototype identiques : oui
- sha256 : `33512a06b873d4b95638ed1ba07f08ca302d28671a564785ebac9e137d59dd1f`

## Non-changements T042

T042 est une tâche de resynchronisation locale uniquement.

- Aucun JSON modifié.
- Aucun fichier Godot modifié.
- Aucun gameplay modifié.
- Aucun changement UX.
- Schéma T003 conservé.

## Fichiers resynchronisés par T042

- `roadmap_double_vie_discord.txt`
- `discord_blocks/bloc_04.txt`
- `discord_blocks/bloc_07.txt` pour neutraliser l’ancien intitulé T041 obsolète.

La Roadmap Discord reste la source de vérité pour les IDs Txxx.

## Prochaine étape logique

T043 — décider la suite après cohérence J1 Camille/Sarah : playtest global J1 ou nouveau contenu.
