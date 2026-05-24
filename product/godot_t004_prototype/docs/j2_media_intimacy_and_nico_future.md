# J2 — Médias, intimité future et dynamiques Nico

## 1. Principe général

Le J2 est stabilisé narrativement. Les prochains enrichissements doivent ajouter de la texture sans casser :

* la cohérence des savoirs ;
* le rythme des révélations ;
* le consentement des personnages ;
* la distinction entre trace, soupçon et preuve.

Règle centrale :
**Une photo ne révèle pas la vérité. Elle révèle le climat.**

Les médias ne doivent jamais devenir :

* des preuves absolues ;
* des récompenses mécaniques ;
* des raccourcis vers l’intimité ;
* des contenus privés partagés sans consentement.

Cette note complète les cadres existants : `j2_story_reframe.md`, `j1_to_j2_information_map.md`, `j2_dynamic_systems.md` et `j2_playable_structure.md`. Elle ne prescrit aucune intégration immédiate dans les JSON.

## 2. État actuel des médias

### J1

* Maya photo de groupe :
  `res://assets/media/j1_v2/maya_photo_groupe_j1.png`
* Nico meme :
  `res://assets/media/j1_v2/nico_meme_j1.png`
* Sarah assiette :
  `res://assets/media/j1_v2/sarah_assiette_j1.png`

### J2

* Maya réutilise actuellement la photo de groupe J1 :
  `res://assets/media/j1_v2/maya_photo_groupe_j1.png`

### Constat

* Maya est déjà médiatisée.
* Sarah a déjà une trace domestique en J1.
* Nico a déjà son meme J1.
* Camille et Inès sont les meilleurs candidats pour un enrichissement média J2 prudent.

## 3. Médias additionnels J2 — candidats

### 3.1 Camille — trace du dehors

Média possible :

* coin de rue vide ;
* banc dehors ;
* lumière de lampadaire ;
* photo floue du lieu ;
* mur / porte / sol du lieu où ils étaient.

Asset proposé :
`res://assets/media/j2_v2/camille_dehors_j2.png`

Caption fallback :
`[photo du dehors envoyée]`

Conditions recommandées :

* `admitted_tension_to_camille`
* ou `protected_camille_boundary`
* ou `uncertain_with_camille`

Rôle :

* rappeler le lieu sans prouver ;
* matérialiser le souvenir ;
* créer une intimité symbolique ;
* ne pas devenir une récompense du désir.

À éviter :

* média si `early_desire_to_camille` sans réparation ;
* média si `pression_camille` trop haute ;
* média si `respect_camille` trop bas ;
* photo explicitement séduisante ;
* photo qui confirmerait objectivement une faute.

Intention :
Camille peut envoyer une trace du dehors si elle se sent reconnue ou respectée. Si elle s’est sentie pressée ou minimisée, elle ne devrait pas offrir ce média.

### 3.2 Inès — image calme

Média possible :

* fenêtre le soir ;
* lumière douce ;
* tasse / thé ;
* coin calme ;
* lampe floue ;
* ciel de nuit vu depuis une fenêtre.

Asset proposé :
`res://assets/media/j2_v2/ines_fenetre_soir_j2.png`

Caption fallback :
`[photo d’un coin calme envoyée]`

Conditions recommandées :

* `opened_to_ines`
* ou `kept_ines_at_distance`
* ou fatigue émotionnelle élevée.

Rôle :

* incarner le calme ;
* offrir une présence douce ;
* ne pas devenir une échappatoire.

À éviter :

* photo romantique ;
* selfie ;
* photo corporelle ;
* média si `sexualized_ines_too_early` ;
* média si le joueur cherche explicitement refuge sans limite.

Intention :
Inès peut montrer un espace calme. Elle ne doit pas s’offrir comme solution.

### 3.3 Sarah — trace domestique

Média possible :

* pull sur la chaise ;
* table rangée ;
* tasse froide ;
* place vide.

Asset proposé futur :
`res://assets/media/j2_v2/sarah_pull_chaise_j2.png`

Caption fallback :
`[photo du pull envoyée]`

Conditions recommandées :

* `late_reply_sarah_meal_j1`
* ou `sarah_j1_domestic_presence`
* ou `used_work_excuse_sarah_j1`
* ou distance Sarah élevée.

Rôle :

* montrer ce qui reste ;
* inscrire la tension dans le quotidien ;
* faire sentir l’absence sans accuser.

