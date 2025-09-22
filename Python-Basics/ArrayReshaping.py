#To reshape a numpy array, we make use of the reshape() function
#Reshaping can help us in changing the dimensions of an array
#We can increase the dimensions/decrease the dimensions(Flattening)

#Reshaping an one dimensional array to a 2d array
import numpy as np
nbasearray = np.array([1,2,3,4,5,6])
print(nbasearray)
nreshapedarray = nbasearray.reshape(3,2)
print(nreshapedarray)

#Flattening
nbase3darray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(nbase3darray)
nres3array = nbase3darray.reshape(-1)
print(nres3array)

print(nbase3darray.shape)
nresultexarray = nbase3darray.reshape(2,3,2)
print(nresultexarray)