from helpers import cryptography
from json import dumps, loads

class Wallet:
    
    def __init__(self):
        self.__privateKey = cryptography.generate_random_private_key() 
        self.publicKey = cryptography.get_public_key_from_private_key(self.__privateKey)  
        
    def sign(self, certificate):
        certificate.signature = cryptography.sign_hash_with_private_key(certificate.hash() , self.__privateKey)
        
    def display(self):
        return {
            'type': 'Wallet',
            'publicKey': self.publicKey,
            'privateKey': self.__privateKey
        }
