# T110 — Décider Inès J5 : réserve ou micro-bloc

Statut : DONE
Thread : Narration jours / Roadmap

## Décision

**Option A retenue — Inès reste en réserve J5.**

Aucun JSON Inès J5 n’est écrit maintenant. Inès reste une tension latente issue de J4, utilisable en rappel indirect ou comme promesse de complication future, mais elle ne reçoit pas de conversation active J5 dans le MVP actuel.

## Rationale

J5 est déjà structurellement dense avec :

- **Sarah J5** : poids intime, besoin de présence, gêne douce ;
- **Camille J5** : risque affectif plus coûteux, demande de disponibilité ;
- **Nico J5** : couverture fragile, miroir social ;
- **Maya J5** : témoin social, trace visible.

Le cadrage T106 recommandait une version MVP 8 blocs :

```txt
S5A → C5A → N5A → S5B → C5B → M5A → S5C → C5C
```

T107, T108 et T109 ont déjà produit exactement les pièces nécessaires pour cette structure :

- `s5_block_a/b/c` pour Sarah ;
- `c5_block_a/b/c` pour Camille ;
- `n5_block_a` pour Nico ;
- `m5_block_a` pour Maya.

Ajouter Inès maintenant créerait une variante plus sociale / plus dense, mais avec trois risques :

1. **Dilution du cœur J5**  
   J5 doit faire payer l’équilibre Sarah/Camille. Un bloc Inès actif risque de déplacer l’attention vers une troisième romance au moment où le coût intime doit devenir visible.

2. **Surcharge d’intégration T112**  
   Chaque conversation active ajoute un bloc, un ordre d’unlock, des badges/previews, une vérification de transitions et un playtest runtime. Le MVP est plus sûr avec 8 blocs déjà cadrés.

3. **Meilleur usage d’Inès plus tard**  
   Inès est plus forte si elle reste une tension non traitée : un fil ouvert, pas encore résolu. Son absence active en J5 peut devenir une dette narrative utile pour J6 / fin, plutôt qu’un micro-bloc vite consommé.

## Effet narratif retenu pour Inès

Inès ne disparaît pas : elle reste **latente**.

Elle peut être portée par :

- un flag existant ou futur comme `ines_interest_seeded` ;
- une hésitation du joueur dans Sarah/Camille ;
- un rappel social indirect via Maya/Nico si cohérent ;
- une dette narrative réactivable en J6/Jfin.

Mais T110 décide de ne pas créer `ines_j5_complete.json` et de ne pas ajouter `i5_block_a` à l’intégration J5 actuelle.

## Conséquences Roadmap

La suite reste simple :

- pas de T111 “Écrire Inès J5 micro-bloc” ;
- la relecture cohérence J5 peut passer directement après T110 ;
- l’intégration Godot J5 peut viser la structure 8 blocs déjà prévue.

## Non-changements

T110 ne modifie pas :

- les JSON dialogues ;
- les copies prototype ;
- les scripts Godot ;
- `conversation_blocks.json` ;
- la sauvegarde ;
- l’UX ;
- le schéma T003.

## Next step recommandé

**T111 — Relecture cohérence J5 / J1→J5**.

Objectif T111 : relire ensemble Sarah J5, Camille J5, Nico J5 et Maya J5 pour vérifier :

- cohérence J5 avec le cadrage T106 ;
- voix distinctes ;
- absence de crise finale prématurée ;
- poids Sarah/Camille dominant ;
- Nico/Maya comme pression sociale limitée ;
- Inès conservée en réserve sans impression de trou narratif bloquant.
