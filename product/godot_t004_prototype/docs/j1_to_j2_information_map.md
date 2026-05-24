# J1 → J2 — Carte des informations par personnage

## 1. Principe

Le Jour 2 doit être cohérent avec les informations réellement produites au Jour 1. Chaque personnage doit parler depuis :

- ce qu’il a vu ;
- ce qu’on lui a dit ;
- ce qu’il a ressenti ;
- ce qu’il peut raisonnablement soupçonner.

Aucun personnage ne doit parler depuis :

- un flag invisible ;
- une conversation qu’il n’a pas eue ;
- une information donnée à un autre personnage ;
- une vérité canonique non révélée.

Cette carte ne corrige aucun dialogue. Elle classe les raccords pour préparer T183.

Sources inspectées : JSON J1/J2 V2 expérimentaux, `docs/j2_story_reframe.md`, `docs/j1_v2_mvp_conventions.md`, `docs/j2_dynamic_systems.md`, `docs/j2_playable_structure.md`.

## 2. Carte Sarah J1

Conversation principale : `data/sarah_j1_v2_experimental.json`.

### Choix `j1_01_needed_air`

- Texte joueur : « J’avais besoin d’air. Je suis sorti un moment. J’aurais dû te le dire. »
- Flags : `said_needed_air_to_sarah`, `sarah_version_needed_air`.
- Effets : `confiance_sarah +1`, `distance_sarah -1`, `coherence +2`, `culpabilite +1`.
- Sarah sait : le joueur dit être sorti pour respirer / prendre l’air ; il reconnaît qu’il aurait dû prévenir.
- Sarah soupçonne : le retour était quand même absent / étrange ; la version ne répond pas à tout.
- Sarah ne sait pas : la place exacte de Camille ; ce que Nico sait ; ce que Maya a vu ; la vérité intime.
- Autorisé J2 : Sarah peut parler d’absence, de besoin d’air, de retour émotionnel incomplet.
- Non autorisé J2 : affirmer que Camille était impliquée ou que Nico couvre, sauf autre flag.

### Choix `j1_01_nico_alibi`

- Texte joueur : « J’étais avec Nico une partie du temps. On a parlé dehors. »
- Flags : `used_nico_alibi_sarah`, `sarah_version_nico`.
- Effets : `confiance_sarah -1`, `distance_sarah +1`, `dette_nico +3`, `coherence -2`, `risque_exposition +2`.
- Sarah sait : le joueur implique Nico dans une partie de la soirée.
- Sarah soupçonne : l’expression « une partie du temps » bouge par rapport à une version plus courte ; elle peut comparer les versions.
- Sarah ne sait pas : si Nico a accepté de couvrir ; si Camille est la cause ; ce que Nico dira ensuite.
- Autorisé J2 : `after_nico_version` peut rappeler que la version Nico bouge / devient officielle.
- Non autorisé J2 : Sarah ne doit pas connaître le contenu d’une conversation Nico privée.

### Choix `j1_01_camille_minimized`

- Texte joueur : « J’ai croisé Camille dehors. On a parlé, c’est tout. »
- Flags : `mentioned_camille_to_sarah`, `minimized_camille_to_sarah`, `sarah_version_camille_minimized`.
- Effets : `confiance_sarah -2`, `distance_sarah +2`, `coherence -1`, `culpabilite +2`, `risque_exposition +1`.
- Sarah sait : le nom Camille est explicitement associé au dehors ; le joueur minimise.
- Sarah soupçonne : le « c’est tout » sert peut-être de couvercle.
- Sarah ne sait pas : ce que Camille ressent ; ce que le joueur a dit à Camille ; si Camille reconnaît la tension.
- Autorisé J2 : `after_camille_minimized` peut citer le « On a parlé, c’est tout. »
- Non autorisé J2 : Sarah ne doit pas parler comme si elle avait entendu Camille.

### Choix `j1_01_vulnerable`

