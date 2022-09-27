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

# my_file = open("1stFile.txt", "a+")
# my_file.write("\nDoe")
# my_file.close()
# print(type(my_file))
with open('1stFile.txt', 'a+') as forRead_file:
    # forRead_file.write('\nabraCadabra')
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
    # forRead_file.close()
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

# list
int_list = [1, 2, 3]
mixed_list = [1, 1.2, 'string']
print(len(mixed_list))
names1 = ['Jonhdd', "dsdsd", "Asd"]
names2 = ['Tracy', 'Ekskdasd']
print(names1 + names2)
names1.append('Черноголовка')
names1.sort()
print(names1)
names1.sort(key=len)
print(names1)
names1.sort(reverse=True)
print(names1)

# dict
players = {'First': 1, "Second": 2, "Third": 3, "Четвертый": 4}
print(type(players))
players_another = dict(Первый=1, ВТорой=2, Третий=3, Четвертый=4)
print(type(players_another))
print(players.get('Second'))
players['So'] = 5  # добавляем в словарь пару ключ значение
print(f"Это словарь: {players}")
players["So"] = 6
del players["So"]
print(type(players.keys()))
print(players.keys())
keys_as_list = list(players.keys())
print(sorted(players.keys()))
print('First' in players)
print('Первый' not in players)
dic_values = players.values()
print(dic_values)
for k, v in players.items():
    print(k, v)
print(players.items())
players.pop('First')
print(players.items())
players.setdefault("Десятый")
print(players.items())

# tuple
strings = ('das1', 'dsass2', 'dssa3')
print(strings[-1])
print(type(strings))

# named tuple
new_players = [('warlsen', 1990, 2843), ('tuborg', 190, 43), ('çan', 1994, 28223)]
print(new_players[0])
from collections import namedtuple

Player = namedtuple('Player', 'name age rating')
nnew_players = [Player('dsds32', 12323, 1321), Player('dsds31', 1323, 121), Player('dsds33', 1243, 11)]
print(nnew_players[0].name)
p1 = nnew_players[0]
print(p1.name)
print(p1.age)
print(p1.rating)

# if else
if True:
    print('índeed, true.')
if 3 > 2:
    print('3 is greater than 2')
is_admin = True
if is_admin:
    print("It's admin, look at him")

# selected_character = input()
# if selected_character == 'Protos':
#     print("Protos win")
# elif selected_character == "Zerg":
#     print("Protos failed. Zerg win.")
# elif selected_character == "Terrain":
#     print("Terrain is chosen")
# else:
#     print('It seems we have a new race')


# set
my_set = set()
print(type(my_set))
my_set.add(1)
my_set.add(2)
print(my_set)
my_set.add(2)
print(my_set)

my_list = [1, 1, 1, 1, 2, 2, 2, 4, 4, 4]
s = set(my_list)
print(s)
len(s)
print(1 in s)
print(5 in s)

# for
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

for i in numbers:
    print(i * i)

numbers = range(1, 6)
type(numbers)

for i in range(1, 6):
    print(i)

for i in range(1, 6):
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

numbers = [1, 3, 5, 7, 9]
for i, item in enumerate(numbers):
    numbers[i] *= 2
print(numbers)

list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]

pairs = []
for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))
print(pairs)

# list comprehension
greeting = 'hello, world!'
chars = []
for i in greeting:
    chars.append(i)
print(chars)

chars = [i for i in greeting]
print(chars)

chars = [i for i in 'bla, bla-bla']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [n for n in range(0, 10)]
print(numbers)

# while
x = 0
while x < 3:
    print(f'x equals {x}')
    x += 1
else:
    print('Çondition is not met')

vals = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in vals:
    if v % 2 ==0:
        continue
    else:
        sum +=v
    if sum > 10:
        break
print(sum)
