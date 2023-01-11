# Implementation for Diagonalization of a Square Matrix (assuming that matrix is symmetric):
import numpy as np     
print("Implementation for Diagonalization of a Square Matrix")
A=np.array([[1,0,-1],[1,2,1],[2,2,3]])
print(A)

from numpy.linalg import eig
eigen =eig(A)

D= np.diag(eigen[0]) # diagonalisation of A from its eigen values
print("Diagonal form 'D' of Input Matrix 'A' is:")
print(D)