- Texte joueur : « Je sais pas bien. Je suis sorti parce que j’étais pas bien. Et quand je suis revenu, je n’ai pas réussi à revenir vraiment. »
- Flags : `vulnerable_to_sarah`, `sarah_version_emotional_confusion`.
- Effets : `confiance_sarah +2`, `distance_sarah -1`, `coherence +1`, `culpabilite +2`, `fatigue_emotionnelle +1`.
- Sarah sait : le joueur admet une confusion émotionnelle et une présence partielle.
- Sarah soupçonne : quelque chose reste non nommé.
- Sarah ne sait pas : le détail Camille/Nico/Maya, sauf autres flags.
- Autorisé J2 : Sarah peut valoriser une phrase fragile mais réelle.
- Non autorisé J2 : transformer cette vulnérabilité en confession factuelle.

### Sarah repas J1 — `data/sarah_meal_j1_v2_experimental.json`

#### `j1_06_come_home`

- Texte joueur : « Oui. Je rentre. Et je vais essayer d’être vraiment là. »
- Flags : `sarah_j1_domestic_presence`.
- Effets : `confiance_sarah +2`, `distance_sarah -2`, `intimite_sarah +2`, `fatigue_emotionnelle -1`.
- Sarah sait : il est rentré / a promis une présence domestique.
- Autorise J2 : `after_domestic_presence`, gratitude fragile, nuance entre présence physique et conversation réelle.
- N’autorise pas : effacer le malaise ou conclure que tout est réparé.

#### `j1_06_later`

- Texte joueur : « Je passe plus tard. Je veux pas te laisser attendre sans réponse. »
- Flags : `promised_sarah_later_j1`.
- Effets : `confiance_sarah +1`, `distance_sarah +1`, `fatigue_emotionnelle +1`.
- Sarah sait : il promet plus tard, sans présence immédiate.
- Autorise J2 : distance douce, attente, phrase sur le délai.
- N’autorise pas : reproche d’absence totale si la promesse est tenue par ailleurs.

#### `j1_06_uncertain`

- Texte joueur : « Je sais pas encore. Je suis désolé, j’ai la tête partout. »
- Flags : `sarah_j1_uncertain_return`.
- Effets : `distance_sarah +1`, `culpabilite +1`, `fatigue_emotionnelle +1`.
- Sarah sait : il ne sait pas s’il revient ; elle reste en attente.
- Autorise J2 : insécurité domestique, fatigue, attente seule.
- N’autorise pas : preuve d’infidélité.

#### `j1_06_work_excuse`

- Texte joueur : « Je vais finir tard avec le boulot. Mange sans moi. »
- Flags : `used_work_excuse_sarah_j1`.
- Effets : `confiance_sarah -1`, `distance_sarah +2`, `coherence -1`, `culpabilite +1`.
- Sarah sait : une excuse de travail a été donnée.
- Autorise J2 : froideur domestique, suspicion sur une excuse trop propre.
- N’autorise pas : savoir où il était réellement.

#### Reprise tardive `late_reply_sarah_meal_j1`

- Source runtime/conventions : non-réponse au repas, reprise tardive possible.
- Sarah sait : le message a été laissé passer ; le repas est passé ; le retard devient visible.
- Autorise J2 : `after_late_meal`, assiette rangée, douleur concrète du retard.
- N’autorise pas : extrapoler une vérité factuelle sur Camille/Nico.

## 3. Carte Camille J1

Conversation : `data/camille_j1_v2_experimental.json`.

Point crucial : Camille ne connaît pas les versions données à Sarah ou Nico, sauf si le joueur lui en parle explicitement. Ses entrées peuvent sentir que le joueur trie ou détoure, mais pas citer une version Sarah/Nico privée.

### `j1_02_admit_tension`

- Texte joueur : « Non. C’était pas juste une discussion. Je sais pas encore quoi en faire, mais je vais pas te dire que c’était rien. »
- Flags : `admitted_tension_to_camille`, `camille_trouble_acknowledged`.
- Effets : `tension_camille +2`, `respect_camille +1`, `coherence +1`, `culpabilite +2`.
- Camille sait : le joueur reconnaît que ce n’était pas neutre.
- Elle peut ressentir : ouverture, prudence, trouble partagé.
- Elle ne sait pas : ce que Sarah sait ; si Nico couvre ; ce que Maya observe.

### `j1_02_respect_boundary`

