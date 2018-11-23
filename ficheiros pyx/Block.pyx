# -*- coding: utf-8 -*-

import time
import json
import hashlib
import json

#Block Class
class Block(object):

    '''
    Class Constructor
    @param index - index of the block
    @param previous_hash - hash of previous block
    @param name - name of the person that will receive
    @param id_person - id of the person that will receive
    @param course - course of the person that will receive
    @param degree - degree of the person that will receive
    @param institute - institute of the person that will receive
    @param keyCreator - PublicKey of the block creator
    @param keyReceiver - PublicKey of the person that will receive
    '''
    def __init__(self, int index, str previous_hash, str name, str id_person, str course, str degree, str institute, str keyCreator, str keyReceiver):
        self.index = index
        self.creator = "Ricardo Lucas"
        self.keyCreator = keyCreator
        self.name = name
        self.id_person = id_person
        self.course = course
        self.degree = degree
        self.institute = institute
        self.keyReceiver = keyReceiver
        self.previous_hash = previous_hash
        self.time_stamp = time.time()
        self.nonce = 0
        self.hash_value = self.calculateHash() 

    '''
    In this method will be applyed sha256 to the input, returning a digital signature
    @param input - String that will be applyed sha256
    @return sha_signature - digital signature
    '''
    def applySha(self, str input):
        cdef str sha_signature = hashlib.sha256(input.encode()).hexdigest()
        return sha_signature

    '''
    This method will return calculated hash
    @return calculated_hash - digital signature
    '''
    def calculateHash(self):
        cdef str calculated_hash = self.applySha(self.previous_hash+str(self.time_stamp)+str(self.nonce)+str(self.index)+self.creator+self.name+str(self.id_person)+self.course+self.degree+self.institute+str(self.keyCreator)+str(self.keyReceiver))
        return calculated_hash
    
    '''
    In this method the block is going to be mined, the block only going to be mined if the signature has enough 0 conform difficulty, if not, i will be repeated until the 
    signature be valid, for each time that it fails increments nonce that it how many times was the hash was created. 
    @param difficulty - Int that represents how many 0 the hash will have
    '''
    def mineBlock(self, int difficulty):
        cdef str target = "0" * difficulty
        while not self.hash_value[0:difficulty] == target:
            self.nonce += 1
            self.hash_value = self.calculateHash()
        #print("Block mined!!! : " + self.hash_value)