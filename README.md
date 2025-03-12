# Blockchain & Cryptography

Hands-on Python exercises for practical learning.  
Clear explanations of core blockchain principles.

## Topics Covered

1. **Introduction to Blockchain** – Understanding the origins, principles, and impact of blockchain technology.
2. **Blockchain as a Data Structure** – Exploring how transactions are stored, linked, and verified through cryptographic hashing.
3. **Consensus Algorithms** – Studying how networks achieve agreement using Proof-of-Work (PoW), Proof-of-Stake (PoS), and other mechanisms.
4. **Nodes & Network Architecture** – Learning how blockchain networks are structured and how nodes maintain the distributed ledger.
5. **Smart Contracts** – Implementing self-executing contracts that automate trustless agreements.

---

# Blockchain & Cryptography Quizzes : 

## Quand a été inventée la première blockchain ?
1. 1982
2. 1995
3. 2008
4. 2015

**Réponse:** 1

**Pourquoi ?**  
La première mention d'un concept de blockchain remonte à 1982, dans une thèse de David Chaum sur les bases de données sécurisées. Ce n’est qu’en 2008 que Satoshi Nakamoto a proposé le Bitcoin, qui a utilisé la première implémentation réelle d’une blockchain. Les autres dates ne correspondent pas à l'invention du concept.

## À votre avis, les transactions de Bitcoin sont-elles anonymes ?
1. Oui
2. Non

**Réponse:** 2

**Pourquoi ?**  
Les transactions Bitcoin ne sont pas anonymes mais pseudonymes. Elles sont publiquement visibles sur la blockchain et associées à des adresses, ce qui permet de retracer l’historique des transactions. Avec des analyses avancées, il est possible d’identifier les utilisateurs.

## Combien de traîtres/défectueux doit-il y avoir au maximum pour se mettre d'accord ?
1. 1
2. 24%
3. 33%
4. 49%
5. 66%
6. 74%

**Réponse:** 3 et 4

**Pourquoi ?**  
Dans le problème des généraux byzantins, une blockchain tolère jusqu'à 1/3 (≈33%) de nœuds malveillants dans un consensus Byzantine Fault Tolerant (BFT). Pour les blockchains basées sur le Proof-of-Work (PoW), un attaquant doit contrôler plus de 50% (donc 49% est encore sûr) du réseau pour compromettre la sécurité.

## Parmi ces qualificatifs, lesquels, pensez-vous, décrivent la technologie blockchain ?
1. Immutabilité
2. Sécurité
3. Centralisation de l'autorité
4. Anonymat
5. Adaptabilité
6. Automatisation

**Réponse:** 1, 2, 5, 6

**Pourquoi ?**  
- **Immutabilité :** Une fois une transaction enregistrée, elle ne peut pas être modifiée.
- **Sécurité :** Grâce au chiffrement et aux mécanismes de consensus, la blockchain est sécurisée.
- **Adaptabilité :** Les blockchains évoluent et s’adaptent à différents cas d’usage.
- **Automatisation :** Les smart contracts permettent d’exécuter automatiquement des actions.

**Les mauvaises réponses :**  
- **Centralisation de l'autorité :** Faux, la blockchain est décentralisée.
- **Anonymat :** Faux, elle est pseudonyme (les transactions sont publiques).

## Si vous aviez 200 bitcoins en 2010, combien aviez-vous d'euros environ ?
1. 10 euros
2. 50 centimes
3. 7500 euros
4. Rien car c'est de la pure spéculation

**Réponse:** 2

**Pourquoi ?**  
En 2010, le Bitcoin valait moins d'un centime d'euro. 200 BTC avaient donc une valeur extrêmement faible, environ 50 centimes.

## Une résolution exacte du problème des généraux byzantins doit contenir :
1. Au maximum 1/2 patriotes
2. Au maximum 3/4 patriotes
3. Au maximum 1/3 traîtres
4. Au maximum 1/2 traîtres

**Réponse:** 3

**Pourquoi ?**  
Le problème des généraux byzantins établit qu’un système peut tolérer jusqu’à 1/3 de traîtres tout en garantissant un consensus correct. Si le nombre de traîtres dépasse 33%, il devient impossible d’assurer un consensus fiable.

## Si une blockchain tourne sur 100 machines dont 3 frauduleuses, combien de machines faut-il détruire au minimum pour altérer la blockchain ?
1. 95
2. 6
3. 51
4. 91

**Réponse:** 1

**Pourquoi ?**  
Pour prendre le contrôle du réseau, un attaquant doit posséder plus de 50% des machines. Ici, il faudrait donc détruire 95 machines, laissant ainsi 5 machines actives, dont 3 frauduleuses, ce qui donne une majorité malveillante.

## Que peut-on stocker dans une blockchain ?
1. Les restes de la veille
2. Des transactions
3. Des jeux vidéos
4. Les photos de la dernière soirée

**Réponse:** 2, 3, 4

**Pourquoi ?**  
Une blockchain peut stocker des transactions financières, des applications décentralisées (dont des jeux vidéo) et même des fichiers multimédias comme des images.

## Dans le système de signature aveugle, qui n'a pas accès à l'identité du client ?
1. Le client
2. L'autorité de signature
3. Le marchand
4. Un observateur de la transaction

**Réponse:** 3, 4

**Pourquoi ?**  
La signature aveugle permet d’authentifier une transaction sans révéler l’identité du client. Seuls l'autorité signataire et le client connaissent l’identité, mais le marchand et les observateurs ne la voient pas.



## What is a blockchain?
1. A microprocessor
2. A Data structure
3. A software
4. A cryptocurrency

**Réponse:** 2

**Pourquoi ?**  
Une blockchain est une structure de données qui enregistre des blocs de transactions liés cryptographiquement. Elle n'est ni un microprocesseur, ni un logiciel en soi, ni une cryptomonnaie (Bitcoin est une cryptomonnaie, mais pas la blockchain elle-même).

## Which of the following are legit ways to authenticate a document?
1. A barcode
2. A hand signature
3. A coffee stain
4. A bit of wax hit by your family's treasured ring

**Réponse:** 1, 2, 4

