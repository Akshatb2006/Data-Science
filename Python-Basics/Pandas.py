# Pandas
# An open source library which is considered to be one of the most powerful libraries
# for data analysis + data manipulation in Python

# Pandas is used mainly for data cleaning, reading the data, from small/ large datasets, external CSVs, Excel, JSON etc
# and making it relevant for data science
# Pandas DataFrames are created by pandas.DataFrame() method
# Pandas DataFrames are a form of tabular structured display of data.
# Parameters inlcuded in this DataFrame() method are :

# data = the exact data that you are trying to convert into a dataframe
# index = gives us the index of a specified cell(s)
# dtype = gives us the datatype of each column
# column = to manipulate column labels
# copy = to copy the data into another DataFrame

import pandas as pd

data = {
    'Student' : ['Raj', 'Abhishek', 'Debashish', 'Sanket', 'Kalash'],
    'Subject' : ['Python', 'Sanskrit', 'JavaScript', 'Java', 'Biology'],
    'Marks' : [72,88,2,33,99]
}
#Converting a given dictionary into a dataframe

dataframe = pd.DataFrame(data)
print(dataframe)

# Providing indexes to each row

dataframe1 = pd.DataFrame(data, index = ['Index1','Index2','Index3','Index4','Index5'])
print("\n\n",dataframe1)

# Accessing these elements (a group of row and column(cell))
# To access elements we make use of the pandas.loc() method

print("\n\n", dataframe1.loc['Index1','Student']) # syntax : loc['row_name','column_name']
# Java
# 99

# We use iloc() method for accessing elements through indexes

print("\n\n", dataframe1.iloc[2,0]) # syntax : iloc['row_index','column_index']
print("\n\n", dataframe1.iloc[[2,3],[]])

# Accessing the columns :
print("\n\n")
print("Columns: \n")
for col in dataframe1:
  print(col)