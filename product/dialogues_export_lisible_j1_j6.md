# Double Vie — Export dialogues lisible J1→J6 + finale
> Export généré pour relecture humaine. Les IDs sont conservés pour signaler précisément une phrase à corriger.
> Format : messages visibles + choix. La structure technique/branches n’est pas modifiée.
## Note de relecture rapide
- Si une phrase est incompréhensible : noter `Jour`, `Contact`, `ID`.
- Les lignes `Système` correspondent souvent à des transitions/blocs visibles ou semi-visibles.
- Les choix sont listés sous le node de choix, avec leurs effets masqués non détaillés.

---

# Jour 1

## Camille — `camille_j1_complete`

Source: `narrative/t007_camille_j1_complete.json`  
Start: `c1_001`

`c1_001` **Camille** : Alors… tu fais toujours semblant d’être sérieux le matin ? Le café du coin passe un morceau beaucoup trop dramatique pour 9h, ça aide peut-être. → `c1_002`

**CHOIX** `c1_002` — Répondre à Camille sur le ton du jeu, pas de la survie.
- 1. `c1_002_a` → Seulement quand on me surveille. _(next: `c1_003_flirt`)_
- 2. `c1_002_b` → Je suis très sérieux. Trop, même. Surtout avant le deuxième café. _(next: `c1_003_soft`)_
- 3. `c1_002_c` → Ignorer pour l’instant _(next: `c1_003_ignore`)_

`c1_003_flirt` **Vous** : Seulement quand on me surveille. → `c1_004_flirt`

`c1_004_flirt` **Camille** : Donc si je te surveille, tu redeviens sage ? Intéressant. Je note la théorie sur une serviette en papier. → `c1_005`

`c1_003_soft` **Vous** : Je suis très sérieux. Trop, même. Surtout avant le deuxième café. → `c1_004_soft`

`c1_004_soft` **Camille** : Ça sonne comme un défi, pas comme une information. Tu as hésité avant d’envoyer, non ? → `c1_005`

`c1_003_ignore` **Système** : Camille reste en attente. La notification disparaît, pas la tension. → `c1_004_ignore`

`c1_004_ignore` **Camille** : Je vois. Monsieur sérieux a aussi l’option silence. Il est assez bien habillé, ce silence. → `c1_005_ignore_choice`

**CHOIX** `c1_005_ignore_choice` — Camille relance après le silence.
- 1. `c1_005_ignore_a` → J’étais occupé, pas indifférent. _(next: `c1_006_ignore_a`)_
- 2. `c1_005_ignore_b` → Je ne voulais pas répondre trop vite. _(next: `c1_006_ignore_b`)_

`c1_006_ignore_a` **Vous** : J’étais occupé, pas indifférent. → `c1_007_ignore_a`

`c1_007_ignore_a` **Camille** : Bonne réponse. Je préfère quand tu assumes un minimum. Même si c’est juste la moitié d’une phrase au fond d’un café. → `c1_005`

`c1_006_ignore_b` **Vous** : Je ne voulais pas répondre trop vite. → `c1_007_ignore_b`

`c1_007_ignore_b` **Camille** : Ah. Donc tu calcules. C’est presque pire… mais pas inintéressant. Garde cette prudence, elle te resservira. → `c1_005`

`c1_005` **Camille** : Je passe près de ton quartier ce soir. Enfin… peut-être. → `c1_006`

**CHOIX** `c1_006` — Camille ouvre une porte.
- 1. `c1_006_a` → Préviens-moi si le peut-être devient sûr. _(next: `c1_007_a`)_
- 2. `c1_006_b` → Ce soir c’est compliqué. _(next: `c1_007_b`)_
- 3. `c1_006_c` → Compliqué, mais j’ai envie de savoir. _(next: `c1_007_c`)_

`c1_007_a` **Vous** : Préviens-moi si le peut-être devient sûr. → `c1_008_a`

`c1_008_a` **Camille** : Je note. J’aime bien quand tu réponds vite. → `c1_009_pause`

`c1_007_b` **Vous** : Ce soir c’est compliqué. → `c1_008_b`

`c1_008_b` **Camille** : Toujours sérieux, donc. Dommage, j’étais curieuse. → `c1_009_pause`

`c1_007_c` **Vous** : Compliqué, mais j’ai envie de savoir. → `c1_008_c`

`c1_008_c` **Camille** : Voilà. Là tu es beaucoup plus intéressant. → `c1_009_pause`

`c1_009_pause` **Système** : La journée avance. Camille ne renvoie rien pendant un moment. C’est pire que si elle insistait. → `c1_010`

`c1_010` **Camille** : Je viens de passer devant le café au coin. Il avait l’air vide. Presque fait exprès. → `c1_011`

**CHOIX** `c1_011` — Répondre au message du soir
- 1. `c1_011_a` → Tu fais exprès de me mettre ça en tête. _(next: `c1_012_a`)_
- 2. `c1_011_b` → Je suis pris ce soir. Vraiment. _(next: `c1_012_b`)_
- 3. `c1_011_c` → Si tu y retournes, je veux le savoir. _(next: `c1_012_c`)_

`c1_012_a` **Vous** : Tu fais exprès de me mettre ça en tête. → `c1_013_a`

`c1_013_a` **Camille** : Peut-être. Ça marche ? → `c1_014`

`c1_012_b` **Vous** : Je suis pris ce soir. Vraiment. → `c1_013_b`

`c1_013_b` **Camille** : Vraiment, c’est le mot qu’on ajoute quand on veut que ça ait l’air simple. → `c1_014`

`c1_012_c` **Vous** : Si tu y retournes, je veux le savoir. → `c1_013_c`

`c1_013_c` **Camille** : Attention. Tu commences à parler comme quelqu’un qui attend une notification. → `c1_014`

`c1_014` **Camille** : Dis-moi juste un truc : si je t’écris tard, tu réponds ? → `c1_015`

**CHOIX** `c1_015` — Camille teste la limite du soir.
- 1. `c1_015_a` → Ça dépend de ce que tu écris. _(next: `c1_016_a`)_
- 2. `c1_015_b` → Je ne devrais pas. _(next: `c1_016_b`)_
- 3. `c1_015_c` → Oui. _(next: `c1_016_c`)_

`c1_016_a` **Vous** : Ça dépend de ce que tu écris. → `c1_017_a`

`c1_017_a` **Camille** : Alors je vais choisir mes mots. → `c1_018_wait`

`c1_016_b` **Vous** : Je ne devrais pas. → `c1_017_b`

`c1_017_b` **Camille** : Je n’ai pas demandé ce que tu devrais faire. → `c1_018_wait`

`c1_016_c` **Vous** : Oui. → `c1_017_c`

`c1_017_c` **Camille** : Simple. Dangereux. J’aime bien. → `c1_018_wait`

`c1_018_wait` **Système** : Plus rien. L’écran reste calme assez longtemps pour que tu le vérifies deux fois. → `c1_019`

`c1_019` **Camille** : 23:42. → `c1_020`

`c1_020` **Camille** : Je suis devant le café. Je ne sais pas pourquoi je t’écris au lieu de rentrer. → `c1_021`

**CHOIX** `c1_021` — Cliffhanger fin J1
- 1. `c1_021_a` → Ne bouge pas. _(next: `c1_end_go`)_
- 2. `c1_021_b` → Rentre, Camille. _(next: `c1_end_resist`)_
- 3. `c1_021_c` → Vu à 23:42 _(next: `c1_end_seen`)_

`c1_end_go` **[FIN]** **Système** : Fin J1 : tu as répondu. Camille attend. Le téléphone aussi.

`c1_end_resist` **[FIN]** **Système** : Fin J1 : tu poses une limite. Mais le message reste là, intact.

`c1_end_seen` **[FIN]** **Système** : Fin J1 : tu n’as pas répondu. C’est parfois la trace la plus bruyante.

## Sarah — `sarah_j1_complete`

Source: `narrative/t037_sarah_j1_complete.json`  
Start: `s1_001`

`s1_001` **Sarah** : T’es déjà parti ? J’ai pas entendu la porte. Ni le bruit de tes clés, d’ailleurs. → `s1_002`

`s1_002` **Sarah** : J’ai laissé ton café sur le plan de travail. Il doit être froid maintenant. J’ai même remis ta clé sous le bol, comme une personne très organisée et pas du tout inquiète. → `s1_003`

**CHOIX** `s1_003` — Répondre à Sarah sans transformer le matin en dossier.
- 1. `s1_003_a` → Désolé, je suis parti tôt. J’aurais dû boire le café avec toi deux minutes. _(next: `s1_004_a`)_
- 2. `s1_003_b` → Réunion tôt. J’ai filé sans réfléchir. _(next: `s1_004_b`)_
- 3. `s1_003_c` → Je suis encore dans le coin. Je peux repasser deux minutes. _(next: `s1_004_c`)_

`s1_004_a` **Vous** : Désolé, je suis parti tôt. J’aurais dû boire le café avec toi deux minutes. → `s1_005_a`

`s1_005_a` **Sarah** : C’est gentil. Mais j’aime bien quand tu me dis au revoir, même à moitié endormie. Ça prend trois secondes et ça change la cuisine entière. → `s1_006`

`s1_004_b` **Vous** : Réunion tôt. J’ai filé sans réfléchir. → `s1_005_b`

`s1_005_b` **Sarah** : Tu me l’avais pas dit hier. C’est nouveau ? Je demande avant de ranger ça dans ma tête avec le café froid. → `s1_006`

`s1_004_c` **Vous** : Je suis encore dans le coin. Je peux repasser deux minutes. → `s1_005_c`

`s1_005_c` **Sarah** : Deux minutes et un vrai sourire, alors. Pas ton sourire de couloir avec une main déjà sur la poignée. → `s1_006`

`s1_006` **Sarah** : Au fait… ton téléphone a vibré deux fois sur la table cette nuit. J’ai pas regardé. Je l’ai juste retourné parce que la lumière me réveillait. → `s1_007`

**CHOIX** `s1_007` — Sarah a remarqué les notifications.
- 1. `s1_007_a` → C’était sûrement le boulot. _(next: `s1_008_a`)_
- 2. `s1_007_b` → J’ai vu après. Rien d’important. _(next: `s1_008_b`)_
- 3. `s1_007_c` → Merci de ne pas avoir regardé. _(next: `s1_008_c`)_

`s1_008_a` **Vous** : C’était sûrement le boulot. → `s1_009_a`

`s1_009_a` **Sarah** : Sûrement ? Tu réponds comme quelqu’un qui n’a pas envie de vérifier. → `s1_010`

`s1_008_b` **Vous** : J’ai vu après. Rien d’important. → `s1_009_b`

`s1_009_b` **Sarah** : Ok. Je te crois. C’est juste que ça m’a réveillée, alors j’y ai pensé. → `s1_010`

`s1_008_c` **Vous** : Merci de ne pas avoir regardé. → `s1_009_c`

`s1_009_c` **Sarah** : Je ne fouille pas. J’aimerais juste ne pas avoir envie de poser la question. → `s1_010`

`s1_010` **Sarah** : Ce soir, on mange ensemble ? J’ai gardé ma soirée pour nous. → `s1_011`

**CHOIX** `s1_011` — La soirée avec Sarah devient un engagement.
- 1. `s1_011_a` → Oui. Je rentre tôt, promis. _(next: `s1_012_a`)_
- 2. `s1_011_b` → Je te confirme dans la journée. _(next: `s1_012_b`)_
- 3. `s1_011_c` → J’ai peut-être un truc pro. Je sais pas encore. _(next: `s1_012_c`)_

`s1_012_a` **Vous** : Oui. Je rentre tôt, promis. → `s1_013_a`

`s1_013_a` **Sarah** : Promis, c’est noté. Je vais faire semblant de ne pas compter les minutes. → `s1_014`

`s1_012_b` **Vous** : Je te confirme dans la journée. → `s1_013_b`

`s1_013_b` **Sarah** : D’accord. Mais me laisse pas dans le flou jusqu’au dernier moment, s’il te plaît. → `s1_014`

`s1_012_c` **Vous** : J’ai peut-être un truc pro. Je sais pas encore. → `s1_013_c`

`s1_013_c` **Sarah** : Encore un truc pro qui apparaît le matin même ? Ok. On en reparle ce midi. → `s1_014`

`s1_014` **Système** : La matinée passe. Sarah n’insiste pas. Son silence ressemble moins à de la paix qu’à une attente. → `s1_015`

`s1_015` **Sarah** : J’ai retrouvé ton écharpe sur la chaise. Tu veux que je te la laisse dans l’entrée ? → `s1_016`

`s1_016` **Sarah** : Et ne réponds pas “comme tu veux”. Je connais déjà cette réponse. → `s1_017`

**CHOIX** `s1_017` — Répondre à Sarah en fin de journée
- 1. `s1_017_a` → Garde-la. Je la prendrai en rentrant. _(next: `s1_018_a`)_
- 2. `s1_017_b` → Laisse-la dans l’entrée, je passerai vite. _(next: `s1_018_b`)_
- 3. `s1_017_c` → Je risque de rentrer tard. Ne m’attends pas. _(next: `s1_018_c`)_

`s1_018_a` **Vous** : Garde-la. Je la prendrai en rentrant. → `s1_019_a`

`s1_019_a` **Sarah** : D’accord. Alors je t’attends pour manger. → `s1_020`

`s1_018_b` **Vous** : Laisse-la dans l’entrée, je passerai vite. → `s1_019_b`

`s1_019_b` **Sarah** : “Passer vite”, c’est pas vraiment rentrer. Mais ok. → `s1_020`

`s1_018_c` **Vous** : Je risque de rentrer tard. Ne m’attends pas. → `s1_019_c`

`s1_019_c` **Sarah** : Je déteste quand tu dis ça avant même que la journée soit finie. → `s1_020`

`s1_020` **Sarah** : Je vais poser une question simple, mais je veux pas que ça sonne comme un piège. → `s1_021`

`s1_021` **Sarah** : J’ai l’impression que tu es ailleurs depuis ce matin. Je me trompe ? → `s1_022`

**CHOIX** `s1_022` — Cliffhanger Sarah J1
- 1. `s1_022_a` → Non. Je suis juste fatigué. _(next: `s1_end_deny`)_
- 2. `s1_022_b` → Pas maintenant. Je t’expliquerai ce soir. _(next: `s1_end_delay`)_
- 3. `s1_022_c` → Oui. Mais je ne sais pas comment te le dire. _(next: `s1_end_confess_hint`)_

`s1_end_deny` **[FIN]** **Système** : Fin J1 Sarah : tu fermes la porte. Sarah ne tape plus. Le silence reste ouvert.

`s1_end_delay` **[FIN]** **Système** : Fin J1 Sarah : tu gagnes quelques heures. Pas forcément de la confiance.

`s1_end_confess_hint` **[FIN]** **Système** : Fin J1 Sarah : trois points apparaissent, disparaissent, puis reviennent. Elle est en train d’écrire.

---

# Jour 2

## Camille — `camille_j2_complete`

Source: `narrative/t061_camille_j2_complete.json`  
Start: `c2_block_a`

`c2_block_a` **Système** : C2A — Reprise après 23:42 → `c2_001`

`c2_001` **Camille** : J’ai relu ton message de cette nuit. → `c2_002`

`c2_002` **Camille** : Enfin… ton message, ton silence, ou ton “ne bouge pas”. Peu importe. Ça m’a tenue éveillée plus longtemps que prévu. → `c2_003`

**CHOIX** `c2_003` — Camille revient sur 23:42.
- 1. `c2_003_a` → Moi aussi j’y ai repensé. Surtout au café, et c’est agaçant. _(next: `c2_004_a`)_
- 2. `c2_003_b` → C’était une mauvaise idée de continuer si tard. _(next: `c2_004_b`)_
- 3. `c2_003_c` → Tu étais vraiment devant le café ? _(next: `c2_004_c`)_

`c2_004_a` **Vous** : Moi aussi j’y ai repensé. Surtout au café, et c’est agaçant. → `c2_005_a`

`c2_005_a` **Camille** : Je m’en doutais. Tu as cette façon de répondre comme si tu voulais faire semblant de ne pas attendre. → `c2_006`

`c2_004_b` **Vous** : C’était une mauvaise idée de continuer si tard. → `c2_005_b`

`c2_005_b` **Camille** : Mauvaise idée, peut-être. Mais tu n’as pas dit que tu regrettais. → `c2_006`

`c2_004_c` **Vous** : Tu étais vraiment devant le café ? → `c2_005_c`

`c2_005_c` **Camille** : Oui. Et j’ai détesté le fait que ce soit presque normal de t’écrire de là. → `c2_006`

`c2_006` **Camille** : Aujourd’hui je passe encore dans le coin. Pas par hasard cette fois. → `c2_007`

**CHOIX** `c2_007` — Réagir à son passage annoncé.
- 1. `c2_007_a` → Tu cherches les problèmes, ou juste une table au fond ? _(next: `c2_008_a`)_
- 2. `c2_007_b` → Dis-moi juste quand. _(next: `c2_008_b`)_
- 3. `c2_007_c` → Je ne peux pas te voir aujourd’hui. _(next: `c2_008_c`)_

`c2_008_a` **Vous** : Tu cherches les problèmes, ou juste une table au fond ? → `c2_009_a`

`c2_009_a` **Camille** : Non. Je vérifie si tu en es un. → `c2_block_b`

`c2_008_b` **Vous** : Dis-moi juste quand. → `c2_009_b`

`c2_009_b` **Camille** : Voilà. Là, tu ne joues plus au sérieux. → `c2_block_b`

`c2_008_c` **Vous** : Je ne peux pas te voir aujourd’hui. → `c2_009_c`

`c2_009_c` **Camille** : Tu dis “je ne peux pas”, pas “je ne veux pas”. C’est noté. → `c2_block_b`

`c2_block_b` **Système** : C2B — Proposition ambiguë → `c2_010`

`c2_010` **Camille** : Pause déjeuner. 12:40. Le café au coin a une table près de la vitre. → `c2_011`

`c2_011` **Camille** : Je ne te demande pas de venir. Je te donne juste une information inutile. → `c2_012`

**CHOIX** `c2_012` — Camille transforme l’attente en disponibilité concrète.
- 1. `c2_012_a` → Une information inutile que je vais retenir. _(next: `c2_013_a`)_
- 2. `c2_012_b` → Ne m’envoie pas ce genre d’info si tu ne demandes rien. _(next: `c2_013_b`)_
- 3. `c2_012_c` → Je serai trop loin à cette heure-là. _(next: `c2_013_c`)_

`c2_013_a` **Vous** : Une information inutile que je vais retenir. → `c2_014_a`

`c2_014_a` **Camille** : Je préfère quand tu admets que tu retiens les choses. → `c2_015`

`c2_013_b` **Vous** : Ne m’envoie pas ce genre d’info si tu ne demandes rien. → `c2_014_b`

`c2_014_b` **Camille** : D’accord. Alors je ne demande rien. Et toi tu n’as rien à refuser. → `c2_015`

`c2_013_c` **Vous** : Je serai trop loin à cette heure-là. → `c2_014_c`

`c2_014_c` **Camille** : Trop loin, c’est une distance. Pas une décision. → `c2_015`

`c2_015` **Système** : Le téléphone reste calme quelques minutes. Le calme ressemble à une invitation à vérifier l’écran. → `c2_016`

`c2_016` **Camille** : Je suis arrivée. → `c2_017`

