# T199 — Audit oralité / naturel des dialogues J3 V2

Document de relecture pour le polish J3 V2. Objectif : identifier les lignes qui risquent de sonner trop écrites, analytiques ou longues en lecture messagerie, sans modifier le runtime.

## Périmètre

- `data/sarah_j3_v2_experimental.json` — 55 nodes, 55 messages, 9 choix, longueur moyenne ≈ 9.4 mots/message
- `data/camille_j3_v2_experimental.json` — 55 nodes, 55 messages, 9 choix, longueur moyenne ≈ 9.0 mots/message
- `data/maya_j3_v2_experimental.json` — 55 nodes, 55 messages, 9 choix, longueur moyenne ≈ 8.6 mots/message
- `data/nico_j3_v2_experimental.json` — 55 nodes, 55 messages, 9 choix, longueur moyenne ≈ 8.1 mots/message
- `data/ines_j3_v2_experimental.json` — 55 nodes, 55 messages, 9 choix, longueur moyenne ≈ 9.3 mots/message

## Synthèse GO / NO GO

**GO contenu** : J3 V2 est jouable et les voix sont distinctes. Le polish nécessaire est surtout micro-oralité : raccourcir quelques phrases, casser les formulations trop explicatives, et préserver les tics propres à chaque contact.

**NO GO pour une refonte lourde** : aucun fichier ne demande une réécriture structurelle avant playtest. Les risques repérés sont localisés.

## Points d’attention transverses

- Éviter les phrases qui expliquent l’émotion au lieu de la laisser passer dans le rythme.
- Préférer 2 bulles courtes à 1 bulle longue quand la ligne dépasse ~22 mots.
- Garder les réponses joueur simples : moins de justification, plus de réaction immédiate.
- Ne pas lisser Nico/Inès : leur naturel vient aussi des ruptures et de l’imperfection.

## Sarah — `sarah_j3_v2_experimental.json`

Voix attendue : quotidien conjugal, chaleur sous fatigue, inquiétude indirecte. À surveiller : ne pas rendre Sarah trop “diagnostic”.

- Longueur moyenne : **9.4 mots/message**.
- Lignes longues repérées : **5** dans l’échantillon automatique.
- Formulations potentiellement analytiques repérées : **5** dans l’échantillon automatique.

### Exemples à relire pour longueur / respiration

- `j3_01_sarah_entry_fragile_004` **** : Je crois que j’ai moins besoin d’une version parfaite que d’une présence qui ne se sauve pas dès qu’elle tremble.
- `j3_01_sarah_003` **** : Et puis j’ai trouvé ça triste de me demander si j’avais le droit de prendre de la place dès le matin.
- `j3_01_sarah_player_show_with_actions` **** : Tu as raison. Aujourd’hui, je veux arrêter de te répondre seulement avec des phrases. Je vais te le montrer dans les gestes.
- `j3_01_sarah_player_honest_uncertainty` **** : Je veux que tu aies une vraie place. Mais je ne veux pas te promettre une clarté que je n’ai pas encore complètement.
- `j3_01_sarah_player_ask_more_time` **** : Je sais que ça te pèse. Mais j’ai encore besoin d’un peu de temps pour ne pas te répondre de travers.

### Exemples à relire pour naturel / sous-texte

- `j3_01_sarah_entry_minimized_002` **** : Mais je crois que j’ai besoin de te dire une chose.
- `j3_01_sarah_entry_minimized_003` **** : Quand tu appelles ça “une soirée bizarre”, j’ai l’impression que tu ranges aussi ce que moi j’ai senti.
- `j3_01_sarah_entry_fragile_004` **** : Je crois que j’ai moins besoin d’une version parfaite que d’une présence qui ne se sauve pas dès qu’elle tremble.
- `j3_01_sarah_response_uncertainty_003` **** : Je crois que je peux faire quelque chose avec ça.
- `j3_01_sarah_player_defensive` **** : J’ai l’impression que quoi que je dise, ça devient une preuve que je fais mal.

### Verdict polish

- Priorité : **P1** — passer une coupe longueur sur les bulles les plus explicatives.

## Camille — `camille_j3_v2_experimental.json`

Voix attendue : lucidité, détour, tension contenue. À surveiller : réduire les formulations trop littéraires si elles cassent la messagerie.

- Longueur moyenne : **9.0 mots/message**.
- Lignes longues repérées : **2** dans l’échantillon automatique.
- Formulations potentiellement analytiques repérées : **4** dans l’échantillon automatique.

### Exemples à relire pour longueur / respiration

- `j3_03_camille_player_recognize_without_using` **** : Je ne veux pas effacer ce moment. Mais je ne veux pas non plus t’utiliser pour sortir de ce que je n’arrive pas à régler ailleurs.
- `j3_03_camille_player_keep_boundary` **** : Je crois qu’il faut encore garder une limite. Pas pour nier ce qu’il y a, mais pour ne pas te faire porter ma confusion.

