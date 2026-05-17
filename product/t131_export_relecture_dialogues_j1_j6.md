# T131 — Export relecture dialogues J1→J6

Statut : DONE  
Thread : Roadmap / Dialogues  
Portée : préparation d’un export lisible pour relecture humaine, sans modification JSON

## Déclencheur

Ludo souhaite faire relire les dialogues, car une phrase dès le début paraît incompréhensible.

Phrase repérée au début de Camille J1 :

> Alors… tu fais toujours semblant d’être sérieux le matin ? Le café du coin passe un morceau beaucoup trop dramatique pour 9h, ça aide peut-être.

Diagnostic rapide : la phrase a une intention de ton Camille, mais elle arrive sans contexte suffisant et peut sembler gratuite/confuse comme première accroche.

## Export généré

Deux fichiers ont été créés :

- `product/dialogues_export_lisible_j1_j6.md`
- `product/dialogues_export_simple_j1_j6.txt`

Contenu :

- 20 dialogues actifs J1→J6/finale ;
- messages visibles ;
- choix joueur ;
- IDs de nodes pour signaler précisément une ligne à corriger ;
- source JSON de chaque conversation ;
- organisation par jour et contact.

## Non modifié

- Aucun JSON dialogue ;
- aucune copie Godot data ;
- aucun `conversation_blocks.json` ;
- aucun script Godot ;
- aucun schéma T003 ;
- aucune save/runtime/UX.

## Prochaine étape recommandée

Faire relire l’export, puis ouvrir une tâche de correction ciblée :

**T132 — Corrections lisibilité dialogues après relecture externe**

Format de retour recommandé :

```txt
Jour :
Contact :
ID :
Problème : incompréhensible / trop long / pas naturel / mauvais ton
Suggestion éventuelle :
```