À éviter :

* refaire exactement la photo d’assiette J1 ;
* transformer l’image en preuve ;
* faire une image trop dramatique.

Recommandation :
Ne pas intégrer Sarah média immédiatement. À garder pour une extension après playtest.

### 3.4 Maya — recadrage de photo

Média possible :

* détail de photo de groupe ;
* version recadrée ;
* zoom sur une absence ;
* image floutée.

Asset proposé futur :
`res://assets/media/j2_v2/maya_photo_detail_j2.png`

Caption fallback :
`[détail de la photo envoyé]`

Conditions recommandées :

* `maya_photo_possible`
* ou suspicion Maya élevée ;
* ou `played_dumb_with_maya`.

Rôle :

* renforcer l’impression sociale ;
* ne jamais prouver.

À éviter :

* montrer explicitement Camille + joueur ;
* transformer Maya en détective ;
* donner une preuve matérielle.

Recommandation :
Maya a déjà un média J2. Ne pas ajouter de recadrage avant d’avoir testé la version actuelle.

### 3.5 Nico — pas de média J2 immédiat

Nico a déjà le meme J1. En J2, il porte surtout :

* l’alibi ;
* la dette ;
* la limite amicale.

Recommandation :
Ne pas ajouter de média Nico en J2.

## 4. Échelle future d’intimité / explicite

Prévoir une évolution possible vers du contenu plus intime ou explicite, mais en paliers.

### Niveau 0 — neutre

Objets, lieux, groupe, quotidien.

Exemples :

* photo de table ;
* rue vide ;
* groupe ;
* fenêtre.

### Niveau 1 — intime émotionnel

Trace personnelle, souvenir, lieu chargé, détail de présence.

Exemples :

* pull ;
* photo du dehors ;
* lumière de chambre sans personne ;
* message plus vulnérable.

### Niveau 2 — ambigu / suggestif

Cadrage plus intime, tension assumée, sous-entendu. Toujours non explicite.

Exemples :

* photo partielle mais non sexuelle ;
* détail corporel non suggestif ;
* message qui nomme le désir sans image explicite.

### Niveau 3 — sensuel explicite léger

Désir clairement nommé. Photo ou message clairement chargé, mais non pornographique. À réserver à des routes avancées, consenties et préparées.

### Niveau 4 — explicite adulte

Contenu sexuel assumé. Seulement dans des routes adultes, consenties, préparées, et verrouillées par :

* confiance ;
* respect ;
* absence de pression ;
* cohérence relationnelle ;
* consentement narratif clair.

Important :
Ne pas intégrer les niveaux 3 ou 4 dans le J2 MVP.

## 5. Garde-fous consentement / pression / confiance

Règles strictes :

* jamais d’image intime si le personnage a été mis sous pression ;
* jamais d’image intime comme récompense mécanique ;
* jamais d’image intime si le joueur a utilisé l’autre comme fuite ;
* jamais d’image privée partagée sans consentement ;
* jamais de contenu explicite en cas de respect bas ;
* jamais de progression intime si le personnage vient de poser une limite.

### Camille

Peut évoluer vers une route plus sensuelle plus tard si :

* `respect_camille` haut ;
* `pression_camille` basse ;
* tension reconnue ;
* limite respectée.

Doit se fermer si :

* `early_desire_to_camille` sans réparation ;
* pression haute ;
* minimisation répétée ;
* refuge tenté trop brutalement.

### Sarah

Intimité possible plus tard dans le registre :

* confiance ;
* couple ;
* réparation ;
* quotidien ;
* vulnérabilité.

À éviter :

* sexe comme réparation rapide ;
* image “osée” pour compenser la culpabilité ;
* contenu intime si confiance basse.

### Inès

Très prudente. Elle ne doit pas devenir explicite si elle sert de refuge. Une route plus intime n’est possible que si :

* la relation sort du rôle d’échappatoire ;
* le joueur respecte la distance ;
* Inès exprime clairement son propre désir.

### Maya

Maya est surtout sociale / piquante / observatrice. Ne pas la pousser vite vers l’explicite.

Éventuellement plus tard :

* jeu verbal ;
* ambiguïté sociale ;
* flirt léger ;

mais pas au J2.

### Nico

Pas concerné par une route intime avec le joueur dans l’état actuel. Mais il peut avoir une vie sentimentale hors joueur.

## 6. Nico — vie sentimentale hors joueur

