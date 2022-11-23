def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print("Ошибка деления на ноль. Нельзя вводить ноль. Выполнение программы продолжается.")
    except TypeError as ex:
        print("Введен не поддерживаемый тип. Нельзя вводить ноль. Выполнение программы продолжается.")
    print("Программа выполнена целиком")


divide(4, "d")
