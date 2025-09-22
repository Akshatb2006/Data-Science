# dtypes
# ndim
# index
# size
# shape
# T - Transpose changes rows to columns, columns to rows(2,3) - (3,2)
# head() - first 5 rows
# tail() - last 5 rows

data = {
    'Student' : ['Raj', 'Abhishek', 'Debashish', 'Sanket', 'Kalash','Jacob','King','Jack'],
    'Subject' : ['Python', 'Sanskrit', 'JavaScript', 'Java', 'Biology','Sorcery','Hotel management','casino player'],
    'Marks' : [72,88,2,33,99,44,56,78]
}

dataframe2 = pd.DataFrame(data, index = ['Index1','Index2','Index3','Index4','Index5','Index6','Index7','Index8'])

print(dataframe2)

#Datatypes in the Dataframe

print("\n\nDatatypes in this dataframe\n",dataframe2.dtypes)

#Dimensions in this Dataframe

print("\n\nDimensions in this dataframe : ",dataframe2.ndim)

#Shape in this Dataframe

print("\n\nShape of this dataframe : ",dataframe2.shape)

#Index in this Dataframe

print("\n\nIndexes in this dataframe : ",dataframe2.index)

#Size in this Dataframe

print("\n\nSize of this dataframe : ",dataframe2.size)

#Transpose of this Dataframe

print("\n\nTranspose of this dataframe : \n",dataframe2.T)

#Methods in DataFrames

# Using head() - prints the first 5 rows
print("\n\nFirst 5 rows of this dataframe : \n",dataframe2.head())
# Specifying this parameter
print("\n\nFirst 2 rows of this dataframe : \n",dataframe2.head(2))

# Using tail() - prints the last 5 rows
print("\n\nLast 5 rows of this dataframe : \n",dataframe2.tail())
# Specifying this parameter
print("\n\nLast 2 rows of this dataframe : \n",dataframe2.tail(2))


data1 = {
    'Student' : ['Raj', 'Abhishek', 'Debashish', 'Sanket'],
    'Subject' : ['Python', 'Sanskrit', 'JavaScript', 'Java'],
    'Marks' : [72,88,2,33]
}

data2 ={
    'Name' : ['Kalash','Jacob','King','Jack'],
    'Fields' : ['Biology','Sorcery','Hotel management','casino player'],
    'Ranks' : [99,44,56,78]
}

dataframe1 = pd.DataFrame(data1)
dataframe2 = pd.DataFrame(data2)

print(dataframe1)
print("\n\n", dataframe2)
# We make use of the join() method to join 2 different dataframes with each other.
print("\n\nAfter joining:\n",dataframe1.join(dataframe2))

resultant = pd.concat([dataframe1,dataframe2])
print("\n\n",resultant)