**Pourquoi ?**  
- Un code-barres peut être utilisé pour vérifier l'authenticité d’un document, car il contient des informations vérifiables.
- Une signature manuscrite est une méthode reconnue légalement pour valider des documents.
- Un sceau en cire était historiquement utilisé pour authentifier des documents officiels.

**Les fausses réponses :**  
- Une tache de café ne suit aucun protocole d’authentification et ne prouve rien.

## In this model, what do I absolutely need to create an authentic certificate for someone else?
1. His/her statement
2. His/her handwriting
3. His/her blood
4. His/her name

**Réponse:** 3, 4

**Pourquoi ?**  
- Le nom est essentiel pour qu'un certificat puisse être associé à une personne spécifique. Sans ce nom, le certificat ne peut pas être attribué à un individu précis.
- Le sang peut être utilisé dans des méthodes biométriques d'authentification ultra-sécurisées, car l'ADN contenu dans le sang est unique à chaque individu. Cela garantit une identification fiable.

**Pourquoi les autres réponses sont fausses ?**  
- La déclaration (statement) n’a aucune valeur d’authentification, car une simple déclaration verbale ou écrite ne prouve pas l’identité de quelqu'un de manière vérifiable.
- L'écriture manuscrite (handwriting) peut être imitée ou falsifiée, ce qui la rend insuffisante pour garantir l'authenticité d’un certificat. Contrairement au sang ou à une clé cryptographique, l’écriture ne fournit pas un identifiant unique et infalsifiable.

The representation of 47 in base 4 is:
1. 301
2. 233
3. 11
4. 434
5. 323

**Reponse:** 2  
**Pourquoi:** 233 = 2\*4^2 + 3\*4^1 + 3\*4^0 = 47

---

In the assignment 1 hashing, which line causes the one-way characteristic?
1. `output += ord(characters)`
2. `output ^= (output * 31)`
3. `output %= 2**32`
4. the integer limit

**Reponse:** 2

**Pourquoi avec un exemple concret:**

Prenons une valeur initiale :

```python
output = 10
character = 'A'  # 'A' a une valeur ASCII de 65
```

Regardons ce que chaque ligne ferait :

1. `output += ord(character)`
    - `output = 10 + 65 = 75`
    - ✅ Réversible : On peut simplement soustraire 65 pour retrouver l'entrée.

2. `output ^= (output * 31)` (Bonne réponse)
    - `output = 10 ^ (10 * 31) = 10 ^ 310`
    - Convertissons en binaire :
      - 10 = 00001010  
      - 310 = 100110110  
      - XOR = 100100100 (292 en décimal)
    - 🚫 Irréversible : Le XOR mélange les bits, rendant impossible de retrouver 10 juste avec 292. Chaque petit changement en entrée donne une sortie complètement différente (effet avalanche).

3. `output %= 2**32`
    - Si `output` dépasse 2^32, on prend le reste de la division.
    - ✅ Ce n'est pas un effet "one-way", juste une limitation de taille.

4. the integer limit
    - ✅ Ne change pas directement la propriété de hachage, c'est juste une contrainte mémoire.

---

Which way interests us most?
1. The private key encrypts, the public key decrypts
2. The public key encrypts, the private key decrypts

**Reponse:** 1  
**Pourquoi ?**  
Dans la signature numérique, la clé privée chiffre (signer) et la clé publique déchiffre (vérifier). Cela permet à tout le monde de vérifier qu’une signature vient bien du propriétaire de la clé privée.

**Pourquoi la réponse 2 est fausse ?**  
Si la clé publique chiffrait, tout le monde pourrait chiffrer un message et seul le propriétaire de la clé privée pourrait le lire. C’est le cas du chiffrement asymétrique utilisé pour sécuriser les messages, mais pas pour la signature numérique.

---

Among the following, which ones should better be added to the payload?
1. The recipient
2. The signature date
3. A link to another certificate
4. The length of a document stored inside the certificate

**Reponse:** 1, 3  
**Pourquoi ?**  
Le destinataire (recipient) est important car il indique à qui est destiné le certificat. Un lien vers un autre certificat permet d’assurer une continuité et de valider des références.

**Pourquoi les autres réponses sont fausses ?**  
La date de signature peut être importante, mais elle est souvent stockée ailleurs (métadonnées). La longueur du document est inutile car elle ne change pas la validité du certificat.

---

If Charlie wants the blockchain to be valid again, what can he do?
1. add useless data in the tampered block and get lucky
2. change the parent property of next block
3. change the parent property of all next blocks
4. Sign it

**Reponse:** 1, 3  
**Pourquoi ?**  
Ajouter des données et recalculer le hash peut, par chance, recréer une validité, mais c'est improbable. Changer tous les blocs suivants permet de reconstruire une chaîne valide en manipulant l’historique.

**Pourquoi les autres réponses sont fausses ?**  
Modifier uniquement le parent du bloc suivant ne suffit pas, car le hash du bloc actuel est basé sur les précédents. Signer ne rend pas le bloc valide si ses données sont déjà corrompues.

---

What means can store a wallet?
1. .py file
2. Exchange website (Binance, Coinbase,...)
3. A post-it
4. Your brain

**Reponse:** 1, 2, 3, 4  
**Pourquoi ?**  
Un fichier .py peut contenir une clé privée. Un exchange (Binance, etc.) stocke les wallets numériques. Un post-it peut contenir la phrase de récupération du wallet. Un cerveau peut mémoriser une phrase mnémonique pour restaurer un wallet.

---

If I get one of Alice's certificate, change its issuer to my public key and I sign it. Is it authentic?
1. Yes
2. No

**Reponse:** 1  
**Pourquoi ?**  
En remplaçant l'émetteur et en le signant avec une nouvelle clé privée, le certificat devient valide sous cette nouvelle identité. Ce n’est plus l’original, mais il est bien authentique pour la nouvelle signature.

---

I received the hash of a certificate. Using this hash I can get:
1. its issuer
2. its signature
3. its creation date
4. whether this certificate is identical to another one

**Reponse:** 4  
**Pourquoi ?**  
Un hash permet uniquement de vérifier si deux certificats sont identiques, car le hash est unique pour chaque document.