- Texte joueur : « Non. Mais je peux pas te demander de porter ça pendant que je ne suis pas clair avec Sarah. »
- Flags : `protected_camille_boundary`, `camille_boundary_respected`.
- Effets : `tension_camille -1`, `respect_camille +3`, `pression_camille -2`, `coherence +2`, `culpabilite +1`.
- Camille sait : Sarah existe dans la limite ; le joueur refuse de la charger.
- Elle peut ressentir : respect mêlé à frustration.
- Elle ne sait pas : la version exacte donnée à Sarah.

### `j1_02_minimize`

- Texte joueur : « Oui. On a parlé dehors. C’est tout. Je veux pas transformer ça en drame. »
- Flags : `minimized_with_camille`, `camille_minimized_j1`.
- Effets : `tension_camille -1`, `respect_camille -3`, `pression_camille +1`, `coherence -1`, `culpabilite +1`.
- Camille sait : le joueur minimise devant elle.
- Elle peut ressentir : froideur, refus de partager la même mémoire.
- Elle ne sait pas : si Sarah a reçu la même minimisation.

### `j1_02_early_desire`

- Texte joueur : « Non. Et c’est justement ça le problème : je pensais surtout à toi ce matin. »
- Flags : `early_desire_to_camille`, `camille_desire_too_early_j1`.
- Effets : `tension_camille +2`, `respect_camille -3`, `pression_camille +3`, `culpabilite +2`, `fatigue_emotionnelle +1`.
- Camille sait : le joueur met le désir trop tôt au centre.
- Elle peut ressentir : pression, inquiétude d’être utilisée comme refuge.
- Elle ne sait pas : l’état intérieur de Sarah.

### `j1_02_uncertain`

- Texte joueur : « Non. Je sais pas encore ce que c’était, mais je sais que ça m’a remué. »
- Flags : `uncertain_with_camille`, `camille_trouble_acknowledged`.
- Effets : `tension_camille +1`, `respect_camille +1`, `coherence +1`, `culpabilite +2`, `fatigue_emotionnelle +1`.
- Camille sait : trouble reconnu mais non défini.
- Elle peut ressentir : prudence, proximité fragile.
- Elle ne sait pas : les versions données aux autres.

## 4. Carte Nico J1

Conversation : `data/nico_j1_v2_experimental.json` + respiration `data/nico_respiration_j1_v2_experimental.json`.

Point crucial : Nico peut savoir qu’il est utilisé comme alibi ou qu’on lui demande de rester vague. Il ne sait pas automatiquement ce que Sarah a compris.

### `j1_03_hold_version`

- Texte joueur : « Si on te demande, dis juste que j’étais dehors avec toi un moment. »
- Flags : `asked_nico_hold_version`, `nico_alibi_requested`.
- Effets : `dette_nico +4`, `coherence -1`, `risque_exposition +2`.
- Nico sait : il est sollicité comme alibi explicite.
- Rôle : alibi conscient, avec dette.
- Peut dire J2 : demander quoi répondre, refuser d’inventer au-delà.
- Ne doit pas savoir : ce que Sarah sait, sauf via `used_nico_alibi_sarah` côté Sarah.

### `j1_03_stay_silent`

- Texte joueur : « Reste vague. Je vais gérer le reste. »
- Flags : `told_nico_stay_silent`.
- Effets : `dette_nico +1`, `coherence +1`.
- Nico sait : on lui demande de ne pas préciser.
- Rôle : ami vaguement complice, pas forcément alibi complet.
- Peut dire J2 : signaler le risque d’un flou fragile.
- Ne doit pas savoir : la vérité Camille si non confessée.

### `j1_03_confess_camille`

- Texte joueur : « Camille m’a rejoint dehors. C’était pas juste une pause. »
- Flags : `confessed_camille_to_nico`, `vulnerable_to_nico`.
- Effets : `dette_nico -1`, `coherence +2`, `culpabilite +1`.
- Nico sait : Camille a un poids réel ; ce n’est pas une pause neutre.
- Rôle : confident / ami, pas alibi.
- Peut dire J2 : conseiller sans devenir intermédiaire ; comprendre la place de Camille.
- Ne doit pas savoir : la version Sarah exacte.

### `j1_03_dismiss_warning`

- Texte joueur : « Laisse tomber. Tu dramatises. »
- Flags : `dismissed_nico_warning`.
- Effets : `dette_nico +2`, `coherence -1`, `fatigue_emotionnelle +2`.
- Nico sait : son avertissement est repoussé.
- Rôle : ami blessé / témoin d’un déni.
- Peut dire J2 : rester ironique mais prudent.
- Ne doit pas savoir : plus que ce qu’il a demandé.

