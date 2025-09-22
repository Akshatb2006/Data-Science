#There's a function which solves a purpose.
#The place of execution of any program would be your RAM
# The RAM is a volatile form of memory in which all your contents are lost...
#...once the program terminates
#To store any form of data permanently you need files

#HDD is a form of non-volatile memory which can save files permanently

# reading from text files and writing into text files
from google.colab import files
uploaded = files.upload()

for filename in uploaded :
  #Opens the file
  f = open(filename)  #open() function - ("filename", "operation")
  #Reads the file
  data = f.read()
  #prints the data
  print(data)
  #Closes the file
  f.close()


# read() function variants
# readline()
# readlines()

from google.colab import files
uploaded = files.upload()

for filename in uploaded :
  with open(filename, "r") as f:  #with helps you avoid explicit declaraion of close()
    line1 = f.readline()
    print(line1, type(line1))
    line2 = f.readline()
    print(line2, type(line2))
    line3 = f.readline()
    print(line3, type(line3))
    line4 = f.readline()
    print(line4, type(line4))

    from google.colab import files
uploaded = files.upload()

for filename in uploaded :
  with open(filename, "r") as f:
    lines = f.readlines()
    print(lines, type(lines))

#Read from a file names animals.txt and
#check whether the file contains the word "hen" in it