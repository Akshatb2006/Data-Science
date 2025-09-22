num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

avg = (num1+num2+num3)/3

print("The average of these three numbers is : " + str(avg))

def avg() :   #function declaration
  num1 = int(input("Enter num1: "))
  num2 = int(input("Enter num2: "))
  num3 = int(input("Enter num3: "))
                                      #function definition
  avg = (num1+num2+num3)/3

  print("The average of these three numbers is : " + str(avg))
avg() #function call

def cube() :   #function declaration
  num1 = int(input("Enter num1: "))
                                      #function definition
  cube = num1*num1*num1

  print("The cube of the number is : " + str(cube))
cube() #function call

# 2 types of function in python, 1.Built in(len,input,print,etc)  2.User Defined
# functions with arguments

def greet(name):
  print(f"Good Afternoon Sire {name}")

greet("Sai")

def greet1(name,title="Singh"):
  print(f"Good Afternoon Sire {name} {title}")

greet1("Sai")
greet1("Sai","Kumar")

def func1(val):
  return val*2
func1(5)

def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
factorial(5)