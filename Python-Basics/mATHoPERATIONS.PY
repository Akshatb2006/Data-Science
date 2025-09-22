import numpy as np
matharr = np.array([1,2,3,4,5,6])
print(f"Sum of this array : {np.sum(matharr)}")
print(f"Mean of this array : {np.mean(matharr)}")
print(f"Min of this array : {np.min(matharr)}")
print(f"Max of this array : {np.max(matharr)}")
print(f"Product of this array : {np.prod(matharr)}")
print(f"Standard Deviation of this array : {np.std(matharr)}")

math2darray = np.array([[1,2,3],[4,5,6]])
print(math2darray)
print(f"Column wise sum: {np.sum(math2darray, axis = 0)}") #column wise sum
print(f"Row wise sum: {np.sum(math2darray, axis = 1)}") #row wise sum
print(f"Column wise product: {np.prod(math2darray, axis = 0)}") #column wise prod
print(f"Row wise product : {np.prod(math2darray, axis = 1)}") #row wise prod

# cumsum() #for cumulative sum
# cumprod() #for cumulative prod
print(f"cumulative Sum : {np.cumsum(matharr)}")
print(f"Normal Sum: {np.sum(matharr)}")

arr3 = np.array([-1.7,2.4,3.6,-4.8])
print(f"Absolute of this array : {np.abs(arr3)}")
print(f"Round of this array : {np.round(arr3)}")
print(f"Floor of this array : {np.floor(arr3)}")
print(f"Ceil of this array : {np.ceil(arr3)}")


