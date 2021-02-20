"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения. Например, в первом задании выводим целые числа,
начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено. """

from itertools import count, cycle
from sys import argv


def count_wrapper(start: int, end: int):
    for i in count(start):
        print(i, end=' ')
        if i == end:
            break


def cycle_wrapper(iter_list: list, iter_count: int):
    repeat = 0
    for i in cycle(iter_list):
        print(i, end=' ')
        repeat += 1
        if repeat == iter_count:
            break


def main(*args):
    print("Numbers from 10 to 15:", end=' ')
    count_wrapper(10, 15)
    print()

    print("Cycle trought [1, 2, 3] 5 times:", end=' ')
    cycle_wrapper([1, 2, 3], 5)
    print()


if __name__ == '__main__':
    main(*argv)
