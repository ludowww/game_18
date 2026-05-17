# T130 — Validation cohérence finale voix/personnages + copies Godot

Statut : DONE  
Thread : Roadmap / Dialogues  
Portée : validation finale après T126A/T126B/T127/T128/T129, sans patch JSON

## Objectif

Valider que la passe “refonte ressentie des personnages” a bien été menée après le retour Ludo :

> je n'ai pas vu de refonte des dialogues des personnages, c'est normal ?

La réponse produit était : T118 était seulement un polish ciblé. La vraie passe a donc été distribuée puis exécutée :

- T126A — bible jouable forte Personnages ;
- T126B — plan de patch voix Dialogues ;
- T127 — patch voix Sarah/Camille J1→J6 ;
- T128 — patch voix Maya/Nico/Inès J4→J6 ;
- T129 — respirations sans pression transversales J1→J6.

T130 vérifie la cohérence finale, les copies Godot et la stabilité technique.

## Résultat Roadmap

Validation finale OK.

Les dialogues J1→J6/finale ont maintenant une couche de voix/personnage beaucoup plus visible :

- **Sarah** : domestique, intime, confiance abîmée, motifs maison.
- **Camille** : trouble, lucidité, musique, lieux, silences.
- **Maya** : social, piquant, détails publics, groupe/photo/story.
- **Nico** : oralité de pote, humour, bouffe, limite amicale.
- **Inès** : rareté, hésitation, trajet/nuit/ticket, porte latérale.

La structure narrative/technique reste stable : aucun changement d’IDs, branches, choices, effects, flags ou schéma T003 dans T127/T128/T129.

## Corpus validé

20 dialogues actifs J1→J6/finale :

- Camille J1/J2/J3/J4/J5/J6 ;
- Sarah J1/J2/J3/J5/J6 ;
- Maya J4/J5/J6 ;
- Nico J4/J5/J6 ;
- Inès J4/J6 ;
- finale MVP.

Toutes les copies Godot data correspondantes sont synchronisées avec les sources narratives.

## Validation voix par contact

### Sarah

Motifs repérés après patches :

- café ;
- assiette ;
- mug ;
- cuisine ;
- canapé ;
- chargeur ;
- chaussures ;
- épisode ;
- clé ;
- frigo.

Validation : OK.

Sarah ne fonctionne plus seulement comme “partenaire officiel / suspicion”. Elle a davantage de texture domestique et d’intimité pratique. Les choix donnent plus souvent la possibilité de répondre avec maladresse douce ou attention concrète.

Limite : Sarah J3 reste moins marquée que J1/J2/J5/J6. Ce n’est pas bloquant, car J3 est moins prioritaire dans la passe demandée, mais pourra être renforcé si Ludo ressent encore une faiblesse.

### Camille

Motifs repérés après patches :

- café ;
- morceau / musique ;
- téléphone ;
- silence ;
- porte ;
- serviette ;
- table ;
- pluie ;
- vitrines.

Validation : OK.

Camille est plus reconnaissable par les lieux, les silences et les sous-entendus. Elle garde sa lucidité sans redevenir pure phrase-thème.

### Maya

Motifs repérés après patches :

- photo ;
- story ;
- groupe ;
- épaule ;
- porte ;
- vanne ;
- tribunal ;
- détail vu / regard.

Validation : OK.

Maya est davantage sociale et piquante. Elle observe des détails publics sans devenir omnisciente ni policière.

### Nico

Motifs repérés après patches :

- sandwich ;
- frites ;
- sauce ;
- match ;
- standard de crise ;
- pote ;
- chaos.

Validation : OK.

Nico a plus d’oralité et de sas comique. Il reste utile comme respiration mais conserve sa limite amicale.

### Inès

Motifs repérés après patches :

- trajet ;
- ticket ;
- arrêt ;
- bus ;
- nuit ;
- vitrine ;
- hésité / effacé ;
- seuil ;
- doucement.

Validation : OK.

Inès reste rare, flottante, à contretemps. Elle ne devient pas une romance bonus, mais sa présence est plus identifiable.

## Validation technique

Vérifications effectuées sur les 20 dialogues actifs :

- JSON parsés ;
- aucun duplicate ID ;
- aucun `next` manquant ;
- tous les nodes atteignables ;
- effects valides ;
- SHA source/copie Godot identiques ;
- schéma T003 inchangé ;
- `conversation_blocks.json` inchangé par T130 ;
- scripts Godot inchangés par T130.

## Tests exécutés

Régressions directes attendues :

```txt
python3 tests/test_t124_j6_fins_integration.py
python3 tests/test_t125_j6_second_block_quick_switch.py
python3 tests/test_t112_j5_integration.py
python3 tests/test_t097_j4_integration.py
python3 tests/test_t090_dialogue_block_validator.py
python3 tests/test_t078_j3_integration.py
python3 tests/test_t063_j2_integration.py
```

Validateur global attendu :

```txt
T090 dialogue/block validation: OK
Active dialogues: 20
Blocks: 46
Errors: 0
Warnings: 5
```

## Limites

- T130 ne modifie aucun contenu ; il valide.
- Runtime Godot non testé côté VPS : Godot CLI absent.
- La perception finale de la refonte reste à valider en lecture/playtest Ludo.
- Si Ludo trouve encore un personnage faible, prochaine action recommandée : patch ciblé par contact, pas nouvelle refonte globale.

## Décision Roadmap

La séquence refonte voix/personnages est prête pour playtest de perception.

Prochaine étape recommandée :

**T131 — Playtest perception personnages J1→J6 côté Ludo**

Checklist :

1. Sarah est-elle identifiable dès ses premiers messages ?
2. Camille a-t-elle une couleur distincte de Sarah ?
3. Maya/Nico/Inès sont-ils reconnaissables sans regarder le nom ?
4. Y a-t-il assez de moments sans pression ?
5. Les choix semblent-ils moins “questionnaire dramatique” ?
6. Un personnage reste-t-il plat ou forcé ?
