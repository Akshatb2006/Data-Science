# To initialize an empty array in numpy we use numpy,zeroes() function

import numpy as np
initArray = np.zeros((3,4))
print(initArray)
print(type(initArray))

# Initialize this array with some values using loops
# make use of np.shape()
'''rows, cols = np.shape(initArray)
for i in range(rows):
    for j in range(cols):
        initArray[i][j] = i + j

print("\nUpdated Array:")
print(initArray)'''

for i in range(initArray.shape[0]):
  for j in range(initArray.shape[1]):
    initArray[i][j] = (i+1)*(j+1)
print(initArray)