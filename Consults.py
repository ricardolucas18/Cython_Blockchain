from Database import Database
import time

'''
Class Consults
'''
__author__ = "Ricardo Lucas"
__license__= ""
__version__= "1.0"
__maintainer__= "Ricardo Lucas"
__status__= "Development"

class Consults():

    def consult(self):
        conn = Database.create_connection()

        #Creates indexes
        create_index = Database.create_indexes(self, conn)

        #Consults how many persons frequent Engenharia Informática
        course_ei = Database.search_course_ei(self, conn)

        #Consults how many persons frequent Turismo
        course_tur = Database.search_course_tur(self, conn)

        #Consults how many persons frequent Engenharia Solicitadoria
        course_sol = Database.search_course_sol(self, conn)

        #Consults how many persons frequent Enfermagem
        course_enf = Database.search_course_enf(self, conn)

        #Consults how many persons has name starting with specific letter
        persons_letter = Database.search_person_letter(self, conn)

        #Consults how many persons have a specific number on id
        persons_id = Database.search_person_id(self, conn)

        #Consults how many hash have eda on the hash
        hash_eda = Database.search_hash_eda(self, conn)

        #Consults how many hash have eda on the previousHash
        previousHash_ei = Database.search_previousHash_eda(self, conn)
        '''
        print("\nPessoas com o curso de Engenharia Informática:\n")
        for i in course_ei:
            print(i)
		
        print("\nPessoas com o curso de Turismo:\n")
        for i in course_tur:
            print(i)
			
        print("\nPessoas com o curso de Solicitadoria:\n")
        for i in course_sol:
            print(i)
		
        print("\nPessoas com o curso de Enfermagem:\n")
        for i in course_enf:
            print(i)
			
        
        print("\nPessoas com eda:\n")
        for i in previousHash_ei:
            print(i)
        '''        
start_time = time.time()
for i in range(1000):
    #print(i)
    consults = Consults()
    consults.consult()

execution_time = time.time() - start_time
print("Consults Execution Time: "+str(execution_time) +"seconds")