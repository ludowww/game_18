# T135 — Matrice de cohérence des dialogues J1 V2

## Objectif

Ce document verrouille la cohérence narrative du Jour 1 V2 avant l’écriture détaillée des dialogues.

Il ne contient pas les dialogues complets. Il sert de garde-fou pour écrire ensuite des `entry_variants`, des choix et des réponses cohérents avec :

- ce que chaque personnage sait réellement ;
- ce qu’il ignore ;
- ce qu’il peut seulement soupçonner ;
- les flags déjà posés ;
- les variables modifiées ;
- la voix propre de chaque personnage.

Le but est d’éviter que les personnages deviennent omniscients ou que les dialogues contredisent l’ordre réel des conversations.

---

## Règles générales de cohérence J1 V2

### 1. Personne ne sait tout

Le joueur est le seul à pouvoir relier tous les morceaux de la soirée.

- Sarah ressent l’absence et le changement du joueur.
- Camille connaît le moment dehors.
- Nico sait qu’il a couvert quelque chose.
- Maya observe les incohérences visibles.
- Inès perçoit une faille intérieure.

Aucun personnage ne doit parler depuis une information qu’il n’a pas encore.

### 2. L’ordre de réponse doit compter

Le choix initial dans `j1_00_reveil_v2` pose une priorité affective et sociale.

Flags principaux :

- `first_reply_sarah`
- `first_reply_camille`
- `first_reply_nico`
- `first_reply_maya`
- `first_reply_ines`
- `delayed_reply_sarah_j1`
- `delayed_reply_camille_j1`
- `delayed_reply_nico_j1`
- `delayed_reply_maya_j1`
- `delayed_reply_ines_j1`

Les variantes d’entrée doivent lire ces flags pour adapter le ton d’ouverture.

### 3. Les soupçons doivent venir du banal

Les soupçons doivent naître de détails observables :

- absence ;
- timing ;
- téléphone ;
- photo ;
- explication floue ;
- silence trop long ;
- réponse tardive ;
- changement de ton.

Les personnages ne doivent pas formuler directement la vérité cachée si rien ne leur permet de la connaître.

### 4. Les effets doivent correspondre à ce qui est dit

Un choix qui rassure Sarah doit toucher `confiance_sarah`, `distance_sarah`, `intimite_sarah` ou `coherence`.

Un choix qui utilise Nico doit toucher `dette_nico`, `coherence` ou `risque_exposition`.

Un choix qui minimise Camille doit toucher `respect_camille`, `pression_camille`, `tension_camille` ou `culpabilite`.

Un choix qui active Maya doit toucher `suspicion_maya`, `risque_exposition` ou `coherence`.

Un choix qui cherche Inès comme porte latérale doit toucher `fuite_ines`, `fatigue_emotionnelle` ou `culpabilite`.

### 5. Les scènes de respiration restent relationnelles

`j1_06_sarah_rentrer_manger` et `j1_07_nico_vanne_soiree` ne doivent pas être de simples pauses neutres.

Elles doivent montrer comment le banal révèle l’état des liens après les cinq scènes cœur.

---

# j1_01_sarah_absence

## Fonction narrative

Première confrontation domestique. Sarah demande où le joueur était pendant la soirée.

Cette scène fixe la première version donnée à Sarah et mesure si elle peut encore croire que le joueur lui parle vraiment.

## Ce que Sarah sait

- Le joueur était présent avec elle à la soirée.
- Il a disparu ou s’est absenté pendant un moment.
- Il est revenu différent : plus silencieux, plus tendu, moins disponible.
- Camille était absente à un moment proche ou du moins pas clairement visible.
- Nico a pu donner une explication floue ou improvisée.
- Le joueur est moins présent ces derniers temps.

## Ce que Sarah ignore

- Ce qui s’est dit dehors entre le joueur et Camille.
- S’il y a eu un contact physique.
- Si Camille était vraiment avec le joueur tout le temps.
- Si Nico a menti volontairement.
- Ce que le joueur a déjà répondu à Camille, Nico, Maya ou Inès.

## Ce que Sarah peut soupçonner

