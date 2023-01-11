import numpy as np
import csv
#Read matrix A from csv file
matrix=open("matrix.csv")
A=np.loadtxt(matrix, dtype='int', delimiter=',')
print("Read matrix from csv file is shown below: \n")
print(A)

#Read Vector b from csv
print("\n")
print("Read vector from csv file is shown below: \n")
vector=open("vector b.csv")
b=np.loadtxt(vector, dtype='int', delimiter=',')
print(b)
