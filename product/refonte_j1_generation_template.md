# Double Vie — Refonte J1 — Gabarit de génération scène

## Rôle

Ce gabarit sert à générer une scène J1 sans flou, en restant compatible avec la nouvelle vision et avec une conversion future vers le JSON plat Godot.

À utiliser scène par scène. Ne pas générer tout le Jour 1 en une seule passe.

Sources à fournir au générateur :

- `product/mvp_refonte_source_verite.md`
- `product/refonte_j1_structure_scenes.md`
- `product/godot_t004_prototype/data/schema/variables_and_flags_schema.json`

---

# Prompt générique

Je développe un jeu narratif de messagerie sous Godot 4 intitulé “Double Vie”.
Je veux générer uniquement la scène suivante du Jour 1 : `[SCENE_ID]`.

## Contexte canonique

La veille, le joueur était à une soirée avec Sarah, Camille, Maya, Nico et Inès.
Il est sorti prendre l’air. Camille l’a rejoint. Ils sont restés absents environ vingt minutes.
Il ne s’est pas forcément passé de baiser ou de sexe, mais il y a eu un moment émotionnellement trop intime : proximité, silence, phrase ambiguë, trouble non interrompu.
Le joueur est revenu auprès de Sarah avec quelque chose de déplacé intérieurement.

## Règles absolues

- Ne réinvente pas la soirée.
- Ne donne pas au personnage plus d’informations qu’il n’en possède.
- Personne ne doit être omniscient.
- Le silence, le retard et l’ordre des réponses comptent.
- Les messages doivent être naturels, courts ou moyens, façon messagerie.
- Pas de prose trop littéraire.
- Pas de choix “gentil / méchant”.
- Chaque choix important doit avoir effets + flags.
- Les effets utilisent les variables V2.
- Les effets sont relatifs.
- Les flags doivent être explicites et réutilisables.
- Le banal doit révéler la relation.
- La scène doit avoir une fonction jouable, pas seulement une ambiance.

## Variables V2 disponibles

- confiance_sarah
- distance_sarah
- tension_camille
- respect_camille
- pression_camille
- intimite_sarah
- intimite_camille
- attente_image_camille
- suspicion_maya
- dette_nico
- fuite_ines
- coherence
- culpabilite
- risque_exposition
- fatigue_emotionnelle

## Personnage actif

`[CONTACT]`

Ce que ce personnage sait :
`[CONTACT_KNOWS]`

Ce que ce personnage ignore :
`[CONTACT_IGNORES]`

Fonction de la scène :
`[SCENE_FUNCTION]`

Ton attendu :
`[VOICE_RULES]`

## Format de sortie attendu

Produis une version lisible, pas encore du JSON runtime.

Utilise ce format :

```text
SCENE_ID:
CONTACT:
FONCTION:
CONNAISSANCES DU CONTACT:
IGNORANCES DU CONTACT:
TON:

MESSAGES:
[node_id] Contact : texte
[node_id] Joueur : texte

CHOIX:
- [choice_id] Texte joueur
  Effets : { ... }
  Flags : [ ... ]
  Suite : [node_id ou scene_id]
  Intention : ...

SORTIES POSSIBLES:
- ...

NOTES DE VALIDATION:
- ...
```

## Contraintes de taille

- 8 à 18 messages visibles maximum pour une scène principale.
- 3 à 5 choix principaux maximum.
- 1 ou 2 relances après choix, pas plus.
- Retour vers des sorties communes si possible.
- Pas d’arbre exponentiel.

---

# Fiches préremplies J1

## `j1_01_sarah_absence`

CONTACT : Sarah

CONTACT_KNOWS :
- Le joueur était moins présent pendant la soirée.
- Il s’est absenté.
- Camille était absente à un moment proche.
- Nico a donné une explication floue.
- Le joueur est revenu changé.

CONTACT_IGNORES :
- Ce qui s’est dit dehors.
- S’il y a eu contact physique.
- Ce que Camille pense du moment.
- Ce que le joueur dit aux autres.

SCENE_FUNCTION :
Sarah demande où le joueur était et pourquoi il est revenu différent. La scène fixe la première version donnée à Sarah.

VOICE_RULES :
Sarah part du concret : café, clés, retour, fatigue, téléphone, silence. Elle est douce ou blessée, pas policière. Elle veut savoir si elle invente son malaise.

---

