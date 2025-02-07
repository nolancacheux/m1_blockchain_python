

class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def solve_puzzle(self, block):
        begin = '0' * self.difficulty
        while not block.hash().startswith(begin):
            block.nonce += 1

    def is_next_block_forger_legit(self, blockList, nextBlock):
        begin = '0' * self.difficulty
        for block in blockList:
            if block.hash().startswith(begin):
                return True
        return nextBlock.hash().startswith(begin)

    def is_blockchain_legit(self, blockchain):
        for i in range(1, len(blockchain.blockList)):  # 1 because the first block is forged by the black hole
            if not self.is_next_block_forger_legit(blockchain.blockList[:i], blockchain.blockList[i]):
                #(blockchain.blockList[:i], blockchain.blockList[i]) because we want to check if the next block is legit 
                #so we need to check if the block before it is legit
                # (blockchain.blockList[:i] is the list of blocks before the next block)
                # (blockchain.blockList[i] is the next block)
                return False
        return True
