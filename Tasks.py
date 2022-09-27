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
#print(type(generatedNumber))

for i in range(0, 6):
    input_digit = int(input())
    #print(type(input_digit))
    if input_digit == generatedNumber:
        print(f'Congratulations. You guessed the number {input_digit}.')
        break
    elif i == 5:
        print(f'Number is not correct. The game is over.')
    else:
        print(f'Number is not correct. Please choose another number. {5 - i} trying left.')
