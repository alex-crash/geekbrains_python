"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов. """


def my_func(*args):
    """
    Возвращает сумму наибольших двух аргументов

    :param args: Аргументы для вычислений
    :return: Сумма наибольших двух аргументов
    """

    sorted_args = sorted(args, reverse=True)
    return sum(sorted_args[:2])


print(my_func(4, 2, 7))