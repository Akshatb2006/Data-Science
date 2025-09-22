# To sort a numpy array we make use of the .sort() function
import numpy as np

# Sorting a 1D array

n1 = np.array([20,12,1,33,66,45])
n2 = np.array(["Shiv", "Mahadev", "Bholenath", "Nataraj", "Adidev", "Shankar"])

print("Unsorted Array : ", n1)
print("Sorted Array : ", np.sort(n1))

print("\n\nUnsorted Array : ", n2)
print("Sorted Array : ", np.sort(n2))

# Sorting a 2D array

n3 = np.array([[23,2,1],[44,5,68]])
print("\n\nUnsorted Array : \n", n3)
print("Sorted Array : \n", np.sort(n3))# Finding an element's index from an array
# We make use of where() function to do it

import numpy as np

n1 = np.array([1,2,3,4,33,5,6,23])

nresval = np.where(n1 == 33)
print(nresval)