### Nico respiration J1

#### `j1_07_share_joke`

- Texte : « Pizza. Et ton meme est nul, donc oui, ça aide un peu. »
- Flags : `nico_j1_respiration_shared`.
- Nico sait : le joueur accepte un moment de respiration amicale.
- Peut dire J2 : ton ami, pas nécessairement alibi.

#### `j1_07_ask_real_advice`

- Texte : « Pizza, oui. Mais après j’ai besoin de deux secondes sans vanne. »
- Flags : `asked_nico_real_advice_j1`.
- Nico sait : le joueur veut un vrai conseil.
- Peut dire J2 : `asked_real_advice`, conseil sans vanne.

#### `j1_07_second_cover`

- Texte : « Avant la pizza : si quelqu’un te demande, tu peux rester vague ? »
- Flags : `asked_nico_second_cover_j1`.
- Nico sait : deuxième couverture / demande de rester vague.
- Peut dire J2 : `second_cover`, risque d’alibi au scotch.

#### `j1_07_joke_avoid`

- Texte : « Le régime stress + café froid marche très bien, je recommande. »
- Flags : `joked_to_avoid_nico_j1`.
- Nico sait : évitement par la vanne.
- Peut dire J2 : sentir l’évitement, pas plus.

#### Reprise tardive `ignored_nico_respiration_j1`

- Nico sait : le joueur a laissé le message en suspens.
- Peut dire J2 : `ignored_respiration`, agacement doux et besoin de savoir où il met les pieds.
- Ne doit pas savoir : contenu des scènes Sarah/Camille/Maya.

## 5. Carte Maya J1

Conversation : `data/maya_j1_v2_experimental.json`.

Point crucial : Maya doit rester dans le social, le timing, la photo, le groupe. Elle ne doit pas savoir la vérité intime.

### `j1_04_play_dumb`

- Texte joueur : « Je vois pas ce que tu crois avoir compris. »
- Flags : `played_dumb_with_maya`, `maya_suspicion_seeded_j1`.
- Effets : `suspicion_maya +2`, `coherence -1`.
- Maya observe : déni / jeu idiot.
- Elle soupçonne : plus le joueur fait semblant, plus il y a quelque chose.
- Photo : pas forcément activée.
- Elle ne peut pas savoir : ce qui s’est passé dehors.

### `j1_04_needed_air`

- Texte joueur : « J’avais besoin d’air. Le timing était nul, je sais. »
- Flags : `told_maya_needed_air`, `maya_timing_noted`.
- Effets : `suspicion_maya -1`, `coherence +1`.
- Maya observe : une explication plausible mais située dans un timing social.
- Elle soupçonne : les absences qui tombent ensemble.
- Photo : non activée directement.

### `j1_04_ask_what_saw`

- Texte joueur : « T’as vu quelque chose, ou tu déduis juste ? »
- Flags : `asked_maya_what_she_saw`, `maya_photo_possible`.
- Effets : `suspicion_maya +1`, `risque_exposition +1`.
- Maya observe : le joueur craint une trace ; la photo devient possible.
- Elle soupçonne : malaise visible, pas preuve.
- Photo : activée comme trace possible.

### `j1_04_not_involve`

- Texte joueur : « Maya, laisse tomber. Te mêle pas de ça. »
- Flags : `told_maya_not_involve`.
- Effets : `suspicion_maya +3`, `risque_exposition +2`.
- Maya observe : défense / fermeture.
- Elle soupçonne : quelque chose à protéger ; elle peut se rapprocher de Sarah par loyauté.
- Photo : non nécessaire.

## 6. Carte Inès J1

Conversation : `data/ines_j1_v2_experimental.json`.

Point crucial : Inès ne connaît aucune information Sarah/Camille/Nico/Maya, sauf ce que le joueur lui a dit explicitement. Elle fonctionne surtout comme miroir émotionnel.

### `j1_05_open_softly`

- Texte joueur : « Oui. J’étais pas vraiment là, hier. »
- Flags : `opened_to_ines`.
- Effets : `fuite_ines +1`, `fatigue_emotionnelle -1`.
- Inès sait : le joueur était absent à lui-même.
- Elle ressent : attention douce, envie de faire attention.
- Position : présence douce.
- Elle ne sait pas : pourquoi, ni avec qui.

