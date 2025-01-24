from helpers import cryptography
from block import Block

class Blockchain:
    def genesis_block():
        genesis = Block(cryptography.get_black_hole_public_key(), 0, cryptography.get_default_hash(), [])
        #certificateAlice1.timestamp -= 1
        # assert not blockchain.is_legit()
        genesis.timestamp=0
        return genesis
    
    def __init__(self):
        self.blockList = [Blockchain.genesis_block()]
    
    def get_latest_block(self):
        return self.blockList[-1]
    
    def is_legit(self):
        # not legit si le premier bloc n'est pas le bloc genesis
        if not self.blockList[0].equals(Blockchain.genesis_block()):
            return False
        # not legit si un des blocs n'est pas légitime
        for i in range(1, len(self.blockList)):
            
            if (
                # vérifie que l'index du bloc actuel (self.blockList[i].indexInBlockchain) est 
                # bien le suivant de l'index du bloc précédent (self.blockList[i - 1].indexInBlockchain + 1)
                self.blockList[i].indexInBlockchain != self.blockList[i - 1].indexInBlockchain + 1 
                or 
                #vérifie que le hash du bloc parent (self.blockList[i].parentBlockHash) 
                # correspond bien au hash du bloc précédent (self.blockList[i - 1].hash()
                self.blockList[i].parentBlockHash != self.blockList[i - 1].hash()
                or
                #vérifie si le bloc actuel est légitime
                not self.blockList[i].is_legit()
                ):
                return False
        return True


    def display(self):
        for i, block in enumerate(self.blockList) : print( '\n'.join([f"Block {i}:\n{block.display()}"]))
