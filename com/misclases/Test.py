'''
Created on 13/12/2016

@author: Bruno
'''
from com.misclases.Hijo import Hijo
from com.misclases.Padre import Padre

p = Padre("PADRE")
h = Hijo("HIJO")

p.imprimir("\nMetodo Imprimir de la clase Padre\n");
p.suma(8,8);

h.imprimir("\nSoy el hijo usando el metodo de imprimir de la clase Padre\n")
h.suma(4,4)
h.imprimir_hijo()
