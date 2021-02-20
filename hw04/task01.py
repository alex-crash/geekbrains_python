"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. """

from sys import argv


def salary_calc(hours: float, rate: float, premium: float):
    """
    (float, float, float) -> float

    Рассчитывает заработную плату

    :param hours: выработка в часах
    :param rate: ставка в час
    :param premium: премия
    :return: (float) заработная плата
    """

    return hours * rate + premium


def main(*args):
    try:
        hours = float(args[1])
        rate = float(args[2])
        premium = float(args[3])
    except (IndexError, ValueError):
        print(f"Usage: {args[0]} <hours> <rate> <premium>")

    print(f"Заработная плата: {salary_calc(hours, rate, premium)}")


if __name__ == '__main__':
    main(*argv)
