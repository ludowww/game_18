# J1 V2 MVP — Conventions validées

## 1. Statut

Le J1 V2 MVP est validé à ce stade.

Cette documentation fige les conventions de dialogue, de navigation, d’état, de non-réponse, de reprises tardives et de médias avant le démarrage du Jour 2. Toute modification qui contredit ces conventions doit faire l’objet d’une tâche dédiée, avec tests ciblés.

## 2. Flux général

Le J1 V2 démarre depuis l’écran Messages.

Le joueur accède d’abord aux cinq scènes cœur J1 V2 : Sarah, Camille, Nico, Maya et Inès. L’ouverture d’une première conversation pose les flags d’entrée et de rythme utilisés par les autres scènes, notamment les familles `first_reply_*` et `delayed_reply_*`.

Les variantes d’entrée permettent aux conversations ouvertes plus tard de tenir compte du fait que le joueur a déjà répondu ailleurs, a tardé, ou a laissé une conversation ouverte. Elles doivent rester lisibles depuis le dernier message affiché.

Après complétion des cinq scènes cœur, les scènes de respiration sont débloquées :

- Sarah repas ;
- Nico respiration.

Une fois ces scènes disponibles, le raccourci `Messages non lus...` doit apparaître pour guider le joueur vers les nouveaux messages sans casser la conversation en cours.

## 3. Dialogues

Les dialogues J1 V2 sont stabilisés. Ils ne doivent pas être réécrits massivement sans raison explicite.

Règles d’écriture :

- chaque personnage doit rester dans son savoir réel ;
- éviter les variantes omniscientes : un personnage ne doit pas parler comme s’il connaissait un flag système ou une scène cachée ;
- les choix doivent répondre clairement au dernier message affiché avant le choice node ;
- les raccords d’ouverture doivent rester naturels quelle que soit la variante d’entrée ;
- les micro-réponses joueur doivent être des choix uniques manuels, pas des réponses automatiques invisibles.

Une variante d’entrée peut refléter une ambiance ou un délai, mais ne doit pas révéler une information que le personnage ne peut pas connaître.

## 4. Choix uniques

Les choix uniques manuels utilisent la convention d’id `_single_reply_`.

Convention obligatoire :

- le node est de `type: "choice"` ;
- son id contient `_single_reply_` ;
- il contient exactement un choix ;
- il ne porte pas d’`effects` ;
- il ne modifie pas de flags ;
- le texte du choix doit être strictement identique au texte du node `sender: "player"` associé ;
- le choix pointe vers ce node player associé.

Usage : faire cliquer le joueur pour valider une micro-réponse sans créer une vraie décision narrative.

Le runtime ne doit pas afficher deux fois la réponse joueur : le node player associé reste la bulle canonique.

Quitter une conversation pendant un choix unique ne doit pas déclencher une non-réponse forte.

## 5. Choix multiples

Les choix multiples représentent une posture narrative réelle.

Ils peuvent incarner notamment :

- mentir ;
- assumer ;
- esquiver ;
- poser une limite ;
- demander une couverture ;
- chercher une fuite ;
- revenir vers une forme de sincérité.

Ils doivent être cohérents avec le dernier message affiché et avec toutes les variantes d’entrée qui peuvent y mener.

Ils ne doivent pas inclure de choix visible du type “ne pas répondre” si la mécanique système `left_open` peut gérer ce silence. La non-réponse est une action de sortie ou d’abandon, pas forcément une ligne de dialogue proposée au joueur.

## 6. Non-réponse / left_open

La non-réponse J1 V2 repose sur l’état système `left_open`.

Règles :

- quitter une conversation pendant un choix unique `_single_reply_` ne déclenche rien de fort ;
- quitter une conversation pendant un choix multiple narratif peut poser `left_open` ;
- l’état conserve notamment `left_open_choice_node`, `left_open_flag` et `late_reply_prepared` ;
- tous les chemins de sortie d’une conversation doivent appeler `mark_current_left_open_if_pending_choice()` ;
- les sorties concernées incluent le retour à Messages, le bouton retour et les changements rapides de conversation.

