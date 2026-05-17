# T008 — Resynchroniser la roadmap locale

Statut : DONE

## Décision

La **Roadmap Discord** reste la source de vérité pour les IDs `Txxx`.

La roadmap locale est réalignée sur les décisions prises dans le thread **Scope MVP / technique**.

Aucun changement fonctionnel n’a été fait au prototype Godot ni au JSON T003.

## Roadmap locale resynchronisée — T001 à T007

### T001 — J1 Camille / scénario prototype

- Thread : Dialogues
- Statut : DONE
- Sortie : conversation jouable brute pour valider la boucle messages → choix → attente.

### T002 — Normalisation du format dialogue

- Thread : Dialogues
- Statut : DONE
- Sortie : J1 Camille structuré avec IDs, speakers, délais, choix, branches et effets simples.

### T003 — Mini-schéma JSON stable Godot

- Thread : Scope MVP / technique
- Statut : DONE
- Sortie : format JSON plat, lisible, stable, suffisant pour Godot.

### T004 — Prototype conversation Godot

- Thread : Scope MVP / technique
- Statut : DONE
- Sortie : prototype Godot minimal lisant le JSON T003 et affichant une conversation interactive.

### T005 — Tester / ajuster l’UX faux smartphone minimal

- Thread : Scope MVP / technique
- Statut : DONE
- Sortie : audit UX statique + ajustements MVP faux smartphone.

### T006 — Polish UX faux smartphone court

- Thread : Scope MVP / technique
- Statut : DONE
- Sortie : polish léger de l’interface messagerie mobile, sans nouveau système.

### T007 — Étendre Camille J1 en contenu complet intégrable

- Thread : Dialogues / Scope MVP
- Statut : DONE
- Sortie : contenu J1 Camille complet intégrable produit et validé.
- Preuves :
  - `narrative/t007_camille_j1_complete.json`
  - `product/godot_t004_prototype/data/camille_j1_complete.json`
  - `product/t007_camille_j1_complete.md`
- Validation : 45 nodes, 6 choice_nodes, 3 end_nodes, aucun duplicate_id, aucun missing_next_target.

## Correction appliquée

Ancien intitulé local de T007 corrigé :

- Ancien : `Créer confident optionnel`
- Nouveau : `Étendre Camille J1 en contenu complet intégrable`

## Hors modification

- Prototype Godot non modifié.
- JSON T003 non modifié.
- Contenu JSON T007 non modifié.
- Fichier Camille J1 prototype non modifié.
- Aucun nouveau système ajouté.
