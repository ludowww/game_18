# Jour 2 — Systèmes dynamiques

## 1. Objectif général

Le Jour 2 ne doit pas seulement être une suite de dialogues.

Il doit rendre visibles les conséquences du Jour 1 à travers :

- les états émotionnels ;
- les versions données ;
- les silences ;
- la temporalité ;
- les dettes ;
- les soupçons ;
- les médias ;
- les relations entre personnages.

Principe central : le joueur ne choisit pas seulement des réponses. Il crée un climat relationnel qui modifie progressivement les routes.

Le système dynamique ne doit pas rendre le jeu opaque ou purement mécanique. Les variables doivent soutenir l’écriture, nuancer les variantes, déclencher quelques bifurcations lisibles, et donner au joueur l’impression que le téléphone vit avec les conséquences de ses actes.

## 2. Variables narratives existantes

Les variables suivantes existent déjà dans `V2_VARIABLE_DEFAULTS`.

### `confiance_sarah`

- Mesure : la capacité de Sarah à croire encore le joueur, à rester disponible, à supposer une bonne intention.
- Ne mesure pas : l’amour de Sarah, sa naïveté, ou une validation morale absolue.
- Influence dialogues : ton plus ouvert si haut, plus sec ou retenu si bas.
- Influence routes : peut ouvrir des réponses domestiques tendres, ou au contraire des routes où Sarah demande moins et se protège davantage.

### `distance_sarah`

- Mesure : le retrait émotionnel entre Sarah et le joueur.
- Ne mesure pas : une rupture mécanique immédiate.
- Influence dialogues : Sarah parle moins depuis la demande directe et davantage depuis le constat.
- Influence routes : peut favoriser les silences, les réponses froides, les scènes domestiques plus fragiles.

### `tension_camille`

- Mesure : l’intensité ambiguë ou conflictuelle avec Camille.
- Ne mesure pas : un consentement, une promesse, ou une progression romantique garantie.
- Influence dialogues : Camille peut être plus directe, plus électrique, ou plus prudente selon le contexte.
- Influence routes : peut ouvrir des variantes plus chargées, mais doit rester bornée par `respect_camille` et les flags de limite.

### `respect_camille`

- Mesure : la perception que Camille a du joueur comme quelqu’un qui reconnaît ses limites.
- Ne mesure pas : son attirance, ni une autorisation de pousser plus loin.
- Influence dialogues : respect haut = Camille peut rester proche sans se sentir utilisée ; respect bas = elle reprend le contrôle ou ferme.
- Influence routes : peut bloquer des médias ou variantes ambiguës si trop bas.

### `pression_camille`

- Mesure : le degré de pression émotionnelle ou ambiguë exercée autour de Camille.
- Ne mesure pas : un désir réciproque.
- Influence dialogues : pression haute = Camille nomme l’inconfort ou refuse l’ambiguïté.
- Influence routes : peut empêcher une route plus douce, ou transformer une scène en pose de limite.

### `intimite_sarah`

- Mesure : la proximité domestique et émotionnelle avec Sarah.
- Ne mesure pas : un contenu explicite ou une récompense.
- Influence dialogues : permet des détails quotidiens plus tendres, des souvenirs, des gestes simples.
- Influence routes : peut ouvrir des variantes de réparation discrète ou de présence à la maison.

### `intimite_camille`

- Mesure : le niveau de complicité et de proximité émotionnelle avec Camille.
- Ne mesure pas : une escalade sexuelle automatique.
- Influence dialogues : Camille peut être plus personnelle, moins défensive, mais pas moins lucide.
- Influence routes : peut rendre possibles des médias symboliques ou ambigus si `respect_camille` est aussi haut.

### `attente_image_camille`

- Mesure : l’attente ou la tension autour d’un possible média/image avec Camille.
- Ne mesure pas : une obligation d’envoi.
- Influence dialogues : peut faire exister l’attente, le sous-entendu ou le refus.
- Influence routes : peut déclencher une absence de média, une image symbolique, ou une limite claire selon le climat.

### `suspicion_maya`

- Mesure : l’intensité des soupçons sociaux de Maya.
- Ne mesure pas : une connaissance factuelle de la vérité.
- Influence dialogues : suspicion haute = Maya insiste davantage, pointe des timings, devient moins joueuse.
- Influence routes : peut ouvrir des variantes où le groupe ou la photo reviennent plus frontalement.

### `dette_nico`

