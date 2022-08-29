import os

print("My name is {}".format("Elias"))
my_name = "John"
print("My name is {}".format(my_name))
name = "Jon"
age = 30
print(f"My name is {name} and I'm {age}")

dirpath = os.getcwd()
print(f"Path is {dirpath}")

#my_file = open("1stFile.txt", "a+")
#my_file.write("\nDoe")
#my_file.close()
#print(type(my_file))

with open('1stFile.txt', 'a+') as forRead_file:
    #forRead_file.write('\nabraCadabra')
    forRead_file.seek(0)
    dataStr = forRead_file.read()
    forRead_file.seek(0)
    dataList = forRead_file.readlines()
    print(type(dataList))
    print(dataList)
    forRead_file.seek(0)
    print("file dataStr: " + dataStr)
    print(forRead_file.read())


