#The kinds of Data Types numpy supports are :
'''
b - boolean
u - unasigned char
m - timedelta
M - date time
U - unicode string
i - integer
f - float
c - complex float
O - object
'''

#TO determine the kind of data the array is holding, we use the 'dtype' attribute

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(arr.dtype) #int32 or int64 depends upon system u r working on, 32bit or 64bit

import numpy as np
sArray = np.array(["apple", "bananas", "cherry"])
print(sArray)
print(sArray.dtype) #U7 - unicode string, 7(Maximum character a string holds)

#type conversion of numpy arrays
#the function used for type conversion in numpy is "astype()"

import numpy as np
arr = np.array(['1','2','3','4','5'])
arr2 = np.astype(arr,"i")
print(arr.dtype)
arr = arr.astype("i")
print(arr.dtype)
print(arr2.dtype)
arr2 = arr2.astype("U")
print(arr2.dtype)

#Using dtype
array = np.array(["aaa","bbb","ccc","ddd"],dtype = 'S3')
print(array)
print(array.dtype)

from datetime import date
#Type declarations one by one

booleanarray = np.array([True, False, True])
print(booleanarray)
print(booleanarray.dtype)

integerarray = np.array([1,2,3,4,5],dtype = 'u1')
print(integerarray)
print(integerarray.dtype)
#Explanation = u1 denotes 8 bits. (range = 0-255)
#Explanation = u2 denotes 16 bits.
#Explanation = u4 denotes 32 bits.
#Explanation = u8 denotes 64 bits.

# 1+2j
#complex Array
newArr = np.array([1+2j, 3+4j, 5+6j], dtype='c8') #c8 is complex64
print(newArr)
print(newArr.dtype)

a = np.array(['5', '2', '3'], dtype='f8')
print(a)
print(a.dtype)

timedeltaArr = np.array([1,2,3,4], dtype = 'm8[D]')
print(timedeltaArr)
print(timedeltaArr.dtype)
#variations = m8[h], m8[s] fpr hours and seconds

datetimearr = np.array(["2025-08-10","2025-09-11"], dtype='M8[D]') #Datetime - day precision
print(datetimearr)
print(datetimearr.dtype)
#variations = m8[ms], m8[s]

objectarr = np.array([1,2,3,4], dtype='O')
print(objectarr)
print(objectarr.dtype)

stringarr = np.array(["aaa","bbb","ccc","ddd"],dtype = 'S')
print(stringarr)
print(stringarr.dtype)