`c2_017` **Camille** : La table près de la vitre est libre. Évidemment. → `c2_018`

**CHOIX** `c2_018` — La proposition devient presque réelle.
- 1. `c2_018_a` → Arrête de me donner envie de passer. _(next: `c2_019_a`)_
- 2. `c2_018_b` → Je ne passerai pas. Mais je lis. _(next: `c2_019_b`)_
- 3. `c2_018_c` → Si je viens, cinq minutes maximum. _(next: `c2_019_c`)_

`c2_019_a` **Vous** : Arrête de me donner envie de passer. → `c2_020_a`

`c2_020_a` **Camille** : Je ne t’ai jamais demandé de ne pas avoir envie. → `c2_block_c`

`c2_019_b` **Vous** : Je ne passerai pas. Mais je lis. → `c2_020_b`

`c2_020_b` **Camille** : Lire, c’est déjà être un peu là. Tu le sais ? → `c2_block_c`

`c2_019_c` **Vous** : Si je viens, cinq minutes maximum. → `c2_020_c`

`c2_020_c` **Camille** : Cinq minutes, c’est le genre de mensonge poli qui dure toujours plus longtemps. → `c2_block_c`

`c2_block_c` **Système** : C2C — Point de bascule J2 → `c2_021`

`c2_021` **Camille** : Je vais partir dans dix minutes. → `c2_022`

`c2_022` **Camille** : Si tu voulais faire semblant que ce n’était qu’un jeu de messages, c’est le moment de réussir. → `c2_023`

**CHOIX** `c2_023` — Point de bascule Camille J2.
- 1. `c2_023_a` → Pars. On arrête là pour aujourd’hui. _(next: `c2_end_boundary`)_
- 2. `c2_023_b` → Reste dix minutes de plus. _(next: `c2_end_stay`)_
- 3. `c2_023_c` → Je ne viens pas. Mais écris quand tu rentres. _(next: `c2_end_thread`)_

`c2_end_boundary` **[FIN]** **Système** : Fin Camille J2 : tu poses une limite. Camille s’éloigne, mais elle sait maintenant où elle peut appuyer.

`c2_end_stay` **[FIN]** **Système** : Fin Camille J2 : elle reste. Le risque n’est plus seulement dans les messages.

`c2_end_thread` **[FIN]** **Système** : Fin Camille J2 : tu ne viens pas, mais tu gardes le fil ouvert. C’est peut-être le plus dangereux.

## Sarah — `sarah_j2_complete`

Source: `narrative/t062_sarah_j2_complete.json`  
Start: `s2_block_a`

`s2_block_a` **Système** : S2A — Matin après malaise → `s2_001`

`s2_001` **Sarah** : Tu es parti tôt encore ? Ton chargeur est resté côté canapé. → `s2_002`

`s2_002` **Sarah** : Je ne te reproche rien. J’ai lancé l’épisode sans toi hier. J’ai tenu huit minutes, exploit. Après j’ai surtout eu l’impression qu’on avait laissé une phrase en suspens. → `s2_003`

**CHOIX** `s2_003` — Répondre au malaise du matin avec une présence simple.
- 1. `s2_003_a` → Je sais. J’aurais dû être plus présent. _(next: `s2_004_a`)_
- 2. `s2_003_b` → J’étais juste fatigué, rien de plus. _(next: `s2_004_b`)_
- 3. `s2_003_c` → On en parle ce soir ? Là je vais être en retard. _(next: `s2_004_c`)_

`s2_004_a` **Vous** : Je sais. J’aurais dû être plus présent. → `s2_005_a`

`s2_005_a` **Sarah** : Merci de le dire. Ça compte, même par message. Je l’ai lu avec mon café trop fort, donc c’est presque une scène de couple. → `s2_006`

`s2_004_b` **Vous** : J’étais juste fatigué, rien de plus. → `s2_005_b`

`s2_005_b` **Sarah** : Peut-être. Mais quand tu es fatigué, d’habitude tu viens t’écraser sur le canapé à côté de moi. Là, même ton pull arrive avant toi. → `s2_006`

`s2_004_c` **Vous** : On en parle ce soir ? Là je vais être en retard. → `s2_005_c`

`s2_005_c` **Sarah** : D’accord. Mais “ce soir” ne doit pas devenir le tiroir où on range tout ce qu’on n’ose pas ouvrir. → `s2_006`

`s2_006` **Sarah** : Je vais faire simple : aujourd’hui, j’ai besoin d’un vrai message. Pas parfait. Juste un truc qui ne ressemble pas à une réponse envoyée entre deux portes. → `s2_007`

**CHOIX** `s2_007` — Sarah demande une présence réelle.
- 1. `s2_007_a` → Je t’écris dès que j’ai une pause. Promis. _(next: `s2_008_a`)_
- 2. `s2_007_b` → Je ne peux pas garantir ma journée, mais je vais essayer. _(next: `s2_008_b`)_
- 3. `s2_007_c` → Je suis là. Même si je réponds mal. Je peux commencer par un vrai message. _(next: `s2_008_c`)_

`s2_008_a` **Vous** : Je t’écris dès que j’ai une pause. Promis. → `s2_009_a`

`s2_009_a` **Sarah** : Je prends le promis. Je vais essayer de ne pas le surveiller comme une idiote. → `s2_block_b`

`s2_008_b` **Vous** : Je ne peux pas garantir ma journée, mais je vais essayer. → `s2_009_b`

`s2_009_b` **Sarah** : Essayer, ça me va. Tant que ce n’est pas juste un mot pratique. → `s2_block_b`

`s2_008_c` **Vous** : Je suis là. Même si je réponds mal. Je peux commencer par un vrai message. → `s2_009_c`

`s2_009_c` **Sarah** : C’est peut-être la réponse la plus honnête que tu pouvais faire. → `s2_block_b`

`s2_block_b` **Système** : S2B — Demande de présence → `s2_010`

`s2_010` **Sarah** : Je suis passée devant la boulangerie. Ils avaient les petits pains que tu prends toujours. → `s2_011`

`s2_011` **Sarah** : J’en ai pris deux. C’était peut-être optimiste. → `s2_012`

**CHOIX** `s2_012` — Répondre à son geste du quotidien.
- 1. `s2_012_a` → Garde-m’en un. Je passerai vraiment. _(next: `s2_013_a`)_
- 2. `s2_012_b` → Tu aurais dû en prendre un seul, je suis pas sûr de passer. _(next: `s2_013_b`)_
- 3. `s2_012_c` → Tu me connais trop bien. _(next: `s2_013_c`)_

`s2_013_a` **Vous** : Garde-m’en un. Je passerai vraiment. → `s2_014_a`

`s2_014_a` **Sarah** : Je vais faire semblant de ne pas sourire à mon téléphone. → `s2_015`

`s2_013_b` **Vous** : Tu aurais dû en prendre un seul, je suis pas sûr de passer. → `s2_014_b`

`s2_014_b` **Sarah** : Ok. Je le savais un peu, mais ça fait différent quand tu l’écris. → `s2_015`

`s2_013_c` **Vous** : Tu me connais trop bien. → `s2_014_c`

`s2_014_c` **Sarah** : C’est justement ça qui me rend attentive quand quelque chose sonne faux. → `s2_015`

`s2_015` **Sarah** : Ce soir, j’aimerais qu’on mange sans téléphone sur la table. Même pas longtemps. → `s2_016`

`s2_016` **Sarah** : Je ne veux pas faire la police. Je veux juste retrouver le calme avec toi. → `s2_017`

**CHOIX** `s2_017` — Sarah demande un moment sans téléphone.
- 1. `s2_017_a` → D’accord. Téléphone loin de la table. _(next: `s2_018_a`)_
- 2. `s2_017_b` → Je peux essayer, mais j’attends peut-être un message pro. _(next: `s2_018_b`)_
- 3. `s2_017_c` → On peut juste éviter d’en faire un symbole ? _(next: `s2_018_c`)_

`s2_018_a` **Vous** : D’accord. Téléphone loin de la table. → `s2_019_a`

`s2_019_a` **Sarah** : Merci. Vraiment. → `s2_block_c`

`s2_018_b` **Vous** : Je peux essayer, mais j’attends peut-être un message pro. → `s2_019_b`

`s2_019_b` **Sarah** : Peut-être. Pro. Encore des mots qui laissent de la place à tout. → `s2_block_c`

`s2_018_c` **Vous** : On peut juste éviter d’en faire un symbole ? → `s2_019_c`

`s2_019_c` **Sarah** : Je n’essaye pas de gagner un débat. J’aimerais juste ne pas me sentir idiote d’attendre ton message. → `s2_block_c`

`s2_block_c` **Système** : S2C — Doute formulé doucement → `s2_020`

`s2_020` **Sarah** : Je viens de relire nos messages d’aujourd’hui. → `s2_021`

`s2_021` **Sarah** : Il y a des moments où tu es tendre, et d’autres où j’ai l’impression de parler à quelqu’un qui regarde ailleurs. → `s2_022`

`s2_022` **Sarah** : Je ne veux pas te coincer. Je veux comprendre où tu es, là, maintenant. → `s2_023`

**CHOIX** `s2_023` — Point de bascule Sarah J2.
- 1. `s2_023_a` → Je suis avec toi. Je vais faire mieux ce soir. _(next: `s2_end_presence`)_
- 2. `s2_023_b` → Je suis perdu, mais ce n’est pas contre toi. _(next: `s2_end_fragile`)_
- 3. `s2_023_c` → Je ne peux pas parler de ça maintenant. _(next: `s2_end_distance`)_

`s2_end_presence` **[FIN]** **Système** : Fin Sarah J2 : tu promets une présence. Sarah veut y croire, mais le moindre délai comptera plus qu’avant.

`s2_end_fragile` **[FIN]** **Système** : Fin Sarah J2 : tu n’avoues rien, mais tu cesses de jouer lisse. Sarah reste là, prudente.

`s2_end_distance` **[FIN]** **Système** : Fin Sarah J2 : tu repousses encore. Sarah ne force pas. C’est précisément ce qui rend son silence plus lourd.

---

# Jour 3

## Camille — `camille_j3_complete`

Source: `narrative/t075_camille_j3_complete.json`  
Start: `c3_block_a`

`c3_block_a` **Système** : C3A — Reprise selon J2 → `c3_001`

`c3_001` **Camille** : Je marche depuis dix minutes. Même rue, mêmes vitrines. Je me demandais si aujourd’hui tu allais faire comme si hier n’avait pas existé. → `c3_002`

`c3_002` **Camille** : Tu sais, les dix minutes. Le fil gardé ouvert. Ou la limite posée avec un air raisonnable, comme un téléphone retourné sur une table. → `c3_003`

**CHOIX** `c3_003` — Camille revient sur J2 sans nommer la route exacte.
- 1. `c3_003_a` → Je n’ai pas fait semblant. J’y ai pensé. _(next: `c3_004_a`)_
- 2. `c3_003_b` → Je préfère ne pas trop repenser à ça. _(next: `c3_004_b`)_
- 3. `c3_003_c` → Tu veux vraiment savoir ce que ça a changé ? _(next: `c3_004_c`)_

`c3_004_a` **Vous** : Je n’ai pas fait semblant. J’y ai pensé. → `c3_005_a`

`c3_005_a` **Camille** : Bien. Je préfère être une pensée gênante qu’un message oublié. Les pensées gênantes tiennent mieux sous la pluie. → `c3_006`

`c3_004_b` **Vous** : Je préfère ne pas trop repenser à ça. → `c3_005_b`

`c3_005_b` **Camille** : C’est drôle, les gens disent ça quand ils y repensent déjà trop. Ça sonnait presque vrai, en plus. → `c3_006`

`c3_004_c` **Vous** : Tu veux vraiment savoir ce que ça a changé ? → `c3_005_c`

`c3_005_c` **Camille** : Oui. Mais je préfère quand tu hésites avant de répondre. → `c3_006`

`c3_006` **Camille** : Aujourd’hui je n’ai pas beaucoup de temps. Le café ferme tôt, et moi aussi, apparemment. C’est peut-être mieux comme ça. → `c3_007`

**CHOIX** `c3_007` — Camille pose une fenêtre courte, presque légère, avant que ça redevienne sérieux.
- 1. `c3_007_a` → Mieux pour qui ? Pour toi, pour moi, ou pour le café qui nous supporte ? _(next: `c3_008_a`)_
- 2. `c3_007_b` → Tu rends ça dangereux exprès. _(next: `c3_008_b`)_
- 3. `c3_007_c` → Alors ne commence pas si tu dois disparaître. _(next: `c3_008_c`)_

`c3_008_a` **Vous** : Mieux pour qui ? Pour toi, pour moi, ou pour le café qui nous supporte ? → `c3_009_a`

`c3_009_a` **Camille** : Pour celui qui prétend encore pouvoir gérer son attention. → `c3_block_b`

`c3_008_b` **Vous** : Tu rends ça dangereux exprès. → `c3_009_b`

`c3_009_b` **Camille** : Non. Je retire juste les endroits où tu peux te cacher. → `c3_block_b`

`c3_008_c` **Vous** : Alors ne commence pas si tu dois disparaître. → `c3_009_c`

`c3_009_c` **Camille** : Trop tard. Tu as déjà lu. → `c3_block_b`

`c3_block_b` **Système** : C3B — Fenêtre courte → `c3_010`

`c3_010` **Camille** : Je suis dans une boutique où ils passent une chanson beaucoup trop calme pour mon humeur. → `c3_011`

`c3_011` **Camille** : Je pars dans douze minutes. Après, je coupe mon téléphone jusqu’à ce soir. → `c3_012`

**CHOIX** `c3_012` — La fenêtre courte force un arbitrage d’attention.
- 1. `c3_012_a` → Alors ces douze minutes comptent. _(next: `c3_013_a`)_
- 2. `c3_012_b` → Je ne peux pas être disponible sur commande. _(next: `c3_013_b`)_
- 3. `c3_012_c` → Écris-moi une seule chose que je ne pourrai pas ignorer. _(next: `c3_013_c`)_

`c3_013_a` **Vous** : Alors ces douze minutes comptent. → `c3_014_a`

`c3_014_a` **Camille** : Je savais que tu comprenais très bien les choses quand elles deviennent courtes. → `c3_015`

`c3_013_b` **Vous** : Je ne peux pas être disponible sur commande. → `c3_014_b`

`c3_014_b` **Camille** : Je ne commande pas. Je constate à quelle vitesse tu réponds quand tu dis non. → `c3_015`

`c3_013_c` **Vous** : Écris-moi une seule chose que je ne pourrai pas ignorer. → `c3_014_c`

`c3_014_c` **Camille** : D’accord. J’ai aimé attendre ton message hier. Voilà, c’est dit. → `c3_015`

`c3_015` **Système** : Pendant quelques minutes, aucun autre message n’arrive. C’est presque pire : toute ton attention reste suspendue à cette fenêtre. → `c3_016`

`c3_016` **Camille** : Il me reste cinq minutes. → `c3_017`

`c3_017` **Camille** : Je voulais voir si tu pouvais me garder dans un coin de ta journée sans que je sois juste une distraction. → `c3_018`

**CHOIX** `c3_018` — Camille demande une place, pas un rendez-vous.
- 1. `c3_018_a` → Tu prends déjà plus qu’un coin. _(next: `c3_019_a`)_
- 2. `c3_018_b` → Je ne peux pas te donner plus que des messages. _(next: `c3_019_b`)_
- 3. `c3_018_c` → Je ne sais pas ce que je peux te donner. _(next: `c3_019_c`)_

`c3_019_a` **Vous** : Tu prends déjà plus qu’un coin. → `c3_020_a`

`c3_020_a` **Camille** : C’est le genre de phrase qu’on regrette seulement après l’avoir relue. → `c3_block_c`

`c3_019_b` **Vous** : Je ne peux pas te donner plus que des messages. → `c3_020_b`

`c3_020_b` **Camille** : Les messages suffisent parfois à déplacer quelqu’un. Tu devrais le savoir maintenant. → `c3_block_c`

`c3_019_c` **Vous** : Je ne sais pas ce que je peux te donner. → `c3_020_c`

`c3_020_c` **Camille** : Au moins, tu ne mens pas proprement. C’est presque rassurant. → `c3_block_c`

`c3_block_c` **Système** : C3C — Ce qui reste après le silence → `c3_021`

`c3_021` **Camille** : Je n’ai pas coupé tout de suite. → `c3_022`

`c3_022` **Camille** : Je voulais voir si ça te ferait quelque chose de savoir que j’avais menti sur les cinq minutes. → `c3_023`

`c3_023` **Camille** : Pas une grande invention. Juste assez pour rester près de la porte, là où tu pouvais encore répondre sans entrer vraiment. → `c3_024`

**CHOIX** `c3_024` — Fin Camille J3 : que faire de ce qui reste ?
- 1. `c3_024_a` → J’aurais répondu même après cinq minutes. _(next: `c3_end_pull`)_
- 2. `c3_024_b` → Ne fais pas ça. Pas avec moi. _(next: `c3_end_boundary`)_
- 3. `c3_024_c` → Je vais garder ce message. Je ne sais pas pourquoi. _(next: `c3_end_trace`)_

`c3_end_pull` **[FIN]** **Système** : Fin Camille J3 : tu confirmes que la fenêtre importe moins que le fil. Camille le sait maintenant.

`c3_end_boundary` **[FIN]** **Système** : Fin Camille J3 : tu poses une limite. Camille recule, mais le message reste dans la conversation.

`c3_end_trace` **[FIN]** **Système** : Fin Camille J3 : tu ne promets rien. Tu gardes quelque chose ouvert. C’est déjà une décision dangereuse.

## Sarah — `sarah_j3_complete`

Source: `narrative/t076_sarah_j3_complete.json`  
Start: `s3_block_a`

`s3_block_a` **Système** : S3A — Matin prudent → `s3_001`

`s3_001` **Sarah** : Je me suis réveillée avant toi. J’ai failli t’écrire, puis je me suis dit que ça ferait trop. → `s3_002`

`s3_002` **Sarah** : Alors j’ai attendu un peu. C’est idiot comme stratégie, non ? → `s3_003`

**CHOIX** `s3_003` — Sarah ouvre la journée avec prudence.
- 1. `s3_003_a` → Non. J’aime bien que tu m’écrives. _(next: `s3_004_a`)_
- 2. `s3_003_b` → Je suis un peu débordé ce matin. _(next: `s3_004_b`)_
- 3. `s3_003_c` → Tu peux m’écrire sans calculer. _(next: `s3_004_c`)_

`s3_004_a` **Vous** : Non. J’aime bien que tu m’écrives. → `s3_005_a`

`s3_005_a` **Sarah** : Je vais essayer de le retenir sans en faire une preuve officielle. → `s3_006`

`s3_004_b` **Vous** : Je suis un peu débordé ce matin. → `s3_005_b`

`s3_005_b` **Sarah** : Oui. Je le sens. J’essaie juste de comprendre si je suis dans le débordement ou à côté. → `s3_006`

`s3_004_c` **Vous** : Tu peux m’écrire sans calculer. → `s3_005_c`

`s3_005_c` **Sarah** : C’est exactement le genre de phrase qui me donne envie d’y croire. → `s3_006`

`s3_006` **Sarah** : Je ne veux pas te prendre toute ta journée. Juste savoir si j’y ai encore une vraie place. → `s3_007`

