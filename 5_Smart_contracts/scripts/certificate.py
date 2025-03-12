from helpers import timestamp, cryptography
from json import dumps

class Certificate : 
    
    def __init__(self, issuerPublicKey):
        self.issuerPublicKey = issuerPublicKey
        self.signature = ""
        self.timestamp = timestamp.now() 
    
    def build_payload(self):
        #list_payload = [self.issuerPublicKey, self.timestamp]
        #return list_payload
        dict_payload = {}
        dict_payload['issuerPublicKey'] = self.issuerPublicKey  
        dict_payload['timestamp'] = self.timestamp             
        return dict_payload    
    
    def hash(self):
        payload = self.build_payload()                    
        payloadString = dumps(payload, sort_keys=True)     
        hashed_payload = cryptography.hash_string(payloadString)    
        return hashed_payload
    
    #on réécrit la méthode __hash__ pour que le hash du certificat soit un entier
    def __hash__(self):
        return int(self.hash(), 16)
    
    
    def equals(self,otherCertificate):
        if self.hash() == otherCertificate.hash(): 
            return True
        return False
    
    def __eq__(self, otherCertificate): 
        return self.equals(otherCertificate)
    
    def is_legit(self):
        return cryptography.has_public_key_signed_this_hash(self.issuerPublicKey, self.signature, self.hash())
        
        
    def display(self):
        return {
            'type': self.__class__.__name__,
            'issuerPublicKey': self.issuerPublicKey[:10],#sinon trop lo,ng
            'timestamp': self.timestamp,
            'hash': self.hash(),
            'signature': self.signature
        }
        