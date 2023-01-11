import numpy as np
import scipy.linalg as lg
import csv
matrix=open("matrix.csv")
A=np.loadtxt(matrix, dtype='int', delimiter=',')
P, L, U=lg.lu(A)
print(" \n Lower Traingle:\n",L)
print(" \n Upper Traingle:\n",U)

decomposition=P.dot((L.dot(U)))
print("\n After LU decomposition, Original matrix is given below: \n", decomposition)
