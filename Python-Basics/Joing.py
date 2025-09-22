#To join 2 numpy arrays we make use of the concatenate() method

import numpy as np

n = np.array([1,2,3,4])
p = np.array([5,6,7,8])

resarray = np.concatenate((n,p))

print(resarray)

#Addition of arrays through Stack

# stack()
# vstack()
# hstack()
# dstack() - 3D array (height wise)
# column_stack() - 2D array

# Using stack()

n1 = np.array([1,2,3,4,5])
n2 = np.array([5,6,7,8,9])

n3 = np.array([[1,2,3],[4,5,6]])
n4 = np.array([["a","b","c"],["d","e","f"]])

resultant_array = np.stack((n1,n2)) # the default axis is 0 which stacking row-wise
resultant2array = np.stack((n1,n2),axis = 0)
print("\n",resultant_array)
print("\n",resultant2array)
print(resultant_array.shape)
print(resultant2array.shape)

# Stacking using vstack()
resultantvarray = np.vstack((n1,n2))
print("\n\n", resultantvarray)
print(type(resultantvarray))

# Stacking using hstack()
resultantharray = np.hstack((n1,n2))
print("\n\n",resultantharray)


# Stacking of 2D arrays - return a 2D array itself.
# Stacking using dstack()
resultdarray = np.dstack((n3,n4))
print("\n\n",resultdarray)
print(resultdarray.shape)

# Stacking using column_stack()
resultcolumn_array = np.column_stack((n3,n4))
print("\n\n", resultcolumn_array)
print(resultcolumn_array.shape)