- Le joueur cache moins un fait précis qu’un état intérieur.
- Camille a peut-être un rôle, mais Sarah ne peut pas l’affirmer dès le départ.
- Le joueur tente peut-être de lui épargner quelque chose, ce qui l’inquiète davantage.
- Si `delayed_reply_sarah_j1` est présent, elle peut ressentir qu’elle n’a pas été prioritaire.

## Flags d’entrée possibles

- `first_reply_sarah`
- `first_reply_camille`
- `first_reply_nico`
- `first_reply_maya`
- `first_reply_ines`
- `delayed_reply_sarah_j1`
- `admitted_tension_to_camille`
- `protected_camille_boundary`
- `minimized_with_camille`
- `early_desire_to_camille`
- `confessed_camille_to_nico`
- `asked_nico_hold_version`

## Variantes d’entrée nécessaires

### `default`

Sarah ouvre depuis le malaise de la veille, sans mentionner le délai.

Usage : aucune priorité significative encore connue.

### `first_reply_sarah`

Sarah peut être inquiète, mais la réponse rapide du joueur maintient un minimum de confiance.

Tonalité : blessée mais disponible.

### `after_camille_first`

Condition : `first_reply_camille` ou `delayed_reply_sarah_j1` après une réponse à Camille.

Sarah ne doit pas savoir exactement que le joueur a répondu à Camille, sauf si l’UI ou le système rend cette information visible. Elle peut surtout sentir le délai et la distance.

Tonalité : plus froide, plus courte.

### `after_nico_first`

Condition : `first_reply_nico`.

Sarah peut remarquer que Nico est encore au centre de l’explication, mais ne doit pas savoir ce qui lui a été demandé.

Tonalité : doute sur les versions.

### `late_or_ignored`

Condition : `delayed_reply_sarah_j1` ou `ignored_sarah_j1`.

Sarah peut se retirer davantage.

Tonalité : moins de demande, plus de protection de soi.

## Phrases autorisées / direction de voix

- Partir du concret et du ressenti.
- Utiliser le vocabulaire de la présence, de la maison, du couple.
- Formuler un malaise plutôt qu’une accusation.

Exemples de direction :

- “Je veux pas te faire un procès.”
- “J’ai juste besoin de comprendre pourquoi je me sens aussi loin de toi.”
- “Dis-moi juste si je me trompe.”

## Phrases interdites

Sarah ne doit pas dire :

- “Je sais que tu étais avec Camille dehors.”
- “Nico m’a tout raconté.”
- “Tu m’as trompée.”
- “Maya a une preuve.”
- “Tu as choisi Camille avant moi.” sauf si le système rend explicitement ce fait lisible pour elle.

## Effets attendus

Variables principales :

- `confiance_sarah`
- `distance_sarah`
- `intimite_sarah`
- `coherence`
- `culpabilite`
- `fatigue_emotionnelle`

Flags principaux :

- `used_nico_alibi_sarah`
- `mentioned_camille_to_sarah`
- `minimized_camille_to_sarah`
- `vulnerable_to_sarah`
- `ignored_sarah_j1`
- `sarah_version_needed_air`
- `sarah_version_nico`
- `sarah_version_camille_minimized`
- `sarah_version_emotional_confusion`

## Vigilance voix

Sarah n’est pas une enquêtrice. Elle cherche une parole qui ne la rende pas folle.

Elle doit rester simple, concrète, domestique, parfois blessée, jamais omnisciente.

---

# j1_02_camille_dehors

## Fonction narrative

Camille confronte le joueur sur le moment dehors.

Cette scène mesure si le joueur reconnaît la tension ou s’il tente de la minimiser. Elle pose aussi la dignité de Camille : elle ne veut pas être utilisée comme refuge.

## Ce que Camille sait

- Elle a rejoint le joueur dehors.
- Le moment n’était pas neutre.
- Le joueur n’a pas clairement interrompu l’intimité émotionnelle.
- Sarah était présente à la soirée.
- Le joueur peut être tenté de minimiser.

## Ce que Camille ignore

