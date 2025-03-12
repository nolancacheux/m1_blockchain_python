# -----------------------------------------------------------
# IMPORTATIONS ET PRÉPARATION DE L'ENVIRONNEMENT
# -----------------------------------------------------------
# On importe le type List depuis le module typing.
# Ceci nous permet d’utiliser des annotations de type pour préciser le contenu des listes.
# Dans un projet blockchain, la clarté des types aide à éviter les erreurs dans le passage d’arguments,
# notamment lorsque l’on transmet des données sensibles comme les arguments d’un smart contract.
from typing import List  

# On importe la classe Blockchain depuis le module dédié.
# La classe Blockchain représente la structure entière de la chaîne de blocs, avec ses blocs et certificats.
# Ici, nous aurons besoin de parcourir cette blockchain pour reconstituer l’état final d’un smart contract.
from blockchain import Blockchain  

# On importe la classe Certificate depuis le module certificate.
# Certificate est la classe de base qui gère l’authenticité, la signature, et le hash des certificats,
# essentiels pour garantir que chaque opération enregistrée sur la blockchain est vérifiée et non modifiée.
from certificate import Certificate  

# -----------------------------------------------------------
# DÉFINITION DE LA CLASSE SmartContractDefinition
# -----------------------------------------------------------
# La classe SmartContractDefinition hérite de Certificate afin de bénéficier des fonctionnalités
# de signature et de vérification. Elle représente la « publication » ou le déploiement d’un smart contract
# sur la blockchain, et stocke le code source complet qui sera exécuté pour créer le contrat.
class SmartContractDefinition(Certificate):
    # Attribut destiné à contenir le code source du smart contract sous forme de chaîne de caractères.
    # Ce code source définit la logique (les règles) du smart contract, ici pour gérer des NFT.
    sourceCode: str  
    # Attribut qui contient la liste des arguments à passer lors de l’instanciation du smart contract.
    # Ces arguments (comme le nom de la collection, le timestamp de début, etc.) permettent de paramétrer
    # le comportement du contrat dès son déploiement.
    classArgumentList: List[any]  

    # Constructeur de la classe SmartContractDefinition.
    # Il reçoit la clé publique de l’émetteur (pour la signature), le code source du contrat,
    # et une liste d’arguments pour l’instanciation.
    def __init__(self, issuerPublicKey: str, sourceCode: str, classArgumentList: List[any] = []):
        # Appel du constructeur de la classe parente Certificate.
        # Ceci initialise la partie sécurité et signature du certificat, garantissant l’intégrité du déploiement.
        super().__init__(issuerPublicKey)
        # On stocke le code source du contrat dans l’attribut sourceCode.
        # Ce code est crucial, car il sera exécuté plus tard pour créer dynamiquement le smart contract.
        self.sourceCode = sourceCode  
        # On enregistre la liste des arguments qui seront passés au constructeur du smart contract lors de son instanciation.
        self.classArgumentList = classArgumentList  

    # Méthode build_payload() : elle construit le dictionnaire de données qui sera signé et enregistré sur la blockchain.
    # Ce payload contient toutes les informations indispensables pour vérifier que le déploiement est authentique.
    def build_payload(self):
        # On commence par récupérer le payload de base hérité de Certificate, qui inclut déjà certaines données sécurisées.
        payload = super().build_payload()  
        # On ajoute ensuite le code source du smart contract dans le payload.
        # Cela permet de s’assurer que le contrat déployé correspond exactement au code qui a été signé.
        payload['sourceCode'] = self.sourceCode  
        # On retourne le payload complet, qui sera utilisé pour calculer le hash et pour la signature.
        return payload  

    # Méthode instantiate_contract() : elle exécute dynamiquement le code source pour créer une instance du smart contract.
    # Pourquoi ? Dans une blockchain, déployer un smart contract consiste à exécuter son code afin de le charger en mémoire.
    def instantiate_contract(self):
        # On utilise exec() pour exécuter le code source stocké dans sourceCode dans l'espace local.
        # Cela transforme le code (qui est une chaîne de caractères) en objets Python réels.
        exec(self.sourceCode)
        
        # Une fois exec() exécuté, la classe SmartContract doit être présente dans l'espace local.
        # On récupère cette classe via locals()['SmartContract'].
        # Ceci suppose que le code source respecte la convention de nommer la classe de contrat "SmartContract".
        contract_class = locals()['SmartContract']
        
        # On instancie le smart contract en appelant son constructeur avec les arguments préalablement stockés.
        # Ces arguments peuvent inclure des informations comme le nom du contrat, la période de mint, etc.
        contract_instance = contract_class(*self.classArgumentList)
        
        # Pour le déboggage, on affiche l'instance créée, ce qui aide à vérifier que l'exécution s'est bien déroulée.
        print(f"Instantiated contract: {contract_instance}")
        
        # On retourne l'instance du smart contract, qui sera utilisée pour appliquer les opérations enregistrées.
        return contract_instance

    # Méthode statique get_smart_contract_at_current_state() :
    # Cette méthode parcourt la blockchain pour reconstituer l'état actuel d'un smart contract en appliquant
    # successivement toutes les opérations (mint, transfert, etc.) qui ont été enregistrées après son déploiement.
    @staticmethod
    def get_smart_contract_at_current_state(blockchain: Blockchain, targetSmartContractHash: str):
        # On initialise une liste pour collecter toutes les opérations qui visent ce smart contract.
        operations = []  
        # On initialise une variable pour retenir la définition initiale (le déploiement) du smart contract.
        smartContractDef = None  

        # On parcourt chaque bloc de la blockchain.
        for block in blockchain.blockList:
            # Pour chaque bloc, on parcourt la liste des certificats qui y sont enregistrés.
            for certificate in block.certificateList:
                # Si le certificat est une SmartContractDefinition et que son hash correspond au hash ciblé...
                if isinstance(certificate, SmartContractDefinition) and certificate.hash() == targetSmartContractHash:
                    # ...alors nous avons trouvé le déploiement initial du contrat.
                    smartContractDef = certificate
                    continue  # On passe au certificat suivant sans exécuter d'autres vérifications.
                # Si le certificat est une opération d'écriture (SmartContractWritingOperation)
                # et que son champ targetSmartContractHash correspond au contrat ciblé...
                if isinstance(certificate, SmartContractWritingOperation) and certificate.targetSmartContractHash == targetSmartContractHash:
                    # ...on ajoute cette opération à la liste, car elle modifiera l'état du contrat.
                    operations.append(certificate)
                    continue

        # Après avoir collecté la définition et toutes les opérations, on instancie le smart contract via sa définition.
        smartContract = smartContractDef.instantiate_contract()

        # On trie ensuite toutes les opérations par ordre chronologique, mais uniquement celles qui ont été
        # effectuées après le déploiement initial (vérification via le timestamp).
        for operation in sorted(filter(lambda x: x.timestamp > smartContractDef.timestamp, operations),
                                key=lambda x: x.timestamp):
            # Pour chaque opération, on l'applique sur l'instance du smart contract, ce qui met à jour son état.
            operation.apply_on_contract(smartContract)
        
        # On retourne l'instance du smart contract dans son état le plus à jour.
        return smartContract

