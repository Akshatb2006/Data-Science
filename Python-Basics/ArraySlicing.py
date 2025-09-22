#Numpy array slicing is performed very similarly as normal arrays and strings

slicearray= np.array([20,30,40,50,60,70])
print(slicearray[2:4])
print(slicearray[:6]) #start to 5th
print(slicearray[2:])#2nd index to end
print(slicearray[::2])#slicing with 3 parameters
print(slicearray[1::-3])

#slicing in 2D array
slice2darray = np.array([[2,3,1,4,5,6],[7,8,9,10,11,12]])
print(slice2darray[0][1:4])
print(slice2darray[0:2,1:4])

