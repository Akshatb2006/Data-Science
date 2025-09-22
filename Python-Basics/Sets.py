#Set Declaration
set1 = {1,2,3,4,5,"Hello",False}
emptyset = set()
set2 = set([1,2,3,"aaa","bbb","ccc"])
print(type(emptyset))
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1|set2)
print(set1&set2)
print(len(set1))
print(set1.clear())

#Reads True and 1 as same, False and 0

'''
r = opens file in read mode
w = opens file in write mode + creates new file if doesn't exist
a = opens file in append mode
+- = opens file for updation
rb = opens file to read in binary mode
rt = opens file to read in text mode
r+, w+, a+ = opens file in modifyable mode (r+w), (w+r), (w+a)
'''

#WAP to write tables(2x1 = 2) from 2 to 20 in different text files.
#Store them in a folder

f = open("file.txt", "w")
newString = "This is replaced text"
f.write(newString)
#write() function replaces the existing data if the file exists
#Write() function creates a new file with the mentioned name and data if file doesn't exist
f.close()

f = open("file.txt", "a")
addedString = "\nThis is new line added with append"
f.write(addedString)
#append() function adds the new data mentioned.
f.close()

#This will not work in this VM
#Try running this code in a local IDE