# -----------------------------------------------------------
# DÉFINITION D'UNE CLASSE D'ARGUMENTS POUR LES OPÉRATIONS D'ÉCRITURE
# -----------------------------------------------------------
# La classe WritingOperationArguments encapsule des données simples (clé publique et timestamp)
# qui sont nécessaires pour authentifier et ordonner les opérations sur le smart contract.
class WritingOperationArguments():
    def __init__(self, issuerPublicKey: str, timestamp: int):
        # Stocke la clé publique de l'émetteur, élément fondamental pour vérifier l'identité dans une blockchain.
        self.issuerPublicKey = issuerPublicKey  
        # Stocke le timestamp indiquant le moment précis de l'opération,
        # ce qui est crucial pour respecter l'ordre chronologique et les contraintes temporelles du smart contract.
        self.timestamp = timestamp  

# -----------------------------------------------------------
# DÉFINITION DE LA CLASSE SmartContractWritingOperation
# -----------------------------------------------------------
# Cette classe représente une opération de modification de l'état d'un smart contract, par exemple
# la création (mint) ou le transfert d'un NFT. Elle hérite de Certificate pour assurer que l'opération
# est signée et sécurisée, et qu'elle peut être vérifiée sur la blockchain.
class SmartContractWritingOperation(Certificate):
    # Attribut qui contient le hash identifiant le smart contract cible.
    # Cela permet de lier l'opération à un contrat précis dans la blockchain.
    targetSmartContractHash: str  
    # Attribut qui contient le nom de la fonction à appeler sur le smart contract (par exemple "mint" ou "transfer").
    targetFunctionName: str  
    # Attribut qui contient une liste d'arguments à transmettre à la fonction ciblée.
    # Ces arguments détaillent la nature de l'opération (exemple : nouveau propriétaire, identifiant du token, etc.).
    functionArgumentList: List[any]  

    # Constructeur de la classe SmartContractWritingOperation.
    # Il initialise tous les paramètres spécifiques à l'opération d'écriture sur le smart contract.
    def __init__(self, issuerPublicKey: str, targetSmartContractHash: str, targetFunctionName: str, functionArgumentList: List[any] = []):
        # Appel du constructeur de Certificate pour assurer la signature et l'intégrité de l'opération.
        super().__init__(issuerPublicKey)
        # Enregistre le hash du smart contract ciblé par l'opération.
        self.targetSmartContractHash = targetSmartContractHash  
        # Enregistre le nom de la fonction qui sera appelée sur le smart contract.
        self.targetFunctionName = targetFunctionName  
        # Enregistre la liste des arguments qui seront passés à la fonction appelée.
        self.functionArgumentList = functionArgumentList  

    # Méthode pour construire le payload de l'opération, qui contiendra toutes les informations
    # nécessaires à sa validation et à son enregistrement sur la blockchain.
    def build_payload(self):
        # On récupère d'abord le payload standard hérité de Certificate.
        payload = super().build_payload()  
        # On ajoute au payload le hash du smart contract ciblé.
        payload['targetSmartContractHash'] = self.targetSmartContractHash  
        # On ajoute au payload le nom de la fonction ciblée (définit l'intention de l'opération).
        payload['targetFunctionName'] = self.targetFunctionName  
        # On ajoute au payload la liste des arguments à fournir lors de l'appel de la fonction.
        payload['functionArgumentList'] = self.functionArgumentList  
        # On retourne le payload complet, qui sera utilisé pour la signature et la vérification de l'opération.
        return payload  

    # Méthode apply_on_contract() qui applique l'opération sur l'instance d'un smart contract.
    # Cette méthode est centrale car elle permet de modifier l'état du smart contract en fonction de l'opération.
    def apply_on_contract(self, contract):
        # On récupère la méthode à appeler dans le smart contract en se basant sur le nom stocké dans targetFunctionName.
        # Cela permet une exécution dynamique : le même type d'opération peut être appliqué sur différents contrats.
        target_function = getattr(contract, self.targetFunctionName)
        # On appelle la méthode récupérée en passant la clé publique de l'émetteur (pour l'authentification)
        # et les arguments contenus dans functionArgumentList (déballés grâce à l'opérateur *).
        result = target_function(self.issuerPublicKey, *self.functionArgumentList)
        # On retourne le résultat de l'opération, qui peut être utilisé pour vérifier le succès ou identifier une erreur.
        return result  