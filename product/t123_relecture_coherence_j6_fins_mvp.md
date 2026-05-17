# T123 — Relecture cohérence J6 / fins MVP

Statut : DONE  
Thread : Dialogues / Roadmap  
Portée : relecture cohérence narrative + validation statique J6/fins, sans patch JSON ni intégration Godot

## Objectif

Relire l’ensemble J6 + fins MVP après écriture :

- T120 — Sarah/Camille J6 résolution MVP ;
- T121 — Nico/Maya/Inès J6 pression finale courte ;
- T122 — fins MVP / conversation finale dédiée.

T123 vérifie que J6 respecte le cadrage post-polish :

- voix personnages distinctes ;
- pas de retour à un tunnel dramatique pur ;
- pas de vocabulaire conceptuel visible ;
- pas de révélation totale obligatoire ;
- fins lisibles, courtes, rejouables ;
- structure prête pour intégration T124.

## Corpus relu

JSON J6 / fins :

- `narrative/t120_sarah_j6_complete.json`
- `narrative/t120_camille_j6_complete.json`
- `narrative/t121_nico_j6_complete.json`
- `narrative/t121_maya_j6_complete.json`
- `narrative/t121_ines_j6_complete.json`
- `narrative/t122_finales_mvp_complete.json`

Copies Godot data vérifiées :

- `product/godot_t004_prototype/data/sarah_j6_complete.json`
- `product/godot_t004_prototype/data/camille_j6_complete.json`
- `product/godot_t004_prototype/data/nico_j6_complete.json`
- `product/godot_t004_prototype/data/maya_j6_complete.json`
- `product/godot_t004_prototype/data/ines_j6_complete.json`
- `product/godot_t004_prototype/data/finales_mvp_complete.json`

## Résultat Roadmap

J6 + fins MVP sont **cohérents pour intégration T124**.

Aucun patch JSON n’est nécessaire dans T123.

La séquence J6 fonctionne comme clôture MVP :

```txt
S6A → C6A → N6A → M6A → S6B → C6B → I6A → FIN
```

Les personnages ne deviennent pas des fonctions abstraites :

- Sarah reste dans l’intime/domestique ;
- Camille reste lucide et oblique, sans ultimatum caricatural ;
- Nico pose une limite d’ami sans devenir tutoriel ;
- Maya amène une pression sociale concrète sans omniscience ;
- Inès ouvre une fuite possible sans devenir romance bonus ;
- la conversation finale clôt les routes sans expliquer un score au joueur.

## Relecture par contact

### Sarah J6

Fichier : `narrative/t120_sarah_j6_complete.json`  
Blocs : `s6_block_a`, `s6_block_b`  
Volume : 50 nodes, 6 choix, 3 ends.

Validation narrative : OK.

Sarah porte bien :

- le quotidien qui ne tient plus ;
- le mug / l’assiette / le téléphone ;
- la fatigue de devoir croire ;
- la question intime : être là ou juste faire tenir.

Elle ne bascule pas en détective. Elle ne mène pas d’enquête. Elle ne prononce pas la thèse du jeu.

End seeds cohérents pour fins :

- `s6_end_repair` ;
- `s6_end_uncertain` ;
- `s6_end_distance`.

### Camille J6

Fichier : `narrative/t120_camille_j6_complete.json`  
Blocs : `c6_block_a`, `c6_block_b`  
Volume : 50 nodes, 6 choix, 3 ends.

Validation narrative : OK.

Camille porte bien :

- le morceau de musique ;
- le café banal / porte de secours ;
- le téléphone encore allumé ;
- la demande de ne plus être une parenthèse ou un refuge.

Elle demande une position sans devenir ultimatum brutal. Elle reste attirante par sa lucidité, pas par une récompense mécanique.

Note audit : un scan lexical a signalé deux faux positifs `cout` dans `écoute` / `l’écoute`. Ce n’est pas le mot conceptuel `coût` et ce n’est pas bloquant.

End seeds cohérents :

- `c6_end_chosen_seed` ;
- `c6_end_respect_distance` ;
- `c6_end_cuts_short`.

### Nico J6

Fichier : `narrative/t121_nico_j6_complete.json`  
Bloc : `n6_block_a`  
Volume : 32 nodes, 4 choix, 3 ends.

Validation narrative : OK.

Nico porte bien :

- l’humour ;
- les frites / la ponctuation de guerre ;
- la limite amicale ;
- le refus d’être alibi permanent.

Il ne sauve pas tout. Il ne devient pas un moraliste ni un système d’aide.

End seeds cohérents :

- `n6_end_loyal_limit` ;
- `n6_end_steps_back` ;
- `n6_end_friend_hurt`.

### Maya J6

Fichier : `narrative/t121_maya_j6_complete.json`  
Bloc : `m6_block_a`  
Volume : 32 nodes, 4 choix, 3 ends.

Validation narrative : OK.