### Exemples à relire pour naturel / sous-texte

- `j3_03_camille_entry_refuge_003` **** : Ou peut-être que tu l’as dit exactement comme tu le ressentais.
- `j3_03_camille_001` **** : Je ne sais pas si je devrais rouvrir le sujet du dehors.
- `j3_03_camille_player_reopen_tension` **** : Oui, j’y pense encore. Et je crois que j’ai envie de savoir ce que ça pourrait devenir.
- `j3_03_camille_response_pressure_001` **** : Je crois que tu confonds encore deux choses.

### Verdict polish

- Priorité : **P2** — garder pour playtest, retoucher seulement si une ligne accroche à la lecture.

## Maya — `maya_j3_v2_experimental.json`

Voix attendue : observation sociale piquante, énergie de groupe, humour. À surveiller : garder le mordant sans transformer chaque message en punchline.

- Longueur moyenne : **8.6 mots/message**.
- Lignes longues repérées : **0** dans l’échantillon automatique.
- Formulations potentiellement analytiques repérées : **0** dans l’échantillon automatique.

### Verdict polish

- Priorité : **P2** — garder pour playtest, retoucher seulement si une ligne accroche à la lecture.

## Nico — `nico_j3_v2_experimental.json`

Voix attendue : pote oral, vanne, sas comique, limite amicale claire. À surveiller : ne pas trop expliquer la fonction de confident.

- Longueur moyenne : **8.1 mots/message**.
- Lignes longues repérées : **2** dans l’échantillon automatique.
- Formulations potentiellement analytiques repérées : **2** dans l’échantillon automatique.

### Exemples à relire pour longueur / respiration

- `j3_02_nico_player_ask_more_help` **** : J’ai encore besoin que tu m’aides un peu. Pas pour mentir, juste pour éviter que ça parte dans tous les sens.
- `j3_02_nico_player_sarah_observes` **** : Sarah observe tout maintenant. Même quand elle ne pose pas de question, j’ai l’impression qu’elle regarde si mes gestes tiennent.

### Exemples à relire pour naturel / sous-texte

- `j3_02_nico_004` **** : mais je crois que je vais avoir une journée moins disponible que prévu.
- `j3_02_nico_player_sarah_observes` **** : Sarah observe tout maintenant. Même quand elle ne pose pas de question, j’ai l’impression qu’elle regarde si mes gestes tiennent.

### Verdict polish

- Priorité : **P2** — garder pour playtest, retoucher seulement si une ligne accroche à la lecture.

## Inès — `ines_j3_v2_experimental.json`

Voix attendue : marge, perception, flottement. À surveiller : rester mystérieuse sans devenir opaque.

- Longueur moyenne : **9.3 mots/message**.
- Lignes longues repérées : **3** dans l’échantillon automatique.
- Formulations potentiellement analytiques repérées : **6** dans l’échantillon automatique.

### Exemples à relire pour longueur / respiration

- `j3_05_ines_player_clear_presence` **** : Je veux être là clairement. Pas pour fuir le reste, et pas pour te demander de porter ce que je n’ai pas réglé.
- `j3_05_ines_player_keep_soft_distance` **** : Je crois qu’il faut qu’on garde quelque chose de doux, mais à distance. Je ne veux pas mélanger plus que je ne comprends.
- `j3_05_ines_player_step_back` **** : Je crois que je devrais prendre un peu de recul. Pas contre toi. Pour éviter de te mettre dans quelque chose qui me dépasse.

### Exemples à relire pour naturel / sous-texte

- `j3_05_ines_entry_careful_003` **** : je crois que c’est pour ça que je te réponds ce soir.
- `j3_05_ines_entry_repair_001` **** : je crois que ta phrase d’hier m’a aidée.
- `j3_05_ines_002` **** : parce que je crois que parfois, on peut être présent sans prendre toute la place.
- `j3_05_ines_response_clear_presence_002` **** : je crois que j’avais besoin de cette précision.
- `j3_05_ines_player_seek_refuge_again` **** : J’ai encore besoin de calme ce soir. Avec toi, j’ai l’impression que le bruit baisse.

### Verdict polish

- Priorité : **P2** — garder pour playtest, retoucher seulement si une ligne accroche à la lecture.

## Checklist de correction proposée

1. Relire les IDs listés ci-dessus dans le flux Godot, pas isolés.
2. Pour chaque ligne longue : couper, supprimer une justification, ou remplacer par une réaction plus orale.
3. Pour chaque ligne analytique : transformer “je crois/j’ai l’impression” en geste, vanne, silence ou image concrète.
4. Revalider avec `python3 tools/validate_j1_v2_experimental.py`.

## Conclusion

T199 peut être considéré comme un audit documentaire : aucune donnée runtime n’a été modifiée. Le prochain ticket utile serait un polish ciblé des IDs relevés après playtest ou relecture humaine.
