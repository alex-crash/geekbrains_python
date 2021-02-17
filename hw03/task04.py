"""4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
** Подсказка:** попробуйте решить задачу двумя
способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла. """
from math import exp, log


def my_func(x, y):
    """
    Возвращает x в степени y

    :param x: основание
    :param y: показатель
    :return: степень с основанием x и показателем y
    """

    return x ** y


def my_func1(x, y):
    """
    Возвращает x в степени y

    :param x: основание
    :param y: показатель
    :return: степень с основанием x и показателем y
    """

    positive_power = 1
    for i in range(abs(y)):
        positive_power *= x

    return 1 / positive_power


def input_number(prompt, input_type):
    """
    Запрашивает целое число у пользователя

    :param prompt: приглашение для ввода
    :param input_type: тип числа
    :return: введенное число
    """
    while True:
        user_input = input(prompt)

        try:
            return input_type(user_input)
        except ValueError:
            print(f"Это не число типа {input_type}!")


base = input_number("Введите действительное положительное число: ", float)
while base <= 0:
    base = input_number("Введите положительное число: ", float)

power = input_number("Введите целое отрицательное число: ", int)
while power >= 0:
    power = input_number("Введите отрицательное число: ", int)

print(f"[Способ №0] {base} в степени {power} равно {exp(power * log(base))}")
print(f"[Способ №1] {base} в степени {power} равно {my_func(base, power)}")
print(f"[Способ №2] {base} в степени {power} равно {my_func1(base, power)}")
