from network import Node
from blockchain import Blockchain
from block import Block
from certificate import Certificate

class BlockchainNode(Node):
    def __init__(self, wallet, consensusAlgorithm):
        super().__init__(wallet.publicKey)
        self.wallet = wallet
        self.consensusAlgorithm = consensusAlgorithm
        self.blockchain = Blockchain()
        self.__certificateBox = set()
        # Set pour stocker les blocs reçus trop en avance
        self.pending_blocks = set()
        #print("BlockchainNode initialized with wallet:", wallet.publicKey)

    def new_certificate(self, certificate):
        # Validation du certificat
        if not certificate.is_legit():
            return
        if certificate in self.__certificateBox:
            return
        if self.blockchain.contains_certificate(certificate):
            return
        
        # Ajout du certificat à la boîte
        self.__certificateBox.add(certificate)
        
        if len(self.__certificateBox) >= 5:
            # Création du nouveau bloc
            new_block = Block(
                self.wallet.publicKey,
                self.blockchain.get_latest_block().indexInBlockchain + 1,
                self.blockchain.get_latest_block().hash(),
                list(self.__certificateBox)
            )
            self.wallet.sign(new_block)

            if self.consensusAlgorithm.is_next_block_forger_legit(self.blockchain.blockList, new_block):
                # Ajout du bloc à la blockchain
                self.blockchain.blockList.append(new_block)
                
                # Suppression des certificats qui viennent d'être intégrés
                for cert in new_block.certificateList:
                    self.__certificateBox.discard(cert)

                # Diffusion du bloc aux autres nœuds
                self.broadcast_object(new_block)
                # Vérification des blocs en attente
                self.process_pending_blocks()
            else:
                # Si le bloc n'est pas validé, on diffuse le certificat
                self.broadcast_object(certificate)

    def new_block(self, block):
        # Validation du bloc
        if not block.is_legit():
            return
        if len(block.certificateList) < 5:
            return
        if block in self.blockchain.blockList:
            return
        
        expected_index = self.blockchain.get_latest_block().indexInBlockchain + 1

        # Si le bloc est trop en avance
        if block.indexInBlockchain > expected_index:
            # Ajout du bloc dans l'ensemble des blocs en attente
            self.pending_blocks.add(block)
            # Demande du bloc manquant (celui avec l'index attendu)
            self.broadcast_object(expected_index)
            #print(f"Block with index {block.indexInBlockchain} set aside. Requesting missing block with index {expected_index}")
            return

        # Si le bloc a un index inférieur à celui attendu, il est obsolète
        if block.indexInBlockchain < expected_index:
            return

        # À partir d'ici, block.indexInBlockchain == expected_index
        if block.parentBlockHash != self.blockchain.get_latest_block().hash():
            return
        # Vérifier que les certificats ne sont pas déjà présents dans la blockchain
        for cert in block.certificateList:
            if self.blockchain.contains_certificate(cert):
                return
        if not self.consensusAlgorithm.is_next_block_forger_legit(self.blockchain.blockList, block):
            return

        # Ajout du bloc à la blockchain
        self.blockchain.blockList.append(block)
        for cert in block.certificateList:
            self.__certificateBox.discard(cert)
        self.broadcast_object(block)
        
        # Vérification des blocs en attente
        self.process_pending_blocks()
        
    def process_pending_blocks(self):
        """
        Vérifie si l'un des blocs en attente (pending_blocks) peut être ajouté à la blockchain.
        Tant qu'il existe un bloc dont l'index correspond à (dernier index + 1), il est intégré.
        """
        added = True # Indique si un bloc a été ajouté
        while added:  
            added = False
            expected_index = self.blockchain.get_latest_block().indexInBlockchain + 1
            candidate = None
            # Parcours des blocs en attente pour trouver celui avec l'index attendu
            for pending_block in list(self.pending_blocks):
                if pending_block.indexInBlockchain == expected_index:
                    candidate = pending_block
                    break
            if candidate is None:
                break  # Aucun bloc en attente avec l'index attendu

            # Retirer le bloc de l'ensemble et vérifier son intégrité par rapport au bloc précédent
            self.pending_blocks.remove(candidate)
            if candidate.parentBlockHash != self.blockchain.get_latest_block().hash():
                # Si le hash du bloc parent ne correspond pas, on ne l'intègre pas
                continue

            # Ajout du bloc candidate à la blockchain
            self.blockchain.blockList.append(candidate)
            for cert in candidate.certificateList:
                self.__certificateBox.discard(cert)
            self.broadcast_object(candidate)
            added = True

    def receive_object_from_node(self, obj, nodeIdentifier):
        if isinstance(obj, Block):
            self.new_block(obj)
        elif isinstance(obj, Certificate):
            self.new_certificate(obj)
        elif isinstance(obj, int):
            # Un entier représente une requête pour un bloc manquant (l'index du bloc demandé)
            requested_index = obj
            if requested_index <= self.blockchain.get_latest_block().indexInBlockchain:
                block_to_send = self.blockchain.blockList[requested_index]
                self.send_object_to_node(block_to_send, nodeIdentifier)
                #print(f"Sent block with index {requested_index} to node {nodeIdentifier}")
        else:
            print("Received object of unknown type:", obj)