Objectif :
Donner à Nico une vie propre, au-delà du rôle ami/alibi.

### 6.1 Nico et ses conquêtes

Nico peut évoquer :

* dates ;
* messages ;
* stories publiques ;
* situations ambiguës ;
* photos non privées ;
* humour sur ses propres flirts.

Rôle narratif :

* montrer qu’il a sa vie ;
* créer un contraste avec le joueur ;
* faire de Nico un miroir imparfait ;
* montrer une autre manière de gérer désir / version / légèreté.

Garde-fous :

* pas de photo intime de conquête partagée sans consentement ;
* pas de nude transmis pour rire ;
* pas de contenu privé exposé ;
* pas de personnage féminin réduit à une image.

Types de médias possibles :

* story publique floutée ;
* photo de verre / bar / table ;
* profil flouté ;
* capture de conversation non explicite ;
* photo de soirée où l’identité n’est pas exposée.

### 6.2 Nico ↔ Maya

Piste très intéressante pour J3/J4.

Pourquoi :

* Maya observe ;
* Nico esquive ;
* leur dynamique peut être piquante ;
* le joueur perd le contrôle d’une partie du groupe ;
* Nico cesse d’être uniquement l’allié / alibi du joueur.

Possibilités :

* Maya écrit à Nico ;
* Nico reçoit une remarque de Maya ;
* Nico cache au joueur qu’il a parlé à Maya ;
* Nico commence à apprécier le regard direct de Maya ;
* Maya utilise Nico comme baromètre social.

Effets narratifs :

* complexifie le groupe ;
* crée une vie hors joueur ;
* rend l’alibi plus fragile ;
* peut rendre Nico moins disponible comme outil.

À ne pas faire trop tôt :

* romance Nico/Maya frontale dès J2 ;
* trahison de Nico ;
* triangle spectaculaire artificiel.

Recommandation :
Préparer Nico ↔ Maya pour J3, pas J2.

### 6.3 Nico ↔ Sarah

Possible mais explosif. À garder pour beaucoup plus tard.

Risque :
Nico peut devenir rival moral ou présence fiable pour Sarah. Cela changerait très fortement l’équilibre.

Recommandation :
Ne pas activer maintenant.

### 6.4 Nico ↔ Inès ou Camille

Pas prioritaire. Camille est déjà centrale avec le joueur. Inès doit rester calme / fuite. À éviter dans le court terme.

## 7. Recommandation d’intégration future

### T187 — intégrer seulement deux médias J2 prudents

À intégrer :

1. Camille — trace du dehors
2. Inès — image calme

Ne pas intégrer encore :

* Sarah média domestique ;
* Maya recadrage photo ;
* Nico conquêtes / médias ;
* contenu explicite.

Raison :
Camille et Inès enrichissent deux axes émotionnels sans casser le social ou le domestique.

### T188 — playtest médias J2

Tester :

* le média ne donne pas une preuve ;
* le média apparaît seulement dans la bonne variante ;
* le média ne s’affiche pas comme récompense sexuelle ;
* le zoom fonctionne ;
* caption fallback correcte ;
* pas d’asset manquant.

### T189 — premières dynamiques Nico futures

Créer une doc ou une scène préparatoire J3 :

* Nico évoque une conquête ;
* Nico reçoit un message de Maya ;
* aucune photo privée non consentie ;
* pas de route explicite immédiate.

## 8. Tests futurs

Pour T187 :

* test média Camille J2 ;
* test média Inès J2 ;
* test absence de média dans les variantes non concernées ;
* test paths assets ;
* test captions fallback ;
* test pas de média Nico J2 ;
* test pas de média Sarah/Maya additionnel si non demandé.

Pour contenu explicite futur :

* test de conditions de consentement ;
* test pression basse ;
* test respect haut ;
* test absence de sexualisation trop tôt ;
* test blocage si personnage se ferme.

## 9. À ne pas faire sans tâche dédiée

* Ne pas ajouter d’asset média réel sans test de path et fallback.
* Ne pas intégrer de média dans les conversations J2 sans valider les conditions par personnage.
* Ne pas introduire de contenu niveau 3 ou 4 dans le J2 MVP.
* Ne pas utiliser Nico comme distributeur de contenus privés.
* Ne pas transformer Maya en preuve vivante ou détective.
* Ne pas faire d’Inès une route de fuite intime.
* Ne pas faire de Camille une récompense de tension.
