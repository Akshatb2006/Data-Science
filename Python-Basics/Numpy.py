# Numpy stands for numerical python
# Numpy works with multi-dimensional arrays
# This is an open-source pythoon library which is built on python and c
# The kinds of operations on arrays numpy supports are:
## Array innitialization
## Array Slicing
## Array Reshaping
## Supports zero,one and two(matrix) dimensional arrays
## Array join
## Array Split

import numpy as np

#FUnction to create numpy arrays - numpy.arrays()
#Two ways to create numpy arrays - 1. Passing a List,   2. Passing a Tuple

#1. Passing a Tuple
npobj = np.array((1,2,3))
print(npobj)
print(type(npobj))

#2. Passing a List
npobj1 = np.array([1,2,3,4])
print(npobj1)
print(type(npobj))

#Dimensions of a Numpy array
# The dimensions of an ndarray are also known as 'ranks' of the array
# To check the dimensions of a numpy array we make use of the attribute 'ndim'

# The kinds of Arrays that can be created are:
# Zero DImensional Array
# One Dimensional Array
# Two Dimensional Array (basically a matrix)


# Zero DImensional Array
import numpy as np
zeroedinArray = np.array(46)
print(zeroedinArray)
print(type(zeroedinArray))
print(f"Dimensions: {zeroedinArray.ndim} ")

# One Dimensional Array
import numpy as np
onedimensionalArray = np.array([1,2,3,4,5])
print(onedimensionalArray)
print(type(onedimensionalArray))
print(f"Dimensions: {onedimensionalArray.ndim} ")

# Two Dimensional Array
import numpy as np
twodimensionalArray = np.array([[1,2,3],[4,5,6]]) #This should always be declared structured
print(twodimensionalArray)
print(type(twodimensionalArray))
print(f"Dimensions: {twodimensionalArray.ndim} ")

