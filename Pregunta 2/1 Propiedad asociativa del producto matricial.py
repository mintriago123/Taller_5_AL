#demuestra la propiedad asociativa del producto matricial
import numpy as np

# Creamos tres matrices cuadradas de 3x3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 1]])
C = np.array([[3, 4, 5], [6, 7, 8], [9, 1, 2]])

# Primero, calculamos el producto matricial de B y C
BC = np.dot(B, C)

# Luego, calculamos el producto matricial de A y BC
ABC = np.dot(A, BC)

# Ahora, calculamos el producto matricial de A y B
AB = np.dot(A, B)

# Finalmente, calculamos el producto matricial de AB y C
ABC_2 = np.dot(AB, C)

# Comprobamos si las expresiones son iguales
if np.array_equal(ABC, ABC_2):
    print('A=',A)
    print()
    print ('B=',B)
    print()
    print ('C=',C)
    print()
    print(ABC == ABC_2)
    print("La propiedad asociativa del producto matricial se cumple")
else:
    print (ABC1==ABC2)
    print("La propiedad asociativa del producto matricial no se cumple")
