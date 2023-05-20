#Propiedad asociativo escalamiento matricial
import numpy as np

# Creamos una matriz de ejemplo de 3x3 y dos escalares
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k1 = 2
k2 = 3

# Aplicamos los dos escalares sucesivamente
k1k2A = np.dot(k1*k2, A)

# Aplicamos los dos escalares simultáneamente
kkA = np.dot(k1, np.dot(k2, A))

# Comprobamos si las expresiones son iguales
if np.array_equal(k1k2A, kkA):
    print('A=',A)
    print()
    print ('K1=',k1)
    print()
    print ('K2=',k2)
    print()
    print(k1k2A==kkA)
    print("La propiedad asociativa en el escalamiento matricial se cumple")
else:
    print("La propiedad asociativa en el escalamiento matricial no se cumple")