**CHOIX** `s3_007` — Répondre au besoin de place.
- 1. `s3_007_a` → Tu as une place. Je dois juste mieux la montrer. _(next: `s3_008_a`)_
- 2. `s3_007_b` → Je ne sais pas comment répondre sans promettre trop. _(next: `s3_008_b`)_
- 3. `s3_007_c` → Là, tu dramatises un peu. _(next: `s3_008_c`)_

`s3_008_a` **Vous** : Tu as une place. Je dois juste mieux la montrer. → `s3_009_a`

`s3_009_a` **Sarah** : D’accord. Alors aujourd’hui je vais regarder les gestes, pas les grands mots. → `s3_block_b`

`s3_008_b` **Vous** : Je ne sais pas comment répondre sans promettre trop. → `s3_009_b`

`s3_009_b` **Sarah** : C’est peut-être mieux qu’une promesse automatique. Au moins je t’entends réfléchir. → `s3_block_b`

`s3_008_c` **Vous** : Là, tu dramatises un peu. → `s3_009_c`

`s3_009_c` **Sarah** : Peut-être. Mais je préférerais dramatiser avec toi que me calmer toute seule. → `s3_block_b`

`s3_block_b` **Système** : S3B — Petit rituel → `s3_010`

`s3_010` **Sarah** : Tu te souviens de la plante sur le rebord de la fenêtre ? Celle que tu as failli jeter parce qu’elle faisait “déprimée”. → `s3_011`

`s3_011` **Sarah** : Elle a une nouvelle feuille. Minuscule. J’ai pensé à toi, forcément. → `s3_012`

**CHOIX** `s3_012` — Sarah propose un rituel simple, loin du dîner et du téléphone.
- 1. `s3_012_a` → Décris-la-moi. Je veux la voir ce soir. _(next: `s3_013_a`)_
- 2. `s3_012_b` → Je suis étonné qu’elle ait survécu à nous deux. _(next: `s3_013_b`)_
- 3. `s3_012_c` → Je réponds plus tard, je suis en plein truc. _(next: `s3_013_c`)_

`s3_013_a` **Vous** : Décris-la-moi. Je veux la voir ce soir. → `s3_014_a`

`s3_014_a` **Sarah** : Description mentale : une feuille ridicule, beaucoup trop fière d’exister. → `s3_015`

`s3_013_b` **Vous** : Je suis étonné qu’elle ait survécu à nous deux. → `s3_014_b`

`s3_014_b` **Sarah** : Elle tient mieux que nous certains matins. Mais elle ne répond pas aux messages, ça aide. → `s3_015`

`s3_013_c` **Vous** : Je réponds plus tard, je suis en plein truc. → `s3_014_c`

`s3_014_c` **Sarah** : Ok. Je garde ma petite feuille pour plus tard alors. → `s3_015`

`s3_015` **Sarah** : Ce soir, tu pourras l’arroser ? Pas parce que c’est important. Juste parce que ça me ferait plaisir que ce soit toi. → `s3_016`

**CHOIX** `s3_016` — Le petit rituel devient un test de présence fiable.
- 1. `s3_016_a` → Oui. Je le ferai en rentrant. _(next: `s3_017_a`)_
- 2. `s3_016_b` → Rappelle-le-moi, j’ai peur d’oublier. _(next: `s3_017_b`)_
- 3. `s3_016_c` → Je ne sais pas à quelle heure je rentre. _(next: `s3_017_c`)_

`s3_017_a` **Vous** : Oui. Je le ferai en rentrant. → `s3_018_a`

`s3_018_a` **Sarah** : Je sais que c’est minuscule. Mais j’avais besoin d’un oui minuscule aujourd’hui. → `s3_block_c`

`s3_017_b` **Vous** : Rappelle-le-moi, j’ai peur d’oublier. → `s3_018_b`

`s3_018_b` **Sarah** : Je peux te le rappeler. J’aimerais juste ne pas avoir l’impression de te rappeler moi aussi. → `s3_block_c`

`s3_017_c` **Vous** : Je ne sais pas à quelle heure je rentre. → `s3_018_c`

`s3_018_c` **Sarah** : D’accord. Je vais essayer de ne pas traduire ça trop vite dans ma tête. → `s3_block_c`

`s3_block_c` **Système** : S3C — Doute doux → `s3_019`

`s3_019` **Sarah** : Je crois que ce qui me fatigue, ce n’est pas quand tu es absent. → `s3_020`

`s3_020` **Sarah** : C’est quand je ne sais pas si je dois t’attendre, t’excuser, ou faire comme si ça ne me touchait pas. → `s3_021`

`s3_021` **Sarah** : Je ne veux pas devenir quelqu’un qui compte les minutes. Je veux juste savoir si tu fais attention à nous. → `s3_022`

**CHOIX** `s3_022` — Fin Sarah J3 : répondre au doute doux.
- 1. `s3_022_a` → Oui. Et je vais te le prouver avec des gestes, pas des excuses. _(next: `s3_end_presence`)_
- 2. `s3_022_b` → Je fais attention, mais je suis mauvais pour le montrer. _(next: `s3_end_fragile`)_
- 3. `s3_022_c` → Je ne peux pas gérer ça maintenant. _(next: `s3_end_distance`)_

`s3_end_presence` **[FIN]** **Système** : Fin Sarah J3 : tu choisis le geste concret. Sarah ne demande pas plus pour l’instant, mais elle attendra de voir.

`s3_end_fragile` **[FIN]** **Système** : Fin Sarah J3 : tu restes imparfait mais lisible. Pour Sarah, c’est déjà moins seul.

`s3_end_distance` **[FIN]** **Système** : Fin Sarah J3 : tu repousses le moment. Sarah ne force pas. Elle commence juste à se protéger.

---

# Jour 4

## Camille — `camille_j4_complete`

Source: `narrative/t092_camille_j4_complete.json`  
Start: `c4_block_a`

`c4_block_a` **Système** : C4A — Camille : une fenêtre qui s’ouvre → `c4_001`

`c4_001` **Camille** : Je viens de passer devant le café aux tables bancales. Celui où on ne se croise jamais par hasard. → `c4_002`

`c4_002` **Camille** : J’ai pensé à toi. Pas au café. Pas à hier. Au moment précis où quelqu’un regarde une porte et prétend réfléchir à autre chose. → `c4_003`

**CHOIX** `c4_003` — Camille teste si J4 devient concret.
- 1. `c4_003_a` → Tu as choisi l’endroit exprès ? _(next: `c4_004_a`)_
- 2. `c4_003_b` → Aujourd’hui je dois rester prudent. _(next: `c4_004_b`)_
- 3. `c4_003_c` → Dis-moi juste combien de temps elle reste ouverte. _(next: `c4_004_c`)_

`c4_004_a` **Vous** : Tu as choisi l’endroit exprès ? → `c4_005_a`

`c4_005_a` **Camille** : J’ai surtout choisi un endroit où tu ne peux pas répondre “c’est compliqué” sans que la table entière se moque de toi. → `c4_006`

`c4_004_b` **Vous** : Aujourd’hui je dois rester prudent. → `c4_005_b`

`c4_005_b` **Camille** : Prudent, c’est joli. Ça veut parfois dire que tu as déjà imaginé le contraire. → `c4_006`

`c4_004_c` **Vous** : Dis-moi juste combien de temps elle reste ouverte. → `c4_005_c`

`c4_005_c` **Camille** : Voilà. Là tu regardes la porte. C’est plus honnête que de commenter la poignée. → `c4_006`

`c4_006` **Camille** : Quarante minutes. Fin d’après-midi. Table du fond, café trop fort. Juste assez loin de tes habitudes pour que tu hésites déjà. → `c4_007`

**CHOIX** `c4_007` — Répondre à la fenêtre concrète de Camille.
- 1. `c4_007_a` → Je peux peut-être disparaître quarante minutes. _(next: `c4_008_a`)_
- 2. `c4_007_b` → J’ai pas envie de passer ma soirée à regarder derrière moi. _(next: `c4_008_b`)_
- 3. `c4_007_c` → Si on le fait, personne ne doit pouvoir le lire après. _(next: `c4_008_c`)_

`c4_008_a` **Vous** : Je peux peut-être disparaître quarante minutes. → `c4_009_a`

`c4_009_a` **Camille** : “Peut-être disparaître”, c’est presque une promesse quand ça vient de toi. → `c4_block_b`

`c4_008_b` **Vous** : J’ai pas envie de passer ma soirée à regarder derrière moi. → `c4_009_b`

`c4_009_b` **Camille** : Alors efface l’idée. Mais ne fais pas semblant qu’elle n’a pas laissé de marque. → `c4_block_b`

`c4_008_c` **Vous** : Si on le fait, personne ne doit pouvoir le lire après. → `c4_009_c`

`c4_009_c` **Camille** : Tu vois ? Tu réponds déjà depuis le seuil, comme si entrer et repartir demandaient la même phrase. → `c4_block_b`

`c4_block_b` **Système** : C4B — Camille : une proposition plus difficile à ranger → `c4_010`

`c4_010` **Camille** : Je n’ai pas bougé. Je suis même arrivée trop tôt, ce qui est très mauvais signe. → `c4_011`

`c4_011` **Camille** : Je pourrais t’envoyer l’adresse. Ou je pourrais te laisser choisir de ne pas la demander. → `c4_012`

**CHOIX** `c4_012` — Camille met le joueur devant une demande explicite.
- 1. `c4_012_a` → Envoie. _(next: `c4_013_a`)_
- 2. `c4_012_b` → Ne l’envoie pas. Si je demande, ce sera déjà trop. _(next: `c4_013_b`)_
- 3. `c4_012_c` → Décris juste l’endroit, sans adresse. _(next: `c4_013_c`)_

`c4_013_a` **Vous** : Envoie. → `c4_014_a`

`c4_014_a` **Camille** : Tu sais que ce mot est beaucoup plus clair que toutes tes phrases raisonnables ? → `c4_015`

`c4_013_b` **Vous** : Ne l’envoie pas. Si je demande, ce sera déjà trop. → `c4_014_b`

`c4_014_b` **Camille** : Tu essaies encore de sauver une version de toi qui n’a pas ouvert cette conversation. → `c4_015`

`c4_013_c` **Vous** : Décris juste l’endroit, sans adresse. → `c4_014_c`

`c4_014_c` **Camille** : Un banc sombre, une vitrine fermée, un reflet où tu aurais l’air plus honnête si tu venais vraiment. → `c4_015`

`c4_015` **Camille** : Je ne te demande pas de choisir ta vie. Juste de voir si tu peux mentir à ton agenda sans te mentir à toi-même. → `c4_016`

**CHOIX** `c4_016` — Choisir comment gérer l’alibi immédiat.
- 1. `c4_016_a` → Je vais inventer un détour simple. _(next: `c4_017_a`)_
- 2. `c4_016_b` → Je ne veux pas mentir pour quarante minutes. _(next: `c4_017_b`)_
- 3. `c4_016_c` → Je peux rester en messages, pas plus. _(next: `c4_017_c`)_

`c4_017_a` **Vous** : Je vais inventer un détour simple. → `c4_018_a`

`c4_018_a` **Camille** : Simple, c’est le mot qu’on utilise avant que quelqu’un remarque un détail. → `c4_block_c`

`c4_017_b` **Vous** : Je ne veux pas mentir pour quarante minutes. → `c4_018_b`

`c4_018_b` **Camille** : Alors ne mens pas. Mais ne m’écris pas comme si tu étais déjà venu. → `c4_block_c`

`c4_017_c` **Vous** : Je peux rester en messages, pas plus. → `c4_018_c`

`c4_018_c` **Camille** : Les messages sont aussi des endroits. Certains sont plus compromettants que des rues. → `c4_block_c`

`c4_block_c` **Système** : C4C — Camille : ce qui reste après la fenêtre → `c4_019`

`c4_019` **Camille** : Je vais partir dans quelques minutes. Ça te laisse le temps d’être courageux, lâche, ou très poli. → `c4_020`

`c4_020` **Camille** : Je ne sais pas lequel m’agace le plus. → `c4_021`

**CHOIX** `c4_021` — Camille laisse la fenêtre ouverte dans la tête du joueur.
- 1. `c4_021_a` → Je n’ai pas été poli. J’ai eu peur. _(next: `c4_022_a`)_
- 2. `c4_021_b` → Reste encore un peu. _(next: `c4_022_b`)_
- 3. `c4_021_c` → Pars. Ce sera plus simple pour tout le monde. _(next: `c4_022_c`)_

`c4_022_a` **Vous** : Je n’ai pas été poli. J’ai eu peur. → `c4_023_a`

`c4_023_a` **Camille** : Ça, au moins, c’est une vraie phrase. Je peux faire quelque chose avec la peur. Pas avec les excuses. → `c4_024`

`c4_022_b` **Vous** : Reste encore un peu. → `c4_023_b`

`c4_023_b` **Camille** : Je reste. Mais maintenant c’est toi qui as créé l’attente, pas moi. → `c4_024`

`c4_022_c` **Vous** : Pars. Ce sera plus simple pour tout le monde. → `c4_023_c`

`c4_023_c` **Camille** : Simple, oui. Et étrangement pas très propre. → `c4_024`

`c4_024` **Camille** : Demain, je ne te demanderai pas si tu pouvais venir. Je te demanderai ce que tu as fait de cette possibilité. → `c4_025`

**CHOIX** `c4_025` — Clore Camille J4.
- 1. `c4_025_a` → Je veux garder cette possibilité ouverte. _(next: `c4_026_a`)_
- 2. `c4_025_b` → Je ne peux pas te promettre plus que des messages. _(next: `c4_026_b`)_
- 3. `c4_025_c` → Je dois refermer avant que ça déborde. _(next: `c4_026_c`)_

`c4_026_a` **Vous** : Je veux garder cette possibilité ouverte. → `c4_end_window`

`c4_end_window` **[FIN]** **Camille** : Alors garde-la bien. Les possibilités ouvertes finissent toujours par laisser entrer quelque chose.

`c4_026_b` **Vous** : Je ne peux pas te promettre plus que des messages. → `c4_end_trace`

`c4_end_trace` **[FIN]** **Camille** : Les messages suffisent parfois. Surtout quand ils disent exactement ce que tu refuses de faire.

`c4_026_c` **Vous** : Je dois refermer avant que ça déborde. → `c4_end_retreat`

`c4_end_retreat` **[FIN]** **Camille** : Referme. Je saurai quand même que tu as regardé par l’ouverture.

## Maya — `maya_j4_complete`

Source: `narrative/t093_maya_j4_complete.json`  
Start: `m4_block_a`

`m4_block_a` **Système** : M4A — Maya : regard social / remarque légère → `m4_001`

`m4_001` **Maya** : Je pose ça là : sur la photo de groupe, tu es techniquement “pas là”, mais ton épaule fait une carrière solo. → `m4_002`

`m4_002` **Maya** : C’est une compétence ? Une phase ? Ou juste ton nouveau mode camouflage social niveau amateur ? → `m4_003`

**CHOIX** `m4_003` — Maya remarque une absence sans accuser.
- 1. `m4_003_a` → Je suis juste un peu dispersé. Niveau photo floue, apparemment. _(next: `m4_004_a`)_
- 2. `m4_003_b` → Tu as remarqué ça comment ? _(next: `m4_004_b`)_
- 3. `m4_003_c` → Disons que je gère plusieurs trucs à la fois. _(next: `m4_004_c`)_

`m4_004_a` **Vous** : Je suis juste un peu dispersé. Niveau photo floue, apparemment. → `m4_005_a`

`m4_005_a` **Maya** : Oui, “dispersé”, c’est le mot poli pour dire que trois personnes demandent où tu es pendant que ton épaule répond à ta place. → `m4_006`

`m4_004_b` **Vous** : Tu as remarqué ça comment ? → `m4_005_b`

`m4_005_b` **Maya** : Parce que tu réponds vite aux mauvaises questions et lentement aux simples. Même le groupe a moins de flou sur ses photos. → `m4_006`

`m4_004_c` **Vous** : Disons que je gère plusieurs trucs à la fois. → `m4_005_c`

`m4_005_c` **Maya** : Ah. La phrase préférée des gens qui ont déjà perdu le fil mais refusent de lâcher un fil. → `m4_006`

`m4_006` **Maya** : Je ne te fais pas un interrogatoire. Je te dis juste que le “il est où ?” est parti trop vite. Trois têtes se sont tournées. Ambiance. → `m4_007`

**CHOIX** `m4_007` — Réagir au regard social de Maya sans lui donner un rôle de vigile.
- 1. `m4_007_a` → Et toi, tu as rempli avec quoi ? _(next: `m4_008_a`)_
- 2. `m4_007_b` → Je préfère que personne ne remplisse rien. _(next: `m4_008_b`)_
- 3. `m4_007_c` → Si quelqu’un demande, tu peux juste dire que j’étais occupé. _(next: `m4_008_c`)_

`m4_008_a` **Vous** : Et toi, tu as rempli avec quoi ? → `m4_009_a`

`m4_009_a` **Maya** : Avec pas grand-chose. Pour l’instant. C’est ça qui devrait te rassurer ou t’inquiéter, je ne sais pas. → `m4_block_b`

`m4_008_b` **Vous** : Je préfère que personne ne remplisse rien. → `m4_009_b`

`m4_009_b` **Maya** : Alors évite de laisser des blancs pile là où tout le monde regarde. Conseil gratuit. → `m4_block_b`

`m4_008_c` **Vous** : Si quelqu’un demande, tu peux juste dire que j’étais occupé. → `m4_009_c`

`m4_009_c` **Maya** : Je peux. Mais note que tu viens de me demander une couverture avant même qu’on sache pour quoi. → `m4_block_b`

`m4_block_b` **Système** : M4B — Maya : petit détail vu trop vite → `m4_010`

`m4_010` **Maya** : Petit détail amusant : Nico m’a demandé si tu étais avec nous tout à l’heure, avec son visage de mec qui a perdu le script. → `m4_011`

`m4_011` **Maya** : Je lui ai dit “je crois”. Et je me suis entendue dire “je crois”. Tu vois le problème ? → `m4_012`

**CHOIX** `m4_012` — Maya pointe une micro-contradiction sociale.
- 1. `m4_012_a` → Nico dramatise toujours les absences. _(next: `m4_013_a`)_
- 2. `m4_012_b` → Merci de ne pas avoir creusé. _(next: `m4_013_b`)_
- 3. `m4_012_c` → Tu as dit quoi exactement ? _(next: `m4_013_c`)_

`m4_013_a` **Vous** : Nico dramatise toujours les absences. → `m4_014_a`

`m4_014_a` **Maya** : Peut-être. Mais là, ce n’est pas son ton qui m’a marquée. C’est ton réflexe de minimiser avant de savoir. → `m4_015`

`m4_013_b` **Vous** : Merci de ne pas avoir creusé. → `m4_014_b`

`m4_014_b` **Maya** : Je n’ai pas creusé parce que je t’aime bien. Ce qui n’est pas exactement une garantie durable. → `m4_015`

`m4_013_c` **Vous** : Tu as dit quoi exactement ? → `m4_014_c`

`m4_014_c` **Maya** : Que tu avais dû décrocher. C’est assez vague pour aider, assez précis pour devenir gênant si quelqu’un compare. → `m4_015`

`m4_015` **Maya** : Je ne veux pas savoir ce que tu faisais. Enfin… je veux savoir si tu comprends que ça déborde un peu autour de toi. → `m4_016`

