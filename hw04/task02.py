"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]. """

from sys import argv


def main(*args):
    original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(f"Original list: {original_list}")

    new_list = [original_list[i] for i in range(1, len(original_list)-1) if original_list[i] > original_list[i-1]]
    print(f"New list: {new_list}")


if __name__ == '__main__':
    main(*argv)
