narr = np.array([1,2,3,4,5,6])
#Numpy Arrays do maintain positive and negative indexes

#Indexing in 1D array
print(narr[-2])
print(narr[1])

#Indexing in 2D array
n2darray = np.array([[1,2,3],[2,3,4]])
print(n2darray)
print(n2darray[0][0]) #first [] denotes indexed row and second [] denotes indexed column
print(n2darray[0][1])
print(n2darray[0][2])
print(n2darray[1][0])
print(n2darray[1][1])
print(n2darray[1][2])

# Indexing in 3D array
n3darray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,5,6]]])
print(n3darray)

print(n3darray[0][0][0])
print(n3darray[0][0][1])
print(n3darray[0][0][2])
print(n3darray[0][1][0])
print(n3darray[0][1][1])
print(n3darray[0][1][2])
print(n3darray[1][0][0])
print(n3darray[1][0][1])
print(n3darray[1][0][2])
print(n3darray[1][0][2])
print(n3darray[1][0][2])
print(n3darray[1][0][2])

#numpy arrays also follow negative indexes like normal arrays or strings
import numpy as np

n3darray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(n3darray)
print(n3darray[-1][-2][-2])