**CHOIX** `m4_016` — Choisir jusqu’où se confier à Maya.
- 1. `m4_016_a` → J’ai besoin que tu ne poses pas trop de questions. _(next: `m4_017_a`)_
- 2. `m4_016_b` → Il y a des choses que je gère mal, oui. _(next: `m4_017_b`)_
- 3. `m4_016_c` → Je pensais que ça ne se voyait pas. _(next: `m4_017_c`)_

`m4_017_a` **Vous** : J’ai besoin que tu ne poses pas trop de questions. → `m4_018_a`

`m4_018_a` **Maya** : Alors formule mieux : tu as besoin que je choisisse de ne pas voir. Ce n’est pas pareil. → `m4_block_c`

`m4_017_b` **Vous** : Il y a des choses que je gère mal, oui. → `m4_018_b`

`m4_018_b` **Maya** : Ça, c’est une réponse que je peux respecter. Pas forcément couvrir, mais respecter. → `m4_block_c`

`m4_017_c` **Vous** : Je pensais que ça ne se voyait pas. → `m4_018_c`

`m4_018_c` **Maya** : En général c’est pas le gros truc qui grille quelqu’un. C’est trois petits détails que personne ne devait additionner. → `m4_block_c`

`m4_block_c` **Système** : M4C — Maya : service demandé, sourcil levé → `m4_019`

`m4_019` **Maya** : Je peux te rendre un service social minuscule : ne pas relever, ne pas répéter, ne pas faire la maligne. → `m4_020`

`m4_020` **Maya** : Mais je ne veux pas devenir le meuble derrière lequel tu caches tes trucs. → `m4_021`

**CHOIX** `m4_021` — Maya propose une couverture fragile sans devenir complice totale.
- 1. `m4_021_a` → Je ne te demanderai pas de mentir. _(next: `m4_022_a`)_
- 2. `m4_021_b` → Juste aujourd’hui. Après je remets de l’ordre. _(next: `m4_022_b`)_
- 3. `m4_021_c` → Tu peux aussi me dire si je deviens ridicule. _(next: `m4_022_c`)_

`m4_022_a` **Vous** : Je ne te demanderai pas de mentir. → `m4_023_a`

`m4_023_a` **Maya** : Bien. Parce que je mens très mal quand je trouve la personne en face plus bête que prévue. → `m4_024`

`m4_022_b` **Vous** : Juste aujourd’hui. Après je remets de l’ordre. → `m4_023_b`

`m4_023_b` **Maya** : “Juste aujourd’hui” est une phrase qui vieillit rarement bien. Mais d’accord, je note la date. → `m4_024`

`m4_022_c` **Vous** : Tu peux aussi me dire si je deviens ridicule. → `m4_023_c`

`m4_023_c` **Maya** : Tu n’es pas encore ridicule. Tu es au stade élégant du désordre. C’est plus dangereux. → `m4_024`

`m4_024` **Maya** : Si quelqu’un me demande, je resterai vague. Pas pour te sauver. Pour ne pas être celle qui pousse le premier domino. → `m4_025`

**CHOIX** `m4_025` — Clore Maya J4.
- 1. `m4_025_a` → Je te dois un vrai merci. _(next: `m4_026_a`)_
- 2. `m4_025_b` → Reste vague, c’est tout ce que je demande. _(next: `m4_026_b`)_
- 3. `m4_025_c` → Je vais éviter de te mêler à ça. _(next: `m4_026_c`)_

`m4_026_a` **Vous** : Je te dois un vrai merci. → `m4_end_gratitude`

`m4_end_gratitude` **[FIN]** **Maya** : Garde-le pour le moment où tu auras une explication qui ne tremble pas. Là, ce sera utile.

`m4_026_b` **Vous** : Reste vague, c’est tout ce que je demande. → `m4_end_cover`

`m4_end_cover` **[FIN]** **Maya** : Je resterai vague. Mais les gens vagues finissent parfois par attirer les questions précises.

`m4_026_c` **Vous** : Je vais éviter de te mêler à ça. → `m4_end_distance`

`m4_end_distance` **[FIN]** **Maya** : Bonne idée. Commence par éviter que ton silence fasse toute la conversation à ta place.

## Inès — `ines_j4_complete`

Source: `narrative/t094_ines_j4_complete.json`  
Start: `i4_block_a`

`i4_block_a` **Système** : I4A — Inès : entrée trouble / perturbation → `i4_001`

`i4_001` **Inès** : J’ai hésité avant d’envoyer. Du coup j’envoie avant de re-hésiter : je crois que je viens de tomber sur une version un peu arrangée de toi. → `i4_002`

`i4_002` **Inès** : Ou alors tu as un talent rare pour être vu à des endroits où tu n’es officiellement pas passé. Ça m’est revenu dans le trajet. → `i4_003`

**CHOIX** `i4_003` — Inès apparaît avec une observation ambiguë.
- 1. `i4_003_a` → Ça dépend de ce que tu appelles une version arrangée. _(next: `i4_004_a`)_
- 2. `i4_003_b` → Tu m’as vu où ? _(next: `i4_004_b`)_
- 3. `i4_003_c` → Je pense que tu confonds avec quelqu’un. _(next: `i4_004_c`)_

`i4_004_a` **Vous** : Ça dépend de ce que tu appelles une version arrangée. → `i4_005_a`

`i4_005_a` **Inès** : Elle tient debout, ta version. Elle penche juste un peu quand on la regarde de côté, comme un reflet dans une vitrine de nuit. → `i4_006`

`i4_004_b` **Vous** : Tu m’as vu où ? → `i4_005_b`

`i4_005_b` **Inès** : Près d’un passage où les gens pressés regardent leurs chaussures. Le bus a raté mon arrêt, ou moi le sien, et toi tu regardais ton écran comme s’il contenait une sortie. → `i4_006`

`i4_004_c` **Vous** : Je pense que tu confonds avec quelqu’un. → `i4_005_c`

`i4_005_c` **Inès** : Possible. Mais la personne qui te ressemble a aussi ta façon de répondre trop proprement. → `i4_006`

`i4_006` **Inès** : Rassure-toi, je ne fais pas de rapport. Je voulais juste vérifier que je n’avais pas inventé ce moment bizarre entre toi, ton écran, et la vitrine. → `i4_007`

**CHOIX** `i4_007` — Réagir à la curiosité d’Inès sans fermer la porte trop fort.
- 1. `i4_007_a` → Tu remarques toujours les gens dans les trajets comme ça ? _(next: `i4_008_a`)_
- 2. `i4_007_b` → Je préfère rester une seule version, merci. _(next: `i4_008_b`)_
- 3. `i4_007_c` → Deux versions, c’est parfois pratique. _(next: `i4_008_c`)_

`i4_008_a` **Vous** : Tu remarques toujours les gens dans les trajets comme ça ? → `i4_009_a`

`i4_009_a` **Inès** : Seulement quand ils ne se comportent pas comme des inconnus pour tout le monde. → `i4_block_b`

`i4_008_b` **Vous** : Je préfère rester une seule version, merci. → `i4_009_b`

`i4_009_b` **Inès** : Alors elle a dû se fatiguer, cette version. Parce qu’elle avait l’air de courir après quelque chose. → `i4_block_b`

`i4_008_c` **Vous** : Deux versions, c’est parfois pratique. → `i4_009_c`

`i4_009_c` **Inès** : Pratique, oui. Jusqu’au moment où quelqu’un parle à la mauvaise. → `i4_block_b`

`i4_block_b` **Système** : I4B — Inès : intérêt ambigu / déséquilibre → `i4_010`

`i4_010` **Inès** : Je suis dans le coin encore vingt minutes. Pas pour toi, officiellement. J’ai un ticket froissé dans la poche qui prétend le contraire. → `i4_011`

`i4_011` **Inès** : Mais si tu passes devant la même vitrine que tout à l’heure, je saurai peut-être si je dois continuer à être curieuse. → `i4_012`

**CHOIX** `i4_012` — Inès ouvre une proximité avec porte de sortie sociale.
- 1. `i4_012_a` → Tu me proposes un hasard organisé ? _(next: `i4_013_a`)_
- 2. `i4_012_b` → Je ne suis pas disponible pour ce genre de hasard. _(next: `i4_013_b`)_
- 3. `i4_012_c` → Je peux passer sans m’arrêter. _(next: `i4_013_c`)_

`i4_013_a` **Vous** : Tu me proposes un hasard organisé ? → `i4_014_a`

`i4_014_a` **Inès** : Je propose une phrase qui reste défendable si quelqu’un la relit. C’est plus élégant. → `i4_015`

`i4_013_b` **Vous** : Je ne suis pas disponible pour ce genre de hasard. → `i4_014_b`

`i4_014_b` **Inès** : Dommage. Tu avais pourtant l’air de quelqu’un qui se retrouve souvent au mauvais endroit au bon moment. → `i4_015`

`i4_013_c` **Vous** : Je peux passer sans m’arrêter. → `i4_014_c`

`i4_014_c` **Inès** : Passer sans s’arrêter, c’est souvent ce que les gens font quand ils veulent vérifier qu’ils auraient pu. → `i4_015`

`i4_015` **Inès** : Je ne te demande rien de compromettant. Juste un signe que je n’ai pas inventé ton air pressé. → `i4_016`

**CHOIX** `i4_016` — Décider quel signe laisser à Inès.
- 1. `i4_016_a` → Je peux t’envoyer un signe quand je passe. _(next: `i4_017_a`)_
- 2. `i4_016_b` → Aucun signe, c’est plus sûr. _(next: `i4_017_b`)_
- 3. `i4_016_c` → Tu n’as pas inventé. Mais ça doit rester léger. _(next: `i4_017_c`)_

`i4_017_a` **Vous** : Je peux t’envoyer un signe quand je passe. → `i4_018_a`

`i4_018_a` **Inès** : Un signe, alors. Pas un dossier. Les dossiers vieillissent mal. → `i4_block_c`

`i4_017_b` **Vous** : Aucun signe, c’est plus sûr. → `i4_018_b`

`i4_018_b` **Inès** : Tu es prudent. Ou tu as déjà trop de choses à effacer. Je vais choisir la version flatteuse. → `i4_block_c`

`i4_017_c` **Vous** : Tu n’as pas inventé. Mais ça doit rester léger. → `i4_018_c`

`i4_018_c` **Inès** : Léger, c’est bien. Ça permet aux choses de flotter avant de tomber quelque part. → `i4_block_c`

`i4_block_c` **Système** : I4C — Inès : clôture de tension J4 / promesse de complication → `i4_019`

`i4_019` **Inès** : Je pars. Avant que cette conversation devienne une chose qu’il faudrait expliquer avec trop de détails. → `i4_020`

`i4_020` **Inès** : Mais je garde ton air pressé en mémoire. Pas comme dossier. Comme question. → `i4_021`

**CHOIX** `i4_021` — Inès laisse une question ouverte pour J5.
- 1. `i4_021_a` → Et si je réponds à la question plus tard ? _(next: `i4_022_a`)_
- 2. `i4_021_b` → Oublie mon air pressé. _(next: `i4_022_b`)_
- 3. `i4_021_c` → Garde seulement la version qui te plaît. _(next: `i4_022_c`)_

`i4_022_a` **Vous** : Et si je réponds à la question plus tard ? → `i4_023_a`

`i4_023_a` **Inès** : Alors je déciderai si j’aime mieux tes réponses ou tes esquives. Pour l’instant, les deux se défendent. → `i4_024`

`i4_022_b` **Vous** : Oublie mon air pressé. → `i4_023_b`

`i4_023_b` **Inès** : Je peux oublier une phrase. Une silhouette qui se contredit, c’est plus difficile. → `i4_024`

`i4_022_c` **Vous** : Garde seulement la version qui te plaît. → `i4_023_c`

`i4_023_c` **Inès** : C’est dangereux de laisser quelqu’un choisir ta meilleure version. On finit par vouloir la vérifier. → `i4_024`

`i4_024` **Inès** : Demain, si on se recroise, je ferai semblant que c’est normal. Tu pourras faire semblant aussi, si tu es encore doué. → `i4_025`

**CHOIX** `i4_025` — Clore Inès J4.
- 1. `i4_025_a` → Je suis assez doué pour ça. _(next: `i4_026_a`)_
- 2. `i4_025_b` → Je préfère qu’on ne teste pas trop. _(next: `i4_026_b`)_
- 3. `i4_025_c` → Si on se recroise, ce sera peut-être moins normal que prévu. _(next: `i4_026_c`)_

`i4_026_a` **Vous** : Je suis assez doué pour ça. → `i4_end_open`

`i4_end_open` **[FIN]** **Inès** : Alors attention. Les gens doués attirent plus facilement ceux qui veulent les voir rater.

`i4_026_b` **Vous** : Je préfère qu’on ne teste pas trop. → `i4_end_boundary`

`i4_end_boundary` **[FIN]** **Inès** : Sage. Ou déjà occupé ailleurs. Je ne choisirai pas encore.

`i4_026_c` **Vous** : Si on se recroise, ce sera peut-être moins normal que prévu. → `i4_end_complication`

`i4_end_complication` **[FIN]** **Inès** : Je note le “peut-être”. C’est souvent là que les vrais ennuis commencent.

## Nico — `nico_j4_complete`

Source: `narrative/t095_nico_j4_complete.json`  
Start: `n4_block_a`

`n4_block_a` **Système** : N4A — Nico : confident ou couverture → `n4_001`

`n4_001` **Nico** : Question simple : tu es en train de gérer ta journée ou de la perdre avec panache ? Je pose mon sandwich pour suivre, c’est dire. → `n4_002`

`n4_002` **Nico** : Je demande parce que Maya m’a répondu “je crois” quand j’ai demandé si tu étais avec nous. “Je crois”, c’est rarement bon signe. Même mon sandwich doute. → `n4_003`

**CHOIX** `n4_003` — Nico repère que le joueur jongle avec trop de choses.
- 1. `n4_003_a` → Tu dramatises pour un “je crois”, ou je dois vraiment poser mon sandwich ? _(next: `n4_004_a`)_
- 2. `n4_003_b` → J’ai juste besoin que tu ne poses pas trop de questions. _(next: `n4_004_b`)_
- 3. `n4_003_c` → Je crois que je commence à mal gérer, oui. _(next: `n4_004_c`)_

`n4_004_a` **Vous** : Tu dramatises pour un “je crois”, ou je dois vraiment poser mon sandwich ? → `n4_005_a`

`n4_005_a` **Nico** : Non, je dramatise quand tu réponds comme un mec qui a déjà préparé trois versions. Là, je m’échauffe à peine, niveau résumé de match nul. → `n4_006`

`n4_004_b` **Vous** : J’ai juste besoin que tu ne poses pas trop de questions. → `n4_005_b`

`n4_005_b` **Nico** : Donc tu veux le service “pote aveugle mais disponible”. C’est plus cher que prévu, et j’accepte pas les paiements en stress. → `n4_006`

`n4_004_c` **Vous** : Je crois que je commence à mal gérer, oui. → `n4_005_c`

`n4_005_c` **Nico** : Ah. Voilà une phrase utile. Inquiétante, mais utile. → `n4_006`

`n4_006` **Nico** : Je peux couvrir un retard, pas devenir ton standard de crise. À un moment je vais finir par oublier quelle version je suis censé raconter. → `n4_007`

**CHOIX** `n4_007` — Demander ou refuser une couverture.
- 1. `n4_007_a` → J’ai besoin d’une couverture simple, juste aujourd’hui. _(next: `n4_008_a`)_
- 2. `n4_007_b` → Non. Je ne veux pas t’embarquer là-dedans. _(next: `n4_008_b`)_
- 3. `n4_007_c` → Tu peux surtout me dire si je deviens ridicule. Version pote, pas conférence TED. _(next: `n4_008_c`)_

`n4_008_a` **Vous** : J’ai besoin d’une couverture simple, juste aujourd’hui. → `n4_009_a`

`n4_009_a` **Nico** : “Simple” et “juste aujourd’hui”, les deux phrases qui finissent toujours en formulaire. Mais d’accord, j’écoute. → `n4_block_b`

`n4_008_b` **Vous** : Non. Je ne veux pas t’embarquer là-dedans. → `n4_009_b`

`n4_009_b` **Nico** : C’est presque mature. Ça me perturbe. Continue, je vais peut-être m’y faire. → `n4_block_b`

`n4_008_c` **Vous** : Tu peux surtout me dire si je deviens ridicule. Version pote, pas conférence TED. → `n4_009_c`

`n4_009_c` **Nico** : Pas encore. Là tu es dans la zone chic du chaos. Après, ça devient très vite une chemise mal boutonnée. → `n4_block_b`

`n4_block_b` **Système** : N4B — Nico : conseil / provocation / avertissement → `n4_010`

`n4_010` **Nico** : Alors, diagnostic de pote : ton plan tient avec du scotch, ma mauvaise foi, et un sandwich que je n’ai toujours pas fini. → `n4_011`

`n4_011` **Nico** : C’est une performance, mais pas dans le sens où tu l’espères. → `n4_012`

**CHOIX** `n4_012` — Nico pousse le joueur à choisir son attitude.
- 1. `n4_012_a` → Je maîtrise plus que tu crois. _(next: `n4_013_a`)_
- 2. `n4_012_b` → J’ai besoin d’un vrai conseil, pas d’une vanne. _(next: `n4_013_b`)_
- 3. `n4_012_c` → Si tu sais quelque chose, dis-le clairement. _(next: `n4_013_c`)_

`n4_013_a` **Vous** : Je maîtrise plus que tu crois. → `n4_014_a`

`n4_014_a` **Nico** : Phrase de mec qui va confondre “maîtriser” et “avoir eu de la chance jusqu’ici”. → `n4_015`

`n4_013_b` **Vous** : J’ai besoin d’un vrai conseil, pas d’une vanne. → `n4_014_b`

`n4_014_b` **Nico** : Vrai conseil : choisis ce que tu veux protéger avant de choisir ce que tu veux obtenir. Sinon tu vas tout traiter comme un obstacle. → `n4_015`

`n4_013_c` **Vous** : Si tu sais quelque chose, dis-le clairement. → `n4_014_c`

`n4_014_c` **Nico** : Je sais surtout que tu changes de sujet quand un nom arrive trop près d’un autre. C’est pas un dossier, c’est pire : c’est automatique. → `n4_015`

`n4_015` **Nico** : Et avant que tu demandes : non, je ne vais pas faire le flic. Mais si je dois mentir pour toi, je veux au moins savoir si je mens pour une erreur ou pour une habitude. → `n4_016`

**CHOIX** `n4_016` — Dire à Nico ce qu’il couvre vraiment.
- 1. `n4_016_a` → C’est une erreur qui s’allonge. _(next: `n4_017_a`)_
- 2. `n4_016_b` → C’est plus compliqué qu’une erreur. _(next: `n4_017_b`)_
- 3. `n4_016_c` → Tu n’as pas besoin de savoir. _(next: `n4_017_c`)_

`n4_017_a` **Vous** : C’est une erreur qui s’allonge. → `n4_018_a`

`n4_018_a` **Nico** : Alors coupe avant que ça ressemble à une décision. Les erreurs aiment bien se déguiser quand on les nourrit. → `n4_block_c`

`n4_017_b` **Vous** : C’est plus compliqué qu’une erreur. → `n4_018_b`

`n4_018_b` **Nico** : Oui, ça je l’avais deviné. “Compliqué” est souvent le mot qu’on met sur une chose simple qu’on ne veut pas payer. → `n4_block_c`

