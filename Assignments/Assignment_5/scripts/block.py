from certificate import Certificate

class Block(Certificate):
       def __init__(self, issuerPublicKey, indexInBlockchain, parentBlockHash, certificateList):
              super().__init__(issuerPublicKey)  
              self.indexInBlockchain = indexInBlockchain
              self.parentBlockHash = parentBlockHash
              self.certificateList = certificateList
              self.nonce = 0  # on initialise nonce to 0

       def build_payload(self):
              payload = super().build_payload()
              payload.update({
                     'indexInBlockchain': self.indexInBlockchain,
                     'parentBlockHash': self.parentBlockHash,
                     'certificateList': [cert.build_payload() for cert in self.certificateList],
                     'nonce': self.nonce  # on inclut le nonce in the payload
              })
              return payload
       
       def is_legit(self):
              # not legit si le certificat du block 'n'est pas légitime
              if not super().is_legit():
                     return False
              
              # not legit si l'index du block dans la blockchain n'est pas un entier positif
              if not isinstance(self.indexInBlockchain, int) or self.indexInBlockchain < 0:
                     return False
              
              # not legit si le hash du bloc parent n'est pas une chaîne de 64 caractères hexadécimaux
              if not isinstance(self.parentBlockHash, str) or len(self.parentBlockHash) != 64:
                     return False
              
              # not legti si la liste des certificats n'est pas légitime
              for cert in self.certificateList:
                     if not cert.is_legit():
                            return False
              
              return True
       
       def display(self):    
              result = super().display()  
              result.update({
                     'index': self.indexInBlockchain,
                     'parent': self.parentBlockHash,
                     'certificates': [cert.display() for cert in self.certificateList],
                     'nonce': self.nonce  # Include nonce in the display
              })
              return result