**Pourquoi les autres réponses sont fausses ?**  
L'émetteur, la signature et la date ne sont pas stockés dans le hash, seul un résumé du contenu est généré.

---

I share my RSA private keys with my parents. They can:
1. sign certificates as me
2. retrieve "p" and "q" that were used to generate it
3. Change a certificate I put yesterday in the blockchain
4. Verify that I signed some certificate

**Reponse:** 1, 4  
**Pourquoi ?**  
La clé privée permet de signer des documents : si vos parents la possèdent, ils peuvent se faire passer pour vous et signer en votre nom. Ils peuvent aussi vérifier vos signatures, car ils ont votre clé privée et peuvent recalculer les valeurs pour voir si elles correspondent.

**Pourquoi les autres réponses sont fausses ?**  
Ils ne peuvent pas retrouver "p" et "q" : ces valeurs ont été utilisées pour générer la clé, mais une fois la clé privée créée, elles ne sont plus accessibles. Ils ne peuvent pas modifier un certificat déjà sur la blockchain, car celle-ci est immuable.

---

The black hole...:
1. can sign certificates
2. can receive bitcoins
3. can check that a signature is authentic
4. owns a public key

**Reponse:** 2, 4  
**Pourquoi ?**  
Un "black hole" est une adresse où l'on peut envoyer des bitcoins, mais sans clé privée pour les récupérer, donc ils sont perdus à jamais. Toute adresse possède une clé publique associée, même si elle n’a pas de clé privée accessible.

**Pourquoi les autres réponses sont fausses ?**  
Le "black hole" ne peut pas signer de certificats, car il ne possède pas de clé privée associée. Il ne peut pas vérifier des signatures, car ce n’est qu’une adresse, pas un système de validation.

---

The blockchain police shows me a certificate with my name on it, my signature and some data, because they suspect a fraud. What information can I provide them to show that it is legit?
1. My private key
2. The signature date
3. Give them money to leave
4. Nothing

**Réponse:** 4  
**Pourquoi ?**  
Une signature numérique est vérifiable publiquement avec une clé publique. Vous n’avez rien à prouver : il suffit qu’ils vérifient la signature eux-mêmes.

**Pourquoi les autres réponses sont fausses ?**  
Donner votre clé privée est dangereux, car elle permettrait de voler votre identité numérique. La date de signature n’est pas suffisante pour prouver l’authenticité. Tenter de les corrompre est illégal (et ne garantit pas qu’ils arrêteront leur enquête).

---

If anyone can add blocks to the blockchain, which of these properties becomes invalid?
1. Immutability
2. Decentralization
3. Resilience
4. Anonymity

**Réponse:** 1, 3  
**Pourquoi ?**  
L’immuabilité est brisée, car si tout le monde peut ajouter des blocs sans restriction, un attaquant pourrait modifier la chaîne à sa guise. La résilience (capacité de résistance) est compromise, car sans contrôle, le réseau pourrait être facilement perturbé par des ajouts frauduleux.

**Pourquoi les autres réponses sont fausses ?**  
La décentralisation ne change pas, car cela dépend de la gouvernance du réseau, pas du fait que tout le monde puisse ajouter des blocs. L’anonymat reste préservé, car même si n’importe qui peut écrire dans la blockchain, cela ne signifie pas que les identités sont exposées.

---

I am mining bitcoin. In what order do I need to try nonces to maximize my chances?
1. In ascending order (0, 1, …)
2. In descending order (2^32, 2^32-1, …)
3. Doesn’t matter
4. Other (community is sharing algorithms everyday)

**Réponse:** 3  
**Pourquoi ?**  
Le minage est une recherche aléatoire : l’ordre dans lequel les nonces sont testés n’a aucun impact sur les chances de succès. Les mineurs utilisent des algorithmes optimisés qui ne suivent pas nécessairement un ordre strict (ascending ou descending).

**Pourquoi les autres réponses sont fausses ?**  
Essayer en ordre croissant ou décroissant ne change rien, car le hash est imprévisible. La communauté partage des algorithmes, mais cela ne garantit pas un ordre optimal unique.

---

Using a 51% attack, what can the attacker do?
1. Create bitcoins
2. Cancel transactions
3. Blacklist people
4. Steal bitcoins

**Réponse:** 2, 3  
**Pourquoi ?**  
Un attaquant contrôlant plus de 50% du réseau peut réorganiser la blockchain, annulant des transactions passées (double dépense). Il peut censurer certaines transactions et empêcher certaines adresses d’envoyer ou recevoir des fonds (blacklistage).

**Pourquoi les autres réponses sont fausses ?**  
Il ne peut pas créer de nouveaux bitcoins, car l’émission est contrôlée par le protocole. Il ne peut pas voler directement des bitcoins, sauf s’il annule des transactions après qu’elles ont été confirmées.

---

Which of the following concepts are deterministic?
1. The validity of a signature
2. The shape of a coffee stain on paper
3. The sentence for a crime
4. The results of presidential elections

**Réponse:** 1, 2, 3, 4  
**Pourquoi ?**  
Une signature est déterministe : une signature donnée pour un même message est toujours vérifiable. La forme d'une tache de café est déterminée par les lois de la physique, donc même si elle semble aléatoire, elle est en réalité déterminée par des facteurs physiques précis. Une sentence pour un crime suit un cadre juridique défini, donc elle est prédictible dans un système légal structuré. Les résultats d’élections sont déterminés par les votes, même si influencés par de nombreux facteurs.

---

"The forger is always Alice" is a consensus algorithm
1. Yes
2. No

**Réponse:** 1  
**Pourquoi ?**  
Un consensus algorithmique est un ensemble de règles définissant qui peut ajouter un bloc à la blockchain. Dire qu’Alice est toujours la forgeron est une règle simple (même si très mauvaise !), donc c’est bien un algorithme de consensus, même s’il ne respecte pas l’idée de décentralisation.

**Pourquoi la réponse "No" est fausse ?**  
Ce n’est pas un bon algorithme, mais c’est quand même un algorithme : il y a une règle claire qui permet de désigner le forgeron.

---

