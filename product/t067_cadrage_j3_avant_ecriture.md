# T067 — Cadrer J3 avant écriture

Thread d’exécution : Dialogues / Roadmap

Statut : DONE

## Objectif J3

J3 doit tester le passage de la double vie “gérable par messages” à une double vie qui commence à demander des arbitrages visibles.

Après J1/J2 :

- Camille a déplacé la tentation vers un risque concret.
- Sarah a formulé un besoin de présence et un doute doux.
- Le joueur ne peut plus simplement répondre au fil de l’eau : il doit choisir où il met son attention.

Intention J3 : **mettre le joueur face à des micro-choix de disponibilité incompatibles**, sans encore déclencher crise ouverte.

## Intention J3 globale

J3 doit créer la sensation suivante :

> Les deux conversations peuvent continuer, mais pas gratuitement.

Objectifs narratifs :

- Faire sentir que les messages commencent à envahir la journée.
- Transformer les délais de réponse en matière dramatique.
- Faire exister les conséquences J2 sans explosion de branches.
- Préparer J4 comme premier vrai risque de découverte / incohérence.

## Évolution Camille J3

### Rôle

Camille reste : tentation / risque / trouble.

Mais J3 doit éviter de la rendre trop directe ou trop disponible. Elle ne doit pas devenir “viens me voir” en boucle.

### Direction

Camille teste moins le désir et plus la capacité du joueur à créer une place pour elle.

Elle peut :

- rappeler subtilement la fin J2 ;
- faire sentir qu’elle n’est pas seulement un jeu ;
- demander une preuve légère d’attention ;
- créer une contrainte de timing courte ;
- pousser le joueur à choisir entre répondre maintenant ou perdre le moment.

### À éviter

- Répéter le café.
- Répéter “je suis près de chez toi”.
- Aller trop vite vers rendez-vous explicite.
- Trop sexualiser / trop frontaliser.
- La faire paraître disponible à l’infini.

### Proposition émotionnelle

Camille J3 = **“tu dis que tu veux garder le fil, mais est-ce que tu fais vraiment de la place ?”**

## Évolution Sarah J3

### Rôle

Sarah reste : intimité / confiance / soupçon doux / culpabilité.

Elle ne doit pas devenir enquêtrice. Elle ne cherche pas une preuve ; elle cherche une présence cohérente.

### Direction

Sarah teste la fiabilité quotidienne du joueur, pas sa culpabilité.

Elle peut :

- proposer un petit rituel simple ;
- remarquer les délais sans accuser ;
- demander une présence concrète mais douce ;
- exprimer une fatigue émotionnelle légère ;
- laisser une porte ouverte à la sincérité.

### À éviter

- Interrogatoire.
- “Tu me caches quelque chose ?” trop direct.
- Répéter dîner / téléphone sur la table.
- La transformer en obstacle moral permanent.
- Lui faire savoir trop tôt qu’il y a Camille.

### Proposition émotionnelle

Sarah J3 = **“je ne veux pas te surveiller, je veux sentir que je compte encore.”**

## Risques à éviter

### 1. Répétition café

Le café a servi J1/J2 pour Camille. J3 doit changer de motif.

Alternatives possibles :

- message depuis un lieu de passage non exploité : librairie, station, rue, hall, parking ;
- objet banal : chanson, photo non envoyée, ticket, parapluie, veste ;
- contrainte temporelle : “je coupe dans 10 minutes”, “je pars bientôt”, “je ne pourrai plus écrire après”.

Recommandation : **utiliser la contrainte de fenêtre courte plutôt qu’un nouveau lieu fixe**.

### 2. Répétition présence / dîner

Sarah J2 a déjà demandé présence + dîner sans téléphone. J3 doit déplacer le quotidien.

Alternatives possibles :

- une course à faire ensemble ;
- un message vocal non utilisé — mais appels/voix hors scope, donc rester texte ;
- un petit service : “tu peux récupérer ça ?” ;
- un souvenir commun ;
- un moment prévu plus tard, mais pas dîner.

Recommandation : **rituel domestique court + souvenir commun**, pas nouveau dîner.

### 3. Sarah trop accusatrice

Sarah doit exprimer : “je sens un écart”, pas “je sais que tu mens”.

Formulations à privilégier :

- “J’ai l’impression de devoir deviner.”
- “Je ne sais pas si je lis trop entre les lignes.”
- “Je préférerais que tu me dises quand tu n’es pas disponible.”
- “J’ai besoin d’un vrai moment, même court.”

Formulations à éviter :

- “Tu me mens.”
- “C’est qui ?”
- “Je sais qu’il y a quelqu’un.”
- “Montre-moi ton téléphone.”

### 4. Camille trop directe

Camille doit rester dangereuse par sous-texte, pas par demande explicite.

Formulations à privilégier :

- “Je voulais voir si tu répondrais vite.”
- “Je n’ai pas beaucoup de temps.”
- “Tu peux ignorer, mais tu vas le lire.”
- “Je ne sais pas pourquoi je t’écris ça maintenant.”

Formulations à éviter :