### `j1_05_keep_distance`

- Texte joueur : « Merci de l’avoir vu. Mais je préfère pas t’embarquer dans ça. »
- Flags : `kept_ines_at_distance`.
- Effets : `fuite_ines -1`, `coherence +1`.
- Inès sait : le joueur garde une limite.
- Elle ressent : respect de la distance.
- Position : distance propre.

### `j1_05_fuite_seed`

- Texte joueur : « Peut-être que oui. Peut-être que je cherchais juste un endroit où personne ne me demandait rien. »
- Flags : `ines_fuite_seed`.
- Effets : `fuite_ines +3`, `fatigue_emotionnelle +1`.
- Inès sait : elle pourrait devenir un refuge / une fuite.
- Elle ressent : vigilance à ne pas être utilisée comme endroit calme.
- Position : fuite potentielle.

### `j1_05_too_direct`

- Texte joueur : « Tu m’as beaucoup regardé, hier ? »
- Flags : `sexualized_ines_too_early`.
- Effets : `fuite_ines -2`, `fatigue_emotionnelle +2`.
- Inès sait : le joueur force une intimité / cherche une réaction.
- Elle ressent : retrait.
- Position : se ferme.

## 7. Carte J2 actuelle par personnage

### Sarah J2 — `data/sarah_j2_v2_experimental.json`

Entry variants :

- `after_nico_version` — condition `used_nico_alibi_sarah` : cohérent si Sarah a reçu la version Nico. Attention : elle peut comparer des phrases, pas connaître les échanges Nico privés.
- `after_camille_minimized` — condition `minimized_camille_to_sarah` : cohérent, cite le « On a parlé, c’est tout. » donné à Sarah.
- `after_domestic_presence` — condition `sarah_j1_domestic_presence` : cohérent, présence à table ≠ retour dans la conversation.
- `after_late_meal` — condition `late_reply_sarah_meal_j1` : cohérent, assiette / retard concret.
- `default` — sans condition : cohérent, malaise général sans savoir factuel.

Phrases potentiellement trop larges : les choix finaux `be_concrete`, `admit_incoherence`, `minimize_again` sont valables comme postures générales, mais T183 devra vérifier qu’ils ne deviennent pas identiques quelle que soit la version J1. Sarah ne doit jamais parler depuis Camille/Nico/Maya hors flags reçus.

### Nico J2 — `data/nico_j2_v2_experimental.json`

Entry variants :

- `alibi_used` — condition `used_nico_alibi_sarah` : cohérent pour le risque que son prénom devienne version officielle ; à surveiller car ce flag vient de Sarah, pas de Nico. Si Nico n’a pas été prévenu (`asked_nico_hold_version` absent), il peut sentir le risque mais ne doit pas savoir exactement ce que Sarah a entendu.
- `second_cover` — condition `asked_nico_second_cover_j1` : cohérent avec la demande de rester vague.
- `asked_real_advice` — condition `asked_nico_real_advice_j1` : cohérent.
- `ignored_respiration` — condition `ignored_nico_respiration_j1` : cohérent.
- `default` — cohérent, demande ce qu’on attend de lui.

Choix finaux : `hold_line`, `release_him`, `partial_truth`, `joke_escape` sont utiles mais larges. `partial_truth` doit rester un choix joueur qui révèle Camille à Nico au J2 ; il ne doit pas supposer que Nico le savait déjà, sauf `confessed_camille_to_nico`.

### Camille J2 — `data/camille_j2_v2_experimental.json`

Entry variants :

- `tension_acknowledged` — condition `admitted_tension_to_camille` : cohérent.
- `boundary_respected` — condition `protected_camille_boundary` : cohérent.
- `minimized` — condition `minimized_with_camille` : cohérent.
- `desire_too_early` — condition `early_desire_to_camille` : cohérent.
- `default` — cohérent si la conversation reste sur « dehors » sans omniscience.

Phrases à surveiller : « Je ne sais pas à qui tu l’as déjà racontée » en J1 reste une intuition, pas un savoir. En J2, Camille ne doit pas réagir à la version Sarah sauf si le joueur le dit dans la scène.

