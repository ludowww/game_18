# J3 — Médias et montée d’intimité future

## 0. Statut et périmètre

Document de design pour T201. Il cadre les médias additionnels possibles du Jour 3 V2 et la montée progressive de l’intimité, sans implémentation.

Périmètre strict :

- aucune modification JSON ;
- aucune modification script/runtime ;
- aucun asset ajouté ;
- aucun média intégré ;
- aucun test ajouté ou modifié.

Documents respectés :

- `docs/j3_design_brief.md` ;
- `docs/j3_v2_dialogue_audit.md` ;
- `docs/j3_orality_polish_audit.md` ;
- `docs/j2_media_intimacy_and_nico_future.md` ;
- `docs/j2_dynamic_systems.md`.

J3 V2 est désormais complet côté dialogues/runtime/polish. T201 sert à éviter que T202 ajoute des images comme bonus mécanique ou comme preuve involontaire.

## 1. Principe général

J3 est le jour des **contradictions contrôlées**.

Les médias J3 ne doivent pas révéler une vérité. Ils doivent rendre le climat plus concret.

Règle centrale :

> Une image ne doit pas prouver. Elle doit déplacer l’ambiance.

Pour J3 :

- médias possibles ;
- niveau intime légèrement supérieur à J2 ;
- pas de contenu explicite ;
- pas de récompense sexuelle ;
- pas de preuve matérielle ;
- pas de photo privée non consentie ;
- pas d’image qui rend un personnage omniscient.

Un média J3 doit donc être une **trace** ou un **déplacement de regard**, jamais un verdict.

## 2. État actuel des médias

### J1

- Maya photo de groupe :
  `res://assets/media/j1_v2/maya_photo_groupe_j1.png`
- Nico meme :
  `res://assets/media/j1_v2/nico_meme_j1.png`
- Sarah assiette :
  `res://assets/media/j1_v2/sarah_assiette_j1.png`

### J2

- Camille dehors :
  `res://assets/media/j2_v2/camille_dehors_j2.png`
- Inès fenêtre / calme :
  `res://assets/media/j2_v2/ines_fenetre_soir_j2.png`
- Maya réutilise la photo de groupe J1 :
  `res://assets/media/j1_v2/maya_photo_groupe_j1.png`

### J3

- Aucun média encore intégré.

Constat : J1/J2 ont déjà installé l’usage prudent des images comme traces de quotidien, lieu, groupe ou calme. J3 peut monter d’un cran, mais seulement par concrétisation du climat, pas par sexualisation.

## 3. Rôle des médias J3

Les médias J3 doivent servir trois objectifs.

### 3.1 Concrétiser les gestes

Sarah parle de gestes. Un média domestique peut matérialiser :

- présence ;
- absence ;
- place ;
- quotidien ;
- attention portée aux détails.

Le média ne doit pas dire : “Sarah a raison” ou “le joueur a tort”. Il doit seulement montrer ce qu’elle regarde, ce qui reste dans la pièce, ce qui rend l’attente concrète.

### 3.2 Montrer que les autres ont une vie hors joueur

Nico commence à exister hors du rôle d’alibi. Un média de sortie / bar / table peut montrer :

- qu’il répond tard pour une vraie raison ;
- qu’il a une vie sociale ;
- que le joueur n’est pas le centre permanent ;
- qu’une amitié ne donne pas un accès illimité.

Le média ne doit pas révéler une relation identifiable, ni transformer Nico en quelqu’un qui expose les autres.

### 3.3 Préparer une montée d’intimité future

Camille peut devenir l’axe principal de tension sexuelle future, mais pas par une image sexy immédiate.

La montée doit rester :

- consentie ;
- liée au respect ;
- liée à la pression basse ;
- liée au désir nommé sans forcer ;
- conditionnée par les limites tenues.

J3 doit préparer le terrain par le langage, les limites et les choix, pas consommer la tension par une récompense visuelle.

## 4. Échelle d’intimité

Cette échelle reprend la logique posée par J2 et la précise pour J3+.

### Niveau 0 — neutre

Objets, lieux, groupe, quotidien.

Exemples :

- table ;
- tasse ;
- rue ;
- photo de groupe ;
- verre ;
- serviette ;
- ticket.

Usage : acceptable tôt, si le média sert le rythme ou la scène.

### Niveau 1 — intime émotionnel

Trace personnelle, lieu chargé, objet qui dit l’absence ou la présence.

Exemples :

- pull ;
- tasse laissée ;
- coin de rue du moment ;
- fenêtre ;
- lumière du soir ;
- place vide.

Usage : acceptable en J3 avec prudence, surtout Sarah/Nico si le média clarifie le climat sans trancher la vérité.

### Niveau 2 — suggestif / ambigu

Cadrage plus intime, désir implicite, détail chargé mais non explicite.

Exemples :

