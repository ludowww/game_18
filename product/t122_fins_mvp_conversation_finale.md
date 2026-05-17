# T122 — Écrire fins MVP / conversation finale

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : création d’une conversation finale MVP pré-intégration, sans modification Godot runtime ni `conversation_blocks.json`

## Objectif

Écrire les fins MVP sous forme d’une conversation finale dédiée, intégrable en T003, après les seeds J6 produits en T120/T121.

Décision de forme : **conversation finale dédiée**.

Raison : cette forme garde les dialogues J6 modulaires (`Sarah`, `Camille`, `Nico`, `Maya`, `Inès`) et isole le choix final MVP dans un seul JSON, plus simple à intégrer et relire en T123/T124.

## Fichiers créés

Sources narratives :

- `narrative/t122_finales_mvp_complete.json`

Copie Godot data synchronisée :

- `product/godot_t004_prototype/data/finales_mvp_complete.json`

Note produit :

- `product/t122_fins_mvp_conversation_finale.md`

## Identité JSON

- `conversation_id`: `finales_mvp_complete`
- `day`: 6
- `contact_id`: `system`
- `start_node`: `final_block_a`
- volume : 50 nodes, 1 choice node principal, 5 end nodes

## Structure

La conversation commence par un bloc d’entrée :

- téléphone encore allumé ;
- Sarah et le mug ;
- Camille et le morceau non relancé ;
- Nico qui ne couvre plus automatiquement ;
- Maya et la photo ;
- Inès et la porte entrouverte.

Puis un choix final principal :

1. `final_choice_repair` → Réparation fragile
2. `final_choice_camille` → Camille assumée
3. `final_choice_control` → Équilibre maintenu
4. `final_choice_fracture` → Tout se fissure
5. `final_choice_flight` → Fuite en avant / solitude

## Fins écrites

### Fin A — Réparation fragile

End node : `final_end_reparation_fragile`

Le joueur rentre parler à Sarah. Pas de pardon magique : Sarah garde le mug comme point de départ, Nico et Maya restent en retombée sociale légère, et la fin insiste sur une discussion possible plutôt qu’une victoire.

### Fin B — Camille assumée

End node : `final_end_camille_assumee`

Le joueur choisit Camille comme relation réelle, pas comme pause. Camille demande une phrase simple, pas belle ; Sarah n’est pas effacée par magie ; Nico marque la limite sociale.

### Fin C — Équilibre maintenu

End node : `final_end_double_vie_maintenue`

Le joueur garde chaque conversation assez calme pour que la nuit passe. Rien n’explose, mais le téléphone reste plus lourd. La fin est volontairement inconfortable : ça tient seulement “pour l’instant”.

### Fin D — Tout se fissure

End node : `final_end_tout_se_fissure`

Le joueur répond trop tard et trop court. Sarah part dormir ailleurs, Camille coupe court, Nico ferme le standard, Maya arrête de regarder pour le joueur. Pas de scène publique : les liens se retirent un par un.

### Fin E — Fuite en avant / solitude

End node : `final_end_fuite_en_avant`

Le joueur ouvre le message d’Inès au lieu de répondre aux anciens. Inès n’est pas une romance bonus : elle nomme l’échappatoire et laisse un seuil ambigu. L’air entre, le froid aussi.

## Garde-fous T116/T118 appliqués

- Pas de scoring expliqué au joueur.
- Pas de victoire parfaite.
- Pas de révélation totale obligatoire.
- Sarah reste dans le quotidien : mug, retour, dormir ailleurs.
- Camille reste lucide : phrase simple, café, morceau non relancé.
- Nico/Maya sont en retombée courte, pas sauveurs ni omniscients.
- Inès reste porte latérale, pas troisième route complète.
- Aucun hit visible sur les mots surveillés : `trace`, `preuve`, `dette`, `coût`, `double vie`, `conséquence`, `incohérence`, `mensonge`.

## Contraintes respectées

Non modifié :

- `conversation_blocks.json`
- scripts Godot
- runtime/save/UX
- intégration Day 6
- schéma T003

Conservé :

- format JSON plat T003 ;
- choices avec `id`, `text`, `next`, `effects` ;
- `flags` sous forme de tableaux de chaînes ;
- gauges sous forme d’entiers ;
- source narrative et copie Godot synchronisées.

## Validation

Validation locale T122 :

```txt
narrative/t122_finales_mvp_complete.json
- 50 nodes
- 1 choice node principal
- 5 end nodes
- start_node final_block_a présent
- senders autorisés : system, player, sarah, camille, nico, maya, ines
- SHA source/copie Godot OK
```

Contrôles OK :

- JSON parsé ;
- `schema_version = 0.1` ;
- identité `conversation_id`, `day`, `contact_id` conforme ;
- aucun ID dupliqué ;
- aucun `next` ou choice target manquant ;
- tous les nodes atteignables depuis `start_node` ;
- effets valides ;
- copie Godot synchronisée ;
- lexique conceptuel surveillé absent des textes visibles.

## Limites

- Fins non intégrées au prototype dans T122.
- `conversation_blocks.json` n’est pas modifié.
- Le mapping exact depuis les seeds J6 vers la route finale reste à décider/intégrer en T124.
- Pas de playtest Godot runtime côté VPS.

## Recommandation Roadmap

Prochaine étape : **T123 — Relecture cohérence J6 / fins MVP**.