`n4_017_c` **Vous** : Tu n’as pas besoin de savoir. → `n4_018_c`

`n4_018_c` **Nico** : Exact. Mais alors tu n’as pas besoin de ma couverture non plus. Logique pénible, mais logique. → `n4_block_c`

`n4_block_c` **Système** : N4C — Nico : service rendu, limite posée → `n4_019`

`n4_019` **Nico** : Bon. Je vais rester vague si quelqu’un me demande. Pas héroïque, pas complice, juste vague. → `n4_020`

`n4_020` **Nico** : Mais retiens un truc : quand plusieurs personnes deviennent vagues autour de toi, ce n’est plus une couverture, c’est un nuage. Et les nuages, ça se voit. → `n4_021`

**CHOIX** `n4_021` — Nico accepte ou refuse de porter ton histoire une fois de plus.
- 1. `n4_021_a` → Je te revaudrai ça. _(next: `n4_022_a`)_
- 2. `n4_021_b` → Ne te mets pas en risque pour moi. _(next: `n4_022_b`)_
- 3. `n4_021_c` → Si tu restes vague, ça suffit. _(next: `n4_022_c`)_

`n4_022_a` **Vous** : Je te revaudrai ça. → `n4_023_a`

`n4_023_a` **Nico** : Tu me revaudras surtout une conversation où tu ne comptes pas mes silences comme des services. → `n4_024`

`n4_022_b` **Vous** : Ne te mets pas en risque pour moi. → `n4_023_b`

`n4_023_b` **Nico** : Trop tard pour le zéro embrouille. Mais évite de filer des rôles aux gens sans les prévenir, quand même. → `n4_024`

`n4_022_c` **Vous** : Si tu restes vague, ça suffit. → `n4_023_c`

`n4_023_c` **Nico** : Ça suffit aujourd’hui. Les phrases comme ça ont une date de péremption courte. → `n4_024`

`n4_024` **Nico** : Demain, soit tu clarifies un minimum, soit tu deviens le mec dont tout le monde protège une version différente. Et crois-moi, ça finit mal dans les groupes. → `n4_025`

**CHOIX** `n4_025` — Clore Nico J4.
- 1. `n4_025_a` → Demain je clarifie quelque chose. _(next: `n4_026_a`)_
- 2. `n4_025_b` → Demain je ferai surtout attention. _(next: `n4_026_b`)_
- 3. `n4_025_c` → Demain, tu n’auras peut-être rien à couvrir. _(next: `n4_026_c`)_

`n4_026_a` **Vous** : Demain je clarifie quelque chose. → `n4_end_clarify`

`n4_end_clarify` **[FIN]** **Nico** : Je note “quelque chose”. C’est flou, mais c’est déjà moins lâche que “on verra”.

`n4_026_b` **Vous** : Demain je ferai surtout attention. → `n4_end_cloud`

`n4_end_cloud` **[FIN]** **Nico** : Faire attention, ce n’est pas réparer. C’est juste marcher moins fort sur les morceaux.

`n4_026_c` **Vous** : Demain, tu n’auras peut-être rien à couvrir. → `n4_end_silence`

`n4_end_silence` **[FIN]** **Nico** : J’espère. Parce que je suis meilleur pour les vannes que pour les alibis propres.

---

# Jour 5

## Sarah — `sarah_j5_complete`

Source: `narrative/t107_sarah_j5_complete.json`  
Start: `s5_block_a`

`s5_block_a` **Système** : S5A — Sarah : retour du poids intime → `s5_001`

`s5_001` **Sarah** : J’ai laissé la petite lumière de la cuisine. Je sais pas pourquoi. Ça faisait moins vide. → `s5_002`

`s5_002` **Sarah** : Je sais que tu as beaucoup de choses en ce moment. Mais parfois j’ai l’impression d’être le message que tu ouvres quand tout le reste est fini. → `s5_003`

**CHOIX** `s5_003` — Sarah parle d’un soir trop silencieux sans accuser.
- 1. `s5_003_a` → Tu n’es pas un reste. Je suis juste mauvais pour le montrer. _(next: `s5_004_a`)_
- 2. `s5_003_b` → Je suis crevé, mais j’ai envie de te retrouver un peu. _(next: `s5_004_b`)_
- 3. `s5_003_c` → Tu lis trop dans mes silences. _(next: `s5_004_c`)_

`s5_004_a` **Vous** : Tu n’es pas un reste. Je suis juste mauvais pour le montrer. → `s5_005_a`

`s5_005_a` **Sarah** : Je préfère cette phrase-là à une phrase parfaite. Au moins elle ne marche pas sur la pointe des pieds dans l’appartement. → `s5_006`

`s5_004_b` **Vous** : Je suis crevé, mais j’ai envie de te retrouver un peu. → `s5_005_b`

`s5_005_b` **Sarah** : Je peux entendre la fatigue. J’ai plus de mal quand elle prend toute la place, même sur le canapé, et qu’il ne reste que des réponses courtes. → `s5_006`

`s5_004_c` **Vous** : Tu lis trop dans mes silences. → `s5_005_c`

`s5_005_c` **Sarah** : Peut-être. Mais quand il y a plus de silence que de gestes, je finis par faire avec ce que j’ai. → `s5_006`

`s5_006` **Sarah** : Hier, tu as eu l’air là par moments. Puis très loin. J’ai gardé ta part au frigo comme si ça allait répondre à ma place. → `s5_007`

**CHOIX** `s5_007` — Répondre avec une phrase qui peut tenir dans la cuisine, pas seulement dans le téléphone.
- 1. `s5_007_a` → Je vais arrêter de te donner deux versions. _(next: `s5_008_a`)_
- 2. `s5_007_b` → Je ne peux pas tout expliquer, mais je peux être plus clair avec toi. _(next: `s5_008_b`)_
- 3. `s5_007_c` → Je ne veux pas qu’un soir où je rentre tard devienne forcément un sujet. _(next: `s5_008_c`)_

`s5_008_a` **Vous** : Je vais arrêter de te donner deux versions. → `s5_009_a`

`s5_009_a` **Sarah** : Alors commence petit. Pas avec une grande promesse. Avec un moment où ton téléphone reste posé et où je n’ai pas besoin de deviner. → `s5_block_b`

`s5_008_b` **Vous** : Je ne peux pas tout expliquer, mais je peux être plus clair avec toi. → `s5_009_b`

`s5_009_b` **Sarah** : C’est déjà une ligne plus honnête que “tout va bien”. Je peux partir de là. → `s5_block_b`

`s5_008_c` **Vous** : Je ne veux pas qu’un soir où je rentre tard devienne forcément un sujet. → `s5_009_c`

`s5_009_c` **Sarah** : Moi non plus. Je voudrais juste qu’elles arrêtent de se transformer toutes seules en distance. → `s5_block_b`

`s5_block_b` **Système** : S5B — Sarah : demande de présence concrète → `s5_010`

`s5_010` **Sarah** : Ce soir, j’ai besoin d’un vrai moment. Pas longtemps. Pas quelque chose d’organisé au millimètre. → `s5_011`

`s5_011` **Sarah** : Juste un moment où tu ne réponds pas comme si tu gardais une porte ouverte ailleurs. → `s5_012`

**CHOIX** `s5_012` — Sarah demande un signe concret de présence.
- 1. `s5_012_a` → Je serai là ce soir, vraiment. _(next: `s5_013_a`)_
- 2. `s5_012_b` → Je peux te promettre un moment, pas toute la soirée. _(next: `s5_013_b`)_
- 3. `s5_012_c` → Ce soir risque d’être compliqué. _(next: `s5_013_c`)_

`s5_013_a` **Vous** : Je serai là ce soir, vraiment. → `s5_014_a`

`s5_014_a` **Sarah** : D’accord. Je vais essayer de croire le “vraiment” sans le serrer trop fort. → `s5_015`

`s5_013_b` **Vous** : Je peux te promettre un moment, pas toute la soirée. → `s5_014_b`

`s5_014_b` **Sarah** : Un moment peut suffire si tu y es vraiment. Mais je crois que je saurai faire la différence. → `s5_015`

`s5_013_c` **Vous** : Ce soir risque d’être compliqué. → `s5_014_c`

`s5_014_c` **Sarah** : Voilà. C’est ce mot qui commence à me fatiguer. “Compliqué” ressemble de plus en plus à une porte fermée doucement. → `s5_015`

`s5_015` **Sarah** : Je ne te demande pas de tout me raconter. Je te demande d’arrêter de me laisser être la personne qui comprend après tout le monde. → `s5_016`

**CHOIX** `s5_016` — Choisir entre présence, demi-vérité ou esquive.
- 1. `s5_016_a` → Tu as raison. Je dois te remettre avant les excuses. _(next: `s5_017_a`)_
- 2. `s5_016_b` → Il y a des choses dont je ne suis pas fier. _(next: `s5_017_b`)_
- 3. `s5_016_c` → Je ne veux pas parler de ça maintenant. _(next: `s5_017_c`)_

`s5_017_a` **Vous** : Tu as raison. Je dois te remettre avant les excuses. → `s5_018_a`

`s5_018_a` **Sarah** : Alors je vais attendre un geste, pas une défense. Ça me semble plus sain pour nous deux. → `s5_block_c`

`s5_017_b` **Vous** : Il y a des choses dont je ne suis pas fier. → `s5_018_b`

`s5_018_b` **Sarah** : Je ne sais pas si ça me rassure. Mais au moins ce n’est pas une phrase qui essaie de m’endormir. → `s5_block_c`

`s5_017_c` **Vous** : Je ne veux pas parler de ça maintenant. → `s5_018_c`

`s5_018_c` **Sarah** : D’accord. Alors je vais arrêter de tirer sur une porte que tu tiens de l’autre côté. → `s5_block_c`

`s5_block_c` **Système** : S5C — Sarah : tension incompatible avec les autres fronts → `s5_019`

`s5_019` **Sarah** : Je vais faire simple : si tu as besoin d’air, dis-le. Si tu as besoin de moi, montre-le. → `s5_020`

`s5_020` **Sarah** : Mais entre les deux, je commence à me perdre un peu. → `s5_021`

**CHOIX** `s5_021` — Sarah pose une limite douce.
- 1. `s5_021_a` → J’ai besoin de toi. Je vais le montrer mieux. _(next: `s5_022_a`)_
- 2. `s5_021_b` → J’ai besoin d’air, mais pas loin de toi. _(next: `s5_022_b`)_
- 3. `s5_021_c` → Je ne sais plus très bien ce dont j’ai besoin. _(next: `s5_022_c`)_

`s5_022_a` **Vous** : J’ai besoin de toi. Je vais le montrer mieux. → `s5_023_a`

`s5_023_a` **Sarah** : Je veux te croire. Mais cette fois, je vais laisser tes gestes parler avant moi. → `s5_024`

`s5_022_b` **Vous** : J’ai besoin d’air, mais pas loin de toi. → `s5_023_b`

`s5_023_b` **Sarah** : C’est une phrase fragile. Je peux la recevoir, si tu ne t’en sers pas pour rester flou. → `s5_024`

`s5_022_c` **Vous** : Je ne sais plus très bien ce dont j’ai besoin. → `s5_023_c`

`s5_023_c` **Sarah** : Alors moi je vais essayer de ne pas devenir seulement une option parmi tes hésitations. → `s5_024`

`s5_024` **Sarah** : Ce soir, je serai là. Pas pour vérifier. Pour voir si on sait encore être simples ensemble. → `s5_025`

**CHOIX** `s5_025` — Clore Sarah J5.
- 1. `s5_025_a` → Je serai là pour quelque chose de simple. _(next: `s5_026_a`)_
- 2. `s5_025_b` → Je vais essayer. Je ne veux pas mentir avec une promesse trop nette. _(next: `s5_026_b`)_
- 3. `s5_025_c` → Si je n’y arrive pas, je te le dirai. _(next: `s5_026_c`)_

`s5_026_a` **Vous** : Je serai là pour quelque chose de simple. → `s5_end_presence`

`s5_end_presence` **[FIN]** **Sarah** : Alors garde ça. Pas comme une phrase à relire. Comme quelque chose à tenir quand le reste voudra t’emmener ailleurs.

`s5_026_b` **Vous** : Je vais essayer. Je ne veux pas mentir avec une promesse trop nette. → `s5_end_fragile`

`s5_end_fragile` **[FIN]** **Sarah** : Je préfère une vérité fragile à une belle promesse vide. Mais fragile, ça veut dire qu’il faudra en prendre soin.

`s5_026_c` **Vous** : Si je n’y arrive pas, je te le dirai. → `s5_end_distance`

`s5_end_distance` **[FIN]** **Sarah** : Dis-le avant que je le devine. Je crois que c’est tout ce que je peux encore demander sans me perdre.

## Camille — `camille_j5_complete`

Source: `narrative/t108_camille_j5_complete.json`  
Start: `c5_block_a`

`c5_block_a` **Système** : C5A — Camille : répondre quand ça déborde → `c5_001`

`c5_001` **Camille** : Je n’ai pas envie de te demander où tu es. Ça ferait trop banal. → `c5_002`

`c5_002` **Camille** : Ce qui m’intéresse, c’est ce que tu choisis de rendre vrai quand personne ne te regarde. → `c5_003`

**CHOIX** `c5_003` — Camille demande un signe qui ne soit pas seulement séduisant.
- 1. `c5_003_a` → Je peux te donner un vrai moment aujourd’hui. _(next: `c5_004_a`)_
- 2. `c5_003_b` → Je veux être honnête : aujourd’hui est compliqué. _(next: `c5_004_b`)_
- 3. `c5_003_c` → Tu sais que je te regarde même quand je réponds peu. _(next: `c5_004_c`)_

`c5_004_a` **Vous** : Je peux te donner un vrai moment aujourd’hui. → `c5_005_a`

`c5_005_a` **Camille** : Un vrai moment, ce n’est pas une parenthèse volée. C’est quand tu assumes qu’elle a compté après. → `c5_006`

`c5_004_b` **Vous** : Je veux être honnête : aujourd’hui est compliqué. → `c5_005_b`

`c5_005_b` **Camille** : Merci pour le mot honnête. Il est petit, mais il change la lumière sur tout le reste. → `c5_006`

`c5_004_c` **Vous** : Tu sais que je te regarde même quand je réponds peu. → `c5_005_c`

`c5_005_c` **Camille** : Oui. Et c’est précisément ça qui devient dangereux : je commence à croire les silences autant que les phrases. → `c5_006`

**CHOIX** `c5_006` — Répondre à la place que Camille te demande vraiment.
- 1. `c5_006_a` → Je garde un fil avec toi, même quand je devrais lâcher mon téléphone. _(next: `c5_007_a`)_
- 2. `c5_006_b` → Je ne veux pas te promettre quelque chose que je cacherai ensuite. _(next: `c5_007_b`)_
- 3. `c5_006_c` → Je peux rester là maintenant, pas tout résoudre. _(next: `c5_007_c`)_

`c5_007_a` **Vous** : Je garde un fil avec toi, même quand je devrais lâcher mon téléphone. → `c5_008_a`

`c5_008_a` **Camille** : Alors ne le dis pas comme une victoire. Dis-le comme quelqu’un qui sait qu’il y aura une facture. → `c5_block_b`

`c5_007_b` **Vous** : Je ne veux pas te promettre quelque chose que je cacherai ensuite. → `c5_008_b`

`c5_008_b` **Camille** : Ça ressemble presque à du courage. Pas celui qui brille, celui qui évite d’abîmer tout le monde. → `c5_block_b`

`c5_007_c` **Vous** : Je peux rester là maintenant, pas tout résoudre. → `c5_008_c`

`c5_008_c` **Camille** : Rester là maintenant, c’est déjà arrêter de me parler depuis le seuil. → `c5_block_b`

`c5_block_b` **Système** : C5B — Camille : oser une moitié de vérité → `c5_009`

`c5_009` **Camille** : Je vais te poser une question simple, et tu vas avoir envie de la rendre compliquée. → `c5_010`

`c5_010` **Camille** : Quand tu me réponds comme ça, est-ce que tu protèges quelqu’un, ou est-ce que tu te protèges surtout toi ? → `c5_011`

**CHOIX** `c5_011` — Répondre à la question de Camille sans tout révéler.
- 1. `c5_011_a` → Je protège quelqu’un, oui. Et je ne suis pas fier de tout. _(next: `c5_012_a`)_
- 2. `c5_011_b` → Je me protège aussi. Je ne vais pas faire semblant. _(next: `c5_012_b`)_
- 3. `c5_011_c` → Je ne peux pas répondre sans faire du mal quelque part. _(next: `c5_012_c`)_

`c5_012_a` **Vous** : Je protège quelqu’un, oui. Et je ne suis pas fier de tout. → `c5_013_a`

`c5_013_a` **Camille** : Voilà. Ce n’est pas confortable, mais au moins ça ne me prend pas pour une décoration dans ta journée. → `c5_014`

`c5_012_b` **Vous** : Je me protège aussi. Je ne vais pas faire semblant. → `c5_013_b`

`c5_013_b` **Camille** : C’est laid et honnête. Parfois, c’est déjà mieux que joli et lâche. → `c5_014`

`c5_012_c` **Vous** : Je ne peux pas répondre sans faire du mal quelque part. → `c5_013_c`

`c5_013_c` **Camille** : Je n’avais pas besoin du détail. J’avais besoin de savoir si tu voyais le mal possible. → `c5_014`

**CHOIX** `c5_014` — Fixer une limite ou franchir un pas avec Camille.
- 1. `c5_014_a` → Tu n’es pas un tiroir. Tu es un choix que je repousse trop souvent. _(next: `c5_015_a`)_
- 2. `c5_014_b` → Je veux te respecter assez pour ne pas te vendre une place fausse. _(next: `c5_015_b`)_
- 3. `c5_014_c` → Je suis mauvais avec les places. Je peux juste être vrai maintenant. _(next: `c5_015_c`)_

`c5_015_a` **Vous** : Tu n’es pas un tiroir. Tu es un choix que je repousse trop souvent. → `c5_016_a`

`c5_016_a` **Camille** : Alors arrête de me repousser avec des mains douces. C’est presque pire. → `c5_block_c`

`c5_015_b` **Vous** : Je veux te respecter assez pour ne pas te vendre une place fausse. → `c5_016_b`

`c5_016_b` **Camille** : Ça me frustre. Mais je préfère une limite qui tient debout à une promesse qui rampe. → `c5_block_c`

`c5_015_c` **Vous** : Je suis mauvais avec les places. Je peux juste être vrai maintenant. → `c5_016_c`

`c5_016_c` **Camille** : Être vrai maintenant, c’est déjà choisir de ne pas me laisser deviner seule. → `c5_block_c`

`c5_block_c` **Système** : C5C — Camille : ce que Camille emporte vers J6 → `c5_017`

`c5_017` **Camille** : Je ne vais pas te demander son nom. Si je fais ça, je deviens quelqu’un qui fouille au lieu d’écouter, et je ne veux pas être cette personne-là. → `c5_018`

`c5_018` **Camille** : Mais comprends une chose : à force de ne pas choisir à voix haute, tu choisis quand même. → `c5_019`

**CHOIX** `c5_019` — Réagir au basculement doux de Camille.
- 1. `c5_019_a` → Je sais. Et je suis en train de t’accorder une place que je ne sais pas ranger. _(next: `c5_020_a`)_
- 2. `c5_019_b` → Je ne veux pas que tu portes ce que je n’assume pas. _(next: `c5_020_b`)_
- 3. `c5_019_c` → Je voudrais te répondre sans calculer les dégâts. _(next: `c5_020_c`)_

