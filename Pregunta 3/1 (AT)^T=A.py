# (AT)^T=A

import numpy as np

# Creamos una matriz de ejemplo de 3x3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Obtenemos la transpuesta de la matriz A
A_T = np.transpose(A)

# Obtener la transpuesta de la matriz A_T
A_T_T = np.transpose(A_T)

# Comprobamos si la matriz original A es igual a A_T_T
if np.array_equal(A, A_T_T):
    print('A=',A)
    print()
    print(A == A_T_T);
    print("La transpuesta de la transpuesta de A es igual a A")
else:
    print("La transpuesta de la transpuesta de A no es igual a A")
