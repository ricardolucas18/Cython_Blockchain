# -*- coding: utf-8 -*-
import time
from BlockChain import BlockChain

#Starts time
start_time = time.time()

#Creates a object blockchain giving a difficulty
runBlockchain = BlockChain(2)

#Call createBlockChain method to create the blockchain
full_blockchain = runBlockchain.createBlockChain()

#Application Execution time
ApplicationTime = (time.time() - start_time)
print("Aplication Duration --- %s seconds ---" % (time.time() - start_time))

#Creates a file to write the Application execution time
aplication_time_file = open('keystimes.txt', 'w')
aplication_time_file.write(str(ApplicationTime))
aplication_time_file.close()