`c5_020_a` **Vous** : Je sais. Et je suis en train de t’accorder une place que je ne sais pas ranger. → `c5_021_a`

`c5_021_a` **Camille** : Alors ne fais pas comme si une belle réponse suffisait à remettre les choses droites. → `c5_022`

`c5_020_b` **Vous** : Je ne veux pas que tu portes ce que je n’assume pas. → `c5_021_b`

`c5_021_b` **Camille** : C’est peut-être la phrase la plus tendre que tu pouvais m’envoyer sans m’offrir ce que je veux. → `c5_022`

`c5_020_c` **Vous** : Je voudrais te répondre sans calculer les dégâts. → `c5_021_c`

`c5_021_c` **Camille** : Le problème, c’est que tu calcules déjà. Tu essaies juste de garder les additions dans des pièces séparées. → `c5_022`

**CHOIX** `c5_022` — Fermer Camille J5.
- 1. `c5_022_a` → Demain je reviendrai avec une réponse moins confortable. _(next: `c5_023_a`)_
- 2. `c5_022_b` → Je ne veux pas te perdre dans mes esquives. _(next: `c5_023_b`)_
- 3. `c5_022_c` → Je préfère une limite claire à un faux espoir. _(next: `c5_023_c`)_

`c5_023_a` **Vous** : Demain je reviendrai avec une réponse moins confortable. → `c5_024_a`

`c5_024_a` **Camille** : Alors je retiens demain. Pas comme une promesse brillante. Comme un endroit où tu peux enfin arrêter de te cacher. → `c5_end_a`

`c5_023_b` **Vous** : Je ne veux pas te perdre dans mes esquives. → `c5_024_b`

`c5_024_b` **Camille** : Alors commence par ne pas appeler ça de la prudence quand c’est de la peur avec un joli manteau. À demain, peut-être. → `c5_end_b`

`c5_023_c` **Vous** : Je préfère une limite claire à un faux espoir. → `c5_024_c`

`c5_024_c` **Camille** : Je peux respecter ça. Mais une limite claire laisse quand même une marque quand elle arrive trop tard. → `c5_end_c`

`c5_end_a` **[FIN]** **Système** : Fin Camille J5 — Camille accepte la place floue que tu lui donnes, et ça pèsera en J6.

`c5_end_b` **[FIN]** **Système** : Fin Camille J5 — lien maintenu, culpabilité plus visible.

`c5_end_c` **[FIN]** **Système** : Fin Camille J5 — limite posée, distance fragile mais respectée.

## Nico — `nico_j5_complete`

Source: `narrative/t109_nico_j5_complete.json`  
Start: `n5_block_a`

`n5_block_a` **Système** : N5A — Nico : couverture fragile / pression sociale → `n5_001`

`n5_001` **Nico** : Dis-moi que le message de Maya à l’instant n’était pas pour vérifier si je savais où tu étais. Je venais de m’asseoir avec des frites, respecte-moi. → `n5_002`

`n5_002` **Nico** : Parce que j’ai répondu “aucune idée” et même moi j’ai trouvé ça peu convaincant. Mes frites ont baissé les yeux. → `n5_003`

**CHOIX** `n5_003` — Nico voit que le joueur commence à impliquer les autres malgré lui.
- 1. `n5_003_a` → Reste vague si on te demande. _(next: `n5_004_a`)_
- 2. `n5_003_b` → Tu aurais pu dire que j’étais occupé. _(next: `n5_004_b`)_
- 3. `n5_003_c` → Non, réponds juste la vérité : tu ne sais pas. Et mange tes frites tranquille. _(next: `n5_004_c`)_

`n5_004_a` **Vous** : Reste vague si on te demande. → `n5_005_a`

`n5_005_a` **Nico** : Ah, la fameuse option “brouillard amical”. Je peux faire ça une fois. Après, j’ouvre une franchise d’excuses claquées. → `n5_006`

`n5_004_b` **Vous** : Tu aurais pu dire que j’étais occupé. → `n5_005_b`

`n5_005_b` **Nico** : Occupé à quoi ? Respirer avec mystère ? Ton excuse a besoin de chaussures et d’un justificatif EDF, sinon ça ne marche pas. → `n5_006`

`n5_004_c` **Vous** : Non, réponds juste la vérité : tu ne sais pas. Et mange tes frites tranquille. → `n5_005_c`

`n5_005_c` **Nico** : Ça, je sais faire. C’est même mon niveau de compétence principal dans ton dossier, juste après “lever les yeux au ciel”. → `n5_006`

`n5_006` **Nico** : Le souci, c’est que quand deux personnes me demandent où tu es dans la même matinée, ça commence à faire club de lecture. → `n5_007`

**CHOIX** `n5_007` — Nico propose une couverture limitée, mais veut une limite claire.
- 1. `n5_007_a` → Si Sarah demande, tu ne sais rien. _(next: `n5_008_a`)_
- 2. `n5_007_b` → Je ne veux pas te mettre là-dedans. T’as déjà assez de problèmes avec tes sauces. _(next: `n5_008_b`)_
- 3. `n5_007_c` → Personne ne va te demander. _(next: `n5_008_c`)_

`n5_008_a` **Vous** : Si Sarah demande, tu ne sais rien. → `n5_009_a`

`n5_009_a` **Nico** : Sarah ? Là tu viens de prononcer un prénom avec une alarme incendie dedans. → `n5_010`

`n5_008_b` **Vous** : Je ne veux pas te mettre là-dedans. T’as déjà assez de problèmes avec tes sauces. → `n5_009_b`

`n5_009_b` **Nico** : Trop tard pour le principe, mais pas trop tard pour éviter de me donner un rôle avec dialogues. → `n5_010`

`n5_008_c` **Vous** : Personne ne va te demander. → `n5_009_c`

`n5_009_c` **Nico** : Tu dis ça avec la confiance d’un gars dont le téléphone est déjà en train de vibrer. → `n5_010`

`n5_010` **Nico** : Je peux couvrir un blanc social. Pas faire la saison 2 de ta journée avec résumé des épisodes précédents. → `n5_011`

`n5_011` **Nico** : Et je te dis ça sans morale. Juste avec l’instinct de survie du pote qui refuse d’être appelé “complice” dans un résumé. → `n5_012`

**CHOIX** `n5_012` — Nico demande quelle posture adopter si le réseau commence à comparer les versions.
- 1. `n5_012_a` → Dis juste que tu m’as vu passer vite fait. _(next: `n5_013_a`)_
- 2. `n5_012_b` → Dis que je gère un truc perso. _(next: `n5_013_b`)_
- 3. `n5_012_c` → Ne dis rien. Je vais reprendre la main. _(next: `n5_013_c`)_

`n5_013_a` **Vous** : Dis juste que tu m’as vu passer vite fait. → `n5_014_a`

`n5_014_a` **Nico** : “Vu passer vite fait”, c’est acceptable. Flou, triste, plausible. Comme ton agenda. → `n5_015`

`n5_013_b` **Vous** : Dis que je gère un truc perso. → `n5_014_b`

`n5_014_b` **Nico** : Ça, je peux le dire. Mais ça donne envie aux gens gentils de demander si ça va. Prépare une réponse. → `n5_015`

`n5_013_c` **Vous** : Ne dis rien. Je vais reprendre la main. → `n5_014_c`

`n5_014_c` **Nico** : Parfait. Reprendre la main, c’est généralement mieux que distribuer des gants à tout le monde. → `n5_015`

`n5_015` **Nico** : Dernier conseil gratuit : si tu dois improviser, évite les plans qui recrutent des bénévoles. → `n5_016`

`n5_016` **Nico** : Je reste joignable, mais je ne deviens pas ton standard téléphonique sentimental. → `n5_017`

**CHOIX** `n5_017` — Clôturer avec Nico : couverture minimale, aveu partiel ou retrait.
- 1. `n5_017_a` → Merci. Juste une couverture minimale. _(next: `n5_end_cover`)_
- 2. `n5_017_b` → Tu as raison. Je vais calmer le jeu. _(next: `n5_end_warned`)_
- 3. `n5_017_c` → T’inquiète, je maîtrise. _(next: `n5_end_cost`)_

`n5_end_cover` **[FIN]** **Système** : Fin Nico J5 — Nico peut couvrir un blanc social, mais il commence à lever les yeux au ciel.

`n5_end_warned` **[FIN]** **Système** : Fin Nico J5 — Nico reste un miroir lucide ; le joueur garde une chance de reprendre la main.

`n5_end_cost` **[FIN]** **Système** : Fin Nico J5 — Nico recule : il a entendu trop de versions et ne veut plus porter le sac.

## Maya — `maya_j5_complete`

Source: `narrative/t109_maya_j5_complete.json`  
Start: `m5_block_a`

`m5_block_a` **Système** : M5A — Maya : un détail qui circule → `m5_001`

`m5_001` **Maya** : Je viens de voir ton nom passer dans deux conversations différentes en moins de cinq minutes. Même les stories ont un meilleur planning. → `m5_002`

`m5_002` **Maya** : Rassure-moi : tu n’es pas devenu une sorte d’événement local ? Parce que j’ai pas prévu de faire l’accueil presse. → `m5_003`

**CHOIX** `m5_003` — Maya remarque un détail qui circule sans connaître toute l’histoire.
- 1. `m5_003_a` → Ok, j’ai peut-être un timing catastrophique, mais les gens exagèrent aussi. _(next: `m5_004_a`)_
- 2. `m5_003_b` → Raconte-moi la scène, version Maya, sans tribunal. _(next: `m5_004_b`)_
- 3. `m5_003_c` → J’ai peut-être mal géré ma présence. _(next: `m5_004_c`)_

`m5_004_a` **Vous** : Ok, j’ai peut-être un timing catastrophique, mais les gens exagèrent aussi. → `m5_005_a`

`m5_005_a` **Maya** : Les gens exagèrent souvent. Mais rarement tous dans la même direction au même moment, avec le même petit regard de “on a vu, non ?”. → `m5_006`

`m5_004_b` **Vous** : Raconte-moi la scène, version Maya, sans tribunal. → `m5_005_b`

`m5_005_b` **Maya** : Rien de spectaculaire. Juste un “il est où ?” lancé trop vite, puis quelqu’un qui a regardé la porte comme si elle allait répondre. → `m5_006`

`m5_004_c` **Vous** : J’ai peut-être mal géré ma présence. → `m5_005_c`

`m5_005_c` **Maya** : Ça, c’est une phrase qui sonne honnête et dangereuse. Mon mélange préféré, apparemment. → `m5_006`

`m5_006` **Maya** : Je ne sais pas ce que tu fais, et je ne veux pas deviner à ta place. Mais de dehors, ton timing dessine des formes très moches. → `m5_007`

**CHOIX** `m5_007` — Maya peut arrondir un détail ou refuser de servir de relais.
- 1. `m5_007_a` → Si on te demande, dis que j’étais avec toi deux minutes. _(next: `m5_008_a`)_
- 2. `m5_007_b` → Ne couvre rien. Je voulais juste savoir. _(next: `m5_008_b`)_
- 3. `m5_007_c` → Tu peux détourner si ça revient ? _(next: `m5_008_c`)_

`m5_008_a` **Vous** : Si on te demande, dis que j’étais avec toi deux minutes. → `m5_009_a`

`m5_009_a` **Maya** : Deux minutes, je peux. Une version complète de ta journée, non. Je n’ai pas l’abonnement premium. → `m5_010`

`m5_008_b` **Vous** : Ne couvre rien. Je voulais juste savoir. → `m5_009_b`

`m5_009_b` **Maya** : Bonne réponse. Pas confortable, mais bonne. Les couvertures improvisées font souvent plus de bruit que le trou initial. → `m5_010`

`m5_008_c` **Vous** : Tu peux détourner si ça revient ? → `m5_009_c`

`m5_009_c` **Maya** : Je peux changer de sujet avec élégance. Je ne peux pas effacer le fait que le sujet existe. → `m5_010`

`m5_010` **Maya** : Et avant que tu paniques : personne n’a “découvert” quoi que ce soit. C’est plutôt le moment gênant où tout le monde prétend regarder son verre. → `m5_011`

`m5_011` **Maya** : C’est fou comme un mini détail peut ruiner un grand discours. → `m5_012`

**CHOIX** `m5_012` — Maya demande si elle doit rester témoin discret ou signaler quand ça devient visible.
- 1. `m5_012_a` → Préviens-moi si ça circule. _(next: `m5_013_a`)_
- 2. `m5_012_b` → Ignore, ça va passer. _(next: `m5_013_b`)_
- 3. `m5_012_c` → Je préfère que tu ne sois pas impliquée. _(next: `m5_013_c`)_

`m5_013_a` **Vous** : Préviens-moi si ça circule. → `m5_014_a`

`m5_014_a` **Maya** : Je peux être un radar, pas un pare-feu. Si ça clignote trop, je t’envoie un emoji sobre et inquiétant. → `m5_015`

`m5_013_b` **Vous** : Ignore, ça va passer. → `m5_014_b`

`m5_014_b` **Maya** : Peut-être. Mais les trucs qui “passent” reviennent souvent avec un ami et une question précise. → `m5_015`

`m5_013_c` **Vous** : Je préfère que tu ne sois pas impliquée. → `m5_014_c`

`m5_014_c` **Maya** : Trop tard pour être totalement extérieure, mais pas trop tard pour rester à distance intelligente. → `m5_015`

`m5_015` **Maya** : Bref : respire, réponds aux vrais messages, et arrête de croire qu’un silence ne se remarque pas. → `m5_016`

**CHOIX** `m5_016` — Clôturer avec Maya : alerte légère, minimisation ou retrait protecteur.
- 1. `m5_016_a` → Ok. Alerte-moi si tu vois autre chose. _(next: `m5_end_watch`)_
- 2. `m5_016_b` → Tu lis trop entre les lignes. _(next: `m5_end_minimized`)_
- 3. `m5_016_c` → Merci. Je vais gérer sans t’embarquer. _(next: `m5_end_distance`)_

`m5_end_watch` **[FIN]** **Système** : Fin Maya J5 — Maya n’a pas tout compris. Mais elle a vu assez pour ne plus regarder pareil.

`m5_end_minimized` **[FIN]** **Système** : Fin Maya J5 — tu minimises. Maya sourit, mais elle garde le détail en tête.

`m5_end_distance` **[FIN]** **Système** : Fin Maya J5 — Maya reste protectrice mais à distance ; la pression sociale existe sans couverture lourde.

---

# Jour 6

## Sarah — `sarah_j6_complete`

Source: `narrative/t120_sarah_j6_complete.json`  
Start: `s6_block_a`

`s6_block_a` **Système** : S6A — Sarah : le quotidien ne tient plus → `s6_001`

`s6_001` **Sarah** : Je viens de rentrer. La lumière de la cuisine était encore allumée. → `s6_002`

`s6_002` **Sarah** : Ton mug est encore dans l’évier, juste à côté de la tasse du café d’hier. J’ai voulu les ranger, puis je les ai reposés exactement au même endroit. → `s6_003`

`s6_003` **Sarah** : C’est idiot, mais ça m’a fait quelque chose. Comme si même l’évier attendait une réponse plus claire que moi. → `s6_004`

**CHOIX** `s6_004` — Répondre au détail du mug sans transformer Sarah en procès.
- 1. `s6_004_a` → Laisse-le là. Je rentre et on parle vraiment. _(next: `s6_005_a`)_
- 2. `s6_004_b` → Je suis désolé. Je pensais pas qu’un mug et une assiette pouvaient dire autant. _(next: `s6_005_b`)_
- 3. `s6_004_c` → Ne fais pas une histoire d’un mug. _(next: `s6_005_c`)_

`s6_005_a` **Vous** : Laisse-le là. Je rentre et on parle vraiment. → `s6_006_a`

`s6_006_a` **Sarah** : D’accord. Mais “vraiment”, ça veut dire sans poser ton téléphone face contre table toutes les deux minutes. → `s6_007`

`s6_005_b` **Vous** : Je suis désolé. Je pensais pas qu’un mug et une assiette pouvaient dire autant. → `s6_006_b`

`s6_006_b` **Sarah** : Je sais. C’est justement le problème. On finit par vivre dans des choses que tu ne vois même plus. → `s6_007`

`s6_005_c` **Vous** : Ne fais pas une histoire d’un mug. → `s6_006_c`

`s6_006_c` **Sarah** : Ce n’est pas le mug. Tu le sais. Le mug, au moins, il est là. → `s6_007`

`s6_007` **Sarah** : J’ai gardé une assiette hier. Puis je l’ai mise au frigo. Puis je l’ai jetée ce matin, entre le café et les courses. Ça m’a énervée d’être triste pour une assiette. → `s6_008`

**CHOIX** `s6_008` — Dire si le joueur accepte le manque concret ou le déplace.
- 1. `s6_008_a` → Tu n’aurais pas dû avoir à m’attendre comme ça. _(next: `s6_009_a`)_
- 2. `s6_008_b` → J’aurais dû prévenir plus tôt. _(next: `s6_009_b`)_
- 3. `s6_008_c` → J’avais juste besoin d’air hier. _(next: `s6_009_c`)_

`s6_009_a` **Vous** : Tu n’aurais pas dû avoir à m’attendre comme ça. → `s6_010_a`

`s6_010_a` **Sarah** : Merci de ne pas me dire que j’exagère. Ça change déjà quelque chose. → `s6_011`

`s6_009_b` **Vous** : J’aurais dû prévenir plus tôt. → `s6_010_b`

`s6_010_b` **Sarah** : Oui. Prévenir, c’est petit. Mais ces derniers temps, les petites choses manquent beaucoup. → `s6_011`

`s6_009_c` **Vous** : J’avais juste besoin d’air hier. → `s6_010_c`

`s6_010_c` **Sarah** : Je peux entendre ça. J’ai juste besoin de savoir si respirer veut dire partir de moi. → `s6_011`

`s6_011` **Sarah** : Je ne veux pas te coincer. Je veux juste arrêter de parler à quelqu’un qui semble déjà ailleurs. → `s6_012`

**CHOIX** `s6_012` — Répondre à la peur de Sarah sans jouer une grande scène.
- 1. `s6_012_a` → Je suis encore là. Maladroitement, mais là. _(next: `s6_013_a`)_
- 2. `s6_012_b` → Je ne sais pas bien où j’en suis, mais je ne veux pas te perdre dans le flou. _(next: `s6_013_b`)_
- 3. `s6_012_c` → J’ai besoin que tu me laisses un peu de silence. _(next: `s6_013_c`)_

`s6_013_a` **Vous** : Je suis encore là. Maladroitement, mais là. → `s6_014_a`

`s6_014_a` **Sarah** : Alors montre-le petit. Rentre. Pose ton téléphone écran vers le haut. Bois un verre d’eau. On commence là. → `s6_block_b`

`s6_013_b` **Vous** : Je ne sais pas bien où j’en suis, mais je ne veux pas te perdre dans le flou. → `s6_014_b`

`s6_014_b` **Sarah** : C’est pas confortable à lire. Mais c’est moins dur que tes phrases toutes lisses. → `s6_block_b`

`s6_013_c` **Vous** : J’ai besoin que tu me laisses un peu de silence. → `s6_014_c`

`s6_014_c` **Sarah** : Je peux laisser du silence. Je ne peux plus faire semblant qu’il ne me parle pas. → `s6_block_b`

