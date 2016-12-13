'''
Created on 13/12/2016

@author: Bruno
'''

class Padre(object):

    def __init__(self,nameClass):
        print("CONSTRUCTOR DEL",nameClass)
        self.a = 6;
        self.b = 6;
        
    def imprimir(self,nameClass):
        print (nameClass);   
        
    def suma(self,a,b):
        c = a + b;
        print ("Esta es la suma de variables ingresadas por parametro",c)       
        c = self.a + self.b;
        print ("Esta es la suma de variables creadas en la clase",c)
        
    def __del__(self):
        print("Me Destruyeron, Soy el Padre\n")             