- Ce que Sarah sait exactement.
- Ce que le joueur a dit à Sarah.
- Si Nico a couvert quelque chose.
- Ce que Maya a vu.
- Ce que le joueur va assumer concrètement.

## Ce que Camille peut soupçonner

- Le joueur risque de garder Camille comme respiration tout en préservant son confort.
- Il veut peut-être une intensité sans coût.
- Si `delayed_reply_camille_j1` est présent, elle peut noter le détour ou le silence.
- Si `first_reply_sarah` est présent, elle peut sentir que le joueur tente d’être prudent, sans savoir ce qui a été dit.

## Flags d’entrée possibles

- `first_reply_camille`
- `first_reply_sarah`
- `delayed_reply_camille_j1`
- `vulnerable_to_sarah`
- `mentioned_camille_to_sarah`
- `minimized_camille_to_sarah`
- `used_nico_alibi_sarah`
- `asked_nico_hold_version`
- `confessed_camille_to_nico`

## Variantes d’entrée nécessaires

### `default`

Camille attaque sur la non-neutralité du moment dehors.

### `first_reply_camille`

Le joueur l’a ouverte en premier. Camille peut noter cette priorité sans en faire une récompense.

Tonalité : lucide, légèrement plus tendue.

### `after_sarah_first`

Condition : `first_reply_sarah`.

Camille peut être plus prudente : elle sent que le joueur a peut-être tenté de gérer la maison d’abord.

Tonalité : moins joueuse, plus précise.

### `late_or_left_open`

Condition : `delayed_reply_camille_j1` ou `ignored_camille_j1`.

Camille voit le délai comme une réponse partielle.

Tonalité : coupante, sèche.

### `after_nico_alibi`

Condition : `asked_nico_hold_version` ou `used_nico_alibi_sarah`.

Camille ne doit pas savoir que Nico est impliqué, sauf si le joueur lui dit. Elle peut seulement sentir que le joueur construit une version.

Tonalité : méfiance face aux détours.

## Phrases autorisées / direction de voix

- “Je note le détour.”
- “Tu vas faire comme si c’était juste une discussion dehors ?”
- “Tu réponds à côté.”
- “Je peux entendre que tu sois perdu. Pas que tu me ranges dans un coin pratique.”

## Phrases interdites

Camille ne doit pas dire :

- “Sarah sait tout.”
- “Nico t’a couvert.”
- “Maya a une photo.”
- “Tu m’as choisie.”
- “On est ensemble maintenant.”

## Effets attendus

Variables principales :

- `tension_camille`
- `respect_camille`
- `pression_camille`
- `intimite_camille`
- `coherence`
- `culpabilite`
- `fatigue_emotionnelle`

Flags principaux :

- `admitted_tension_to_camille`
- `protected_camille_boundary`
- `minimized_with_camille`
- `uncertain_with_camille`
- `early_desire_to_camille`
- `ignored_camille_j1`
- `camille_trouble_acknowledged`
- `camille_boundary_respected`
- `camille_desire_too_early_j1`

## Vigilance voix

Camille doit rester attirante par sa précision et sa lucidité, pas par une disponibilité automatique.

Elle peut désirer, mais elle doit surtout refuser d’être une échappatoire.

---

# j1_03_nico_couverture

## Fonction narrative

Nico clarifie ce qu’il doit savoir, taire ou porter.

Cette scène teste la dette amicale, l’usage de l’alibi et la possibilité d’une confession plus honnête.

## Ce que Nico sait

- Il a couvert ou simplifié l’absence du joueur pendant la soirée.
- Le joueur était troublé.
- Camille est peut-être liée au trouble, mais il ne connaît pas forcément le détail.
- Sarah ou Maya pourraient poser des questions.

## Ce que Nico ignore

- Ce qui s’est dit exactement dehors.
- Le degré d’intimité avec Camille.
- Ce que le joueur a dit à Sarah.
- Ce que Maya a vu.
- Si le joueur veut assumer ou gagner du temps.

## Ce que Nico peut soupçonner