- Mesure : ce que le joueur fait porter à Nico : alibi, silence, couverture, charge émotionnelle.
- Ne mesure pas : l’amitié en général.
- Influence dialogues : dette haute = Nico reste drôle mais devient nerveux, passif-agressif ou plus direct.
- Influence routes : peut fragiliser un alibi, déclencher une limite, ou rendre Nico moins disponible.

### `fuite_ines`

- Mesure : l’usage d’Inès comme espace de fuite émotionnelle.
- Ne mesure pas : l’intimité réelle avec Inès.
- Influence dialogues : fuite haute = Inès peut sentir qu’elle sert de refuge plutôt que d’être rencontrée.
- Influence routes : peut ouvrir des scènes calmes mais ambiguës, ou une fermeture si elle est instrumentalisée.

### `coherence`

- Mesure : la stabilité apparente des versions données aux différents personnages.
- Ne mesure pas : la morale du joueur.
- Influence dialogues : cohérence basse = contradictions, hésitations, reformulations défensives.
- Influence routes : peut augmenter les risques d’exposition, fragiliser les alibis, ou modifier les entrées J2.

### `culpabilite`

- Mesure : le poids émotionnel porté par le joueur et perceptible dans ses réponses.
- Ne mesure pas : la culpabilité objective ou juridique.
- Influence dialogues : réponses plus maladroites, excuses trop rapides, évitements.
- Influence routes : peut rendre certains choix plus défensifs ou ouvrir des variantes de réparation.

### `risque_exposition`

- Mesure : le risque que les versions, absences ou timings deviennent visibles socialement.
- Ne mesure pas : une révélation automatique.
- Influence dialogues : les personnages peuvent remarquer davantage de détails périphériques.
- Influence routes : peut déclencher des messages différés, des remarques de groupe, ou une pression Maya/Nico.

### `fatigue_emotionnelle`

- Mesure : l’usure du joueur et du climat relationnel.
- Ne mesure pas : une barre de santé ou une incapacité mécanique.
- Influence dialogues : réponses plus courtes, irritables, défensives ou imprécises.
- Influence routes : peut limiter les options trop propres, accélérer les silences, ou rendre certains choix plus coûteux.

## 3. Seuils narratifs proposés

Seuils simples proposés :

- 0–25 : très bas ;
- 26–45 : fragile ;
- 46–65 : moyen / instable ;
- 66–80 : élevé ;
- 81–100 : critique ou très fort.

Exemples d’usage :

- `confiance_sarah < 40` : Sarah devient plus sèche, moins disponible.
- `distance_sarah > 65` : Sarah parle davantage depuis le retrait que depuis la demande.
- `dette_nico > 60` : Nico aide encore, mais commence à poser des limites.
- `suspicion_maya > 65` : Maya devient plus directe.
- `coherence < 40` : les contradictions deviennent plus visibles.
- `fatigue_emotionnelle > 70` : le joueur peut avoir des réponses plus courtes, défensives ou maladroites.

Important : ces seuils doivent guider les variantes, pas produire une simulation mécanique trop visible. Une phrase ne doit pas sonner comme “stat basse”, mais comme une conséquence naturelle d’un climat.

## 4. Cohérence des versions

Le Jour 2 doit commencer à documenter et exploiter une dynamique de cohérence des versions.

Exemples de frottements :

- Sarah reçoit une version “Nico”.
- Nico n’a pas été prévenu, ou est déjà sous pression.
- Maya remarque une absence, une photo ou un timing.
- Camille entend une minimisation ou sent qu’on la range dans une case commode.

États possibles :

- version stable : les informations données se recoupent assez pour ne pas créer de pression immédiate ;
- version fragile : une version tient, mais dépend d’un silence ou d’une bonne volonté ;
- version contradictoire : deux personnages peuvent relever des éléments incompatibles ;
- version intenable : l’alibi ou la chronologie ne peut plus rester vague sans coût relationnel.

Variables concernées :

- `coherence` ;
- `risque_exposition` ;
- `dette_nico` ;
- `suspicion_maya` ;
- flags de versions Sarah / Camille / Nico.

Usage J2 : les versions données au Jour 1 doivent commencer à circuler, se frotter, ou se contredire. Cela ne veut pas dire révéler la vérité, mais rendre l’équilibre plus instable.

## 5. Alibis

Le système d’alibis doit rester léger.

Alibi Nico possible :

- `used_nico_alibi_sarah` ;
- `nico_alibi_requested` ;
- `asked_nico_hold_version` ;
- `asked_nico_second_cover_j1` ;
- `dette_nico` ;
- `coherence`.

