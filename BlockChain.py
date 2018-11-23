import time
import json

from Block import Block

class BlockChain():

    global blockchain
    global difficulty
    global nBlocks
    blockchain = []
    difficulty = 5
    nBlocks = 3
    
    def run(self):
        
        for i in range(0, nBlocks):
            if i == 0:
                blockchain.append(Block("Hi i'm the first block", "0"))
                print("Trying to mine block 1 ...")
                blockchain[0].mineBlock(difficulty)
            else:
                blockchain.append(Block("Hi i'm the "+ str(i + 1) +" block", blockchain[len(blockchain)-1].hash_value))
                print("Trying to mine block " + str(i+1) + " ...")
                blockchain[i].mineBlock(difficulty)

        validChain = self.isChainValid()
        print("Is Valid: " + str(validChain))

        for i in range(0, len(blockchain)):
            info = json.dumps(blockchain[i].__dict__, indent=4)
            print(info)

    def isChainValid(self):
        hashTarget = "0" * difficulty

        for i in range(1, len(blockchain)):
            currentBlock = blockchain[i]
            previousBlock = blockchain[i-1]

            if (currentBlock.hash_value != currentBlock.calculateHash()):
                print("Current Hashes not Equal")
                return False
            if (previousBlock.hash_value != currentBlock.previous_hash):
                print("Previous Hashes not Equal")
                return False
            if not currentBlock.hash_value[0:difficulty] == hashTarget:
                print("This block hasn't been mined!")
                return False
        return True

start_time = time.time()
block = BlockChain()
block.run()
print("--- %s seconds ---" % (time.time() - start_time))