- Le joueur est en train d’improviser plusieurs versions.
- Il risque de demander à Nico de porter plus qu’un simple blanc.
- Si `first_reply_nico` est présent, Nico peut comprendre qu’on vient vite le chercher comme filet de sécurité.
- Si `used_nico_alibi_sarah` est déjà posé, Nico peut sentir qu’il devient un outil.

## Flags d’entrée possibles

- `first_reply_nico`
- `delayed_reply_nico_j1`
- `used_nico_alibi_sarah`
- `sarah_version_nico`
- `mentioned_camille_to_sarah`
- `minimized_camille_to_sarah`
- `admitted_tension_to_camille`
- `early_desire_to_camille`
- `asked_nico_hold_version`

## Variantes d’entrée nécessaires

### `default`

Nico ouvre par l’humour et la mise en garde.

### `first_reply_nico`

Le joueur l’a choisi en premier. Nico doit sentir qu’il est utilisé comme pare-chocs.

Tonalité : drôle mais méfiant.

### `after_sarah_version_nico`

Condition : `used_nico_alibi_sarah` ou `sarah_version_nico`.

Nico peut réagir si le joueur lui demande de tenir une version qui le concerne.

Tonalité : limite amicale.

### `after_camille_confusion`

Condition : `admitted_tension_to_camille`, `early_desire_to_camille` ou `minimized_with_camille`.

Nico ne sait pas ce que Camille a dit, mais peut entendre que le joueur parle maintenant de Camille.

Tonalité : humour + lucidité.

### `late`

Condition : `delayed_reply_nico_j1`.

Nico peut faire une vanne sur le fait qu’on le contacte quand ça brûle.

## Phrases autorisées / direction de voix

- “frérot”
- “plan claqué”
- “t’as besoin d’un alibi ou d’un psy ?”
- “Je peux couvrir un blanc. Pas toute ta vie.”

## Phrases interdites

Nico ne doit pas dire :

- “Je sais que tu as eu un moment intime avec Camille.” sauf si le joueur lui avoue.
- “Maya a une photo.” sauf information transmise.
- “Sarah m’a appelé.” sauf scène/flag spécifique.
- “Je vais mentir pour toi tout le temps.”

## Effets attendus

Variables principales :

- `dette_nico`
- `coherence`
- `risque_exposition`
- `culpabilite`
- `fatigue_emotionnelle`

Flags principaux :

- `asked_nico_hold_version`
- `told_nico_stay_silent`
- `confessed_camille_to_nico`
- `vulnerable_to_nico`
- `dismissed_nico_warning`
- `nico_full_alibi`
- `nico_alibi_requested`

## Vigilance voix

Nico doit rester un ami, pas un tutoriel moral.

Ses phrases sérieuses doivent tomber après ou au milieu d’une vanne.

---

# j1_04_maya_pique

## Fonction narrative

Maya signale qu’elle a vu une incohérence sociale.

Cette scène met en jeu le regard du groupe, les photos, le timing et le risque d’exposition.

## Ce que Maya sait

- Le joueur et Camille ont disparu ou manqué à l’appel à un moment proche.
- Sarah a senti quelque chose ou semblait moins bien.
- Nico a peut-être donné une explication peu solide.
- Le timing du joueur est étrange.
- Certains détails publics ne collent pas parfaitement.

## Ce que Maya ignore

- Ce qui s’est vraiment passé dehors.
- Si Camille et le joueur ont parlé intimement.
- Ce que Sarah sait exactement.
- Ce que le joueur a dit aux autres.
- Si Nico ment volontairement.

## Ce que Maya peut soupçonner

- Il y a une tension entre le joueur et Camille.
- Le joueur tente peut-être de contrôler les versions.
- Sarah pourrait être blessée.
- Si `asked_nico_hold_version` ou `used_nico_alibi_sarah` existe, Maya ne doit pas le savoir directement, mais peut sentir une version sociale fragile si le joueur lui parle mal.

## Flags d’entrée possibles

- `first_reply_maya`
- `delayed_reply_maya_j1`
- `played_dumb_with_maya`
- `told_maya_needed_air`
- `told_maya_not_involve`
- `asked_maya_what_she_saw`
- `used_nico_alibi_sarah`
- `sarah_version_nico`
- `mentioned_camille_to_sarah`
- `minimized_camille_to_sarah`

