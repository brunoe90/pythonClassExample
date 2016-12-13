'''
Created on 13/12/2016

@author: Bruno
'''
from com.misclases.Padre import Padre

class Hijo(Padre):
        
    def imprimir_hijo(self):
        print("\nEntre al metodo imprimir del Hijo\n")
        print("Variable creada en el Padre:",self.a,"\n")
        print("Variable creada en el Padre:",self.b,"\n")   
            
    def __del__(self):
        print("Me Destruyeron, soy el Hijo\n")         