# Реализуйте одну классическую и достаточно простую игру: "угадай число".
# Компьютер загадывает число от 1 до 50 и даёт 6 попыток пользователю, чтобы тот смог угадать загаданное число.
# Когда пользователь вводит число, компьютер проверяет угадано ли число и если не угадано, то сообщает пользователю меньше ли
# или больше загаданое число. Если пользователь угадал - то сообщает о том, что число отгадано.
#
# Подсказка: для "загадывания" числа используйте модуль random: импортируйте его и для генерации (загадывания)
# числа вызовите метод random.randint(1, 50).
import random

generatedNumber = random.randint(1, 5)
print(generatedNumber)
# print(type(generatedNumber))

for i in range(0, 6):
    input_digit = int(input())
    # print(type(input_digit))
    if input_digit == generatedNumber:
        print(f'Congratulations. You guessed the number {input_digit}.')
        break
    elif i == 5:
        print(f'Number is not correct. The game is over.')
    else:
        print(f'Number is not correct. Please choose another number. {5 - i} trying left.')

# Даны три неубывающих массива чисел. Найти число, которое присутствует во всех трех массивах.
# Input: [1,2,4,5], [3,3,4], [2,3,4,5,6]
a_list = [1, 2, 4, 5]
b_list = [3, 3, 4]
c_list = [2, 3, 4, 5, 6]


def findNumber(a, b, c):
    answer_list = []
    for i in a:
        for i2 in b:
            for i3 in c:
                if i == i2 and i == i3:
                    if i not in answer_list:
                        answer_list.append(i)
    return answer_list


print(findNumber(a_list, b_list, c_list))
