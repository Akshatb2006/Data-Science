#List, #Tuple, #Dictionary, #Set
my_list =[1,2,3,"hello",4.5,"true",True,None,[2,4,"hello"]]
print(my_list)
print(my_list[1])
for i in my_list:
  print(i)

#Slicing in List
print(my_list[0:4])
print(my_list[-1][-1])

#Functions in list
list1=[2,4,66,12,1,5,3,22]
list1.sort()
list1.reverse()
print(list1)
list1.append(44)
print(list1)
list1.insert(3,47)
print(list1)
list1.index(47)
print(list1.count(47))
list1.pop()
list1.remove(66)
print(list1)

"""
Features of List :
Ordered Collection
Heteregenous Data
Mutable
Indexing/ Slicing
Iterable
Allows Duplicates
Nested Lists are allowed
Non-Hashable

"""

listExample = [1,2,3,55,6,6,2,1,7,7,3,556,56]
def inbuiltSum(listExample):
  return sum(listExample)
inbuiltSum(listExample)

def sum(listExample):
  n=0
  for i in listExample:
    n+=i
  return n
sum(listExample)

a = input().split()
#removes whitespaces from given string
#break the string into smaller chunks detecting a whitespaces
print(a)