The hash of latest block is 42. Which of those 4 tickets (whose hash is given) is the big winner of Proof-of-Stake?
- -35
- 120
- 4782374
- 420

**Réponse:** 1  
**Pourquoi ?**  
Dans PoS, le gagnant est généralement déterminé par une règle où le hash d’un ticket est comparé à celui du dernier bloc. Le plus proche du hash précédent (42) est -35.

**Pourquoi les autres réponses sont fausses ?**  
120, 4782374, et 420 sont plus éloignés de 42 que -35, donc ils ne sont pas choisis.

## Proof-of-Stake (PoS)

### Question:
In Proof-of-Stake (PoS) can I at any point know how many tokens I should have staked to be guaranteed to be the next forger?

- Yes
- No

**Réponse :** 1

**Pourquoi ?**
PoS fonctionne généralement en choisissant un forgeron en fonction du nombre de tokens mis en jeu. Si une personne détient suffisamment de tokens, elle peut s’assurer d’être sélectionnée en contrôlant une part majoritaire du réseau.

**Pourquoi la réponse "No" est fausse ?**
PoS est basé sur des probabilités pondérées par les tokens stakés, donc avec assez de tokens, on peut garantir d’être choisi.

### Question:
Delphine and Bob find at the same time a valid nonce for next block. Who wins?

- The one who has more zeros
- Both until some point
- The eldest on the blockchain
- The richest

**Réponse :** 2

**Pourquoi ?**
Lorsqu’un fork temporaire se produit (deux blocs valides trouvés en même temps), les deux coexistent jusqu’à ce qu’un autre bloc vienne les départager. Le réseau suit la chaîne la plus longue (celle qui accumule le plus de travail), donc au bout d’un certain temps, un des deux blocs sera abandonné.

**Pourquoi les autres réponses sont fausses ?**
- Avoir plus de zéros ne garantit pas d’être sélectionné.
- L’ancienneté n’a pas d’impact sur qui gagne.
- La richesse ne joue pas de rôle en Proof-of-Work (PoW).

## Proof-of-Work (PoW)

### Question:
In a PoW (Proof-of-Work) blockchain, which is true?

- There is a good chance we have two blocks with the same hash in the blockchain
- The more zeros there is in the hash, the better the reward
- There can be blocks with no certificates in it
- In some rare cases (excluding 51% attacks), transactions can be canceled

**Réponse :** 3, 4

**Pourquoi ?**
- **(3) "Il peut y avoir des blocs sans certificats" :**
    Un bloc contient des transactions, mais il peut arriver qu'un bloc soit vide (sans transactions). Cela arrive si un mineur trouve un bloc très rapidement après le précédent et qu’aucune transaction n’a encore été ajoutée au mempool. Cela ne compromet pas la validité du bloc, car ce qui compte, c'est qu'il respecte les règles de la blockchain (ex : bonne structure, bon hash, etc.).
- **(4) "Des transactions peuvent être annulées dans certains cas" :**
    Parfois, une transaction peut être annulée si elle fait partie d’un bloc qui devient orphelin. Un bloc est "orphelin" si un autre mineur a trouvé un autre bloc valide en même temps, et que le réseau décide de suivre l’autre chaîne plus longue. Les transactions du bloc abandonné retournent dans le mempool et doivent être incluses dans un autre bloc.

**Pourquoi les autres réponses sont fausses ?**
- **(1) "Deux blocs peuvent avoir le même hash" :**
    Faux, car un bon algorithme de hachage comme SHA-256 rend extrêmement improbable la génération de deux blocs ayant exactement le même hash. Même une petite modification dans un bloc change totalement son hash (effet avalanche).
- **(2) "Plus il y a de zéros dans le hash, meilleure est la récompense" :**
    Faux, le nombre de zéros dans le hash indique la difficulté de minage, mais la récompense est fixée par le protocole (ex : 6.25 BTC pour un bloc Bitcoin actuellement). Avoir un hash plus difficile ne donne pas une meilleure récompense, cela rend juste le minage plus long.

### Question:
Calculating the hash of a block requires 1 second. If the current PoW difficulty is 2 zeros, how much time in average is needed to forge a block?

- 16 seconds
- 104 seconds
- 128 seconds
- 178 seconds
- 256 seconds

**Réponse :** 4

**Pourquoi ?**
Dans Proof-of-Work (PoW), un mineur doit trouver un hash qui commence par un certain nombre de zéros en notation hexadécimale (ex : 00xxxx...). Chaque chiffre en hexadécimal (0-9 et A-F) a 16 valeurs possibles. Si on veut 2 zéros au début, cela signifie que les deux premiers chiffres hexadécimaux doivent être "00".

**Probabilité d'obtenir un hash valide :**
La probabilité qu’un seul chiffre hexadécimal soit 0 est : 1/16. La probabilité que les deux premiers chiffres soient "00" est donc : 1/16 × 1/16 = 1/256.

**Temps moyen pour trouver un hash valide :**
Si on génère un hash par seconde, alors en moyenne, il faudra 256 essais pour trouver un hash correct. Mais en pratique, la première solution peut être trouvée avant d’avoir testé toutes les possibilités. Le temps moyen suit une loi exponentielle, et la médiane est obtenue avec la formule : (255/256)𝑡 = 0.5. En résolvant cette équation logarithmique, on obtient 178 secondes en moyenne pour qu'un mineur trouve un bloc valide.

### Question:
Do people need to communicate to choose next forger?

- Yes
- No

**Réponse :** 2

**Pourquoi ?**
Dans PoW, il n’y a pas besoin de communication directe pour élire le prochain mineur. Chaque mineur travaille seul sur un problème cryptographique, et celui qui trouve la solution en premier envoie son bloc au réseau. Tous les nœuds vérifient indépendamment que ce bloc est valide, sans besoin de concertation.

**Pourquoi la réponse "Yes" est fausse ?**
Contrairement à PoS (Proof-of-Stake) où un validateur est choisi, ici c’est une compétition ouverte où tout le monde essaie de trouver la solution le plus vite possible. Aucun vote, aucun message entre les mineurs n’est nécessaire pour décider du gagnant. C'est juste une course mathématique.

## Miscellaneous Questions