- “Viens me voir maintenant.” répété.
- “On se cache où ?”
- “Je veux que tu choisisses moi.” trop tôt.

## Rôle des conséquences J2

Les conséquences J2 doivent modifier le ton, pas créer des routes lourdes.

### Flags Camille J2 utiles

- `camille_j2_ending_boundary` : Camille plus distante / ironique, teste si le joueur revient.
- `camille_j2_ending_stay` : Camille plus complice, mais fait sentir que le joueur a franchi une ligne.
- `camille_j2_ending_thread` : Camille insiste sur le fil ouvert et la dépendance aux messages.

Usage J3 : variations de 1–2 lignes en ouverture ou dans les réponses, pas embranchements massifs.

### Flags Sarah J2 utiles

- `sarah_j2_presence_promised` : Sarah attend une preuve de présence.
- `sarah_j2_fragile_opening` : Sarah est plus douce, mais fragile.
- `sarah_j2_distance_widens` : Sarah se protège, messages plus courts.

Usage J3 : ton d’ouverture Sarah + intensité de `sarah_trust`, pas enquête.

## Structure blocs J3 recommandée

### Camille J3

#### C3A — Reprise selon fin J2

Objectif : montrer que Camille a retenu la posture du joueur.

Contenu :

- 1 ouverture liée à J2 ;
- 1 choix joueur sur assumer / minimiser / recadrer ;
- fin de bloc avec attente ou fenêtre courte.

#### C3B — Fenêtre courte

Objectif : créer urgence sans rendez-vous lourd.

Contenu :

- Camille n’a “pas beaucoup de temps” ;
- elle envoie un message qui demande réponse maintenant ;
- choix joueur : répondre vite / temporiser / refuser.

#### C3C — Trace émotionnelle

Objectif : faire sentir que ce n’est plus juste flirt.

Contenu :

- Camille dit une phrase plus sincère mais ambiguë ;
- le joueur peut nourrir, limiter ou laisser en vu ;
- fin J3 ouvre vers J4 : risque d’incohérence ou attente plus lourde.

### Sarah J3

#### S3A — Matin prudent

Objectif : Sarah ne relance pas l’accusation, elle observe le niveau de présence.

Contenu :

- message simple du quotidien ;
- sous-texte : “est-ce que tu es vraiment là ?” ;
- choix joueur : présence / réponse neutre / esquive.

#### S3B — Petit rituel

Objectif : remplacer dîner/téléphone par un geste concret.

Contenu :

- souvenir commun ou petite course ;
- Sarah demande une action simple ;
- choix joueur : accepter / repousser / faire à moitié.

#### S3C — Doute doux mais plus net

Objectif : Sarah formule une limite émotionnelle sans accusation.

Contenu :

- “je ne veux pas deviner” ;
- choix joueur : rassurer / promettre / éviter ;
- fin J3 ouvre vers J4 : confiance tenue, fragilisée, ou distance.

## Rythme d’unlocks J3 recommandé

Rythme conseillé pour conserver l’addiction aux messages :

1. `C3A` Camille relance selon J2.
2. Attente.
3. `S3A` Sarah demande présence simple.
4. Notification / unlock `C3B` : fenêtre courte Camille.
5. `S3B` : petit rituel Sarah.
6. `C3C` : trace émotionnelle Camille.
7. `S3C` : doute doux Sarah.
8. J3 terminé.

Objectif : le joueur alterne entre désir de répondre à Camille et besoin de préserver Sarah.

## Recommandation de production

### T068 — Écrire Camille J3 complet

Thread : Dialogues

Objectif : produire Camille J3 au format JSON T003.

Contraintes :

- `conversation_id = camille_j3_complete`
- `contact_id = camille`
- `day = 3`
- 3 blocs : C3A / C3B / C3C
- 35–50 nodes environ
- 4–6 choix joueur
- 2–3 fins
- utiliser flags J2 en tonalité légère si possible
- éviter café / rendez-vous trop direct

### T069 — Écrire Sarah J3 complet

Thread : Dialogues

Objectif : produire Sarah J3 au format JSON T003.

Contraintes :

- `conversation_id = sarah_j3_complete`
- `contact_id = sarah`
- `day = 3`
- 3 blocs : S3A / S3B / S3C
- 35–50 nodes environ
- 4–6 choix joueur
- 2–3 fins
- utiliser flags J2 en tonalité légère si possible
- éviter dîner / téléphone sur table / accusation directe

### T070 — Intégrer J3 prototype

Thread : Scope MVP / technique

Objectif : intégrer Camille J3 + Sarah J3 au prototype après validation contenu.

Contraintes :

- pas de modification schéma T003 ;
- ajouter les conversations J3 dans le système jours ;
- blocs J3 dans le système de verrous ;
- J1/J2 restent visibles en historique ;
- pas de J4 tant que J3 non testé.

## Décision

J3 doit tester **l’arbitrage d’attention**, pas encore la crise.

Camille tire vers la disponibilité risquée.
Sarah tire vers la présence fiable.

Le joueur doit sentir que répondre à l’une commence à coûter à l’autre, même si aucune découverte frontale n’a encore lieu.
