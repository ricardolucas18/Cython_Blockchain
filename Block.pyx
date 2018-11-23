import datetime
from StringUtil import StringUtil
import json
import hashlib
import json


cdef class Block(object):
    cdef int data
    cdef char previous_hash
    cdef char hash_value
    cdef int nonce

    def __init__(self, int data, char previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.time_stamp = str(datetime.datetime.now())
        self.nonce = 0
        self.hash_value = self.calculateHash() 
    
    cdef char calculateHash(self):
        cdef char calculated_hash = StringUtil.applySha(self.previous_hash+str(self.time_stamp)+str(self.nonce)+self.data)
        return calculated_hash
    
    cdef mineBlock(self, int difficulty):
        target = "0" * difficulty
        while not self.hash_value[0:difficulty] == target:
            self.nonce += 1
            self.hash_value = self.calculateHash()
        print("Block mined!!! : " + self.hash_value)
    