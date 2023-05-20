#Donde k es un escalar y A, B y C son matrices de un tamaño tal que permite la operación. 
import numpy as np

# Creamos una matriz de ejemplo de 3x3 y dos escalares
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
C = np.array([[3, 6, 9], [12, 15, 18], [21, 24, 27]])
k = 2

# Aplicamos el escalar a cada matriz sucesivamente
kAB = np.dot(k, np.dot(A, B))
kABC = np.dot(k, np.dot(np.dot(A, B), C))
ABC = np.dot(np.dot(A, B), C)
k_BC = np.dot(np.dot(k, B), C)



    print ('A=',A)
    print ()
    print ('B=',B)
    print ()
    print ('C=',C)
    print ()
    print ('K=',k)
    print ()
    print ("La propiedad asociativa en el escalamiento matricial se cumple con matrices de tamaño 3x3");