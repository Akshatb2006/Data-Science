# To split numpy array we make use of the numpy.array_split() method

# Splitting a 1D array
import numpy as np

n1 = np.array([1,2,3,4,5,6])

resarray = np.array_split(n1,2)
print(resarray)

# Accessing the splitted arrays
# make use of the indexes

import numpy as np

n1 = np.array([1,2,3,4,5,6])

resarray = np.array_split(n1,2)
print(resarray)

print("\n\n",resarray[0])
print(resarray[0])
print(type(resarray))

n3 = np.array([[1,2,3],[4,5,6]])

# Splitting a 2D array

n3 = np.array([[1,2,3],[4,5,6]])
res2darray = np.array_split(n3,3)
print(res2darray)