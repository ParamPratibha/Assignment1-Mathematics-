import numpy as np  
import csv
matrix=open("matrix.csv")
A=np.loadtxt(matrix, dtype='int', delimiter=',')
#exponential function
print("\n Exponential Value:")
print(np.exp(A))

#sine function
print("\n Sine Value:")
print(np.sin(A * np.pi / 180))

#Sigmoid function
print("\n Sigmoid Value:")
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

print(sigmoid(A))