`s6_block_b` **Système** : S6B — Sarah : rester ou seulement faire tenir → `s6_015`

`s6_015` **Sarah** : Je vais te demander une chose simple. Pas parfaite. Simple. → `s6_016`

`s6_016` **Sarah** : Tu veux encore être là avec moi, ou tu veux juste que ça ne casse pas ce soir ? → `s6_017`

**CHOIX** `s6_017` — Choisir le ton de la réponse intime à Sarah.
- 1. `s6_017_a` → Je veux être là. Pas juste éviter que ça casse. _(next: `s6_018_a`)_
- 2. `s6_017_b` → Je veux qu’on tienne ce soir, et demain je te dirai plus. _(next: `s6_018_b`)_
- 3. `s6_017_c` → Je ne peux pas te donner une réponse propre maintenant. _(next: `s6_018_c`)_

`s6_018_a` **Vous** : Je veux être là. Pas juste éviter que ça casse. → `s6_019_a`

`s6_019_a` **Sarah** : Alors ne commence pas par une promesse. Commence par être joignable quand tu dis que tu l’es. → `s6_020`

`s6_018_b` **Vous** : Je veux qu’on tienne ce soir, et demain je te dirai plus. → `s6_019_b`

`s6_019_b` **Sarah** : Demain, c’est proche. J’accepte proche. Mais je ne veux plus d’un demain qui recule à chaque message. → `s6_020`

`s6_018_c` **Vous** : Je ne peux pas te donner une réponse propre maintenant. → `s6_019_c`

`s6_019_c` **Sarah** : Je ne demande pas propre. Je demande une phrase qui ne me laisse pas seule à deviner. → `s6_020`

`s6_020` **Sarah** : Je suis fatiguée, mais je suis encore là à t’écrire. Ce n’est pas rien pour moi. → `s6_021`

**CHOIX** `s6_021` — Décider quoi faire de cette ouverture.
- 1. `s6_021_a` → Je rentre sans détour. On parle avant de dormir. _(next: `s6_022_a`)_
- 2. `s6_021_b` → Je passe, mais je dois encore régler un truc avant. _(next: `s6_022_b`)_
- 3. `s6_021_c` → Je ne veux pas te mentir : je vais avoir besoin de temps. _(next: `s6_022_c`)_

`s6_022_a` **Vous** : Je rentre sans détour. On parle avant de dormir. → `s6_023_a`

`s6_023_a` **Sarah** : Je laisse le mug dans l’évier alors. Pas comme un test. Comme un point de départ. → `s6_024`

`s6_022_b` **Vous** : Je passe, mais je dois encore régler un truc avant. → `s6_023_b`

`s6_023_b` **Sarah** : Voilà. C’est ce “un truc” qui prend toujours une chaise entre nous. → `s6_024`

`s6_022_c` **Vous** : Je ne veux pas te mentir : je vais avoir besoin de temps. → `s6_023_c`

`s6_023_c` **Sarah** : Merci de le dire comme ça. Ça fait mal, mais au moins je sais où poser mes pieds. → `s6_024`

`s6_024` **Sarah** : Je vais me faire un thé et éteindre la cuisine. C’est minuscule, mais j’ai besoin d’un geste qui n’attend pas ta réponse. → `s6_025`

**CHOIX** `s6_025` — Laisser Sarah partir vers la fin MVP avec une couleur relationnelle.
- 1. `s6_025_a` → Garde-moi une tasse. J’arrive. _(next: `s6_end_repair`)_
- 2. `s6_025_b` → Je t’écris dès que je pars. Pas une minute floue de plus, même si c’est juste “je mets mes chaussures”. _(next: `s6_end_uncertain`)_
- 3. `s6_025_c` → Ne m’attends pas éveillée. _(next: `s6_end_distance`)_

`s6_end_repair` **[FIN]** **Système** : Fin Sarah J6 — Sarah laisse une place ouverte : pas de pardon magique, mais une discussion possible avant la fin MVP.

`s6_end_uncertain` **[FIN]** **Système** : Fin Sarah J6 — Sarah accepte une phrase moins floue, sans savoir encore si elle suffira.

`s6_end_distance` **[FIN]** **Système** : Fin Sarah J6 — Sarah se protège : le quotidien reste debout, mais moins près du joueur.

## Camille — `camille_j6_complete`

Source: `narrative/t120_camille_j6_complete.json`  
Start: `c6_block_a`

`c6_block_a` **Système** : C6A — Camille : le téléphone encore allumé → `c6_001`

`c6_001` **Camille** : J’ai remis le même morceau qu’hier. Le café du fond l’a adopté, mauvaise nouvelle pour moi. → `c6_002`

`c6_002` **Camille** : Mauvaise idée. Il a exactement la durée d’une réponse qu’on attend trop, plus trois secondes pour faire semblant de ne pas attendre. → `c6_003`

`c6_003` **Camille** : Tu vois, je peux être très raisonnable. J’ai juste choisi une chanson qui ne l’est pas et une table près de la porte. → `c6_004`

**CHOIX** `c6_004` — Répondre à Camille comme à quelqu’un de réel, pas comme à une sortie de secours.
- 1. `c6_004_a` → Je l’écoute aussi. Mauvaise idée partagée, au moins pour les vingt premières secondes. _(next: `c6_005_a`)_
- 2. `c6_004_b` → Je ne devrais pas te répondre maintenant, mais je le fais. _(next: `c6_005_b`)_
- 3. `c6_004_c` → Camille, je ne peux pas faire comme si ce message était léger. _(next: `c6_005_c`)_

`c6_005_a` **Vous** : Je l’écoute aussi. Mauvaise idée partagée, au moins pour les vingt premières secondes. → `c6_006_a`

`c6_006_a` **Camille** : Évidemment. Tu as toujours eu du talent pour choisir les mauvaises idées avec un air sincère. C’est presque un style. → `c6_007`

`c6_005_b` **Vous** : Je ne devrais pas te répondre maintenant, mais je le fais. → `c6_006_b`

`c6_006_b` **Camille** : Je note le “mais”. Il a pris toute la place dans ta phrase. Je lui commande un café ? → `c6_007`

`c6_005_c` **Vous** : Camille, je ne peux pas faire comme si ce message était léger. → `c6_006_c`

`c6_006_c` **Camille** : Tant mieux. Je commence à me fatiguer des choses légères qui laissent des bleus. → `c6_007`

`c6_007` **Camille** : Je suis passée devant le café. Celui qui n’a rien d’exceptionnel : table bancale, vitre froide, et toi qui le regardes toujours comme une porte de secours. → `c6_008`

**CHOIX** `c6_008` — Réagir au lieu sans promettre une romance facile.
- 1. `c6_008_a` → Je n’ai pas envie que tu sois une porte de secours. _(next: `c6_009_a`)_
- 2. `c6_008_b` → Ce café me fait penser à toi, même quand je fais semblant de regarder ailleurs. _(next: `c6_009_b`)_
- 3. `c6_008_c` → Je préfère qu’on ne parle pas de lieux ce soir. _(next: `c6_009_c`)_

`c6_009_a` **Vous** : Je n’ai pas envie que tu sois une porte de secours. → `c6_010_a`

`c6_010_a` **Camille** : Alors arrête d’arriver chez moi seulement quand le reste devient irrespirable. → `c6_011`

`c6_009_b` **Vous** : Ce café me fait penser à toi, même quand je fais semblant de regarder ailleurs. → `c6_010_b`

`c6_010_b` **Camille** : Ça sonnait presque vrai. Le “presque” est pénible, mais je l’entends. → `c6_011`

`c6_009_c` **Vous** : Je préfère qu’on ne parle pas de lieux ce soir. → `c6_010_c`

`c6_010_c` **Camille** : Tu préfères souvent ne pas nommer les endroits où tu reviens quand même. → `c6_011`

`c6_011` **Camille** : Je ne te demande pas d’être courageux en majuscules. Juste de ne pas me répondre comme si je tenais dans un coin d’écran. → `c6_012`

**CHOIX** `c6_012` — Dire quelle place Camille peut avoir avant C6B.
- 1. `c6_012_a` → Tu ne tiens pas dans un coin. C’est bien le problème. _(next: `c6_013_a`)_
- 2. `c6_012_b` → Je suis en train de comprendre que je t’ai rangée trop facilement. _(next: `c6_013_b`)_
- 3. `c6_012_c` → Je ne peux pas te donner plus que ce message maintenant. _(next: `c6_013_c`)_

`c6_013_a` **Vous** : Tu ne tiens pas dans un coin. C’est bien le problème. → `c6_014_a`

`c6_014_a` **Camille** : Non. Le problème, c’est ce que tu fais quand quelque chose ne tient plus dans le coin prévu. → `c6_block_b`

`c6_013_b` **Vous** : Je suis en train de comprendre que je t’ai rangée trop facilement. → `c6_014_b`

`c6_014_b` **Camille** : Tu vois. Ce n’était pas si difficile à écrire. Difficile à vivre, peut-être. → `c6_block_b`

`c6_013_c` **Vous** : Je ne peux pas te donner plus que ce message maintenant. → `c6_014_c`

`c6_014_c` **Camille** : Alors lis bien ma réponse. Elle ne va peut-être pas rester disponible longtemps. → `c6_block_b`

`c6_block_b` **Système** : C6B — Camille : ne plus être une parenthèse → `c6_015`

`c6_015` **Camille** : Je vais être claire, mais pas spectaculaire. → `c6_016`

`c6_016` **Camille** : Je ne veux pas être l’endroit où tu respires quand tu n’arrives plus à parler ailleurs. → `c6_017`

**CHOIX** `c6_017` — Répondre à la demande de respect de Camille.
- 1. `c6_017_a` → Tu mérites mieux qu’une cachette. _(next: `c6_018_a`)_
- 2. `c6_017_b` → Je veux te voir comme quelqu’un de réel, pas comme une pause. _(next: `c6_018_b`)_
- 3. `c6_017_c` → Je crois que je me suis servi de toi pour ne pas regarder le reste. _(next: `c6_018_c`)_

`c6_018_a` **Vous** : Tu mérites mieux qu’une cachette. → `c6_019_a`

`c6_019_a` **Camille** : Je n’avais pas prévu d’être un meuble discret dans ta panique, non. → `c6_020`

`c6_018_b` **Vous** : Je veux te voir comme quelqu’un de réel, pas comme une pause. → `c6_019_b`

`c6_019_b` **Camille** : Alors il faudra supporter que le réel réponde parfois non. Ou pas tout de suite. → `c6_020`

`c6_018_c` **Vous** : Je crois que je me suis servi de toi pour ne pas regarder le reste. → `c6_019_c`

`c6_019_c` **Camille** : C’est une phrase moche. Donc probablement utile. → `c6_020`

`c6_020` **Camille** : J’ai posé mon téléphone sur la table. Écran vers le haut. Je ne fais jamais ça quand j’attends quelqu’un. → `c6_021`

**CHOIX** `c6_021` — Décider si Camille doit attendre, reculer ou recevoir une position claire.
- 1. `c6_021_a` → N’attends pas en silence. Je veux te voir, mais pas en cachette. _(next: `c6_022_a`)_
- 2. `c6_021_b` → Je ne peux pas venir. Mais je ne veux plus te laisser dans le flou. _(next: `c6_022_b`)_
- 3. `c6_021_c` → Je vais encore te faire attendre si je réponds mal maintenant. _(next: `c6_022_c`)_

`c6_022_a` **Vous** : N’attends pas en silence. Je veux te voir, mais pas en cachette. → `c6_023_a`

`c6_023_a` **Camille** : Voilà. Pas une belle phrase. Une phrase avec des chaussures. Elle peut marcher quelque part. → `c6_024`

`c6_022_b` **Vous** : Je ne peux pas venir. Mais je ne veux plus te laisser dans le flou. → `c6_023_b`

`c6_023_b` **Camille** : Je préfère une porte fermée à une poignée qu’on touche toutes les dix minutes. → `c6_024`

`c6_022_c` **Vous** : Je vais encore te faire attendre si je réponds mal maintenant. → `c6_023_c`

`c6_023_c` **Camille** : Tu as cette manière de prendre soin en reculant. Je ne sais pas encore si ça me touche ou si ça m’épuise. → `c6_024`

`c6_024` **Camille** : Le morceau vient de finir. Je ne le relance pas. À toi de ne pas transformer ce silence en meuble. → `c6_025`

**CHOIX** `c6_025` — Laisser Camille vers les futures fins MVP.
- 1. `c6_025_a` → Je vais dire une chose simple : je te choisis comme une vraie personne, pas comme une pause. _(next: `c6_end_chosen_seed`)_
- 2. `c6_025_b` → Je dois d’abord parler ailleurs. Si je reviens, ce sera debout. _(next: `c6_end_respect_distance`)_
- 3. `c6_025_c` → Je ne sais pas faire mieux que ce silence ce soir. _(next: `c6_end_cuts_short`)_

`c6_end_chosen_seed` **[FIN]** **Système** : Fin Camille J6 — Camille entend une position plus nette. Elle ne récompense pas encore : elle attend que les actes rejoignent la phrase.

`c6_end_respect_distance` **[FIN]** **Système** : Fin Camille J6 — Camille accepte la distance si elle est honnête. La porte reste réelle, mais pas ouverte pour fuir.

`c6_end_cuts_short` **[FIN]** **Système** : Fin Camille J6 — Camille coupe court avec dignité : elle refuse de devenir un silence confortable.

## Nico — `nico_j6_complete`

Source: `narrative/t121_nico_j6_complete.json`  
Start: `n6_block_a`

`n6_block_a` **Système** : N6A — Nico : dernier service, vraie limite → `n6_001`

`n6_001` **Nico** : J’ai commandé trop de frites. Encore. C’est ma stabilité émotionnelle à moi. → `n6_002`

`n6_002` **Nico** : C’est pas le sujet, mais ça m’aide à réfléchir sans casser une chaise ni envoyer un vocal de dix minutes. → `n6_003`

`n6_003` **Nico** : Et là, réflexion terminée : je peux couvrir un blanc. Pas devenir ton service après-vente avec musique d’attente. → `n6_004`

**CHOIX** `n6_004` — Nico pose la limite sans cesser d’être l’ami.
- 1. `n6_004_a` → Je te demande pas de porter ça. Juste de ne pas m’enfoncer. _(next: `n6_005_a`)_
- 2. `n6_004_b` → T’as raison. Je t’ai trop mis au milieu. Et personne ne mérite ça, même pas tes frites. _(next: `n6_005_b`)_
- 3. `n6_004_c` → Si t’es mon ami, aide-moi encore une fois. _(next: `n6_005_c`)_

`n6_005_a` **Vous** : Je te demande pas de porter ça. Juste de ne pas m’enfoncer. → `n6_006_a`

`n6_006_a` **Nico** : Ah, nuance de juriste fatigué. “Ne pas m’enfoncer”, c’est déjà porter un petit sac, tu vois. → `n6_007`

`n6_005_b` **Vous** : T’as raison. Je t’ai trop mis au milieu. Et personne ne mérite ça, même pas tes frites. → `n6_006_b`

`n6_006_b` **Nico** : Merci. J’aime quand tu découvres les évidences avant que je fasse un PowerPoint avec des frites et des flèches rouges. → `n6_007`

`n6_005_c` **Vous** : Si t’es mon ami, aide-moi encore une fois. → `n6_006_c`

`n6_006_c` **Nico** : Oh non. Pas le bouton “si t’es mon ami”. Celui-là, il sent la pizza froide et le chantage affectif. → `n6_007`

`n6_007` **Nico** : Maya m’a écrit “il fait quoi exactement ?” avec trois points. Trois points, frérot. Elle a sorti la ponctuation de guerre et moi j’avais de la sauce sur les doigts. → `n6_008`

**CHOIX** `n6_008` — Décider comment Nico doit répondre à Maya.
- 1. `n6_008_a` → Dis-lui que tu sais pas. Simple. _(next: `n6_009_a`)_
- 2. `n6_008_b` → Dis-lui que je règle un truc perso. _(next: `n6_009_b`)_
- 3. `n6_008_c` → Ne réponds pas pour l’instant. _(next: `n6_009_c`)_

`n6_009_a` **Vous** : Dis-lui que tu sais pas. Simple. → `n6_010_a`

`n6_010_a` **Nico** : Ça, je peux. Incroyable concept : répondre ce que je sais. On tient peut-être une innovation. → `n6_011`

`n6_009_b` **Vous** : Dis-lui que je règle un truc perso. → `n6_010_b`

`n6_010_b` **Nico** : Ça passe une fois. Mais “un truc perso”, c’est une tente Quechua : pratique, moche, pas faite pour vivre dedans. → `n6_011`

`n6_009_c` **Vous** : Ne réponds pas pour l’instant. → `n6_010_c`

`n6_010_c` **Nico** : Donc ta stratégie c’est que tout le monde devienne silencieux en même temps. Audacieux. Nul, mais audacieux. → `n6_011`

`n6_011` **Nico** : Je rigole, mais je suis sérieux deux secondes : je suis ton pote, pas ton standard de crise, et j’ai pas envie que ton bazar change ma façon de parler aux gens. → `n6_012`

**CHOIX** `n6_012` — Réagir à la limite de Nico sans le transformer en hotline émotionnelle.
- 1. `n6_012_a` → Je veux pas t’abîmer avec mes histoires. _(next: `n6_013_a`)_
- 2. `n6_012_b` → Je suis en train de perdre le contrôle, je crois. _(next: `n6_013_b`)_
- 3. `n6_012_c` → On en reparlera après, là j’ai besoin d’une solution. _(next: `n6_013_c`)_

`n6_013_a` **Vous** : Je veux pas t’abîmer avec mes histoires. → `n6_014_a`

`n6_014_a` **Nico** : Bien. Parce que moi je suis déjà abîmé par mes choix de sauces, ça suffit pour ce soir. → `n6_015`

`n6_013_b` **Vous** : Je suis en train de perdre le contrôle, je crois. → `n6_014_b`

`n6_014_b` **Nico** : Je vais pas applaudir, mais au moins tu regardes le volant. C’est mieux que conduire les yeux fermés. → `n6_015`

`n6_013_c` **Vous** : On en reparlera après, là j’ai besoin d’une solution. → `n6_014_c`

`n6_014_c` **Nico** : Non. Ça, c’est exactement le moment où je deviens une appli gratuite dans ta tête. Je passe mon tour. → `n6_015`

`n6_015` **Nico** : Dernière offre : je réponds un truc propre si on me demande. Pas beau. Pas héroïque. Propre. → `n6_016`

**CHOIX** `n6_016` — Fixer le seed de fin côté Nico.
- 1. `n6_016_a` → Réponds propre. Et après je gère moi-même. _(next: `n6_end_loyal_limit`)_
- 2. `n6_016_b` → Ne réponds rien. Je vais arrêter de t’utiliser comme tampon. _(next: `n6_end_steps_back`)_
- 3. `n6_016_c` → Laisse tomber. Je vais trouver quelqu’un d’autre. _(next: `n6_end_friend_hurt`)_

`n6_end_loyal_limit` **[FIN]** **Système** : Fin Nico J6 — Nico aide une dernière fois, mais avec une limite nette : après ça, le joueur devra parler lui-même.

`n6_end_steps_back` **[FIN]** **Système** : Fin Nico J6 — Nico respecte l’effort du joueur et sort du rôle de tampon social.

