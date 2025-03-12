from smart_contract import SmartContractDefinition, SmartContractWritingOperation, WritingOperationArguments


# -----------------------------------------------------------
# DÉFINITION DE LA CLASSE SmartContract POUR LA GESTION DES NFT
# -----------------------------------------------------------
# La classe SmartContract implémente toute la logique métier relative à une collection de NFT :
# - Création (mint) d’un nouveau NFT
# - Transfert d’un NFT d’un utilisateur à un autre
# - Affichage de l’état de la collection, etc.
class SmartContract():
    
    # Constructeur du smart contract.
    # Il initialise le contrat avec des paramètres essentiels tels que le nom de la collection,
    # la période autorisée pour le mint, la limite du nombre de NFT, etc.
    def __init__(self, name: str, start_mint_timestamp: int, max_token = 10, mint_time: int = 60000):
        self.name = name  # Le nom de la collection, qui identifie le projet NFT.
        self.token_id = 0  # Un compteur qui démarre à zéro et s'incrémente à chaque nouveau NFT.
        
        # Dictionnaire qui associe chaque NFT (par son identifiant) à la clé publique de son propriétaire.
        # Cela permet de tracer la propriété de chaque NFT sur la blockchain.
        self.token_owners = {}  
        self.max_token = max_token  # Le nombre maximum de NFT pouvant être créés, garantissant la rareté.
        # Timestamp indiquant le début de la période pendant laquelle le mint est autorisé.
        self.start_mint_timestamp = start_mint_timestamp  
        self.mint_time = mint_time  # La durée (en millisecondes) pendant laquelle le mint est possible.

    # Méthode mint() qui permet de créer un nouveau NFT.
    # Avant de créer le NFT, la méthode vérifie que le nombre maximum n'est pas dépassé
    # et que l'opération se situe dans la période de mint autorisée.
    def mint(self, operation_arguments: SmartContractWritingOperation) -> tuple[int, str]:
        # Vérification de la limite de création : si le nombre de NFT créés atteint ou dépasse la limite...
        if self.token_id >= self.max_token:
            # ...on retourne une erreur pour empêcher la création d'un NFT supplémentaire.
            return None, "Maximum number of tokens reached"
        # Vérification temporelle : le timestamp de l'opération doit être entre le début du mint et la fin de la fenêtre autorisée.
        if operation_arguments.timestamp < self.start_mint_timestamp or \
           operation_arguments.timestamp > self.start_mint_timestamp + self.mint_time:
            # Si l'opération n'est pas dans la bonne période, on renvoie un message d'erreur.
            return None, "Minting is not allowed at this time"
        # Si toutes les conditions sont réunies, on incrémente le compteur de NFT.
        self.token_id += 1
        # On associe le nouveau NFT à l'émetteur de l'opération en enregistrant sa clé publique.
        self.token_owners[self.token_id] = operation_arguments.issuerPublicKey
        # On retourne l'identifiant du NFT nouvellement créé et None pour indiquer l'absence d'erreur.
        return self.token_id, None

    # Méthode statique mint_certificate() qui crée un certificat d'opération de mint.
    # Ceci permet de standardiser et d'encapsuler la création d'une demande de mint dans un objet signé.
    @staticmethod
    def mint_certificate(issuerPublicKey: str, targetSmartContract: SmartContractDefinition) -> SmartContractWritingOperation:
        # On retourne une instance de SmartContractWritingOperation configurée pour exécuter la fonction "mint".
        return SmartContractWritingOperation(issuerPublicKey, targetSmartContract.hash(), "mint")
        
    # Méthode transfer() qui permet de transférer un NFT d'un utilisateur à un autre.
    # La méthode vérifie que le transfert est valide en s'assurant que l'émetteur est bien le propriétaire
    # et que le destinataire n'est pas déjà le propriétaire.
    def transfer(self, to: str, token_id: int, operation_arguments: SmartContractWritingOperation) -> tuple[None , str]:
        # Vérification : si le destinataire est déjà le propriétaire du NFT, le transfert est inutile.
        if self.token_owners[token_id] == to:
            return None, "You are already the owner of this token"
        # Vérification de l'identité : seul le propriétaire actuel (indiqué par la signature) peut transférer son NFT.
        if self.token_owners[token_id] != operation_arguments.issuerPublicKey:
            return None, "You are not the owner of this token"
        # Si les vérifications sont franchies, on met à jour la propriété du NFT en assignant le token au nouveau propriétaire.
        self.token_owners[token_id] = to
        # On retourne un tuple indiquant que le transfert s'est effectué sans erreur.
        return None, None
        
    # Méthode statique transfer_certificate() qui génère un certificat d'opération de transfert.
    # Cela permet de créer de manière standardisée une demande de transfert, qui sera signée et vérifiée sur la blockchain.
    @staticmethod
    def transfer_certificate(issuerPublicKey: str, targetSmartContract: SmartContractDefinition, to: str, token_id: int) -> SmartContractWritingOperation:
        # On crée et retourne une instance de SmartContractWritingOperation configurée pour exécuter "transfer",
        # en passant la clé du destinataire et l'identifiant du NFT dans la liste des arguments.
        return SmartContractWritingOperation(issuerPublicKey, targetSmartContract.hash(), "transfer", [to, token_id])

    # Méthode get_owner() qui retourne la clé publique du propriétaire d'un NFT identifié par token_id.
    def get_owner(self, token_id: int):
        return self.token_owners[token_id]

    # Méthode display() qui affiche l'état global du smart contract.
    # Ceci inclut le nom de la collection, la liste des NFT et de leurs propriétaires, ainsi que les paramètres de mint.
    def display(self):
        print(f"SmartContract {self.name}:")  # Affiche le nom du smart contract pour identifier la collection.
        # Affiche la liste des NFT avec un extrait de la clé publique de chaque propriétaire pour la lisibilité.
        print('Token owners:', [f"{token_id}: {owner[256:264]}" for token_id, owner in self.token_owners.items()])
        print('Start mint timestamp:', self.start_mint_timestamp)  # Affiche le moment de début du mint.
        print('Mint time:', self.mint_time)  # Affiche la durée pendant laquelle le mint est autorisé.
        print('Token id:', self.token_id)  # Affiche le nombre total de NFT créés.

    # Méthode get_nft_icon() qui retourne un emoji unique basé sur l'identifiant du NFT.
    # Pourquoi ? L'utilisation d'emojis permet d'attribuer une représentation visuelle ludique et unique à chaque NFT.
    def get_nft_icon(self, token_id: int) -> str:
        """Returns a unique Unicode emoji based on token_id"""
        base_unicode = 0x1F400  # Le point de départ dans la table Unicode (ici, l'emoji du rat).
        # On calcule un emoji en ajoutant au code de base le reste de la division du token_id par 80,
        # ce qui permet de "cycler" parmi 80 emojis et d'assurer que chaque NFT ait une icône déterministe.
        return chr(base_unicode + (token_id % 80))
