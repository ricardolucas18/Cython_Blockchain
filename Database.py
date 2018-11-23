# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error

'''
Class Database
'''
__author__ = "Ricardo Lucas"
__license__= ""
__version__= "1.0"
__maintainer__= "Ricardo Lucas"
__status__= "Development"

class Database:
    
    #Create a connection to Database People
    def create_connection():
        try:
            conn = sqlite3.connect("People.db")
            return conn
        except Error as e:
            print(e)
    
        return None

    '''
    In this method it will be select all persons that are in People table and returns the number of people after we use fetchall
    @param conn - Databse connection
    @return rows - people to create blocks
    '''
    def select_all(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM People")
    
        rows = cur.fetchall()

        conn.close()

        return rows

    '''
    In this method it will be select all persons that frequent engenharia informática in blockchain table
    @param conn - Databse connection
    @return rows - people that frequents engenharia informática
    '''
    def search_course_ei(self, conn):

        cur = conn.cursor()
                
        cur.execute("""SELECT namePersonReceiver, id_person, institute FROM blockChain WHERE course = 'Engenharia Informática'""")

        rows = cur.fetchall()

        return rows

    '''
    In this method it will be select all persons that frequent Turismo in blockchain table
    @param conn - Databse connection
    @return rows - people that frequents Turismo
    '''
    def search_course_tur(self, conn):

        cur = conn.cursor()
                
        cur.execute("""SELECT namePersonReceiver, id_person, institute FROM blockChain WHERE course = 'Turismo'""")

        rows = cur.fetchall()

        return rows

    '''
    In this method it will be select all persons that frequent Solicitadoria in blockchain table
    @param conn - Databse connection
    @return rows - people that frequents Solicitadoria
    '''
    def search_course_sol(self, conn):

        cur = conn.cursor()
                
        cur.execute("""SELECT namePersonReceiver, id_person, institute FROM blockChain WHERE course = 'Solicitadoria'""")

        rows = cur.fetchall()

        return rows

    '''
    In this method it will be select all persons that frequent Enfermagem in blockchain table
    @param conn - Databse connection
    @return rows - people that frequents Enfermagem
    '''
    def search_course_enf(self, conn):

        cur = conn.cursor()
                
        cur.execute("""SELECT namePersonReceiver, id_person, institute, course FROM blockChain WHERE course = 'Enfermagem'""")

        rows = cur.fetchall()

        return rows

    '''
    In this method it will be select all persons that witch their names start with letter R
    @param conn - Databse connection
    @return rows - people that their name starts with R
    '''
    def search_person_letter(self, conn):

        cur = conn.cursor()
                
        cur.execute("""SELECT namePersonReceiver, id_person, institute FROM blockChain WHERE namePersonReceiver LIKE 'R%'""")

        rows = cur.fetchall()

        return rows
    
    '''
    In this method it will be select all persons id that have 123 in the middle of their id
    @param conn - Databse connection
    @return rows - people that have 123 in the midle of their id
    '''
    def search_person_id(self, conn):

        cur = conn.cursor()
                
        cur.execute("""SELECT namePersonReceiver, id_person, institute FROM blockChain WHERE id_person LIKE '%123%'""")

        rows = cur.fetchall()

        return rows

    '''
    In this method it will be select all hashes that have eda in the middle of their hash
    @param conn - Databse connection
    @return rows - hashes that have eda
    '''
    def search_hash_eda(self, conn):

        cur = conn.cursor()
                
        cur.execute("""SELECT namePersonReceiver, id_person, institute, blockHash FROM blockChain WHERE blockHash LIKE '%eda%'""")

        rows = cur.fetchall()

        return rows

    '''
    In this method it will be select all previoushashes that have eda in the middle of their hash
    @param conn - Databse connection
    @return rows - previoushashes that have eda
    '''
    def search_previousHash_eda(self, conn):

        cur = conn.cursor()
                
        cur.execute("""SELECT previousBlockHash FROM blockChain WHERE previousBlockHash LIKE '%eda%'""")

        rows = cur.fetchall()

        return rows

    '''
    In this method it will create indexes to get best performance
    @param conn - Databse connection
    '''
    def create_indexes(self, conn):

        cur = conn.cursor()
                
        cur.execute("""CREATE INDEX IF NOT EXISTS idx_course ON blockChain (course)""")
        cur.execute("""CREATE INDEX IF NOT EXISTS idx_name ON blockChain (namePersonReceiver)""")
        cur.execute("""CREATE  INDEX IF NOT EXISTS idx_person_id ON blockChain (id_person)""")
        cur.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_person_id ON blockChain (blockHash)""")
        cur.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_person_id ON blockChain (previousBlockHash)""")


    