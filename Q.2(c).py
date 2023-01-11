import numpy as np
import csv
matrix=open("matrix.csv")
A=np.loadtxt(matrix, dtype='int', delimiter=',')
vector=open("vector b.csv")
b=np.loadtxt(vector, dtype='int', delimiter=',')
result=np.linalg.solve(A,b)
print("\n result= ")
print(result)