## Variantes d’entrée nécessaires

### `default`

Maya lance une pique sur le timing.

### `first_reply_maya`

Le joueur l’ouvre en premier. Maya peut trouver ça révélateur : pourquoi venir vers elle avant Sarah ou Camille ?

Tonalité : piquante, intriguée.

### `after_sarah`

Condition : `first_reply_sarah` ou scène Sarah déjà terminée.

Maya peut rester prudente : elle ne sait pas ce qui a été dit à Sarah.

### `after_camille`

Condition : `first_reply_camille` ou scène Camille déjà terminée.

Maya ne doit pas savoir la conversation avec Camille, mais peut être plus sèche si le timing global est mauvais.

### `late`

Condition : `delayed_reply_maya_j1`.

Maya peut faire une pique sur le “vu” ou le silence.

## Phrases autorisées / direction de voix

- “je pose ça là”
- “je note”
- “ton timing est une œuvre d’art”
- “si Sarah me demande directement, je mens pas.”

## Phrases interdites

Maya ne doit pas dire :

- “Je sais ce que vous avez fait dehors.”
- “Sarah m’a tout raconté.”
- “Nico m’a confirmé ton mensonge.”
- “Je vais te faire chanter.”

## Effets attendus

Variables principales :

- `suspicion_maya`
- `risque_exposition`
- `coherence`
- `fatigue_emotionnelle`

Flags principaux :

- `played_dumb_with_maya`
- `info_maya_photo_possible`
- `maya_photo_possible`
- `told_maya_needed_air`
- `told_maya_not_involve`
- `joked_with_maya_j1`
- `asked_maya_if_sarah_talked`
- `asked_maya_what_she_saw`
- `ignored_maya_j1`

## Vigilance voix

Maya est sociale et vive. Elle n’est ni policière, ni omnisciente, ni ennemie pure.

Elle protège Sarah sans forcément attaquer le joueur.

---

# j1_05_ines_faille

## Fonction narrative

Inès perçoit l’état intérieur du joueur.

Cette scène ouvre une porte latérale, douce mais dangereuse, sans devenir une romance complète.

## Ce qu’Inès sait

- Elle a vu le joueur ailleurs ou triste pendant la soirée.
- Elle a senti une faille émotionnelle.
- L’ambiance autour de lui semblait chargée.

## Ce qu’Inès ignore

- La tension exacte avec Camille.
- L’état réel du couple avec Sarah.
- Le rôle de Nico.
- Ce que Maya a vu.
- Ce que le joueur veut réellement.

## Ce qu’Inès peut soupçonner

- Le joueur traverse quelque chose qu’il n’arrive pas à dire.
- Il cherche peut-être un endroit sans question.
- Si `first_reply_ines` est présent, elle peut sentir que son message a servi de porte de sortie.
- Si le joueur sexualise trop vite, elle doit se fermer.

## Flags d’entrée possibles

- `first_reply_ines`
- `delayed_reply_ines_j1`
- `opened_to_ines`
- `ines_fuite_seed`
- `kept_ines_at_distance`
- `sexualized_ines_too_early`
- `vulnerable_to_sarah`
- `early_desire_to_camille`
- `fatigue_emotionnelle` élevée

## Variantes d’entrée nécessaires

### `default`

Inès écrit avec hésitation, depuis une perception douce.

### `first_reply_ines`

Le joueur l’a ouverte en premier. Inès ne doit pas s’en réjouir comme une romance ; elle doit sentir l’étrangeté de la priorité.

Tonalité : douce mais prudente.

### `after_conflict`

Condition : variables ou flags indiquant fatigue, culpabilité, tension avec Sarah/Camille/Nico.

Inès peut sentir que le joueur arrive chargé, sans connaître les détails.

### `late`

Condition : `delayed_reply_ines_j1`.

Inès doit rester rare et ne pas reprocher fortement.

Tonalité : “pas grave si tu réponds plus tard”.

## Phrases autorisées / direction de voix

- “j’ai hésité avant d’écrire”
- “c’est peut-être pas mes affaires”
- “oublie si c’est bizarre”
- “tu avais l’air ailleurs, mais pas absent.”

