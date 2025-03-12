from stake import StakingOperation  
from ticket import RaffleTicket 

class ProofOfStake:
    
    def __init__(self, defaultForgerPublicKey):
        self.defaultForgerPublicKey = defaultForgerPublicKey  # La clé publique par défaut du forgeron

    def hash_distance(self, hash1, hash2):
        hash1_int = int(hash1, 16)  # On convertit le premier hash en entier
        hash2_int = int(hash2, 16)  # On convertit le deuxième hash en entier
        return abs(hash1_int - hash2_int)  # On calcule la distance absolue entre les deux hashs

    def get_next_forger_public_key(self, blockList):
        if not blockList:
            return self.defaultForgerPublicKey  # Si la liste de blocs est vide, on retourne la clé publique par défaut

        staking_accounts = StakingOperation.build_staking_accounts(blockList)  # On construit les comptes de staking à partir de la liste de blocs
        if not staking_accounts:
            return self.defaultForgerPublicKey  # Si aucun compte de staking n'est trouvé, on retourne la clé publique par défaut

        last_block_hash = str(blockList[-1].hash())  # On récupère le hash du dernier bloc sous forme de chaîne de caractères
        closest_distance = None  # On initialise la distance la plus proche à None
        next_forger = None  # On initialise le prochain forgeron à None

        for account, stake in staking_accounts.items():  # On parcourt les comptes de staking et leurs mises
            for ticket_number in range(int(stake)):  # On génère des tickets de loterie en fonction de la mise
                ticket = RaffleTicket(account, ticket_number, last_block_hash)  # On crée un ticket de loterie
                ticket_hash = ticket.hash()  # On calcule le hash du ticket
                distance = self.hash_distance(last_block_hash, ticket_hash)  # On calcule la distance entre le hash du dernier bloc et le hash du ticket
                if closest_distance is None or distance < closest_distance:  # Si la distance est la plus petite trouvée
                    closest_distance = distance  # On met à jour la distance la plus proche
                    next_forger = account  # On met à jour le prochain forgeron

        return next_forger  # On retourne la clé publique du prochain forgeron
    
    def is_next_block_forger_legit(self, blockList, nextBlock):
        next_forger_public_key = self.get_next_forger_public_key(blockList)  # On récupère la clé publique du prochain forgeron
        return next_forger_public_key == nextBlock.issuerPublicKey  # On vérifie si la clé publique du forgeron du prochain bloc correspond à celle du gagnant de la loterie

    def is_blockchain_legit(self, blockchain):
        blockList = blockchain.blockList
        if not blockList:
            return False  # Une blockchain vide n'est pas valide

        for i in range(1, len(blockList)):  # On commence à 1 car le premier bloc est forgé par le black hole
            if not self.is_next_block_forger_legit(blockList[:i], blockList[i]):
                return False  # Si un bloc n'est pas forgé par le bon ""forgeron", la blockchain n'est pas valide

        return True  # Si tous les blocs sont forgés par les bons "forgerons", la blockchain est valide