### Question:
On a new blockchain, Alice is the default forger. Bob decides to stake 1, Charlie 2 and Delphine 3. Who is the likeliest forger for block 1?

- Alice
- Bob
- Charlie
- Delphine
- Everyone

**Réponse :** 1

**Pourquoi ?**
Dans certaines blockchains, le premier bloc (genesis block) est toujours forgé par un compte par défaut (ici Alice). Les mises (stakes) des autres participants ne sont prises en compte qu’après ce premier bloc.

**Pourquoi les autres réponses sont fausses ?**
Bob, Charlie et Delphine ne peuvent pas être sélectionnés pour le premier bloc car leurs stakes ne comptent pas encore.

### Question:
Which of the following systems are decentralized?

- Sending/receiving parcels
- Gossips
- An election
- An epidemic

**Réponse :** 2, 4

**Pourquoi ?**
- Les rumeurs (gossips) se propagent sans un point central de contrôle, donc c'est un réseau décentralisé.
- Une épidémie se propage aussi de manière décentralisée, par interactions locales.

**Pourquoi les autres réponses sont fausses ?**
- L’envoi de colis dépend de services centralisés (ex : La Poste, FedEx).
- Une élection est généralement organisée par un gouvernement ou une institution centrale.

### Question:
How could you know in advance that a file was not fraudulent?

- Its title is right
- Its file extension is right
- It comes from the right IP address
- By downloading it from multiple sources
- There is no guarantee

**Réponse :** 5

**Pourquoi ?**
Aucune de ces méthodes ne garantit à 100% qu’un fichier est légitime. Un titre ou une extension peuvent être falsifiés. Un fichier peut provenir d’une IP légitime mais être compromis. Télécharger depuis plusieurs sources ne prouve pas que le fichier est authentique.

### Question:
Is it mandatory to keep a full copy of the blockchain to be a validator?

- Yes
- No

**Réponse :** 2

**Pourquoi ?**
Un validateur dans un réseau Proof-of-Stake (PoS) ou même Proof-of-Work (PoW) n’a pas nécessairement besoin d’avoir une copie complète de la blockchain. Un validateur peut fonctionner avec une version "light" de la blockchain qui ne conserve que les headers des blocs et les informations nécessaires à la validation des transactions. Des nœuds "light" (clients légers) permettent d’économiser du stockage tout en participant à la validation.

**Pourquoi la réponse "Yes" est fausse ?**
Seuls les "full nodes" conservent toute la blockchain, mais un validateur peut utiliser un "light client" qui se connecte aux full nodes pour vérifier les blocs sans les stocker entièrement.

### Question:
Alice owns no node/validator. Can she stake?

- Yes
- No

**Réponse :** 1

**Pourquoi ?**
Dans un système Proof-of-Stake (PoS), il est possible de staker ses tokens sans posséder de nœud complet. Alice peut déléguer ses tokens à un validateur existant (exemple : sur Ethereum 2.0, Cardano, Solana). Cela permet aux petits investisseurs de participer à la sécurisation du réseau sans avoir d’infrastructure technique.

### Question:
Among the following tests, which are mandatory for validating a block sent by another node?

- All of its certificates are more recent than any other in previous blocks
- Its forger is right
- All of its certificates are unique
- The sending node never failed me

**Réponse :** 2, 3

**Pourquoi ?**
- **(2) "Its forger is right" :**
    Un bloc doit être signé par un forgeron valide (c’est-à-dire un mineur en PoW ou un validateur en PoS). Si le forgeron n’a pas été élu par le protocole, le bloc est invalide.
- **(3) "All of its certificates are unique" :**
    Chaque certificat (transaction, signature) doit être unique pour éviter les doublons et les fraudes (comme la double dépense).

**Pourquoi les autres réponses sont fausses ?**
- **(1) "All of its certificates are more recent than any other in previous blocks" :**
    Faux, car un bloc peut contenir des transactions plus anciennes qui n’ont pas encore été confirmées. L’ordre exact des transactions n’a pas besoin d’être strictement chronologique.
- **(4) "The sending node never failed me" :**
    Faux, car la validation d’un bloc repose sur les règles cryptographiques et non sur la "confiance" envers un nœud.

### Question:
In a fully decentralized network, where all machines are connected to all other machines, which mathematical function describes the growth of the amount of connections in total?

- N
- N²
- N^3
- 2^N
- N!

**Réponse :** 2

**Pourquoi ?**
Dans un réseau totalement connecté, chaque machine est connectée à toutes les autres. Le nombre total de connexions possibles dans un réseau complet est donné par la formule des combinaisons : 𝐶(𝑁,2) = 𝑁(𝑁−1)/2 ≈ 𝑁². Cela signifie que si N machines sont présentes, le nombre de connexions croît proportionnellement à N².

### Question:
In the following network,
1 connected to 2,3
2 connected to 1,3,4,5
3 connected to 1,2,4
4 connected to 2,3
5 connected to 2
every connection works and needs 1 second to send data. Alice inputs a certificate on node 1. How much time passes before Alice can be sure it is going to be in the next block?

- 1 second
- 2 seconds
- 3 seconds
- 4 seconds

**Réponse :** 2

**Pourquoi ?**
Chaque connexion prend 1 seconde pour transmettre l’information.

**Propagation des données dans le réseau :**
- À t = 1s : Le certificat est transmis aux nœuds 2 et 3.
- À t = 2s : Les nœuds 2 et 3 retransmettent aux autres (4 et 5).

Tous les nœuds ont maintenant le certificat après 2 secondes.

**Pourquoi les autres réponses sont fausses ?**
- 1 seconde : Faux, car le certificat n’a atteint que 2 nœuds à ce stade.
- 3 ou 4 secondes : Faux, car la propagation s’effectue en 2 étapes seulement.
### Question 21:
**I lost my private key. Who can give it back to me?**

- I can find it in the blockchain
- Any node
- The last node I sent a certificate to
- No one. It's lost forever

**Réponse:** 4

**Pourquoi?**
Une clé privée n’est jamais stockée dans la blockchain. Elle est générée localement et n’est connue que par son propriétaire. Si vous la perdez, personne ne peut la récupérer.

