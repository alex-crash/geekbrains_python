"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
from random import randint
from itertools import starmap, repeat


def gen_file(filename, gen_count, gen_min, gen_max):
    """
    Записывает набор случайных чисел в файл

    :param filename: Имя файла
    :param gen_count: Количество чисел
    :param gen_min: Нижняя граница диапазона чисел
    :param gen_max: Верхняя граница диапазона чисел
    """
    try:
        with open(filename, 'w') as f_obj:
            numbers = starmap(randint, repeat((gen_min, gen_max), gen_count))
            print(*numbers, sep=' ', file=f_obj)
    except IOError:
        print("Ошибка ввода/вывода! Сделайте с этим что-нибудь...")


def get_sum(filename):
    """
    Подсчитывает сумму чисел в файле

    :param filename: Имя файла
    :return: Сумма чисел в файле
    """
    file_sum = 0

    try:
        with open(filename) as f_obj:
            for line in f_obj:
                try:
                    numbers = map(int, line.split())
                except ValueError:
                    print(f"Какая-то ошибка в файле...")
                else:
                    file_sum += sum(numbers)
    except IOError:
        print("Ошибка ввода/вывода! Сделайте с этим что-нибудь...")
    else:
        return file_sum


def main():
    filename = r"task05.txt"

    gen_file(filename, 5, -10, 10)
    print("Сумма чисел в файле: ", get_sum(filename))


if __name__ == '__main__':
    main()