États possibles :

- alibi non utilisé ;
- alibi demandé ;
- alibi fragile ;
- alibi tenu ;
- alibi presque cassé ;
- alibi refusé ou trop coûteux.

Principe : un alibi ne doit pas casser immédiatement. Il doit devenir instable, coûter de la dette, ou créer un risque.

Exemples :

- Nico accepte de rester vague, mais devient nerveux.
- Nico aide encore, mais demande au joueur d’arrêter de l’utiliser.
- Sarah remarque que les versions ne se recoupent pas.
- Maya remarque un trou temporel.

Nico doit rester un ami, pas un outil. Plus l’alibi est sollicité, plus son humour doit montrer le coût.

## 6. Temporalité

La temporalité J2 doit être simple par blocs, pas une horloge réaliste.

Blocs proposés :

- matin ;
- fin de matinée ;
- midi ;
- après-midi ;
- soir ;
- nuit.

Rôle :

- aider le joueur à se repérer ;
- rendre les alibis plus lisibles ;
- faire compter l’ordre des conversations ;
- faire exister les délais et les silences.

Exemples de formulations :

- “ce matin” ;
- “tout à l’heure” ;
- “à midi” ;
- “avant que tu répondes” ;
- “après la photo” ;
- “hier soir”.

Principe : le joueur ne doit pas gérer un planning précis, mais il doit sentir que les absences et les délais laissent des traces.

## 7. Dynamiques entre personnages

Les personnages peuvent influencer indirectement les autres.

Exemples de dynamiques possibles :

- Nico ↔ Sarah : Nico peut être fragilisé si Sarah lui demande une version.
- Maya ↔ Sarah : Maya peut prendre des nouvelles ou faire sentir que le malaise sort du privé.
- Maya ↔ Camille : Maya peut remarquer un timing sans connaître la vérité.
- Nico ↔ joueur : Nico peut passer d’ami léger à ami sous pression.
- Inès ↔ joueur : Inès peut devenir un espace de fuite, mais pas une solution gratuite.

Important : les personnages ne doivent pas devenir omniscients.

Ils peuvent :

- soupçonner ;
- interpréter ;
- demander ;
- se tromper ;
- se rapprocher ;
- s’éloigner.

La dynamique croisée doit passer par des traces visibles : horaires, photos, messages, attitudes, demandes. Pas par une lecture directe des flags.

## 8. Comportements inattendus mais cohérents

Certains comportements peuvent surprendre le joueur, mais ils doivent toujours être cohérents avec les stats et les flags.

Exemples :

- Nico se rapproche de Sarah ou lui répond maladroitement si sa dette est trop haute.
- Sarah ne confronte pas, mais devient silencieuse si la distance est haute.
- Camille refuse soudain l’ambiguïté si la pression est trop haute.
- Maya devient plus sociale si la suspicion monte.
- Inès se ferme si le joueur l’a sexualisée trop tôt.

Ces comportements doivent être rares, lisibles, et préparés par le climat relationnel. Le joueur doit pouvoir se dire “je l’ai provoqué” après coup, même si l’événement surprend sur le moment.

## 9. Médias variables selon les stats

Principe : les médias ne doivent pas être des récompenses sexuelles. Ils doivent refléter le climat relationnel.

Niveaux proposés :

- Niveau 0 : média banal ou neutre ;
- Niveau 1 : média personnel ;
- Niveau 2 : média ambigu ;
- Niveau 3 : média risqué / intime, mais non explicite dans le MVP.

### Sarah

Variables :

- `confiance_sarah` ;
- `distance_sarah` ;
- `intimite_sarah` ;
- `culpabilite`.

Possibilités :

- confiance haute : photo domestique plus tendre ;
- distance haute : photo plus froide ou pratique ;
- culpabilité haute : photo chargée émotionnellement.

Sarah ne doit pas envoyer un média “osé”. Son registre est domestique, intime, quotidien.

### Camille

Variables :

- `tension_camille` ;
- `respect_camille` ;
- `pression_camille` ;
- `intimite_camille` ;
- `early_desire_to_camille`.

Possibilités :

- respect haut + tension haute : média ambigu mais maîtrisé ;
- pression haute + respect bas : Camille n’envoie pas, ou pose une limite ;
- désir trop tôt : pas de récompense, plutôt fermeture ou reprise de contrôle ;
- incertitude : média symbolique, détail de lieu ou souvenir flou.

