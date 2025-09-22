# Fetching columns through labels(column_names)
res = csvdf['Age']
print(res)

# Fetching multiple columns :
resmuiltple = csvdf[['Age','City']]
print("\n\n",resmuiltple)

# Fetching rows through customised indexes in loc
resloc = csvdf.loc["Bob"]
print("\n\n", resloc)

# Fetching rows through iloc()

resiloc = csvdf.iloc[2]
print("\n\n",resiloc)