# Double Vie — Refonte J1 — Point d’intégration avant Godot

## Statut actuel

La refonte narrative J1 est cadrée et les scènes sont rédigées en drafts lisibles.
Aucun fichier runtime actif n’a encore été modifié.

## Fichiers de cadrage créés

- `product/mvp_refonte_source_verite.md`
- `product/refonte_j1_structure_scenes.md`
- `product/godot_t004_prototype/data/schema/variables_and_flags_schema.json`
- `product/refonte_j1_generation_template.md`

## Drafts J1 créés

- `product/refonte_j1_00_reveil_messages_draft.md`
- `product/refonte_j1_01_sarah_absence_draft.md`
- `product/refonte_j1_02_camille_dehors_draft.md`
- `product/refonte_j1_03_nico_couverture_draft.md`
- `product/refonte_j1_04_maya_pique_draft.md`
- `product/refonte_j1_05_ines_faille_draft.md`
- `product/refonte_j1_06_sarah_rentrer_manger_draft.md`
- `product/refonte_j1_07_nico_vanne_soiree_draft.md`

## Validation effectuée

- Tous les blocs d’effets JSON présents dans les drafts sont valides.
- Aucune variable V2 inconnue détectée.
- Aucun flag inconnu détecté.
- Le schéma V2 contient 15 variables officielles et 68 flags uniques.
- Le validateur runtime existant reste OK : 20 dialogues actifs, 46 blocs, 0 erreur.

## Ce qui n’a pas été modifié

- `scripts/conversation_screen.gd`
- `scripts/conversation_list.gd`
- `scripts/conversation_state.gd`
- `data/conversation_blocks.json`
- les JSON runtime actifs `*_complete.json`

## Quand demander un test Godot à Ludo

Pas encore nécessaire.

Le test Godot devient nécessaire après la prochaine étape technique : conversion d’une première boucle J1 V2 en JSON runtime expérimental.

Premier test recommandé plus tard :

1. intégrer `j1_00_reveil_messages` comme conversation système expérimentale ;
2. brancher au moins Sarah et Camille J1 V2 derrière deux choix ;
3. vérifier dans Godot :
   - affichage ouverture ;
   - lisibilité des choix ;
   - application des effets V2 ;
   - sauvegarde ;
   - retour liste conversation ;
   - absence de régression UX typing/scroll.

## Prochaine étape recommandée

Créer un export de relecture J1 V2 ou convertir les drafts en JSON runtime expérimental.

Recommandation : avant runtime, faire une passe de relecture lisible consolidée :

- `product/refonte_j1_export_relecture.md`

Puis seulement ensuite :

- `product/godot_t004_prototype/data/j1_v2_reveil_messages.json`
- éventuellement `sarah_j1_v2.json`, `camille_j1_v2.json`, etc.

Objectif : éviter de corriger du JSON si le problème est encore narratif.
