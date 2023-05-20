#(kA)^T = k(A^T)
import numpy as np

# Creamos una matriz de ejemplo de 3x3 y un escalar
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 2

# Obtenemos la matriz escalar k multiplicada por la matriz A
kA = np.dot(k, A)

# Obtenemos la transpuesta de la matriz A
A_T = np.transpose(A)

# Obtenemos la matriz escalar k multiplicada por la transpuesta de A
kA_T = np.dot(k, A_T)

# Obtenemos la transpuesta de la matriz escalar k multiplicada por A
kA_T_T = np.transpose(kA)

# Comprobamos si las expresiones son iguales
if np.array_equal(kA_T_T, kA_T):
    print('A=',A)
    print()
    print ('K=',k)
    print()
    print (kA_T_T==kA_T)
    print("La transpuesta de kA es igual a k por la transpuesta de A")
else:
    print("La transpuesta de kA no es igual a k por la transpuesta de A")


