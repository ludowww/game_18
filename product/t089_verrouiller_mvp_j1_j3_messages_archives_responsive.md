# T089 — Verrouiller MVP J1→J3 Messages + Archives + Responsive

Statut : DONE
Thread : Roadmap / Scope MVP / technique

## Décision

Le socle **Messages J1→J3** est verrouillé comme tranche MVP validée côté runtime Ludo :

- écran Messages centré sur le jour courant ;
- J1/J2 déplacés dans `Archives / Jours précédents`, repliées par défaut ;
- archives ouvrables et relisibles ;
- badges/previews actifs limités au jour courant ;
- cartes Messages contraintes à la largeur disponible ;
- previews lisibles en wrap + ellipsis de sécurité ;
- header debug `Reset` / `Mode test rapide` propre sur une deuxième ligne compacte ;
- mode test rapide disponible sans changer le rythme normal par défaut.

## Chaîne de validation verrouillée

- **T082** — MVP J3 intégré verrouillé : Camille/Sarah J3, six blocs J3, rythme `C3A → S3A → C3B → S3B → C3C → S3C`, J1/J2 historiques, save/reload.
- **T083** — Mode test accéléré : toggle debug discret, OFF par défaut, rythme normal inchangé.
- **T085** — Archives jours passés : Messages = jour courant, archives J1/J2 repliées et relisibles.
- **T086** — Playtest runtime archives : validé côté Ludo ; J1/J2 relisibles depuis archives, pas de pollution de la boîte active.
- **T087** — Correction overflow horizontal Messages : cartes/header/previews rendus responsive côté Godot UI.
- **T088** — Playtest runtime Messages responsive + archives : validé côté Ludo ; cartes sans débordement, previews lisibles, header propre, archives OK.

## Ce qui est verrouillé

### Messages / inbox active

- La liste active affiche seulement les conversations du `current_day`.
- En Jour 3, Camille J3 et Sarah J3 sont les conversations actives visibles par défaut.
- Les anciens jours ne donnent plus l’impression d’être des messages frais à traiter.

### Archives

- `Archives / Jours précédents` reste secondaire et repliée par défaut.
- Les conversations J1/J2 restent ouvrables via le même chemin de navigation que les conversations actives.
- Les anciens états restent relisibles sans dupliquer la logique d’ouverture.

### Responsive Messages

- Les cartes sont contraintes à la largeur disponible.
- Les previews sont en wrap intelligent, avec ellipsis de sécurité plutôt qu’un clipping brutal hors écran.
- Le header debug est séparé du sous-titre pour éviter le débordement horizontal.

### Non-régression systèmes

- JSON dialogues inchangés.
- Schéma T003 inchangé.
- `data/conversation_blocks.json` inchangé.
- Sauvegarde / payload inchangé.
- Pas de nouveau calendrier, recherche, corbeille, filtres avancés, notification OS, scheduler ou temps réel.

## Validation statique

Régressions à conserver comme garde-fous :

```bash
python3 tests/test_t087_messages_horizontal_overflow.py
python3 tests/test_t085_archives_jours_passes.py
python3 tests/test_t083_mode_test_accelere.py
python3 tests/test_t080_day_transition_button_label.py
python3 tests/test_t078_j3_integration.py
python3 tests/test_t072_repair_existing_save_badges.py
python3 tests/test_t068_externalized_blocks.py
python3 tests/test_t063_j2_integration.py
python3 tests/test_t057_narrative_blocks.py
python3 tests/test_t053_notification_guards.py
```

Les 9 fichiers JSON data du prototype doivent rester parseables.

## Validation runtime

Validation runtime déclarée côté Ludo dans Godot 4.6 :

- Archives validées.
- Correctif Messages responsive validé.
- Aucun nouveau bug runtime signalé après T087/T088.

Le VPS n’a pas de Godot CLI (`godot_cli_absent`) : la validation runtime locale reste côté Ludo.

## Limites MVP assumées

- J4 non cadré / non écrit.
- Pas d’images, appels, galerie ou médias.
- Pas de contacts système complets.
- Pas de recherche ou corbeille d’archives.
- Pas de notifications OS / temps réel / scheduler.
- Blocs narratifs encore prototype-side/config JSON dédiée, pas un outil auteur complet.
- Mode test rapide debug uniquement, OFF par défaut.

## Prochaine étape recommandée

Avant d’ajouter du contenu, décision Roadmap à prendre :

1. **T090 — Cadrer J4** : continuer l’expansion narrative.
2. **T090 — Polish rythme/UX J1→J3** : stabiliser confort de lecture et tempo avant plus de contenu.
3. **T090 — Outillage blocs/dialogues** : réduire le coût de production/validation avant J4+.

Recommandation produit : **cadrer J4 seulement si le confort Messages/archives reste stable après quelques manipulations de reset/save ; sinon polish UX/rythme court avant expansion.**