`n6_end_friend_hurt` **[FIN]** **Système** : Fin Nico J6 — Nico recule, blessé d’être traité comme un outil remplaçable.

## Maya — `maya_j6_complete`

Source: `narrative/t121_maya_j6_complete.json`  
Start: `m6_block_a`

`m6_block_a` **Système** : M6A — Maya : une photo, pas une enquête → `m6_001`

`m6_001` **Maya** : J’ai failli rien dire. Puis le groupe a relancé la photo comme si c’était un épisode bonus. → `m6_002`

`m6_002` **Maya** : Puis j’ai revu la photo du groupe. Celle où tu es censé ne pas être passé, sauf ton épaule, visiblement très indépendante. → `m6_003`

`m6_003` **Maya** : Je précise : je n’ai pas un mur avec des fils rouges chez moi. J’ai juste des yeux, un dimanche trop calme, et une story mal cadrée. → `m6_004`

**CHOIX** `m6_004` — Maya pose un détail public, sans tout savoir.
- 1. `m6_004_a` → Ok, raconte l’épaule superstar. _(next: `m6_005_a`)_
- 2. `m6_004_b` → Si c’est flou, laisse tomber. _(next: `m6_005_b`)_
- 3. `m6_004_c` → Je préfère que tu me dises franchement ce qui circule. _(next: `m6_005_c`)_

`m6_005_a` **Vous** : Ok, raconte l’épaule superstar. → `m6_006_a`

`m6_006_a` **Maya** : Ton épaule. Enfin je crois. Très mauvaise célébrité : reconnaissable par textile et zéro sens du timing. → `m6_007`

`m6_005_b` **Vous** : Si c’est flou, laisse tomber. → `m6_006_b`

`m6_006_b` **Maya** : Flou ne veut pas dire invisible. Ça veut juste dire que tout le monde zoome comme des idiots. → `m6_007`

`m6_005_c` **Vous** : Je préfère que tu me dises franchement ce qui circule. → `m6_006_c`

`m6_006_c` **Maya** : Ok. Une photo, deux “il était pas ailleurs lui ?”, et quelqu’un qui a répondu “laisse”. Ambiance nappe en papier qui brûle. → `m6_007`

`m6_007` **Maya** : Je veux pas être mêlée. Je dis ça en étant déjà un peu mêlée, ce qui ruine mon image de neutralité. → `m6_008`

**CHOIX** `m6_008` — Décider si le joueur demande aide, distance ou franchise sociale.
- 1. `m6_008_a` → Ne couvre rien. Dis juste que tu ne sais pas. _(next: `m6_009_a`)_
- 2. `m6_008_b` → Si tu peux calmer le groupe avec une vanne moche, je prends. _(next: `m6_009_b`)_
- 3. `m6_008_c` → J’ai besoin que tu ne parles pas de ça. _(next: `m6_009_c`)_

`m6_009_a` **Vous** : Ne couvre rien. Dis juste que tu ne sais pas. → `m6_010_a`

`m6_010_a` **Maya** : Parfait. Ma spécialité : ne pas savoir officiellement. Ça demande peu d’entraînement. → `m6_011`

`m6_009_b` **Vous** : Si tu peux calmer le groupe avec une vanne moche, je prends. → `m6_010_b`

`m6_010_b` **Maya** : Je peux dire “on va pas commenter une épaule”. C’est nul, mais c’est légal moralement. → `m6_011`

`m6_009_c` **Vous** : J’ai besoin que tu ne parles pas de ça. → `m6_010_c`

`m6_010_c` **Maya** : Besoin ou confort ? Parce que l’un se comprend. L’autre me donne envie de ranger mon téléphone très loin. → `m6_011`

`m6_011` **Maya** : Et avant que tu paniques : non, je ne pense pas tout savoir. Je pense juste que ton timing est une œuvre d’art contemporaine. → `m6_012`

**CHOIX** `m6_012` — Réagir au regard social de Maya sans la transformer en outil.
- 1. `m6_012_a` → Merci de ne pas faire comme si tu savais tout. _(next: `m6_013_a`)_
- 2. `m6_012_b` → Je suis en train de mettre tout le monde dans une position bizarre. _(next: `m6_013_b`)_
- 3. `m6_012_c` → Tu dramatises une épaule sur une photo. _(next: `m6_013_c`)_

`m6_013_a` **Vous** : Merci de ne pas faire comme si tu savais tout. → `m6_014_a`

`m6_014_a` **Maya** : Je suis agaçante, pas omnisciente. Nuance importante pour mon image de marque. → `m6_015`

`m6_013_b` **Vous** : Je suis en train de mettre tout le monde dans une position bizarre. → `m6_014_b`

`m6_014_b` **Maya** : Oui. Et bizarre, ça se gère. Tant que tu n’obliges pas les autres à sourire pendant que ça brûle. → `m6_015`

`m6_013_c` **Vous** : Tu dramatises une épaule sur une photo. → `m6_014_c`

`m6_014_c` **Maya** : Possible. Mais ton épaule a actuellement une meilleure intrigue que la moitié du groupe. → `m6_015`

`m6_015` **Maya** : Je pose ça là : si tu dois parler à quelqu’un, fais-le avant que le groupe écrive le résumé à ta place avec des emojis beaucoup trop confiants. → `m6_016`

**CHOIX** `m6_016` — Fixer le seed de fin côté Maya.
- 1. `m6_016_a` → Je vais parler avant que ça tourne en version de groupe. _(next: `m6_end_warned`)_
- 2. `m6_016_b` → Gagne-moi juste un peu de calme, sans inventer. _(next: `m6_end_soft_cover`)_
- 3. `m6_016_c` → Laisse-les parler. Je verrai après. _(next: `m6_end_minimized`)_

`m6_end_warned` **[FIN]** **Système** : Fin Maya J6 — Maya a vu assez pour prévenir, mais laisse au joueur la responsabilité de parler avant le groupe.

`m6_end_soft_cover` **[FIN]** **Système** : Fin Maya J6 — Maya amortit le détail sans inventer, tout en gardant une distance prudente.

`m6_end_minimized` **[FIN]** **Système** : Fin Maya J6 — le joueur minimise ; Maya se retire et laisse le groupe tirer ses propres fils.

## Inès — `ines_j6_complete`

Source: `narrative/t121_ines_j6_complete.json`  
Start: `i6_block_a`

`i6_block_a` **Système** : I6A — Inès : porte latérale à contretemps → `i6_001`

`i6_001` **Inès** : J’ai écrit trois versions de ce message. J’en ai effacé deux et demie. → `i6_002`

`i6_002` **Inès** : Celle-ci est la moins étrange. Je crois. Oublie si c’est déjà trop. → `i6_003`

`i6_003` **Inès** : Je suis passée près de l’arrêt où je t’avais vu marcher trop vite. Le bus a raté mon arrêt. Ou moi le sien. J’ai pensé à ton air de quelqu’un qui cherche une sortie sans panneau. → `i6_003b`

`i6_003b` **Inès** : J’ai gardé le ticket du trajet dans ma poche. Aucune raison. Juste un petit papier qui insistait plus que moi. → `i6_004`

**CHOIX** `i6_004` — Inès revient comme une porte latérale, pas une route complète.
- 1. `i6_004_a` → C’est bizarre, mais ton message arrive doucement. Ça me fait du bien. _(next: `i6_005_a`)_
- 2. `i6_004_b` → Je ne devrais pas ouvrir une autre porte maintenant. Même si elle a l’air calme. _(next: `i6_005_b`)_
- 3. `i6_004_c` → Tu tombes au mauvais moment. _(next: `i6_005_c`)_

`i6_005_a` **Vous** : C’est bizarre, mais ton message arrive doucement. Ça me fait du bien. → `i6_006_a`

`i6_006_a` **Inès** : Je ne sais pas si c’est une bonne chose. Parfois être content d’un message, c’est juste éviter les autres. → `i6_007`

`i6_005_b` **Vous** : Je ne devrais pas ouvrir une autre porte maintenant. Même si elle a l’air calme. → `i6_006_b`

`i6_006_b` **Inès** : Oui. J’ai hésité à ne pas frapper. C’est peut-être plus honnête de rester sur le seuil, surtout quand la lumière est déjà allumée ailleurs. → `i6_007`

`i6_005_c` **Vous** : Tu tombes au mauvais moment. → `i6_006_c`

`i6_006_c` **Inès** : Je sais. C’est un talent triste, tomber dans les interstices. → `i6_007`

`i6_007` **Inès** : Je ne te demande rien. Je voulais juste vérifier que tu n’étais pas en train de disparaître dans une version trop pratique de toi. Pas grave si tu réponds plus tard. → `i6_008`

**CHOIX** `i6_008` — Répondre à la tentation de fuite sans transformer Inès en issue romance.
- 1. `i6_008_a` → J’ai envie de répondre parce que c’est plus simple que choisir. _(next: `i6_009_a`)_
- 2. `i6_008_b` → Je vais répondre aux anciens messages avant d’en ouvrir de nouveaux. _(next: `i6_009_b`)_
- 3. `i6_008_c` → Reste là un peu. Sans demander. _(next: `i6_009_c`)_

`i6_009_a` **Vous** : J’ai envie de répondre parce que c’est plus simple que choisir. → `i6_010_a`

`i6_010_a` **Inès** : Alors ne me transforme pas en endroit simple. Je ne suis pas sûre d’aimer ce rôle. → `i6_011`

`i6_009_b` **Vous** : Je vais répondre aux anciens messages avant d’en ouvrir de nouveaux. → `i6_010_b`

`i6_010_b` **Inès** : C’est probablement la phrase la moins jolie. Donc peut-être la plus juste. → `i6_011`

`i6_009_c` **Vous** : Reste là un peu. Sans demander. → `i6_010_c`

`i6_010_c` **Inès** : Je peux rester un peu. Mais pas pour devenir la lumière allumée pendant que tu éteins les autres pièces. → `i6_011`

`i6_011` **Inès** : J’efface beaucoup avant d’envoyer. Ce soir, je t’en laisse une seule : ne choisis pas seulement l’endroit où ça fait le moins de bruit. → `i6_012`

**CHOIX** `i6_012` — Fixer le seed de fin côté Inès.
- 1. `i6_012_a` → Je vais fermer cette porte pour l’instant. Pas contre toi. Pour répondre ailleurs. _(next: `i6_end_boundary`)_
- 2. `i6_012_b` → Je ne promets rien, mais ton message reste dans ma tête. _(next: `i6_end_ambiguous`)_
- 3. `i6_012_c` → Je crois que j’ai juste envie de disparaître avec quelqu’un qui ne demande rien. _(next: `i6_end_flight`)_

`i6_end_boundary` **[FIN]** **Système** : Fin Inès J6 — le joueur refuse la porte latérale pour répondre aux liens déjà ouverts.

`i6_end_ambiguous` **[FIN]** **Système** : Fin Inès J6 — Inès reste une phrase en suspens, assez présente pour troubler la fin.

`i6_end_flight` **[FIN]** **Système** : Fin Inès J6 — la porte de fuite s’ouvre : pas une romance bonus, une échappatoire dangereuse.

## Finale — `finales_mvp_complete`

Source: `narrative/t122_finales_mvp_complete.json`  
Start: `final_block_a`

`final_block_a` **Système** : FIN — Choisir ce qui reste ouvert → `final_001`

`final_001` **Système** : Le téléphone reste allumé. Les derniers messages sont là, pas rangés, pas effacés. Quelque part, quelqu’un envoie sûrement une photo de dessert moche. → `final_002`

`final_002` **Système** : Sarah a laissé le mug dans l’évier. Camille n’a pas relancé le morceau. Nico attend sans couvrir. Maya a vu la photo. Inès a laissé une porte entrouverte. → `final_003`

`final_003` **Système** : Il n’y a pas de phrase parfaite. Seulement la prochaine réponse. → `final_choice`

**CHOIX** `final_choice` — Choisir la route de fin MVP.
- 1. `final_choice_repair` → Rentrer parler à Sarah, sans promettre que tout est réparé. _(next: `final_repair_001`)_
- 2. `final_choice_camille` → Dire à Camille une phrase simple, et assumer ce qu’elle implique. _(next: `final_camille_001`)_
- 3. `final_choice_control` → Garder chaque conversation assez calme pour que la nuit passe, sans faire tomber tous les verres. _(next: `final_control_001`)_
- 4. `final_choice_fracture` → Répondre trop tard, trop court, à trop de monde. _(next: `final_fracture_001`)_
- 5. `final_choice_flight` → Ouvrir le message d’Inès au lieu de répondre aux anciens. _(next: `final_flight_001`)_

`final_repair_001` **Vous** : Je rentre. Pas pour faire comme si tout allait bien. Pour parler avant de dormir. → `final_repair_002`

`final_repair_002` **Sarah** : J’ai pas rangé le mug. → `final_repair_003`

`final_repair_003` **Sarah** : Je sais pas pourquoi je commence par ça. Peut-être parce que c’est plus facile que de dire que je tremble un peu. → `final_repair_004`

`final_repair_004` **Vous** : Ne le range pas. J’arrive et je pose mon téléphone sur la table. Écran vers le haut. → `final_repair_005`

`final_repair_005` **Sarah** : D’accord. Mais demain, on ne fait pas semblant que ce soir a tout nettoyé. → `final_repair_006`

`final_repair_006` **Nico** : Pour info, j’ai répondu propre à Maya. Et j’ai mangé tes frites émotionnelles à ta place. Tu me dois un vrai repas, pas un plan claqué. → `final_repair_007`

`final_repair_007` **Maya** : Je pose ça là : parler avant le résumé du groupe, c’était pas l’idée la plus nulle de ta semaine. Le groupe survivra sans PowerPoint de ton épaule. → `final_repair_008`

`final_repair_008` **Système** : Sarah laisse la porte ouverte. Pas grande. Pas sans peur. Juste assez pour entrer et commencer par une phrase vraie. → `final_end_reparation_fragile`

`final_end_reparation_fragile` **[FIN]** **Système** : Fin MVP — Réparation fragile : rien n’est effacé, mais le joueur choisit de revenir dans le quotidien au lieu de le contourner.

`final_camille_001` **Vous** : Je ne veux pas que tu sois une pause. Je veux te voir comme quelqu’un de réel. → `final_camille_002`

`final_camille_002` **Camille** : C’est une phrase simple. Elle arrive tard. → `final_camille_003`

`final_camille_003` **Vous** : Je sais. Et elle va faire mal ailleurs. → `final_camille_004`

`final_camille_004` **Camille** : Alors ne la rends pas jolie. Les jolies phrases glissent trop bien. → `final_camille_005`

`final_camille_005` **Sarah** : J’ai compris que tu ne rentrais pas pour parler comme tu l’avais dit. J’aurais préféré une phrase moins douce plus tôt. → `final_camille_006`

`final_camille_006` **Nico** : Je vais pas te jeter des cailloux par texto. Mais demain, évite de m’appeler pour traduire le silence des autres. Je suis ton pote, pas Google Traduction du chaos. → `final_camille_007`

`final_camille_007` **Camille** : Je suis au café. Pas pour te sauver de ce que tu viens d’ouvrir. Si tu viens, viens debout. → `final_camille_008`

`final_camille_008` **Système** : Camille ne devient pas une récompense. Elle devient une adresse réelle, avec le poids de tout ce qui n’est pas venu avec toi. → `final_end_camille_assumee`

`final_end_camille_assumee` **[FIN]** **Système** : Fin MVP — Camille assumée : le joueur choisit Camille comme relation réelle, attirante et lourde à porter, sans effacer Sarah par magie.

`final_control_001` **Vous** : Je vais répondre à tout le monde. Pas parfaitement. Juste assez pour ce soir. → `final_control_002`

`final_control_002` **Sarah** : “Ce soir”, ça revient souvent dans tes phrases. → `final_control_003`

`final_control_003` **Camille** : Je note le détour. Il est mieux habillé que les précédents. → `final_control_004`

`final_control_004` **Nico** : Bon. Personne ne crie, donc techniquement ton château de cartes tient encore. Je déteste que cette phrase soit vraie. → `final_control_005`

`final_control_005` **Maya** : Le groupe passe à autre chose pour l’instant. Enfin, à une photo de dessert moche. Profite de cette diversion historique. → `final_control_006`

`final_control_006` **Inès** : Pas grave si tu réponds plus tard. Je crois que tu as déjà beaucoup de fenêtres ouvertes. → `final_control_007`

`final_control_007` **Système** : Aucune explosion. Aucun message définitif. Seulement le téléphone, un peu plus lourd, posé près de la main. → `final_control_008`

`final_control_008` **Système** : Ça tient. Pour l’instant. Et “pour l’instant” n’a jamais semblé aussi court. → `final_end_double_vie_maintenue`

`final_end_double_vie_maintenue` **[FIN]** **Système** : Fin MVP — Équilibre maintenu : le joueur garde le contrôle une nuit de plus, mais chaque fil tire plus fort.

`final_fracture_001` **Vous** : Je répondrai demain. → `final_fracture_002`

`final_fracture_002` **Sarah** : D’accord. → `final_fracture_003`

`final_fracture_003` **Sarah** : Je vais dormir chez ma sœur ce soir. Le mug est dans l’évier si tu rentres. → `final_fracture_004`

`final_fracture_004` **Camille** : Pas maintenant, alors. Peut-être pas demain non plus. → `final_fracture_005`

`final_fracture_005` **Nico** : Je t’aime bien, mon reuf, mais là je ferme le standard. Je suis pas ouvert 24/7. → `final_fracture_006`

`final_fracture_006` **Maya** : On va dire que j’ai rien vu. Mais je vais surtout arrêter de regarder pour toi. Même mon visage neutre demande des congés. → `final_fracture_007`

`final_fracture_007` **Système** : Les messages ne disparaissent pas. Ils arrêtent juste de revenir vers toi. → `final_fracture_008`

`final_fracture_008` **Système** : Le silence n’a pas besoin de faire du bruit pour changer une pièce. → `final_end_tout_se_fissure`

`final_end_tout_se_fissure` **[FIN]** **Système** : Fin MVP — Tout se fissure : pas de scène publique, mais les liens se retirent un par un.

`final_flight_001` **Vous** : Tu disais que tu avais écrit trois versions. Garde celle-ci ouverte encore un peu. → `final_flight_002`

`final_flight_002` **Inès** : Je peux. Mais je ne veux pas devenir l’endroit où tu vas parce que les autres pièces ont trop de lumière. → `final_flight_003`

`final_flight_003` **Vous** : Je sais. Je crois que j’ai juste envie d’un endroit qui ne demande rien. → `final_flight_004`

`final_flight_004` **Inès** : Les endroits qui ne demandent rien finissent souvent par prendre beaucoup. → `final_flight_005`

`final_flight_005` **Sarah** : Je vais dormir. On parlera si tu rentres vraiment. → `final_flight_006`

`final_flight_006` **Camille** : Je ne relance pas le morceau. Bonne nuit. → `final_flight_007`

`final_flight_007` **Système** : Tu ouvres une nouvelle fenêtre au lieu de répondre aux anciennes. L’air entre. Le froid aussi. → `final_flight_008`

`final_flight_008` **Inès** : Oublie si c’est trop. Ou réponds si c’est juste assez loin. Pas grave si tu réponds plus tard. Peut-être même mieux. → `final_end_fuite_en_avant`

`final_end_fuite_en_avant` **[FIN]** **Système** : Fin MVP — Fuite en avant / solitude : le joueur choisit l’échappatoire, pas une nouvelle histoire sauvée.