**Pourquoi les autres réponses sont fausses?**
1. "Dans la blockchain" : Impossible, car seule la clé publique est exposée.
2. "Un nœud peut la retrouver" : Faux, les nœuds n’ont aucun accès aux clés privées des utilisateurs.
3. "Le dernier nœud que j’ai utilisé" : Faux, la blockchain ne stocke pas cette information.

### Question 22:
**In a 4-node network, each directly connected to all others, we forge a 1 MB block. What amount of data in total will transit on the network?**

- 3 MB
- 6 MB
- 12 MB
- 18 MB

**Réponse:** 3

**Pourquoi?**
Chaque nœud doit envoyer le bloc de 1 MB aux 3 autres. Il y a 4 nœuds, donc 4 × 3 = 12 MB en circulation.

### Question 23:
**In which situation can I add an illegal certificate to the blockchain?**

- I own >50% of the staked tokens
- I own >50% of the network validators
- I know everyone's private keys
- Never

**Réponse:** 2

**Pourquoi?**
Dans Proof-of-Stake (PoS), un attaquant contrôlant plus de 50% des validateurs peut censurer ou modifier des blocs. Il peut inclure des certificats frauduleux et forcer leur validation.

**Pourquoi les autres réponses sont fausses?**
1. "Posséder >50% des tokens" : Pas suffisant, car il faut aussi être validateur actif.
3. "Connaître toutes les clés privées" : Cela permettrait de voler des fonds, mais pas de modifier directement la blockchain.
4. "Jamais" : Faux, un attaquant avec >50% des validateurs peut manipuler la blockchain.

### Question 24:
**Can I cancel a certificate?**

- No
- Yes, until it reaches a validator
- Yes, until a block containing it has been forged
- Yes

**Réponse:** 3

**Pourquoi?**
Une transaction (certificat) est annulable tant qu’elle n’a pas été incluse dans un bloc. Une fois qu’un bloc est validé, elle devient immuable.

**Pourquoi les autres réponses sont fausses?**
1. "Non" : Faux, car avant d’être confirmée, une transaction peut être annulée ou remplacée.
2. "Jusqu’à un validateur" : Faux, un validateur peut encore décider de ne pas inclure la transaction.
4. "Toujours annulable" : Faux, après inclusion dans un bloc, c’est définitif.

### Question 25:
**What's the supposed name of the inventor of Bitcoin?**

- Satoshi Nakamoto
- Hayao Miyazaki
- Ryohei Arisu
- Eiichiro Oda

**Réponse:** 1

**Pourquoi?**
Satoshi Nakamoto est le pseudonyme du créateur de Bitcoin et du whitepaper de 2008. Son identité reste inconnue, et il a disparu des médias en 2011.

**Pourquoi les autres réponses sont fausses?**
2. Hayao Miyazaki : Réalisateur de films d’animation japonais (Studio Ghibli).
3. Ryohei Arisu : Personnage fictif de Alice in Borderland.
4. Eiichiro Oda : Créateur du manga One Piece.

### Question 26:
**Which mechanism makes the third party obsolete?**

- The consensus algorithm
- The signature process
- The distinction between validators and nodes
- The hashing chain between blocks

**Réponse:** 1

**Pourquoi?**
Le consensus algorithmique (PoW, PoS, etc.) permet au réseau d’atteindre un accord décentralisé sans intermédiaire. Il remplace les tiers de confiance (banques, notaires, etc.) en garantissant la validité des transactions.

**Pourquoi les autres réponses sont fausses?**
2. La signature garantit l’authenticité, mais pas l’élimination d’un tiers de confiance.
3. La distinction entre nœuds et validateurs est une structure interne, elle ne remplace pas un tiers.
4. La chaîne de hash sécurise les blocs, mais ne supprime pas directement le besoin d’un intermédiaire.

### Question 27:
**Among the following flaws of third parties, which ones are addressed by blockchain technologies in general?**

- Speed
- Trust
- Bias
- Fees
- Privacy

**Réponse:** 2, 3

**Pourquoi?**
2. La blockchain remplace la "confiance" par des règles cryptographiques. Les utilisateurs n'ont pas besoin de faire confiance à une banque ou une entité centrale.
3. La blockchain élimine les biais humains, car les règles sont fixées dans le protocole et appliquées de manière impartiale.

**Pourquoi les autres réponses sont fausses?**
1. La vitesse dépend de la blockchain : certaines sont lentes (Bitcoin), d’autres rapides (Solana). Ce n’est pas une garantie.
4. Les frais existent toujours (ex : gas fees sur Ethereum), même s’ils sont parfois réduits.
5. La vie privée n’est pas forcément garantie : la plupart des blockchains publiques (Bitcoin, Ethereum) sont transparentes.

### Question 28:
**Who decides the logic that results from all kinds of statements?**

- The issuer of the statement
- The official blockchain software
- The validators
- The next forger

**Réponse:** 2

**Pourquoi?**
Les règles de la blockchain sont définies dans son code source (le logiciel officiel). Chaque participant applique les mêmes règles pour éviter toute divergence.

**Pourquoi les autres réponses sont fausses?**
1. L’émetteur d’une transaction ne décide pas des règles, il ne fait que proposer une action.
3. Les validateurs appliquent les règles, mais ne les créent pas.
4. Le forgeron ne change pas les règles, il applique seulement le protocole existant.

### Question 29:
**If Bob is out of money, what can happen?**

- He gets debts
- The smart contracts consider Alice’s flat to be free of rent
- The smart contract removes Bob’s rental certificate from the blockchain
- The smart contract gives 3 months to Bob to pay

**Réponse:** 1, 2, 4

**Pourquoi?**
1. Un smart contract peut enregistrer des dettes si c’est programmé ainsi.
2. S’il n’y a pas de paiement, le contrat peut conclure que le bien devient gratuit.
4. Un délai de paiement peut être inclus dans la logique du contrat.

**Pourquoi la réponse 3 est fausse?**
Un smart contract ne peut pas supprimer des données de la blockchain, tout est immuable.

### Question 30:
**Why are Smart Contracts using the term "Contract"?**

- Because it involves more than one party in the process
- Because it is legally binding
- Because it is signed
- Because it describes a fixed set of rules