Maya porte bien :

- le détail social concret ;
- la photo de groupe ;
- l’épaule reconnaissable ;
- la possibilité que le groupe écrive le résumé à la place du joueur.

Elle n’est pas omnisciente. Elle ne résout pas l’intrigue. Elle exerce une pression sociale légère mais réelle.

End seeds cohérents :

- `m6_end_warned` ;
- `m6_end_soft_cover` ;
- `m6_end_minimized`.

### Inès J6

Fichier : `narrative/t121_ines_j6_complete.json`  
Bloc : `i6_block_a`  
Volume : 25 nodes, 3 choix, 3 ends.

Validation narrative : OK.

Inès porte bien :

- le message à contretemps ;
- l’hésitation ;
- l’arrêt / ticket de trajet ;
- la porte latérale.

Elle ne devient pas une troisième romance complète. Elle fonctionne comme tentation de fuite ou révélateur, conformément à T119.

End seeds cohérents :

- `i6_end_boundary` ;
- `i6_end_ambiguous` ;
- `i6_end_flight`.

## Relecture des fins MVP

Fichier : `narrative/t122_finales_mvp_complete.json`  
Conversation : `finales_mvp_complete`  
Volume : 50 nodes, 1 choix final principal, 5 ends.

Validation narrative : OK.

Fins présentes :

1. `final_end_reparation_fragile` — réparation fragile avec Sarah, sans pardon magique.
2. `final_end_camille_assumee` — Camille assumée, relation réelle et coûteuse humainement, sans récompense automatique.
3. `final_end_double_vie_maintenue` — équilibre maintenu pour la nuit, inconfortable.
4. `final_end_tout_se_fissure` — liens qui se retirent un par un, sans scène publique obligatoire.
5. `final_end_fuite_en_avant` — fuite / solitude via porte latérale Inès, pas romance bonus.

La forme conversation finale dédiée est cohérente pour l’intégration T124 : elle permet de brancher un bloc final unique après les conversations J6 sans multiplier les routes techniques.

## Garde-fous vérifiés

### Pas de révélation totale obligatoire

OK. Les fins peuvent exposer ou fissurer, mais aucune route n’impose une grande révélation commune à tout le monde.

### Pas de procès final unique

OK. J6 distribue la pression : Sarah intime, Camille affective, Nico amicale, Maya sociale, Inès fuite.

### Pas de personnages omniscients

OK. Maya voit un détail. Sarah ressent un écart. Nico connaît ses limites. Camille demande une place. Inès ouvre une porte.

### Pas de victoire parfaite

OK. Même les fins positives restent fragiles ou coûteuses.

### Messages avant images

OK. Toute la résolution reste dans la messagerie ; pas d’image, appel, média ou nouveau système.

## Validation statique T123

Validation locale effectuée sur les 6 JSON J6/fins :

| Fichier | Nodes | Choix | Ends | Duplicate IDs | Missing next | Source/copie |
|---|---:|---:|---:|---:|---:|---|
| `t120_sarah_j6_complete.json` | 50 | 6 | 3 | 0 | 0 | OK |
| `t120_camille_j6_complete.json` | 50 | 6 | 3 | 0 | 0 | OK |
| `t121_nico_j6_complete.json` | 32 | 4 | 3 | 0 | 0 | OK |
| `t121_maya_j6_complete.json` | 32 | 4 | 3 | 0 | 0 | OK |
| `t121_ines_j6_complete.json` | 25 | 3 | 3 | 0 | 0 | OK |
| `t122_finales_mvp_complete.json` | 50 | 1 | 5 | 0 | 0 | OK |

Autres vérifications :

- JSON parsés ;
- `schema_version = 0.1` ;
- `day = 6` ;
- senders / identités cohérents ;
- markers J6 présents ;
- tous les nodes sont atteignables ;
- effets valides ;
- SHA source/copie Godot identiques ;
- pas de hit visible bloquant sur le lexique conceptuel surveillé.

Le validateur global T090 reste OK sur J1→J5 actifs : 14 dialogues, 38 blocs, 0 erreur, 5 warnings placeholders historiques. J6 n’est pas encore actif/intégré, conformément à T124 à venir.

## Limites

T123 ne modifie pas :

- les JSON J6/fins ;
- les copies Godot data ;
- `conversation_blocks.json` ;
- les scripts Godot ;
- le schéma T003 ;
- la save/runtime/UX.

T123 ne teste pas le runtime Godot : intégration et playtest local relèvent de T124 puis validation Ludo.

## Décision Roadmap

J6 + fins MVP sont prêts pour intégration.

Prochaine étape recommandée :

**T124 — Intégrer J6 + fins MVP Godot**

Objectif T124 : ajouter les conversations J6/fins à l’état conversation, créer les blocs/unlocks day 6, brancher la conversation finale, étendre validateur/tests J1→J6, puis demander playtest runtime local à Ludo.
