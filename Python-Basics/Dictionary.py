dict1 = {"key":"value",  #the keys should be hashable #unique/Immutable
         1:"Hello",
         2:"Bye",
         "word":"String",
         "bool":True,
         "list":[1,2,3,4],
         (1,2,3):"Tuple"}
print(hash((1,2,3)))

mydict = {
    "Raj" : 89,
    "Akshat" : 34,
    "Kalash" : 10,
    "Sneha" : 35,
}
print(type(mydict))
print(mydict["Akshat"])

print(hash(23.49))

'''
Features of a Dictionary
Muttable
key-value pair
keys only accept hashable values
Unordered
Doesn't allow duplicates
Iterable

'''