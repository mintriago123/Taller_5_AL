# -*- coding: utf-8 -*-

import numpy as np

# Creamos tres matrices de ejemplo de 3x3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 1]])
C = np.array([[3, 4, 5], [6, 7, 8], [9, 1, 2]])

# Primero, calculamos la suma de A y B
AB = np.add(A, B)

# Luego, calculamos el producto matricial de AB y C
ABC1 = np.dot(AB, C)

# Después, calculamos el producto matricial de A y C
AC = np.dot(A, C)

# También, calculamos el producto matricial de B y C
BC = np.dot(B, C)

# Finalmente, sumamos AC y BC
ABC2 = np.add(AC, BC)

# Comprobamos si las expresiones son iguales
if np.array_equal(ABC1, ABC2):
    print('A=',A)
    print()
    print ('B=',B)
    print()
    print ('C=',C)
    print()
    print (ABC1==ABC2)
    print("La propiedad distributiva por la derecha del producto matricial se cumple")
else:
    print (ABC1==ABC2)
    print("La propiedad distributiva por la derecha del producto matricial no se cumple")