Pour éviter les boucles de reprise tardive, l’état consommé est conservé via :

- `late_reopen_consumed` ;
- `late_reopen_consumed_flag` ;
- `late_reopen_consumed_choice_node`.

Une reprise déjà consommée pour un même flag et un même choice node ne doit pas être réarmée automatiquement.

## 7. Reprises tardives

Deux reprises tardives sont validées dans le J1 V2 MVP.

### Sarah repas

- Flag : `late_reply_sarah_meal_j1` ;
- choice node concerné : `j1_06_choice_sarah_meal` ;
- reprise : `j1_06_sarah_late_reopen_*`.

La reprise Sarah repas est domestique, blessée, mais pas démonstrative. Elle revient ensuite au choice node existant `j1_06_choice_sarah_meal`.

### Nico respiration

- Flag : `ignored_nico_respiration_j1` ;
- choice node concerné : `j1_07_choice_nico_respiration` ;
- reprise : `j1_07_nico_late_reopen_*`.

La reprise Nico respiration reste légère, amicale et piquante. Elle revient ensuite au choice node existant `j1_07_choice_nico_respiration`.

Chaque reprise tardive est un événement unique. Elle ne doit pas boucler si le joueur ressort à nouveau après l’avoir vue.

## 8. Médias

Les médias narratifs utilisent des nodes `type: "media"`.

Champs attendus :

- `id` ;
- `type: "media"` ;
- `sender` ;
- `media_type` ;
- `asset` ;
- `caption` ;
- `delay` ;
- `next`.

Pour les images :

- `media_type` vaut `"image"` ;
- si `asset` est vide ou introuvable, la `caption` sert de fallback ;
- si la `caption` est vide, le fallback affiché est `[image envoyée]` ;
- une caption entre crochets est considérée comme placeholder technique ;
- si une vraie image est chargée, les placeholders entre crochets ne doivent pas s’afficher sous l’image ;
- une vraie légende narrative peut s’afficher si elle n’est pas un placeholder ;
- une vraie image est cliquable et ouvre un overlay zoom ;
- l’overlay conserve le ratio de l’image et peut être fermé sans changer de scène.

Médias J1 actuels :

- Maya : `product/godot_t004_prototype/assets/media/j1_v2/maya_photo_groupe_j1.png` ;
- Nico : `product/godot_t004_prototype/assets/media/j1_v2/nico_meme_j1.png` ;
- Sarah repas : `product/godot_t004_prototype/assets/media/j1_v2/sarah_assiette_j1.png`.

Ces images sont temporaires et peuvent être remplacées plus tard en conservant les mêmes chemins afin d’éviter de modifier les JSON.

## 9. Tests de référence

Tests clés à relancer dès qu’une tâche touche aux conventions J1 V2 :

- `tests/test_t146_single_reply_nodes.py` ;
- `tests/test_t147_choice_ui_and_player_duplicates.py` ;
- `tests/test_t155_silence_delay_foundation.py` ;
- `tests/test_t157_sarah_meal_late_reopen.py` ;
- `tests/test_t159_late_reopen_does_not_loop.py` ;
- `tests/test_t160_nico_respiration_late_reopen.py` ;
- `tests/test_t162_media_node_support.py` ;
- `tests/test_t166_media_caption_and_zoom.py` ;
- `tools/validate_j1_v2_experimental.py`.

Selon la portée, relancer aussi tous les `tests/test_*.py`.

## 10. À ne pas faire sans tâche dédiée

Ne pas faire sans tâche dédiée et validation explicite :

- supprimer les nodes archive ;
- renommer les ids de choix ;
- modifier les flags existants ;
- modifier les `next` de reprise tardive sans test ciblé ;
- ajouter de l’omniscience dans les variantes d’entrée ;
- ajouter un média qui devient une preuve absolue ;
- transformer un silence système en choix visible si `left_open` peut le gérer ;
- réécrire massivement une scène stabilisée ;
- versionner les fichiers ignorés par `.gitignore` : cache local, `.gd.uid`, métadonnées `.png.import` actuellement non versionnées, doublons de tests locaux.
