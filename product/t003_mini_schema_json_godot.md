# T003 — Mini-schéma JSON stable Godot

Source Roadmap : T003 = définir le format JSON minimal que Godot lira pour afficher une conversation.

Statut : DONE

## 1. Structure JSON proposée

Principe : un fichier = une conversation jouable courte.

```json
{
  "schema_version": "0.1",
  "conversation_id": "camille_j1_intro",
  "day": 1,
  "contact_id": "camille",
  "start_node": "c1_001",
  "nodes": [
    {
      "id": "c1_001",
      "type": "message",
      "sender": "camille",
      "text": "...",
      "delay": 0,
      "next": "c1_002"
    },
    {
      "id": "c1_002",
      "type": "choice",
      "sender": "player",
      "text": "Répondre à Camille",
      "choices": [
        {
          "id": "c1_002_a",
          "text": "...",
          "next": "c1_003_a",
          "effects": {
            "camille_interest": 1,
            "risk": 1,
            "flags": ["answered_camille_fast"]
          }
        }
      ]
    }
  ]
}
```

### Champs racine

- `schema_version` : version du format, string simple.
- `conversation_id` : ID unique de la conversation.
- `day` : jour de jeu.
- `contact_id` : contact principal affiché dans l’écran messages.
- `start_node` : premier node à lire.
- `nodes` : liste ordonnée des messages / choix.

### Champs d’un node

- `id` : ID unique du node.
- `type` : `message`, `choice` ou `end`.
- `sender` : `player`, `system`, ou ID contact (`camille`, `sarah`, etc.).
- `text` : texte affiché.
- `delay` : délai avant affichage, en secondes. Optionnel, défaut `0`.
- `next` : ID du node suivant. Absent si `type: "end"`.
- `choices` : seulement pour `type: "choice"`.
- `effects` : conséquences simples appliquées quand un choix est pris ou quand un node est lu.

### Champs d’un choix

- `id` : ID unique du choix.
- `text` : réponse affichée au joueur.
- `next` : node cible après sélection.
- `effects` : changements simples d’état.

### Format des effets MVP

```json
"effects": {
  "camille_interest": 1,
  "risk": 1,
  "sarah_trust": -1,
  "flags": ["answered_camille_fast"]
}
```

Règle : uniquement des entiers simples pour les jauges, et une liste de flags à ajouter.

## 2. Exemple court — J1 Camille

```json
{
  "schema_version": "0.1",
  "conversation_id": "camille_j1_intro",
  "day": 1,
  "contact_id": "camille",
  "start_node": "c1_001",
  "nodes": [
    {
      "id": "c1_001",
      "type": "message",
      "sender": "camille",
      "text": "Alors… tu fais toujours semblant d’être sérieux le matin ?",
      "delay": 0,
      "next": "c1_002"
    },
    {
      "id": "c1_002",
      "type": "choice",
      "sender": "player",
      "text": "Répondre à Camille",
      "choices": [
        {
          "id": "c1_002_a",
          "text": "Seulement quand on me surveille.",
          "next": "c1_003_a",
          "effects": {
            "camille_interest": 1,
            "risk": 1,
            "flags": ["answered_camille_fast"]
          }
        },
        {
          "id": "c1_002_b",
          "text": "Je suis très sérieux. Trop, même.",
          "next": "c1_end",
          "effects": {
            "camille_interest": 0,
            "flags": ["answered_camille_fast"]
          }
        },
        {
          "id": "c1_002_c",
          "text": "Ignorer pour l’instant",
          "next": "c1_end",
          "effects": {
            "camille_interest": -1,
            "sarah_trust": 1,
            "flags": ["left_camille_on_read"]
          }
        }
      ]
    },
    {
      "id": "c1_003_a",
      "type": "message",
      "sender": "player",
      "text": "Seulement quand on me surveille.",
      "delay": 0,
      "next": "c1_004_a"
    },
    {
      "id": "c1_004_a",
      "type": "message",
      "sender": "camille",
      "text": "Donc si je te surveille, tu redeviens sage ? Intéressant.",
      "delay": 60,
      "next": "c1_end"
    },
    {
      "id": "c1_end",
      "type": "end",
      "sender": "system",
      "text": "Fin temporaire du bloc Camille J1. La conversation reste ouverte.",
      "effects": {
        "flags": ["camille_j1_intro_done"]
      }
    }
  ]
}
```

## 3. Règles minimales de nommage des champs

- Champs en `snake_case` uniquement.
- IDs en minuscules, sans accents, sans espaces.
- Préfixe conseillé : initiale contact + jour + numéro. Exemple : `c1_001`, `c1_002_a`.
- `sender` doit rester stable : `player`, `system`, ou `contact_id`.
- `delay` toujours en secondes, nombre entier.
- `next` pointe toujours vers un `node.id` existant.
- Les flags sont des strings en snake_case : `left_camille_on_read`.
- Les jauges dans `effects` sont des entiers relatifs : `-1`, `0`, `1`, `2`.

## 4. Hors-scope MVP explicite

- Pas de conditions complexes imbriquées.
- Pas de langage de script dans le JSON.
- Pas de calculs dynamiques dans les textes.
- Pas de localisation multi-langue.
- Pas de médias/images dans ce schéma T003.
- Pas de gestion complète des sauvegardes.
- Pas d’éditeur de dialogues.
- Pas de routes profondes multi-jours dans un seul fichier.
- Pas de système de priorité d’événements.
- Pas de randomisation.

Décision : garder un format volontairement plat, lisible, et suffisant pour T004 — Prototype conversation Godot.
