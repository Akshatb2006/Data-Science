#Shape in a numpy array is the exact number of elements in each direction
#We determine the shape of a numpy array through array.shape attribute
nzeroarray = np.array(23)
print(nzeroarray)
print(nzeroarray.ndim)
print(nzeroarray.shape)

nonedarray = np.array([1,2,3,4,5,6,7])
print(nonedarray)
print(nonedarray.ndim)
print(nonedarray.shape)

ntwodarray = np.array([[1,2,3],[4,5,6]])
print(ntwodarray)
print(ntwodarray.ndim)
print(ntwodarray.shape)

nthreedarray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(nthreedarray)
print(nthreedarray.ndim)
print(nthreedarray.shape)