### Inès

Variables :

- `fuite_ines` ;
- `opened_to_ines` ;
- `kept_ines_at_distance` ;
- `sexualized_ines_too_early`.

Possibilités :

- ouverture douce : image calme, floue, personnelle ;
- fuite haute : média qui ressemble à un refuge ;
- sexualisation trop tôt : Inès se ferme, n’envoie pas de média intime ;
- distance : image neutre ou pas de média.

Inès ne doit pas être transformée en romance explicite trop tôt.

### Maya

Variables :

- `suspicion_maya` ;
- `coherence` ;
- flags photo/timing.

Possibilités :

- suspicion basse : photo de groupe traitée sur le ton de la blague ;
- suspicion haute : Maya insiste davantage ;
- cohérence basse : Maya pointe un détail ;
- joueur défensif : Maya devient plus sèche.

Maya ne doit pas produire une preuve absolue.

### Nico

Variables :

- `dette_nico` ;
- `fatigue_emotionnelle` ;
- `coherence`.

Possibilités :

- dette basse : meme léger ;
- dette haute : meme ou image plus passive-agressive ;
- fatigue haute : Nico tente de faire respirer ;
- cohérence basse : Nico utilise l’humour pour signaler que ça devient bancal.

## 10. Garde-fous sur les médias

Règles importantes :

- plus intime ne veut pas dire plus explicite ;
- une photo plus intime doit être une conséquence relationnelle crédible ;
- aucun média intime ne doit être envoyé si le joueur a mis trop de pression ;
- un média peut être refusé, supprimé, remplacé par une phrase, ou ne jamais arriver ;
- les médias ne doivent pas devenir une mécanique de “récompense” ;
- le consentement émotionnel du personnage prime sur l’envie du joueur ;
- dans le MVP, rester sur du suggestif, symbolique, domestique ou ambigu, jamais explicite.

Un média peut renforcer un climat, mais ne doit pas résoudre une scène à lui seul.

## 11. Messages différés

Des messages peuvent arriver après une autre conversation.

Exemples :

- Sarah écrit après que Nico a été sollicité.
- Nico écrit après avoir été utilisé comme alibi.
- Maya écrit après qu’une photo a été vue.
- Inès écrit après un moment de fatigue ou de silence.

Rôle : faire sentir que le téléphone vit sans attendre le joueur.

Attention : ne pas surcharger. Utiliser les messages différés comme événements rares et significatifs.

Un message différé doit avoir une raison : réaction à un ordre de conversation, à un silence, à un flag fort, ou à un seuil narratif.

## 12. Priorités de journée

Le joueur ne doit pas pouvoir tout traiter parfaitement.

Mécaniques possibles :

- premier contact ouvert ;
- conversation laissée ouverte ;
- réponse tardive ;
- ordre des scènes ;
- moment de la journée.

Principe : le joueur peut répondre à tout le monde, mais pas sans que l’ordre et les délais changent le ton.

La priorité de journée doit rester émotionnelle, pas logistique. Le joueur ne gère pas un agenda : il sent que répondre à quelqu’un maintenant, c’est laisser quelqu’un d’autre attendre.

## 13. MVP dynamique recommandé pour Jour 2

Ne pas tout implémenter d’un coup.

Priorité MVP :

1. Cohérence des versions.
2. Dette Nico.
3. Confiance / distance Sarah.
4. Suspicion Maya.
5. Temporalité matin / midi / soir.

Secondaire :

6. Fuite Inès.
7. Médias variables.
8. Dynamiques croisées entre personnages.
9. Messages différés.

À ne pas faire immédiatement :

- système de timeline complexe ;
- simulation sociale complète ;
- médias à nombreux niveaux pour tous les personnages ;
- gros embranchements irréversibles.

Le MVP dynamique J2 doit d’abord prouver que les variables existantes peuvent modifier le ton et l’ordre des scènes sans rendre l’architecture illisible.

## 14. Tests futurs à prévoir

Prévoir plus tard :

- test de définition des seuils ;
- test de cohérence des variables existantes ;
- test de sélection de variantes selon seuil ;
- test alibi Nico fragile / tenu ;
- test média variable selon stats ;
- test temporalité J2 ;
- test absence d’omniscience ;
- test messages différés non dupliqués.

Ces tests devront aussi vérifier que les conventions J1 restent intactes : `_single_reply_`, choix multiples narratifs, `left_open`, médias, fallback, zoom et absence d’omniscience.
