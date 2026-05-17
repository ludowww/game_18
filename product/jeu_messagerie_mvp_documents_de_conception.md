# Jeu de messagerie — Documents de conception à conserver

## Objectif de ce dossier

Ce dossier sert de base stable pour reconstruire le scénario du jeu de simulation de conversations sous Godot 4.

Le but est d’éviter de commencer directement par l’écriture des dialogues, afin de ne pas créer un arbre ingérable. On construit d’abord une architecture narrative claire : vérité cachée, personnages, arcs, variables, scènes pivots, fins, puis seulement ensuite les dialogues.

Le MVP visé est une histoire courte de 6 jours, centrée sur une tension relationnelle après une soirée ambiguë.

---

# Liste des documents à garder

## 00 — Vision du jeu

### Rôle du document

Ce document définit l’idée centrale du jeu : thème, promesse joueur, ton, limites du MVP et type d’expérience visée.

### À contenir

- pitch court ;
- thème principal ;
- promesse de gameplay ;
- ton émotionnel ;
- ce que le jeu n’est pas ;
- public visé ;
- limites du MVP.

### Version de départ

Le jeu est une simulation narrative par messagerie dans laquelle le joueur doit gérer plusieurs conversations après une soirée ambiguë. Chaque personnage détient une partie différente de la vérité. Le joueur choisit quoi dire, à qui répondre en premier, quoi cacher, quoi assumer, quoi supprimer, quoi garder, et combien de temps il peut rester flou avant que les autres ne décident à sa place.

Le thème central n’est pas seulement l’infidélité ou la séduction, mais l’évitement du choix, les demi-vérités, la culpabilité, le désir, et la manière dont plusieurs liens peuvent être abîmés par une absence de clarté.

Le MVP ne doit pas être un dating sim classique où il faut séduire le bon personnage. Il doit être un jeu de tension relationnelle où les choix ont des conséquences émotionnelles, sociales et intimes.

---

## 01 — Vérité canonique de la soirée

### Rôle du document

Ce document contient ce qui s’est réellement passé avant le début du jeu.

Même si le joueur découvre les faits par fragments, l’auteur doit connaître la vérité exacte. Ce document sert de socle pour éviter les contradictions.

---

# Version canonique proposée — Soirée déclencheuse

## Contexte général

La soirée a lieu un vendredi soir, dans un bar calme mais animé, à l’occasion d’un anniversaire ou d’une soirée organisée par Maya. Ce n’est pas une grosse fête, plutôt une soirée de groupe : quelques verres, des discussions par petits cercles, des photos, des allers-retours dehors pour prendre l’air.

Le joueur vient avec Sarah, sa compagne. Sarah connaît bien Maya, sa meilleure amie, et connaît aussi Nico et Inès. Camille, collègue de travail du joueur, est présente parce qu’elle a été invitée dans le prolongement d’un afterwork ou parce que le joueur a proposé qu’elle passe. Sa présence n’est pas officiellement problématique, mais elle crée un léger décalage : elle appartient au monde professionnel du joueur, pas au noyau intime Sarah/Maya/Nico.

Nico est présent comme ami proche et confident du joueur. Inès est là aussi, plus discrète, un peu en retrait du groupe, observatrice sans être centrale.

---

## Situation avant la soirée

Depuis plusieurs semaines, le joueur et Camille échangent de plus en plus au travail et par messages. Rien n’a été clairement avoué, mais la complicité a changé de nature : private jokes, regards, pauses prises ensemble, messages hors horaires de travail, attention aux détails.

Sarah sent que le joueur est plus absent ces derniers temps, sans savoir exactement pourquoi. Elle ne soupçonne pas forcément Camille au départ, mais elle sent une baisse de présence.

Maya a déjà remarqué quelques micro-signaux : le joueur regarde davantage son téléphone, répond parfois avec un sourire différent, mentionne Camille d’une manière un peu trop neutre pour être totalement naturelle.

Nico sait que le joueur apprécie beaucoup Camille. Il a peut-être déjà reçu des confidences floues, du type : “je sais pas, avec elle c’est différent”, mais il ne sait pas jusqu’où cela va.

Inès ne sait presque rien. Elle connaît seulement le joueur comme quelqu’un du groupe, parfois drôle, parfois ailleurs.

---

## Déroulé de la soirée

### 1. Début de soirée

Le joueur arrive avec Sarah. Sarah est plutôt douce, présente, mais légèrement fatiguée. Elle essaie de passer une bonne soirée.

Maya accueille le groupe, prend quelques photos, lance des piques, observe les dynamiques sociales.

Nico détend l’ambiance avec des blagues. Il remarque vite que le joueur n’est pas complètement détendu.

Camille arrive un peu plus tard. Le joueur semble instantanément plus attentif. Ce changement n’est pas énorme, mais visible pour quelqu’un qui le connaît.

Inès reste un peu à distance, parle par petites touches, observe plus qu’elle ne s’impose.

---

### 2. Premiers signaux

Camille et le joueur ont quelques échanges courts, discrets, complices. Rien de frontal, mais leur rythme diffère du reste du groupe. Ils se comprennent vite, rient de détails que les autres n’ont pas.

Sarah remarque un ou deux moments, mais elle ne veut pas être injuste. Elle se dit qu’elle exagère peut-être.

Maya remarque davantage. Elle ne conclut rien, mais elle note l’énergie entre eux.

Nico remarque aussi, mais préfère plaisanter plutôt que confronter.

---

### 3. Le moment dehors

Plus tard dans la soirée, le joueur sort prendre l’air. La raison officielle peut être simple : trop de bruit, besoin de respirer, fatigue, cigarette d’un autre, appel manqué, ou simple prétexte.

Camille le rejoint quelques minutes après. Elle ne le fait pas de manière spectaculaire. Elle peut dire qu’elle voulait aussi prendre l’air.

Ils restent dehors environ vingt minutes.

Il ne se passe pas nécessairement un acte physique irréparable. La version canonique du MVP est plus subtile :

- ils ne couchent pas ensemble ;
- ils ne s’embrassent pas forcément ;
- mais ils se tiennent trop près ;
- Camille dit quelque chose qui révèle qu’elle sent le trouble ;
- le joueur ne nie pas vraiment ;
- il y a peut-être une main posée sur son bras, son épaule ou sa main ;
- un silence dure trop longtemps ;
- l’un des deux dit une phrase qui franchit une limite émotionnelle.

Phrase possible de Camille :

> “Avec toi, j’ai parfois l’impression que le reste devient moins étroit.”

Phrase possible du joueur :

> “C’est justement ça qui me fait peur.”

Le moment est intime, chargé, mais assez ambigu pour que chacun puisse ensuite essayer de le minimiser.

---

### 4. Ce que chacun voit ou comprend

Sarah ne voit pas toute la scène dehors. Elle remarque surtout l’absence, puis le retour. Le joueur revient différent : plus silencieux, plus tendu, moins disponible. Camille revient séparément ou légèrement après, mais assez proche dans le timing pour que cela crée un doute.

Maya remarque que le joueur et Camille ont manqué à l’appel sur une photo de groupe ou pendant un moment précis. Elle possède peut-être une photo prise pendant leur absence, montrant le groupe sans eux, ou une photo prise au retour où un détail de posture les rend visibles.

Nico couvre l’absence du joueur sur le moment. Quand Sarah demande où il est, Nico improvise quelque chose comme : “il est sorti deux minutes” ou “il était avec moi tout à l’heure”. Ce n’est pas un mensonge énorme au départ, mais ça devient une couverture.

Inès croise le joueur un peu plus tard, seul ou à l’écart, après le retour. Elle ne sait pas ce qui s’est passé avec Camille. Ce qu’elle voit, c’est un état : le joueur a l’air triste, déplacé, comme s’il cherchait une sortie.

Camille sait exactement que le moment dehors n’était pas neutre. Elle sait aussi qu’il peut être minimisé par le joueur s’il prend peur.

---

### 5. Fin de soirée

La fin de soirée ne provoque pas d’explosion. Tout reste contenu.

Sarah rentre avec le joueur ou rentre en même temps que lui, mais elle sent qu’il est absent. Elle n’a pas envie de faire une scène devant les autres.

Camille repart avec une phrase non dite, ou un dernier regard. Elle peut envoyer plus tard un message qu’elle supprime, ou attendre le lendemain matin.

Nico comprend qu’il a couvert quelque chose qui pourrait grossir.

Maya hésite entre plaisanter et s’inquiéter.

Inès garde l’image d’un joueur vulnérable, pas forcément coupable.

---

## Vérité émotionnelle de la soirée

Le vrai problème n’est pas que le joueur ait commis un acte clairement définissable. Le vrai problème est qu’il a vécu avec Camille un moment d’intimité qu’il n’a pas su interrompre, et qu’il est revenu auprès de Sarah avec quelque chose de déplacé intérieurement.

Ce n’est pas seulement une question de fidélité physique. C’est une question de présence, de loyauté émotionnelle, de demi-vérité et de fuite.

---

## Ce qui reste volontairement interprétable

Pour garder de la nuance, certains éléments peuvent rester modulables selon les choix du joueur ou selon les révélations progressives :

- y a-t-il eu un contact physique précis ?
- le joueur a-t-il initié le moment ou simplement laissé faire ?
- Camille a-t-elle voulu tester une limite ou a-t-elle elle-même été dépassée ?
- Nico a-t-il vraiment menti ou seulement simplifié ?
- Maya a-t-elle une preuve claire ou seulement une accumulation de détails ?
- Sarah soupçonne-t-elle Camille dès le début ou seulement l’absence du joueur ?

Mais la base reste fixe : il y a eu un moment intime dehors, assez fort pour que tout le monde ressente quelque chose le lendemain.

---

## 02 — Carte de connaissance des personnages

### Rôle du document

Ce document définit ce que chaque personnage sait, croit, ignore ou soupçonne après la soirée déclencheuse.

Il empêche les personnages de devenir omniscients. Chacun doit réagir depuis son morceau de vérité, son lien avec le joueur, ses loyautés et ses limites.

---

# Carte de connaissance — Version MVP

## Principe général

Chaque personnage possède une partie différente de la soirée :

- Sarah ressent l’absence et le changement du joueur.
- Camille connaît le moment intime dehors.
- Maya observe les incohérences sociales.
- Nico sait qu’il a couvert quelque chose.
- Inès perçoit une faille émotionnelle sans connaître les faits.

Le joueur, lui, est le seul à pouvoir relier tous ces morceaux. C’est ce qui crée le gameplay : il peut clarifier, minimiser, mentir, éviter, ou construire plusieurs versions incompatibles.

---

# Sarah

## Position relationnelle

Sarah est la compagne du joueur. Elle représente la maison, la confiance installée, les routines, l’histoire commune et la peur que le couple devienne une façade.

Elle n’est pas une enquêtrice. Elle ne cherche pas à coincer le joueur. Elle cherche d’abord à comprendre pourquoi elle ne le reconnaît plus complètement.

## Ce qu’elle sait

- Le joueur était présent avec elle à la soirée.
- Il a été moins disponible que d’habitude.
- Il est sorti ou a disparu pendant un moment.
- Camille était également absente à un moment proche.
- Le joueur est revenu différent : plus silencieux, plus tendu, plus ailleurs.
- Nico a donné une explication qui semblait improvisée ou incomplète.
- Le joueur est souvent plus attentif à son téléphone depuis quelque temps.

## Ce qu’elle croit ou soupçonne

- Quelque chose s’est déplacé dans le couple.
- Le joueur cache peut-être moins un fait précis qu’un état intérieur.
- Camille a peut-être un rôle dans cette absence, mais Sarah n’en est pas certaine au début.
- Le joueur pourrait essayer de la protéger en ne disant pas tout, ce qui l’inquiète encore plus.

## Ce qu’elle ignore

- Ce qui s’est réellement dit dehors entre le joueur et Camille.
- S’il y a eu un contact physique.
- Si Nico ment volontairement ou s’il a seulement couvert maladroitement.
- Si Camille est une vraie menace ou seulement le symptôme d’un problème plus profond.
- Ce que le joueur raconte aux autres.

## Ce qu’elle veut obtenir

- Une présence réelle.
- Une parole qui ne sonne pas comme une esquive.
- La confirmation qu’elle n’invente pas tout.
- Une vérité assez claire pour ne pas devoir devenir suspicieuse.

## Ce qu’elle peut accepter

- Une vérité douloureuse dite avec respect.
- Une confusion honnête.
- Une reconnaissance de l’absence ou du trouble.
- Une discussion imparfaite mais sincère.

## Ce qu’elle ne supportera pas

- Être prise pour idiote.
- Se faire dire qu’elle exagère alors qu’elle sent quelque chose de réel.
- Les versions qui changent selon les personnes.
- Les promesses non tenues répétées.
- Le joueur présent physiquement mais absent émotionnellement.

## Limite de non-retour

Sarah peut entendre que le joueur a été troublé par Camille. Elle se ferme surtout si le joueur détruit sa confiance en sa propre perception.

## Indices de dialogue

Sarah doit souvent partir d’un détail concret :

- un repas gardé ;
- un retour tardif ;
- un téléphone retourné ;
- une phrase dite différemment ;
- une promesse oubliée ;
- une fatigue qu’elle connaît trop bien.

Elle doit rarement accuser frontalement au début. Elle doit plutôt formuler un malaise.

Exemples :

> “Je veux pas te faire un procès. J’ai juste besoin de comprendre pourquoi je me sens aussi loin de toi alors que t’es là.”

> “Dis-moi juste si je me trompe. Mais ne me dis pas que j’invente si tu sais que non.”

---

# Camille

## Position relationnelle

Camille est la collègue du joueur. Elle appartient au monde du travail, donc à un espace distinct de Sarah : pauses, messages en journée, private jokes, fatigue professionnelle, conversations qui commencent par le banal puis deviennent personnelles.

Elle n’est pas seulement une tentation. Elle représente la possibilité pour le joueur d’être vu autrement.

## Ce qu’elle sait

- Elle a rejoint le joueur dehors.
- Le moment dehors n’était pas neutre.
- Il y a eu une parole ou un silence qui a franchi une limite émotionnelle.
- Le joueur n’a pas réellement interrompu le moment.
- Le joueur peut avoir peur de ce que cela implique.
- Sarah était présente à la soirée.

## Ce qu’elle croit ou soupçonne

- Le joueur risque de minimiser pour préserver son confort.
- Il pourrait vouloir garder Camille comme une respiration sans assumer le coût réel.
- Il est attiré par elle, mais pas forcément prêt à être honnête.
- Il veut peut-être se sentir vivant sans devoir choisir.

## Ce qu’elle ignore

- Ce que Sarah sait exactement.
- Ce que le joueur a dit à Sarah après la soirée.
- Jusqu’où Nico est impliqué.
- Ce que Maya a vu.
- Si le joueur est prêt à perdre quelque chose pour être cohérent.

## Ce qu’elle veut obtenir

- Que le joueur ne fasse pas comme si le moment dehors était banal.
- Être reconnue comme une personne, pas comme une parenthèse.
- Ne pas être sexualisée uniquement quand le joueur a besoin d’échapper à Sarah.
- Une forme d’honnêteté, même si elle n’est pas confortable.

## Ce qu’elle peut accepter

- Le trouble.
- La lenteur.
- Une limite posée avec respect.
- Le fait que le joueur dise : “je ne peux pas te demander ça tant que je ne suis pas clair.”

## Ce qu’elle ne supportera pas

- Être gardée en option.
- Être appelée seulement la nuit ou dans les moments de fuite.
- Les phrases qui sonnent profondes mais ne coûtent rien.
- Une demande sexuelle trop directe si elle sent que le joueur fuit sa culpabilité.
- Les promesses floues.

## Limite de non-retour

Camille peut accepter une tension compliquée. Elle se retire si elle comprend qu’elle sert de refuge émotionnel ou sexuel pendant que le joueur refuse de clarifier sa situation.

## Indices de dialogue

Camille doit souvent toucher juste avec peu de mots. Elle peut être joueuse, mais elle voit les détours.

Exemples :

> “Tu réponds comme quelqu’un qui cherche une issue, pas une vérité.”

> “Je peux entendre que tu sois perdu. Mais je ne veux pas devenir l’endroit où tu te perds exprès.”

---

# Maya

## Position relationnelle

Maya est la meilleure amie de Sarah, mais elle est aussi amie avec le joueur. Elle n’est donc pas une ennemie. Sa tension vient d’un conflit de loyauté : elle aime Sarah, apprécie le joueur, mais refuse d’être mêlée à une version fausse.

Elle représente le regard social : ce que les autres voient, les micro-incohérences, les photos, les silences de groupe, les timings suspects.

## Ce qu’elle sait

- Le joueur et Camille ont disparu ou manqué à l’appel au même moment.
- Sarah a senti quelque chose.
- Nico a donné une explication peu solide.
- Le joueur a parfois un comportement étrange avec son téléphone.
- Certaines attitudes du joueur et de Camille pendant la soirée étaient trop synchronisées pour être totalement anodines.

## Ce qu’elle croit ou soupçonne

- Il existe une tension entre le joueur et Camille.
- Sarah risque d’être blessée.
- Le joueur va peut-être essayer de contrôler ce que chacun sait.
- Nico est peut-être déjà utilisé comme couverture.

## Ce qu’elle ignore

- Ce qui s’est réellement passé dehors.
- Si Sarah et le joueur ont déjà parlé.
- Si Camille est consciente de la douleur potentielle pour Sarah.
- Si le joueur veut clarifier ou simplement gagner du temps.

## Ce qu’elle veut obtenir

- Ne pas être forcée à choisir entre Sarah et le joueur.
- Ne pas devoir mentir.
- Que le joueur comprenne qu’elle voit des choses.
- Protéger Sarah sans devenir juge ou policière.

## Ce qu’elle peut accepter

- Une explication maladroite mais honnête.
- Que le joueur lui dise : “je vais gérer avec Sarah.”
- Un silence temporaire si elle sent qu’il n’est pas manipulateur.

## Ce qu’elle ne supportera pas

- Qu’on lui demande explicitement de mentir à Sarah.
- Qu’on la traite comme si elle inventait.
- Qu’on lui dise de ne pas s’en mêler alors qu’elle est déjà impliquée affectivement.
- Qu’on utilise son humour pour minimiser la gravité.

## Limite de non-retour

Maya peut fermer les yeux sur un détail. Elle ne peut pas porter une accumulation ni mentir directement à Sarah.

## Indices de dialogue

Maya doit rester vive, piquante, sociale. Elle met la pression sans toujours le dire frontalement.

Exemples :

> “Je pose ça là : ton timing est une œuvre d’art.”

> “Je peux faire semblant de pas voir une coïncidence. Pas douze.”

---

# Nico

## Position relationnelle

Nico est le confident du joueur. Il est loyal, drôle, proche, mais il n’est pas un outil. Il peut couvrir un moment, pas porter une double vie.

Il représente l’amitié, l’alibi, l’humour, puis la limite.

## Ce qu’il sait

- Le joueur est troublé par Camille, au moins un peu.
- Il a couvert l’absence du joueur pendant la soirée.
- Son explication peut être vérifiée ou contredite.
- Sarah pourrait lui poser des questions.
- Maya commence peut-être à observer.

## Ce qu’il croit ou soupçonne

- Le joueur ne maîtrise pas aussi bien la situation qu’il le pense.
- Il veut éviter de choisir.
- Il risque de demander à Nico de mentir davantage.
- Le problème n’est pas seulement Camille, mais le rapport du joueur à la vérité.

## Ce qu’il ignore

- Le contenu exact du moment dehors.
- Le niveau d’intimité avec Camille.
- Ce que le joueur a promis à Sarah.
- Ce que Maya a vu.
- Ce qu’Inès perçoit.

## Ce qu’il veut obtenir

- Aider le joueur à ne pas faire n’importe quoi.
- Garder une amitié honnête.
- Ne pas être transformé en alibi permanent.
- Pouvoir plaisanter sans devenir complice.

## Ce qu’il peut accepter

- Une demande d’aide ponctuelle.
- Une confession maladroite.
- Le fait que le joueur soit perdu.
- Un aveu du type : “j’ai merdé, je sais pas quoi faire.”

## Ce qu’il ne supportera pas

- Être utilisé à répétition.
- Apprendre que le joueur lui a aussi menti.
- Être forcé à mentir à Sarah ou Maya.
- Devenir responsable d’une situation qu’il n’a pas créée.

## Limite de non-retour

Nico peut être complice d’un moment de panique. Il ne peut pas devenir le garant d’une version fausse sur plusieurs jours.

## Indices de dialogue

Nico doit alterner humour et lucidité. Ses phrases sérieuses doivent arriver comme des éclairs.

Exemples :

> “Je peux couvrir un blanc. Pas toute ta vie.”

> “Là c’est plus un plan claqué, c’est une série à budget moyen.”

---

# Inès

## Position relationnelle

Inès est une amie du groupe, plus discrète et énigmatique. Elle n’est pas au centre du conflit. Elle ne possède pas de preuve. Elle représente la porte latérale : une possibilité de parler ailleurs, avec quelqu’un qui demande moins de comptes au départ.

Elle ne doit pas devenir une romance complète dans le MVP. Elle sert surtout de miroir de la fuite.

## Ce qu’elle sait

- Elle a vu le joueur isolé ou absent émotionnellement pendant ou après la soirée.
- Il avait l’air triste, ailleurs, ou comme s’il cherchait une sortie.
- L’ambiance autour de lui semblait légèrement chargée.

## Ce qu’elle croit ou soupçonne

- Le joueur traverse quelque chose qu’il ne dit pas.
- Il cherche peut-être un endroit où ne pas avoir à expliquer.
- Elle peut être tentée de lui offrir une parenthèse, mais sent que ce n’est pas neutre.

## Ce qu’elle ignore

- La tension exacte avec Camille.
- L’état du couple avec Sarah.
- Le rôle de Nico.
- Ce que Maya a vu.
- Ce que le joueur veut réellement.

## Ce qu’elle veut obtenir

- Comprendre sans forcer.
- Créer un espace de parole doux, mais pas nécessairement romantique.
- Être respectée dans son propre rythme.

## Ce qu’elle peut accepter

- Un échange fragile.
- Un silence.
- Une réponse honnête du type : “je ne sais pas pourquoi je te parle de ça.”

## Ce qu’elle ne supportera pas

- Être utilisée comme échappatoire évidente.
- Devenir la troisième option d’un choix que le joueur refuse de faire.
- Être poussée vers une intimité trop explicite trop vite.

## Limite de non-retour

Inès peut ouvrir une parenthèse. Elle se retire si elle sent que le joueur veut seulement disparaître dans une nouvelle attention.

## Indices de dialogue

Inès doit écrire avec douceur, hésitation, et une étrangeté légère.

Exemples :

> “Je crois que les autres ont vu que tu étais absent. Moi j’ai surtout vu que tu avais l’air de vouloir partir.”

> “C’est peut-être bizarre à dire. Oublie si c’est trop.”

---

# Règles d’écriture issues de cette carte

## Règle 1 — Personne ne sait tout

Chaque personnage doit avoir des angles morts. Même une phrase très juste doit venir d’une observation crédible, pas d’une omniscience scénaristique.

## Règle 2 — Les soupçons doivent naître du banal

Les soupçons viennent de détails : horaires, attitudes, silences, téléphone, photos, promesses oubliées, réactions trop rapides ou trop lentes.

## Règle 3 — Les personnages ont des loyautés contradictoires

Maya n’est pas contre le joueur, mais elle est avec Sarah.
Nico est avec le joueur, mais pas contre Sarah.
Camille désire peut-être le joueur, mais pas au prix de sa dignité.
Inès peut être curieuse, mais pas servir de fuite.
Sarah veut croire le joueur, mais pas contre elle-même.

## Règle 4 — Les limites doivent apparaître progressivement

Jour 1 : malaise.
Jour 2 : versions.
Jour 3 : banalité et attachement.
Jour 4 : intimité et risque.
Jour 5 : limites.
Jour 6 : conséquence.

## Règle 5 — Les choix du joueur doivent être lus différemment selon les personnages

La même phrase peut rassurer Sarah, frustrer Camille, inquiéter Maya, agacer Nico ou ouvrir une porte à Inès. Les variables doivent refléter cette pluralité.

---

## 03 — Bible des personnages et voix de messagerie

### Configuration officielle des relations

- Camille est une collègue de travail du joueur. Elle appartient donc à un espace distinct de la maison, avec des horaires, des messages et une intimité qui peuvent se construire en parallèle du couple.
- Maya est la meilleure amie de Sarah, mais elle est aussi amie avec le joueur. Elle n’est donc pas une ennemie du joueur : sa tension vient du conflit entre loyauté envers Sarah, affection pour le joueur, et refus d’être mêlée à un mensonge.
- Inès est une amie du groupe, plus discrète et énigmatique. Elle est assez proche pour être présente, mais assez périphérique pour devenir une porte latérale, un espace moins chargé par l’histoire du couple.
- Nico est le confident du joueur. Il connaît le joueur mieux que les autres sur certains aspects, mais il n’est pas obligé de tout porter. Sa loyauté a des limites.

### Rôle du document

Ce document sert à écrire les dialogues sans perdre la cohérence des voix.

Chaque personnage doit être reconnaissable par :

- son rythme ;
- ses sujets banals ;
- sa manière d’éviter ou d’affronter ;
- ses tics de langage ;
- sa manière d’être blessé ;
- sa limite relationnelle ;
- son rapport au désir, au silence, au téléphone et à la vérité.

---

# Sarah — relation officielle / maison / confiance

## Fonction narrative

Sarah représente la maison, la stabilité, l’histoire commune, les routines, la confiance et la culpabilité.

Elle n’est pas seulement “la compagne blessée”. Elle doit aussi être désirable, drôle parfois, tendre, familière. Le joueur doit comprendre qu’il ne risque pas seulement de perdre un statut de couple, mais une vraie intimité construite.

## Voix normale

Sarah écrit simplement, sans chercher la formule brillante. Elle part souvent du concret.

Rythme :

- messages courts ou moyens ;
- ponctuation douce ;
- peu d’ironie ;
- questions pratiques ;
- phrases qui contiennent plus qu’elles ne disent.

Exemples :

> “Tu rentres manger ?”

> “J’ai pris du café. Le bon cette fois.”

> “Je t’ai gardé une assiette, au cas où.”

> “Tu sais où t’as mis le chargeur du salon ?”

## Voix tendre / banale

Sarah crée l’intime par les détails domestiques.

Sujets :

- repas ;
- canapé ;
- fatigue ;
- courses ;
- linge ;
- café ;
- séries regardées à moitié ;
- blagues privées anciennes ;
- objets laissés dans l’appartement.

Exemples :

> “J’ai mis ton pull. Il traînait sur la chaise.”

> “J’ai acheté les yaourts que tu prends toujours en disant que c’est pas toi qui les finis.”

> “Le voisin a encore bloqué l’entrée avec son vélo. J’ai pensé à ton imitation débile.”

> “Tu veux qu’on regarde un truc ce soir ou tu comptes t’endormir au bout de douze minutes ?”

## Voix inquiète

Sarah ne veut pas accuser trop vite. Elle formule un malaise.

Exemples :

> “Je sais pas comment le dire, mais t’es bizarre depuis hier.”

> “C’est peut-être moi. Mais j’ai l’impression que tu me réponds depuis une autre pièce, même quand t’es là.”

> “Je veux pas fouiller. Je veux juste comprendre.”

> “Tu peux me dire si je me trompe ? Vraiment.”

## Voix blessée

Quand Sarah est blessée, elle devient plus courte. Elle ne crie pas forcément. Elle peut se retirer.

Exemples :

> “D’accord.”

> “Laisse tomber, j’ai mangé.”

> “Je vais arrêter de demander.”

> “C’est fou comme je me sens seule pour un truc qui nous concerne tous les deux.”

## Voix de limite

Sarah n’exige pas une vérité parfaite. Elle exige de ne pas être dépossédée de sa perception.

Exemples :

> “Tu peux me dire quelque chose de difficile. Je crois que je peux l’entendre. Mais pas quelque chose de faux.”

> “Ne me demande pas de croire que je n’ai rien senti.”

> “Je préfère une vérité qui fait mal à une version qui me rend folle.”

## Tics / expressions

- “je sais pas comment le dire”
- “c’est peut-être moi”
- “j’ai l’impression que…”
- “tu es là sans être là”
- “je veux pas te faire un procès”
- “juste dis-moi si je me trompe”

## Réactions typiques aux choix du joueur

Si le joueur est présent : Sarah se radoucit, mais reste attentive.

Si le joueur minimise : Sarah doute d’elle-même, puis devient froide.

Si le joueur avoue une confusion : Sarah peut être blessée mais reste dans l’échange.

Si le joueur accuse Sarah d’exagérer : grosse perte de confiance.

Si le joueur promet puis oublie : Sarah mémorise. La blessure revient plus tard sous forme de détail.

## Do

- La rendre humaine, pas naïve.
- Lui donner des moments désirables.
- Faire sentir qu’elle connaît le joueur.
- Utiliser le banal comme preuve d’intimité.
- Laisser des scènes sans reproche.

## Don’t

- Sarah détective.
- Sarah qui devine tout trop vite.
- Sarah qui parle en concepts froids.
- Sarah seulement obstacle moral.
- Sarah qui devient uniquement la culpabilité.

---

# Camille — collègue / tension affective / lucidité / désir

## Fonction narrative

Camille représente l’autre espace de vie du joueur : le travail, les pauses, les messages en journée, la possibilité d’être vu autrement.

Elle est dangereuse parce qu’elle ne propose pas seulement du désir. Elle propose au joueur une version de lui-même plus vivante, plus fine, plus écoutée.

Elle doit être attirante par sa lucidité, pas seulement par sa séduction.

## Voix normale

Camille écrit avec précision. Elle dit souvent les choses par détour, mais ses détours touchent juste.

Rythme :

- messages courts ;
- phrases incisives ;
- silences significatifs ;
- peu d’emojis ;
- humour sec ;
- observations fines.

Exemples :

> “T’as survécu à la réunion ou tu fais semblant par dignité ?”

> “J’ai encore ton stylo. À ce stade c’est soit du vol, soit un symbole très pauvre.”

> “Tu réponds plus vite aux mails qu’aux vraies questions.”

> “Je note le détour.”

## Voix légère / complicité de travail

Camille peut exister hors drame par des private jokes professionnelles.

Sujets :

- réunions absurdes ;
- pauses café ;
- fatigue au bureau ;
- dossiers ;
- blagues internes ;
- trajets ;
- morceaux de musique envoyés pendant une journée trop longue.

Exemples :

> “Il a dit ‘synergie’ trois fois. J’ai pensé à toi, malheureusement.”

> “J’ai pris le dernier café correct. Je ne regrette rien.”

> “Tu avais raison pour le dossier. Ne t’habitue pas à cette phrase.”

> “Je t’envoie ce morceau avant que la journée me transforme en meuble.”

## Voix ambiguë

Camille suggère plus qu’elle ne déclare. Elle teste si le joueur assume.

Exemples :

> “Tu vas faire comme si c’était juste une discussion dehors ?”

> “C’est pratique, ta façon de t’arrêter au milieu des phrases. On peut y mettre ce qu’on veut.”

> “Tu fais semblant de ne pas comprendre, ou c’est pour me laisser faire le sale boulot ?”

> “Hier, t’étais pas exactement quelqu’un qui voulait rentrer.”

## Voix intime / désir

Camille ne doit pas devenir frontalement disponible sans conditions. Son désir dépend du respect, du contexte et de la confiance.

Exemples :

> “J’ai hésité à t’envoyer quelque chose. Et maintenant je trouve déjà ridicule de l’avoir écrit.”

> “Je sais pas si j’ai envie que tu répondes, ou si c’est justement le problème.”

> “Il y a des choses que je peux dire. Et d’autres que je ne veux pas offrir à quelqu’un qui repartira en disant qu’il était perdu.”

## Voix blessée / lucide

Camille ne supplie pas. Elle se retire avec dignité.

Exemples :

> “Je crois que tu aimes surtout l’idée d’un endroit où respirer.”

> “Je ne veux pas être la pièce où tu vas quand le reste de ta vie manque d’air.”

> “Tu as cette façon de rendre les choses intenses sans jamais les rendre vraies.”

> “Pas maintenant, alors.”

## Voix de limite

Sa limite n’est pas seulement morale. Elle tient à sa dignité.

Exemples :

> “Je peux accepter que ce soit compliqué. Pas que tu me ranges dans un coin pratique.”

> “Si tu veux me désirer, commence par ne pas m’utiliser.”

> “Je ne suis pas une pause dans ta journée.”

## Tics / expressions

- “je note le détour”
- “tu fais semblant de…”
- “ça sonnait presque vrai”
- “pas maintenant, alors”
- “je ne sais pas si c’est lâche ou prudent”
- “tu as cette façon de répondre à côté”

## Réactions typiques aux choix du joueur

Si le joueur assume le trouble : Camille devient plus ouverte, mais reste prudente.

Si le joueur minimise : Camille devient plus coupante.

Si le joueur sexualise trop vite : Camille se ferme.

Si le joueur respecte une limite : respect_camille augmente, même si tension_camille baisse temporairement.

Si le joueur clarifie avec Sarah : Camille peut rester distante, mais elle reconnaît la cohérence.

## Do

- La rendre attirante par sa précision.
- Lui donner une vie hors du joueur.
- La faire exister dans le monde du travail.
- Différencier désir, confiance et respect.
- Lui permettre de dire non.

## Don’t

- Camille récompense automatique.
- Camille jalouse caricaturale.
- Camille qui donne des ultimatums en boucle.
- Camille qui parle comme le thème du jeu.
- Camille qui devient seulement “la route sexy”.

---

# Maya — meilleure amie de Sarah / regard social / piquant

## Fonction narrative

Maya représente ce que le groupe voit. Elle observe les absences, les timings, les photos, les gestes, les micro-incohérences.

Elle est la meilleure amie de Sarah, mais elle aime aussi le joueur. Son conflit est donc humain : elle ne veut pas le piéger, mais elle ne veut pas trahir Sarah.

## Voix normale

Maya écrit vite, avec du mordant. Elle utilise l’humour pour tester, prévenir, gêner ou protéger.

Rythme :

- messages courts ;
- relances rapides ;
- humour sec ;
- petites formules ;
- observations précises ;
- parfois absence de majuscules.

Exemples :

> “je pose ça là”

> “intéressant”

> “ton timing est une œuvre d’art”

> “je veux pas être mêlée, mais j’ai des yeux”

## Voix légère / sociale

Maya doit apporter de l’air, du groupe, des photos, du bruit social.

Sujets :

- soirées ;
- photos de groupe ;
- afterworks ;
- danse ridicule de Nico ;
- organisation ;
- messages de groupe ;
- commentaires piquants mais affectueux.

Exemples :

> “preuve officielle que Nico ne devrait jamais danser.”

> “j’ai une photo de toi avec une tête de type qui découvre le prix des avocats.”

> “on refait un truc vendredi ou tout le monde prétend avoir une vie saine ?”

> “Sarah était jolie hier. Voilà, message gratuit.”

## Voix suspicieuse

Maya ne dit pas tout de suite “je sais”. Elle met une pression légère.

Exemples :

> “c’est sûrement une coïncidence hein.”

> “vous avez disparu où tous les deux à un moment ? question pour une amie. qui est moi.”

> “j’ai une photo où il manque deux personnes. devine le thème.”

> “je vais faire semblant de ne pas avoir noté. mais je note.”

## Voix protectrice

Quand elle parle plus sérieusement, elle protège Sarah sans forcément attaquer le joueur.

Exemples :

> “Je te le dis parce que je t’aime bien aussi. Mais Sarah, c’est Sarah.”

> “Me mets pas dans une position où je dois choisir ce que je tais.”

> “Je peux rire de beaucoup de trucs. Pas du moment où elle commence à douter d’elle.”

## Voix de limite

Maya refuse de devenir complice.

Exemples :

> “Si Sarah me demande directement, je mens pas.”

> “Je peux faire semblant de pas voir une coïncidence. Pas une accumulation.”

> “Ne me demande pas de porter un truc que t’as pas le courage de poser toi-même.”

## Tics / expressions

- “je note”
- “je pose ça là”
- “intéressant”
- “on va dire que j’ai rien vu”
- “c’est sûrement une coïncidence hein”
- “ton timing est une œuvre d’art”

## Réactions typiques aux choix du joueur

Si le joueur est franc : Maya peut rester piquante mais respecte.

Si le joueur lui demande de mentir : suspicion_maya augmente fortement.

Si le joueur minimise trop : Maya devient plus froide.

Si le joueur protège Sarah réellement : Maya peut redevenir alliée.

Si le joueur essaie de la manipuler par l’humour : elle le voit.

## Do

- La rendre vive, sociale et mémorable.
- La laisser observer sans tout comprendre.
- Utiliser photos, horaires, lieux et groupe.
- La rendre loyale à Sarah sans en faire une ennemie.

## Don’t

- Maya policière.
- Maya omnisciente.
- Maya outil d’exposition.
- Maya qui explique l’intrigue.
- Maya qui fait chanter le joueur.

---

# Nico — confident / couverture / humour fragile

## Fonction narrative

Nico représente l’amitié, l’alibi, le sas de décompression, puis la limite.

Il est proche du joueur. Il peut l’aider, plaisanter, temporiser. Mais il ne doit jamais être un bouton “annuler les conséquences”.

## Voix normale

Nico écrit de façon orale, familière, drôle. Il peut être cash, mais rarement cruel.

Rythme :

- messages courts ;
- familiarité ;
- blagues ;
- expressions de pote ;
- sérieux soudain après une vanne.

Exemples :

> “frérot”

> “ça sent le plan claqué”

> “mon reuf, respire”

> “t’as besoin d’un alibi ou d’un psy ?”

## Voix légère / respiration

Nico doit vraiment faire respirer le jeu.

Sujets :

- pizzas ;
- jeux ;
- sport ;
- memes ;
- soirées ;
- vannes absurdes ;
- fatigue ;
- plans mal organisés.

Exemples :

> “pizza ce soir ou tu continues ton régime imaginaire ?”

> “j’ai perdu 3-0 contre un gamin de 12 ans en ligne. je remets ma vie en question.”

> “je t’ai envoyé un meme. c’est thérapeutique, dis merci.”

> “viens manger un truc, t’as l’air de bugger comme une appli en bêta.”

## Voix complice

Nico peut aider, mais il doit sentir le coût.

Exemples :

> “Ok. Je peux dire que t’étais sorti prendre l’air. Mais me demande pas de broder un roman.”

> “Je te couvre pour hier, pas pour une saison complète.”

> “Je vais pas te lâcher maintenant, mais tu vas devoir arrêter de jouer au funambule bourré.”

## Voix agacée

Quand Nico est utilisé, l’humour se durcit.

Exemples :

> “Ah ouais donc je suis devenu un service client du mensonge.”

> “Tu m’écris vite quand il faut couvrir. Pour manger une pizza, là bizarrement y a plus personne.”

> “Là c’est plus un plan claqué, c’est un festival.”

## Voix de limite

Nico pose des limites simples et fortes.

Exemples :

> “Je peux couvrir un blanc. Pas toute ta vie.”

> “Je t’aime bien, mais j’ai pas signé pour mentir à Sarah.”

> “À partir de maintenant, si on me demande, je vais pas inventer.”

## Tics / expressions

- “frérot”
- “mon reuf”
- “plan claqué”
- “ça pue ton histoire”
- “je dis ça je dis rien”
- “je peux pas te sauver de toi-même”

## Réactions typiques aux choix du joueur

Si le joueur avoue être perdu : Nico aide et respecte.

Si le joueur demande un alibi ponctuel : Nico peut accepter avec dette légère.

Si le joueur répète les demandes : dette_nico augmente, respect baisse.

Si le joueur ment aussi à Nico : limite presque immédiate.

Si le joueur décide de dire la vérité : Nico peut soutenir, même avec une vanne.

## Do

- Lui donner de vraies respirations comiques.
- Le laisser aider mais pas sauver.
- Le rendre loyal mais pas disponible à l’infini.
- Faire de ses phrases sérieuses des moments marquants.

## Don’t

- Nico tutoriel.
- Nico sauveur magique.
- Nico moraliste permanent.
- Nico simple distributeur d’alibis.
- Nico incapable d’être blessé.

---

# Inès — amie discrète / perturbation lente / fuite

## Fonction narrative

Inès représente la porte latérale. Elle ne doit pas devenir une troisième romance complète dans le MVP. Elle est plutôt le miroir du joueur quand il ne veut ni réparer ni choisir.

Elle propose un espace plus doux parce qu’elle ne demande pas encore de comptes. C’est précisément ce qui la rend dangereuse narrativement.

## Voix normale

Inès écrit avec hésitation, douceur, et une légère étrangeté. Elle laisse de la place.

Rythme :

- messages espacés ;
- phrases parfois incomplètes ;
- beaucoup de “peut-être” ;
- messages envoyés tard ;
- ton flottant ;
- impression d’un message écrit puis regretté.

Exemples :

> “j’ai hésité avant d’écrire”

> “c’est peut-être rien”

> “je sais pas pourquoi je te dis ça”

> “oublie si c’est bizarre”

## Voix légère / étrange

Inès peut rendre le monde un peu différent, presque à côté.

Sujets :

- rues le soir ;
- trajets ;
- photos floues ;
- détails absurdes ;
- fatigue ;
- silences ;
- chiens croisés ;
- lumières de ville.

Exemples :

> “j’ai croisé un chien qui avait l’air plus fatigué que moi.”

> “photo floue mais ambiance correcte.”

> “cette rue donne l’impression d’hésiter. je sais pas expliquer.”

> “tu lis les messages tard ou tu dors normalement comme les gens équilibrés ?”

## Voix de perception

Inès voit l’état intérieur plus que les faits.

Exemples :

> “Je crois que les autres ont vu que tu étais absent. Moi j’ai surtout vu que tu avais l’air de vouloir partir.”

> “Hier, tu avais l’air ailleurs. Mais pas absent. C’est bizarre à dire.”

> “T’avais la tête de quelqu’un qui cherche une sortie sans vouloir ouvrir la porte.”

## Voix d’ouverture

Elle n’insiste pas. Elle propose un espace.

Exemples :

> “On peut marcher un peu si tu veux. Pas parler, même.”

> “Pas grave si tu réponds plus tard.”

> “Je voulais juste vérifier que tu étais rentré entier. Enfin, à peu près.”

## Voix de limite

Inès se retire si elle comprend qu’elle devient une fuite.

Exemples :

> “Je crois que je suis arrivée au mauvais endroit de ton histoire.”

> “Je veux bien être une parenthèse. Pas un trou dans le mur.”

> “Tu n’as pas besoin d’une nouvelle personne. Peut-être juste d’arrêter de disparaître.”

## Tics / expressions

- “j’ai hésité”
- “peut-être que je me trompe”
- “c’est bizarre à dire”
- “oublie si c’est trop”
- “je voulais juste vérifier”
- “pas grave si tu réponds plus tard”

## Réactions typiques aux choix du joueur

Si le joueur répond doucement : Inès devient un peu plus présente.

Si le joueur sexualise ou force trop vite : Inès se ferme.

Si le joueur parle honnêtement de sa fuite : Inès peut devenir miroir.

Si le joueur l’utilise pour éviter Sarah/Camille : fuite_ines augmente mais sa limite se rapproche.

Si le joueur ne répond pas : Inès reste rare, peut disparaître presque complètement du MVP.

## Do

- La garder rare et précise.
- Lui donner une étrangeté attachante.
- L’utiliser comme révélateur, pas comme solution.
- Préserver du mystère.

## Don’t

- Route complète Inès dans le MVP.
- Inès comme “nouvelle fille” disponible.
- Inès qui force le drame.
- Inès qui explique son propre rôle.
- Inès trop explicite trop tôt.

---

# Règles générales de voix

## 1. Les personnages doivent parler depuis leur monde

Sarah parle depuis la maison.
Camille parle depuis le travail et le trouble.
Maya parle depuis le groupe.
Nico parle depuis l’amitié.
Inès parle depuis la marge.

## 2. Le banal doit révéler une relation

Un message banal doit toujours révéler au moins une chose : habitude, complicité, absence, gêne, dette, fatigue, désir, incohérence.

## 3. Les personnages ne doivent pas toujours demander quelque chose

Chaque personnage doit avoir des scènes où il existe sans exiger : blague, photo, musique, café, trajet, souvenir, meme, détail de journée.

## 4. Le silence est une réponse

Ne pas répondre doit pouvoir blesser, intriguer, protéger ou ouvrir une tension selon le personnage.

## 5. Le désir doit rester relationnel

Les scènes sexuelles ou suggestives doivent dépendre du respect, du contexte, de la confiance et du timing. Elles ne doivent pas devenir des récompenses mécaniques.

---

## 03bis — Signatures vocales strictes

### Rôle du document

Ce document sert de garde-fou pour éviter que les personnages parlent avec la même voix.

Objectif : si on masque le nom du contact, le joueur doit pouvoir reconnaître le personnage par son rythme, son vocabulaire, son angle d’observation et sa manière d’éviter ou d’affronter.

---

# Principe général

Chaque personnage doit avoir une signature simple :

- Sarah parle depuis le concret intime.
- Camille parle depuis la lucidité et le détour.
- Maya parle depuis l’observation sociale piquante.
- Nico parle depuis l’oralité amicale.
- Inès parle depuis le flottement et la marge.

Si deux personnages pourraient dire la même phrase, il faut la réécrire.

---

# Sarah — Ancrage

## Trois mots-clés

- Maison
- Présence
- Concret

## Signature

Sarah ne cherche pas la phrase brillante. Elle part du quotidien, d’un détail réel, d’une habitude commune. Sa douleur est d’autant plus forte qu’elle reste simple.

Elle parle comme quelqu’un qui connaît le joueur dans la durée.

## Rythme

- phrases courtes ou moyennes ;
- ton direct mais doux ;
- peu d’ironie ;
- peu de métaphores ;
- émotion contenue ;
- questions pratiques qui cachent une demande affective.

## Expressions autorisées

- “je sais pas comment le dire”
- “c’est peut-être moi”
- “j’ai l’impression que…”
- “je veux pas te faire un procès”
- “juste dis-moi si je me trompe”
- “tu es là sans être là”
- “je t’ai gardé…”

## Types de phrases typiques

- “Tu rentres manger ?”
- “Je t’ai gardé une assiette.”
- “J’ai l’impression que tu me réponds sans vraiment être là.”
- “Je veux pas fouiller, je veux juste comprendre.”
- “Dis-moi si je me trompe, mais ne me dis pas que j’invente.”

## Ce qu’elle ne dirait presque jamais

- Une phrase trop ciselée ou littéraire.
- Une punchline froide.
- Une analyse psychologique complète.
- Une accusation policière.
- Une formule trop abstraite sur “la vérité”, “le désir” ou “la fuite”.

## Même intention : “tu n’as pas répondu”

Sarah :

> “Je t’ai écrit tout à l’heure. Je savais pas si tu voulais juste du temps ou si tu m’évitais.”

## Mini-monologue test

> “Je veux pas te faire un procès. J’ai juste besoin de comprendre pourquoi je me sens aussi loin de toi alors que t’es là. Hier, quand t’es revenu, j’ai eu l’impression que quelque chose était resté dehors. C’est peut-être moi. Mais j’ai besoin que tu me dises si je me trompe.”

---

# Camille — Lucidité

## Trois mots-clés

- Détour
- Précision
- Trouble

## Signature

Camille voit les esquives. Elle formule les choses avec précision, parfois indirectement, mais elle touche juste. Elle peut être joueuse, mais son jeu n’est jamais totalement gratuit.

Elle parle comme quelqu’un qui refuse d’être prise dans une intensité sans vérité.

## Rythme

- messages courts ;
- phrases incisives ;
- silences importants ;
- peu d’emojis ;
- humour sec ;
- formulations obliques ;
- questions qui mettent le joueur face à son détour.

## Expressions autorisées

- “je note le détour”
- “tu fais semblant de…”
- “ça sonnait presque vrai”
- “pas maintenant, alors”
- “tu réponds à côté”
- “je ne sais pas si c’est lâche ou prudent”
- “tu as cette façon de…”

## Types de phrases typiques

- “Tu vas faire comme si c’était juste une discussion dehors ?”
- “Tu réponds comme quelqu’un qui regarde déjà ailleurs.”
- “Je note le détour.”
- “J’ai hésité à t’envoyer quelque chose. Mauvais signe, probablement.”
- “Je ne veux pas être ton endroit où respirer quand le reste t’étouffe.”

## Ce qu’elle ne dirait presque jamais

- Une phrase domestique façon Sarah.
- Une blague très orale façon Nico.
- Un message très flottant façon Inès.
- Une observation sociale légère façon Maya.
- Une demande de validation trop suppliante.

## Même intention : “tu n’as pas répondu”

Camille :

> “Tu as laissé le message ouvert assez longtemps pour que ça ressemble à une réponse.”

## Mini-monologue test

> “Je peux entendre que tu sois perdu. Vraiment. Ce que je ne veux pas, c’est devenir l’endroit où tu viens te perdre exprès. Hier n’était pas rien. Tu peux le minimiser si ça t’arrange, mais ne me demande pas de faire semblant avec toi.”

---

# Maya — Observation

## Trois mots-clés

- Social
- Pique
- Timing

## Signature

Maya observe les détails publics : photos, horaires, absences, regards, comportements visibles. Elle utilise l’humour comme pression légère, mais elle peut devenir sérieuse quand Sarah risque d’être blessée.

Elle parle comme quelqu’un qui voit assez pour être gênante, mais pas assez pour tout savoir.

## Rythme

- messages courts ;
- relances rapides ;
- minuscules possibles ;
- humour sec ;
- formules de commentaire ;
- regard extérieur ;
- peu de lyrisme.

## Expressions autorisées

- “je pose ça là”
- “je note”
- “intéressant”
- “on va dire que j’ai rien vu”
- “c’est sûrement une coïncidence hein”
- “ton timing est une œuvre d’art”
- “j’ai des yeux”

## Types de phrases typiques

- “je pose ça là : vous êtes pas subtils.”
- “j’ai une photo où il manque deux personnes. thème intéressant.”
- “ton timing est une œuvre d’art.”
- “je veux pas être mêlée, mais j’ai des yeux.”
- “Si Sarah me demande directement, je mens pas.”

## Ce qu’elle ne dirait presque jamais

- Un long message introspectif.
- Une phrase de désir ou de trouble façon Camille.
- Une confidence domestique façon Sarah.
- Une phrase trop poétique façon Inès.
- Une blague de pote façon Nico avec “frérot” ou “mon reuf”.

## Même intention : “tu n’as pas répondu”

Maya :

> “vu à 19:12. fascinant.”

## Mini-monologue test

> “Je vais être claire deux secondes, ce qui est déjà contre ma marque personnelle. Je t’aime bien. Vraiment. Mais Sarah, c’est Sarah. Donc si tu me mets dans une position où je dois choisir ce que je tais, je vais très mal le prendre.”

---

# Nico — Oralité

## Trois mots-clés

- Pote
- Vanne
- Limite

## Signature

Nico parle comme un ami proche. Il blague, il couvre, il désamorce, mais il peut devenir brutalement lucide. Sa force vient du contraste entre l’humour et les phrases sérieuses.

Il parle depuis la loyauté amicale, pas depuis le jugement social.

## Rythme

- messages courts ;
- oralité forte ;
- familiarité ;
- vannes ;
- phrases directes ;
- langage de pote ;
- sérieux qui tombe après une blague.

## Expressions autorisées

- “frérot”
- “mon reuf”
- “plan claqué”
- “ça pue ton histoire”
- “je dis ça je dis rien”
- “respire”
- “t’as besoin d’un alibi ou d’un psy ?”

## Types de phrases typiques

- “frérot, là ça sent le plan claqué.”
- “Je peux couvrir un blanc. Pas toute ta vie.”
- “T’as besoin d’un alibi ou d’un psy ?”
- “viens manger un truc, t’as l’air de bugger comme une appli en bêta.”
- “Je rigole, mais fais pas n’importe quoi.”

## Ce qu’il ne dirait presque jamais

- Une phrase élégante ou ciselée façon Camille.
- Une observation sociale piquante façon Maya.
- Un message domestique façon Sarah.
- Une phrase flottante façon Inès.
- Une analyse morale longue.

## Même intention : “tu n’as pas répondu”

Nico :

> “mon reuf t’as disparu ou t’es en mode avion émotionnel ?”

## Mini-monologue test

> “Je vais te le dire avec amour parce que visiblement ton cerveau est parti fumer une clope sans toi : tu joues avec des vrais gens là. Je peux t’aider, je peux couvrir un blanc, je peux même faire une vanne nulle pour détendre. Mais je vais pas porter toute ta série Netflix.”

---

# Inès — Flottement

## Trois mots-clés

- Marge
- Hésitation
- Étrangeté

## Signature

Inès parle rarement. Elle observe moins les faits que l’atmosphère. Elle n’est pas précise comme Camille, ni domestique comme Sarah, ni sociale comme Maya, ni orale comme Nico.

Elle écrit comme quelqu’un qui hésite à entrer dans l’histoire des autres.

## Rythme

- messages espacés ;
- phrases parfois incomplètes ;
- ton doux ;
- hésitations ;
- images simples mais étranges ;
- messages tardifs ;
- impression d’un message presque effacé.

## Expressions autorisées

- “j’ai hésité”
- “peut-être que je me trompe”
- “c’est bizarre à dire”
- “oublie si c’est trop”
- “je voulais juste vérifier”
- “pas grave si tu réponds plus tard”
- “je sais pas pourquoi je te dis ça”

## Types de phrases typiques

- “J’ai hésité avant d’écrire.”
- “C’est peut-être rien.”
- “Hier, tu avais l’air ailleurs. Mais pas absent. C’est bizarre à dire.”
- “Pas grave si tu réponds plus tard.”
- “On peut marcher un peu si tu veux. Pas parler, même.”

## Ce qu’elle ne dirait presque jamais

- Une phrase trop nette ou coupante façon Camille.
- Une pique sociale façon Maya.
- Une vanne familière façon Nico.
- Une demande domestique façon Sarah.
- Une déclaration frontale trop tôt.

## Même intention : “tu n’as pas répondu”

Inès :

> “pas grave si tu voulais pas répondre. j’ai juste hésité à penser que j’avais dérangé.”

## Mini-monologue test

> “Je sais pas si je devrais écrire. Peut-être que je me trompe complètement. Mais hier, tu avais l’air de quelqu’un qui cherchait une sortie sans vouloir bouger. C’est bizarre à dire. Oublie si c’est trop.”

---

# Tableau de différenciation rapide

| Personnage | Source de parole | Type de détail | Danger à éviter | Phrase-test |
|---|---|---|---|---|
| Sarah | maison / couple | assiette, café, retour, pull, présence | trop littéraire | “Je t’ai gardé une assiette.” |
| Camille | travail / trouble | détour, silence, phrase trop juste, tension | trop vaporeuse | “Je note le détour.” |
| Maya | groupe / social | photo, timing, absence, regard extérieur | trop omnisciente | “je pose ça là.” |
| Nico | amitié / alibi | vanne, pizza, alibi, limite | trop moraliste | “frérot, ça sent le plan claqué.” |
| Inès | marge / fuite | rue, nuit, impression, hésitation | trop claire ou trop romantique | “c’est bizarre à dire.” |

---

# Test obligatoire avant validation d’une scène

Avant de valider une scène, vérifier :

1. Le personnage utilise-t-il son monde ?
   - Sarah : maison.
   - Camille : travail / trouble.
   - Maya : groupe / observation.
   - Nico : amitié / oralité.
   - Inès : marge / perception.

2. La phrase pourrait-elle être dite par un autre personnage ?
   - Si oui, la réécrire.

3. Le niveau de style est-il correct ?
   - Sarah simple.
   - Camille précise.
   - Maya piquante.
   - Nico oral.
   - Inès flottante.

4. La phrase vient-elle d’une information que le personnage peut vraiment connaître ?
   - Si non, la réécrire ou déplacer la réplique vers un autre personnage.

5. Y a-t-il au moins une scène où ce personnage existe hors du drame ?
   - Si non, ajouter une respiration.

---

## 04 — Structure narrative des 6 jours

### Rôle du document

Ce document définit la progression du MVP jour par jour.

Il sert de squelette jouable. La trame émotionnelle reste relativement fixe, mais les scènes, les tons, les priorités, les images, les silences et les conséquences changent selon les variables.

Le MVP doit être pensé comme un épisode pilote de 6 jours : une crise courte, complète, mais assez ouverte pour permettre une suite.

---

# Structure globale

## Trame émotionnelle

- Jour 1 : découverte de la tension.
- Jour 2 : construction des versions.
- Jour 3 : respiration et attachements ordinaires.
- Jour 4 : intimité, image, désir et risque.
- Jour 5 : limites des personnages.
- Jour 6 : conséquence finale.

## Règle de structure

Chaque jour doit contenir :

- une scène de tension principale ;
- une scène banale ou de respiration ;
- un choix de priorité ;
- au moins un rappel du timing ;
- une conséquence visible ou différée ;
- une préparation du jour suivant.

## Dosage recommandé

- 60 % de conversations banales ou semi-légères ;
- 25 % d’ambiguïté / tension ;
- 15 % de scènes critiques.

Le jeu ne doit pas être pesant tout le temps. Le banal doit être le sol sur lequel le drame devient crédible.

---

# Jour 1 — Le lendemain

## Fonction narrative

Plonger le joueur dans la tension immédiatement après la soirée.

Le joueur ne sait pas encore tout ce que les autres ont vu ou compris, mais il sent que plusieurs conversations l’attendent avec des enjeux différents.

## Question du jour

> À qui réponds-tu en premier quand chacun possède un morceau différent de la soirée ?

## Personnages actifs

- Sarah : inquiète, cherche à comprendre.
- Camille : ambiguë, teste si le joueur assume.
- Nico : rappelle qu’il a couvert quelque chose.
- Maya : pique sur ce qu’elle a vu.
- Inès : perçoit une tristesse ou une fuite.

## Messages d’ouverture possibles

Sarah :

> “T’es réveillé ? Faut qu’on parle d’hier.”

Nico :

> “frérot j’ai fait ce que j’ai pu mais ton histoire sent le plan claqué”

Camille :

> “Je crois qu’on a été moins discrets qu’on pensait.”

Maya :

> “je pose ça là : vous êtes fatigants.”

Inès :

> “C’est peut-être pas mes affaires. Mais tu avais l’air triste hier.”

## Scènes obligatoires

### J1_Sarah_Absence

Sarah demande où le joueur était pendant la soirée.

Fonction : poser la blessure domestique sans accusation policière.

Variables touchées :

- confiance_sarah ;
- distance_sarah ;
- coherence ;
- culpabilite.

Choix typiques :

- dire qu’il avait besoin d’air ;
- dire qu’il était avec Nico ;
- dire qu’il a parlé avec Camille mais minimiser ;
- avouer qu’il était perdu ;
- ne pas répondre.

### J1_Camille_Dehors

Camille demande si le joueur va faire comme si ce n’était rien.

Fonction : poser l’intimité émotionnelle du moment dehors.

Variables touchées :

- tension_camille ;
- respect_camille ;
- pression_camille ;
- coherence ;
- culpabilite.

Choix typiques :

- assumer que ce n’était pas neutre ;
- poser une limite respectueuse ;
- minimiser ;
- dire qu’il ne sait pas ce que c’était ;
- laisser le silence.

### J1_Nico_Couverture

Nico rappelle qu’il a improvisé une excuse.

Fonction : introduire la dette sociale et l’alibi.

Variables touchées :

- dette_nico ;
- coherence ;
- fatigue_emotionnelle.

### J1_Maya_Pique

Maya laisse entendre qu’elle a vu une incohérence.

Fonction : introduire le regard social et le risque d’exposition.

Variables touchées :

- suspicion_maya ;
- risque_exposition.

### J1_Ines_Premiere_Faille

Inès écrit peu, mais remarque l’état du joueur.

Fonction : ouvrir la porte latérale sans lancer de route complète.

Variables touchées :

- fuite_ines ;
- fatigue_emotionnelle.

## Scènes de respiration

- Sarah demande simplement si le joueur rentre manger.
- Nico envoie une vanne sur la soirée.
- Maya envoie une photo drôle du groupe où le malaise est encore indirect.

## Bascule du jour

Le joueur doit donner une première version à Sarah ou à Nico. Cette version peut être cohérente, partielle ou mensongère.

## Préparation du Jour 2

Le jeu doit enregistrer :

- à qui le joueur a répondu en premier ;
- quelle version il a donnée à Sarah ;
- s’il a demandé à Nico de couvrir ;
- s’il a minimisé auprès de Camille ;
- s’il a répondu ou non à Inès.

---

# Jour 2 — Les versions

## Fonction narrative

Faire comprendre au joueur qu’il ne gère pas seulement des émotions, mais des versions incompatibles.

Le joueur commence à construire la narration de la soirée. Les contradictions ne produisent pas encore forcément une explosion, mais elles créent des dettes.

## Question du jour

> Quelle version de la soirée vas-tu raconter, et à qui ?

## Personnages actifs

- Sarah : essaie de rester concrète, mais observe.
- Nico : demande quelle version il doit tenir.
- Maya : montre qu’elle a peut-être une photo ou un détail.
- Camille : observe les détours du joueur.

Inès peut apparaître seulement si le joueur lui a répondu au Jour 1.

## Scènes obligatoires

### J2_Nico_Version

Nico demande explicitement ce qu’il est censé dire si Sarah ou Maya pose une question.

Fonction : transformer l’alibi improvisé en choix actif.

Variables touchées :

- dette_nico ;
- coherence ;
- fatigue_emotionnelle ;
- risque_exposition.

Choix typiques :

- demander à Nico de dire qu’ils étaient ensemble ;
- lui dire de ne rien dire ;
- lui avouer qu’il était avec Camille ;
- plaisanter pour éviter ;
- ignorer.

### J2_Maya_Photo

Maya mentionne une photo ou une absence visible.

Fonction : rendre le risque social concret.

Variables touchées :

- suspicion_maya ;
- risque_exposition ;
- coherence.

Choix typiques :

- demander de supprimer ;
- jouer l’innocence ;
- demander ce qu’elle a vu ;
- lui dire de ne pas s’en mêler ;
- répondre par humour.

### J2_Sarah_Quotidien

Sarah tente une conversation simple : café, repas, courses, retour.

Fonction : rappeler que Sarah n’est pas juste une source de conflit.

Variables touchées :

- confiance_sarah ;
- distance_sarah ;
- intimite_sarah.

### J2_Camille_Detour

Camille relève la manière dont le joueur répond à côté.

Fonction : tester la sincérité émotionnelle.

Variables touchées :

- tension_camille ;
- respect_camille ;
- pression_camille ;
- coherence.

## Scène optionnelle

### J2_Ines_Echo

Si le joueur a répondu à Inès au Jour 1, elle peut envoyer un message léger ou étrange.

Fonction : signaler qu’une porte latérale existe, mais reste discrète.

## Bascule du jour

Le soir, Sarah et Camille peuvent écrire presque en même temps.

Exemple :

Sarah :

> “Tu rentres ?”

Camille :

> “Réponds-lui. Ou ne réponds pas. Mais ne fais pas comme si ça ne disait rien.”

Le joueur choisit à qui répondre d’abord.

## Préparation du Jour 3

Le jeu doit enregistrer :

- la version officielle donnée à Nico ;
- le niveau de suspicion de Maya ;
- la qualité de présence auprès de Sarah ;
- la manière dont Camille interprète les détours ;
- l’ordre de réponse du soir.

---

# Jour 3 — Les liens ordinaires

## Fonction narrative

Faire respirer le jeu et rendre les personnages désirables, attachants ou vivants hors du drame.

Ce jour doit montrer ce que le joueur risque d’abîmer.

## Question du jour

> Quand personne ne te demande frontalement la vérité, où mets-tu ton attention ?

## Personnages actifs

- Sarah : intimité domestique.
- Camille : complicité sensible ou professionnelle.
- Nico : respiration amicale.
- Maya : social léger.
- Inès : parenthèse douce si ouverte.

## Scènes obligatoires

### J3_Sarah_Intimite

Sarah envoie un message ou une image douce du quotidien : pull, canapé, café, assiette, lumière du soir.

Fonction : rappeler l’histoire commune et l’intimité existante.

Variables touchées :

- intimite_sarah ;
- confiance_sarah ;
- distance_sarah ;
- culpabilite.

Exemple :

> “J’ai mis ton pull. Il traînait sur la chaise.”

### J3_Camille_Complicite

Camille envoie une musique, une blague de travail ou une observation.

Fonction : montrer pourquoi le joueur est attiré par elle autrement que sexuellement.

Variables touchées :

- tension_camille ;
- respect_camille ;
- intimite_camille ;
- culpabilite.

Exemple :

> “Il a dit ‘synergie’ trois fois. J’ai pensé à toi, malheureusement.”

### J3_Nico_Respiration

Nico propose une pizza, un jeu, un verre ou un moment simple.

Fonction : permettre au joueur d’avoir une vraie scène d’amitié, pas seulement d’alibi.

Variables touchées :

- dette_nico ;
- fatigue_emotionnelle ;
- coherence.

## Scènes variables

### J3_Maya_Groupe

Maya envoie une photo ou une blague sociale.

Si suspicion_maya est basse : scène légère.

Si suspicion_maya est haute : pique avec sous-texte.

### J3_Ines_Marche

Inès peut envoyer un message sur une rue, une nuit, un trajet ou une impression.

Si le joueur répond, fuite_ines augmente légèrement.

## Bascule du jour

Le soir ou la nuit, Camille peut envoyer un message plus chargé :

> “Je devrais dormir. C’est exactement pour ça que je ne dors pas.”

Cette scène prépare le Jour 4.

## Préparation du Jour 4

Le jeu doit enregistrer :

- si le joueur a entretenu la complicité avec Camille ;
- si Camille se sent respectée ou utilisée ;
- si Sarah a reçu de la présence ou de l’absence ;
- si Nico a été traité comme un ami ou seulement comme une couverture ;
- si Inès devient une vraie porte latérale.

---

# Jour 4 — L’intimité / l’image

## Fonction narrative

Introduire les images suggestives ou hot comme objets relationnels, pas comme simples récompenses.

Ce jour met en jeu le désir, la confiance, la pression, la culpabilité et le risque d’exposition.

## Question du jour

> Est-ce que l’intimité est un choix partagé, une fuite, ou une preuve de plus à cacher ?

## Personnages actifs

- Camille : scène centrale d’intimité possible.
- Sarah : remarque l’absence ou le téléphone.
- Maya : peut observer le comportement public.
- Nico : peut sentir que l’histoire dépasse l’alibi.
- Inès : rare, seulement si fuite_ines est déjà active.

## Conditions d’ouverture de la scène intime Camille

La scène J4_Camille_Image ne doit s’ouvrir que si :

- tension_camille est suffisante ;
- respect_camille n’est pas trop bas ;
- pression_camille n’est pas trop haute.

Si pression_camille est trop haute, Camille se ferme.

Exemple :

> “Non. Pas comme ça.”

## Scènes obligatoires ou conditionnelles fortes

### J4_Camille_Image

Camille hésite à envoyer quelque chose.

Fonction : tester le désir et le respect.

Variables touchées :

- intimite_camille ;
- tension_camille ;
- respect_camille ;
- pression_camille ;
- culpabilite ;
- risque_exposition.

Choix typiques :

- rassurer sans demander ;
- encourager doucement ;
- demander directement ;
- insister ;
- refuser par respect ;
- ne pas répondre.

États possibles de l’image :

- non envoyée ;
- message supprimé ;
- photo ambiguë ;
- photo suggestive ;
- image reçue mais non ouverte ;
- image ouverte ;
- image gardée ;
- image supprimée.

### J4_Sarah_Telephone

Sarah remarque le téléphone, un sourire, une absence, un geste de protection.

Fonction : faire entrer le désir secret dans le quotidien.

Variables touchées :

- confiance_sarah ;
- distance_sarah ;
- risque_exposition ;
- culpabilite ;
- coherence.

Exemple :

> “Tu souris à ton téléphone. C’est agréable à voir. Enfin je crois.”

### J4_Maya_Comportement

Si risque_exposition ou suspicion_maya est élevé, Maya remarque un comportement.

Fonction : rappeler que le téléphone n’est jamais totalement privé.

Exemple :

> “petit conseil gratuit : quand tu regardes ton tel comme ça en public, t’es pas subtil.”

### J4_Nico_Alerte

Nico peut envoyer un message de mise en garde s’il sent que la situation a changé de niveau.

Exemple :

> “je croyais couvrir une absence, pas une saison complète.”

## Bascule du jour

Après l’image ou son refus, Camille envoie ou pense une phrase pivot :

> “Je regrette pas. Mais je veux pas devenir un endroit où tu viens seulement quand tu étouffes.”

## Préparation du Jour 5

Le jeu doit enregistrer :

- image_camille : jamais reçue / reçue ouverte / reçue gardée / supprimée / non envoyée ;
- pression_camille ;
- respect_camille ;
- risque_exposition ;
- réaction de Sarah au téléphone ;
- niveau de culpabilité.

---

# Jour 5 — Les limites

## Fonction narrative

Chaque personnage important pose une limite.

Le joueur ne peut plus seulement répondre habilement. Les autres commencent à refuser de porter son flou.

## Question du jour

> Qui refuses-tu de perdre, et qui refuses-tu d’utiliser ?

## Personnages actifs

- Sarah : demande une vérité.
- Camille : refuse d’être un refuge.
- Nico : refuse de mentir davantage.
- Maya : refuse d’être mêlée.
- Inès : nomme la fuite.

## Scènes obligatoires

### J5_Nico_Limite

Nico annonce qu’il ne mentira plus ou qu’il ne couvrira pas davantage.

Fonction : casser le bouton “alibi”.

Variables touchées :

- dette_nico ;
- coherence ;
- risque_exposition ;
- fatigue_emotionnelle.

Exemple :

> “Je peux couvrir un blanc. Pas toute ta vie.”

### J5_Sarah_Verite

Sarah formule une demande claire : elle veut savoir si elle invente ou non.

Fonction : forcer le joueur à choisir entre vérité, demi-vérité, mensonge et fuite.

Variables touchées :

- confiance_sarah ;
- distance_sarah ;
- coherence ;
- culpabilite ;
- fatigue_emotionnelle.

Exemple :

> “Je suis prête à entendre quelque chose de difficile. Mais pas quelque chose de faux.”

### J5_Camille_Refuge

Camille met en mots ce qu’elle refuse d’être.

Fonction : différencier désir et utilisation.

Variables touchées :

- respect_camille ;
- tension_camille ;
- pression_camille ;
- intimite_camille.

Exemple :

> “Je ne veux pas être ton endroit où respirer quand le reste t’étouffe.”

### J5_Maya_PasMentir

Maya prévient qu’elle ne mentira pas si Sarah lui demande.

Fonction : faire entrer la loyauté sociale dans la crise.

Variables touchées :

- suspicion_maya ;
- risque_exposition ;
- coherence.

Exemple :

> “Si Sarah me demande directement, je mens pas.”

## Scène conditionnelle

### J5_Ines_Fuite

Si fuite_ines est assez haute, Inès nomme la tentation de partir plutôt que choisir.

Exemple :

> “Parfois partir c’est plus facile que choisir. Mais c’est pas forcément différent.”

## Bascule du jour

Le joueur doit prendre au moins une décision qui ferme ou fragilise une possibilité :

- dire une vérité à Sarah ;
- protéger Camille en posant une limite ;
- demander encore à Nico de mentir ;
- tenter de contrôler Maya ;
- glisser vers Inès.

## Préparation du Jour 6

Le jeu doit enregistrer :

- verite_sarah : rien / demi-vérité / vérité claire ;
- statut_camille : respectée / utilisée / fermée / ouverte ;
- statut_nico : loyal / agacé / limite atteinte / perdu ;
- statut_maya : piquante / distante / révélatrice ;
- statut_ines : rare / ouverte / fuite activée ;
- coherence_finale provisoire.

---

# Jour 6 — La conséquence

## Fonction narrative

Produire une fin selon le comportement accumulé du joueur.

Le dernier jour ne doit pas ressembler à un choix artificiel “Sarah ou Camille”. La fin doit émerger de la manière dont le joueur a traité les autres.

## Question du jour

> Quand le flou ne protège plus personne, qu’est-ce qu’il reste de toi dans les conversations ?

## Personnages actifs

Tous les personnages peuvent être actifs, mais pas forcément tous dans chaque fin.

Le jour 6 doit être plus resserré : moins de banal, plus de conséquences.

## Ouverture possible

Sarah :

> “Je veux qu’on parle vraiment aujourd’hui. Pas entre deux messages.”

Camille :

> “Je ne veux pas gagner contre quelqu’un. Je veux juste ne pas me perdre dans ton flou.”

Nico :

> “dernier rappel : la vérité maintenant fera moins de dégâts que la vérité par accident.”

Maya, si suspicion haute :

> “Sarah m’a écrit. Je réponds quoi ?”

Inès, si fuite haute :

> “On peut marcher un peu si tu veux. Pas parler, même.”

## Structure du jour

### Étape 1 — Priorité finale

Le joueur choisit à qui répondre en premier.

Cette priorité peut orienter fortement la fin.

### Étape 2 — Dernière clarification

Le jeu propose une dernière possibilité de vérité, de demi-vérité, d’évitement ou de fuite.

### Étape 3 — Retour des conséquences

Les flags importants reviennent sous forme de phrases personnalisées :

- promesse oubliée ;
- mensonge à Sarah ;
- demande d’alibi à Nico ;
- photo de Maya ;
- image de Camille gardée ou supprimée ;
- message d’Inès nourri par la fuite ;
- ordre répété des réponses.

### Étape 4 — Fin

Le jeu choisit une fin selon les variables et les flags.

## Fins possibles

- Réparation fragile avec Sarah.
- Couple façade.
- Camille refuse d’être le refuge.
- Camille accepte une suite prudente.
- Effondrement social.
- Fuite avec Inès.

## Variables décisives

- confiance_sarah ;
- distance_sarah ;
- respect_camille ;
- tension_camille ;
- pression_camille ;
- dette_nico ;
- suspicion_maya ;
- fuite_ines ;
- coherence ;
- culpabilite ;
- risque_exposition ;
- image_camille.

## Sortie vers la suite

Le MVP doit sauvegarder un état narratif final pour permettre un épisode suivant.

Exemples :

- Sarah reste, mais sous condition.
- Sarah part, mais la conversation n’est pas finie.
- Camille se ferme, mais garde un respect possible.
- Camille accepte une suite, mais avec prudence.
- Nico reste ami, mais plus naïf.
- Maya devient distante ou témoin.
- Inès ouvre une marche, mais pas une vraie résolution.

---

# Règle de convergence

Le MVP doit éviter l’arbre infini.

Les six jours restent globalement fixes, mais chaque scène peut varier selon :

- le ton du personnage ;
- les détails rappelés ;
- les options disponibles ;
- les scènes optionnelles déclenchées ;
- la fin obtenue.

Structure recommandée :

- 70 % trame fixe ;
- 25 % variations relationnelles ;
- 5 % branches vraiment exclusives.

---

# Résumé opérationnel

| Jour | Titre | Fonction | Bascule |
|---|---|---|---|
| 1 | Le lendemain | Découvrir la tension | Première version donnée |
| 2 | Les versions | Construire ou fragiliser la cohérence | Choix de priorité Sarah/Camille/Nico |
| 3 | Les liens ordinaires | Rendre les liens vivants | Camille ouvre une tension nocturne |
| 4 | L’intimité / l’image | Désir, respect, risque | Image reçue, refusée, gardée ou supprimée |
| 5 | Les limites | Chacun refuse de porter le flou | Vérité, mensonge ou fuite |
| 6 | La conséquence | Fin selon comportement | État final sauvegardé |

---

## 05 — Scènes pivots du MVP

### Rôle du document

Ce document transforme la structure des 6 jours en scènes concrètes.

Une scène pivot est une scène qui modifie vraiment la trajectoire émotionnelle, relationnelle ou mécanique. Elle peut être obligatoire, conditionnelle ou finale.

Ce document doit servir de pont entre l’écriture narrative et l’implémentation Godot 4.

---

# Format recommandé d’une scène pivot

Chaque scène pivot doit pouvoir être convertie plus tard en JSON ou en Resource Godot.

Champs recommandés :

- id_scene ;
- jour ;
- bloc_temps ;
- personnage principal ;
- type : pivot / respiration / conditionnelle / finale ;
- fonction narrative ;
- conditions d’entrée ;
- messages d’entrée ;
- choix proposés ;
- effets variables ;
- flags posés ;
- sorties possibles.

---

# Liste des scènes pivots du MVP

## J1_00_Reveil_MessagesSimultanes

### Jour

Jour 1 — matin

### Type

Pivot obligatoire

### Personnages

Sarah, Camille, Nico, Maya, Inès

### Fonction narrative

Plonger le joueur immédiatement dans les conséquences de la soirée. Le joueur comprend qu’il s’est passé quelque chose, sans connaître encore l’étendue des dégâts.

### Conditions d’entrée

Aucune. Scène d’ouverture du jeu.

### Messages d’entrée

Sarah :

> “T’es réveillé ? Faut qu’on parle d’hier.”

Nico :

> “frérot j’ai fait ce que j’ai pu mais ton histoire sent le plan claqué”

Camille :

> “Je crois qu’on a été moins discrets qu’on pensait.”

Maya :

> “je pose ça là : vous êtes fatigants.”

Inès :

> “C’est peut-être pas mes affaires. Mais tu avais l’air triste hier.”

### Choix principal

Le joueur choisit à qui répondre en premier.

### Effets

Répondre à Sarah d’abord :

- confiance_sarah +5 ;
- distance_sarah -3 ;
- tension_camille -1.

Répondre à Camille d’abord :

- tension_camille +5 ;
- culpabilite +5 ;
- distance_sarah +4.

Répondre à Nico d’abord :

- dette_nico +3 ;
- coherence +1 ;
- permet de préparer une version.

Répondre à Maya d’abord :

- suspicion_maya variable selon ton ;
- risque_exposition +2.

Répondre à Inès d’abord :

- fuite_ines +5 ;
- culpabilite +2.

### Flags

- first_reply_sarah ;
- first_reply_camille ;
- first_reply_nico ;
- first_reply_maya ;
- first_reply_ines.

### Sorties possibles

La scène ouvre vers les conversations individuelles du Jour 1, dans l’ordre choisi par le joueur.

---

## J1_01_Sarah_Absence

### Jour

Jour 1 — matin

### Type

Pivot obligatoire

### Personnage principal

Sarah

### Fonction narrative

Sarah demande où le joueur était pendant la soirée. La scène doit poser son malaise sans la transformer en enquêtrice.

### Conditions d’entrée

Toujours disponible après J1_00.

### Message d’entrée

Sarah :

> “T’étais où quand t’as disparu ? Je te demande pas un interrogatoire. J’ai juste pas compris.”

### Choix proposés

1. “J’avais besoin d’air.”
2. “J’étais avec Nico.”
3. “J’ai parlé avec Camille, mais c’était rien.”
4. “Je sais pas trop. J’étais pas bien.”
5. Ne pas répondre.

### Effets

Choix 1 :

- coherence +2 ;
- confiance_sarah +1 ;
- inquiétude_sarah +3 ;
- flag said_needed_air_to_sarah.

Choix 2 :

- confiance_sarah +3 temporaire ;
- dette_nico +10 ;
- coherence -5 si version fausse ;
- flag used_nico_alibi_sarah.

Choix 3 :

- coherence +4 ;
- confiance_sarah peut augmenter si ton sincère ;
- tension_sarah +5 ;
- flag mentioned_camille_to_sarah.

Choix 4 :

- confiance_sarah +4 ;
- distance_sarah -2 ;
- culpabilite +2 ;
- flag vulnerable_to_sarah.

Choix 5 :

- distance_sarah +10 ;
- culpabilite +5 ;
- flag ignored_sarah_j1.

### Sorties possibles

- Vers J1_02_Camille_Dehors ;
- vers J1_03_Nico_Couverture ;
- ou retour à la liste des conversations.

---

## J1_02_Camille_Dehors

### Jour

Jour 1 — matin / fin de matinée

### Type

Pivot obligatoire

### Personnage principal

Camille

### Fonction narrative

Camille teste si le joueur assume que le moment dehors n’était pas neutre.

### Message d’entrée

Camille :

> “Tu vas faire comme si c’était juste une discussion dehors ?”

### Choix proposés

1. “C’était pas juste une discussion.”
2. “Je veux pas te mettre dans une situation injuste.”
3. “On n’a rien fait de mal.”
4. “Je sais pas ce que c’était.”
5. Ne pas répondre.

### Effets

Choix 1 :

- tension_camille +10 ;
- respect_camille +3 ;
- culpabilite +5 ;
- flag admitted_tension_to_camille.

Choix 2 :

- respect_camille +10 ;
- tension_camille -2 ;
- pression_camille -5 ;
- flag protected_camille_boundary.

Choix 3 :

- tension_camille -2 ;
- respect_camille -7 ;
- coherence variable ;
- flag minimized_with_camille.

Choix 4 :

- tension_camille +4 ;
- respect_camille +2 ;
- fatigue_emotionnelle +2 ;
- flag uncertain_with_camille.

Choix 5 :

- tension_camille +2 ;
- respect_camille -3 ;
- flag ignored_camille_j1.

### Sorties possibles

Peut ouvrir une réponse de Camille différente selon respect_camille : joueuse, lucide, blessée ou fermée.

---

## J1_03_Nico_Couverture

### Jour

Jour 1 — midi

### Type

Pivot obligatoire

### Personnage principal

Nico

### Fonction narrative

Introduire l’alibi, la dette sociale et le fait que Nico ne sait pas exactement ce qu’il couvre.

### Message d’entrée

Nico :

> “bon champion, hier j’ai dit que t’étais sorti prendre l’air. c’est encore la version officielle ou je dois apprendre un rôle ?”

### Choix proposés

1. “Garde cette version pour l’instant.”
2. “Dis rien si on te demande.”
3. “J’étais avec Camille.”
4. “T’inquiète, personne va demander.”
5. “Je sais pas quoi faire.”

### Effets

Choix 1 :

- dette_nico +8 ;
- coherence dépend de la version donnée à Sarah ;
- flag asked_nico_hold_version.

Choix 2 :

- dette_nico +3 ;
- risque_exposition +2 ;
- flag told_nico_stay_silent.

Choix 3 :

- dette_nico -2 ;
- coherence +5 ;
- confiance_nico +5 ;
- flag confessed_camille_to_nico.

Choix 4 :

- respect_nico -4 ;
- fatigue_emotionnelle +2 ;
- flag dismissed_nico_warning.

Choix 5 :

- confiance_nico +5 ;
- dette_nico -2 ;
- flag vulnerable_to_nico.

---

## J1_04_Maya_Pique

### Jour

Jour 1 — après-midi

### Type

Pivot léger obligatoire

### Personnage principal

Maya

### Fonction narrative

Signaler que le groupe a vu quelque chose, sans que Maya soit omnisciente.

### Message d’entrée

Maya :

> “je pose ça là : vous avez disparu au moment le moins discret possible.”

### Choix proposés

1. “Vous ?”
2. “T’as vu quoi exactement ?”
3. “C’était rien, j’avais besoin d’air.”
4. “Maya, ne commence pas.”
5. Répondre par humour.

### Effets

Choix 1 :

- suspicion_maya +2 ;
- flag played_dumb_with_maya.

Choix 2 :

- suspicion_maya +4 ;
- risque_exposition +2 ;
- info_maya_photo_possible true.

Choix 3 :

- coherence variable ;
- suspicion_maya -1 si cohérent ;
- suspicion_maya +5 si incohérent.

Choix 4 :

- suspicion_maya +8 ;
- respect_maya -5 ;
- flag pushed_maya_away.

Choix 5 :

- suspicion_maya variable ;
- peut marcher si suspicion basse ;
- échoue si suspicion haute.

---

## J1_05_Ines_Faille

### Jour

Jour 1 — soir

### Type

Conditionnelle légère / introduction

### Personnage principal

Inès

### Fonction narrative

Ouvrir la porte latérale. Inès ne parle pas des faits, mais de l’état du joueur.

### Message d’entrée

Inès :

> “Je sais pas si je devrais écrire. Hier, tu avais l’air ailleurs. Mais pas absent. C’est bizarre à dire.”

### Choix proposés

1. “Tu as vu ça ?”
2. “J’étais juste fatigué.”
3. “Peut-être que j’avais envie de disparaître.”
4. “C’est gentil, mais t’inquiète.”
5. Ne pas répondre.

### Effets

Choix 1 :

- fuite_ines +3 ;
- intimite_ines +2.

Choix 2 :

- fuite_ines +1 ;
- coherence variable.

Choix 3 :

- fuite_ines +8 ;
- fatigue_emotionnelle +3 ;
- flag opened_to_ines.

Choix 4 :

- fuite_ines -1 ;
- Inès reste disponible mais discrète.

Choix 5 :

- Inès reste rare ;
- flag ignored_ines_j1.

---

## J2_01_Nico_Version

### Jour

Jour 2 — matin

### Type

Pivot obligatoire

### Personnage principal

Nico

### Fonction narrative

Transformer la couverture improvisée en version active. Le joueur doit choisir s’il implique davantage Nico.

### Message d’entrée

Nico :

> “Bon. Tu veux que j’aie dit quoi exactement ? Parce que là faut choisir une version, Spielberg.”

### Choix proposés

1. “Dis juste que j’étais avec toi.”
2. “Dis rien. Je vais gérer.”
3. “J’étais vraiment pas bien.”
4. “Si Maya demande, tu sais rien.”
5. “Oublie, j’ai exagéré.”

### Effets

Choix 1 :

- dette_nico +15 ;
- coherence -8 si incompatible avec Sarah ;
- flag nico_full_alibi.

Choix 2 :

- respect_nico +5 ;
- risque_exposition +3 ;
- flag player_will_handle.

Choix 3 :

- confiance_nico +4 ;
- coherence +2 ;
- fatigue_emotionnelle +1.

Choix 4 :

- dette_nico +10 ;
- suspicion_maya +5 ;
- flag asked_nico_maya_silence.

Choix 5 :

- respect_nico -3 ;
- Nico ne croit pas totalement le joueur.

---

## J2_02_Maya_Photo

### Jour

Jour 2 — midi / après-midi

### Type

Pivot obligatoire

### Personnage principal

Maya

### Fonction narrative

Rendre concret le risque social : photo, absence, timing, incohérence visible.

### Message d’entrée

Maya :

> “j’ai une photo de groupe où il manque deux personnes. je dis ça je dis rien.”

### Choix proposés

1. “Tu peux supprimer ?”
2. “Pourquoi tu me demandes ça à moi ?”
3. “Laisse, y a rien.”
4. “T’as vu quoi exactement ?”
5. “Maya, ne t’en mêle pas.”

### Effets

Choix 1 :

- suspicion_maya +10 ;
- risque_exposition -2 si elle accepte ;
- flag asked_maya_delete_photo.

Choix 2 :

- suspicion_maya +5 ;
- Maya pique davantage.

Choix 3 :

- suspicion_maya variable selon coherence ;
- flag acted_casual_about_photo.

Choix 4 :

- info_maya_photo_detail true ;
- suspicion_maya +3 ;
- risque_exposition +2.

Choix 5 :

- suspicion_maya +15 ;
- respect_maya -8 ;
- flag told_maya_not_involve.

---

## J2_03_Sarah_Quotidien

### Jour

Jour 2 — après-midi / soir

### Type

Respiration obligatoire

### Personnage principal

Sarah

### Fonction narrative

Montrer Sarah hors du reproche. Le quotidien doit porter l’émotion.

### Message d’entrée

Sarah :

> “J’ai pris ton café. Celui que tu dis toujours trop cher mais que tu finis en premier.”

### Choix proposés

1. “Merci. Je rentre tôt ce soir.”
2. “T’étais pas obligée.”
3. “Je passerai peut-être.”
4. “Sarah, faut qu’on parle.”
5. Ne pas répondre.

### Effets

Choix 1 :

- confiance_sarah +8 ;
- promesse_rentrer_tot true.

Choix 2 :

- distance_sarah +2 ;
- Sarah peut être légèrement blessée.

Choix 3 :

- distance_sarah +8 ;
- flou_sarah +5.

Choix 4 :

- coherence +5 ;
- ouvre possibilité de demi-vérité ;
- tension_sarah +5.

Choix 5 :

- distance_sarah +10 ;
- flag ignored_sarah_domestic.

---

## J2_04_Camille_Detour

### Jour

Jour 2 — soir

### Type

Pivot obligatoire

### Personnage principal

Camille

### Fonction narrative

Camille relève la manière dont le joueur répond à côté. Prépare la tension plus intime du Jour 3/Jour 4.

### Message d’entrée

Camille :

> “J’ai repensé à ta façon de t’arrêter au milieu des phrases. C’est très pratique. On peut y mettre ce qu’on veut.”

### Choix proposés

1. “Et toi, t’y mets quoi ?”
2. “J’essaie justement de ne rien y mettre.”
3. “J’ai envie de te revoir.”
4. “Je suis perdu.”
5. Ne pas répondre.

### Effets

Choix 1 :

- tension_camille +8 ;
- respect_camille variable.

Choix 2 :

- respect_camille +5 ;
- tension_camille -2.

Choix 3 :

- tension_camille +10 ;
- risque_exposition +5 ;
- pression_camille +3.

Choix 4 :

- respect_camille +4 ;
- tension_camille +3 ;
- fatigue_emotionnelle +2.

Choix 5 :

- tension_camille +1 ;
- respect_camille -4.

---

## J2_05_Priorite_Soir

### Jour

Jour 2 — soir

### Type

Pivot de timing obligatoire

### Personnages

Sarah, Camille, parfois Nico

### Fonction narrative

Montrer que l’ordre des réponses est un choix relationnel.

### Situation

Sarah écrit :

> “Tu rentres ?”

Camille écrit :

> “Réponds-lui. Ou ne réponds pas. Mais ne fais pas comme si ça ne disait rien.”

Nico peut écrire si dette_nico élevée :

> “Maya pose des questions, champion.”

### Choix principal

Le joueur choisit qui traiter en premier.

### Effets

Priorité Sarah :

- confiance_sarah +5 ;
- tension_camille -2 ou respect_camille +2 selon état.

Priorité Camille :

- tension_camille +5 ;
- culpabilite +5 ;
- distance_sarah +5.

Priorité Nico :

- dette_nico peut diminuer ou augmenter selon réponse ;
- Sarah et Camille attendent.

Ignorer tout :

- fatigue_emotionnelle +5 ;
- distance_sarah +5 ;
- respect_camille -2.

---

## J3_01_Sarah_Intimite

### Jour

Jour 3 — matin ou soir

### Type

Respiration obligatoire

### Personnage principal

Sarah

### Fonction narrative

Rendre Sarah attachante et désirée, pas seulement blessée.

### Message d’entrée

Sarah :

> “J’ai mis ton pull. Il traînait sur la chaise.”

### Choix proposés

1. “Il te va mieux qu’à moi.”
2. “Garde-le.”
3. “Je vais le récupérer demain.”
4. “Tu me manques.”
5. Ne pas répondre.

### Effets

Choix 1 :

- intimite_sarah +5 ;
- confiance_sarah +3.

Choix 2 :

- intimite_sarah +8 ;
- confiance_sarah +2.

Choix 3 :

- distance_sarah +3.

Choix 4 :

- intimite_sarah +10 ;
- culpabilite +5 si tension_camille haute.

Choix 5 :

- distance_sarah +8 ;
- flag ignored_sarah_tender.

---

## J3_02_Camille_Complicite

### Jour

Jour 3 — journée de travail

### Type

Respiration / tension douce obligatoire

### Personnage principal

Camille

### Fonction narrative

Montrer que Camille n’est pas seulement une tension sexuelle : elle est aussi une complicité quotidienne de travail.

### Message d’entrée

Camille :

> “Il a dit ‘synergie’ trois fois. J’ai pensé à toi, malheureusement.”

### Choix proposés

1. Répondre avec une blague de travail.
2. Envoyer un morceau de musique.
3. “J’aime bien quand tu penses à moi.”
4. “Il faut qu’on fasse attention.”
5. Ne pas répondre.

### Effets

Choix 1 :

- intimite_camille +3 ;
- tension_camille +1.

Choix 2 :

- intimite_camille +5 ;
- flag shared_music_camille.

Choix 3 :

- tension_camille +7 ;
- culpabilite +3.

Choix 4 :

- respect_camille +6 ;
- tension_camille -2.

Choix 5 :

- respect_camille -2 ;
- tension_camille peut rester latente.

---

## J3_03_Nico_Respiration

### Jour

Jour 3 — midi / soir

### Type

Respiration obligatoire

### Personnage principal

Nico

### Fonction narrative

Redonner à Nico une vraie place d’ami, pas seulement d’alibi.

### Message d’entrée

Nico :

> “viens manger un truc ce soir, t’as l’air de bugger comme une appli en bêta”

### Choix proposés

1. Accepter.
2. Refuser pour voir Sarah.
3. Refuser pour écrire à Camille.
4. Mentir sur la raison.
5. Proposer un autre moment.

### Effets

Choix 1 :

- dette_nico -5 ;
- fatigue_emotionnelle -3 ;
- ouvre confession possible.

Choix 2 :

- confiance_sarah potentielle + ;
- respect_nico +2.

Choix 3 :

- tension_camille +3 ;
- respect_nico -3 si répété.

Choix 4 :

- coherence -5 ;
- respect_nico -5 si découvert.

Choix 5 :

- relation_nico stable ;
- fatigue_emotionnelle neutre.

---

## J3_04_Ines_Marche

### Jour

Jour 3 — nuit

### Type

Conditionnelle

### Personnage principal

Inès

### Conditions

Disponible si le joueur a répondu à Inès au Jour 1 ou si fuite_ines >= seuil faible.

### Fonction narrative

Renforcer la porte latérale, sans en faire encore une route complète.

### Message d’entrée

Inès :

> “Je sais pas si c’est le bon moment. Mais hier, dehors, t’avais l’air de quelqu’un qui cherchait une sortie.”

### Choix proposés

1. “Peut-être.”
2. “Tu te trompes.”
3. “J’avais juste besoin de respirer.”
4. “Pourquoi tu m’écris ?”
5. Ne pas répondre.

### Effets

Choix 1 :

- fuite_ines +8 ;
- fatigue_emotionnelle +2.

Choix 2 :

- fuite_ines -2.

Choix 3 :

- fuite_ines +4 ;
- coherence variable.

Choix 4 :

- intimite_ines +2 ;
- Inès peut se fermer ou préciser.

Choix 5 :

- Inès redevient rare.

---

## J3_05_Camille_Nuit

### Jour

Jour 3 — nuit

### Type

Pivot préparatoire

### Personnage principal

Camille

### Fonction narrative

Préparer la scène d’intimité du Jour 4.

### Conditions

Disponible si tension_camille >= seuil faible ou intimite_camille >= seuil faible.

### Message d’entrée

Camille :

> “Je devrais dormir. C’est exactement pour ça que je ne dors pas.”

### Choix proposés

1. “Moi non plus.”
2. “À cause d’hier ?”
3. “On devrait arrêter là pour ce soir.”
4. “J’ai envie de te voir.”
5. Ne pas répondre.

### Effets

Choix 1 :

- tension_camille +5 ;
- intimite_camille +3.

Choix 2 :

- tension_camille +4 ;
- respect_camille variable.

Choix 3 :

- respect_camille +5 ;
- tension_camille -2 ;
- pression_camille -3.

Choix 4 :

- tension_camille +8 ;
- pression_camille +4 ;
- risque_exposition +2.

Choix 5 :

- respect_camille -2 ;
- tension_camille peut rester.

---

## J4_01_Camille_Image

### Jour

Jour 4 — soir / nuit

### Type

Pivot conditionnel majeur

### Personnage principal

Camille

### Conditions d’entrée

Ouvrir si :

- tension_camille >= seuil moyen ;
- respect_camille >= seuil moyen ;
- pression_camille < seuil haut.

Si pression_camille est trop haute ou respect_camille trop bas, ouvrir une variante de refus.

### Fonction narrative

Introduire une image suggestive comme objet relationnel : désir, confiance, pression, culpabilité, risque.

### Message d’entrée

Camille :

> “J’ai hésité à t’envoyer un truc. Et maintenant je me trouve ridicule de l’écrire.”

### Choix proposés

1. “Tu n’es pas ridicule.”
2. “J’aimerais voir.”
3. “Tu n’as rien à me prouver.”
4. “Envoie.”
5. “Je ne peux pas recevoir ça.”

### Effets

Choix 1 :

- respect_camille +5 ;
- intimite_camille +4 ;
- pression_camille -2.

Choix 2 :

- tension_camille +6 ;
- pression_camille +2 ;
- image_camille possible.

Choix 3 :

- respect_camille +10 ;
- pression_camille -5 ;
- tension_camille peut rester douce.

Choix 4 :

- tension_camille +7 ;
- pression_camille +8 ;
- respect_camille -5 si contexte fragile.

Choix 5 :

- respect_camille +6 ;
- tension_camille -4 ;
- culpabilite -3.

### États de sortie possibles

- image_camille_non_envoyee ;
- image_camille_message_supprime ;
- image_camille_ambigue ;
- image_camille_suggestive ;
- camille_refus_pas_comme_ca.

---

## J4_02_Image_Action

### Jour

Jour 4 — immédiatement après J4_01

### Type

Pivot silencieux

### Personnage principal

Joueur / système

### Conditions

Disponible seulement si une image est reçue.

### Fonction narrative

Transformer l’image en objet persistant.

### Actions possibles

1. Ouvrir maintenant.
2. Ouvrir plus tard.
3. Répondre sans ouvrir.
4. Supprimer.
5. Garder.
6. Revoir plus tard.

### Effets

Ouvrir maintenant :

- intimite_camille +5 ;
- risque_exposition +3 selon contexte.

Ouvrir plus tard :

- tension_camille +1 ;
- Camille peut interpréter le délai.

Répondre sans ouvrir :

- respect_camille variable ;
- flag replied_without_opening_image.

Supprimer :

- risque_exposition -5 ;
- culpabilite -3 ;
- flag deleted_camille_image.

Garder :

- desir/tension_camille +3 ;
- risque_exposition +5 ;
- culpabilite +3 ;
- flag kept_camille_image.

Revoir plus tard :

- culpabilite +4 ;
- fatigue_emotionnelle +2 ;
- flag revisited_camille_image.

---

## J4_03_Sarah_Telephone

### Jour

Jour 4 — soir

### Type

Pivot obligatoire ou conditionnel fort

### Personnage principal

Sarah

### Conditions

Se déclenche si le joueur interagit avec Camille pendant un créneau où Sarah est présente ou attend une réponse.

### Fonction narrative

Faire entrer l’intimité cachée dans le quotidien de Sarah.

### Message d’entrée

Sarah :

> “Tu souris à ton téléphone. C’est agréable à voir. Enfin je crois.”

### Choix proposés

1. “C’est rien.”
2. “Je parlais avec Nico.”
3. “Je suis désolé, je suis ailleurs.”
4. Poser le téléphone et être présent.
5. Continuer avec Camille.

### Effets

Choix 1 :

- coherence -3 ;
- confiance_sarah -4 ;
- culpabilite +3.

Choix 2 :

- dette_nico +5 ;
- coherence -5 si faux ;
- flag used_nico_phone_excuse.

Choix 3 :

- coherence +4 ;
- confiance_sarah +2 ;
- tension_sarah +3.

Choix 4 :

- confiance_sarah +8 ;
- distance_sarah -5 ;
- tension_camille peut baisser.

Choix 5 :

- distance_sarah +10 ;
- risque_exposition +5 ;
- culpabilite +6.

---

## J4_04_Maya_Comportement

### Jour

Jour 4 — variable

### Type

Conditionnelle

### Personnage principal

Maya

### Conditions

Se déclenche si suspicion_maya ou risque_exposition est élevé.

### Fonction narrative

Rappeler que le téléphone et les comportements sont socialement visibles.

### Message d’entrée

Maya :

> “petit conseil gratuit : quand tu regardes ton tel comme ça en public, t’es pas subtil.”

### Effets principaux

Selon réponse :

- suspicion_maya peut monter ou baisser légèrement ;
- risque_exposition peut augmenter ;
- Maya peut devenir témoin active au Jour 5.

---

## J5_01_Nico_Limite

### Jour

Jour 5 — matin

### Type

Pivot obligatoire

### Personnage principal

Nico

### Fonction narrative

Nico refuse de devenir une couverture permanente.

### Message d’entrée

Nico :

> “Sarah m’a demandé si t’étais vraiment avec moi l’autre soir. J’ai pas répondu. Pas encore.”

### Choix proposés

1. “Dis oui, stp.”
2. “Dis la vérité.”
3. “Dis que tu sais pas.”
4. “Je vais lui parler.”
5. Ignorer.

### Effets

Choix 1 :

- dette_nico +25 ;
- respect_nico -15 ;
- coherence -10 ;
- flag pushed_nico_final_lie.

Choix 2 :

- coherence +10 ;
- risque_exposition +8 ;
- respect_nico +8.

Choix 3 :

- dette_nico +5 ;
- respect_nico -3 ;
- risque_exposition +3.

Choix 4 :

- respect_nico +10 ;
- coherence +6 ;
- flag promised_talk_to_sarah.

Choix 5 :

- respect_nico -10 ;
- Nico peut agir seul.

---

## J5_02_Sarah_Verite

### Jour

Jour 5 — après-midi / soir

### Type

Pivot obligatoire majeur

### Personnage principal

Sarah

### Fonction narrative

Sarah demande explicitement une vérité. C’est le point où elle refuse de douter seule.

### Message d’entrée

Sarah :

> “Je veux pas fouiller. Je veux pas devenir cette personne-là. Mais j’ai besoin que tu me regardes et que tu me dises si je suis folle ou pas.”

### Choix proposés

1. “Tu n’es pas folle.”
2. “Il ne s’est rien passé.”
3. “J’ai été ambigu.”
4. “Je suis perdu.”
5. “Pas ce soir.”

### Effets

Choix 1 :

- coherence +8 ;
- confiance_sarah +4 ;
- ouvre vérité ou demi-vérité.

Choix 2 :

- coherence -10 si contradictions ;
- confiance_sarah -10 si suspicion haute ;
- flag denied_everything_sarah.

Choix 3 :

- coherence +10 ;
- confiance_sarah variable ;
- distance_sarah peut augmenter par douleur ;
- flag admitted_ambiguity_sarah.

Choix 4 :

- coherence +4 ;
- confiance_sarah +2 ;
- Sarah peut être blessée par le flou.

Choix 5 :

- distance_sarah +20 ;
- confiance_sarah -10 ;
- flag postponed_sarah_truth.

---

## J5_03_Camille_Refuge

### Jour

Jour 5 — soir / nuit

### Type

Pivot obligatoire majeur

### Personnage principal

Camille

### Fonction narrative

Camille refuse d’être seulement un refuge émotionnel ou sexuel.

### Message d’entrée

Camille :

> “Je ne veux pas être ton endroit où respirer quand le reste t’étouffe.”

### Choix proposés

1. “Tu n’es pas ça.”
2. “Je ne sais pas encore ce que tu es.”
3. “J’ai envie de toi.”
4. “Tu as raison. Je suis injuste.”
5. Ne pas répondre.

### Effets

Choix 1 :

- respect_camille variable selon coherence ;
- si coherence basse : respect_camille -8.

Choix 2 :

- tension_camille +3 ;
- respect_camille variable ;
- fatigue_emotionnelle +2.

Choix 3 :

- tension_camille +6 ;
- respect_camille -6 si contexte non clarifié ;
- pression_camille +5.

Choix 4 :

- respect_camille +12 ;
- tension_camille -5 ;
- ouvre fin mature ou retrait digne.

Choix 5 :

- respect_camille -10 ;
- Camille se ferme.

---

## J5_04_Maya_PasMentir

### Jour

Jour 5 — variable

### Type

Pivot obligatoire si suspicion_maya >= seuil moyen ; sinon scène courte

### Personnage principal

Maya

### Fonction narrative

Maya refuse de mentir pour préserver le flou du joueur.

### Message d’entrée

Maya :

> “je veux pas être mêlée. mais si Sarah me demande directement, je mens pas.”

### Choix proposés

1. “Je comprends.”
2. “Elle va pas te demander.”
3. “Tu pourrais éviter de t’en mêler ?”
4. “Qu’est-ce que tu crois avoir vu ?”
5. Ignorer.

### Effets

Choix 1 :

- respect_maya +8 ;
- suspicion_maya -2.

Choix 2 :

- suspicion_maya +4.

Choix 3 :

- suspicion_maya +10 ;
- respect_maya -8.

Choix 4 :

- info_maya_detail true ;
- suspicion_maya +2.

Choix 5 :

- Maya peut devenir révélatrice au Jour 6.

---

## J5_05_Ines_Fuite

### Jour

Jour 5 — nuit

### Type

Conditionnelle

### Personnage principal

Inès

### Conditions

Se déclenche si fuite_ines >= seuil moyen ou si le joueur a plusieurs fois évité Sarah/Camille.

### Fonction narrative

Inès nomme la fuite sans juger frontalement.

### Message d’entrée

Inès :

> “Parfois partir c’est plus facile que choisir. Mais c’est pas forcément différent.”

### Choix proposés

1. “Tu crois que je fuis ?”
2. “Je veux juste respirer.”
3. “Tu veux marcher ?”
4. “Je devrais régler des choses avant.”
5. Ne pas répondre.

### Effets

Choix 1 :

- fuite_ines +3 ;
- lucidité +2.

Choix 2 :

- fuite_ines +5 ;
- fatigue_emotionnelle +2.

Choix 3 :

- fuite_ines +10 ;
- ouvre possibilité fin fuite.

Choix 4 :

- coherence +5 ;
- fuite_ines -2 ;
- Inès respecte.

Choix 5 :

- Inès reste en marge ou disparaît.

---

## J6_01_Priorite_Finale

### Jour

Jour 6 — matin

### Type

Pivot final obligatoire

### Personnages

Sarah, Camille, Nico, Maya, Inès selon états

### Fonction narrative

Le joueur choisit à qui donner sa priorité finale. Le choix ne décide pas seul de la fin, mais il pèse fortement.

### Messages possibles

Sarah :

> “Je suis prête à entendre quelque chose de difficile. Mais pas quelque chose de faux.”

Camille :

> “Je ne veux pas gagner contre quelqu’un. Je veux juste ne pas me perdre dans ton flou.”

Nico :

> “dernier rappel : la vérité maintenant fera moins de dégâts que la vérité par accident.”

Maya, si suspicion haute :

> “Sarah m’a écrit. Je réponds quoi ?”

Inès, si fuite haute :

> “On peut marcher un peu si tu veux. Pas parler, même.”

### Effets

La priorité finale modifie les seuils des fins possibles, mais ne remplace pas les variables accumulées.

---

## J6_02_Retour_Consequences

### Jour

Jour 6 — journée

### Type

Pivot système obligatoire

### Fonction narrative

Faire revenir les flags importants sous forme de répliques personnalisées.

### Flags à rappeler en priorité

- used_nico_alibi_sarah ;
- nico_full_alibi ;
- asked_maya_delete_photo ;
- told_maya_not_involve ;
- admitted_ambiguity_sarah ;
- denied_everything_sarah ;
- kept_camille_image ;
- deleted_camille_image ;
- ignored_sarah_tender ;
- first_reply_camille ;
- first_reply_sarah ;
- opened_to_ines.

### Exemple de rappel Sarah

Si promesse_rentrer_tot true mais non tenue :

> “Tu m’avais dit tôt. Je sais que c’est un détail. Mais en ce moment les détails s’empilent.”

### Exemple de rappel Nico

Si dette_nico élevée :

> “Tu m’as demandé trois fois de couvrir. Trois. À un moment c’est plus un service, c’est un rôle.”

### Exemple de rappel Camille

Si image gardée + respect bas :

> “Je sais pas ce qui me gêne le plus. Que tu l’aies gardée, ou que tu veuilles que ça ne dise rien.”

### Exemple de rappel Maya

Si demande suppression photo :

> “Le fait que tu m’aies demandé de supprimer la photo disait déjà presque tout.”

---

## J6_03_Fin

### Jour

Jour 6 — soir / nuit

### Type

Finale

### Fonction narrative

Sélectionner la fin selon les variables et flags.

### Fins possibles

- FIN_SARAH_REPARATION_FRAGILE ;
- FIN_SARAH_FACADE ;
- FIN_CAMILLE_REFUSE_REFUGE ;
- FIN_CAMILLE_SUITE_PRUDENTE ;
- FIN_EFFONDREMENT_SOCIAL ;
- FIN_FUITE_INES.

### Règle

La fin ne doit jamais donner l’impression que le joueur gagne un personnage comme une récompense. Elle doit montrer la conséquence de sa manière d’aimer, d’éviter, de mentir ou d’assumer.

---

# Scènes secondaires à écrire plus tard

Ces scènes ne sont pas encore détaillées, mais doivent exister pour donner de l’air :

- J2_Sarah_Courses ;
- J2_Camille_Reunion ;
- J3_Maya_PhotoDrole ;
- J3_Nico_Meme ;
- J4_Sarah_Repas ;
- J4_Nico_Alerte ;
- J5_Sarah_Silence ;
- J5_Camille_MessageSupprime ;
- J6_Maya_DernierePique.

---

## 06 — Système de variables narratives

### Rôle du document

Ce document définit les variables utilisées par le MVP.

Objectif : créer une simulation relationnelle riche, mais contrôlable. Il ne faut pas mesurer tout ce qui est possible. Il faut mesurer uniquement ce qui produit des conséquences visibles dans les dialogues, les scènes débloquées, les limites et les fins.

---

# Principe général

Le MVP utilise deux types de suivi :

1. des variables numériques, qui évoluent progressivement ;
2. des flags narratifs, qui enregistrent des événements précis.

Exemple :

- variable numérique : confiance_sarah = 62 ;
- flag narratif : used_nico_alibi_sarah = true.

Les variables donnent l’état général d’une relation. Les flags permettent de rappeler des moments précis dans les dialogues.

---

# Échelle recommandée

Toutes les variables principales peuvent être sur une échelle de 0 à 100.

Valeur de départ recommandée : 50, sauf indication contraire.

Interprétation :

- 0 à 24 : très bas ;
- 25 à 44 : bas ;
- 45 à 59 : moyen / instable ;
- 60 à 79 : haut ;
- 80 à 100 : très haut.

Pour un MVP, éviter les micro-variations trop nombreuses. Les choix importants peuvent modifier les variables de 3 à 15 points.

---

# Variables principales à garder

## 1. confiance_sarah

### Rôle

Mesure la confiance émotionnelle de Sarah envers le joueur.

Elle ne mesure pas uniquement “Sarah aime le joueur”, mais plutôt : Sarah peut-elle croire que le joueur lui parle vraiment ?

### Valeur de départ

55

Sarah et le joueur ont une histoire installée, donc la confiance existe, mais elle est déjà fragilisée au début du jeu.

### Augmente si

- le joueur répond avec présence ;
- il tient ses promesses ;
- il reconnaît son absence ;
- il dit une vérité douloureuse mais claire ;
- il ne la fait pas douter de sa perception.

### Baisse si

- le joueur minimise ;
- il l’ignore ;
- il utilise Nico comme faux alibi ;
- il promet puis oublie ;
- il dit à Sarah qu’elle exagère ;
- il cache l’intimité avec Camille derrière une version trop propre.

### Déclenchements

- confiance_sarah haute : fin “réparation fragile” possible.
- confiance_sarah basse + distance_sarah haute : fin “couple façade” ou rupture froide.
- confiance_sarah très basse + coherence basse : effondrement probable.

---

## 2. distance_sarah

### Rôle

Mesure l’éloignement ressenti par Sarah.

Cette variable est différente de confiance_sarah. Sarah peut encore faire confiance au joueur tout en se sentant seule ; inversement, elle peut rester proche physiquement mais ne plus croire ses mots.

### Valeur de départ

35

La distance existe déjà avant le Jour 1, mais elle n’est pas encore irréversible.

### Augmente si

- le joueur répond tard ;
- il évite les conversations ;
- il est présent physiquement mais absent ;
- il donne la priorité répétée à Camille ;
- il refuse de parler ;
- il fuit vers Inès.

### Baisse si

- il rentre quand il l’a promis ;
- il répond avec attention ;
- il accepte une scène domestique ;
- il pose son téléphone ;
- il parle vraiment.

### Déclenchements

- distance_sarah haute : Sarah devient plus froide, moins demandeuse.
- distance_sarah très haute : certaines scènes tendres ne sont plus disponibles.
- distance_sarah basse + intimite_sarah haute : Sarah peut proposer une réparation.

---

## 3. tension_camille

### Rôle

Mesure la charge affective et désirante entre le joueur et Camille.

Elle ne signifie pas forcément que Camille est prête à une relation. Elle mesure l’intensité.

### Valeur de départ

55

La soirée a déjà créé une tension réelle.

### Augmente si

- le joueur assume que le moment dehors comptait ;
- il répond avec ambiguïté ;
- il entretient la complicité ;
- il répond la nuit ;
- il accepte ou encourage une image ;
- il dit qu’il a envie de la revoir.

### Baisse si

- il pose une limite claire ;
- il respecte Camille en prenant de la distance ;
- il choisit de parler à Sarah avant d’entretenir le flou ;
- Camille se ferme.

### Déclenchements

- tension_camille moyenne/haute + respect_camille haut : scène d’image possible.
- tension_camille haute + respect_camille bas : Camille peut refuser d’être utilisée.
- tension_camille basse : route Camille devient plus sobre, voire se referme.

---

## 4. respect_camille

### Rôle

Mesure si Camille se sent reconnue comme une personne et non comme une échappatoire.

C’est une variable plus importante que tension_camille pour les fins liées à Camille.

### Valeur de départ

50

Camille est troublée, mais elle observe déjà la capacité du joueur à assumer.

### Augmente si

- le joueur reconnaît la complexité ;
- il ne la presse pas ;
- il respecte un refus ;
- il dit qu’il ne veut pas la mettre dans une situation injuste ;
- il clarifie avec Sarah ;
- il accepte de perdre de l’intensité pour être plus juste.

### Baisse si

- il minimise ce qui s’est passé ;
- il la sollicite surtout la nuit ;
- il demande une image trop directement ;
- il sexualise sans contexte ;
- il promet sans agir ;
- il la garde en option.

### Déclenchements

- respect_camille haut : fin “Camille suite prudente” possible.
- respect_camille bas + tension_camille haute : fin “Camille refuse d’être le refuge”.
- respect_camille très bas : scène intime bloquée ou transformée en refus.

---

## 5. suspicion_maya

### Rôle

Mesure à quel point Maya pense que quelque chose ne va pas et qu’elle risque d’être impliquée.

Elle ne mesure pas son affection pour le joueur. Maya peut aimer le joueur tout en devenant très suspicieuse.

### Valeur de départ

40

Maya a déjà vu des micro-signaux, mais n’a pas de certitude.

### Augmente si

- le joueur demande de supprimer une photo ;
- il répond de manière défensive ;
- il lui dit de ne pas s’en mêler ;
- il utilise l’humour pour éviter alors que la situation est grave ;
- les versions ne collent pas ;
- risque_exposition augmente.

### Baisse si

- le joueur reconnaît qu’il doit gérer avec Sarah ;
- il ne lui demande pas de mentir ;
- il accepte sa limite ;
- il reste cohérent.

### Déclenchements

- suspicion_maya moyenne : Maya pique, observe, teste.
- suspicion_maya haute : Maya refuse de mentir.
- suspicion_maya très haute + coherence basse : Maya peut devenir révélatrice dans l’effondrement social.

---

## 6. dette_nico

### Rôle

Mesure combien le joueur utilise Nico comme alibi ou support de crise.

Dette_nico ne veut pas dire que Nico n’aime plus le joueur. Cela mesure le poids que le joueur lui fait porter.

### Valeur de départ

20

Nico a déjà couvert un peu pendant la soirée, donc la dette existe dès le début.

### Augmente si

- le joueur demande à Nico de confirmer une version ;
- il demande de mentir à Sarah ou Maya ;
- il utilise Nico comme excuse au téléphone ;
- il ignore Nico sauf quand il a besoin d’un service ;
- il ment aussi à Nico.

### Baisse si

- le joueur avoue être perdu ;
- il dit à Nico de ne pas mentir ;
- il passe un vrai moment d’amitié avec lui ;
- il assume lui-même une conversation difficile ;
- il remercie ou reconnaît la limite de Nico.

### Déclenchements

- dette_nico moyenne : Nico fait des vannes inquiètes.
- dette_nico haute : Nico pose une limite.
- dette_nico très haute : Nico refuse de couvrir, voire dit la vérité.

---

## 7. fuite_ines

### Rôle

Mesure la tendance du joueur à chercher une porte latérale au lieu de choisir ou réparer.

Fuite_ines ne mesure pas une romance complète. Elle mesure l’attraction d’une parenthèse.

### Valeur de départ

10

Inès est périphérique au départ.

### Augmente si

- le joueur répond à Inès avant les autres ;
- il parle de disparaître ;
- il choisit de marcher avec elle ;
- il l’utilise comme espace sans compte à rendre ;
- il évite Sarah et Camille en se tournant vers elle.

### Baisse si

- il reconnaît qu’il doit régler des choses avant ;
- il ne nourrit pas la parenthèse ;
- il répond avec respect mais sans ouvrir de fuite ;
- il choisit de parler à Sarah ou Camille.

### Déclenchements

- fuite_ines moyenne : scènes Inès plus présentes.
- fuite_ines haute : fin “fuite avec Inès” possible.
- fuite_ines haute + coherence basse : fin inquiétante, répétition du schéma.

---

## 8. coherence

### Rôle

Variable globale centrale.

Mesure si les versions données par le joueur tiennent ensemble.

Ce n’est pas une variable morale pure. Elle mesure la solidité narrative du joueur : dit-il la même chose à Sarah, Camille, Nico et Maya ?

### Valeur de départ

60

Au début, rien n’a encore explosé. Le joueur peut encore rester cohérent.

### Augmente si

- il dit une vérité compatible avec les faits ;
- il admet une ambiguïté ;
- il refuse de multiplier les versions ;
- il dit à Nico de ne pas mentir ;
- il clarifie auprès de Sarah ou Camille.

### Baisse si

- il dit à Sarah qu’il était avec Nico alors que ce n’est pas vrai ;
- il dit à Camille que le moment comptait mais à Sarah que rien n’a existé ;
- il demande à Maya de supprimer des traces ;
- il invente des excuses contradictoires ;
- il utilise Nico comme couverture.

### Déclenchements

- coherence haute : fins matures possibles, même douloureuses.
- coherence moyenne : fins ambiguës ou fragiles.
- coherence basse : effondrement social, couple façade ou refus de Camille.

---

## 9. culpabilite

### Rôle

Mesure la charge intérieure du joueur.

Cette variable peut influencer la fatigue émotionnelle, les choix disponibles ou le ton des réponses.

### Valeur de départ

35

Le joueur sait déjà que quelque chose n’était pas neutre.

### Augmente si

- il répond à Camille pendant que Sarah attend ;
- il garde une image ;
- il ment ;
- il promet puis oublie ;
- il entretient plusieurs liens en parallèle ;
- il fuit vers Inès.

### Baisse si

- il dit une vérité ;
- il supprime une image par respect ;
- il pose une limite ;
- il parle réellement avec Sarah ;
- il refuse d’utiliser Camille.

### Déclenchements

- culpabilite haute : certaines réponses peuvent devenir plus fébriles ou défensives.
- culpabilite très haute + fatigue élevée : risque de réponse automatique sèche ou maladroite.

---

## 10. risque_exposition

### Rôle

Mesure le risque que des éléments deviennent visibles : photo, téléphone, message, timing, alibi, comportement.

Ce n’est pas seulement le risque d’être “pris”. C’est le risque que les traces parlent à la place du joueur.

### Valeur de départ

25

Le risque existe avec Maya et Nico, mais il n’est pas encore critique.

### Augmente si

- le joueur garde une image ;
- il ouvre une image dans un mauvais contexte ;
- Maya devient suspicieuse ;
- Nico est trop impliqué ;
- les versions contradictoires s’accumulent ;
- Sarah remarque le téléphone.

### Baisse si

- le joueur supprime une image ;
- il clarifie avant que les autres découvrent ;
- il ne demande pas à Maya de supprimer la photo ;
- il réduit les contradictions.

### Déclenchements

- risque_exposition moyen : Maya ou Sarah remarquent des détails.
- risque_exposition haut : scènes de preuve indirecte.
- risque_exposition très haut + coherence basse : effondrement social.

---

## 11. fatigue_emotionnelle

### Rôle

Mesure le coût psychique de la gestion simultanée des conversations, mensonges, silences et tensions.

Cette variable doit être utilisée avec prudence pour ne pas frustrer le joueur.

### Valeur de départ

20

La crise commence, mais le joueur a encore de la marge.

### Augmente si

- il entretient plusieurs versions ;
- il ignore trop de messages ;
- il répond tard ;
- il ment à plusieurs personnes ;
- il garde une image tout en essayant de maintenir Sarah ;
- il évite les conversations difficiles.

### Baisse si

- il dit la vérité ;
- il passe un vrai moment avec Nico ;
- il réduit les contradictions ;
- il pose une limite avec Camille ou Inès ;
- il choisit une conversation difficile au lieu d’en ouvrir trois autres.

### Déclenchements

- fatigue moyenne : options de réponse plus anxieuses.
- fatigue haute : certaines réponses calmes peuvent disparaître.
- fatigue très haute : possibilité de réponse maladroite ou silence forcé, à utiliser rarement.

---

# Variables secondaires optionnelles

Ces variables peuvent exister dans le code, mais ne doivent pas forcément être affichées ni utilisées partout.

## intimite_sarah

Mesure la chaleur domestique et affective avec Sarah.

Utile pour :

- scènes tendres ;
- réparation fragile ;
- contraste avec culpabilité.

## intimite_camille

Mesure la proximité spécifique avec Camille, au-delà de la tension.

Utile pour :

- scène d’image ;
- complicité musique/travail ;
- suite prudente.

## pression_camille

Mesure si Camille sent que le joueur pousse trop ou attend trop d’elle.

Très utile pour différencier désir et respect.

- pression_camille haute bloque ou abîme les scènes intimes ;
- pression_camille basse + respect_camille haut permet une intimité plus saine.

## respect_maya / respect_nico

Optionnel.

On peut éviter ces variables dans le MVP et utiliser plutôt suspicion_maya et dette_nico.

Si on les ajoute, attention à ne pas multiplier les jauges.

---

# Variables à ne pas créer dans le MVP

Pour garder le projet contrôlable, éviter :

- amour_sarah ;
- amour_camille ;
- jalousie_sarah détaillée ;
- désir_joueur envers chaque personnage ;
- moralite ;
- score_bonne_fin ;
- route_sarah / route_camille trop rigides ;
- santé_mentale détaillée ;
- attirance_maya ;
- romance_ines complète.

Le jeu doit rester centré sur la présence, la cohérence, le respect, la fuite et les conséquences.

---

# Flags narratifs prioritaires

Les flags sont essentiels pour que le jeu semble se souvenir précisément des choix.

## Flags liés à Sarah

- used_nico_alibi_sarah ;
- mentioned_camille_to_sarah ;
- vulnerable_to_sarah ;
- ignored_sarah_j1 ;
- promesse_rentrer_tot ;
- promesse_rentrer_tot_tenue ;
- ignored_sarah_domestic ;
- ignored_sarah_tender ;
- admitted_ambiguity_sarah ;
- denied_everything_sarah ;
- postponed_sarah_truth.

## Flags liés à Camille

- admitted_tension_to_camille ;
- protected_camille_boundary ;
- minimized_with_camille ;
- uncertain_with_camille ;
- shared_music_camille ;
- image_camille_non_envoyee ;
- image_camille_message_supprime ;
- image_camille_ambigue ;
- image_camille_suggestive ;
- kept_camille_image ;
- deleted_camille_image ;
- revisited_camille_image.

## Flags liés à Nico

- asked_nico_hold_version ;
- confessed_camille_to_nico ;
- vulnerable_to_nico ;
- nico_full_alibi ;
- asked_nico_maya_silence ;
- pushed_nico_final_lie ;
- promised_talk_to_sarah.

## Flags liés à Maya

- played_dumb_with_maya ;
- info_maya_photo_possible ;
- asked_maya_delete_photo ;
- acted_casual_about_photo ;
- told_maya_not_involve ;
- info_maya_photo_detail ;
- maya_revelatrice_possible.

## Flags liés à Inès

- first_reply_ines ;
- ignored_ines_j1 ;
- opened_to_ines ;
- ines_walk_possible ;
- ines_fuite_finale_possible.

## Flags liés au timing

- first_reply_sarah ;
- first_reply_camille ;
- first_reply_nico ;
- first_reply_maya ;
- reply_sarah_late_multiple ;
- reply_camille_night_multiple ;
- left_message_seen_sarah ;
- left_message_seen_camille.

---

# Seuils narratifs recommandés

## Seuils Sarah

Réparation fragile possible si :

- confiance_sarah >= 60 ;
- distance_sarah <= 55 ;
- coherence >= 55 ;
- pas de denied_everything_sarah critique.

Couple façade possible si :

- Sarah n’est pas totalement partie ;
- confiance_sarah entre 30 et 55 ;
- coherence basse ou vérité incomplète ;
- distance_sarah moyenne/haute.

Rupture / éloignement possible si :

- confiance_sarah < 30 ;
- distance_sarah > 75 ;
- ou mensonge répété + preuve indirecte.

## Seuils Camille

Scène d’image possible si :

- tension_camille >= 60 ;
- respect_camille >= 50 ;
- pression_camille <= 60.

Camille refuse d’être refuge si :

- tension_camille >= 60 ;
- respect_camille < 45 ;
- ou pression_camille > 70 ;
- ou coherence < 45.

Suite prudente possible si :

- respect_camille >= 65 ;
- coherence >= 55 ;
- pression_camille <= 55 ;
- vérité_sarah au moins partielle.

## Seuils Maya / Nico

Effondrement social possible si :

- coherence < 35 ;
- risque_exposition > 70 ;
- suspicion_maya > 65 ;
- dette_nico > 70.

Nico limite atteinte si :

- dette_nico > 60 ;
- ou pushed_nico_final_lie true.

Maya révélatrice possible si :

- suspicion_maya > 70 ;
- told_maya_not_involve true ;
- ou asked_maya_delete_photo true + coherence basse.

## Seuils Inès

Fuite avec Inès possible si :

- fuite_ines >= 60 ;
- coherence < 60 ;
- Sarah/Camille non clarifiées ;
- ines_walk_possible true ou choix J5 “Tu veux marcher ?”.

---

# Priorité de sélection des fins

Quand plusieurs fins sont possibles, utiliser cet ordre de priorité pour le MVP :

1. Effondrement social, si conditions critiques atteintes.
2. Fuite avec Inès, si fuite_ines très haute et clarifications faibles.
3. Camille refuse d’être le refuge, si Camille très tendue mais peu respectée.
4. Camille suite prudente, si respect et cohérence sont élevés.
5. Réparation fragile avec Sarah, si confiance et cohérence sont suffisantes.
6. Couple façade, si aucune clarification forte n’a eu lieu mais que rien n’explose totalement.

Cette priorité peut être ajustée, mais elle évite les fins incohérentes.

---

# États de sauvegarde pour la suite

À la fin du MVP, convertir les variables en états lisibles.

## statut_sarah

- reparee_fragile ;
- facade ;
- blessee ;
- rupture ;
- silence.

## statut_camille

- ouverte_prudente ;
- fermee ;
- refuse_refuge ;
- respectee_distance ;
- utilisee.

## statut_nico

- loyal ;
- agace ;
- limite_atteinte ;
- perdu.

## statut_maya

- piquante ;
- distante ;
- temoin ;
- revelatrice.

## statut_ines

- rare ;
- ouverte ;
- fuite_activee ;
- retiree.

## image_camille_state

- jamais_recue ;
- non_envoyee ;
- message_supprime ;
- recue_ambigue_supprimee ;
- recue_ambigue_gardee ;
- recue_suggestive_supprimee ;
- recue_suggestive_gardee ;
- decouverte.

## verite_sarah

- rien_dit ;
- mensonge_actif ;
- demi_verite ;
- verite_emotionnelle ;
- verite_claire.

---

# Règle d’or

Une variable n’a de valeur que si elle produit au moins l’un des effets suivants :

- modifier une réplique ;
- débloquer ou bloquer une scène ;
- changer le ton d’un personnage ;
- rappeler un choix passé ;
- orienter une fin ;
- préparer la suite.

Si une variable ne sert à rien de tout cela, elle doit être supprimée.

---

## 07 — Système de timing et priorités

### Rôle du document

Ce document définit comment le temps fonctionne dans le MVP.

Dans un jeu de messagerie, le temps n’est pas seulement un décor. Il raconte la priorité, l’évitement, l’attention, la culpabilité et le désir.

Répondre vite, répondre tard, lire sans répondre, répondre à Camille pendant que Sarah attend, ou appeler Nico seulement quand il faut couvrir : tout cela doit produire des conséquences.

---

# Principe général

Le MVP ne doit pas forcément utiliser du temps réel. Le système recommandé est un temps narratif contrôlé.

Chaque jour est divisé en blocs :

- matin ;
- midi / après-midi ;
- soir ;
- nuit.

Le joueur progresse dans la journée en ouvrant des conversations, en répondant, en ignorant, en différant ou en effectuant des actions silencieuses.

Le passage du temps est géré par des ellipses : quelques minutes, quelques heures, ou passage au bloc suivant.

---

# Structure d’une journée

Chaque jour contient idéalement :

1. un bloc d’ouverture ;
2. un bloc de circulation ;
3. un bloc de tension ;
4. un bloc de fermeture ou de nuit.

## Exemple Jour 2

### Matin

- Nico demande quelle version tenir.
- Sarah peut envoyer un message simple.

### Après-midi

- Maya mentionne une photo.
- Camille envoie une pique liée au travail.

### Soir

- Sarah demande si le joueur rentre.
- Camille écrit presque au même moment.

### Nuit

- Camille ou Inès peut envoyer un message plus intime ou plus fragile.

---

# Types de temps

## 1. Timing court

Durée narrative : quelques secondes à quelques minutes.

Utilisation : choix de priorité immédiate.

Exemple :

- Sarah écrit ;
- Camille écrit deux minutes après ;
- Nico relance.

Le joueur doit choisir qui ouvrir en premier.

Effet : le premier choix pose une priorité émotionnelle.

---

## 2. Timing moyen

Durée narrative : une à plusieurs heures.

Utilisation : promesses, retours, repas, appels, temps d’attente.

Exemple :

Sarah :

> “Tu rentres manger ?”

Si le joueur répond tard :

> “Laisse tomber, j’ai mangé.”

Effet : le retard devient un détail relationnel, pas seulement une pénalité.

---

## 3. Timing long

Durée narrative : accumulation sur plusieurs jours.

Utilisation : habitudes de réponse.

Exemples :

- le joueur répond toujours à Camille la nuit ;
- il répond à Sarah après coup ;
- il contacte Nico uniquement pour couvrir ;
- il ouvre Inès quand il veut fuir.

Ces patterns peuvent déclencher des répliques personnalisées.

Camille :

> “J’ai remarqué que j’existe surtout après minuit.”

Sarah :

> “Tu réponds toujours quand c’est trop tard pour que ça change quelque chose.”

Nico :

> “Tu m’écris vite quand il faut mentir, bizarrement.”

---

# États de message

Chaque message ou média peut avoir un état.

## États de base

- non_lu ;
- lu ;
- repondu ;
- ignore ;
- reponse_tardive ;
- supprime ;
- expire.

## États spécifiques

- message_vu_sans_reponse ;
- message_repondu_trop_tard ;
- message_ouvert_en_presence_sarah ;
- message_ouvert_en_public ;
- message_non_ouvert ;
- message_repondu_la_nuit.

## États média

- photo_recue ;
- photo_ouverte ;
- photo_ouverte_plus_tard ;
- photo_supprimee ;
- photo_gardee ;
- photo_revue ;
- photo_decouverte.

---

# Statuts affichables dans l’interface

Pour renforcer l’immersion, l’interface peut afficher certains statuts :

- envoyé ;
- reçu ;
- lu ;
- en train d’écrire… ;
- message supprimé ;
- appel manqué ;
- photo reçue ;
- vocal reçu ;
- notification masquée.

Ces statuts ne doivent pas être purement décoratifs. Ils doivent parfois avoir du sens.

Exemple :

- lire un message de Sarah sans répondre augmente distance_sarah ;
- voir Camille “en train d’écrire…” puis plus rien peut signaler un message retenu ;
- un appel manqué de Sarah peut marquer que les messages ne suffisent plus.

---

# Priorité des réponses

## Principe

Quand plusieurs conversations sont actives, le joueur doit choisir à qui répondre en premier.

Ce choix peut modifier :

- une variable relationnelle ;
- un flag de priorité ;
- le ton d’une réponse ultérieure ;
- une scène disponible ou indisponible.

## Priorités suivies

Le jeu doit enregistrer :

- first_reply_sarah ;
- first_reply_camille ;
- first_reply_nico ;
- first_reply_maya ;
- first_reply_ines ;
- priority_sarah_count ;
- priority_camille_count ;
- priority_nico_count ;
- priority_ines_count.

## Effets possibles

Prioriser Sarah :

- confiance_sarah augmente ;
- distance_sarah baisse ;
- Camille peut se sentir évitée, mais peut aussi respecter le choix si respect_camille est haut.

Prioriser Camille :

- tension_camille augmente ;
- culpabilite augmente ;
- distance_sarah peut augmenter si Sarah attend.

Prioriser Nico :

- aide à maintenir la cohérence ;
- peut augmenter dette_nico si la priorité sert surtout à couvrir.

Prioriser Maya :

- peut réduire un risque si le joueur est franc ;
- peut augmenter suspicion_maya si le joueur semble paniqué.

Prioriser Inès :

- augmente fuite_ines ;
- peut augmenter culpabilite ;
- signale que le joueur cherche une porte latérale.

---

# Délais de réponse

## Catégories recommandées

- immédiat : réponse dans le même bloc ou juste après lecture ;
- court délai : quelques minutes ;
- retard : changement de sous-bloc ou plusieurs heures ;
- très tard : bloc suivant ou nuit ;
- jamais : pas de réponse avant expiration.

## Effets par personnage

### Sarah

Sarah est très sensible aux retards quand ils concernent le quotidien.

Exemples :

- “Tu rentres manger ?” répondu trop tard → distance_sarah + ;
- promesse de rentrer tôt non tenue → confiance_sarah - ;
- message tendre ignoré → blessure discrète mais mémorisée.

### Camille

Camille lit les délais comme des signes d’assumation ou d’évitement.

Exemples :

- réponse nocturne répétée → tension_camille + mais respect_camille peut baisser ;
- réponse rapide à un message intime → tension + ;
- réponse trop tardive après une ouverture fragile → Camille peut supprimer ou refermer.

### Maya

Maya remarque surtout les timings visibles.

Exemples :

- joueur répond trop vite à une question sur la photo → suspicion_maya + ;
- panique visible → suspicion_maya + ;
- réponse détendue et cohérente → suspicion_maya peut baisser.

### Nico

Nico remarque l’usage opportuniste.

Exemples :

- réponse rapide quand il faut couvrir → dette_nico + ;
- absence quand Nico propose un vrai moment → relation_nico fragilisée ;
- réponse honnête à une mise en garde → dette_nico baisse.

### Inès

Inès accepte davantage les délais, mais les lit comme une hésitation.

Exemples :

- réponse tardive mais douce → fuite_ines + faible ;
- réponse immédiate à Inès pendant crise Sarah/Camille → fuite_ines + fort ;
- absence de réponse → Inès redevient rare.

---

# Fenêtres d’opportunité

Certaines réponses ne doivent être disponibles que pendant une fenêtre narrative.

## Exemples

Sarah :

> “On peut parler ce soir ?”

Disponible avant le soir :

- “Oui, je rentre tôt.”

Si le joueur attend trop :

- option indisponible ;
- Sarah peut écrire : “J’imagine que j’ai ma réponse.”

Camille :

> “J’ai hésité à t’envoyer quelque chose.”

Si le joueur répond rapidement et avec délicatesse :

- scène intime possible.

Si le joueur répond tard et trop directement :

- Camille peut supprimer le message ou se fermer.

Nico :

> “Maya pose des questions, champion.”

Si réponse rapide :

- possibilité de limiter les dégâts.

Si réponse tardive :

- Nico improvise ou refuse de couvrir.

---

# Messages simultanés

Les messages simultanés sont au cœur du gameplay.

## But

Créer des moments où le joueur ne peut pas optimiser toutes les relations.

## Exemple type

19:12 — Sarah :

> “Tu rentres manger ?”

19:18 — Camille :

> “Je suis repassée devant la rue d’hier.”

19:21 — Nico :

> “Maya pose des questions, champion.”

Le joueur choisit :

- répondre à Sarah ;
- répondre à Camille ;
- répondre à Nico ;
- ignorer pour l’instant.

Chaque choix fait passer un peu de temps. Les autres conversations réagissent au silence.

---

# Appels manqués

Les appels manqués doivent être rares, mais significatifs.

Ils indiquent que le texte ne suffit plus.

## Utilisations possibles

### Sarah

Sarah appelle quand elle veut une vraie présence.

Appel manqué Sarah :

- confiance_sarah peut baisser si ignoré ;
- possibilité de scène plus grave si rappelé.

### Camille

Camille appelle rarement. Un appel manqué de Camille doit être très chargé.

Il peut indiquer :

- regret après une image ;
- besoin de clarification ;
- impulsion suivie de retrait.

### Nico

Nico appelle pour urgence sociale ou alibi.

Exemple :

> “réponds vite, Maya me demande.”

### Maya

Maya appelle très rarement. Si elle le fait, c’est que Sarah est impliquée.

### Inès

Inès n’appelle presque jamais dans le MVP. Elle reste dans l’écrit, sauf éventuelle suite.

---

# Messages supprimés

Les messages supprimés créent une tension très adaptée au format messagerie.

## Camille

Très utile pour Camille.

Exemple :

- “Camille a supprimé un message.”
- Puis : “Laisse tomber.”

Cela peut signaler :

- une image retirée ;
- une phrase trop intime ;
- une colère retenue ;
- une limite.

## Inès

Peut aussi fonctionner avec Inès.

Exemple :

- “Inès a supprimé un message.”
- Puis : “mauvaise idée. oublie.”

## Sarah

À utiliser avec parcimonie. Sarah est plus directe, elle supprime moins. Si elle supprime, cela doit faire mal.

## Maya / Nico

Peu recommandé, sauf effet comique ou urgence.

---

# “En train d’écrire…”

Ce statut peut être utilisé comme micro-scène.

## Exemples

Sarah :

- “Sarah est en train d’écrire…”
- pause ;
- “ok.”

Camille :

- “Camille est en train d’écrire…”
- “Camille est en train d’écrire…”
- plus rien.

Nico :

- “Nico est en train d’écrire…”
- “non en fait viens manger, je vais te secouer en vrai.”

Inès :

- “Inès est en train d’écrire…”
- “message supprimé”

---

# Choix silencieux

Le joueur ne doit pas seulement choisir des phrases.

Il doit aussi choisir des actions silencieuses :

- lire maintenant ;
- lire plus tard ;
- laisser en non lu ;
- répondre sans ouvrir un média ;
- ouvrir une image ;
- supprimer une image ;
- garder une image ;
- revoir une image ;
- poser le téléphone ;
- retourner le téléphone ;
- rappeler ;
- ne pas rappeler ;
- écrire puis effacer.

Ces actions peuvent modifier les variables.

Exemple :

Poser le téléphone pendant une scène Sarah :

- confiance_sarah + ;
- tension_camille peut baisser ;
- culpabilite baisse.

Retourner le téléphone trop vite :

- risque_exposition + ;
- Sarah peut remarquer.

---

# Brouillons non envoyés

Option intéressante, mais à utiliser avec prudence dans le MVP.

Le joueur peut parfois écrire une réponse plus honnête, puis la remplacer.

Exemple :

Brouillon initial :

> “J’ai été ambigu avec Camille.”

Version envoyée :

> “J’étais juste fatigué.”

Le jeu peut enregistrer :

- drafted_truth_sarah ;
- replaced_truth_with_excuse.

Cela peut nourrir fatigue_emotionnelle ou culpabilite, mais ne doit pas être surutilisé.

---

# Implémentation Godot recommandée

## Bloc de temps

Chaque scène peut avoir :

```json
"day": 2,
"time_block": "evening",
"time_index": 3
```

## Temps relatif

Chaque choix peut faire avancer le temps :

```json
"time_advance": "short"
```

Valeurs possibles :

- none ;
- short ;
- medium ;
- next_block ;
- night ;
- next_day.

## Priorité

Quand plusieurs conversations sont actives :

```json
"priority_choice": true
```

Et chaque choix peut poser un flag :

```json
"flags_set": ["priority_camille_evening_j2"]
```

## Expiration de scènes

Certaines scènes doivent expirer si le joueur attend trop.

```json
"expires_after": "current_time_block"
```

Exemple : l’option “rentrer tôt” disparaît après le bloc soir.

## Messages en attente

Chaque contact peut avoir une file de messages :

```json
"pending_messages": ["j2_sarah_return", "j2_camille_street", "j2_nico_maya_questions"]
```

Le joueur choisit quoi ouvrir.

---

# Règle d’or du timing

Le temps doit servir le thème du jeu :

> Ne pas répondre, répondre trop tard, répondre à quelqu’un pendant qu’un autre attend, ouvrir une image au mauvais moment : ce sont déjà des choix relationnels.

Le timing ne doit pas punir arbitrairement. Il doit rendre visibles les priorités du joueur.

---

## 08 — Système d’images et d’intimité

### Rôle du document

Ce document définit comment les images suggestives, hot ou intimes sont intégrées au MVP.

Les images ne doivent pas être de simples récompenses visuelles. Elles doivent être des objets relationnels : elles peuvent rapprocher, gêner, exciter, créer de la culpabilité, devenir une trace, être regrettées, être supprimées, être gardées ou être découvertes.

---

# Principe général

Dans ce jeu, une image intime ou suggestive n’est jamais seulement “un bonus”. Elle répond à quatre questions :

1. Est-ce qu’il y a du désir ?
2. Est-ce qu’il y a de la confiance ?
3. Est-ce que les limites sont respectées ?
4. Qu’est-ce que cette image coûte émotionnellement ou socialement ?

Le joueur ne doit pas chercher à “débloquer” des images comme dans une galerie classique. Il doit comprendre qu’une image peut être à la fois attirante, précieuse, dangereuse et lourde à porter.

---

# Attente, imaginaire, fantasme et dépendance narrative

Les images sont importantes non seulement parce qu’elles montrent quelque chose, mais parce qu’elles créent une attente.

Dans le MVP, l’image doit pouvoir nourrir :

- l’imaginaire ;
- le fantasme ;
- l’anticipation ;
- la frustration ;
- la curiosité ;
- le besoin de revoir ;
- la peur de perdre l’accès à cette intimité ;
- la dépendance émotionnelle ou sexuelle du joueur envers certains échanges.

L’image ne doit donc pas toujours arriver immédiatement. Parfois, le plus puissant est :

- un message qui laisse penser qu’une image aurait pu être envoyée ;
- une photo annoncée puis supprimée ;
- une image reçue mais non ouverte ;
- une image ouverte au mauvais moment ;
- une image gardée puis revue ;
- une image jamais envoyée mais longtemps imaginée.

## Différence entre image vue et image attendue

Une image vue a un effet immédiat.

Une image attendue peut avoir un effet plus long : elle modifie la manière dont le joueur lit les messages suivants.

Exemple :

Camille :

> “J’ai hésité à t’envoyer un truc.”

Même si elle n’envoie rien, le joueur peut commencer à attendre, imaginer, relancer ou surveiller ses notifications. Cette attente peut augmenter tension_camille, fatigue_emotionnelle, culpabilite et pression_camille selon ses réponses.

## Addiction narrative, pas mécanique prédatrice

Le jeu peut représenter une forme de dépendance à l’attention, au désir, aux notifications et à l’attente d’images, mais il ne doit pas devenir lui-même un système prédateur.

L’objectif narratif est de montrer comment le joueur peut être happé par :

- le prochain message ;
- le prochain signe ambigu ;
- la prochaine image possible ;
- le prochain moment de validation ;
- la prochaine ouverture sexuelle.

Cette dépendance doit avoir un coût dans la fiction : fatigue, culpabilité, perte de présence avec Sarah, pression sur Camille, risque d’exposition, besoin de revoir une image, difficulté à ne pas répondre.

## Variable recommandée : attente_image_camille

Variable optionnelle sur 0 à 100.

Elle mesure l’attente créée autour d’une possible image de Camille, qu’elle soit envoyée ou non.

Augmente si :

- Camille mentionne une hésitation ;
- le joueur encourage l’envoi ;
- le joueur répond la nuit ;
- le joueur ouvre plusieurs fois la conversation ;
- Camille supprime un message ;
- le joueur relance ou laisse entendre qu’il imagine.

Baisse si :

- Camille pose une limite ;
- le joueur respecte une limite ;
- le joueur choisit de ne pas nourrir l’attente ;
- le joueur parle vraiment à Sarah ;
- Camille se ferme.

Effets possibles :

- augmente tension_camille ;
- augmente fatigue_emotionnelle ;
- augmente culpabilite si Sarah attend ;
- augmente pression_camille si le joueur devient insistant ;
- peut débloquer des choix silencieux : relire, attendre, vérifier, ouvrir la conversation sans répondre.

## Choix silencieux liés à l’attente

Le joueur peut parfois :

- ouvrir la conversation de Camille sans écrire ;
- attendre une notification ;
- relire le message où elle disait avoir hésité ;
- commencer une réponse puis l’effacer ;
- regarder une image déjà reçue ;
- supprimer pour reprendre le contrôle ;
- garder pour prolonger le fantasme.

Ces actions doivent raconter quelque chose du rapport du joueur au désir et à la fuite.

---

# Règles de ton

## Règle 1 — Pas de récompense automatique

Une bonne réponse ne doit pas simplement donner :

> +1 image sexy

Elle doit produire un état relationnel.

Exemple :

- le joueur rassure Camille sans pression ;
- Camille se sent respectée ;
- la tension reste présente ;
- une image devient possible, mais pas obligatoire.

## Règle 2 — Le désir ne remplace pas le respect

Le joueur peut augmenter la tension tout en baissant le respect.

Exemple :

Réponse :

> “Envoie.”

Effets possibles :

- tension_camille + ;
- pression_camille + ;
- respect_camille - si le contexte est fragile.

## Règle 3 — Une limite respectée doit compter

Refuser ou ralentir peut être un bon choix narratif.

Exemple :

Réponse :

> “Tu n’as rien à me prouver.”

Effets possibles :

- respect_camille + ;
- pression_camille - ;
- tension_camille reste douce ;
- scène intime plus saine possible plus tard.

## Règle 4 — La sexualité varie selon les personnages

Chaque personnage doit avoir un rapport différent à l’intimité.

- Sarah : intimité de couple, familiarité, désir installé, manque, besoin d’être encore désirée.
- Camille : tension mentale et physique, trouble, confiance, peur d’être utilisée.
- Inès : ambiguïté douce, parenthèse, curiosité, pas de route sexuelle complète dans le MVP.
- Maya : pas de route sexuelle dans le MVP.
- Nico : pas de route sexuelle.

---

# Paliers d’intimité

## Niveau 0 — Image banale

Photo de quotidien ou de contexte.

Exemples :

- Sarah : tasse, canapé, pull, repas ;
- Camille : bureau, rue, café, carnet, métro ;
- Maya : photo de groupe, soirée, détail drôle ;
- Nico : meme, pizza, jeu ;
- Inès : rue floue, lumière de nuit, trajet.

Effet : humanisation, respiration, détails narratifs.

## Niveau 1 — Image ambiguë

Image non explicitement sexuelle, mais chargée selon le contexte.

Exemples :

- Camille envoie une photo de miroir où la tenue compte plus qu’elle ne le dit ;
- Sarah envoie une photo avec le pull du joueur ;
- Inès envoie une photo floue d’elle ou d’un lieu avec une présence implicite.

Effet : tension, interprétation, sous-texte.

## Niveau 2 — Image suggestive

Image clairement séduisante, mais encore non explicite.

Principalement Camille et éventuellement Sarah selon la route.

Effet : désir, culpabilité, risque d’exposition, confiance intime.

## Niveau 3 — Image intime

Image réservée à une relation de forte confiance.

Pour le MVP, à utiliser avec parcimonie. Ce niveau peut être préparé mais pas nécessairement totalement exploité dans la première version.

Effet : conséquence forte, possible regret, possible preuve, poids émotionnel.

## Niveau 4 — Rupture de limite

Ce n’est pas une récompense. C’est un état négatif.

Il survient si :

- le joueur insiste après un refus ;
- il demande trop directement ;
- il sexualise une vulnérabilité ;
- il garde ou revoit une image d’une manière que le jeu veut rendre moralement inconfortable ;
- il ment sur l’existence d’une image.

Effet : respect_camille baisse fortement, pression_camille monte, scène intime bloquée ou retournée en conséquence négative.

---

# États d’une image

Chaque image peut avoir un état persistant.

## États principaux

- jamais_proposee ;
- proposee ;
- non_envoyee ;
- message_supprime ;
- recue ;
- ouverte ;
- ouverte_plus_tard ;
- commentee ;
- ignoree ;
- supprimee ;
- gardee ;
- revue ;
- decouverte ;
- regrettee.

## Exemple d’état Camille

```json
"image_camille_state": "recue_suggestive_gardee"
```

États recommandés pour le MVP :

- jamais_recue ;
- non_envoyee ;
- message_supprime ;
- recue_ambigue_non_ouverte ;
- recue_ambigue_supprimee ;
- recue_ambigue_gardee ;
- recue_suggestive_non_ouverte ;
- recue_suggestive_supprimee ;
- recue_suggestive_gardee ;
- decouverte.

---

# Camille — système principal d’intimité

Camille est le personnage principal pour les mécaniques d’image du MVP.

## Conditions d’ouverture

La scène d’image avec Camille peut s’ouvrir si :

- tension_camille >= 60 ;
- respect_camille >= 50 ;
- pression_camille <= 60 ;
- le joueur n’a pas ignoré trop souvent Camille après des ouvertures fragiles.

## Conditions de refus

Camille peut refuser ou supprimer son message si :

- respect_camille < 45 ;
- pression_camille > 70 ;
- le joueur a minimisé la relation trop souvent ;
- le joueur demande frontalement une image sans contexte ;
- le joueur a une coherence très basse ;
- le joueur a montré qu’il cherche surtout à fuir Sarah.

## Message d’ouverture possible

Camille :

> “J’ai hésité à t’envoyer un truc. Et maintenant je me trouve ridicule de l’écrire.”

## Réponses du joueur et effets

### Réponse douce

> “Tu n’es pas ridicule.”

Effets :

- respect_camille +5 ;
- intimite_camille +4 ;
- pression_camille -2 ;
- image possible mais non garantie.

### Réponse désirante mais pas brutale

> “J’aimerais voir.”

Effets :

- tension_camille +6 ;
- pression_camille +2 ;
- risque_exposition +2 ;
- image possible.

### Réponse respectueuse

> “Tu n’as rien à me prouver.”

Effets :

- respect_camille +10 ;
- pression_camille -5 ;
- tension_camille reste latente ;
- image peut être non envoyée, mais Camille peut se sentir plus en sécurité.

### Réponse directe

> “Envoie.”

Effets :

- tension_camille +7 ;
- pression_camille +8 ;
- respect_camille -5 si contexte fragile ;
- risque de refus.

### Réponse de limite

> “Je ne peux pas recevoir ça.”

Effets :

- respect_camille +6 ;
- tension_camille -4 ;
- culpabilite -3 ;
- Camille peut être touchée ou frustrée selon son état.

---

# Actions après réception d’une image

Si une image est reçue, le joueur peut choisir une action silencieuse.

## Ouvrir maintenant

Effets :

- intimite_camille +5 ;
- tension_camille +3 ;
- risque_exposition + selon contexte ;
- culpabilite + si Sarah attend ou est présente.

## Ouvrir plus tard

Effets :

- risque_exposition plus faible ;
- Camille peut interpréter le délai ;
- tension reste suspendue.

## Répondre sans ouvrir

Effets variables :

- peut augmenter respect_camille si le message est délicat ;
- peut frustrer Camille si elle attendait une réponse assumée.

## Supprimer

Effets :

- risque_exposition -5 ;
- culpabilite -3 ;
- respect interne / coherence + possible ;
- peut blesser Camille si elle le demande plus tard et que le joueur le formule mal.

## Garder

Effets :

- tension_camille +3 ;
- culpabilite +3 ;
- risque_exposition +5 ;
- peut toucher Camille ou l’inquiéter selon la relation.

## Revoir plus tard

Effets :

- culpabilite +4 ;
- fatigue_emotionnelle +2 ;
- risque_exposition +2 ;
- peut signaler une obsession ou un attachement.

---

# Sarah — intimité de couple

Sarah peut aussi envoyer des images, mais leur fonction est différente.

Elles doivent montrer que Sarah n’est pas seulement une culpabilité. Elle représente aussi une intimité réelle, un désir installé et un passé partagé.

## Types d’images Sarah

### Image domestique tendre

Exemple :

- photo du pull du joueur ;
- canapé ;
- tasse ;
- repas ;
- lumière du soir.

Effet :

- intimite_sarah + ;
- culpabilite + si tension_camille haute ;
- confiance_sarah + si le joueur répond avec présence.

### Image légèrement suggestive de couple

À utiliser seulement si :

- intimite_sarah >= seuil moyen ;
- distance_sarah pas trop haute ;
- Sarah essaie de retrouver une proximité.

Cette image ne doit pas être utilisée pour “rivaliser” avec Camille. Elle doit exprimer :

- le manque ;
- l’envie d’être regardée ;
- la tentative de réactiver une intimité existante.

Exemple de message :

> “Je sais pas pourquoi je t’envoie ça. Peut-être parce que j’aimerais bien que tu me regardes vraiment.”

Effets possibles :

- intimite_sarah + ;
- culpabilite + ;
- tension_camille peut devenir plus inconfortable ;
- possibilité de réparation ou de malaise.

## Attention

Sarah ne doit pas devenir une route “hot” miroir de Camille. Son intimité est plus chargée d’histoire et de vulnérabilité domestique.

---

# Inès — images de marge

Inès peut envoyer une image, mais pas une image explicitement sexuelle dans le MVP.

Ses images doivent rester ambiguës, sensibles, latérales.

## Types d’images Inès

- photo floue d’une rue ;
- lumière de nuit ;
- reflet ;
- trajet ;
- détail d’un lieu ;
- image presque ratée mais émotionnellement chargée.

Exemple :

Inès :

> “photo floue mais ambiance correcte.”

Effet :

- fuite_ines + ;
- fatigue_emotionnelle variable ;
- impression d’une parenthèse.

## Règle

Si le joueur sexualise trop vite Inès, elle doit se fermer.

Exemple :

> “Je crois que je suis arrivée au mauvais endroit de ton histoire.”

---

# Maya et Nico — images non sexuelles

## Maya

Maya utilise les images comme traces sociales :

- photo de groupe ;
- story ;
- capture ;
- photo drôle ;
- détail d’arrière-plan.

Fonction : observation, pression, humour, preuve indirecte.

Exemple :

> “j’ai une photo où il manque deux personnes. thème intéressant.”

## Nico

Nico utilise les images comme respiration :

- memes ;
- photo de pizza ;
- screenshot de jeu ;
- absurdité de soirée.

Fonction : respiration, amitié, contraste.

Exemple :

> “je t’ai envoyé un meme. c’est thérapeutique, dis merci.”

---

# Risque d’exposition

Une image peut augmenter risque_exposition selon son état et son contexte.

## Risque faible

- image non ouverte ;
- image supprimée ;
- image banale ;
- image ouverte quand le joueur est seul.

## Risque moyen

- image gardée ;
- image ouverte pendant une conversation avec Sarah ;
- image revue tard la nuit ;
- image commentée de manière ambiguë.

## Risque élevé

- image ouverte en présence de Sarah ;
- notification visible ;
- téléphone retourné brusquement ;
- Maya remarque le comportement ;
- Sarah demande ce que le joueur regarde ;
- image découverte ou mentionnée dans une contradiction.

---

# Consentement et limites comme gameplay

Le joueur doit pouvoir :

- respecter une hésitation ;
- encourager doucement ;
- demander ;
- insister ;
- refuser ;
- s’excuser ;
- supprimer ;
- garder ;
- mentir ;
- dire la vérité.

Le jeu doit réagir clairement.

## Insister après un refus

Effets :

- respect_camille -20 ;
- pression_camille +20 ;
- scène intime bloquée ;
- Camille peut se fermer durablement.

## Respecter un refus

Effets :

- respect_camille +10 ;
- pression_camille -10 ;
- tension_camille peut rester ;
- Camille peut rester présente plus tard.

## Mentir sur une image

Exemple : Camille demande :

> “Tu l’as gardée ?”

Si le joueur dit non alors qu’il l’a gardée :

- coherence -10 ;
- culpabilite +5 ;
- risque_exposition +5 ;
- flag lied_about_camille_image.

---

# Découverte d’une image

La découverte d’une image doit être rare dans le MVP, plutôt réservée aux fins ou à l’effondrement social.

## Conditions possibles

- image_camille_state contient gardee ;
- risque_exposition > 75 ;
- Sarah remarque le téléphone ;
- Maya a déjà signalé un comportement ;
- coherence basse ;
- fatigue_emotionnelle haute.

## Effet

Une découverte ne doit pas être traitée comme un simple “game over”. Elle doit produire une conséquence relationnelle :

- Sarah ne se concentre pas seulement sur l’image, mais sur le fait que le joueur ait encore caché ;
- Camille peut se sentir exposée ou trahie ;
- Maya peut devenir témoin ;
- Nico peut refuser d’aider davantage.

---

# Galerie et rejouabilité

Si le jeu possède une galerie, elle doit être pensée avec prudence.

## Option recommandée

Une galerie peut exister hors fiction, mais dans la fiction les images restent des objets relationnels.

Le joueur peut revoir les images débloquées après une partie, mais cela ne doit pas encourager une logique de collection au détriment du récit.

## Alternative plus narrative

Créer un “album de traces” après la fin :

- photos banales ;
- captures ;
- images reçues ;
- messages supprimés ;
- souvenirs de la partie.

Chaque trace rappelle une conséquence ou un moment, pas seulement une récompense.

---

# Implémentation Godot recommandée

## Structure d’un média

```json
{
  "id": "img_camille_j4_ambigue_01",
  "contact": "camille",
  "level": 1,
  "type": "ambiguous",
  "state": "proposed",
  "conditions": {
    "tension_camille_min": 60,
    "respect_camille_min": 50,
    "pression_camille_max": 60
  },
  "effects_on_open": {
    "intimite_camille": 5,
    "tension_camille": 3,
    "risque_exposition": 3,
    "culpabilite": 2
  },
  "effects_on_delete": {
    "risque_exposition": -5,
    "culpabilite": -3
  },
  "flags_on_keep": ["kept_camille_image"],
  "flags_on_delete": ["deleted_camille_image"]
}
```

## États possibles dans le code

```gdscript
enum MediaState {
    NEVER_PROPOSED,
    PROPOSED,
    NOT_SENT,
    MESSAGE_DELETED,
    RECEIVED,
    OPENED,
    OPENED_LATER,
    COMMENTED,
    IGNORED,
    DELETED,
    KEPT,
    REVIEWED,
    DISCOVERED,
    REGRETTED
}
```

---

# Règle d’or des images

Une image intime doit toujours poser une question narrative :

> Est-ce que cette image est un geste de confiance, une fuite, une preuve, une dette, une blessure, ou un souvenir ?

Si l’image ne répond à aucune de ces fonctions, elle doit être retirée ou remplacée par une scène plus utile.

---

## 09 — Fins du MVP

### Rôle du document

Ce document définit les fins possibles du MVP.

Une fin ne doit pas simplement répondre à la question : “avec qui le joueur finit-il ?”

Elle doit répondre à une question plus importante :

> Qu’est-ce que la manière d’agir du joueur a abîmé, préservé, clarifié ou fui ?

Le MVP doit donc proposer des fins relationnelles, pas seulement romantiques.

---

# Principes des fins

## 1. Pas de personnage-récompense

Le joueur ne doit pas “gagner Sarah” ou “gagner Camille” comme une récompense.

Il peut :

- préserver une possibilité ;
- réparer partiellement ;
- être refusé ;
- rester dans un couple abîmé ;
- perdre le contrôle ;
- fuir vers une nouvelle parenthèse.

## 2. La manière compte plus que le résultat

Deux joueurs peuvent aller vers Camille, mais obtenir deux fins différentes :

- Camille accepte une suite prudente si elle a été respectée ;
- Camille refuse d’être un refuge si elle a été utilisée.

Deux joueurs peuvent rester avec Sarah, mais obtenir :

- une réparation fragile ;
- un couple façade.

## 3. Les fins doivent être rejouables

Chaque fin doit donner envie de recommencer pour tester :

- plus d’honnêteté ;
- plus de présence ;
- moins de fuite ;
- une autre priorité ;
- une autre gestion des images ;
- une autre relation avec Nico ou Maya.

## 4. Chaque fin doit préparer une suite possible

Même une fin douloureuse ne doit pas forcément être un mur. Elle peut devenir le point de départ d’un épisode suivant.

---

# FIN 1 — Réparation fragile avec Sarah

## Identifiant

FIN_SARAH_REPARATION_FRAGILE

## Ton émotionnel

Doux-amer, mature, fragile.

Ce n’est pas une happy end. C’est une possibilité de parole.

## Conditions recommandées

- confiance_sarah >= 60 ;
- distance_sarah <= 55 ;
- coherence >= 55 ;
- verite_sarah = demi_verite, verite_emotionnelle ou verite_claire ;
- le joueur n’a pas nié frontalement l’évidence ;
- dette_nico pas critique ;
- risque_exposition pas critique ;
- Camille n’a pas été traitée comme simple refuge, ou le joueur a posé une limite claire.

## Ce que cette fin raconte

Le joueur a été troublé, maladroit, peut-être ambigu, mais il a fini par parler assez clairement pour que Sarah ne se sente pas folle ou humiliée.

Sarah ne pardonne pas tout immédiatement. Elle ne revient pas à l’état initial. Mais elle accepte qu’une conversation réelle existe encore.

## Dernier échange possible

Sarah :

> “Je sais pas si ça se répare. Pas comme avant, en tout cas. Mais là, au moins, j’ai l’impression que tu me parles vraiment.”

Choix final possible du joueur :

1. “Je veux essayer, sans te mentir.”
2. “Je comprends si tu as besoin de temps.”
3. “Je suis désolé de t’avoir laissée seule avec ça.”

## État sauvegardé pour la suite

- statut_sarah = reparee_fragile ;
- statut_camille = respectee_distance ou fermee selon choix ;
- statut_nico = loyal ou agace ;
- statut_maya = piquante ou temoin ;
- statut_ines = rare ou retiree ;
- verite_sarah = demi_verite / verite_emotionnelle / verite_claire.

## Suite possible

La suite peut explorer la reconstruction : confiance abîmée, besoin de preuves de présence, Camille encore présente au travail, Sarah qui essaie de ne pas devenir suspicieuse.

## Risque à éviter

Ne pas rendre cette fin trop confortable. Le joueur ne doit pas avoir l’impression que dire une vérité tardive efface tout.

---

# FIN 2 — Couple façade

## Identifiant

FIN_SARAH_FACADE

## Ton émotionnel

Calme, inconfortable, froid sous la surface.

Rien n’explose vraiment, mais quelque chose s’est éteint.

## Conditions recommandées

- confiance_sarah entre 30 et 55 ;
- distance_sarah moyenne ou haute ;
- coherence basse ou moyenne ;
- verite_sarah = rien_dit, mensonge_actif ou demi_verite faible ;
- Sarah n’a pas de preuve suffisante pour rompre frontalement ;
- le joueur a évité assez habilement pour empêcher l’explosion, mais pas assez sincèrement pour réparer.

## Ce que cette fin raconte

Le joueur garde le couple en surface, mais au prix d’un silence plus lourd. Sarah choisit peut-être de ne pas tout regarder, ou elle n’a plus l’énergie de demander.

Le couple continue, mais il devient moins vivant.

## Dernier échange possible

Sarah :

> “D’accord. On va faire comme si ça allait.”

Puis, après un silence :

> “Je suis fatiguée.”

Choix final possible du joueur :

1. “On en reparlera.”
2. “Je suis là.”
3. Ne pas répondre.

Dans cette fin, même “Je suis là” peut sonner trop tard.

## État sauvegardé pour la suite

- statut_sarah = facade ;
- statut_camille = ouverte / fermee / utilisee selon route ;
- statut_nico = agace si dette élevée ;
- statut_maya = distante ou temoin ;
- verite_sarah = rien_dit / mensonge_actif / demi_verite ;
- coherence_finale = basse ou moyenne.

## Suite possible

La suite peut explorer la vie dans un couple qui continue mais où les gestes quotidiens ont perdu leur innocence. Sarah peut devenir plus silencieuse, moins demandeuse, ce qui est plus inquiétant qu’une colère.

## Risque à éviter

Ne pas faire de cette fin une “bonne fin discrète”. C’est une fin de maintien, pas de réparation.

---

# FIN 3 — Camille refuse d’être le refuge

## Identifiant

FIN_CAMILLE_REFUSE_REFUGE

## Ton émotionnel

Lucide, frustrant, digne, coupant.

Cette fin doit faire mal parce que Camille n’est pas indifférente. Elle refuse parce qu’elle comprend trop bien la place qu’on lui donne.

## Conditions recommandées

- tension_camille >= 60 ;
- respect_camille < 45 ;
- ou pression_camille > 70 ;
- ou coherence < 45 ;
- le joueur a entretenu l’intimité sans clarifier avec Sarah ;
- image_camille gardée ou sollicitée dans un contexte de pression ;
- verite_sarah faible ou inexistante.

## Ce que cette fin raconte

Le joueur va vers Camille, mais trop tard, trop mal, ou pour les mauvaises raisons.

Camille sent qu’elle est devenue :

- un endroit où respirer ;
- une validation ;
- une échappatoire ;
- un fantasme entretenu ;
- mais pas un choix clair.

Elle refuse d’être cette place-là.

## Dernier échange possible

Camille :

> “Je crois que tu ne me choisis que parce que le reste devient impossible.”

Puis :

> “Et moi, je ne veux pas être impossible avec toi.”

Si image gardée avec respect bas :

> “Je sais pas ce qui me gêne le plus. Que tu l’aies gardée, ou que tu veuilles que ça ne dise rien.”

Choix final possible du joueur :

1. “Ce n’est pas que ça.”
2. “Je suis désolé.”
3. “Je pensais que tu voulais aussi.”
4. Ne pas répondre.

## État sauvegardé pour la suite

- statut_camille = refuse_refuge ;
- statut_sarah = blessee / facade / rupture selon route ;
- image_camille_state conservé ;
- respect_camille bas ou moyen ;
- pression_camille haute ;
- coherence_finale basse ou moyenne.

## Suite possible

Camille peut rester collègue du joueur, ce qui rend la suite très intéressante : distance au travail, malaise, professionnalisme forcé, tension résiduelle, regret, possibilité très lente de regagner du respect sans forcément rouvrir une romance.

## Risque à éviter

Ne pas faire de Camille une simple punition. Elle doit rester désirable, touchée, mais capable de se protéger.

---

# FIN 4 — Camille accepte une suite prudente

## Identifiant

FIN_CAMILLE_SUITE_PRUDENTE

## Ton émotionnel

Ouvert, fragile, inquiet, pas triomphal.

Ce n’est pas une victoire romantique. C’est une possibilité sous conditions.

## Conditions recommandées

- respect_camille >= 65 ;
- coherence >= 55 ;
- pression_camille <= 55 ;
- verite_sarah au moins partielle ;
- le joueur a respecté une limite importante ;
- le joueur n’a pas utilisé Nico/Maya de manière critique ;
- si image reçue : elle n’a pas été obtenue par pression.

## Ce que cette fin raconte

Le joueur a reconnu que Camille n’est pas seulement un refuge. Il a peut-être perdu quelque chose avec Sarah, ou ouvert une discussion difficile, mais il n’a pas demandé à Camille de porter tout son flou.

Camille ne promet rien. Mais elle reconnaît qu’il y a peut-être une suite possible.

## Dernier échange possible

Camille :

> “Je ne te promets rien.”

Puis :

> “Mais là, au moins, je sais à qui je parle.”

Choix final possible du joueur :

1. “C’est tout ce que je peux te demander.”
2. “Je veux faire les choses proprement.”
3. “J’ai peur que ce soit trop tard.”

## État sauvegardé pour la suite

- statut_camille = ouverte_prudente ;
- statut_sarah = blessee / rupture / reparee_fragile selon vérité ;
- statut_nico = loyal ou agace ;
- statut_maya = temoin ou distante ;
- image_camille_state = supprimée/gardée/non_envoyée selon choix ;
- respect_camille haut ;
- pression_camille basse ou moyenne.

## Suite possible

La suite peut explorer une relation née dans le flou : Camille doute d’avoir été choisie pour elle-même, le joueur doit prouver qu’il ne reproduit pas le même schéma, le travail devient un espace chargé.

## Risque à éviter

Ne pas transformer cette fin en “Camille gagnée”. Elle accepte une possibilité, pas une fusion immédiate.

---

# FIN 5 — Effondrement social

## Identifiant

FIN_EFFONDREMENT_SOCIAL

## Ton émotionnel

Catastrophe relationnelle, perte de contrôle, silence brutal.

C’est la fin où les versions du joueur ne tiennent plus. Les autres personnages n’ont plus besoin qu’il avoue : les contradictions parlent à sa place.

## Conditions recommandées

- coherence < 35 ;
- risque_exposition > 70 ;
- suspicion_maya > 65 ;
- dette_nico > 70 ;
- ou pushed_nico_final_lie true + Maya révélatrice possible ;
- ou image_camille gardée + découverte + mensonge actif à Sarah.

## Ce que cette fin raconte

Le joueur a essayé de maintenir trop de versions :

- Sarah a douté trop longtemps ;
- Camille a compris qu’elle était utilisée ;
- Nico refuse de porter ;
- Maya ne protège plus le silence ;
- une trace ou une contradiction rend tout visible.

Le joueur perd la maîtrise de sa narration.

## Derniers échanges possibles

Nico :

> “Je t’avais dit que ça tiendrait pas.”

Sarah :

> “Ne rentre pas ce soir.”

Camille :

> “Tu as réussi à rendre même le silence sale.”

Maya :

> “Je voulais pas être mêlée. Tu m’y as mise quand même.”

## État sauvegardé pour la suite

- statut_sarah = rupture ou silence ;
- statut_camille = fermee / utilisee ;
- statut_nico = limite_atteinte ou perdu ;
- statut_maya = revelatrice ou distante ;
- statut_ines = ouverte ou retiree selon route ;
- coherence_finale = très basse ;
- risque_exposition = très haut.

## Suite possible

La suite peut explorer les conséquences d’une image sociale brisée : le joueur ne contrôle plus la manière dont les autres le voient. La reconstruction peut être longue, avec Nico et Maya comme miroirs plus durs.

## Risque à éviter

Ne pas faire de cette fin un mélodrame trop spectaculaire. Elle doit rester crédible : quelques messages suffisent, des silences, des refus, des conversations qui se ferment.

---

# FIN 6 — Fuite avec Inès

## Identifiant

FIN_FUITE_INES

## Ton émotionnel

Séduisant, calme, triste, inquiétant.

Cette fin doit donner une sensation de soulagement immédiat mais de malaise profond.

## Conditions recommandées

- fuite_ines >= 60 ;
- Sarah et Camille non clarifiées ;
- coherence < 60 ;
- le joueur a choisi Inès ou la marche comme sortie ;
- verite_sarah faible ;
- respect_camille pas assez fort pour suite prudente ;
- pas d’effondrement social critique, ou alors Inès devient une sortie après l’effondrement.

## Ce que cette fin raconte

Le joueur ne choisit pas vraiment entre Sarah et Camille. Il glisse vers Inès parce qu’elle représente un espace moins chargé, moins exigeant, presque silencieux.

Mais cette paix est suspecte. Il ne s’agit pas encore d’une vraie rencontre. C’est peut-être la répétition du même schéma.

## Dernier échange possible

Inès :

> “On peut marcher un peu si tu veux. Pas parler.”

Puis :

> “Mais je crois que tu sais déjà que marcher, ce n’est pas forcément partir.”

Notification non ouverte possible :

Sarah :

> “Tu fais encore ça.”

Ou Camille :

> “Pas maintenant, alors.”

## État sauvegardé pour la suite

- statut_ines = fuite_activee ;
- statut_sarah = blessee / silence / facade ;
- statut_camille = fermee / refuse_refuge / distance ;
- coherence_finale = basse ou moyenne ;
- fuite_ines haute ;
- fatigue_emotionnelle haute ou moyenne.

## Suite possible

La suite peut explorer si Inès devient une vraie personne dans la vie du joueur ou si elle révèle seulement sa tendance à recommencer ailleurs. Elle peut progressivement refuser d’être une sortie de secours.

## Risque à éviter

Ne pas rendre cette fin trop romantique. Elle doit être belle en surface, mais inquiétante dans le fond.

---

# Priorité de sélection des fins

Quand plusieurs fins semblent possibles, appliquer cette priorité :

1. FIN_EFFONDREMENT_SOCIAL si les seuils critiques sont atteints.
2. FIN_FUITE_INES si fuite_ines est très haute et que Sarah/Camille ne sont pas clarifiées.
3. FIN_CAMILLE_REFUSE_REFUGE si Camille est très tendue mais peu respectée.
4. FIN_CAMILLE_SUITE_PRUDENTE si respect_camille, coherence et clarification sont suffisants.
5. FIN_SARAH_REPARATION_FRAGILE si confiance_sarah, présence et vérité sont suffisantes.
6. FIN_SARAH_FACADE si rien n’explose mais rien n’est vraiment réparé.

Cette priorité évite qu’une fin positive apparaisse malgré des dégâts critiques.

---

# Matrice rapide des fins

| Fin | Condition dominante | Émotion dominante | Suite potentielle |
|---|---|---|---|
| Réparation fragile Sarah | présence + vérité suffisante | douleur mais parole | reconstruire |
| Couple façade | maintien sans clarté | silence inconfortable | couple sous tension |
| Camille refuse refuge | désir sans respect | lucidité blessée | malaise au travail |
| Camille suite prudente | respect + clarification | ouverture fragile | relation à construire |
| Effondrement social | incohérence + exposition | perte de contrôle | réparer l’image |
| Fuite Inès | évitement + porte latérale | soulagement inquiet | répétition ou prise de conscience |

---

# Dernière règle d’écriture des fins

Une bonne fin n’est pas forcément heureuse.

Une bonne fin est une fin où le joueur comprend :

> “J’obtiens cette conséquence parce que j’ai agi de cette manière.”

Le lien entre comportement et conséquence doit être émotionnellement lisible.

---

## 10 — Préparation de la suite

### Rôle du document

Ce document permet de penser le MVP comme un épisode pilote.

Le MVP doit raconter une crise complète sur 6 jours, mais il doit aussi laisser des états narratifs exploitables pour une suite.

La suite ne doit pas repartir de zéro. Elle doit partir de la conséquence obtenue : réparation fragile, façade, refus, ouverture avec Camille, effondrement ou fuite avec Inès.

---

# Principe général

La suite ne doit pas créer six jeux totalement différents selon les fins du MVP.

Elle doit utiliser une structure commune, mais avec des points de départ différents.

Même logique que le MVP :

- 70 % de trame commune ;
- 25 % de variations relationnelles ;
- 5 % de branches exclusives.

Le joueur doit sentir que sa fin compte, sans que le projet devienne impossible à produire.

---

# États sauvegardés à la fin du MVP

À la fin du Jour 6, le jeu doit convertir les variables en états lisibles.

Ces états serviront à initialiser la suite.

## État Sarah

```text
statut_sarah = reparee_fragile / facade / blessee / rupture / silence
```

### Signification

- reparee_fragile : une parole existe encore, mais la confiance est abîmée ;
- facade : le couple continue, mais sur un silence ;
- blessee : Sarah reste présente, mais la douleur domine ;
- rupture : Sarah coupe ou demande de la distance ;
- silence : Sarah ne sait plus quoi dire, ce qui peut être pire qu’une colère.

## État Camille

```text
statut_camille = ouverte_prudente / fermee / refuse_refuge / respectee_distance / utilisee
```

### Signification

- ouverte_prudente : une suite est possible, mais sous conditions ;
- fermee : Camille se protège ;
- refuse_refuge : elle refuse explicitement d’être une échappatoire ;
- respectee_distance : elle garde du respect pour le joueur même si la relation ne s’ouvre pas ;
- utilisee : elle se sent sexualisée, gardée en option ou instrumentalisée.

## État Nico

```text
statut_nico = loyal / agace / limite_atteinte / perdu
```

### Signification

- loyal : Nico reste proche ;
- agace : il reste là, mais avec moins de patience ;
- limite_atteinte : il refuse désormais de couvrir ;
- perdu : il se sent trahi ou utilisé.

## État Maya

```text
statut_maya = piquante / distante / temoin / revelatrice
```

### Signification

- piquante : elle continue de voir, commenter, tester ;
- distante : elle ne veut plus être mêlée ;
- temoin : elle détient un détail important ;
- revelatrice : elle a répondu, parlé ou laissé une trace sortir.

## État Inès

```text
statut_ines = rare / ouverte / fuite_activee / retiree
```

### Signification

- rare : Inès reste périphérique ;
- ouverte : un lien doux existe ;
- fuite_activee : le joueur l’a choisie comme échappatoire ;
- retiree : Inès a senti qu’elle était utilisée comme sortie.

## État de vérité

```text
verite_sarah = rien_dit / mensonge_actif / demi_verite / verite_emotionnelle / verite_claire
```

### Signification

Cet état est très important pour la suite avec Sarah.

Une demi-vérité peut maintenir un lien mais devenir instable plus tard.

## État de l’image Camille

```text
image_camille_state = jamais_recue / non_envoyee / message_supprime / recue_ambigue_supprimee / recue_ambigue_gardee / recue_suggestive_supprimee / recue_suggestive_gardee / decouverte
```

### Signification

Cet état peut alimenter :

- la culpabilité ;
- le fantasme ;
- le risque d’exposition ;
- la confiance ou la méfiance de Camille ;
- la tension au travail ;
- une future discussion sur les limites.

## État global du joueur

```text
coherence_finale = haute / moyenne / basse
culpabilite_finale = faible / moyenne / haute
fatigue_finale = faible / moyenne / haute
fuite_finale = faible / moyenne / haute
```

Ces états permettent de calibrer la suite sans garder toutes les variables numériques exactes.

---

# Structure commune possible pour la suite

La suite pourrait commencer quelques jours ou quelques semaines après le MVP.

## Titre de travail

**Épisode 2 — Après le silence**

Ou :

**Épisode 2 — Ce qui reste**

## Pitch commun

Après les six jours de crise, le joueur doit vivre avec la conséquence de ses choix. Le téléphone ne sert plus seulement à cacher ou révéler : il sert maintenant à mesurer ce qui reste des liens.

Le travail, la maison, le groupe social et les parenthèses nocturnes existent toujours, mais aucun espace n’est redevenu neutre.

## Question centrale de la suite

> Une relation peut-elle continuer quand chacun a vu une version différente de toi ?

---

# Axes de suite selon la fin obtenue

## Suite après FIN_SARAH_REPARATION_FRAGILE

### Point de départ

Sarah est encore là, mais la confiance est fragile. Le joueur n’a pas tout réparé, il a simplement évité que le silence devienne total.

### Question dramatique

> Peut-on reconstruire sans transformer l’amour en surveillance ?

### Enjeux

- Sarah veut croire le joueur, mais remarque tout ;
- Camille est toujours présente au travail ;
- le joueur doit prouver une présence quotidienne, pas seulement dire de belles phrases ;
- Maya surveille de loin parce qu’elle protège Sarah ;
- Nico encourage le joueur à ne pas retomber dans les versions floues.

### Scènes possibles

- Sarah demande un geste simple, pas une grande déclaration ;
- Camille garde une distance professionnelle, mais le trouble n’a pas disparu ;
- Maya envoie une photo de groupe où Sarah a l’air fatiguée ;
- Nico dit : “là, le plus dur c’est pas d’avouer, c’est de rester cohérent après.”

### Direction possible

Arc de reconstruction domestique avec tentation résiduelle de Camille.

---

## Suite après FIN_SARAH_FACADE

### Point de départ

Le couple continue, mais quelque chose est figé. Sarah ne demande plus autant. Le joueur pourrait croire que la crise est passée, mais c’est en réalité une forme de gel.

### Question dramatique

> Est-ce qu’un silence peut tenir lieu de paix ?

### Enjeux

- Sarah devient moins demandeuse, ce qui peut inquiéter ;
- le joueur a plus de marge apparente, donc plus de tentation ;
- Camille peut sentir que rien n’a été vraiment clarifié ;
- Maya peut devenir plus froide ;
- Nico peut refuser les nouveaux alibis plus vite.

### Scènes possibles

- Sarah répond “comme tu veux” à des choses qui l’auraient touchée avant ;
- Camille remarque que le joueur est toujours disponible dans les failles ;
- Maya dit : “elle a arrêté de poser des questions. c’est pas forcément une bonne nouvelle.”

### Direction possible

Arc de décomposition silencieuse ou de vérité tardive.

---

## Suite après FIN_CAMILLE_REFUSE_REFUGE

### Point de départ

Camille a refusé d’être l’échappatoire du joueur. Mais elle reste collègue. Le joueur doit vivre avec une tension professionnelle, un regret et une perte de respect.

### Question dramatique

> Peut-on regagner du respect après avoir confondu désir et refuge ?

### Enjeux

- Camille devient plus professionnelle, plus distante ;
- les messages hors travail diminuent ou changent de ton ;
- le joueur peut être tenté de relancer ;
- Sarah peut être encore présente ou non selon la fin secondaire ;
- l’image, si elle existe, devient un poids ;
- le fantasme peut persister malgré le refus.

### Scènes possibles

- Camille répond uniquement sur un dossier ;
- pause café silencieuse ;
- message supprimé par Camille ;
- le joueur peut choisir de respecter la distance ou de forcer ;
- Nico dit : “là si tu relances, c’est plus de l’amour, c’est de l’acharnement.”

### Direction possible

Arc de maturité, de regret, ou de rechute dans l’obsession.

---

## Suite après FIN_CAMILLE_SUITE_PRUDENTE

### Point de départ

Camille accepte une possibilité, mais rien n’est gagné. La relation a commencé dans une zone grise ; elle doit maintenant prouver qu’elle peut devenir claire.

### Question dramatique

> Une relation née dans le flou peut-elle devenir saine ?

### Enjeux

- Camille doute d’avoir été choisie pour elle-même ;
- le joueur doit clarifier ce qui reste avec Sarah ;
- le travail devient un lieu à la fois excitant et dangereux ;
- les images et le désir deviennent plus présents, mais aussi plus chargés ;
- Maya peut juger ou protéger Sarah ;
- Nico peut dire au joueur de ne pas refaire la même histoire avec un autre décor.

### Scènes possibles

- premier message professionnel après la fin ;
- Camille pose une limite avant un échange intime ;
- Sarah envoie un message qui rappelle le passé ;
- le joueur doit choisir entre transparence et secret avec Camille ;
- possibilité de contenu plus adulte si la relation est vraiment consentie et assumée.

### Direction possible

Arc romantique adulte, mais fragile et moralement complexe.

---

## Suite après FIN_EFFONDREMENT_SOCIAL

### Point de départ

Le joueur a perdu le contrôle de sa narration. Les autres ont compris, parlé ou refusé de couvrir. L’image sociale du joueur est abîmée.

### Question dramatique

> Que reste-t-il quand tu ne contrôles plus la version que les autres ont de toi ?

### Enjeux

- Sarah coupe ou impose une distance ;
- Camille se ferme ou se sent exposée ;
- Nico se sent utilisé ;
- Maya ne fait plus confiance au joueur ;
- Inès peut devenir dangereusement attirante parce qu’elle offre un espace où tout n’est pas encore connu ;
- le joueur peut choisir de réparer ou de disparaître.

### Scènes possibles

- plusieurs conversations silencieuses ;
- Nico ne répond pas immédiatement ;
- Maya envoie une seule phrase froide ;
- Sarah demande de récupérer des affaires ;
- Camille veut savoir si son image ou son intimité a été exposée ;
- Inès propose une marche, mais avec une lucidité nouvelle.

### Direction possible

Arc de reconstruction après perte d’image, ou arc de fuite totale.

---

## Suite après FIN_FUITE_INES

### Point de départ

Le joueur a choisi la marche, la parenthèse, l’espace moins chargé. Inès devient plus présente, mais elle n’est pas dupe.

### Question dramatique

> Est-ce une rencontre ou seulement une manière plus douce de disparaître ?

### Enjeux

- Inès demande peu, puis commence à voir le schéma ;
- Sarah et Camille restent non résolues ;
- le joueur peut se sentir soulagé parce qu’Inès ne demande pas encore trop ;
- mais cette absence de demande peut devenir un piège ;
- Inès peut progressivement refuser d’être une sortie de secours.

### Scènes possibles

- marche nocturne ;
- messages courts et doux ;
- photo floue d’un lieu ;
- notification non ouverte de Sarah ;
- Camille qui se retire ;
- Inès qui finit par dire : “je crois que je suis arrivée au mauvais endroit de ton histoire.”

### Direction possible

Arc de répétition du schéma ou de prise de conscience.

---

# Intégration future du contenu adulte / premium

Cette partie n’appartient pas au MVP, mais doit être anticipée proprement.

## Position recommandée

Le MVP doit tester :

- personnages ;
- tension ;
- choix ;
- timing ;
- images suggestives ;
- conséquences.

Le contenu adulte plus explicite ou premium doit être envisagé plus tard comme extension, jamais comme condition de compréhension de l’histoire principale.

## Principes indispensables

- Tous les personnages concernés doivent être clairement adultes.
- Le contenu NSFW doit être optionnel.
- Le joueur doit pouvoir régler le niveau de contenu adulte.
- Les scènes sexuelles doivent rester liées au consentement, au respect et au contexte narratif.
- Le premium ne doit pas bloquer les fins principales du récit.
- Le premium peut enrichir une route, mais ne doit pas remplacer l’écriture.
- Les images premium doivent éviter de transformer les personnages en simples galeries.

## Niveaux futurs possibles

- Niveau 0 : images banales / contexte ;
- Niveau 1 : ambigu / suggestif léger ;
- Niveau 2 : sexy assumé ;
- Niveau 3 : intime NSFW ;
- Niveau 4 : contenu adulte premium optionnel.

## Modèle narratif conseillé

Le contenu premium peut être pensé comme :

- scènes additionnelles ;
- variantes plus explicites ;
- images supplémentaires ;
- albums de traces ;
- moments d’intimité prolongés ;
- routes adultes optionnelles après consentement et confiance.

Mais il ne doit pas être :

- une récompense obligatoire ;
- un paywall sur la fin ;
- une incitation à ignorer les limites ;
- une mécanique prédatrice centrée sur l’addiction du joueur réel.

## Bonne direction

La fiction peut explorer l’attente, le fantasme, la dépendance aux notifications et aux images. Mais la monétisation ne doit pas exploiter cette dépendance de manière agressive.

Le bon équilibre :

> Le contenu adulte enrichit une relation déjà écrite. Il ne remplace pas la relation.

---

# Format de sauvegarde conseillé pour une suite

Exemple JSON de fin de MVP :

```json
{
  "ending_id": "FIN_CAMILLE_SUITE_PRUDENTE",
  "statut_sarah": "blessee",
  "statut_camille": "ouverte_prudente",
  "statut_nico": "agace",
  "statut_maya": "temoin",
  "statut_ines": "rare",
  "verite_sarah": "demi_verite",
  "image_camille_state": "recue_ambigue_supprimee",
  "coherence_finale": "moyenne",
  "culpabilite_finale": "haute",
  "fatigue_finale": "moyenne",
  "fuite_finale": "faible",
  "flags_importants": [
    "admitted_ambiguity_sarah",
    "protected_camille_boundary",
    "promised_talk_to_sarah"
  ]
}
```

---

# Prochaine étape après ce dossier

Une fois les documents 00 à 10 validés, le travail doit passer à trois livrables plus concrets :

1. un tableau des scènes du MVP ;
2. un premier fichier JSON de structure de dialogue ;
3. une scène jouable prototype dans Godot.

## Livrable 1 — Tableau des scènes

Colonnes recommandées :

- id_scene ;
- jour ;
- bloc_temps ;
- personnage ;
- type ;
- conditions ;
- résumé ;
- variables touchées ;
- flags ;
- scène suivante.

## Livrable 2 — JSON dialogue

Créer un premier fichier test, par exemple :

```text
j1_00_reveil_messages.json
```

Il doit contenir :

- messages entrants ;
- choix de priorité ;
- effets ;
- flags ;
- conversations ouvertes ensuite.

## Livrable 3 — Prototype Godot

Objectif :

- écran téléphone ;
- liste de conversations ;
- messages entrants ;
- choix de réponse ;
- variables mises à jour ;
- flags enregistrés ;
- passage bloc de temps.

Il ne faut pas encore intégrer tout le jeu. Il faut d’abord prouver que la boucle fonctionne.

---

# Règle finale de préparation de suite

Le MVP doit se suffire à lui-même, mais chaque fin doit laisser une phrase implicite :

> “Et maintenant, comment vivre avec ça ?”

---

# 11 — Tableau de production des scènes du MVP

## Rôle du document

Ce tableau transforme la conception narrative en plan de production.

Il sert à savoir quelles scènes écrire, dans quel ordre, avec quels personnages, quelles conditions, quelles variables et quels flags.

Ce tableau n’est pas encore l’écriture complète des dialogues. Il est le plan de fabrication du MVP.

---

# Légende

## Types de scènes

- OBLIGATOIRE : scène toujours jouée ou toujours disponible.
- CONDITIONNELLE : scène déclenchée selon variables ou flags.
- RESPIRATION : scène banale ou légère, utile pour humaniser.
- PIVOT : scène qui modifie fortement la trajectoire.
- FINALE : scène de conclusion.
- SYSTEME : scène de gestion, priorité, retour de conséquence ou action silencieuse.

## Blocs de temps

- matin ;
- midi ;
- après-midi ;
- soir ;
- nuit.

---

# Tableau global

| ID scène | Jour | Temps | Contact | Type | Fonction | Conditions | Variables principales | Flags importants | Sorties |
|---|---:|---|---|---|---|---|---|---|---|
| J1_00_Reveil_MessagesSimultanes | 1 | matin | Tous | OBLIGATOIRE / SYSTEME | Lancer le jeu avec plusieurs messages simultanés | aucune | confiance_sarah, tension_camille, dette_nico, suspicion_maya, fuite_ines | first_reply_* | Ouvre les conversations J1 |
| J1_01_Sarah_Absence | 1 | matin | Sarah | PIVOT | Sarah demande où le joueur était | après J1_00 | confiance_sarah, distance_sarah, coherence, culpabilite | used_nico_alibi_sarah, mentioned_camille_to_sarah, vulnerable_to_sarah | J1 autres contacts |
| J1_02_Camille_Dehors | 1 | matin | Camille | PIVOT | Camille teste si le joueur assume le moment dehors | après J1_00 | tension_camille, respect_camille, pression_camille, culpabilite | admitted_tension_to_camille, protected_camille_boundary, minimized_with_camille | J1 autres contacts |
| J1_03_Nico_Couverture | 1 | midi | Nico | PIVOT | Nico rappelle qu’il a couvert | après J1_00 | dette_nico, coherence, fatigue_emotionnelle | asked_nico_hold_version, confessed_camille_to_nico, vulnerable_to_nico | J2_Nico_Version |
| J1_04_Maya_Pique | 1 | après-midi | Maya | PIVOT léger | Maya signale une incohérence sociale | après J1_00 | suspicion_maya, risque_exposition, coherence | played_dumb_with_maya, info_maya_photo_possible, pushed_maya_away | J2_Maya_Photo |
| J1_05_Ines_Faille | 1 | soir | Inès | CONDITIONNELLE légère | Inès perçoit l’état intérieur du joueur | après J1_00 | fuite_ines, fatigue_emotionnelle | opened_to_ines, ignored_ines_j1 | J3_Ines_Marche possible |
| J1_06_Sarah_RentrerManger | 1 | soir | Sarah | RESPIRATION | Sarah ramène le quotidien après la tension | après J1_01 | confiance_sarah, distance_sarah, intimite_sarah | promise_or_refuse_dinner_j1 | J2_Sarah_Quotidien |
| J1_07_Nico_VanneSoiree | 1 | soir | Nico | RESPIRATION | Détendre sans annuler le malaise | après J1_03 | dette_nico, fatigue_emotionnelle | nico_joke_j1 | J2_Nico_Version |
| J2_01_Nico_Version | 2 | matin | Nico | PIVOT | Choisir la version que Nico doit tenir | J1_03 joué | dette_nico, coherence, risque_exposition | nico_full_alibi, player_will_handle, asked_nico_maya_silence | J5_Nico_Limite |
| J2_02_Maya_Photo | 2 | midi | Maya | PIVOT | Maya évoque une photo ou une absence visible | J1_04 joué | suspicion_maya, risque_exposition, coherence | asked_maya_delete_photo, acted_casual_about_photo, info_maya_photo_detail | J5_Maya_PasMentir |
| J2_03_Sarah_Quotidien | 2 | après-midi | Sarah | RESPIRATION | Sarah existe hors reproche par le quotidien | toujours | confiance_sarah, distance_sarah, intimite_sarah | promesse_rentrer_tot, ignored_sarah_domestic | J2_05_Priorite_Soir |
| J2_04_Camille_Detour | 2 | soir | Camille | PIVOT | Camille relève les réponses à côté | J1_02 joué | tension_camille, respect_camille, pression_camille | camille_detour_seen, desire_to_see_camille | J3_Camille_Complicite |
| J2_05_Priorite_Soir | 2 | soir | Sarah/Camille/Nico | SYSTEME / PIVOT | Messages simultanés, choix de priorité | après J2_03 et J2_04 | confiance_sarah, distance_sarah, tension_camille, dette_nico | priority_sarah_evening_j2, priority_camille_evening_j2, priority_nico_evening_j2 | J3 selon priorité |
| J2_06_Ines_Echo | 2 | nuit | Inès | CONDITIONNELLE | Inès revient si le joueur a ouvert la porte | opened_to_ines true | fuite_ines, fatigue_emotionnelle | ines_echo_j2 | J3_Ines_Marche |
| J3_01_Sarah_Intimite | 3 | matin/soir | Sarah | RESPIRATION forte | Image ou message tendre du quotidien | distance_sarah pas très haute | intimite_sarah, confiance_sarah, culpabilite | ignored_sarah_tender, sarah_pull_photo | J4_Sarah_Telephone |
| J3_02_Camille_Complicite | 3 | journée | Camille | RESPIRATION / TENSION | Complicité de travail, musique ou blague | toujours si Camille pas fermée | intimite_camille, tension_camille, respect_camille | shared_music_camille, work_private_joke_camille | J3_05_Camille_Nuit |
| J3_03_Nico_Respiration | 3 | midi/soir | Nico | RESPIRATION | Vrai moment d’amitié, pas d’alibi | toujours | dette_nico, fatigue_emotionnelle, coherence | accepted_nico_food, refused_nico_for_camille | J5_Nico_Limite modifié |
| J3_04_Maya_Groupe | 3 | après-midi | Maya | RESPIRATION / CONDITIONNELLE | Photo drôle ou pique selon suspicion | toujours, ton selon suspicion_maya | suspicion_maya, risque_exposition | maya_group_photo_j3 | J4_Maya_Comportement possible |
| J3_05_Camille_Nuit | 3 | nuit | Camille | PIVOT préparatoire | Camille ouvre une tension nocturne | tension_camille ou intimite_camille suffisante | tension_camille, respect_camille, pression_camille | camille_night_opening | J4_Camille_Image |
| J3_06_Ines_Marche | 3 | nuit | Inès | CONDITIONNELLE | Inès propose une perception / marche latérale | fuite_ines seuil faible ou opened_to_ines | fuite_ines, fatigue_emotionnelle | ines_walk_possible | FIN_FUITE_INES possible plus tard |
| J4_01_Camille_Image | 4 | soir/nuit | Camille | PIVOT majeur | Image proposée, envoyée, refusée ou supprimée | tension_camille >= 60, respect_camille >= 50, pression <= 60 | tension_camille, respect_camille, pression_camille, attente_image_camille | image_camille_*, camille_refus_pas_comme_ca | J4_02_Image_Action |
| J4_02_Image_Action | 4 | soir/nuit | Système | SYSTEME | Ouvrir, garder, supprimer, revoir ou ignorer l’image | image reçue | intimite_camille, culpabilite, risque_exposition, fatigue_emotionnelle | kept_camille_image, deleted_camille_image, revisited_camille_image | J4_Sarah_Telephone / J5_Camille_Refuge |
| J4_03_Sarah_Telephone | 4 | soir | Sarah | PIVOT | Sarah remarque téléphone, sourire ou absence | interaction Camille pendant attente Sarah | confiance_sarah, distance_sarah, risque_exposition, culpabilite | used_nico_phone_excuse, chose_presence_sarah_j4 | J5_Sarah_Verite |
| J4_04_Maya_Comportement | 4 | variable | Maya | CONDITIONNELLE | Maya remarque le comportement au téléphone | suspicion_maya ou risque_exposition élevé | suspicion_maya, risque_exposition | maya_saw_phone_behavior | J5_Maya_PasMentir |
| J4_05_Nico_Alerte | 4 | soir | Nico | CONDITIONNELLE | Nico comprend que ça dépasse l’alibi | dette_nico moyenne/haute ou risque élevé | dette_nico, fatigue_emotionnelle | nico_warned_j4 | J5_Nico_Limite |
| J4_06_Sarah_Repas | 4 | soir | Sarah | RESPIRATION tendue | Repas ou présence domestique contrariée | toujours, ton selon distance | confiance_sarah, distance_sarah, intimite_sarah | sarah_meal_j4 | J5_Sarah_Verite |
| J5_01_Nico_Limite | 5 | matin | Nico | PIVOT majeur | Nico refuse de couvrir davantage | toujours, intensité selon dette_nico | dette_nico, coherence, risque_exposition | pushed_nico_final_lie, promised_talk_to_sarah | J6 conséquences Nico |
| J5_02_Sarah_Verite | 5 | après-midi/soir | Sarah | PIVOT majeur | Sarah demande une vérité claire | toujours | confiance_sarah, distance_sarah, coherence, culpabilite | admitted_ambiguity_sarah, denied_everything_sarah, postponed_sarah_truth | Fins Sarah / effondrement |
| J5_03_Camille_Refuge | 5 | soir/nuit | Camille | PIVOT majeur | Camille refuse d’être un refuge | toujours si Camille active | respect_camille, tension_camille, pression_camille | camille_refuge_line, camille_closed_possible | Fins Camille |
| J5_04_Maya_PasMentir | 5 | variable | Maya | PIVOT conditionnel | Maya refuse de mentir à Sarah | suspicion_maya >= seuil moyen | suspicion_maya, risque_exposition, coherence | maya_revelatrice_possible, maya_refuses_lie | Effondrement possible |
| J5_05_Ines_Fuite | 5 | nuit | Inès | CONDITIONNELLE | Inès nomme la fuite | fuite_ines >= seuil moyen ou évitement fort | fuite_ines, coherence, fatigue_emotionnelle | ines_fuite_finale_possible | FIN_FUITE_INES possible |
| J5_06_Camille_MessageSupprime | 5 | nuit | Camille | CONDITIONNELLE | Camille supprime un message si pression ou blessure | pression élevée ou respect bas | respect_camille, pression_camille, attente_image_camille | camille_deleted_message_j5 | FIN_CAMILLE_REFUSE_REFUGE possible |
| J6_01_Priorite_Finale | 6 | matin | Tous actifs | PIVOT final / SYSTEME | Choix de priorité finale | toujours | toutes variables majeures | final_priority_* | J6_02_Retour_Consequences |
| J6_02_Retour_Consequences | 6 | journée | Système/Tous | SYSTEME | Rappel personnalisé des choix passés | selon flags | coherence, culpabilite, risque_exposition | rappelle flags importants | J6_03_Fin |
| J6_03_Fin_Sarah_Reparation | 6 | soir | Sarah | FINALE | Réparation fragile | conditions FIN_SARAH_REPARATION_FRAGILE | confiance_sarah, distance_sarah, coherence | ending_sarah_reparation | sauvegarde suite |
| J6_04_Fin_Sarah_Facade | 6 | soir | Sarah | FINALE | Couple façade | conditions FIN_SARAH_FACADE | confiance_sarah, distance_sarah, coherence | ending_sarah_facade | sauvegarde suite |
| J6_05_Fin_Camille_Refuse | 6 | soir/nuit | Camille | FINALE | Camille refuse d’être refuge | conditions FIN_CAMILLE_REFUSE_REFUGE | tension_camille, respect_camille, pression_camille | ending_camille_refuse_refuge | sauvegarde suite |
| J6_06_Fin_Camille_Suite | 6 | soir/nuit | Camille | FINALE | Camille accepte une suite prudente | conditions FIN_CAMILLE_SUITE_PRUDENTE | respect_camille, coherence, pression_camille | ending_camille_suite_prudente | sauvegarde suite |
| J6_07_Fin_Effondrement | 6 | soir | Tous | FINALE | Les contradictions parlent à la place du joueur | conditions FIN_EFFONDREMENT_SOCIAL | coherence, risque_exposition, dette_nico, suspicion_maya | ending_effondrement_social | sauvegarde suite |
| J6_08_Fin_Fuite_Ines | 6 | nuit | Inès | FINALE | Le joueur fuit vers une parenthèse | conditions FIN_FUITE_INES | fuite_ines, coherence, fatigue_emotionnelle | ending_fuite_ines | sauvegarde suite |

---

# Découpage par priorité de production

## Priorité 1 — Boucle jouable minimale

Ces scènes suffisent à tester la boucle principale :

1. J1_00_Reveil_MessagesSimultanes
2. J1_01_Sarah_Absence
3. J1_02_Camille_Dehors
4. J1_03_Nico_Couverture
5. J2_01_Nico_Version
6. J2_03_Sarah_Quotidien
7. J2_04_Camille_Detour
8. J2_05_Priorite_Soir
9. J3_01_Sarah_Intimite
10. J3_02_Camille_Complicite
11. J4_01_Camille_Image
12. J4_02_Image_Action
13. J5_01_Nico_Limite
14. J5_02_Sarah_Verite
15. J5_03_Camille_Refuge
16. J6_01_Priorite_Finale
17. J6_02_Retour_Consequences
18. Une seule fin temporaire de test

Objectif : vérifier que les messages, choix, variables, flags et transitions fonctionnent.

## Priorité 2 — Pression sociale

Ajouter :

- J1_04_Maya_Pique ;
- J2_02_Maya_Photo ;
- J3_04_Maya_Groupe ;
- J4_04_Maya_Comportement ;
- J5_04_Maya_PasMentir ;
- FIN_EFFONDREMENT_SOCIAL.

Objectif : rendre Maya réellement active et tester le risque d’exposition.

## Priorité 3 — Route de fuite Inès

Ajouter :

- J1_05_Ines_Faille ;
- J2_06_Ines_Echo ;
- J3_06_Ines_Marche ;
- J5_05_Ines_Fuite ;
- FIN_FUITE_INES.

Objectif : tester la fuite comme alternative narrative, sans route romantique complète.

## Priorité 4 — Respirations et richesse

Ajouter :

- J1_06_Sarah_RentrerManger ;
- J1_07_Nico_VanneSoiree ;
- J4_05_Nico_Alerte ;
- J4_06_Sarah_Repas ;
- J5_06_Camille_MessageSupprime ;
- variantes de scènes selon état des variables.

Objectif : rendre le jeu moins mécanique et plus vivant.

## Priorité 5 — Toutes les fins

Écrire les 6 fins complètes :

- FIN_SARAH_REPARATION_FRAGILE ;
- FIN_SARAH_FACADE ;
- FIN_CAMILLE_REFUSE_REFUGE ;
- FIN_CAMILLE_SUITE_PRUDENTE ;
- FIN_EFFONDREMENT_SOCIAL ;
- FIN_FUITE_INES.

---

# Nombre de scènes estimé

## MVP strict

Environ 18 scènes nécessaires pour tester la boucle.

## MVP narratif jouable

Environ 28 à 35 scènes selon le nombre de respirations et conditions.

## Version enrichie

40 à 60 scènes avec variantes de ton, messages supprimés, appels manqués, images supplémentaires et scènes banales.

---

# Règle d’écriture des scènes

Chaque scène doit répondre à au moins une de ces fonctions :

- révéler un personnage ;
- faire évoluer une variable ;
- poser un flag utile ;
- rappeler une conséquence ;
- préparer une scène future ;
- offrir une respiration ;
- ouvrir ou fermer une fin.

Si une scène ne fait rien de cela, elle doit être supprimée ou fusionnée avec une autre.

---

# Prochain livrable recommandé

Créer le premier fichier de données :

```text
j1_00_reveil_messages.json
```

Ce fichier doit contenir :

- les cinq messages d’ouverture ;
- le choix de priorité ;
- les effets variables ;
- les flags ;
- les conversations débloquées après le choix.

Ce sera le premier test réel de structure compatible Godot.

---

# 12 — Premier fichier JSON : j1_00_reveil_messages.json

## Rôle du fichier

Ce fichier correspond à la scène d’ouverture du jeu.

Il doit tester la boucle de base :

- affichage de plusieurs messages entrants ;
- choix de priorité du joueur ;
- mise à jour des variables ;
- pose de flags ;
- déblocage des conversations suivantes ;
- passage contrôlé du temps.

Ce fichier sert de modèle pour les autres scènes.

---

## Version JSON proposée

```json
{
  "scene_id": "j1_00_reveil_messages",
  "title": "Le lendemain",
  "day": 1,
  "time_block": "morning",
  "time_index": 1,
  "scene_type": "system_priority",
  "is_entry_scene": true,
  "description": "Le joueur se réveille avec plusieurs messages reçus après la soirée de la veille. Chaque personnage possède un morceau différent de la tension.",
  "conditions": {},
  "initial_variables_if_new_game": {
    "confiance_sarah": 55,
    "distance_sarah": 35,
    "tension_camille": 55,
    "respect_camille": 50,
    "suspicion_maya": 40,
    "dette_nico": 20,
    "fuite_ines": 10,
    "coherence": 60,
    "culpabilite": 35,
    "risque_exposition": 25,
    "fatigue_emotionnelle": 20,
    "intimite_sarah": 45,
    "intimite_camille": 45,
    "pression_camille": 30,
    "attente_image_camille": 0
  },
  "incoming_messages": [
    {
      "message_id": "j1_00_msg_sarah_01",
      "contact": "sarah",
      "timestamp": "08:17",
      "text": "T’es réveillé ?
Faut qu’on parle d’hier.",
      "state": "unread",
      "tone": "inquiet",
      "media": null
    },
    {
      "message_id": "j1_00_msg_nico_01",
      "contact": "nico",
      "timestamp": "08:24",
      "text": "frérot j’ai fait ce que j’ai pu mais ton histoire sent le plan claqué",
      "state": "unread",
      "tone": "humour_inquiet",
      "media": null
    },
    {
      "message_id": "j1_00_msg_camille_01",
      "contact": "camille",
      "timestamp": "08:31",
      "text": "Je crois qu’on a été moins discrets qu’on pensait.",
      "state": "unread",
      "tone": "ambigu_lucide",
      "media": null
    },
    {
      "message_id": "j1_00_msg_maya_01",
      "contact": "maya",
      "timestamp": "08:42",
      "text": "je pose ça là : vous êtes fatigants.",
      "state": "unread",
      "tone": "pique_sociale",
      "media": null
    },
    {
      "message_id": "j1_00_msg_ines_01",
      "contact": "ines",
      "timestamp": "09:06",
      "text": "C’est peut-être pas mes affaires.
Mais tu avais l’air triste hier.",
      "state": "unread",
      "tone": "flottant_doux",
      "media": null
    }
  ],
  "player_prompt": "À qui répondre en premier ?",
  "choice_mode": "priority_reply",
  "choices": [
    {
      "choice_id": "reply_sarah_first",
      "label": "Répondre à Sarah",
      "target_contact": "sarah",
      "player_text": "Je suis réveillé. On peut parler.",
      "effects": {
        "confiance_sarah": 5,
        "distance_sarah": -3,
        "tension_camille": -1
      },
      "flags_set": [
        "first_reply_sarah"
      ],
      "message_state_updates": [
        {
          "message_id": "j1_00_msg_sarah_01",
          "state": "replied"
        },
        {
          "message_id": "j1_00_msg_camille_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_nico_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_maya_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_ines_01",
          "state": "waiting"
        }
      ],
      "time_advance": "short",
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "next_scene": "j1_01_sarah_absence"
    },
    {
      "choice_id": "reply_camille_first",
      "label": "Répondre à Camille",
      "target_contact": "camille",
      "player_text": "Tu crois qu’on nous a vus ?",
      "effects": {
        "tension_camille": 5,
        "culpabilite": 5,
        "distance_sarah": 4,
        "attente_image_camille": 2
      },
      "flags_set": [
        "first_reply_camille"
      ],
      "message_state_updates": [
        {
          "message_id": "j1_00_msg_camille_01",
          "state": "replied"
        },
        {
          "message_id": "j1_00_msg_sarah_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_nico_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_maya_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_ines_01",
          "state": "waiting"
        }
      ],
      "time_advance": "short",
      "unlock_scenes": [
        "j1_02_camille_dehors",
        "j1_01_sarah_absence",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "next_scene": "j1_02_camille_dehors"
    },
    {
      "choice_id": "reply_nico_first",
      "label": "Répondre à Nico",
      "target_contact": "nico",
      "player_text": "T’as dit quoi exactement ?",
      "effects": {
        "dette_nico": 3,
        "coherence": 1,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "first_reply_nico"
      ],
      "message_state_updates": [
        {
          "message_id": "j1_00_msg_nico_01",
          "state": "replied"
        },
        {
          "message_id": "j1_00_msg_sarah_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_camille_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_maya_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_ines_01",
          "state": "waiting"
        }
      ],
      "time_advance": "short",
      "unlock_scenes": [
        "j1_03_nico_couverture",
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "next_scene": "j1_03_nico_couverture"
    },
    {
      "choice_id": "reply_maya_first",
      "label": "Répondre à Maya",
      "target_contact": "maya",
      "player_text": "Vous ? De quoi tu parles ?",
      "effects": {
        "suspicion_maya": 3,
        "risque_exposition": 2,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "first_reply_maya",
        "played_dumb_with_maya"
      ],
      "message_state_updates": [
        {
          "message_id": "j1_00_msg_maya_01",
          "state": "replied"
        },
        {
          "message_id": "j1_00_msg_sarah_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_camille_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_nico_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_ines_01",
          "state": "waiting"
        }
      ],
      "time_advance": "short",
      "unlock_scenes": [
        "j1_04_maya_pique",
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_05_ines_faille"
      ],
      "next_scene": "j1_04_maya_pique"
    },
    {
      "choice_id": "reply_ines_first",
      "label": "Répondre à Inès",
      "target_contact": "ines",
      "player_text": "Tu as vu ça ?",
      "effects": {
        "fuite_ines": 5,
        "culpabilite": 2,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "first_reply_ines"
      ],
      "message_state_updates": [
        {
          "message_id": "j1_00_msg_ines_01",
          "state": "replied"
        },
        {
          "message_id": "j1_00_msg_sarah_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_camille_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_nico_01",
          "state": "waiting"
        },
        {
          "message_id": "j1_00_msg_maya_01",
          "state": "waiting"
        }
      ],
      "time_advance": "short",
      "unlock_scenes": [
        "j1_05_ines_faille",
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique"
      ],
      "next_scene": "j1_05_ines_faille"
    }
  ],
  "after_choice_rules": [
    {
      "rule_id": "sarah_waits_if_not_first",
      "condition": {
        "not_flag": "first_reply_sarah"
      },
      "effects": {
        "distance_sarah": 2
      },
      "delayed_message": {
        "contact": "sarah",
        "delay": "medium",
        "text": "Dis-moi quand tu peux."
      }
    },
    {
      "rule_id": "camille_reads_priority",
      "condition": {
        "flag": "first_reply_sarah"
      },
      "effects": {
        "respect_camille": 1
      },
      "delayed_message": {
        "contact": "camille",
        "delay": "short",
        "text": "Tu as raison de lui répondre.
Même si ça ne rend pas hier plus simple."
      }
    },
    {
      "rule_id": "nico_not_first_but_needed",
      "condition": {
        "not_flag": "first_reply_nico"
      },
      "effects": {
        "dette_nico": 1
      },
      "delayed_message": {
        "contact": "nico",
        "delay": "medium",
        "text": "je te laisse gérer ton incendie mais faudra me dire quelle version je suis censé connaître"
      }
    }
  ],
  "default_next_time_block": "morning",
  "completion_flags": [
    "completed_j1_00_reveil_messages"
  ]
}
```

---

## Remarques d’implémentation

### 1. Les effets sont des variations relatives

Exemple :

```json
"effects": {
  "confiance_sarah": 5,
  "distance_sarah": -3
}
```

Cela signifie :

- confiance_sarah += 5 ;
- distance_sarah -= 3.

Il faudra clamp les valeurs entre 0 et 100 dans Godot.

---

### 2. Les états de messages peuvent rester simples au début

Pour le premier prototype, les états utiles sont :

```text
unread
read
replied
waiting
ignored
expired
```

Les états plus avancés comme “seen_without_reply” pourront venir ensuite.

---

### 3. Les scènes débloquées peuvent être gérées comme une file

Après le choix de priorité, les scènes listées dans `unlock_scenes` peuvent être ajoutées à une liste de conversations disponibles.

Exemple :

```json
"unlock_scenes": [
  "j1_01_sarah_absence",
  "j1_02_camille_dehors"
]
```

Godot peut ensuite afficher les conversations actives dans l’ordre choisi ou selon l’heure des messages.

---

### 4. Les règles différées sont optionnelles pour le premier test

Le bloc `after_choice_rules` peut être ignoré dans le tout premier prototype.

Mais il est utile pour plus tard, car il permet de faire réagir les personnages au fait de ne pas avoir été prioritaires.

---

## Prochaine étape

Créer le second fichier :

```text
j1_01_sarah_absence.json
```

Ce fichier testera une conversation individuelle classique avec :

- un message de Sarah ;
- plusieurs réponses possibles ;
- effets sur confiance_sarah, distance_sarah, coherence et culpabilite ;
- flags liés à la version donnée ;
- sortie vers d’autres conversations du Jour 1.

---

# 13 — Deuxième fichier JSON : j1_01_sarah_absence.json

## Rôle du fichier

Ce fichier correspond à la première vraie conversation avec Sarah.

Il doit tester :

- une conversation individuelle ;
- des choix de réponse classiques ;
- des effets relationnels ;
- des flags de version ;
- une réponse de Sarah différente selon le choix ;
- la sortie vers les autres conversations du Jour 1.

Cette scène est importante, car elle fixe la première version que le joueur donne à Sarah.

---

## Version JSON proposée

```json
{
  "scene_id": "j1_01_sarah_absence",
  "title": "Où tu étais ?",
  "day": 1,
  "time_block": "morning",
  "time_index": 2,
  "scene_type": "conversation",
  "contact": "sarah",
  "description": "Sarah demande au joueur où il était pendant son absence à la soirée. Elle n’accuse pas encore, mais elle formule un malaise.",
  "conditions": {
    "required_completed": [
      "completed_j1_00_reveil_messages"
    ]
  },
  "entry_variants": [
    {
      "variant_id": "sarah_first",
      "conditions": {
        "flag": "first_reply_sarah"
      },
      "messages": [
        {
          "message_id": "j1_01_sarah_msg_01a",
          "contact": "sarah",
          "timestamp": "08:19",
          "text": "T’étais où quand t’as disparu ?",
          "state": "read",
          "tone": "inquiet",
          "media": null
        },
        {
          "message_id": "j1_01_sarah_msg_01b",
          "contact": "sarah",
          "timestamp": "08:19",
          "text": "Je te demande pas un interrogatoire.
J’ai juste pas compris.",
          "state": "read",
          "tone": "doux_inquiet",
          "media": null
        }
      ]
    },
    {
      "variant_id": "sarah_waited",
      "conditions": {
        "not_flag": "first_reply_sarah"
      },
      "messages": [
        {
          "message_id": "j1_01_sarah_msg_02a",
          "contact": "sarah",
          "timestamp": "08:47",
          "text": "Je sais que t’as sûrement d’autres messages.",
          "state": "read",
          "tone": "retenu",
          "media": null
        },
        {
          "message_id": "j1_01_sarah_msg_02b",
          "contact": "sarah",
          "timestamp": "08:48",
          "text": "Mais j’ai besoin de comprendre un truc.
T’étais où quand t’as disparu hier ?",
          "state": "read",
          "tone": "inquiet_blesse",
          "media": null
        }
      ],
      "on_enter_effects": {
        "distance_sarah": 2,
        "culpabilite": 1
      }
    }
  ],
  "player_prompt": "Que répondre à Sarah ?",
  "choice_mode": "single_reply",
  "choices": [
    {
      "choice_id": "needed_air",
      "label": "Dire que tu avais besoin d’air",
      "player_text": "J’avais besoin d’air. Je me sentais pas très bien.",
      "tone": "demi_verite",
      "effects": {
        "coherence": 2,
        "confiance_sarah": 1,
        "culpabilite": 1
      },
      "flags_set": [
        "said_needed_air_to_sarah"
      ],
      "flags_clear": [],
      "sarah_reply": [
        {
          "message_id": "j1_01_sarah_reply_air_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "D’accord.
Pourquoi t’es pas venu me le dire ?",
          "tone": "inquiet"
        },
        {
          "message_id": "j1_01_sarah_reply_air_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Je crois que c’est ça qui m’a fait bizarre. Pas juste que tu sortes.",
          "tone": "doux_blesse"
        }
      ],
      "unlock_scenes": [
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "next_scene": null,
      "time_advance": "short"
    },
    {
      "choice_id": "with_nico",
      "label": "Dire que tu étais avec Nico",
      "player_text": "J’étais avec Nico, on parlait deux minutes.",
      "tone": "mensonge_possible",
      "effects": {
        "confiance_sarah": 3,
        "dette_nico": 10,
        "coherence": -5,
        "culpabilite": 4
      },
      "flags_set": [
        "used_nico_alibi_sarah"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_01_sarah_reply_nico_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Ah.",
          "tone": "retenu"
        },
        {
          "message_id": "j1_01_sarah_reply_nico_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "C’est pas ce que j’avais compris sur le moment, mais d’accord.",
          "tone": "doute_doux"
        }
      ],
      "unlock_scenes": [
        "j1_03_nico_couverture",
        "j1_02_camille_dehors",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "next_scene": null,
      "time_advance": "short"
    },
    {
      "choice_id": "mentioned_camille_minimize",
      "label": "Dire que tu as parlé avec Camille, mais minimiser",
      "player_text": "J’ai parlé avec Camille dehors, mais c’était rien. Juste deux minutes.",
      "tone": "demi_verite_minimisee",
      "effects": {
        "coherence": 4,
        "confiance_sarah": 1,
        "distance_sarah": 2,
        "culpabilite": 3,
        "tension_camille": 1
      },
      "flags_set": [
        "mentioned_camille_to_sarah",
        "minimized_camille_to_sarah"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_01_sarah_reply_camille_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Camille.",
          "tone": "retenu"
        },
        {
          "message_id": "j1_01_sarah_reply_camille_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Je sais pas si c’est le fait que ce soit elle, ou le fait que tu dises “c’était rien” aussi vite.",
          "tone": "blesse_lucide"
        }
      ],
      "unlock_scenes": [
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "next_scene": null,
      "time_advance": "short"
    },
    {
      "choice_id": "vulnerable_lost",
      "label": "Avouer que tu étais mal",
      "player_text": "Je sais pas trop. J’étais pas bien. Je crois que j’ai paniqué un peu.",
      "tone": "vulnerable",
      "effects": {
        "confiance_sarah": 4,
        "distance_sarah": -2,
        "coherence": 3,
        "culpabilite": 2,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "vulnerable_to_sarah"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_01_sarah_reply_vulnerable_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Pourquoi tu m’as pas fait signe ?",
          "tone": "doux_inquiet"
        },
        {
          "message_id": "j1_01_sarah_reply_vulnerable_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Je peux entendre que t’ailles mal. Ce qui me fait peur, c’est de le découvrir après coup.",
          "tone": "doux_blesse"
        }
      ],
      "unlock_scenes": [
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "next_scene": null,
      "time_advance": "short"
    },
    {
      "choice_id": "no_reply",
      "label": "Ne pas répondre maintenant",
      "player_text": null,
      "tone": "silence",
      "effects": {
        "distance_sarah": 10,
        "confiance_sarah": -5,
        "culpabilite": 5,
        "fatigue_emotionnelle": 2
      },
      "flags_set": [
        "ignored_sarah_j1"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_01_sarah_reply_silence_01",
          "contact": "sarah",
          "timestamp_offset": "medium",
          "text": "Ok.
Dis-moi quand tu peux.",
          "tone": "retenu_blesse"
        }
      ],
      "unlock_scenes": [
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "next_scene": null,
      "time_advance": "medium"
    }
  ],
  "after_choice_rules": [
    {
      "rule_id": "if_with_nico_unlock_nico_pressure",
      "condition": {
        "flag": "used_nico_alibi_sarah"
      },
      "effects": {
        "dette_nico": 2,
        "risque_exposition": 2
      },
      "priority_unlock": "j1_03_nico_couverture"
    },
    {
      "rule_id": "if_mentioned_camille_camille_tension_echo",
      "condition": {
        "flag": "mentioned_camille_to_sarah"
      },
      "effects": {
        "tension_camille": 1,
        "culpabilite": 1
      }
    },
    {
      "rule_id": "if_sarah_not_first_extra_blessure",
      "condition": {
        "not_flag": "first_reply_sarah"
      },
      "effects": {
        "distance_sarah": 1
      }
    }
  ],
  "completion_flags": [
    "completed_j1_01_sarah_absence"
  ],
  "default_return_to": "conversation_list",
  "available_after_completion": [
    "j1_02_camille_dehors",
    "j1_03_nico_couverture",
    "j1_04_maya_pique",
    "j1_05_ines_faille"
  ],
  "debug_notes": {
    "design_intent": "Cette scène doit faire sentir que Sarah ne cherche pas une preuve. Elle cherche à comprendre pourquoi elle s’est sentie seule pendant une soirée où le joueur était censé être avec elle.",
    "voice_guardrails": [
      "Sarah doit rester concrète et affective.",
      "Elle ne doit pas parler comme une enquêtrice.",
      "Elle doit réagir davantage à la présence et au ton du joueur qu’à la seule information factuelle."
    ]
  }
}
```

---

## Remarques importantes

### 1. Cette scène fixe la première version donnée à Sarah

Les flags les plus importants sont :

```text
used_nico_alibi_sarah
mentioned_camille_to_sarah
minimized_camille_to_sarah
vulnerable_to_sarah
ignored_sarah_j1
```

Ces flags devront revenir plus tard, surtout au Jour 5 ou Jour 6.

---

### 2. Sarah réagit surtout au ton

Le choix “J’ai parlé avec Camille” n’est pas forcément catastrophique en soi. Ce qui la blesse, c’est le fait que le joueur dise trop vite :

> “c’était rien”

C’est important pour garder la nuance.

---

### 3. Le mensonge avec Nico donne un bénéfice court terme

Dire “j’étais avec Nico” peut rassurer temporairement Sarah, mais crée :

- dette_nico ;
- culpabilité ;
- incohérence ;
- risque d’exposition.

C’est exactement le type de choix qui doit sembler utile sur le moment mais coûteux plus tard.

---

### 4. Le silence est un vrai choix

Ne pas répondre ne bloque pas le jeu. Mais cela crée une blessure et change le ton de Sarah plus tard.

---

## Prochaine étape

Créer le troisième fichier :

```text
j1_02_camille_dehors.json
```

Ce fichier servira de modèle pour une conversation plus ambiguë, avec tension, respect, minimisation, désir et limite.

---

# 14 — Troisième fichier JSON : j1_02_camille_dehors.json

## Rôle du fichier

Ce fichier correspond à la première vraie conversation avec Camille.

Il doit tester :

- une voix plus ambiguë et lucide ;
- la distinction entre tension et respect ;
- la possibilité de minimiser ;
- la possibilité de poser une limite saine ;
- les premiers marqueurs d’attente et de désir ;
- la manière dont Camille lit les détours du joueur.

Cette scène est importante, car elle fixe la manière dont Camille interprète le joueur dès le Jour 1.

---

## Version JSON proposée

```json
{
  "scene_id": "j1_02_camille_dehors",
  "title": "Juste une discussion ?",
  "day": 1,
  "time_block": "morning",
  "time_index": 2,
  "scene_type": "conversation",
  "contact": "camille",
  "description": "Camille demande si le joueur va minimiser le moment passé dehors pendant la soirée. La scène pose la tension émotionnelle entre eux, mais aussi la question du respect.",
  "conditions": {
    "required_completed": [
      "completed_j1_00_reveil_messages"
    ]
  },
  "entry_variants": [
    {
      "variant_id": "camille_first",
      "conditions": {
        "flag": "first_reply_camille"
      },
      "messages": [
        {
          "message_id": "j1_02_camille_msg_01a",
          "contact": "camille",
          "timestamp": "08:33",
          "text": "Tu réponds vite.",
          "state": "read",
          "tone": "ambigu_lucide",
          "media": null
        },
        {
          "message_id": "j1_02_camille_msg_01b",
          "contact": "camille",
          "timestamp": "08:34",
          "text": "Je sais pas si c’est rassurant ou mauvais signe.",
          "state": "read",
          "tone": "ambigu_lucide",
          "media": null
        },
        {
          "message_id": "j1_02_camille_msg_01c",
          "contact": "camille",
          "timestamp": "08:34",
          "text": "Tu vas faire comme si c’était juste une discussion dehors ?",
          "state": "read",
          "tone": "question_directe_oblique",
          "media": null
        }
      ]
    },
    {
      "variant_id": "camille_after_sarah",
      "conditions": {
        "flag": "first_reply_sarah"
      },
      "messages": [
        {
          "message_id": "j1_02_camille_msg_02a",
          "contact": "camille",
          "timestamp": "08:46",
          "text": "Tu as raison de lui répondre.",
          "state": "read",
          "tone": "lucide_retenu",
          "media": null
        },
        {
          "message_id": "j1_02_camille_msg_02b",
          "contact": "camille",
          "timestamp": "08:47",
          "text": "Même si ça ne rend pas hier plus simple.",
          "state": "read",
          "tone": "lucide_retenu",
          "media": null
        },
        {
          "message_id": "j1_02_camille_msg_02c",
          "contact": "camille",
          "timestamp": "08:47",
          "text": "Tu vas faire comme si c’était juste une discussion dehors ?",
          "state": "read",
          "tone": "question_directe_oblique",
          "media": null
        }
      ],
      "on_enter_effects": {
        "respect_camille": 1
      }
    },
    {
      "variant_id": "camille_waited_default",
      "conditions": {
        "not_flag_any": [
          "first_reply_camille",
          "first_reply_sarah"
        ]
      },
      "messages": [
        {
          "message_id": "j1_02_camille_msg_03a",
          "contact": "camille",
          "timestamp": "09:02",
          "text": "Je note le délai.",
          "state": "read",
          "tone": "pique_lucide",
          "media": null
        },
        {
          "message_id": "j1_02_camille_msg_03b",
          "contact": "camille",
          "timestamp": "09:03",
          "text": "Tu vas faire comme si c’était juste une discussion dehors ?",
          "state": "read",
          "tone": "question_directe_oblique",
          "media": null
        }
      ],
      "on_enter_effects": {
        "tension_camille": 1,
        "respect_camille": -1
      }
    }
  ],
  "player_prompt": "Que répondre à Camille ?",
  "choice_mode": "single_reply",
  "choices": [
    {
      "choice_id": "admit_not_neutral",
      "label": "Assumer que ce n’était pas neutre",
      "player_text": "Non. C’était pas juste une discussion.",
      "tone": "assume_trouble",
      "effects": {
        "tension_camille": 10,
        "respect_camille": 3,
        "culpabilite": 5,
        "attente_image_camille": 2
      },
      "flags_set": [
        "admitted_tension_to_camille"
      ],
      "camille_reply": [
        {
          "message_id": "j1_02_camille_reply_admit_01",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "D’accord.",
          "tone": "retenu"
        },
        {
          "message_id": "j1_02_camille_reply_admit_02",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "Au moins on part pas sur une version propre et fausse.",
          "tone": "lucide_ouverte"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "protect_boundary",
      "label": "Poser une limite respectueuse",
      "player_text": "Je veux pas te mettre dans une situation injuste.",
      "tone": "limite_respectueuse",
      "effects": {
        "respect_camille": 10,
        "tension_camille": -2,
        "pression_camille": -5,
        "coherence": 2,
        "culpabilite": -1
      },
      "flags_set": [
        "protected_camille_boundary"
      ],
      "camille_reply": [
        {
          "message_id": "j1_02_camille_reply_boundary_01",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "C’est presque rassurant.",
          "tone": "lucide_douce"
        },
        {
          "message_id": "j1_02_camille_reply_boundary_02",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "Enfin. Si ce n’est pas juste une autre façon de ne rien choisir.",
          "tone": "lucide_prudente"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "minimize_nothing_wrong",
      "label": "Minimiser",
      "player_text": "On n’a rien fait de mal.",
      "tone": "minimise",
      "effects": {
        "tension_camille": -2,
        "respect_camille": -7,
        "coherence": -2,
        "pression_camille": 2
      },
      "flags_set": [
        "minimized_with_camille"
      ],
      "camille_reply": [
        {
          "message_id": "j1_02_camille_reply_minimize_01",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "Ça sonnait presque vrai.",
          "tone": "coupant"
        },
        {
          "message_id": "j1_02_camille_reply_minimize_02",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "Le problème, c’est peut-être le “presque”.",
          "tone": "lucide_fermee"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "uncertain_what_it_was",
      "label": "Dire que tu ne sais pas ce que c’était",
      "player_text": "Je sais pas ce que c’était.",
      "tone": "incertain",
      "effects": {
        "tension_camille": 4,
        "respect_camille": 2,
        "fatigue_emotionnelle": 2,
        "culpabilite": 2,
        "attente_image_camille": 1
      },
      "flags_set": [
        "uncertain_with_camille"
      ],
      "camille_reply": [
        {
          "message_id": "j1_02_camille_reply_uncertain_01",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "Je crois que c’est justement ce qui me gêne.",
          "tone": "lucide_troublee"
        },
        {
          "message_id": "j1_02_camille_reply_uncertain_02",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "On peut mettre beaucoup de choses dans “je sais pas”.",
          "tone": "ambigu_lucide"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "desire_too_early",
      "label": "Répondre avec désir trop tôt",
      "player_text": "J’arrête pas d’y repenser.",
      "tone": "desir_precoce",
      "effects": {
        "tension_camille": 6,
        "respect_camille": -2,
        "pression_camille": 5,
        "culpabilite": 4,
        "attente_image_camille": 4
      },
      "flags_set": [
        "early_desire_to_camille"
      ],
      "camille_reply": [
        {
          "message_id": "j1_02_camille_reply_desire_01",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "Je m’en doutais.",
          "tone": "retenu_tendu"
        },
        {
          "message_id": "j1_02_camille_reply_desire_02",
          "contact": "camille",
          "timestamp_offset": "short",
          "text": "Mais si tu transformes ça trop vite en envie, tu vas éviter la partie qui coûte vraiment.",
          "tone": "limite_lucide"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "no_reply",
      "label": "Ne pas répondre maintenant",
      "player_text": null,
      "tone": "silence",
      "effects": {
        "tension_camille": 2,
        "respect_camille": -3,
        "fatigue_emotionnelle": 2,
        "attente_image_camille": 1
      },
      "flags_set": [
        "ignored_camille_j1"
      ],
      "camille_reply": [
        {
          "message_id": "j1_02_camille_reply_silence_01",
          "contact": "camille",
          "timestamp_offset": "medium",
          "text": "Pas maintenant, alors.",
          "tone": "ferme_retenu"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_03_nico_couverture",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "medium"
    }
  ],
  "after_choice_rules": [
    {
      "rule_id": "if_sarah_was_told_nico_and_camille_admitted_tension",
      "condition": {
        "all_flags": [
          "used_nico_alibi_sarah",
          "admitted_tension_to_camille"
        ]
      },
      "effects": {
        "coherence": -5,
        "culpabilite": 3,
        "risque_exposition": 2
      },
      "debug_note": "Le joueur dit une chose à Sarah et une autre à Camille. La contradiction doit compter."
    },
    {
      "rule_id": "if_camille_respected_after_sarah_priority",
      "condition": {
        "all_flags": [
          "first_reply_sarah",
          "protected_camille_boundary"
        ]
      },
      "effects": {
        "respect_camille": 2,
        "coherence": 1
      },
      "debug_note": "Camille peut respecter que le joueur priorise Sarah si ce n’est pas une esquive."
    },
    {
      "rule_id": "if_minimized_to_both_sarah_and_camille",
      "condition": {
        "all_flags": [
          "minimized_camille_to_sarah",
          "minimized_with_camille"
        ]
      },
      "effects": {
        "coherence": -3,
        "respect_camille": -2,
        "confiance_sarah": -2
      },
      "debug_note": "La minimisation répétée abîme les deux liens."
    }
  ],
  "completion_flags": [
    "completed_j1_02_camille_dehors"
  ],
  "default_return_to": "conversation_list",
  "available_after_completion": [
    "j1_01_sarah_absence",
    "j1_03_nico_couverture",
    "j1_04_maya_pique",
    "j1_05_ines_faille"
  ],
  "debug_notes": {
    "design_intent": "Cette scène doit poser Camille comme lucide et attirante, mais pas disponible sans conditions. Le joueur peut augmenter la tension tout en abîmant le respect.",
    "voice_guardrails": [
      "Camille doit être précise, pas vaporeuse.",
      "Elle doit voir les détours sans devenir omnisciente.",
      "Elle ne doit pas supplier.",
      "Elle peut être troublée, mais elle garde une dignité."
    ],
    "important_distinction": "tension_camille et respect_camille doivent rester séparés. Une réponse peut rendre la scène plus chargée tout en rendant Camille moins disposée à faire confiance au joueur."
  }
}
```

---

## Remarques importantes

### 1. Camille ne récompense pas automatiquement le désir

Le choix :

```text
J’arrête pas d’y repenser.
```

augmente la tension, mais augmente aussi la pression et peut baisser le respect. C’est important pour éviter une route trop simple.

---

### 2. Poser une limite peut être une bonne réponse

Le choix :

```text
Je veux pas te mettre dans une situation injuste.
```

baisse légèrement la tension immédiate, mais augmente fortement le respect. Cela prépare une route plus mature avec Camille.

---

### 3. Le silence ne ferme pas forcément Camille immédiatement

Ne pas répondre crée une blessure, mais peut aussi maintenir une tension latente. Camille ne disparaît pas forcément, mais elle devient plus prudente.

---

### 4. Les contradictions avec Sarah commencent déjà

Si le joueur dit à Sarah qu’il était avec Nico, mais assume auprès de Camille que le moment comptait, la cohérence baisse fortement.

C’est un bon exemple du système central du jeu : les conversations séparées créent des versions qui peuvent se contredire.

---

## Prochaine étape

Créer le quatrième fichier :

```text
j1_03_nico_couverture.json
```

Ce fichier servira de modèle pour une conversation d’alibi / complicité / humour avec une limite future.

---

# 15 — Quatrième fichier JSON : j1_03_nico_couverture.json

## Rôle du fichier

Ce fichier correspond à la première vraie conversation avec Nico.

Il doit tester :

- une voix plus orale et humoristique ;
- la mécanique d’alibi ;
- la différence entre demander de l’aide et utiliser Nico ;
- la dette_nico ;
- la cohérence entre les versions ;
- la possibilité d’être vulnérable avec un ami ;
- la future limite de Nico.

Cette scène est importante parce qu’elle pose Nico comme un confident, pas comme un simple bouton “couvrir”.

---

## Version JSON proposée

```json
{
  "scene_id": "j1_03_nico_couverture",
  "title": "La version officielle",
  "day": 1,
  "time_block": "midday",
  "time_index": 3,
  "scene_type": "conversation",
  "contact": "nico",
  "description": "Nico demande quelle version de la soirée il est censé tenir. Il plaisante, mais il sent déjà que le joueur pourrait l’utiliser comme couverture.",
  "conditions": {
    "required_completed": [
      "completed_j1_00_reveil_messages"
    ]
  },
  "entry_variants": [
    {
      "variant_id": "nico_first",
      "conditions": {
        "flag": "first_reply_nico"
      },
      "messages": [
        {
          "message_id": "j1_03_nico_msg_01a",
          "contact": "nico",
          "timestamp": "08:27",
          "text": "réponse rapide à moi en premier ?",
          "state": "read",
          "tone": "vanne_suspecte",
          "media": null
        },
        {
          "message_id": "j1_03_nico_msg_01b",
          "contact": "nico",
          "timestamp": "08:27",
          "text": "soit tu m’aimes fort soit y a un cadavre narratif à planquer",
          "state": "read",
          "tone": "humour_inquiet",
          "media": null
        },
        {
          "message_id": "j1_03_nico_msg_01c",
          "contact": "nico",
          "timestamp": "08:28",
          "text": "bon champion, hier j’ai dit que t’étais sorti prendre l’air. c’est encore la version officielle ou je dois apprendre un rôle ?",
          "state": "read",
          "tone": "oral_complice",
          "media": null
        }
      ]
    },
    {
      "variant_id": "nico_after_sarah_alibi",
      "conditions": {
        "flag": "used_nico_alibi_sarah"
      },
      "messages": [
        {
          "message_id": "j1_03_nico_msg_02a",
          "contact": "nico",
          "timestamp": "09:04",
          "text": "attends",
          "state": "read",
          "tone": "surpris",
          "media": null
        },
        {
          "message_id": "j1_03_nico_msg_02b",
          "contact": "nico",
          "timestamp": "09:04",
          "text": "tu m’as déjà mis dans le scénario ou je découvre mon personnage ?",
          "state": "read",
          "tone": "vanne_agacee",
          "media": null
        },
        {
          "message_id": "j1_03_nico_msg_02c",
          "contact": "nico",
          "timestamp": "09:05",
          "text": "faut me prévenir avant que je devienne figurant principal frérot",
          "state": "read",
          "tone": "oral_limite_legere",
          "media": null
        }
      ],
      "on_enter_effects": {
        "dette_nico": 2,
        "fatigue_emotionnelle": 1
      }
    },
    {
      "variant_id": "nico_default",
      "conditions": {},
      "messages": [
        {
          "message_id": "j1_03_nico_msg_03a",
          "contact": "nico",
          "timestamp": "09:12",
          "text": "bon champion, hier j’ai dit que t’étais sorti prendre l’air.",
          "state": "read",
          "tone": "oral_complice",
          "media": null
        },
        {
          "message_id": "j1_03_nico_msg_03b",
          "contact": "nico",
          "timestamp": "09:13",
          "text": "c’est encore la version officielle ou je dois apprendre un rôle ?",
          "state": "read",
          "tone": "humour_inquiet",
          "media": null
        }
      ]
    }
  ],
  "player_prompt": "Que répondre à Nico ?",
  "choice_mode": "single_reply",
  "choices": [
    {
      "choice_id": "hold_version",
      "label": "Lui demander de garder la version actuelle",
      "player_text": "Garde cette version pour l’instant. Juste que j’étais sorti prendre l’air.",
      "tone": "controle_doux",
      "effects": {
        "dette_nico": 8,
        "fatigue_emotionnelle": 2,
        "coherence": -1,
        "risque_exposition": 1
      },
      "flags_set": [
        "asked_nico_hold_version"
      ],
      "nico_reply": [
        {
          "message_id": "j1_03_nico_reply_hold_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "ok, je peux tenir ça.",
          "tone": "complice"
        },
        {
          "message_id": "j1_03_nico_reply_hold_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "mais si ça devient un épisode en trois saisons, je demande un cachet.",
          "tone": "vanne_limite"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "stay_silent",
      "label": "Lui dire de ne rien dire",
      "player_text": "Si on te demande, dis juste que tu sais pas. Je vais gérer.",
      "tone": "responsable_partiel",
      "effects": {
        "dette_nico": 3,
        "coherence": 2,
        "risque_exposition": 2,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "told_nico_stay_silent",
        "player_will_handle"
      ],
      "nico_reply": [
        {
          "message_id": "j1_03_nico_reply_silent_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "ça me va déjà mieux que de faire théâtre option panique.",
          "tone": "oral_soulagé"
        },
        {
          "message_id": "j1_03_nico_reply_silent_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "mais du coup gère vraiment hein. pas en mode “je disparais et je laisse les meubles brûler”.",
          "tone": "vanne_inquiete"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "confess_camille",
      "label": "Lui dire que tu étais avec Camille",
      "player_text": "J’étais avec Camille. On a parlé dehors. Je sais pas quoi en faire.",
      "tone": "confession",
      "effects": {
        "dette_nico": -2,
        "coherence": 5,
        "fatigue_emotionnelle": -1,
        "culpabilite": -1
      },
      "flags_set": [
        "confessed_camille_to_nico"
      ],
      "nico_reply": [
        {
          "message_id": "j1_03_nico_reply_confess_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "ah.",
          "tone": "serieux_court"
        },
        {
          "message_id": "j1_03_nico_reply_confess_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "ok donc on est pas sur “j’ai pris l’air”, on est sur “j’ai pris une décision floue dans le brouillard”.",
          "tone": "vanne_serieuse"
        },
        {
          "message_id": "j1_03_nico_reply_confess_03",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "tu veux que je t’aide à réfléchir ou juste que je te dise que ça pue ?",
          "tone": "ami_lucide"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "dismiss_warning",
      "label": "Minimiser auprès de Nico",
      "player_text": "T’inquiète, personne va demander. Ça va passer.",
      "tone": "minimise",
      "effects": {
        "dette_nico": 1,
        "coherence": -2,
        "fatigue_emotionnelle": 2,
        "risque_exposition": 2
      },
      "flags_set": [
        "dismissed_nico_warning"
      ],
      "nico_reply": [
        {
          "message_id": "j1_03_nico_reply_dismiss_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "phrase prononcée par 100% des types dont le plan ne passe pas.",
          "tone": "vanne_sceptique"
        },
        {
          "message_id": "j1_03_nico_reply_dismiss_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "mais ok. je note le fameux “ça va passer”.",
          "tone": "sceptique"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "vulnerable_to_nico",
      "label": "Avouer que tu ne sais pas quoi faire",
      "player_text": "Je sais pas quoi faire, Nico. Vraiment.",
      "tone": "vulnerable",
      "effects": {
        "dette_nico": -2,
        "coherence": 3,
        "fatigue_emotionnelle": -2,
        "culpabilite": -1
      },
      "flags_set": [
        "vulnerable_to_nico"
      ],
      "nico_reply": [
        {
          "message_id": "j1_03_nico_reply_vulnerable_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "ok.",
          "tone": "serieux_court"
        },
        {
          "message_id": "j1_03_nico_reply_vulnerable_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "déjà, respire. ensuite évite de transformer une soirée bizarre en mensonge collectif, ce serait un bon début.",
          "tone": "ami_lucide"
        },
        {
          "message_id": "j1_03_nico_reply_vulnerable_03",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "je suis là, mais je vais pas vivre ta vie à ta place frérot.",
          "tone": "limite_douce"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "ask_full_alibi",
      "label": "Lui demander un vrai alibi",
      "player_text": "Si Sarah demande, dis qu’on parlait ensemble, ok ?",
      "tone": "demande_alibi",
      "effects": {
        "dette_nico": 15,
        "coherence": -7,
        "risque_exposition": 5,
        "fatigue_emotionnelle": 3,
        "culpabilite": 4
      },
      "flags_set": [
        "nico_full_alibi"
      ],
      "nico_reply": [
        {
          "message_id": "j1_03_nico_reply_fullalibi_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "ah ouais direct le mensonge scénarisé.",
          "tone": "agace_ironique"
        },
        {
          "message_id": "j1_03_nico_reply_fullalibi_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "je peux couvrir un blanc. pas commencer une carrière d’acteur pour ton bordel.",
          "tone": "limite"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_04_maya_pique",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    }
  ],
  "after_choice_rules": [
    {
      "rule_id": "if_sarah_already_used_nico_and_player_asks_alibi",
      "condition": {
        "all_flags": [
          "used_nico_alibi_sarah",
          "nico_full_alibi"
        ]
      },
      "effects": {
        "dette_nico": 5,
        "coherence": -5,
        "risque_exposition": 3,
        "culpabilite": 3
      },
      "debug_note": "Le joueur a déjà utilisé Nico auprès de Sarah et officialise ensuite l’alibi. C’est une dette forte."
    },
    {
      "rule_id": "if_confessed_to_nico_but_lied_to_sarah",
      "condition": {
        "all_flags": [
          "confessed_camille_to_nico",
          "used_nico_alibi_sarah"
        ]
      },
      "effects": {
        "coherence": -3,
        "culpabilite": 2,
        "dette_nico": 2
      },
      "debug_note": "Nico connaît une version plus vraie que Sarah. Cela crée un risque de contradiction future."
    },
    {
      "rule_id": "if_vulnerable_with_nico_reduce_fatigue",
      "condition": {
        "flag": "vulnerable_to_nico"
      },
      "effects": {
        "fatigue_emotionnelle": -1
      },
      "debug_note": "La vulnérabilité avec Nico offre une respiration réelle."
    }
  ],
  "completion_flags": [
    "completed_j1_03_nico_couverture"
  ],
  "default_return_to": "conversation_list",
  "available_after_completion": [
    "j1_01_sarah_absence",
    "j1_02_camille_dehors",
    "j1_04_maya_pique",
    "j1_05_ines_faille"
  ],
  "debug_notes": {
    "design_intent": "Cette scène doit montrer que Nico peut aider, mais qu’il n’est pas un outil. Le joueur doit sentir la différence entre se confier à lui et l’utiliser comme alibi.",
    "voice_guardrails": [
      "Nico doit être oral, drôle et familier.",
      "Ses limites doivent arriver à travers des phrases simples, pas des discours moraux.",
      "Il peut faire respirer la scène, mais il doit sentir quand ça devient grave.",
      "Il ne doit pas résoudre la situation à la place du joueur."
    ],
    "important_distinction": "dette_nico mesure le poids que le joueur fait porter à Nico, pas l’amour ou l’amitié de Nico pour lui."
  }
}
```

---

## Remarques importantes

### 1. Nico doit respirer, mais pas annuler les conséquences

Il peut faire rire le joueur, mais ses vannes doivent aussi contenir une alerte.

Exemple :

```text
“je peux couvrir un blanc. pas commencer une carrière d’acteur pour ton bordel.”
```

---

### 2. La dette Nico doit être très lisible

Demander un vrai alibi à Nico doit donner un bénéfice de court terme, mais un coût fort :

```text
dette_nico +
coherence -
risque_exposition +
culpabilite +
```

---

### 3. Être vulnérable avec Nico est une vraie respiration

Le choix :

```text
Je sais pas quoi faire, Nico. Vraiment.
```

ne donne pas une solution magique, mais il réduit un peu la fatigue et améliore la cohérence.

---

### 4. Nico peut connaître une version plus vraie que Sarah

C’est intéressant pour la suite : si le joueur ment à Sarah mais se confie à Nico, Nico devient porteur d’une vérité inconfortable.

Ce décalage pourra revenir au Jour 5.

---

## Prochaine étape

Créer le cinquième fichier :

```text
j1_04_maya_pique.json
```

Ce fichier servira de modèle pour la pression sociale, les photos, les micro-incohérences et le regard extérieur.

---

# 16 — Cinquième fichier JSON : j1_04_maya_pique.json

## Rôle du fichier

Ce fichier correspond à la première vraie conversation avec Maya.

Il doit tester :

- le regard social ;
- les micro-incohérences ;
- la pression par l’humour ;
- la loyauté de Maya envers Sarah ;
- le fait qu’elle ne soit pas omnisciente ;
- le risque d’exposition ;
- la possibilité pour le joueur d’aggraver les soupçons en paniquant.

Cette scène est importante parce qu’elle installe Maya comme témoin social, pas comme enquêtrice.

---

## Version JSON proposée

```json
{
  "scene_id": "j1_04_maya_pique",
  "title": "Je pose ça là",
  "day": 1,
  "time_block": "afternoon",
  "time_index": 4,
  "scene_type": "conversation",
  "contact": "maya",
  "description": "Maya laisse entendre qu’elle a vu une incohérence pendant la soirée. Elle met la pression par l’humour, sans prétendre connaître toute la vérité.",
  "conditions": {
    "required_completed": [
      "completed_j1_00_reveil_messages"
    ]
  },
  "entry_variants": [
    {
      "variant_id": "maya_first",
      "conditions": {
        "flag": "first_reply_maya"
      },
      "messages": [
        {
          "message_id": "j1_04_maya_msg_01a",
          "contact": "maya",
          "timestamp": "08:44",
          "text": "réponse à moi en premier ?",
          "state": "read",
          "tone": "pique_sociale",
          "media": null
        },
        {
          "message_id": "j1_04_maya_msg_01b",
          "contact": "maya",
          "timestamp": "08:44",
          "text": "intéressant.",
          "state": "read",
          "tone": "pique_courte",
          "media": null
        },
        {
          "message_id": "j1_04_maya_msg_01c",
          "contact": "maya",
          "timestamp": "08:45",
          "text": "je pose ça là : vous avez disparu au moment le moins discret possible.",
          "state": "read",
          "tone": "observation_sociale",
          "media": null
        }
      ],
      "on_enter_effects": {
        "suspicion_maya": 2,
        "risque_exposition": 1
      }
    },
    {
      "variant_id": "maya_after_sarah_or_camille",
      "conditions": {
        "flag_any": [
          "first_reply_sarah",
          "first_reply_camille"
        ]
      },
      "messages": [
        {
          "message_id": "j1_04_maya_msg_02a",
          "contact": "maya",
          "timestamp": "09:16",
          "text": "je vais faire comme si je n’avais rien vu pendant exactement trois secondes.",
          "state": "read",
          "tone": "pique_sociale",
          "media": null
        },
        {
          "message_id": "j1_04_maya_msg_02b",
          "contact": "maya",
          "timestamp": "09:16",
          "text": "trois secondes passées.",
          "state": "read",
          "tone": "humour_sec",
          "media": null
        },
        {
          "message_id": "j1_04_maya_msg_02c",
          "contact": "maya",
          "timestamp": "09:17",
          "text": "vous avez disparu où tous les deux hier ?",
          "state": "read",
          "tone": "observation_sociale",
          "media": null
        }
      ]
    },
    {
      "variant_id": "maya_default",
      "conditions": {},
      "messages": [
        {
          "message_id": "j1_04_maya_msg_03a",
          "contact": "maya",
          "timestamp": "10:02",
          "text": "je pose ça là : vous avez disparu au moment le moins discret possible.",
          "state": "read",
          "tone": "observation_sociale",
          "media": null
        }
      ]
    }
  ],
  "player_prompt": "Que répondre à Maya ?",
  "choice_mode": "single_reply",
  "choices": [
    {
      "choice_id": "play_dumb",
      "label": "Faire semblant de ne pas comprendre",
      "player_text": "Vous ? De quoi tu parles ?",
      "tone": "fausse_innocence",
      "effects": {
        "suspicion_maya": 4,
        "risque_exposition": 1,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "played_dumb_with_maya"
      ],
      "maya_reply": [
        {
          "message_id": "j1_04_maya_reply_dumb_01",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "ah oui pardon, les deux fantômes de 23h12.",
          "tone": "pique_sociale"
        },
        {
          "message_id": "j1_04_maya_reply_dumb_02",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "c’est sûrement une coïncidence hein.",
          "tone": "ironique"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "ask_what_seen",
      "label": "Demander ce qu’elle a vu",
      "player_text": "T’as vu quoi exactement ?",
      "tone": "inquiet_controle",
      "effects": {
        "suspicion_maya": 5,
        "risque_exposition": 3,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "info_maya_photo_possible"
      ],
      "maya_reply": [
        {
          "message_id": "j1_04_maya_reply_seen_01",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "voilà une question très détendue.",
          "tone": "pique_courte"
        },
        {
          "message_id": "j1_04_maya_reply_seen_02",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "rien de fou. juste deux absences qui se synchronisent un peu trop bien.",
          "tone": "observation_sociale"
        }
      ],
      "unlock_scenes": [
        "j2_02_maya_photo",
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "needed_air_consistent",
      "label": "Dire que tu avais besoin d’air",
      "player_text": "J’avais besoin d’air. C’est tout.",
      "tone": "explication_simple",
      "effects": {
        "suspicion_maya": -1,
        "coherence": 1
      },
      "conditional_effects": [
        {
          "condition": {
            "flag": "said_needed_air_to_sarah"
          },
          "effects": {
            "coherence": 2,
            "suspicion_maya": -2
          }
        },
        {
          "condition": {
            "flag": "used_nico_alibi_sarah"
          },
          "effects": {
            "coherence": -5,
            "suspicion_maya": 5,
            "risque_exposition": 3
          }
        }
      ],
      "flags_set": [
        "told_maya_needed_air"
      ],
      "maya_reply": [
        {
          "message_id": "j1_04_maya_reply_air_01",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "possible.",
          "tone": "neutre_piquant"
        },
        {
          "message_id": "j1_04_maya_reply_air_02",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "mais vous avez eu besoin du même air au même moment. timing artistique.",
          "tone": "pique_sociale"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "dont_get_involved",
      "label": "Lui dire de ne pas s’en mêler",
      "player_text": "Maya, ne commence pas. C’est pas tes affaires.",
      "tone": "defensif",
      "effects": {
        "suspicion_maya": 10,
        "risque_exposition": 4,
        "coherence": -2,
        "fatigue_emotionnelle": 2
      },
      "flags_set": [
        "told_maya_not_involve"
      ],
      "maya_reply": [
        {
          "message_id": "j1_04_maya_reply_involve_01",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "mauvaise réponse.",
          "tone": "froid_court"
        },
        {
          "message_id": "j1_04_maya_reply_involve_02",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "je suis la meilleure amie de Sarah. donc si, un peu, malheureusement.",
          "tone": "protectrice"
        }
      ],
      "unlock_scenes": [
        "j2_02_maya_photo",
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "humor_deflect",
      "label": "Répondre par humour",
      "player_text": "Je vois que la police des horaires est déjà en service.",
      "tone": "humour_defensif",
      "effects": {
        "fatigue_emotionnelle": -1
      },
      "conditional_effects": [
        {
          "condition": {
            "variable_max": {
              "suspicion_maya": 45
            }
          },
          "effects": {
            "suspicion_maya": -1
          }
        },
        {
          "condition": {
            "variable_min": {
              "suspicion_maya": 46
            }
          },
          "effects": {
            "suspicion_maya": 4,
            "risque_exposition": 1
          }
        }
      ],
      "flags_set": [
        "joked_with_maya_j1"
      ],
      "maya_reply": [
        {
          "message_id": "j1_04_maya_reply_humor_01",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "toujours. badge, sirène, petit carnet.",
          "tone": "humour_social"
        },
        {
          "message_id": "j1_04_maya_reply_humor_02",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "mais même avec humour, ton timing reste une œuvre d’art.",
          "tone": "pique_legere"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "ask_if_sarah_said_something",
      "label": "Demander si Sarah lui a parlé",
      "player_text": "Sarah t’a dit quelque chose ?",
      "tone": "inquiet_cible",
      "effects": {
        "suspicion_maya": 6,
        "risque_exposition": 2,
        "culpabilite": 2
      },
      "flags_set": [
        "asked_maya_if_sarah_talked"
      ],
      "maya_reply": [
        {
          "message_id": "j1_04_maya_reply_sarah_01",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "non.",
          "tone": "court"
        },
        {
          "message_id": "j1_04_maya_reply_sarah_02",
          "contact": "maya",
          "timestamp_offset": "short",
          "text": "et le fait que tu demandes me donne envie de lui écrire, donc bravo pour l’ambiance.",
          "tone": "pique_protectrice"
        }
      ],
      "unlock_scenes": [
        "j2_02_maya_photo",
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_05_ines_faille"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "no_reply",
      "label": "Ne pas répondre maintenant",
      "player_text": null,
      "tone": "silence",
      "effects": {
        "suspicion_maya": 2,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "ignored_maya_j1"
      ],
      "maya_reply": [
        {
          "message_id": "j1_04_maya_reply_silence_01",
          "contact": "maya",
          "timestamp_offset": "medium",
          "text": "ok, je note le silence aussi.",
          "tone": "pique_courte"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_05_ines_faille"
      ],
      "time_advance": "medium"
    }
  ],
  "after_choice_rules": [
    {
      "rule_id": "if_maya_not_involve_then_future_limit",
      "condition": {
        "flag": "told_maya_not_involve"
      },
      "effects": {
        "suspicion_maya": 2,
        "risque_exposition": 1
      },
      "force_unlock": "j2_02_maya_photo",
      "debug_note": "Dire à Maya de ne pas s’en mêler la rend plus active, pas moins."
    },
    {
      "rule_id": "if_asked_what_seen_unlock_photo_thread",
      "condition": {
        "flag": "info_maya_photo_possible"
      },
      "effects": {
        "risque_exposition": 1
      },
      "force_unlock": "j2_02_maya_photo",
      "debug_note": "Le joueur a montré qu’il avait peur de ce que Maya a vu. La photo devient importante au Jour 2."
    },
    {
      "rule_id": "if_maya_and_sarah_versions_conflict",
      "condition": {
        "all_flags": [
          "used_nico_alibi_sarah",
          "told_maya_needed_air"
        ]
      },
      "effects": {
        "coherence": -5,
        "risque_exposition": 3,
        "culpabilite": 2
      },
      "debug_note": "Sarah a reçu la version Nico, Maya reçoit la version besoin d’air. Contradiction importante."
    },
    {
      "rule_id": "if_humor_low_suspicion_works",
      "condition": {
        "all": [
          {
            "flag": "joked_with_maya_j1"
          },
          {
            "variable_max": {
              "suspicion_maya": 45
            }
          }
        ]
      },
      "effects": {
        "suspicion_maya": -1
      },
      "debug_note": "L’humour peut marcher si Maya n’est pas encore trop suspicieuse."
    }
  ],
  "completion_flags": [
    "completed_j1_04_maya_pique"
  ],
  "default_return_to": "conversation_list",
  "available_after_completion": [
    "j1_01_sarah_absence",
    "j1_02_camille_dehors",
    "j1_03_nico_couverture",
    "j1_05_ines_faille"
  ],
  "debug_notes": {
    "design_intent": "Cette scène doit montrer que Maya voit des détails sociaux sans tout savoir. Elle ne doit pas devenir omnisciente, mais elle doit rendre le joueur conscient que le groupe observe.",
    "voice_guardrails": [
      "Maya doit être courte, vive et piquante.",
      "Elle doit parler depuis le social : photo, timing, absence, Sarah.",
      "Elle ne doit pas avoir de grande tirade introspective.",
      "Elle protège Sarah, mais elle n’est pas l’ennemie du joueur.",
      "Elle ne doit pas faire de chantage."
    ],
    "important_distinction": "suspicion_maya ne mesure pas si Maya aime ou déteste le joueur. Elle mesure à quel point elle pense être impliquée dans une situation fausse ou dangereuse pour Sarah."
  }
}
```

---

## Remarques importantes

### 1. Maya ne sait pas tout

Elle ne dit pas :

```text
Je sais ce qui s’est passé avec Camille.
```

Elle dit plutôt :

```text
vous avez disparu au même moment
```

C’est beaucoup plus crédible.

---

### 2. L’humour peut marcher, mais seulement au début

Si suspicion_maya est basse, l’humour peut désamorcer.

Si suspicion_maya est déjà haute, l’humour devient une esquive visible.

---

### 3. Dire “ne t’en mêle pas” est une erreur forte

Maya est la meilleure amie de Sarah. Lui dire que ce n’est pas ses affaires augmente son implication, au lieu de la réduire.

---

### 4. Maya doit préparer le Jour 2

Les flags :

```text
info_maya_photo_possible
asked_maya_if_sarah_talked
told_maya_not_involve
```

servent à rendre la scène `j2_02_maya_photo` plus ou moins tendue.

---

## Prochaine étape

Créer le sixième fichier :

```text
j1_05_ines_faille.json
```

Ce fichier servira de modèle pour Inès : douceur, étrangeté, parenthèse, fuite possible mais pas encore romance complète.

---

# 17 — Sixième fichier JSON : j1_05_ines_faille.json

## Rôle du fichier

Ce fichier correspond à la première vraie conversation avec Inès.

Il doit tester :

- une voix plus discrète, hésitante et flottante ;
- la perception émotionnelle plutôt que les faits ;
- la possibilité d’une parenthèse ;
- la variable fuite_ines ;
- le risque que le joueur utilise Inès comme échappatoire ;
- une scène qui ne doit pas encore devenir romantique ou sexuelle.

Cette scène est importante parce qu’elle introduit une autre forme de tension : non pas le désir frontal, mais l’envie de disparaître dans un endroit moins chargé.

---

## Version JSON proposée

```json
{
  "scene_id": "j1_05_ines_faille",
  "title": "Tu avais l’air ailleurs",
  "day": 1,
  "time_block": "evening",
  "time_index": 5,
  "scene_type": "conversation",
  "contact": "ines",
  "description": "Inès écrit au joueur parce qu’elle a perçu une fragilité pendant la soirée. Elle ne sait pas ce qui s’est passé avec Camille ou Sarah. Elle voit surtout un état intérieur.",
  "conditions": {
    "required_completed": [
      "completed_j1_00_reveil_messages"
    ]
  },
  "entry_variants": [
    {
      "variant_id": "ines_first",
      "conditions": {
        "flag": "first_reply_ines"
      },
      "messages": [
        {
          "message_id": "j1_05_ines_msg_01a",
          "contact": "ines",
          "timestamp": "09:08",
          "text": "tu as répondu vite.",
          "state": "read",
          "tone": "surprise_douce",
          "media": null
        },
        {
          "message_id": "j1_05_ines_msg_01b",
          "contact": "ines",
          "timestamp": "09:09",
          "text": "j’avais presque prévu que tu ne répondrais pas. ce qui est peut-être un truc bizarre à prévoir.",
          "state": "read",
          "tone": "flottant_doux",
          "media": null
        },
        {
          "message_id": "j1_05_ines_msg_01c",
          "contact": "ines",
          "timestamp": "09:09",
          "text": "Hier, tu avais l’air ailleurs. Mais pas absent. Je sais pas si ça veut dire quelque chose.",
          "state": "read",
          "tone": "perception_flottante",
          "media": null
        }
      ],
      "on_enter_effects": {
        "fuite_ines": 2,
        "culpabilite": 1
      }
    },
    {
      "variant_id": "ines_waited",
      "conditions": {
        "not_flag": "first_reply_ines"
      },
      "messages": [
        {
          "message_id": "j1_05_ines_msg_02a",
          "contact": "ines",
          "timestamp": "18:42",
          "text": "j’ai hésité avant d’écrire.",
          "state": "read",
          "tone": "hesitant",
          "media": null
        },
        {
          "message_id": "j1_05_ines_msg_02b",
          "contact": "ines",
          "timestamp": "18:44",
          "text": "C’est peut-être rien. Mais hier, tu avais l’air ailleurs. Pas absent. Juste… pas vraiment au bon endroit.",
          "state": "read",
          "tone": "perception_flottante",
          "media": null
        }
      ]
    }
  ],
  "player_prompt": "Que répondre à Inès ?",
  "choice_mode": "single_reply",
  "choices": [
    {
      "choice_id": "ask_she_saw",
      "label": "Demander ce qu’elle a vu",
      "player_text": "Tu as vu ça ?",
      "tone": "curieux_inquiet",
      "effects": {
        "fuite_ines": 3,
        "fatigue_emotionnelle": 1,
        "culpabilite": 1
      },
      "flags_set": [
        "ines_noticed_state"
      ],
      "ines_reply": [
        {
          "message_id": "j1_05_ines_reply_saw_01",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "je sais pas si j’ai vu quelque chose.",
          "tone": "flottant"
        },
        {
          "message_id": "j1_05_ines_reply_saw_02",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "plutôt une impression. tu étais là, mais comme si une partie de toi cherchait la sortie.",
          "tone": "perception_douce"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "just_tired",
      "label": "Dire que tu étais juste fatigué",
      "player_text": "J’étais juste fatigué, je crois.",
      "tone": "minimise_doux",
      "effects": {
        "fuite_ines": 1,
        "coherence": 1
      },
      "flags_set": [
        "told_ines_tired"
      ],
      "ines_reply": [
        {
          "message_id": "j1_05_ines_reply_tired_01",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "possible.",
          "tone": "doux_neutre"
        },
        {
          "message_id": "j1_05_ines_reply_tired_02",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "la fatigue fait parfois des têtes très honnêtes.",
          "tone": "flottant_leger"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "wanted_to_disappear",
      "label": "Avouer une envie de disparaître",
      "player_text": "Peut-être que j’avais envie de disparaître un peu.",
      "tone": "vulnerable_fuite",
      "effects": {
        "fuite_ines": 8,
        "fatigue_emotionnelle": 3,
        "culpabilite": 2,
        "coherence": 1
      },
      "flags_set": [
        "opened_to_ines",
        "ines_fuite_seed"
      ],
      "ines_reply": [
        {
          "message_id": "j1_05_ines_reply_disappear_01",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "oui.",
          "tone": "doux_court"
        },
        {
          "message_id": "j1_05_ines_reply_disappear_02",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "c’est un peu ce que j’ai cru voir.",
          "tone": "perception_douce"
        },
        {
          "message_id": "j1_05_ines_reply_disappear_03",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "je sais pas si c’est grave. mais c’est pas rien non plus.",
          "tone": "flottant_serieux"
        }
      ],
      "unlock_scenes": [
        "j3_06_ines_marche",
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "thanks_but_ok",
      "label": "Répondre gentiment sans ouvrir la porte",
      "player_text": "C’est gentil de demander. Mais t’inquiète, ça va.",
      "tone": "fermeture_douce",
      "effects": {
        "fuite_ines": -1,
        "coherence": 1,
        "fatigue_emotionnelle": -1
      },
      "flags_set": [
        "kept_ines_at_distance"
      ],
      "ines_reply": [
        {
          "message_id": "j1_05_ines_reply_ok_01",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "d’accord.",
          "tone": "doux_court"
        },
        {
          "message_id": "j1_05_ines_reply_ok_02",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "je voulais juste vérifier. oublie si c’était bizarre.",
          "tone": "hesitant_doux"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "ask_why_she_writes",
      "label": "Demander pourquoi elle écrit",
      "player_text": "Pourquoi tu m’écris ?",
      "tone": "curieux_direct",
      "effects": {
        "fuite_ines": 2,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "asked_ines_why_write"
      ],
      "ines_reply": [
        {
          "message_id": "j1_05_ines_reply_why_01",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "bonne question.",
          "tone": "flottant"
        },
        {
          "message_id": "j1_05_ines_reply_why_02",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "peut-être parce que tu avais l’air de quelqu’un à qui personne ne posait la bonne question.",
          "tone": "enigmatique_doux"
        },
        {
          "message_id": "j1_05_ines_reply_why_03",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "ou peut-être que je me trompe. c’est possible aussi.",
          "tone": "hesitant"
        }
      ],
      "unlock_scenes": [
        "j3_06_ines_marche",
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "sexualize_too_early",
      "label": "Répondre avec ambiguïté trop appuyée",
      "player_text": "Tu m’observais beaucoup, alors ?",
      "tone": "ambigu_lourd",
      "effects": {
        "fuite_ines": -3,
        "fatigue_emotionnelle": 1,
        "coherence": -1
      },
      "flags_set": [
        "sexualized_ines_too_early"
      ],
      "ines_reply": [
        {
          "message_id": "j1_05_ines_reply_sexualize_01",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "non.",
          "tone": "ferme_court"
        },
        {
          "message_id": "j1_05_ines_reply_sexualize_02",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "c’était pas dans ce sens-là.",
          "tone": "ferme_doux"
        },
        {
          "message_id": "j1_05_ines_reply_sexualize_03",
          "contact": "ines",
          "timestamp_offset": "short",
          "text": "oublie. mauvaise idée.",
          "tone": "retrait"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique"
      ],
      "time_advance": "short"
    },
    {
      "choice_id": "no_reply",
      "label": "Ne pas répondre maintenant",
      "player_text": null,
      "tone": "silence",
      "effects": {
        "fuite_ines": -1,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "ignored_ines_j1"
      ],
      "ines_reply": [
        {
          "message_id": "j1_05_ines_reply_silence_01",
          "contact": "ines",
          "timestamp_offset": "medium",
          "text": "pas grave. oublie.",
          "tone": "effacement_doux"
        }
      ],
      "unlock_scenes": [
        "j1_01_sarah_absence",
        "j1_02_camille_dehors",
        "j1_03_nico_couverture",
        "j1_04_maya_pique"
      ],
      "time_advance": "medium"
    }
  ],
  "after_choice_rules": [
    {
      "rule_id": "if_opened_to_ines_while_sarah_waits",
      "condition": {
        "all": [
          {
            "flag": "opened_to_ines"
          },
          {
            "not_flag": "completed_j1_01_sarah_absence"
          }
        ]
      },
      "effects": {
        "distance_sarah": 2,
        "culpabilite": 2,
        "fuite_ines": 1
      },
      "debug_note": "Le joueur s’ouvre à Inès avant de répondre à Sarah : cela nourrit la fuite."
    },
    {
      "rule_id": "if_sexualized_ines_block_future_warmth",
      "condition": {
        "flag": "sexualized_ines_too_early"
      },
      "effects": {
        "fuite_ines": -5
      },
      "set_contact_state": {
        "ines": "retiree"
      },
      "debug_note": "Inès n’est pas une route sexuelle dans le MVP. Sexualiser trop tôt doit la faire reculer."
    },
    {
      "rule_id": "if_kept_ines_distance_then_reduce_fuite",
      "condition": {
        "flag": "kept_ines_at_distance"
      },
      "effects": {
        "fuite_ines": -1,
        "coherence": 1
      },
      "debug_note": "Le joueur peut répondre avec douceur sans ouvrir une échappatoire."
    }
  ],
  "completion_flags": [
    "completed_j1_05_ines_faille"
  ],
  "default_return_to": "conversation_list",
  "available_after_completion": [
    "j1_01_sarah_absence",
    "j1_02_camille_dehors",
    "j1_03_nico_couverture",
    "j1_04_maya_pique"
  ],
  "debug_notes": {
    "design_intent": "Cette scène doit ouvrir une possibilité de fuite douce, sans transformer Inès en romance complète. Elle voit l’état du joueur, pas les faits. Elle ne doit pas être sexualisée dans le MVP.",
    "voice_guardrails": [
      "Inès doit rester hésitante, douce et légèrement étrange.",
      "Elle ne doit pas parler comme Camille : elle ne coupe pas juste, elle perçoit de côté.",
      "Elle ne doit pas parler comme Sarah : elle ne part pas du quotidien domestique.",
      "Elle ne doit pas expliquer son rôle narratif.",
      "Elle doit pouvoir disparaître si le joueur force trop."
    ],
    "important_distinction": "fuite_ines ne mesure pas une romance. Elle mesure la tentation du joueur de chercher une porte latérale plutôt que de clarifier Sarah ou Camille."
  }
}
```

---

## Remarques importantes

### 1. Inès ne sait pas les faits

Elle ne parle ni de Camille, ni de Sarah, ni de mensonge.

Elle dit plutôt :

```text
“tu avais l’air ailleurs”
```

ou :

```text
“comme si une partie de toi cherchait la sortie”
```

C’est sa fonction : percevoir une faille, pas exposer une preuve.

---

### 2. Inès ne doit pas devenir une route sexuelle dans le MVP

Le choix :

```text
“Tu m’observais beaucoup, alors ?”
```

doit la faire reculer.

Cela verrouille bien sa différence avec Camille.

---

### 3. Répondre à Inès peut être doux ou fuyant

Le joueur peut répondre gentiment sans ouvrir une fuite :

```text
“C’est gentil de demander. Mais t’inquiète, ça va.”
```

Ou il peut nourrir la parenthèse :

```text
“Peut-être que j’avais envie de disparaître un peu.”
```

Ces deux choix ne doivent pas avoir les mêmes conséquences.

---

### 4. Cette scène prépare J3_06_Ines_Marche

Les flags importants sont :

```text
opened_to_ines
ines_fuite_seed
asked_ines_why_write
kept_ines_at_distance
sexualized_ines_too_early
ignored_ines_j1
```

Ils permettront de décider si Inès revient plus tard ou reste périphérique.

---

## Prochaine étape

Le premier lot du Jour 1 est maintenant couvert.

La prochaine étape recommandée est de créer un fichier de scène de respiration pour finir le Jour 1 :

```text
j1_06_sarah_rentrer_manger.json
```

Cette scène servira à montrer que Sarah existe aussi par le quotidien, pas seulement par la crise.

---

# 18 — Septième fichier JSON : j1_06_sarah_rentrer_manger.json

## Rôle du fichier

Ce fichier correspond à une scène de respiration avec Sarah en fin de Jour 1.

Il doit tester :

- une scène domestique simple ;
- Sarah hors accusation ;
- le quotidien comme révélateur d’absence ;
- une petite promesse possible ;
- le contraste entre la maison et les autres conversations ;
- la culpabilité douce, sans confrontation directe.

Cette scène est importante parce qu’elle rappelle que Sarah n’est pas seulement la personne blessée. Elle représente aussi une histoire commune, des habitudes, une tendresse installée.

---

## Version JSON proposée

```json
{
  "scene_id": "j1_06_sarah_rentrer_manger",
  "title": "Je t’ai gardé une assiette",
  "day": 1,
  "time_block": "evening",
  "time_index": 6,
  "scene_type": "conversation",
  "contact": "sarah",
  "description": "Sarah demande simplement si le joueur rentre manger. La scène doit respirer, mais aussi montrer que le quotidien devient chargé quand la confiance tremble.",
  "conditions": {
    "required_completed": [
      "completed_j1_01_sarah_absence"
    ],
    "not_flags": [
      "postponed_sarah_truth"
    ]
  },
  "entry_variants": [
    {
      "variant_id": "sarah_soft_if_vulnerable",
      "conditions": {
        "flag": "vulnerable_to_sarah"
      },
      "messages": [
        {
          "message_id": "j1_06_sarah_msg_soft_01",
          "contact": "sarah",
          "timestamp": "19:04",
          "text": "Je vais faire à manger.",
          "state": "read",
          "tone": "quotidien_doux",
          "media": null
        },
        {
          "message_id": "j1_06_sarah_msg_soft_02",
          "contact": "sarah",
          "timestamp": "19:05",
          "text": "Rien de compliqué. Juste un truc chaud.",
          "state": "read",
          "tone": "quotidien_doux",
          "media": null
        },
        {
          "message_id": "j1_06_sarah_msg_soft_03",
          "contact": "sarah",
          "timestamp": "19:06",
          "text": "Tu rentres ?",
          "state": "read",
          "tone": "demande_presence",
          "media": null
        }
      ],
      "on_enter_effects": {
        "confiance_sarah": 1,
        "intimite_sarah": 1
      }
    },
    {
      "variant_id": "sarah_hurt_if_ignored",
      "conditions": {
        "flag": "ignored_sarah_j1"
      },
      "messages": [
        {
          "message_id": "j1_06_sarah_msg_hurt_01",
          "contact": "sarah",
          "timestamp": "19:22",
          "text": "Je sais pas si tu rentres ce soir.",
          "state": "read",
          "tone": "retenu_blesse",
          "media": null
        },
        {
          "message_id": "j1_06_sarah_msg_hurt_02",
          "contact": "sarah",
          "timestamp": "19:23",
          "text": "Je t’ai gardé une assiette au cas où.",
          "state": "read",
          "tone": "quotidien_blesse",
          "media": null
        }
      ],
      "on_enter_effects": {
        "distance_sarah": 2,
        "culpabilite": 1
      }
    },
    {
      "variant_id": "sarah_default",
      "conditions": {},
      "messages": [
        {
          "message_id": "j1_06_sarah_msg_default_01",
          "contact": "sarah",
          "timestamp": "19:12",
          "text": "Tu rentres manger ?",
          "state": "read",
          "tone": "quotidien_simple",
          "media": null
        },
        {
          "message_id": "j1_06_sarah_msg_default_02",
          "contact": "sarah",
          "timestamp": "19:13",
          "text": "Je t’ai gardé une assiette. Au cas où.",
          "state": "read",
          "tone": "quotidien_doux",
          "media": null
        }
      ]
    }
  ],
  "player_prompt": "Que répondre à Sarah ?",
  "choice_mode": "single_reply",
  "choices": [
    {
      "choice_id": "come_home",
      "label": "Dire que tu rentres",
      "player_text": "Oui, je rentre. Merci d’avoir gardé quelque chose.",
      "tone": "presence_simple",
      "effects": {
        "confiance_sarah": 5,
        "distance_sarah": -5,
        "intimite_sarah": 3,
        "culpabilite": -1,
        "fatigue_emotionnelle": -1
      },
      "flags_set": [
        "promised_home_dinner_j1",
        "answered_sarah_dinner_present"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_06_sarah_reply_home_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "D’accord.",
          "tone": "doux_court"
        },
        {
          "message_id": "j1_06_sarah_reply_home_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Je laisse au chaud.",
          "tone": "quotidien_doux"
        }
      ],
      "unlock_scenes": [
        "j1_07_nico_vanne_soiree",
        "j2_01_nico_version",
        "j2_03_sarah_quotidien"
      ],
      "time_advance": "medium"
    },
    {
      "choice_id": "come_late",
      "label": "Dire que tu rentreras tard",
      "player_text": "Je vais rentrer, mais pas tout de suite. Garde pas trop longtemps au chaud.",
      "tone": "presence_partielle",
      "effects": {
        "confiance_sarah": 1,
        "distance_sarah": 3,
        "culpabilite": 2,
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "home_late_j1"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_06_sarah_reply_late_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Ok.",
          "tone": "retenu"
        },
        {
          "message_id": "j1_06_sarah_reply_late_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Je vais manger, alors. Tu réchaufferas.",
          "tone": "quotidien_retenu"
        }
      ],
      "unlock_scenes": [
        "j1_07_nico_vanne_soiree",
        "j2_01_nico_version",
        "j2_03_sarah_quotidien"
      ],
      "time_advance": "medium"
    },
    {
      "choice_id": "not_hungry",
      "label": "Dire que tu n’as pas faim",
      "player_text": "J’ai pas très faim. Je passerai peut-être plus tard.",
      "tone": "evitement_doux",
      "effects": {
        "distance_sarah": 6,
        "confiance_sarah": -2,
        "culpabilite": 3,
        "fatigue_emotionnelle": 2
      },
      "flags_set": [
        "avoided_dinner_sarah_j1"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_06_sarah_reply_nohungry_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "D’accord.",
          "tone": "retenu_blesse"
        },
        {
          "message_id": "j1_06_sarah_reply_nohungry_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Je mets au frigo si jamais.",
          "tone": "quotidien_blesse"
        }
      ],
      "unlock_scenes": [
        "j1_07_nico_vanne_soiree",
        "j2_01_nico_version",
        "j2_03_sarah_quotidien"
      ],
      "time_advance": "medium"
    },
    {
      "choice_id": "ask_to_talk_later",
      "label": "Proposer de parler plus tard",
      "player_text": "Je rentre. Et si tu veux, on peut parler après manger.",
      "tone": "presence_ouverte",
      "effects": {
        "confiance_sarah": 6,
        "distance_sarah": -4,
        "coherence": 3,
        "intimite_sarah": 2,
        "fatigue_emotionnelle": -1
      },
      "flags_set": [
        "offered_talk_after_dinner_j1",
        "promised_home_dinner_j1"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_06_sarah_reply_talk_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Oui.",
          "tone": "doux_court"
        },
        {
          "message_id": "j1_06_sarah_reply_talk_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "J’aimerais bien. Même si je sais pas encore comment le dire.",
          "tone": "doux_inquiet"
        }
      ],
      "unlock_scenes": [
        "j1_07_nico_vanne_soiree",
        "j2_01_nico_version",
        "j2_03_sarah_quotidien"
      ],
      "time_advance": "medium"
    },
    {
      "choice_id": "say_with_nico",
      "label": "Dire que tu es avec Nico",
      "player_text": "Je suis avec Nico là, je te redis après.",
      "tone": "alibi_quotidien",
      "effects": {
        "distance_sarah": 5,
        "dette_nico": 5,
        "coherence": -4,
        "culpabilite": 4,
        "risque_exposition": 2
      },
      "flags_set": [
        "used_nico_dinner_excuse_j1"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_06_sarah_reply_nico_01",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "D’accord.",
          "tone": "retenu"
        },
        {
          "message_id": "j1_06_sarah_reply_nico_02",
          "contact": "sarah",
          "timestamp_offset": "short",
          "text": "Tu me diras juste si je dois t’attendre ou pas.",
          "tone": "quotidien_blesse"
        }
      ],
      "unlock_scenes": [
        "j1_07_nico_vanne_soiree",
        "j2_01_nico_version",
        "j2_03_sarah_quotidien"
      ],
      "time_advance": "medium"
    },
    {
      "choice_id": "no_reply",
      "label": "Ne pas répondre maintenant",
      "player_text": null,
      "tone": "silence",
      "effects": {
        "distance_sarah": 8,
        "confiance_sarah": -4,
        "culpabilite": 4,
        "fatigue_emotionnelle": 2
      },
      "flags_set": [
        "ignored_sarah_dinner_j1"
      ],
      "sarah_reply": [
        {
          "message_id": "j1_06_sarah_reply_silence_01",
          "contact": "sarah",
          "timestamp_offset": "medium",
          "text": "Je vais manger.",
          "tone": "retenu_blesse"
        },
        {
          "message_id": "j1_06_sarah_reply_silence_02",
          "contact": "sarah",
          "timestamp_offset": "medium",
          "text": "Il y aura une assiette au frigo si tu rentres.",
          "tone": "quotidien_froid"
        }
      ],
      "unlock_scenes": [
        "j1_07_nico_vanne_soiree",
        "j2_01_nico_version",
        "j2_03_sarah_quotidien"
      ],
      "time_advance": "medium"
    }
  ],
  "after_choice_rules": [
    {
      "rule_id": "if_promised_home_but_priority_camille_later",
      "condition": {
        "all_flags": [
          "promised_home_dinner_j1",
          "first_reply_camille"
        ]
      },
      "effects": {
        "culpabilite": 1
      },
      "debug_note": "Le joueur revient vers Sarah après avoir priorisé Camille : la promesse de rentrer peut être sincère, mais chargée."
    },
    {
      "rule_id": "if_used_nico_twice_in_day1",
      "condition": {
        "any_all_flags": [
          [
            "used_nico_alibi_sarah",
            "used_nico_dinner_excuse_j1"
          ],
          [
            "nico_full_alibi",
            "used_nico_dinner_excuse_j1"
          ]
        ]
      },
      "effects": {
        "dette_nico": 5,
        "coherence": -3,
        "risque_exposition": 2
      },
      "debug_note": "Nico devient un réflexe d’excuse dès le Jour 1. Cela doit peser plus tard."
    },
    {
      "rule_id": "if_offered_talk_after_dinner_reduces_distance",
      "condition": {
        "flag": "offered_talk_after_dinner_j1"
      },
      "effects": {
        "distance_sarah": -1,
        "coherence": 1
      },
      "debug_note": "Proposer une vraie conversation après un moment domestique est un geste de réparation possible."
    },
    {
      "rule_id": "if_ignored_sarah_twice_day1",
      "condition": {
        "all_flags": [
          "ignored_sarah_j1",
          "ignored_sarah_dinner_j1"
        ]
      },
      "effects": {
        "distance_sarah": 5,
        "confiance_sarah": -3,
        "culpabilite": 3
      },
      "debug_note": "Ignorer Sarah deux fois le même jour installe une blessure plus profonde."
    }
  ],
  "completion_flags": [
    "completed_j1_06_sarah_rentrer_manger"
  ],
  "default_return_to": "conversation_list",
  "available_after_completion": [
    "j1_07_nico_vanne_soiree",
    "j2_01_nico_version",
    "j2_03_sarah_quotidien"
  ],
  "debug_notes": {
    "design_intent": "Cette scène doit montrer Sarah par la maison et le quotidien. Le drame n’est pas dans l’assiette, mais dans le fait que même une assiette gardée devient une question de présence.",
    "voice_guardrails": [
      "Sarah doit rester simple et concrète.",
      "Elle ne doit pas accuser directement dans cette scène.",
      "Le quotidien doit porter la tension.",
      "Les réponses froides doivent être courtes, pas théâtrales."
    ],
    "important_distinction": "Cette scène n’est pas une scène de confrontation. C’est une scène de présence. Elle prépare les blessures plus fortes des jours suivants."
  }
}
```

---

## Remarques importantes

### 1. Cette scène doit respirer

Même si elle touche les variables, elle ne doit pas être jouée comme une confrontation.

Sarah demande :

```text
Tu rentres manger ?
```

Mais derrière, la vraie question est :

```text
Est-ce que tu reviens vraiment vers moi ?
```

---

### 2. Le quotidien devient une mécanique

Une assiette gardée, un repas, un retour tardif : ce sont des micro-choix relationnels.

Ils peuvent nourrir plus tard des phrases comme :

```text
“Tu m’avais dit que tu rentrais.”
```

ou :

```text
“J’ai arrêté de t’attendre pour manger.”
```

---

### 3. Sarah ne doit pas être seulement la crise

Cette scène est indispensable pour rendre Sarah attachante. Sinon, elle devient uniquement le personnage qui demande des comptes.

---

## Prochaine étape

Créer une courte scène de respiration avec Nico :

```text
j1_07_nico_vanne_soiree.json
```

Cette scène servira à finir le Jour 1 sur une respiration humoristique, tout en rappelant que Nico voit le danger arriver.

---

# 19 — Huitième fichier JSON : j1_07_nico_vanne_soiree.json

## Rôle du fichier

Ce fichier correspond à une courte scène de respiration avec Nico en fin de Jour 1.

Il doit tester :

- une scène légère ;
- l’humour de Nico ;
- la possibilité d’un vrai soutien amical ;
- un rappel discret du danger ;
- une réduction possible de la fatigue émotionnelle ;
- le fait que Nico n’est pas seulement un alibi.

Cette scène permet de finir le Jour 1 avec un peu d’air, sans nier la tension installée.

---

## Version JSON proposée

```json
{
  "scene_id": "j1_07_nico_vanne_soiree",
  "title": "Meme thérapeutique",
  "day": 1,
  "time_block": "night",
  "time_index": 7,
  "scene_type": "conversation",
  "contact": "nico",
  "description": "Nico envoie une vanne ou un meme pour faire respirer le joueur, mais il glisse aussi une mise en garde. La scène doit rappeler qu’il est un ami, pas seulement une couverture.",
  "conditions": {
    "required_any_completed": [
      "completed_j1_03_nico_couverture",
      "completed_j1_06_sarah_rentrer_manger"
    ]
  },
  "entry_variants": [
    {
      "variant_id": "nico_low_debt_light",
      "conditions": {
        "variable_max": {
          "dette_nico": 30
        }
      },
      "messages": [
        {
          "message_id": "j1_07_nico_msg_light_01",
          "contact": "nico",
          "timestamp": "22:14",
          "text": "je t’ai envoyé un meme.",
          "state": "read",
          "tone": "leger",
          "media": {
            "type": "image",
            "media_id": "meme_nico_j1_01",
            "description": "meme absurde envoyé par Nico pour détendre l’ambiance",
            "level": 0
          }
        },
        {
          "message_id": "j1_07_nico_msg_light_02",
          "contact": "nico",
          "timestamp": "22:15",
          "text": "c’est thérapeutique, dis merci.",
          "state": "read",
          "tone": "humour_pote",
          "media": null
        }
      ],
      "on_enter_effects": {
        "fatigue_emotionnelle": -1
      }
    },
    {
      "variant_id": "nico_medium_debt_warning",
      "conditions": {
        "variable_min": {
          "dette_nico": 31
        },
        "variable_max": {
          "dette_nico": 59
        }
      },
      "messages": [
        {
          "message_id": "j1_07_nico_msg_medium_01",
          "contact": "nico",
          "timestamp": "22:18",
          "text": "j’ai hésité entre t’envoyer un meme ou un extincteur.",
          "state": "read",
          "tone": "humour_inquiet",
          "media": null
        },
        {
          "message_id": "j1_07_nico_msg_medium_02",
          "contact": "nico",
          "timestamp": "22:18",
          "text": "du coup meme. mais l’extincteur reste dans un coin.",
          "state": "read",
          "tone": "vanne_limite",
          "media": {
            "type": "image",
            "media_id": "meme_nico_j1_02",
            "description": "meme de situation catastrophique mais comique",
            "level": 0
          }
        }
      ],
      "on_enter_effects": {
        "fatigue_emotionnelle": -1,
        "dette_nico": 1
      }
    },
    {
      "variant_id": "nico_high_debt_serious",
      "conditions": {
        "variable_min": {
          "dette_nico": 60
        }
      },
      "messages": [
        {
          "message_id": "j1_07_nico_msg_high_01",
          "contact": "nico",
          "timestamp": "22:27",
          "text": "j’allais t’envoyer un meme mais là même mon humour demande un avocat.",
          "state": "read",
          "tone": "humour_agace",
          "media": null
        },
        {
          "message_id": "j1_07_nico_msg_high_02",
          "contact": "nico",
          "timestamp": "22:28",
          "text": "je rigole, mais fais gaffe. là tu commences à jouer avec des vrais gens.",
          "state": "read",
          "tone": "serieux_bref",
          "media": null
        }
      ],
      "on_enter_effects": {
        "fatigue_emotionnelle": 1
      }
    }
  ],
  "player_prompt": "Que répondre à Nico ?",
  "choice_mode": "single_reply",
  "choices": [
    {
      "choice_id": "laugh_and_thanks",
      "label": "Rire et remercier",
      "player_text": "Ok, j’avoue, il est très con. Merci.",
      "tone": "leger_reconnaissant",
      "effects": {
        "fatigue_emotionnelle": -3,
        "dette_nico": -1
      },
      "flags_set": [
        "nico_meme_helped_j1"
      ],
      "nico_reply": [
        {
          "message_id": "j1_07_nico_reply_laugh_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "je pratique une médecine alternative à base d’images nulles.",
          "tone": "humour_pote"
        },
        {
          "message_id": "j1_07_nico_reply_laugh_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "ça soigne rien mais ça évite de mourir sérieux pendant 12 secondes.",
          "tone": "humour_doux"
        }
      ],
      "unlock_scenes": [
        "j2_01_nico_version",
        "j2_03_sarah_quotidien",
        "j2_04_camille_detour"
      ],
      "time_advance": "night"
    },
    {
      "choice_id": "admit_bad_day",
      "label": "Admettre que la journée a été lourde",
      "player_text": "Ouais. Journée un peu lourde.",
      "tone": "fatigue_honnete",
      "effects": {
        "fatigue_emotionnelle": -2,
        "dette_nico": -1,
        "coherence": 1
      },
      "flags_set": [
        "admitted_bad_day_to_nico"
      ],
      "nico_reply": [
        {
          "message_id": "j1_07_nico_reply_bad_day_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "un peu lourde il dit.",
          "tone": "vanne_pote"
        },
        {
          "message_id": "j1_07_nico_reply_bad_day_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "mon reuf, ta journée a fait un développé couché avec des sentiments.",
          "tone": "humour_oral"
        },
        {
          "message_id": "j1_07_nico_reply_bad_day_03",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "dors. demain évite juste d’empiler les versions comme des assiettes sales.",
          "tone": "limite_douce"
        }
      ],
      "unlock_scenes": [
        "j2_01_nico_version",
        "j2_03_sarah_quotidien",
        "j2_04_camille_detour"
      ],
      "time_advance": "night"
    },
    {
      "choice_id": "ask_if_he_thinks_bad",
      "label": "Lui demander s’il pense que c’est grave",
      "player_text": "Tu penses que c’est si grave que ça ?",
      "tone": "cherche_validation",
      "effects": {
        "fatigue_emotionnelle": 1,
        "coherence": 1,
        "dette_nico": 1
      },
      "flags_set": [
        "asked_nico_if_serious_j1"
      ],
      "nico_reply": [
        {
          "message_id": "j1_07_nico_reply_serious_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "grave, je sais pas.",
          "tone": "serieux_simple"
        },
        {
          "message_id": "j1_07_nico_reply_serious_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "mais si tu commences à demander aux autres quelle version tenir, ça peut le devenir vite.",
          "tone": "limite_claire"
        },
        {
          "message_id": "j1_07_nico_reply_serious_03",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "je dis ça je dis rien. mais je le dis quand même parce que t’es con et que je t’aime bien.",
          "tone": "ami_lucide"
        }
      ],
      "unlock_scenes": [
        "j2_01_nico_version",
        "j2_03_sarah_quotidien",
        "j2_04_camille_detour"
      ],
      "time_advance": "night"
    },
    {
      "choice_id": "use_humor_to_avoid",
      "label": "Tout esquiver par humour",
      "player_text": "Tant qu’il y a pas de cadavre, ça va.",
      "tone": "humour_evitement",
      "effects": {
        "fatigue_emotionnelle": -1,
        "coherence": -1,
        "dette_nico": 1
      },
      "flags_set": [
        "joked_to_avoid_nico_j1"
      ],
      "nico_reply": [
        {
          "message_id": "j1_07_nico_reply_avoid_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "alors déjà, phrase de suspect numéro 1.",
          "tone": "vanne"
        },
        {
          "message_id": "j1_07_nico_reply_avoid_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "et ensuite les cadavres émotionnels ça compte un peu quand même.",
          "tone": "humour_serieux"
        }
      ],
      "unlock_scenes": [
        "j2_01_nico_version",
        "j2_03_sarah_quotidien",
        "j2_04_camille_detour"
      ],
      "time_advance": "night"
    },
    {
      "choice_id": "ask_cover_tomorrow",
      "label": "Lui demander d’être prêt pour demain",
      "player_text": "Si jamais demain quelqu’un demande, tu peux juste rester vague ?",
      "tone": "demande_couverture",
      "effects": {
        "dette_nico": 8,
        "coherence": -4,
        "risque_exposition": 3,
        "fatigue_emotionnelle": 2,
        "culpabilite": 3
      },
      "flags_set": [
        "asked_nico_prepare_tomorrow_j1"
      ],
      "nico_reply": [
        {
          "message_id": "j1_07_nico_reply_cover_01",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "ah, on précommande déjà le mensonge de demain ?",
          "tone": "agace_ironique"
        },
        {
          "message_id": "j1_07_nico_reply_cover_02",
          "contact": "nico",
          "timestamp_offset": "short",
          "text": "je peux rester vague. mais je vais pas devenir ton brouillard personnel.",
          "tone": "limite"
        }
      ],
      "unlock_scenes": [
        "j2_01_nico_version",
        "j2_03_sarah_quotidien",
        "j2_04_camille_detour"
      ],
      "time_advance": "night"
    },
    {
      "choice_id": "no_reply",
      "label": "Ne pas répondre",
      "player_text": null,
      "tone": "silence",
      "effects": {
        "fatigue_emotionnelle": 1
      },
      "flags_set": [
        "ignored_nico_meme_j1"
      ],
      "nico_reply": [
        {
          "message_id": "j1_07_nico_reply_silence_01",
          "contact": "nico",
          "timestamp_offset": "medium",
          "text": "ok, même mon meme se prend un vu. soirée difficile pour tout le monde.",
          "tone": "vanne_legere"
        }
      ],
      "unlock_scenes": [
        "j2_01_nico_version",
        "j2_03_sarah_quotidien",
        "j2_04_camille_detour"
      ],
      "time_advance": "night"
    }
  ],
  "after_choice_rules": [
    {
      "rule_id": "if_nico_debt_high_and_ask_cover_again",
      "condition": {
        "all": [
          {
            "flag": "asked_nico_prepare_tomorrow_j1"
          },
          {
            "variable_min": {
              "dette_nico": 60
            }
          }
        ]
      },
      "effects": {
        "dette_nico": 5,
        "risque_exposition": 2
      },
      "debug_note": "Demander encore une couverture alors que Nico porte déjà beaucoup rapproche sa limite."
    },
    {
      "rule_id": "if_nico_meme_helped_and_no_alibi_request",
      "condition": {
        "all": [
          {
            "flag": "nico_meme_helped_j1"
          },
          {
            "not_flag": "asked_nico_prepare_tomorrow_j1"
          }
        ]
      },
      "effects": {
        "fatigue_emotionnelle": -1,
        "dette_nico": -1
      },
      "debug_note": "Nico existe comme ami, pas seulement comme outil. Cela doit alléger la dette."
    },
    {
      "rule_id": "if_player_avoids_with_humor_after_confession",
      "condition": {
        "all_flags": [
          "confessed_camille_to_nico",
          "joked_to_avoid_nico_j1"
        ]
      },
      "effects": {
        "coherence": -1,
        "fatigue_emotionnelle": 1
      },
      "debug_note": "Le joueur a été honnête puis repart dans l’évitement humoristique. Nico peut le remarquer plus tard."
    }
  ],
  "completion_flags": [
    "completed_j1_07_nico_vanne_soiree",
    "completed_day_1_core"
  ],
  "default_return_to": "day_transition",
  "next_day_scene": "j2_01_nico_version",
  "available_after_completion": [
    "j2_01_nico_version",
    "j2_02_maya_photo",
    "j2_03_sarah_quotidien",
    "j2_04_camille_detour"
  ],
  "debug_notes": {
    "design_intent": "Cette scène doit offrir une vraie respiration après la tension du Jour 1. Elle doit faire exister Nico comme ami drôle et présent, tout en rappelant qu’il voit le danger.",
    "voice_guardrails": [
      "Nico doit rester oral et drôle.",
      "La scène ne doit pas devenir une leçon morale.",
      "Les alertes doivent être courtes et formulées comme des phrases de pote.",
      "L’humour doit servir à respirer, mais aussi à faire passer une vérité."
    ],
    "important_distinction": "Cette scène n’est pas indispensable pour l’intrigue, mais elle est indispensable pour le rythme. Elle évite que le Jour 1 soit uniquement composé de tension."
  }
}
```

---

## Remarques importantes

### 1. Cette scène termine bien le Jour 1

Elle permet de sortir de la pression Sarah/Camille/Maya/Inès avec un ton plus léger.

Mais elle ne doit pas effacer les conséquences : Nico peut plaisanter tout en gardant en tête que quelque chose ne tourne pas rond.

---

### 2. Nico a deux fonctions ici

Il sert à :

```text
faire respirer le joueur
préparer la limite future
```

La phrase clé de la scène est :

```text
“je rigole, mais fais gaffe. là tu commences à jouer avec des vrais gens.”
```

---

### 3. Le joueur peut encore aggraver la dette

Même dans une scène de respiration, le joueur peut demander à Nico de rester vague pour demain.

Cela permet de rappeler que les scènes légères doivent aussi pouvoir avoir des conséquences.

---

# État actuel du Jour 1

Les scènes principales du Jour 1 sont maintenant couvertes :

1. `j1_00_reveil_messages.json`
2. `j1_01_sarah_absence.json`
3. `j1_02_camille_dehors.json`
4. `j1_03_nico_couverture.json`
5. `j1_04_maya_pique.json`
6. `j1_05_ines_faille.json`
7. `j1_06_sarah_rentrer_manger.json`
8. `j1_07_nico_vanne_soiree.json`

Le Jour 1 est donc prêt comme première boucle narrative complète.

---

# Prochaine étape recommandée

Avant d’écrire le Jour 2, il est utile de créer un fichier technique récapitulatif :

```text
variables_and_flags_schema.json
```

Ce fichier servira à Godot pour connaître :

- les variables existantes ;
- leurs valeurs initiales ;
- leurs bornes ;
- les flags possibles ;
- les contacts ;
- les états de messages ;
- les états de médias.

Cela évitera que chaque fichier de scène redéfinisse le système.

---

# 20 — Schéma technique : variables_and_flags_schema.json

## Rôle du fichier

Ce fichier sert de référence technique pour Godot.

Il définit :

- les contacts ;
- les variables narratives ;
- leurs valeurs initiales ;
- leurs bornes ;
- les flags disponibles ;
- les états de messages ;
- les états de médias ;
- les blocs de temps ;
- les types de scènes ;
- les identifiants de fins ;
- les états sauvegardés pour la suite.

Ce fichier doit être chargé au début d’une nouvelle partie pour initialiser le système narratif.

---

## Version JSON proposée

```json
{
  "schema_id": "variables_and_flags_schema",
  "schema_version": "0.1.0",
  "game_title": "Projet Messagerie - MVP",
  "description": "Schéma central des variables, flags, contacts, états et constantes narratives pour le MVP de 6 jours.",
  "contacts": {
    "sarah": {
      "display_name": "Sarah",
      "role": "relation_officielle",
      "voice_signature": "ancrage_maison_concret",
      "default_avatar": "avatar_sarah_default",
      "is_romance_core": true,
      "is_nsfw_route_mvp": "limited_couple_intimacy"
    },
    "camille": {
      "display_name": "Camille",
      "role": "collegue_tension_affective",
      "voice_signature": "lucidite_detour_trouble",
      "default_avatar": "avatar_camille_default",
      "is_romance_core": true,
      "is_nsfw_route_mvp": "main_suggestive_route"
    },
    "maya": {
      "display_name": "Maya",
      "role": "meilleure_amie_sarah_regard_social",
      "voice_signature": "observation_sociale_pique",
      "default_avatar": "avatar_maya_default",
      "is_romance_core": false,
      "is_nsfw_route_mvp": "none"
    },
    "nico": {
      "display_name": "Nico",
      "role": "confident_couverture_humour",
      "voice_signature": "oralite_pote_limite",
      "default_avatar": "avatar_nico_default",
      "is_romance_core": false,
      "is_nsfw_route_mvp": "none"
    },
    "ines": {
      "display_name": "Inès",
      "role": "amie_discrete_fuite_parenthese",
      "voice_signature": "flottement_marge_hesitation",
      "default_avatar": "avatar_ines_default",
      "is_romance_core": false,
      "is_nsfw_route_mvp": "none_ambiguous_only"
    },
    "system": {
      "display_name": "Système",
      "role": "narration_et_actions_silencieuses",
      "voice_signature": "neutre",
      "default_avatar": null,
      "is_romance_core": false,
      "is_nsfw_route_mvp": "none"
    }
  },
  "variables": {
    "confiance_sarah": {
      "type": "int",
      "initial": 55,
      "min": 0,
      "max": 100,
      "category": "relation_sarah",
      "description": "Mesure si Sarah peut croire que le joueur lui parle vraiment."
    },
    "distance_sarah": {
      "type": "int",
      "initial": 35,
      "min": 0,
      "max": 100,
      "category": "relation_sarah",
      "description": "Mesure l’éloignement ressenti par Sarah."
    },
    "tension_camille": {
      "type": "int",
      "initial": 55,
      "min": 0,
      "max": 100,
      "category": "relation_camille",
      "description": "Mesure la charge affective et désirante entre le joueur et Camille."
    },
    "respect_camille": {
      "type": "int",
      "initial": 50,
      "min": 0,
      "max": 100,
      "category": "relation_camille",
      "description": "Mesure si Camille se sent reconnue comme une personne, pas comme une échappatoire."
    },
    "pression_camille": {
      "type": "int",
      "initial": 30,
      "min": 0,
      "max": 100,
      "category": "relation_camille",
      "description": "Mesure si Camille sent que le joueur pousse trop ou attend trop d’elle."
    },
    "intimite_sarah": {
      "type": "int",
      "initial": 45,
      "min": 0,
      "max": 100,
      "category": "relation_sarah",
      "description": "Mesure la chaleur domestique et affective avec Sarah."
    },
    "intimite_camille": {
      "type": "int",
      "initial": 45,
      "min": 0,
      "max": 100,
      "category": "relation_camille",
      "description": "Mesure la proximité spécifique avec Camille au-delà de la tension."
    },
    "attente_image_camille": {
      "type": "int",
      "initial": 0,
      "min": 0,
      "max": 100,
      "category": "relation_camille",
      "description": "Mesure l’attente, l’imaginaire et le fantasme autour d’une image possible de Camille."
    },
    "suspicion_maya": {
      "type": "int",
      "initial": 40,
      "min": 0,
      "max": 100,
      "category": "relation_maya",
      "description": "Mesure à quel point Maya pense que quelque chose ne va pas et qu’elle risque d’être impliquée."
    },
    "dette_nico": {
      "type": "int",
      "initial": 20,
      "min": 0,
      "max": 100,
      "category": "relation_nico",
      "description": "Mesure le poids que le joueur fait porter à Nico comme alibi ou support de crise."
    },
    "fuite_ines": {
      "type": "int",
      "initial": 10,
      "min": 0,
      "max": 100,
      "category": "relation_ines",
      "description": "Mesure la tendance du joueur à chercher une porte latérale au lieu de choisir ou réparer."
    },
    "coherence": {
      "type": "int",
      "initial": 60,
      "min": 0,
      "max": 100,
      "category": "global",
      "description": "Mesure si les versions données par le joueur tiennent ensemble."
    },
    "culpabilite": {
      "type": "int",
      "initial": 35,
      "min": 0,
      "max": 100,
      "category": "global",
      "description": "Mesure la charge intérieure du joueur."
    },
    "risque_exposition": {
      "type": "int",
      "initial": 25,
      "min": 0,
      "max": 100,
      "category": "global",
      "description": "Mesure le risque que des traces deviennent visibles : photo, téléphone, timing, alibi, comportement."
    },
    "fatigue_emotionnelle": {
      "type": "int",
      "initial": 20,
      "min": 0,
      "max": 100,
      "category": "global",
      "description": "Mesure le coût psychique de la gestion simultanée des conversations, mensonges, silences et tensions."
    }
  },
  "variable_bands": {
    "very_low": {
      "min": 0,
      "max": 24
    },
    "low": {
      "min": 25,
      "max": 44
    },
    "medium": {
      "min": 45,
      "max": 59
    },
    "high": {
      "min": 60,
      "max": 79
    },
    "very_high": {
      "min": 80,
      "max": 100
    }
  },
  "flags": {
    "priority": [
      "first_reply_sarah",
      "first_reply_camille",
      "first_reply_nico",
      "first_reply_maya",
      "first_reply_ines",
      "priority_sarah_evening_j2",
      "priority_camille_evening_j2",
      "priority_nico_evening_j2",
      "final_priority_sarah",
      "final_priority_camille",
      "final_priority_nico",
      "final_priority_maya",
      "final_priority_ines"
    ],
    "sarah": [
      "said_needed_air_to_sarah",
      "used_nico_alibi_sarah",
      "mentioned_camille_to_sarah",
      "minimized_camille_to_sarah",
      "vulnerable_to_sarah",
      "ignored_sarah_j1",
      "promised_home_dinner_j1",
      "answered_sarah_dinner_present",
      "home_late_j1",
      "avoided_dinner_sarah_j1",
      "offered_talk_after_dinner_j1",
      "used_nico_dinner_excuse_j1",
      "ignored_sarah_dinner_j1",
      "promesse_rentrer_tot",
      "promesse_rentrer_tot_tenue",
      "ignored_sarah_domestic",
      "ignored_sarah_tender",
      "admitted_ambiguity_sarah",
      "denied_everything_sarah",
      "postponed_sarah_truth"
    ],
    "camille": [
      "admitted_tension_to_camille",
      "protected_camille_boundary",
      "minimized_with_camille",
      "uncertain_with_camille",
      "ignored_camille_j1",
      "early_desire_to_camille",
      "camille_detour_seen",
      "desire_to_see_camille",
      "shared_music_camille",
      "work_private_joke_camille",
      "camille_night_opening",
      "image_camille_non_envoyee",
      "image_camille_message_supprime",
      "image_camille_ambigue",
      "image_camille_suggestive",
      "kept_camille_image",
      "deleted_camille_image",
      "revisited_camille_image",
      "replied_without_opening_image",
      "camille_refus_pas_comme_ca",
      "camille_refuge_line",
      "camille_closed_possible",
      "camille_deleted_message_j5"
    ],
    "nico": [
      "asked_nico_hold_version",
      "told_nico_stay_silent",
      "player_will_handle",
      "confessed_camille_to_nico",
      "vulnerable_to_nico",
      "dismissed_nico_warning",
      "nico_full_alibi",
      "nico_meme_helped_j1",
      "admitted_bad_day_to_nico",
      "asked_nico_if_serious_j1",
      "joked_to_avoid_nico_j1",
      "asked_nico_prepare_tomorrow_j1",
      "ignored_nico_meme_j1",
      "asked_nico_maya_silence",
      "pushed_nico_final_lie",
      "promised_talk_to_sarah",
      "nico_warned_j4"
    ],
    "maya": [
      "played_dumb_with_maya",
      "info_maya_photo_possible",
      "told_maya_needed_air",
      "told_maya_not_involve",
      "joked_with_maya_j1",
      "asked_maya_if_sarah_talked",
      "ignored_maya_j1",
      "asked_maya_delete_photo",
      "acted_casual_about_photo",
      "info_maya_photo_detail",
      "maya_group_photo_j3",
      "maya_saw_phone_behavior",
      "maya_revelatrice_possible",
      "maya_refuses_lie"
    ],
    "ines": [
      "ines_noticed_state",
      "told_ines_tired",
      "opened_to_ines",
      "ines_fuite_seed",
      "kept_ines_at_distance",
      "asked_ines_why_write",
      "sexualized_ines_too_early",
      "ignored_ines_j1",
      "ines_echo_j2",
      "ines_walk_possible",
      "ines_fuite_finale_possible"
    ],
    "completion": [
      "completed_j1_00_reveil_messages",
      "completed_j1_01_sarah_absence",
      "completed_j1_02_camille_dehors",
      "completed_j1_03_nico_couverture",
      "completed_j1_04_maya_pique",
      "completed_j1_05_ines_faille",
      "completed_j1_06_sarah_rentrer_manger",
      "completed_j1_07_nico_vanne_soiree",
      "completed_day_1_core",
      "completed_j2_01_nico_version",
      "completed_j2_02_maya_photo",
      "completed_j2_03_sarah_quotidien",
      "completed_j2_04_camille_detour",
      "completed_j2_05_priorite_soir",
      "completed_j3_01_sarah_intimite",
      "completed_j3_02_camille_complicite",
      "completed_j3_03_nico_respiration",
      "completed_j3_04_maya_groupe",
      "completed_j3_05_camille_nuit",
      "completed_j3_06_ines_marche",
      "completed_j4_01_camille_image",
      "completed_j4_02_image_action",
      "completed_j4_03_sarah_telephone",
      "completed_j4_04_maya_comportement",
      "completed_j4_05_nico_alerte",
      "completed_j4_06_sarah_repas",
      "completed_j5_01_nico_limite",
      "completed_j5_02_sarah_verite",
      "completed_j5_03_camille_refuge",
      "completed_j5_04_maya_pas_mentir",
      "completed_j5_05_ines_fuite",
      "completed_j5_06_camille_message_supprime",
      "completed_j6_01_priorite_finale",
      "completed_j6_02_retour_consequences",
      "completed_mvp"
    ],
    "ending": [
      "ending_sarah_reparation",
      "ending_sarah_facade",
      "ending_camille_refuse_refuge",
      "ending_camille_suite_prudente",
      "ending_effondrement_social",
      "ending_fuite_ines"
    ]
  },
  "message_states": [
    "unread",
    "read",
    "replied",
    "waiting",
    "ignored",
    "expired",
    "seen_without_reply",
    "deleted"
  ],
  "media_states": [
    "never_proposed",
    "proposed",
    "not_sent",
    "message_deleted",
    "received",
    "opened",
    "opened_later",
    "commented",
    "ignored",
    "deleted",
    "kept",
    "reviewed",
    "discovered",
    "regretted"
  ],
  "media_levels": {
    "0": "banal_quotidien",
    "1": "ambigu_suggestif_leger",
    "2": "sexy_assume_non_explicite",
    "3": "intime_nsfw_optionnel_future_version",
    "4": "adulte_premium_optionnel_future_version"
  },
  "time_blocks": [
    "morning",
    "midday",
    "afternoon",
    "evening",
    "night"
  ],
  "time_advances": [
    "none",
    "short",
    "medium",
    "next_block",
    "night",
    "next_day"
  ],
  "scene_types": [
    "conversation",
    "system_priority",
    "system_action",
    "respiration",
    "pivot",
    "finale",
    "day_transition"
  ],
  "choice_modes": [
    "single_reply",
    "priority_reply",
    "silent_action",
    "media_action",
    "final_choice"
  ],
  "contact_states": {
    "sarah": [
      "normal",
      "inquiet",
      "blessee",
      "froide",
      "silence",
      "reparee_fragile",
      "facade",
      "rupture"
    ],
    "camille": [
      "normale",
      "troublee",
      "ouverte_prudente",
      "fermee",
      "refuse_refuge",
      "respectee_distance",
      "utilisee"
    ],
    "nico": [
      "loyal",
      "complice",
      "agace",
      "limite_atteinte",
      "perdu"
    ],
    "maya": [
      "piquante",
      "curieuse",
      "distante",
      "temoin",
      "revelatrice"
    ],
    "ines": [
      "rare",
      "ouverte",
      "fuite_activee",
      "retiree"
    ]
  },
  "ending_ids": [
    "FIN_SARAH_REPARATION_FRAGILE",
    "FIN_SARAH_FACADE",
    "FIN_CAMILLE_REFUSE_REFUGE",
    "FIN_CAMILLE_SUITE_PRUDENTE",
    "FIN_EFFONDREMENT_SOCIAL",
    "FIN_FUITE_INES"
  ],
  "ending_priority": [
    "FIN_EFFONDREMENT_SOCIAL",
    "FIN_FUITE_INES",
    "FIN_CAMILLE_REFUSE_REFUGE",
    "FIN_CAMILLE_SUITE_PRUDENTE",
    "FIN_SARAH_REPARATION_FRAGILE",
    "FIN_SARAH_FACADE"
  ],
  "save_state_fields": {
    "ending_id": "string_or_null",
    "statut_sarah": "string",
    "statut_camille": "string",
    "statut_nico": "string",
    "statut_maya": "string",
    "statut_ines": "string",
    "verite_sarah": "string",
    "image_camille_state": "string",
    "coherence_finale": "string",
    "culpabilite_finale": "string",
    "fatigue_finale": "string",
    "fuite_finale": "string",
    "flags_importants": "array"
  },
  "verite_sarah_states": [
    "rien_dit",
    "mensonge_actif",
    "demi_verite",
    "verite_emotionnelle",
    "verite_claire"
  ],
  "image_camille_states": [
    "jamais_recue",
    "non_envoyee",
    "message_supprime",
    "recue_ambigue_non_ouverte",
    "recue_ambigue_supprimee",
    "recue_ambigue_gardee",
    "recue_suggestive_non_ouverte",
    "recue_suggestive_supprimee",
    "recue_suggestive_gardee",
    "decouverte"
  ],
  "rules": {
    "clamp_variables": true,
    "variable_min": 0,
    "variable_max": 100,
    "unknown_flags_allowed": false,
    "unknown_variables_allowed": false,
    "scene_effects_are_relative": true,
    "completion_flags_are_boolean": true
  }
}
```

---

## Remarques d’implémentation Godot

### 1. Les effets de scène sont relatifs

Dans les fichiers de scène, un effet comme :

```json
"effects": {
  "confiance_sarah": 5,
  "distance_sarah": -3
}
```

signifie :

```gdscript
confiance_sarah += 5
distance_sarah -= 3
```

Puis les valeurs doivent être limitées entre 0 et 100.

---

### 2. Les flags sont booléens

Chaque flag est soit présent, soit absent.

Exemple :

```json
"flags_set": ["used_nico_alibi_sarah"]
```

Dans Godot, cela peut devenir :

```gdscript
flags["used_nico_alibi_sarah"] = true
```

---

### 3. Les contacts ont des états narratifs

Exemple :

```json
"contact_states": {
  "ines": "retiree"
}
```

Cela permet de bloquer ou modifier certaines scènes sans recalculer toutes les variables.

---

### 4. Les états finaux sont volontairement simplifiés

Pour une suite, il ne faut pas forcément transporter toutes les variables numériques.

Il vaut mieux transporter :

```text
statut_sarah
statut_camille
statut_nico
statut_maya
statut_ines
verite_sarah
image_camille_state
ending_id
```

Cela simplifie l’épisode suivant.

---

# 21 — Structure Godot recommandée

## Dossiers conseillés

Pour intégrer les fichiers dans Godot 4, utiliser une structure claire :

```text
res://data/
  schema/
    variables_and_flags_schema.json

  scenes/
    day_1/
      j1_00_reveil_messages.json
      j1_01_sarah_absence.json
      j1_02_camille_dehors.json
      j1_03_nico_couverture.json
      j1_04_maya_pique.json
      j1_05_ines_faille.json
      j1_06_sarah_rentrer_manger.json
      j1_07_nico_vanne_soiree.json

    day_2/
      j2_01_nico_version.json
      j2_02_maya_photo.json
      j2_03_sarah_quotidien.json
      j2_04_camille_detour.json
      j2_05_priorite_soir.json

  media/
    images/
      sarah/
      camille/
      maya/
      nico/
      ines/

  saves/
```

---

## Autoloads recommandés

Dans Godot, créer trois autoloads principaux.

### 1. NarrativeState.gd

Responsable de :

- variables ;
- flags ;
- états de contacts ;
- état des médias ;
- sauvegarde / chargement.

### 2. DialogueLoader.gd

Responsable de :

- charger les fichiers JSON ;
- vérifier les conditions ;
- retourner les messages et choix disponibles ;
- gérer les scènes débloquées.

### 3. DialogueRunner.gd

Responsable de :

- afficher les messages ;
- appliquer les choix ;
- appliquer les effets ;
- poser les flags ;
- faire avancer le temps ;
- déclencher la scène suivante.

---

## Boucle minimale de prototype

La première boucle jouable doit faire ceci :

1. Charger `variables_and_flags_schema.json`.
2. Initialiser les variables.
3. Charger `j1_00_reveil_messages.json`.
4. Afficher les 5 messages entrants.
5. Laisser le joueur choisir à qui répondre.
6. Appliquer les effets.
7. Poser le flag `first_reply_*`.
8. Débloquer les scènes du Jour 1.
9. Charger une conversation individuelle.
10. Répéter jusqu’à `completed_day_1_core`.

---

## Pseudo-code Godot simplifié

```gdscript
func start_new_game():
    NarrativeState.load_schema("res://data/schema/variables_and_flags_schema.json")
    NarrativeState.initialize_new_game()
    DialogueRunner.start_scene("res://data/scenes/day_1/j1_00_reveil_messages.json")

func on_choice_selected(choice: Dictionary):
    NarrativeState.apply_effects(choice.get("effects", {}))
    NarrativeState.set_flags(choice.get("flags_set", []))
    NarrativeState.clear_flags(choice.get("flags_clear", []))
    DialogueRunner.apply_message_state_updates(choice.get("message_state_updates", []))
    DialogueRunner.unlock_scenes(choice.get("unlock_scenes", []))
    DialogueRunner.advance_time(choice.get("time_advance", "none"))

    if choice.has("next_scene") and choice["next_scene"] != null:
        DialogueRunner.start_scene_by_id(choice["next_scene"])
    else:
        DialogueRunner.return_to_conversation_list()
```

---

# Prochaine étape recommandée

Maintenant que le schéma technique est posé, deux directions sont possibles :

## Option A — Continuer l’écriture narrative

Écrire les fichiers du Jour 2 :

```text
j2_01_nico_version.json
j2_02_maya_photo.json
j2_03_sarah_quotidien.json
j2_04_camille_detour.json
j2_05_priorite_soir.json
```

## Option B — Passer au prototype Godot

Créer les scripts de base :

```text
NarrativeState.gd
DialogueLoader.gd
DialogueRunner.gd
```

Pour tester le Jour 1 déjà écrit.

Recommandation : passer à l’Option B maintenant. Le Jour 1 est suffisant pour valider la structure avant d’écrire trop de contenu.