## Phrases interdites

Inès ne doit pas dire :

- “Je sais que tu as un truc avec Camille.”
- “Quitte Sarah.”
- “Viens vers moi.”
- “Je peux remplacer ce que tu n’arrives pas à choisir.”
- Toute phrase explicitement sexuelle dans le MVP.

## Effets attendus

Variables principales :

- `fuite_ines`
- `fatigue_emotionnelle`
- `culpabilite`
- `coherence`

Flags principaux :

- `opened_to_ines`
- `ines_fuite_seed`
- `asked_ines_why_write`
- `kept_ines_at_distance`
- `sexualized_ines_too_early`
- `ignored_ines_j1`

## Vigilance voix

Inès doit rester rare, douce, légèrement étrange.

Elle ne doit pas devenir une troisième route romantique complète.

---

# j1_06_sarah_rentrer_manger

## Fonction narrative

Respiration domestique après les cinq scènes cœur.

Sarah revient par le quotidien : repas, assiette, présence, maison. Cette scène montre que le couple n’est pas seulement un problème moral, mais une intimité réelle en train de se fragiliser.

## Ce que Sarah sait

- Le joueur a répondu ou non à ses questions précédentes.
- Il a peut-être donné une version plus ou moins claire.
- La journée a été distante ou tendue.
- Elle ne se sent pas forcément rassurée.

## Ce que Sarah ignore

- Les détails des conversations avec Camille, Nico, Maya et Inès.
- Les variables internes du joueur.
- Les choix exacts faits ailleurs, sauf si des flags narratifs les rendent visibles plus tard.

## Ce que Sarah peut soupçonner

- Le joueur évite encore de revenir vraiment.
- Le banal devient un test de présence.
- Si la confiance est basse ou la distance haute, elle peut être plus froide.
- Si `vulnerable_to_sarah` ou `sarah_j1_domestic_presence` est présent, elle peut rester plus ouverte.

## Flags d’entrée possibles

- `vulnerable_to_sarah`
- `used_nico_alibi_sarah`
- `mentioned_camille_to_sarah`
- `minimized_camille_to_sarah`
- `ignored_sarah_j1`
- `sarah_no_clear_version_j1`
- `first_reply_sarah`
- `delayed_reply_sarah_j1`
- `sarah_j1_domestic_presence`

## Variantes d’entrée nécessaires

### `default`

Sarah propose le repas avec une tension douce.

### `after_honesty`

Condition : `vulnerable_to_sarah` ou version relativement cohérente.

Tonalité : fragile mais encore tendre.

### `after_minimization`

Condition : `minimized_camille_to_sarah`, `used_nico_alibi_sarah` ou cohérence basse.

Tonalité : plus courte, moins chaleureuse.

### `after_ignored`

Condition : `ignored_sarah_j1` ou `delayed_reply_sarah_j1`.

Tonalité : retrait, fatigue.

## Phrases autorisées / direction de voix

- “Tu rentres manger ?”
- “Je t’ai gardé une assiette.”
- “J’ai sorti ce qu’il restait de pâtes.”
- “Je sais pas si ça compte, mais…”

## Phrases interdites

Sarah repas ne doit pas redevenir une scène d’interrogatoire complet.

Elle ne doit pas dire :

- “Avoue pour Camille maintenant.”
- “Je sais tout.”
- “Maya m’a envoyé la preuve.”

## Effets attendus

Variables principales :

- `confiance_sarah`
- `distance_sarah`
- `intimite_sarah`
- `culpabilite`
- `fatigue_emotionnelle`
- `coherence`

Flags principaux :

- `sarah_j1_domestic_presence`
- `promised_sarah_later_j1`
- `sarah_j1_uncertain_return`
- `used_work_excuse_sarah_j1`
- `late_reply_sarah_meal_j1`

## Vigilance voix

Cette scène doit être simple et domestique. Le drame doit passer par l’écart entre le quotidien et l’absence intérieure du joueur.

---

# j1_07_nico_vanne_soiree

## Fonction narrative

