import gnupg
import time
import shutil
import os

from Database import Database
'''
Class GPGKeys
'''
__author__ = "Ricardo Lucas"
__license__= ""
__version__= "1.0"
__maintainer__= "Ricardo Lucas"
__status__= "Development"

class GPGKeys:
    def generateKeysDB(self, startRange):
        '''
        This if will check the OS where Application is being executed
        nt = Windows
        posix = Linux
        '''
        if os.name == 'nt':
            gpg = gnupg.GPG(gnupghome='keysDB', gpgbinary='C:\\Program Files (x86)\\gnupg\\bin\\gpg.exe')
        elif os.name =='posix':
            gpg = gnupg.GPG(gnupghome='./KeysDB', gpgbinary="/usr/bin/gpg")

        rows = self.dbConnection()

        print("Generating Keys ...")
        #Generate key - Default RSA 1024 bits
        for x in range(startRange, len(rows)):
            input_data = gpg.gen_key_input( name_real=rows[x][1], passphrase=rows[x][2])
            key = gpg.gen_key(input_data)

        #List keys with all data - WARNING IT'S A LOT OF DATA
        list_keysDB = gpg.list_keys() # Public keys
        #list_priv_keys = gpg.list_keys(True) -> Private Keys

        print ("All keys have been Generated!")
        return list_keysDB

    def listAllKeys(self):
        '''
        This if will check the OS where Application is being executed
        nt = Windows
        posix = Linux
        '''
        if os.name == 'nt':
            gpg = gnupg.GPG(gnupghome='keysDB', gpgbinary='C:\\Program Files (x86)\\gnupg\\bin\\gpg.exe')
        elif os.name =='posix':
            gpg = gnupg.GPG(gnupghome='./KeysDB', gpgbinary="/usr/bin/gpg")

        list_keysDB = gpg.list_keys() # Public keys
        #list_priv_keys = gpg.list_keys(True) -> Private Keys

        return list_keysDB

    
    def generateKeysInput(self):
        '''
        This if will check the OS where Application is being executed
        nt = Windows
        posix = Linux
        '''
        if os.name == 'nt':
            gpg = gnupg.GPG(gnupghome='keysDB', gpgbinary='C:\\Program Files (x86)\\gnupg\\bin\\gpg.exe')
        elif os.name =='posix':
            gpg = gnupg.GPG(gnupghome='./KeysDB', gpgbinary="/usr/bin/gpg")

        dir_path = os.path.dirname(os.path.realpath(__file__))
        # Delete creator public key directory
        if os.path.isdir(dir_path + "\\keysCreator"):
            shutil.rmtree(dir_path + "\\keysCreator")


        print("Generating Creator Key ...")
        input_data = gpg.gen_key_input( name_real = "Ricardo Lucas", passphrase = "12345")
        key = gpg.gen_key(input_data)

        list_keysCreator = gpg.list_keys()
        #print ("Key Generated!")
        return list_keysCreator

    def dbConnection(self):
        # create a database connection
        conn = Database.create_connection()

        rows = Database.select_all(conn)

        return rows