#Propiedad distributiva por la izquierda del producto matricial en py
import numpy as np
# Como ejemplo, creamos tres matrices de 3x3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 1]])
C = np.array([[3, 4, 5], [6, 7, 8], [9, 1, 2]])

# Primero, calculamos el producto matricial de B y C
BC = np.add(B, C)

# Luego, calculamos el producto matricial de A y BC
ABC1 = np.dot(A, BC)

# Después, calculamos el producto matricial de A y B
AB = np.dot(A, B)

# También, calculamos el producto matricial de A y C
AC = np.dot(A, C)

# Finalmente, sumamos los productos A * B y A * C
ABC2 = np.add(AB, AC)

# Comprobamos si las expresiones son iguales
if np.array_equal(ABC1, ABC2):
    print('A=',A)
    print()
    print ('B=',B)
    print()
    print ('C=',C)
    print()
    print(ABC1==ABC2)
    print("La propiedad distributiva por la izquierda del producto matricial se cumple")
else:
    print (ABC1==ABC2)
    print("La propiedad distributiva por la izquierda del producto matricial no se cumple")
