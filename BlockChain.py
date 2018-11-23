# -*- coding: utf-8 -*-
import time
import json
import getpass

from Block import Block
from Database import Database
from GPGKeys import GPGKeys


'''
Class BlockChain
'''
__author__ = "Ricardo Lucas"
__license__= ""
__version__= "1.0"
__maintainer__= "Ricardo Lucas"
__status__= "Development"

class BlockChain():
    '''
    Class Constructor
    @param difficulty - index of the block
    '''
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blockchain = []

    '''
    In this method it will be created the blockchain, creating the public keys, adding the blocks to the chain with the database information and then the blocks are mined, after all that check
    checks if the chain is valid and it writes in a file the execution times of each block
    @return blockchain - returns the blockchain
    '''
    def createBlockChain(self):

        nBlocks = 100

        rows = self.dbConnection()
        blockstimes=[]
        keyDB = GPGKeys.listAllKeys(self)

        if (len(keyDB) < len(rows)):
            keyDB = GPGKeys.generateKeysDB(self, len(keyDB))
        
        keyCreator = GPGKeys.generateKeysInput(self)
        for i in range(0, nBlocks):
            if i == 0:
                self.blockchain.append(Block((i + 1), "0", rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], keyCreator[i]['fingerprint'], keyDB[i]['fingerprint']))
                print("Trying to mine block 1 ...")
                start_time = time.time()
                self.blockchain[0].mineBlock(self.difficulty)
                block_time = time.time() - start_time
                blockstimes.append(block_time)
                print(str(block_time) +"seconds")

            else:
                self.blockchain.append(Block(
                    (i + 1), self.blockchain[len(self.blockchain)-1].hash_value, rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], keyCreator[0]['fingerprint'], keyDB[i]['fingerprint']))
                print("Trying to mine block " + str(i+1) + " ...")
                start_time = time.time()
                self.blockchain[i].mineBlock(self.difficulty)
                block_time = time.time() - start_time
                blockstimes.append(block_time)
                print(str(block_time) +"seconds")

        validChain = self.isChainValid()
        print("Chain is Valid: " + str(validChain))
        '''
        #Apresenta a Blockchain Bloco a bloco usando o formato Json
        for i in range(0, len(self.blockchain)):
            info = json.dumps(self.blockchain[i].__dict__, indent=4, ensure_ascii=False)
            print(info)
        '''
        block_time_file = open('blocksTimes.txt', 'w')
        for times in blockstimes:
            block_time_file.write("%s\n" % times)

        block_time_file.close()
        
        tableBlocksCreation = self.tableCreation()

        return self.blockchain

    '''
    Checks if chain is valid
    @return true or false - returns true if chain is valid and false if chain is invalid
    '''
    def isChainValid(self):
        hashTarget = "0" * self.difficulty

        for i in range(1, len(self.blockchain)):
            currentBlock = self.blockchain[i]
            previousBlock = self.blockchain[i-1]

            if (currentBlock.hash_value != currentBlock.calculateHash()):
                print("Current Hashes not Equal")
                return False
            if (previousBlock.hash_value != currentBlock.previous_hash):
                print("Previous Hashes not Equal")
                return False
            if not currentBlock.hash_value[0:self.difficulty] == hashTarget:
                print("This block hasn't been mined!")
                return False
        return True
    
    '''
    Database Connection
    @return rows - returns rows that are all the people to create blocks in this case
    '''
    def dbConnection(self):
        # create a database connection
        conn = Database.create_connection()

        rows = Database.select_all(conn)

        return rows

    '''
    Blockchain Table creation and inserts
    '''
    def tableCreation(self):
        conn = Database.create_connection()
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS blockChain (id integer PRIMARY KEY, id_index integer NOT NULL, creatorName text NOT NULL, keyCreator text NOT NULL, namePersonReceiver text NOT NULL, id_person integer NOT NULL, course text NOT NULL, degree text NOT NULL, institute text NOT NULL, keyReceiver text NOT NULL, previousBlockHash text NOT NULL, timestamp double NOT NULL, nonce integer NOT NULL, blockHash integer NOT NULL)')
        for i in range(0, len(self.blockchain)):
            c.execute("INSERT INTO blockChain (id_index, creatorName, keyCreator, namePersonReceiver, id_person, course, degree, institute, keyReceiver, previousBlockHash, timestamp, nonce, blockHash) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (self.blockchain[i].index, self.blockchain[i].creator, self.blockchain[i].keyCreator, self.blockchain[i].name, self.blockchain[i].id_person, self.blockchain[i].course, self.blockchain[i].degree, self.blockchain[i].institute, self.blockchain[i].keyReceiver, self.blockchain[i].previous_hash, self.blockchain[i].time_stamp, self.blockchain[i].nonce, self.blockchain[i].hash_value))
        conn.commit()
        c.close()
        conn.close()  


