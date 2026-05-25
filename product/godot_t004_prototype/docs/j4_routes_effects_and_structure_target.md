# J4 V2 — Routes, effets et structure cible

## 0. Statut et périmètre

Document de cahier des charges technique/narratif pour T211. Il prépare la structure J4 sans l’implémenter.

Contraintes T210 :

- aucun JSON modifié ;
- aucun script modifié ;
- aucune conversation J4 créée ;
- aucun dialogue complet écrit ;
- aucun asset ajouté ;
- aucun test modifié ;
- documentation uniquement.

Documents respectés :

- `docs/j4_macro_brief.md` ;
- `docs/j4_temporality_and_availability.md` ;
- `docs/j4_character_arc_matrix.md` ;
- `docs/j4_sarah_nico_cross_thread_design.md` ;
- `docs/narrative_production_bible_j4_plus.md`.

## 1. Rôle de ce document

Ce document prépare la structure technique J4 sans l’implémenter.

Il fixe :

- conversations J4 à créer ;
- ordre de déblocage ;
- required ;
- optionnel ;
- flags MVP ;
- variables à utiliser ;
- effets par posture ;
- limites runtime ;
- tests futurs.

But : T211 pourra créer les JSON skeleton et le runtime J4 sans redécider le design.

## 2. Liste exacte des conversations J4 MVP

Créer à terme six conversations J4 V2 :

1. `sarah_j4_v2`
2. `nico_j4_v2`
3. `sarah_j4_followup_v2`
4. `camille_j4_v2`
5. `maya_j4_v2`
6. `ines_j4_v2`

### Rôle

#### `sarah_j4_v2`

Sarah matin. Détail du quotidien / geste / incohérence faible.

#### `nico_j4_v2`

Consultation / alibi / limite / seed soirée jeux vidéo.

#### `sarah_j4_followup_v2`

Retour Sarah après Nico. Sarah ne sait pas que Nico a été consulté, mais sent délai / ton / formulation.

#### `camille_j4_v2`

Pause midi / travail / tension / limite.

#### `maya_j4_v2`

Fin d’après-midi / ambiance sociale / signaux faibles.

#### `ines_j4_v2`

Soir tard optionnel / calme / fuite.

## 3. Required J4

Required :

- `sarah_j4_v2`
- `nico_j4_v2`
- `sarah_j4_followup_v2`
- `camille_j4_v2`
- `maya_j4_v2`

Optionnelle :

- `ines_j4_v2`

Justification : le follow-up Sarah est required parce qu’il ferme le premier croisement Sarah ↔ Nico. Inès reste optionnelle comme en J2/J3.

## 4. Ordre de déblocage

### Début J4

Disponible :

- `sarah_j4_v2`

Verrouillé :

- `nico_j4_v2`
- `sarah_j4_followup_v2`
- `camille_j4_v2`
- `maya_j4_v2`
- `ines_j4_v2`

### Après `sarah_j4_v2` terminé

Débloquer :

- `nico_j4_v2`

Badge :

`Nico répond quand il peut.`

### Après `nico_j4_v2` terminé

Débloquer :

- `sarah_j4_followup_v2`

Badge :

`Sarah attend toujours ta réponse.`

### Après `sarah_j4_followup_v2` terminé

Débloquer :

- `camille_j4_v2`

Badge :

`Camille écrit pendant sa pause.`

### Après `camille_j4_v2` terminé

Débloquer :

- `maya_j4_v2`

Badge :

`Maya revient sur l’ambiance.`

### Après `maya_j4_v2` terminé

Débloquer :

- `ines_j4_v2`

Badge :

`Inès écrit tard.`

`ines_j4_v2` ne bloque pas le passage au jour suivant.

## 5. Runtime MVP recommandé

Ne pas créer un système multi-fil complexe.

Pour T211 :

- déclarer les six conversations ;
- Sarah disponible au début J4 ;
- réparer les unlocks dans une fonction dédiée : `_repair_j4_v2_progression_unlocks()` ;
- appeler cette fonction après `mark_current_done()` et dans `refresh_day_progression()` ;
- ajouter `_unlock_j4_v2_initial_conversations()` au passage vers J4 expérimental ;
- mettre required J4 dans `_required_conversations_for_current_mode(4)`.