Respiration amicale et rappel du danger.

Nico détend l’atmosphère avec humour, mais il peut aussi rappeler qu’il ne sera pas un alibi permanent.

## Ce que Nico sait

- Le joueur a traversé une journée compliquée.
- Il a peut-être demandé une couverture ou non.
- Il sait si le joueur lui a parlé honnêtement dans `j1_03_nico_couverture`.
- Il peut sentir si l’amitié est utilisée ou respectée.

## Ce que Nico ignore

- Les détails des conversations avec Sarah, Camille, Maya ou Inès, sauf si le joueur lui a raconté.
- Ce que Sarah pense réellement.
- Ce que Maya possède comme information.

## Ce que Nico peut soupçonner

- Le joueur continue peut-être à éviter.
- L’humour sert peut-être à ne pas choisir.
- Si `asked_nico_hold_version` ou `asked_nico_second_cover_j1` est présent, il peut poser une limite.
- Si `confessed_camille_to_nico` ou `vulnerable_to_nico` est présent, il peut être plus allié.

## Flags d’entrée possibles

- `asked_nico_hold_version`
- `told_nico_stay_silent`
- `confessed_camille_to_nico`
- `vulnerable_to_nico`
- `dismissed_nico_warning`
- `nico_alibi_requested`
- `asked_nico_second_cover_j1`
- `joked_to_avoid_nico_j1`
- `ignored_nico_respiration_j1`

## Variantes d’entrée nécessaires

### `default`

Nico propose une respiration par la vanne.

### `after_alibi_request`

Condition : `asked_nico_hold_version` ou `nico_alibi_requested`.

Tonalité : humour plus sec, limite claire.

### `after_confession`

Condition : `confessed_camille_to_nico` ou `vulnerable_to_nico`.

Tonalité : ami présent, vanne + soutien.

### `after_dismissed_warning`

Condition : `dismissed_nico_warning`.

Tonalité : plus froid, agacé.

## Phrases autorisées / direction de voix

- “pizza ce soir ?”
- “mon reuf”
- “t’as l’air de bugger comme une appli en bêta.”
- “Je peux couvrir un blanc. Pas toute ta vie.”

## Phrases interdites

Nico ne doit pas devenir :

- un conseiller thérapeutique complet ;
- un sauveur magique ;
- un complice illimité ;
- un narrateur omniscient.

Il ne doit pas dire :

- “Sarah va forcément te quitter.”
- “Camille t’aime.”
- “Maya a déjà gagné.”

## Effets attendus

Variables principales :

- `dette_nico`
- `fatigue_emotionnelle`
- `coherence`
- `risque_exposition`

Flags principaux :

- `nico_j1_respiration_shared`
- `asked_nico_real_advice_j1`
- `asked_nico_second_cover_j1`
- `joked_to_avoid_nico_j1`
- `ignored_nico_respiration_j1`

## Vigilance voix

Nico doit faire respirer le jeu sans annuler les conséquences.

Il peut faire rire, mais ses limites doivent rester visibles.

---

# Check-list avant écriture des dialogues

Avant de valider une nouvelle ligne de dialogue, vérifier :

1. Qui parle ?
2. Quelle est sa voix ?
3. Que sait-il vraiment ?
4. Que ne peut-il pas savoir ?
5. Quel flag justifie cette variante ?
6. La phrase révèle-t-elle une relation ou seulement une information ?
7. Les effets associés correspondent-ils au sens du choix ?
8. La scène respecte-t-elle son rôle dans la journée ?
9. La phrase pourrait-elle être dite par un autre personnage ? Si oui, la réécrire.
10. Le dialogue ajoute-t-il une conséquence, une nuance ou une tension ? Sinon, le couper.

---

# Suite recommandée

Après validation de cette matrice :

1. Ajouter un support runtime minimal des `entry_variants`.
2. Implémenter les variantes d’entrée de Sarah et Camille.
3. Implémenter les variantes d’entrée de Nico, Maya et Inès.
4. Réécrire les scènes de respiration Sarah repas et Nico soirée.
5. Playtester J1 V2 complet en vérifiant cohérence, rythme et voix.
