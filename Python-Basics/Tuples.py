#tuple declaration
t1 = (1,2,3,3,3,"hello",True)
t2 = ()
t3 = (1,)

for i in t1:
  print(i)

t1.count(3)
print(t1[1])

#functions in tuples
t1.count(3)#print the occurrence of 3
t1.index("hello")

'''
Features of Tuples in python
Ordered
Heterogenous
Iterable
Indexing
Slicing
Immutable
Allows Duplicates
Nested Tuples
'''

s = "hello"
sorted_list = sorted(s)
sorted_string = "".join(sorted_list)
print(sorted_string)

list = ['acd','erv','ert']
list.sort()
print(list)

def listinput():
  my_list = []
  for i in range(7):
    user_input = input(f"Enter item {i+1}: ")
    my_list.append(user_input)
  return my_list

print(listinput())