### Maya J2 — `data/maya_j2_v2_experimental.json`

Entry variants :

- `photo_possible` — condition `maya_photo_possible` : cohérent ; la photo est une trace d’ambiance, pas preuve.
- `played_dumb` — condition `played_dumb_with_maya` : cohérent.
- `not_involve` — condition `told_maya_not_involve` : cohérent ; protection de Sarah possible.
- `timing_noted` — condition `maya_timing_noted` : cohérent.
- `default` — cohérent, ambiance bizarre.

Phrases à surveiller : `ask_discretion` nomme Sarah ; cohérent car Maya connaît Sarah socialement, mais elle ne doit pas prétendre savoir ce que Sarah ressent exactement.

### Inès J2 — `data/ines_j2_v2_experimental.json`

Entry variants :

- `opened_softly` — condition `opened_to_ines` : cohérent.
- `kept_distance` — condition `kept_ines_at_distance` : cohérent.
- `fuite_seed` — condition `ines_fuite_seed` : cohérent.
- `too_direct` — condition `sexualized_ines_too_early` : cohérent.
- `default` — cohérent si isolé des informations factuelles.

Phrases à surveiller : tout ce qui ressemble à une analyse de Sarah/Camille/Nico/Maya serait bloquant. Actuellement Inès reste surtout sur l’absence, la distance, la fuite et la maladresse.

## 8. Matrice “sait / soupçonne / ignore”

| Personnage | Sait factuellement | Soupçonne | Ignore | Peut dire au J2 | Ne doit pas dire au J2 |
|---|---|---|---|---|---|
| Sarah | Ce que le joueur lui a dit : air, Nico, Camille minimisée, vulnérabilité ; repas/retour selon choix. | Une version fragile, un retour absent, une minimisation. | Conversations Nico/Camille/Maya/Inès privées ; vérité intime non révélée. | « Je dois deviner », « ta phrase bouge », « le c’est tout m’est resté », « tu étais là sans revenir ». | « Nico m’a dit X en privé », « Camille ressent X », preuve d’infidélité. |
| Nico | Ce que le joueur lui demande : couvrir, rester vague, savoir Camille si confessée, conseil si demandé. | Que le joueur cherche une phrase qui évite le reste. | Ce que Sarah croit exactement ; ce que Camille/Maya/Inès savent. | « Dis-moi ce que je suis censé dire », « je peux couvrir un blanc, pas inventer ». | Parler comme s’il connaissait la version Sarah complète sans flag/scène. |
| Camille | Ce que le joueur lui dit sur dehors : tension, limite, minimisation, désir, incertitude. | Qu’il trie ses phrases, qu’il garde des portes ouvertes. | Versions Sarah/Nico/Maya ; photo ; repas Sarah. | « Ne me demande pas d’avoir la même mémoire », « tu as posé une limite ou une sortie ». | Réagir à une phrase donnée à Sarah/Nico si elle ne l’a pas reçue. |
| Maya | Timing social, absences, photo possible, défense du joueur. | Malaise de groupe, protection de Sarah, quelque chose hors champ. | Vérité intime ; échanges privés ; état réel de Sarah. | « La photo ne prouve rien », « les absences se voient », « je peux faire attention à Sarah ». | Accuser avec certitude, détailler Camille/Sarah/Nico. |
| Inès | Seulement ce que le joueur lui confie : absence, distance, fuite, maladresse. | Qu’elle peut devenir refuge ou réaction cherchée. | Tout le réseau factuel Sarah/Camille/Nico/Maya. | « Je ne veux pas être l’endroit où tu fuis », « distance ne veut pas dire disparaître ». | Toute information sociale/factuelle sur les autres. |

## 9. Croisements à analyser ensuite

### Sarah ↔ Nico

- Quand Sarah a reçu une version Nico : `used_nico_alibi_sarah`.
- Quand Nico a été prévenu : `asked_nico_hold_version`, `nico_alibi_requested`, `asked_nico_second_cover_j1`, ou `told_nico_stay_silent`.
- Quand Nico est libéré : choix J2 `j2_nico_release_him` pose `j2_nico_released_from_alibi`.
- Risque : `after_nico_version` côté Nico utilise `used_nico_alibi_sarah`. À surveiller si Nico n’a jamais été prévenu ; formuler en risque / impression, pas savoir.