Ne pas implémenter :

- retour dynamique vers une conversation en cours ;
- interruptions temps réel ;
- scheduler ;
- branches runtime complexes selon chaque choix ;
- conversation Nico soirée séparée.

## 6. Structure JSON skeleton attendue T211

Chaque conversation J4 V2 doit avoir :

- `schema_version: "0.1-j4-v2-experimental"`
- `conversation_id`
- `day: 4`
- `contact_id`
- `start_node`
- `experimental: true`
- `nodes`
- `entry_variants.default`

Fichiers attendus :

- `data/sarah_j4_v2_experimental.json`
- `data/nico_j4_v2_experimental.json`
- `data/sarah_j4_followup_v2_experimental.json`
- `data/camille_j4_v2_experimental.json`
- `data/maya_j4_v2_experimental.json`
- `data/ines_j4_v2_experimental.json`

Placeholders :

- Sarah : `[J4 placeholder Sarah matin]`
- Nico : `[J4 placeholder Nico consultation]`
- Sarah follow-up : `[J4 placeholder Sarah retour]`
- Camille : `[J4 placeholder Camille pause]`
- Maya : `[J4 placeholder Maya social]`
- Inès : `[J4 placeholder Inès soir]`

## 7. Flags MVP J4 à réserver

### Sarah matin

- `j4_sarah_morning_detail_noted`
- `j4_player_given_direct_sarah_answer`
- `j4_player_chose_prudent_truth`
- `j4_player_delayed_sarah_answer`
- `j4_sarah_answer_pending_nico_check`
- `j4_player_defensive_with_sarah`

### Nico

- `j4_player_checked_with_nico`
- `j4_nico_advice_requested`
- `j4_nico_advised_direct_answer`
- `j4_nico_cover_requested`
- `j4_nico_helped_version`
- `j4_nico_released_again`
- `j4_player_chooses_own_answer`
- `j4_nico_joke_escape`
- `j4_nico_not_a_service`
- `j4_nico_game_evening_seed`
- `j4_player_considers_game_evening`

### Sarah follow-up

- `j4_sarah_delay_admitted`
- `j4_player_owns_delay`
- `j4_sarah_detail_validated`
- `j4_player_simple_answer`
- `j4_sarah_detail_minimized`
- `j4_sarah_trust_strains`
- `j4_player_searched_words`
- `j4_sarah_hears_effort`
- `j4_player_defensive_followup`
- `j4_sarah_closes_after_defense`

### Camille

- `j4_camille_work_pause`
- `j4_camille_limit_tested`
- `j4_camille_teased_during_work`
- `j4_camille_trouble_named`
- `j4_camille_pressure_too_high`
- `j4_camille_boundary_respected`
- `j4_camille_pause_cut_short`

### Maya

- `j4_maya_group_mood_noted`
- `j4_maya_tone_shift_seen`
- `j4_maya_direct_channel_kept`
- `j4_maya_suspicion_pushed`
- `j4_maya_others_possibly_noticed`
- `j4_maya_social_delay_seen`

### Inès

- `j4_ines_late_reply`
- `j4_ines_refuge_risk`
- `j4_ines_clear_distance`
- `j4_ines_soft_presence`
- `j4_player_avoids_using_ines`
- `j4_ines_keeps_distance`

## 8. Variables J4 autorisées

Réutiliser les variables existantes :

- `confiance_sarah`
- `distance_sarah`
- `dette_nico`
- `risque_exposition`
- `coherence`
- `fatigue_emotionnelle`
- `culpabilite`
- `respect_camille`
- `pression_camille`
- `tension_camille`
- `suspicion_maya`
- `fuite_ines`

Ne pas ajouter de nouvelles variables en T211. Si besoin, utiliser des flags.

## 9. Effets attendus par posture

### Sarah matin

#### Réponse directe

