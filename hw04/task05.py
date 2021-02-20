"""5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
списка.
Подсказка: использовать функцию reduce(). """

from functools import reduce
from sys import argv


def main(*args):
    print(f"Generated value: {reduce(lambda x, y: x * y, [i for i in range(100, 1001)])}")


if __name__ == '__main__':
    main(*argv)
