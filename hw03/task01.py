"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль. """


def division(dividend, divisor):
    """
    Выполняет деление двух чисел

    :param dividend: делимое
    :param divisor: делитель
    :return: частное от деления чисел и None при попытке деления на 0
    """

    try:
        return dividend / divisor
    except ZeroDivisionError:
        print("На ноль делить нельзя! (точнее можно, но вы получите бесконечность)")


def input_int(prompt):
    """
    Запрашивает целое число у пользователя

    :param prompt: приглашение для ввода числа
    :return: введенное число
    """
    while True:
        user_input = input(prompt)

        try:
            return int(user_input)
        except ValueError:
            print("Это не целое число!")


a = input_int("Введите делимое: ")
b = input_int("Введите делитель: ")

print(f"Результат деления: {division(a, b)}")
