import numpy as np
from numpy.linalg import eig
matrix=open("matrix.csv")
A=np.loadtxt(matrix, dtype='int', delimiter=',')
EigenValues,EigenVector=eig(A)
print("\n Eigen-value: \n", EigenValues)
print("\n E-vector \n", EigenVector)