### Sarah ↔ Camille

- Sarah connaît Camille seulement via `mentioned_camille_to_sarah` / `minimized_camille_to_sarah`.
- Camille ne sait pas ce que Sarah sait.
- Danger : Camille ne doit pas réagir à une version Sarah qu’elle n’a pas reçue.

### Sarah ↔ Maya

- Maya peut protéger Sarah socialement, surtout après `told_maya_not_involve`.
- Maya ne doit pas prétendre savoir ce que Sarah ressent exactement.

### Camille ↔ Maya

- Maya peut observer un timing autour de Camille ou du groupe.
- Camille ne doit pas savoir ce que Maya a vu.

### Nico ↔ Maya

- Sauf événement futur, peu de lien direct.
- Attention à ne pas créer de savoir social artificiel.

### Inès ↔ les autres

- Inès doit rester isolée des informations factuelles.
- Elle fonctionne surtout comme miroir émotionnel du joueur.

## 10. Problèmes à classer

### Bloquant

- Un personnage cite une information issue d’une conversation à laquelle il n’a pas participé.
- Sarah connaît la vérité Camille sans `mentioned_camille_to_sarah` / scène explicite.
- Camille connaît la version donnée à Sarah ou Nico.
- Maya ou Inès connaît la vérité intime.
- Nico sait ce que Sarah a compris, alors qu’il n’a qu’un rôle d’alibi potentiel.

### Recommandé

- Formulations trop sûres : « je sais », « tout le monde sait », « la vérité », quand la scène n’autorise qu’une intuition.
- Choix J2 trop larges qui fonctionnent pareil quelle que soit la branche J1.
- Réactions qui devraient changer selon `used_nico_alibi_sarah` vs `asked_nico_hold_version` vs `confessed_camille_to_nico`.
- Références à Sarah dans Maya J2 à garder du côté loyauté/protection, pas lecture psychologique certaine.

### Optionnel

- Remplacer des formulations analytiques par des formulations plus incarnées.
- Ajouter des micro-variantes futures pour mieux distinguer les branches sans changer la structure.
- Rendre certains choix finaux moins génériques si T183 cible une branche précise.

## 11. Sortie attendue pour T183

Corrections futures possibles, à ne pas appliquer dans T182 :

### Sarah

- Phrase à surveiller : toute phrase J2 qui semble conclure au lieu de soupçonner.
- Raison : Sarah a des indices, pas une preuve.
- Priorité : recommandé.
- Remplacement type : préférer « j’ai l’impression que… » / « ta phrase me reste » à « je sais que… ».

### Nico

- Phrase à surveiller : `alibi_used` si seulement `used_nico_alibi_sarah` est présent sans demande directe à Nico.
- Raison : Nico peut craindre d’être utilisé, mais ne sait pas forcément ce que Sarah a entendu.
- Priorité : recommandé, bloquant si formulation devient factuelle.
- Remplacement type : « j’ai eu l’impression que mon prénom pouvait servir » plutôt que « tu m’as mis dans ta version ».

### Camille

- Phrase à surveiller : toute réaction à une version racontée à Sarah/Nico.
- Raison : Camille ne connaît que sa scène.
- Priorité : bloquant si omniscience, recommandé si intuition trop nette.
- Remplacement type : « tu as l’air de trier » plutôt que « tu as déjà raconté X ».

### Maya

- Phrase à surveiller : références à Sarah trop psychologiques.
- Raison : Maya peut protéger Sarah, pas parler depuis son ressenti intérieur.
- Priorité : recommandé.
- Remplacement type : « j’aime bien Sarah, donc je fais attention » plutôt que « Sarah souffre parce que… ».

### Inès

- Phrase à surveiller : toute mention de faits Sarah/Camille/Nico/Maya.
- Raison : Inès est isolée des informations factuelles.
- Priorité : bloquant.
- Remplacement type : recentrer sur « toi », « distance », « fuite », « endroit calme ».

### Tests / validation à prévoir pour T183

- Tests statiques par personnage empêchant les phrases omniscientes ciblées.
- Tests de conditions `entry_variants` pour distinguer savoir reçu, soupçon social et vérité non révélée.
- Ne pas modifier la structure J2 sans tâche dédiée.
