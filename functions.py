# embedded functions
abs(-1)
abs(1)
max_number = max(1, 2, 3, 4, 5)
print(f'Max number is {max_number}.')
min_number = min(1, 2, 3, 4, 5)
print(f'Min number is {min_number}.')
h = hex(42)
o = oct(42)
b = bin(42)
print(h)
print(o)
print(b)

letters = 'abcd'
numbers = (10, 20, 30)
zipped = zip(letters, numbers)
print(type(zipped))
print(zipped)
zipped_list = list(zipped)
print(zipped_list)


# basic functions
def greeting():
    """
    DOCSTRING: Information about function
    INPUT: no input ...
    OUTPUT: Hello!
    """
    print('hello')


greeting()
help(greeting)


def print_name(name='Default'):
    print(name)


print_name('Eliad')
print_name()

result = print_name()
print(result)
print(type(result))


def get_greeting(name):
    return 'Hello ' + name


greeting = get_greeting('Adam')
print(greeting)


def get_sum(a, c):
    return a + c


my_sum = get_sum(2, 3)
print(my_sum)


def is_adult(age):
    return age >= 18


is_adult = is_adult(20)
print(is_adult)


def calc_taxes(p1, p2, p3):
    return sum((p1, p2, p3)) * 0.06


calc_taxes1 = calc_taxes(10, 20, 30)
print(calc_taxes1)


def calc_taxes2(*args):
    for x in args:
        print(f'Got payment = {x}')
    return sum(args) * 0.06


calc_taxes2(10, 20, 30, 40)
calc_taxes2 = calc_taxes2(10, 20, 30, 40)
print(calc_taxes2)


def save_players(**kwargs):
    for k, v in kwargs.items():
        print(f'Player {k} has rating {v}')


save_players(Carlsen=2800, Givi=200)


# лямбды
