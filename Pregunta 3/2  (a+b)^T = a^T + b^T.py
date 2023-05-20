#(a+b)^T = a^T + b^T
import numpy as np

# Creamos dos matrices de ejemplo de 3x3
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

# Obtenemos la suma de las matrices a y b
ab = np.add(a, b)

# Obtenemos las transpuestas de las matrices a y b
a_T = np.transpose(a)
b_T = np.transpose(b)

# Obtenemos la suma de las transpuestas de las matrices a y b
a_T_b_T = np.add(a_T, b_T)

# Obtenemos la transpuesta de la suma de las matrices a y b
ab_T = np.transpose(ab)

# Comprobamos si las expresiones son iguales
if np.array_equal(ab_T, a_T_b_T):
    print('A=',a)
    print()
    print ('B=',b)
    print()
    print (ab_T==a_T_b_T)
    print("La transpuesta de la suma de a y b es igual a la suma de las transpuestas de a y b")
else:
    print("La transpuesta de la suma de a y b no es igual a la suma de las transpuestas de a y b")