## `j1_02_camille_dehors`

CONTACT : Camille

CONTACT_KNOWS :
- Elle était dehors avec le joueur.
- Le moment n’était pas neutre.
- Une limite émotionnelle a été touchée.
- Le joueur peut minimiser par peur ou confort.

CONTACT_IGNORES :
- Ce que Sarah sait.
- Ce que le joueur a dit à Sarah.
- Ce que Maya a vu.
- Jusqu’où Nico est impliqué.

SCENE_FUNCTION :
Camille demande si le joueur va faire comme si le moment dehors était banal. La scène définit reconnaissance, minimisation, limite ou désir trop direct.

VOICE_RULES :
Camille est précise, oblique, lucide. Elle peut être attirante, mais elle ne devient pas une récompense. Elle refuse d’être un refuge pratique.

---

## `j1_03_nico_couverture`

CONTACT : Nico

CONTACT_KNOWS :
- Il a donné une explication improvisée.
- Le joueur est troublé par Camille.
- Sarah ou Maya pourraient lui poser des questions.
- Son explication peut devenir fragile.

CONTACT_IGNORES :
- Ce qui s’est réellement passé dehors.
- Ce que le joueur a dit à Sarah.
- Ce que Camille attend.
- Ce que Maya a vu.

SCENE_FUNCTION :
Nico rappelle qu’il a couvert ou simplifié l’absence du joueur. Il peut aider, mais il ne veut pas devenir un alibi permanent.

VOICE_RULES :
Nico est oral, drôle, familier. Il peut sortir une phrase sérieuse après une vanne. Il n’est ni tutoriel ni juge moral.

---

## `j1_04_maya_pique`

CONTACT : Maya

CONTACT_KNOWS :
- Le joueur et Camille ont été absents ou difficiles à situer.
- Sarah a senti quelque chose.
- Nico a donné une explication pas totalement solide.
- Le timing est suspect.

CONTACT_IGNORES :
- Le contenu du moment dehors.
- La vérité émotionnelle complète.
- La version donnée à Sarah.
- L’intention de Camille.

SCENE_FUNCTION :
Maya signale une incohérence sociale : timing, absence, photo, comportement du joueur ou de Camille. Elle voit assez pour gêner, pas assez pour savoir.

VOICE_RULES :
Maya est courte, piquante, sociale, rapide. Elle utilise l’humour comme pression légère. Elle protège Sarah sans devenir policière.

---

## `j1_05_ines_faille`

CONTACT : Inès

CONTACT_KNOWS :
- Le joueur avait l’air ailleurs.
- Il semblait triste ou déplacé.
- Il cherchait peut-être une sortie.

CONTACT_IGNORES :
- La tension avec Camille.
- L’état du couple avec Sarah.
- Le rôle de Nico.
- Les observations de Maya.

SCENE_FUNCTION :
Inès écrit peu mais remarque l’état intérieur du joueur. Elle ouvre une porte latérale, sans route romantique complète.

VOICE_RULES :
Inès est douce, hésitante, légèrement étrange. Elle laisse de la place. Elle ne devient pas une nouvelle fille disponible.

---

## `j1_06_sarah_rentrer_manger`

CONTACT : Sarah

CONTACT_KNOWS :
- Ce qui a été dit dans `j1_01_sarah_absence`.
- Son propre malaise.
- Les habitudes domestiques du couple.

CONTACT_IGNORES :
- Ce que le joueur a dit à Camille, Nico, Maya ou Inès.

SCENE_FUNCTION :
Respiration domestique avec Sarah. La scène rappelle que Sarah n’est pas seulement une source de reproche.

VOICE_RULES :
Sarah parle de maison, repas, assiette, café, retour, fatigue. La scène ne doit pas devenir une deuxième interrogation sur Camille.

---

## `j1_07_nico_vanne_soiree`

CONTACT : Nico

CONTACT_KNOWS :
- Ce qui a été dit dans `j1_03_nico_couverture`.
- Que le joueur est en tension.
- Que l’alibi peut grossir.

CONTACT_IGNORES :
- Les versions données aux autres après sa première conversation.

SCENE_FUNCTION :
Respiration amicale avec Nico. Humour, meme, pizza ou soirée, puis rappel léger du danger.

VOICE_RULES :
Nico est oral, drôle, direct. Une phrase sérieuse peut tomber après une vanne. Il ne doit pas devenir un coach narratif.
