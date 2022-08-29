import os
import sys

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
    print(forRead_file.closed)
    #forRead_file.close()
    print(forRead_file.closed)

print(forRead_file.closed)


print(sys.getdefaultencoding())
s = 'hello'
enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8')
enc_utf16 = s.encode('utf16')
print(enc_utf8, enc_utf8, enc_utf16)
result = enc_utf16.decode('utf16')
print("result bytes converted to str:", result)