- `confiance_sarah` +1
- `coherence` +2
- flags :
  - `j4_player_given_direct_sarah_answer`
  - `j4_sarah_morning_detail_noted`

#### Vérité prudente

- `confiance_sarah` +1
- `coherence` +1
- `fatigue_emotionnelle` +1
- flags :
  - `j4_player_chose_prudent_truth`

#### Temporiser

- `distance_sarah` +1
- `fatigue_emotionnelle` +1
- `risque_exposition` +1
- flags :
  - `j4_player_delayed_sarah_answer`

#### Vérifier avant de répondre

- `distance_sarah` +1
- `risque_exposition` +1
- `dette_nico` +1
- flags :
  - `j4_sarah_answer_pending_nico_check`
  - `j4_player_checked_with_nico`
  - `j4_player_delayed_sarah_answer`

#### Défense

- `confiance_sarah` -1
- `distance_sarah` +2
- `coherence` -1
- flags :
  - `j4_player_defensive_with_sarah`

### Nico

#### Conseil

- `coherence` +1
- `dette_nico` +1
- `fatigue_emotionnelle` +1
- flags :
  - `j4_nico_advice_requested`
  - `j4_nico_advised_direct_answer`

#### Couverture

- `dette_nico` +2
- `risque_exposition` +2
- `coherence` -1
- flags :
  - `j4_nico_cover_requested`
  - `j4_nico_helped_version`

#### Libérer Nico

- `dette_nico` -1
- `coherence` +1
- flags :
  - `j4_nico_released_again`
  - `j4_player_chooses_own_answer`

#### Plaisanter / esquiver

- `dette_nico` +1
- `risque_exposition` +1
- flags :
  - `j4_nico_joke_escape`
  - `j4_nico_not_a_service`

#### Soirée console

- `fatigue_emotionnelle` -1
- flags :
  - `j4_nico_game_evening_seed`
  - `j4_player_considers_game_evening`

### Sarah follow-up

#### Assumer le délai

- `confiance_sarah` +1
- `coherence` +1
- `fatigue_emotionnelle` +1
- flags :
  - `j4_sarah_delay_admitted`
  - `j4_player_owns_delay`

#### Réponse simple

- `confiance_sarah` +2
- `distance_sarah` -1
- `coherence` +2
- flags :
  - `j4_sarah_detail_validated`
  - `j4_player_simple_answer`

#### Rester flou

- `confiance_sarah` -1
- `distance_sarah` +1
- `coherence` -1
- flags :
  - `j4_sarah_detail_minimized`
  - `j4_sarah_trust_strains`

#### Chercher ses mots

- `confiance_sarah` +1
- `coherence` +1
- `fatigue_emotionnelle` +1
- flags :
  - `j4_player_searched_words`
  - `j4_sarah_hears_effort`

#### Défense follow-up

- `confiance_sarah` -2
- `distance_sarah` +2
- `coherence` -1
- flags :
  - `j4_player_defensive_followup`
  - `j4_sarah_closes_after_defense`

### Camille

#### Taquiner

- `tension_camille` +1
- flags :
  - `j4_camille_teased_during_work`

#### Respecter pause / limite

- `respect_camille` +2
- `pression_camille` -1
- `coherence` +1
- flags :
  - `j4_camille_boundary_respected`

#### Nommer trouble

- `tension_camille` +2
- `pression_camille` +1
- `risque_exposition` +1
- flags :
  - `j4_camille_trouble_named`

#### Forcer

- `pression_camille` +2
- `respect_camille` -1
- flags :
  - `j4_camille_pressure_too_high`

#### Couper court

- `respect_camille` +1
- `tension_camille` -1
- `coherence` +1
- flags :
  - `j4_camille_pause_cut_short`

### Maya

#### Accepter son regard

- `coherence` +1
- flags :
  - `j4_maya_group_mood_noted`

#### Demander direct

- `suspicion_maya` -1
- `coherence` +1
- flags :
  - `j4_maya_direct_channel_kept`

#### Minimiser

- `suspicion_maya` +2
- `risque_exposition` +1
- flags :
  - `j4_maya_suspicion_pushed`

