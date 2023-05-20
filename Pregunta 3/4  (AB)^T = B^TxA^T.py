#  (AB)^T = B^T*A^T

import numpy as np

# Creamos dos matrices de ejemplo de 3x3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Obtenemos el producto de las matrices A y B
AB = np.dot(A, B)

# Obtenemos la transpuesta de la matriz A
A_T = np.transpose(A)

# Obtenemos la transpuesta de la matriz B
B_T = np.transpose(B)

# Obtenemos la expresión B^T*A^T
B_T_A_T = np.dot(B_T, A_T)

# Obtenemos la transpuesta de la matriz AB
AB_T = np.transpose(AB)

# Comparamos si ambas expresiones son iguales
if np.array_equal(AB_T, B_T_A_T):
    print('A=',A)
    print()
    print ('B=',B)
    print()
    print ((AB_T== B_T_A_T))
    print("La transpuesta del producto AB es igual a B^T*A^T")
else:
    print("La transpuesta del producto AB no es igual a B^T*A^T")
