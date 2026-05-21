# T141 — Préparation refonte UX Réveil J1 V2

Objectif futur : remplacer la conversation systémique `j1_00_reveil_v2` par une entrée plus naturelle depuis l’écran Messages.

## Direction UX

1. Au lancement J1 V2, afficher directement l’écran Messages.
2. Les conversations J1 V2 actives apparaissent avec badge `nouveau`.
3. Une note/popup système courte explique :
   > Tu viens de te réveiller. Plusieurs messages t’attendent. La première conversation que tu ouvres donne le ton de ta matinée.
4. Le joueur ouvre naturellement Sarah / Camille / Nico / Maya / Inès depuis la liste.
5. À la première ouverture d’une conversation J1 V2 prioritaire :
   - poser `first_reply_<contact>` pour la conversation ouverte ;
   - poser les `delayed_reply_<autre_contact>` nécessaires pour les autres fils ;
   - conserver le message initial dans la conversation ouverte ;
   - résoudre ensuite l’`entry_variant` cohérente.

## Garde-fous d’implémentation prochaine tâche

- Ne plus dépendre d’un choice node `j1_00_reveil` pour choisir Sarah/Camille/etc.
- Garder une seule source de vérité côté `ConversationState` pour “première conversation J1 V2 ouverte”.
- Ne pas casser les `entry_variants` T136–T138 : la refonte doit seulement déplacer le moment où les flags sont posés.
- Ajouter un test dédié : première ouverture de chaque contact => flags attendus + conversation courante inchangée + badges autres conversations cohérents.
- Prévoir une migration/compatibilité save si `j1_00_reveil_v2` existe déjà dans une sauvegarde.

## Découpage recommandé

T142 possible : `J1 V2 — remplacer Réveil par écran Messages + popup première ouverture`.

Critère de réussite : le playtest ne voit plus “Réveil — cinq messages” comme conversation à choix, mais comprend immédiatement que le premier fil ouvert compte.