**Réponse:** 4

**Pourquoi?**
Un smart contract définit des règles fixes que tout le monde doit suivre. Contrairement à un contrat classique, il s’exécute automatiquement selon son code.

### Question 31:
**Each user only has one identity on the blockchain**

- Yes
- No

**Réponse:** 2

**Pourquoi?**
Un utilisateur peut créer autant d’adresses blockchain qu’il le souhaite. Rien ne lie une adresse à une personne réelle.

**Pourquoi la réponse 1 est fausse?**
Contrairement aux systèmes centralisés, il n’y a pas de "compte unique" sur la blockchain.

### Question 32:
**Is it a good thing that the source code of the smart contract is public?**

- Yes
- No
- Both

**Réponse:** 3

**Pourquoi?**
Avantage : Transparence et auditabilité par tous. Inconvénient : Un attaquant peut analyser le code pour y trouver des failles.

### Question 33:
**How do you "burn" cryptocurrencies?**

- You send it to yourself
- You send a negative amount
- You send it to the black hole
- It is up to the blockchain to provide such a feature

**Réponse:** 3

**Pourquoi?**
Une adresse "black hole" (sans clé privée connue) est utilisée pour envoyer définitivement des cryptos sans possibilité de récupération.

### Question 34:
**What is handled differently between smart contracts and traditional algorithmics?**

- Randomness
- Data storage
- Permissions
- Time management

**Réponse:** 1, 4

**Pourquoi?**
1. Randomness : Les blockchains ne peuvent pas générer du hasard de manière classique. Elles utilisent des oracles ou des méthodes complexes comme les VRF.
4. Time management : Il n’y a pas de notion de "temps réel", on utilise le numéro du bloc comme référence temporelle.

### Question 35:
**In arts, to increase the value of an NFT collection, you can...**

- "Burn" the contract
- Forbid the transfer of NFTs
- Code it the simplest way possible
- Store the pictures on a blockchain

**Réponse:** 1, 3, 4

**Pourquoi?**
1. "Burner" le smart contract réduit l’offre et peut augmenter la rareté des NFTs.
3. Un code simple évite les bugs et rend les NFTs plus sûrs.
4. Stocker les images sur une blockchain garantit leur pérennité.

**Pourquoi la réponse 2 est fausse?**
Interdire les transferts réduit la liquidité et l’intérêt de l’œuvre.

### Question 36:
**NFT stands for...**

- Non Fungible Token
- Tokens non gongibles
- No finding technology
- No Forge Token

**Réponse:** 1

**Pourquoi?**
NFT signifie "Non-Fungible Token", ce qui signifie qu'il est unique et ne peut pas être échangé à l'identique comme une cryptomonnaie classique.

### Question 37:
**Delphine transfers her NFT to Bob but mistypes one character of his public key. What happens?**
### Question 37:
What happens if you send an NFT to an incorrect address?

1. The NFT is burnt
2. The contract refuses the transfer
3. The contract owner gets the NFT
4. It depends on how the contract is coded

**Réponse :** 4

**Pourquoi ?**
Tout dépend du smart contract :
- S’il n’existe pas d’adresse associée à la clé erronée, les fonds peuvent être perdus définitivement (burn involontaire).
- Certains contrats implémentent des protections, comme une vérification préalable de l'adresse du destinataire.

**Pourquoi les autres réponses sont fausses ?**
1. L’NFT peut être perdu, mais pas nécessairement "brûlé" (envoyé dans une adresse black hole).
2. La plupart des smart contracts n'ont pas de mécanisme de correction automatique.
3. Le propriétaire du contrat ne reçoit pas l’NFT, sauf si le contrat le prévoit.

### Question 38:
What is a blockchain?

1. A data structure
2. An autonomous software
3. A cryptocurrency
4. A deterministic ledger

**Réponse :** 1

**Pourquoi ?**
Une blockchain est avant tout une structure de données (data structure) sous forme de blocs liés cryptographiquement.

**Pourquoi les autres réponses sont fausses ?**
2. "Un logiciel autonome" : Une blockchain repose sur des logiciels, mais elle n’est pas elle-même un logiciel autonome.
3. "Une cryptomonnaie" : Bitcoin utilise une blockchain, mais toutes les blockchains ne sont pas des cryptomonnaies.
4. "Un ledger déterministe" : Une blockchain est un registre, mais peut contenir des processus non totalement déterministes (ex : smart contracts).

### Question 39:
What is the process that ensures the validity of a certificate?

1. The consensus algorithm
2. The hashing
3. The signature
4. The staking

**Réponse :** 3

**Pourquoi ?**
La signature cryptographique garantit l'authenticité d’un certificat et permet de vérifier qu'il n'a pas été falsifié.

**Pourquoi les autres réponses sont fausses ?**
1. Le consensus valide des blocs entiers, pas chaque certificat individuellement.
2. Le hashing sécurise le stockage, mais ne prouve pas l’authenticité d’un certificat.
4. Le staking est un mécanisme d’incitation dans PoS, pas un moyen de validation de certificats.

### Question 40:
Given you have the public key of your neighbor, what can you do?

1. Issue certificates on his behalf
2. Find his private key
3. Steal cryptocurrency from him
4. Check what certificates he issued in the blockchain

**Réponse :** 4

**Pourquoi ?**
Avec une clé publique, on peut vérifier les transactions et certificats qu’elle a signés.

**Pourquoi les autres réponses sont fausses ?**
1. "Émettre des certificats en son nom" : Impossible sans sa clé privée.
2. "Trouver sa clé privée" : Cryptographiquement infaisable avec RSA ou ECDSA.
3. "Voler des cryptos" : Impossible sans la clé privée pour signer des transactions.

### Question 41:
What is a consensus algorithm?

1. A process of exchanging information between nodes to agree on a forger
2. A deterministic algorithm that generates blocks
3. A rule that dictates whether a block should be accepted or not
4. An algorithm that broadcasts blocks in a peculiar manner

**Réponse :** 3

**Pourquoi ?**
Le consensus détermine quelles transactions/blocs sont valides et doivent être acceptés par le réseau.

