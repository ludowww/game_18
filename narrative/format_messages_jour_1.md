# Double Vie — Formats message/choix + JSON narratif + Jour 1 jouable

## Format d’écriture des messages

Objectif : écrire comme une vraie messagerie, pas comme une scène dialoguée.

### Règles d’écriture

- Messages courts, naturels, avec sous-texte.
- Une bulle = une intention claire.
- Pas d’exposition lourde : les infos sortent par friction, retard, mensonge, relance.
- Les choix doivent créer soit : désir, confiance, risque, culpabilité, ou trace.
- Les images restent rares : le moteur principal est l’attente du prochain message.

### Types de nodes

- `text` : bulle envoyée par un contact ou le joueur.
- `choice` : choix joueur avec effets.
- `notification` : interruption entre conversations.
- `system` : retour discret d’état, debug narratif ou fin de segment.

### Champs recommandés

```json
{
  "id": "c1_002",
  "time": "08:43",
  "thread": "camille_day1",
  "sender": "system",
  "type": "choice",
  "prompt": "Répondre à Camille",
  "options": [
    {
      "id": "c1_002_a",
      "label": "Seulement quand on me surveille.",
      "next": "c1_003_flirt",
      "effects": { "camille_interest": 1, "risk": 1 },
      "set_flags": { "answered_camille_fast": true }
    }
  ]
}
```

## Jauges MVP

- `camille_interest` : attraction / curiosité de Camille.
- `sarah_trust` : confiance de Sarah.
- `nico_alert` : degré auquel Nico comprend ce qui se passe.
- `risk` : exposition aux conséquences.
- `guilt` : poids moral, utile pour variations de réponses.

## Flags MVP

- `answered_camille_fast`
- `lied_to_sarah`
- `told_nico_about_camille`
- `left_camille_on_read`

## Conversation Jour 1

Fichier jouable créé :

`/opt/data/profiles/game_18/narrative/jour_1_mvp.json`

Contenu :

1. Camille ouvre avec flirt léger et test de limites.
2. Sarah interrompt avec une question domestique qui peut forcer le mensonge.
3. Nico sert de confident / miroir moral.
4. Fin de segment : le joueur choisit quoi faire de la conversation Camille.

Note : correction appliquée — Sarah est maintenant la partenaire officielle dans contacts, threads, jauges et flags.
