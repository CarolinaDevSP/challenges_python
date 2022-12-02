
#1) leer el quickstart de ambas documentaciones
    # https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    # https://numpy.org/doc/stable/user/quickstart.html
#2) con Numpy hacer dos matrices de 2 x 2 (rellenar la matriz)

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
"""
a = np.ones([2,2])
print(a)
b= np.ones([2,2])*2
print(b)"""

#X = np.array([[2,3], [6,2]])
X= np.random.randint(50, size=(2, 2))
print(X)
#Y = np.array([[4,5], [2,1]])
Y= np.random.randint(50, size=(2, 2))
print(Y)

#3) Aplicar la suma, multiplicacion, resta y division entre ambas matrices
print('------------suma------------------')
suma=print(X+Y)
print('------------resta------------------')
mult=print(X*Y)
print('------------mult------------------')
resta=print(X-Y)
print('------------div------------------')
div=print(X/Y)

#guardar los resultados
#impimir o graficar los resultados
plt.plot(X,Y, 'ro') 
plt.axis([0,100,0,100]) 
plt.show()