- photo floue d’un lieu tardif ;
- détail de main / manche / veste ;
- cadrage proche mais non corporel explicite ;
- message qui nomme le trouble.

Usage : à préparer pour J4/J5, pas comme intégration J3 immédiate. Peut concerner Camille plus tard si respect haut et pression basse.

### Niveau 3 — sensuel adulte

Désir clairement nommé, tension corporelle, photo ou message chargé mais non pornographique.

Usage : à réserver plus tard, dans une route adulte préparée, consentie et verrouillée par les variables de respect/pression/cohérence.

### Niveau 4 — explicite adulte

Contenu sexuel assumé.

Usage : interdit en J3 MVP. Seulement dans des routes adultes, consenties, préparées et verrouillées, si le projet décide d’aller jusque-là.

## 5. Médias J3 recommandés

### 5.1 Sarah — trace domestique

Rôle : concrétiser la thématique des gestes.

Média possible :

- tasse sur table ;
- pull / chaise ;
- place vide ;
- table du matin ;
- objet domestique simple.

Asset proposé :

`res://assets/media/j3_v2/sarah_trace_matin_j3.png`

Caption fallback :

`[photo du matin envoyée]`

Scène recommandée : Sarah J3, uniquement dans une branche positive ou prudente :

- après le choix `j3_01_sarah_show_with_actions` ;
- ou dans une future suite conditionnée par `j3_sarah_promises_actions`.

Insertion T202 recommandée, si intégration immédiate : insertion légère dans la réponse Sarah après le choix “gestes visibles”.

Rôle narratif :

- elle ne prouve rien ;
- elle montre ce que Sarah regarde ;
- elle matérialise le quotidien où les gestes devront exister ;
- elle ne doit pas culpabiliser gratuitement.

À éviter :

- photo trop triste / mélodramatique ;
- photo de lit sexualisée ;
- image qui transforme Sarah en juge ;
- image qui sert de preuve de faute ;
- image qui donne l’impression que Sarah met le joueur face à un dossier.

### 5.2 Nico — vie hors joueur

Rôle : montrer que Nico existe hors du joueur.

Média possible :

- verre sur table ;
- bar flou ;
- table de café ;
- ticket / serviette ;
- lumière de soirée ;
- photo non identifiable d’un lieu social.

Asset proposé :

`res://assets/media/j3_v2/nico_sortie_floue_j3.png`

Caption fallback :

`[photo de sortie envoyée]`

Scène recommandée : Nico J3, branche `j3_02_nico_deflect_to_his_life`.

Insertion possible après :

> disons que quelqu’un m’a écrit.

Avant :

> et pour une fois, ce n’était pas pour me demander de faire le pare-feu humain.

Rôle narratif :

- le joueur comprend que Nico a sa propre vie ;
- le média ne montre pas une conquête identifiable ;
- le média ne révèle pas Maya ;
- le média ne montre pas une photo privée ;
- le média renforce la limite : Nico n’est pas un outil.

À éviter :

- photo de femme identifiable ;
- capture privée ;
- image sexy ;
- nude / sous-vêtement ;
- contenu qui ferait de Nico quelqu’un qui expose les autres ;
- indice trop clair sur une relation Nico ↔ Maya.

### 5.3 Camille — tension future, pas T202 immédiat

Camille est l’axe principal possible de tension sexuelle future.

Mais J3 ne doit pas encore intégrer d’image plus suggestive, car :

- elle a déjà eu le média dehors J2 ;
- J3 Camille teste les limites ;
- une image maintenant risquerait d’être lue comme récompense ;
- la tension Camille doit être gagnée par respect et retenue, pas par déblocage visuel.

Médias futurs possibles :

- lumière d’un lieu ;
- détail de veste ;
- main sur tasse ;
- porte / couloir / rue ;
- cadrage plus proche mais non corporel explicite.

Conditions futures recommandées :

- `respect_camille` haut ;
- `pression_camille` basse ;
- `j3_camille_recognized_without_using` ;
- ou `j3_camille_boundary_kept`.

Interdits si :

- `j3_camille_pressure_rises` ;
- `j3_camille_tension_reopened` sans respect suffisant ;
- `j3_camille_minimized_again` ;
- pression haute ;
- le joueur utilise Camille comme refuge instrumental.

### 5.4 Maya — pas de média J3 immédiat

Maya parle de signaux sociaux. Une image risquerait de devenir une preuve ou un indice trop fort.

Recommandation : pas de média Maya J3 en T202.

Futur possible :

- story floue ;
- groupe ;
- détail social non probant ;
- photo de lieu collectif sans information décisive.

À réserver seulement si on veut renforcer la circulation sociale en J4, et jamais comme preuve que Maya “sait”.

### 5.5 Inès — pas de média J3 immédiat

Inès a déjà eu une image calme en J2. En J3, elle pose la limite entre présence et refuge.

Recommandation : pas de média Inès J3 en T202.

