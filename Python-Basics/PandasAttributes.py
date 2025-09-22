# dtype
# ndim
# size
# shape
# index
# hasnans

#Methods
# head()
# tail()
# info()

data1 = [10,20,30,40,50,60,"hello","hi"]

series1 = pd.Series(data1)
print(series1)

# Using dtype attribute
print("\n\nDatatype of this Series:",series1.dtype)

# Using ndim attribute
print("\n\nDimensions of this Series:",series1.ndim)

# Using size attribute
print("\n\nSize of this Series:",series1.size)

# Using size attribute
print("\n\nSize of this Series:",series1.size)

# Using shape attribute
print("\n\nShape of this Series:",series1.shape)

# Using hasnans attribute
print("\n\nSeries has Node value?:",series1.hasnans)

# Using index attribute
print("\n\nIndexes of this Series:",series1.index)

# Using head() method
print("\n\nFirst 5 rows of this Series:\n",series1.head())

# Using tail() method
print("\n\nLast 5 rows of this Series:\n",series1.tail())

# Using info() method
print("\n\nInformation about this Series:\n",series1.info())

