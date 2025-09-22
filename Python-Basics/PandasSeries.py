# Pandas Series is a kind of one dimensional array which stores the data in a coloumn like structure with indexes
# We make use of the Series() method to create pandas series
#Parameters / Arguments

#data
#index
#coloumn
#copy
#dtype
#name
#index_col

# Declaring a series
import pandas as pd
data = [10,20,30,40,50,60]
series = pd.Series(data)
print(series)

#Accessing elements from the series using index
print("\n\n",series[0])

series1 = pd.Series(data, index = ['a','b','c','d','e','f'])
print("\n\n",series1)
#Accessing through custom index
print("\n\n",series1['a'])