Raison : un nouveau média risquerait de redevenir une récompense visuelle de calme ou un refuge trop confortable.

Futur possible : une image Inès ne devrait arriver que si la relation sort clairement du rôle d’échappatoire.

## 6. Montée sexuelle future

Important : la montée sexuelle doit être préparée, mais pas consommée trop tôt.

Elle doit venir de :

- respect ;
- consentement ;
- limites tenues ;
- désir nommé ;
- pression basse ;
- cohérence élevée ;
- initiative ou désir propre du personnage concerné.

Elle ne doit jamais venir de :

- culpabilité ;
- fuite ;
- pression ;
- dette ;
- manipulation ;
- récompense de choix “drague” ;
- escalade mécanique après un bon score.

### Sarah

Intimité possible plus tard :

- conjugale ;
- domestique ;
- vulnérable ;
- basée sur confiance ;
- liée à des gestes cohérents, pas à une promesse isolée.

Interdit :

- sexe comme réparation rapide ;
- photo osée pour compenser la culpabilité ;
- image intime si confiance basse ;
- image intime si la distance Sarah est haute et non traitée.

### Camille

Axe principal de tension sexuelle future.

Progression recommandée :

1. J3 : tension verbale, limites, pas de média sexy.
2. J4 : désir plus nommé si respect haut.
3. J5+ : média plus suggestif possible si pression basse et consentement clair.

Conditions nécessaires :

- `respect_camille` haut ;
- `pression_camille` basse ;
- pas de minimisation ;
- pas de refuge instrumental ;
- Camille exprime elle-même son désir, pas seulement le joueur.

### Inès

Montée sexuelle très prudente.

Elle ne doit pas devenir explicite si elle sert de refuge.

Conditions nécessaires :

- `fuite_ines` basse ;
- distance respectée ;
- relation sortie du rôle d’échappatoire ;
- Inès exprime un désir propre.

### Maya

Pas de montée sexuelle immédiate.

Possible futur :

- flirt verbal ;
- jeu social ;
- ambiguïté piquante.

Mais pas J3/J4 immédiat sauf décision forte de design. Maya doit d’abord rester un vecteur de circulation sociale et de lecture des signaux.

### Nico

Nico peut avoir une vie sentimentale / sexuelle hors joueur.

Garde-fou :

- jamais de média intime non consenti ;
- jamais de photo privée affichée ;
- jamais de conquête réduite à une image ;
- jamais de révélation indirecte de Maya par média.

## 7. Recommandation T202

Intégrer seulement deux médias J3.

### Sarah

Node proposé :

`j3_01_sarah_media_morning_trace_001`

Asset :

`res://assets/media/j3_v2/sarah_trace_matin_j3.png`

Caption :

`[photo du matin envoyée]`

Insertion recommandée : dans la branche `j3_01_sarah_show_with_actions`, après :

> Alors je vais regarder les gestes.

Avant :

> Pas pour te piéger.

Intention : rendre les gestes concrets, sans preuve ni culpabilisation.

### Nico

Node proposé :

`j3_02_nico_media_social_life_001`

Asset :

`res://assets/media/j3_v2/nico_sortie_floue_j3.png`

Caption :

`[photo de sortie envoyée]`

Insertion recommandée : dans la branche `j3_02_nico_deflect_to_his_life`, après :

> disons que quelqu’un m’a écrit.

Avant :

> et pour une fois, ce n’était pas pour me demander de faire le pare-feu humain.

Intention : montrer que Nico a une vie propre, sans exposer quelqu’un d’autre.

### Ne pas intégrer en T202

- Camille média J3 ;
- Maya média J3 ;
- Inès média J3 ;
- contenu suggestif / explicite ;
- média qui sert de preuve ;
- média qui sexualise un personnage avant consentement clair.

## 8. Tests futurs T202

Prévoir des tests dédiés pour vérifier :

- assets PNG valides ;
- media node Sarah J3 uniquement dans branche gestes ;
- media node Nico J3 uniquement dans branche vie propre ;
- captions fallback présentes ;
- pas de média J3 Camille/Maya/Inès ;
- pas d’asset explicite ;
- choix/player inchangés ;
- structure J3 non cassée ;
- runtime non modifié sauf si T202 l’autorise explicitement ;
- aucun savoir nouveau introduit par les médias ;
- aucun média privé non consenti.

## 9. Conclusion

J3 peut accueillir deux médias prudents :

- Sarah pour matérialiser les gestes ;
- Nico pour montrer sa vie propre.

La montée sexuelle doit être préparée, mais rester future.

Camille doit devenir l’axe principal de tension sexuelle possible, à condition que le joueur respecte ses limites. J3 ne doit pas encore intégrer de média explicitement suggestif.

T202 devrait donc rester une intégration média limitée, testée, non sexuelle, non probante et cohérente avec les savoirs des personnages.