#### Demander qui d’autre

- `risque_exposition` +2
- `fatigue_emotionnelle` +1
- flags :
  - `j4_maya_others_possibly_noticed`

#### Plaisanter

- `fatigue_emotionnelle` -1
- `suspicion_maya` +1
- flags :
  - `j4_maya_social_delay_seen`

### Inès

#### Calme clair

- `fuite_ines` -1
- `coherence` +1
- flags :
  - `j4_ines_soft_presence`

#### Ne pas l’utiliser

- `fuite_ines` -2
- `coherence` +1
- flags :
  - `j4_player_avoids_using_ines`

#### Refuge

- `fuite_ines` +2
- `coherence` -1
- `culpabilite` +1
- flags :
  - `j4_ines_refuge_risk`

#### Se retirer

- `fuite_ines` -1
- `fatigue_emotionnelle` +1
- flags :
  - `j4_ines_clear_distance`

#### Prolonger trop

- `fuite_ines` +1
- `culpabilite` +1
- flags :
  - `j4_ines_late_reply`

## 10. Entry variants futures recommandées

T211 skeleton n’aura que `default`. Les variantes seront ajoutées lors de l’écriture.

À prévoir plus tard :

### Sarah matin

- `after_actions_promised`
- `after_honest_uncertainty`
- `after_more_time`
- `after_defensive`
- `default`

### Nico

- `after_sarah_pending_check`
- `after_direct_sarah_answer`
- `after_sarah_delay`
- `after_sarah_defensive`
- `default`

### Sarah follow-up

- `after_nico_helped_version`
- `after_nico_advice`
- `after_nico_released`
- `after_delay_only`
- `after_defensive`
- `default`

### Camille

- `after_boundary_respected`
- `after_tension_reopened`
- `after_pressure_high`
- `after_minimized`
- `default`

### Maya

- `after_social_thread`
- `after_group_boundary`
- `after_suspicion_reinforced`
- `after_direct_channel`
- `default`

### Inès

- `after_clear_presence`
- `after_soft_distance`
- `after_refuge_risk`
- `after_step_back`
- `default`

## 11. Tests futurs T211

Créer : `tests/test_t211_j4_v2_structure.py`

Le test devra vérifier :

1. Les six JSON J4 existent.
2. Chaque JSON :
   - `schema_version == "0.1-j4-v2-experimental"`
   - `day == 4`
   - `experimental == true`
   - contient `start_node`
   - contient `entry_variants.default`
   - contient un node `end`
3. `conversation_state.gd` déclare :
   - `sarah_j4_v2`
   - `nico_j4_v2`
   - `sarah_j4_followup_v2`
   - `camille_j4_v2`
   - `maya_j4_v2`
   - `ines_j4_v2`
4. Début J4 expérimental : Sarah J4 disponible uniquement.
5. Déblocage :
   - Sarah → Nico
   - Nico → Sarah follow-up
   - Sarah follow-up → Camille
   - Camille → Maya
   - Maya → Inès
6. Required J4 contient :
   - Sarah
   - Nico
   - Sarah follow-up
   - Camille
   - Maya
7. Required J4 ne contient pas Inès.
8. Legacy J4 masqué en mode expérimental.
9. J1/J2/J3 non régressés.

## 12. Décisions finales avant T211

Décisions validées :

- six conversations J4 ;
- Sarah follow-up required ;
- Inès optionnelle ;
- une seule conversation Nico J4 pour le MVP ;
- pas de média J4 au skeleton ;
- pas de runtime multi-fil complexe ;
- croisement Sarah ↔ Nico simulé par unlock + follow-up ;
- required J4 = Sarah/Nico/Sarah follow-up/Camille/Maya.

## 13. Conclusion

T210 fige la cible technique/narrative J4.

T211 peut maintenant ajouter :

- JSON skeleton J4 ;
- déclarations runtime ;
- déblocage progressif ;
- required J4 ;
- tests de structure.

Validation :

- créer uniquement cette doc ;
- lancer : `python3 tools/validate_j1_v2_experimental.py` ;
- git status propre.