### Question 42:
Which of the following is true?

1. Hashing is algorithmically reversible
2. Hashing always produces a different outcome for the same input
3. Hashing always produces a different outcome for different inputs
4. Hashing produces very different outputs for almost identical inputs

**Réponse :** 4

**Pourquoi ?**
Une légère modification de l’entrée entraîne un changement drastique du hash (effet avalanche).

**Pourquoi les autres réponses sont fausses ?**
1. Le hashing est irréversible par définition.
2. Une même entrée donne toujours le même hash.
3. Des entrées différentes peuvent exceptionnellement produire le même hash (collision).

### Question 43:
To write data in a smart contract, I must...

1. Run the smart contract on my local machine
2. Ask at least 51% of nodes to do it for me
3. Issue a new certificate
4. Change the certificate that declared the smart contract

**Réponse :** 3

**Pourquoi ?**
L’ajout de données passe par une transaction signée qui modifie l’état du contrat.

### Question 44:
Which of the following is not a valid hash in base 32?

1. 0110010011
2. 0000000000
3. 47bbe6ac80
4. w6453jkhu6

**Réponse :** 4

**Pourquoi ?**
En base 32, on utilise les chiffres de 0 à 9 et les lettres de A pour 10 à V pour 31. "w" et "u" ne sont pas des caractères valides en base 32.

### Question 45:
What is true about Proof-of-Work and Proof-of-Stake?

1. They both calculate who the next forger is
2. They were created by the same person
3. PoW checks block validity faster than PoS
4. PoS ensures newcomers have the same chances to forge than old players

**Réponse :** 3

**Pourquoi ?**
PoW valide plus rapidement car chaque nœud peut vérifier le hash du bloc immédiatement. PoS nécessite plus de vérifications pour savoir si un validateur est légitime.

**Pourquoi les autres réponses sont fausses ?**
1. Les mécanismes sont très différents : PoW = compétition, PoS = sélection basée sur la mise.
2. PoW a été inventé avec Bitcoin (Satoshi Nakamoto), PoS est venu plus tard (Sunny King).
4. Les anciens validateurs ont souvent plus de poids en PoS.

### Question 46:
Assuming you would want to write a blockchain for a private company, what consensus algorithm would you rather use?

1. Proof-of-Work
2. Proof-of-Stake
3. Delegated Proof-of-Stake
4. Proof-of-Authority
5. Proof-of-Burn

**Réponse :** 4

**Pourquoi ?**
Proof-of-Authority (PoA) est idéal pour les blockchains privées, car il repose sur un nombre limité de validateurs de confiance (ex : administrateurs de l’entreprise). Il est plus rapide et plus efficace que PoW ou PoS, car il ne nécessite pas une compétition pour le minage. Les entreprises préfèrent un modèle centralisé où les décisions sont validées par des nœuds approuvés plutôt que par des mineurs ou des validateurs aléatoires.

**Pourquoi les autres réponses sont fausses ?**
1. PoW : Consomme trop d’énergie et est inutilement complexe pour une entreprise privée.
2. PoS : Moins efficace que PoA pour un environnement centralisé.
3. DPoS : Nécessite une gouvernance communautaire, ce qui n’est pas optimal pour une entreprise privée.
5. PoB : Basé sur la destruction de jetons, inadapté à une blockchain d’entreprise.

### Question 47:
Why is the Byzantine Generals Problem, while still being a good illustration, a somehow misleading explanation of what consensus algorithms are?

1. Because it involves a third party
2. Because it is restricted to a binary output being attack/retreat
3. Because the decision needs to be taken at a specific time
4. Because the generals exchange messages

**Réponse :** 4

**Pourquoi ?**
Le problème des généraux byzantins suppose que les nœuds échangent des messages directement pour parvenir à un consensus. Dans les blockchains, ce consensus est souvent atteint de manière probabiliste (ex : PoW) ou en fonction de règles économiques (ex : PoS), pas uniquement par des messages directs.

### Question 48:
We are at block 42 of a Proof-of-Stake blockchain. Alice staked 2 yet, and Bob staked 4. How much should Alice stake right now to have 60% chances of forging block 43?

1. 2
2. 4
3. 6
4. She can't

**Réponse :** 4

**Pourquoi ?**
Dans Proof-of-Stake (PoS), la sélection du forgeron du prochain bloc (ici, le bloc 43) se fait en fonction de la mise (stake) placée avant un certain moment.

Actuellement, Alice a 2 tokens misés. Bob a 4 tokens misés. Le processus de sélection fonctionne sur la proportion de tokens stakés. Actuellement, Alice a 2 / (2+4) = 33,3% de chances d’être sélectionnée, et Bob a 66,7%. Pour qu’Alice ait 60% de chances, il faudrait qu’elle ait misé une quantité supérieure à celle de Bob avant le début du tirage.

**Pourquoi Alice ne peut pas modifier ses chances maintenant ?**
Le staking a déjà été pris en compte au bloc 42, donc ajouter des tokens après ne change rien pour la sélection du bloc 43. Elle pourra augmenter ses chances pour les blocs suivants, mais pas pour celui en cours.

### Question 49:
Which of the following can cause cryptocurrencies to be created outside of the scope allowed by the blockchain software?

1. If someone holds all the private keys of all blockchain users
2. An update of the programming language the blockchain software uses
3. A 51% attack that aims at reverting a specific certificate
4. Reworking the blockchain software and deploying it on my node

**Réponse :** 2

**Pourquoi ?**
Si la blockchain est écrite dans un langage de programmation (ex : Solidity pour Ethereum), une mise à jour de ce langage peut introduire des failles. Un bug dans la mise à jour pourrait permettre la création de tokens non autorisés (ex : un bug similaire a déjà causé des problèmes dans Ethereum avec un smart contract mal conçu).

**Pourquoi les autres réponses sont fausses ?**
1. Détenir toutes les clés privées ne permet pas de créer de nouvelles cryptos, juste de voler celles existantes.
3. Une attaque 51% permet d’annuler des transactions mais ne crée pas de nouvelles cryptos hors protocole.
4. Modifier le logiciel de son propre nœud n’a aucun impact sur le protocole global de la blockchain.
