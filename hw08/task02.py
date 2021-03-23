"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroDivisionException(Exception):
    def __init__(self, text):
        self.text = text


class Integer:
    def __init__(self, integer: int):
        self.integer = integer

    def __truediv__(self, other):
        if other.integer == 0:
            raise ZeroDivisionException("Попытка деления на ноль")
        else:
            return Integer(self.integer // other.integer)


def main():
    while True:
        user_input = input("Введите два числа через пробел (q для выхода): ")

        if user_input == 'q':
            break

        try:
            a, b = map(int, user_input.split())
            print(f"Результат целочисленного деления: {a} // {b} = {(Integer(a) / Integer(b)).integer}")
        except (ValueError, ZeroDivisionException) as e:
            print(e)


if __name__ == '__main__':
    main()
