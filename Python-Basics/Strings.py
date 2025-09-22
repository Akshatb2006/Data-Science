#Kinds of String Declaration
str1='Hello'
str2='hello'
str3='''hello'''
str4="""hello"""
print(str1)
print(f'{str1} world')
#Strings are immutable in nature
print(len(str2))
print(str2[1:4]) #syntax is [startindex:endindex] - endIndex is discluded
print(str2[:3])

# Slicing with 3 parameters - [startIndex : EndIndex : step]
str='0123456789'
# for i in range(0,len(str),2):
#   if i%2==0:
#     print(str[i])

print('even = ' + str[2::2])
print(str[-2::-3]) #negative slicing