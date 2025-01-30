from certificate import Certificate
from helpers import timestamp

class StakingOperation(Certificate):
    
    def __init__(self, issuerPublicKey, tokenAmount):
        super().__init__(issuerPublicKey)
        self.tokenAmount = tokenAmount
        
    def build_payload(self):
        dict_payload = {}
        dict_payload['issuerPublicKey'] = self.issuerPublicKey  
        dict_payload['timestamp'] = self.timestamp 
        dict_payload['tokenAmount'] = self.tokenAmount            
        return dict_payload  

        
    @staticmethod
    def build_staking_accounts(blockList):
        staking_accounts = {}
        for block in blockList:
            for certificate in block.certificateList:
                #debug : print("certificate", certificate)
                if isinstance(certificate, StakingOperation): 
                    # debug : print("true : certificate.issuerPublicKey", certificate.issuerPublicKey)
                    # isinstance() function returns True if the specified object is of the specified type, otherwise False.
                    issuer = certificate.issuerPublicKey
                    amount = certificate.tokenAmount
                    if issuer in staking_accounts: #si il y a déjà un compte pour cet émetteur
                        staking_accounts[issuer] += amount #    on ajoute le montant
                    else:
                        staking_accounts[issuer] = amount #   sinon on crée un nouveau compte
        return staking_accounts
    
    
    
    