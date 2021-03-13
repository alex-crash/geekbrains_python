"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
from json import dump


def profit_calc(filename):
    """
    Вычисляет прибыль компаний, а также среднюю прибыль

    :param filename: Имя файла
    :return: Список с информацией о прибыли компаний
    """
    firms_dict = {}

    # Здесь будет храниться количество фирм и средняя прибыль соответственно
    counts = [0, 0]

    try:
        with open(filename) as f_obj:
            for line in f_obj:
                firm_name, firm_type, firm_proceeds, firm_costs = line.split()

                try:
                    firm_profit = int(firm_proceeds) - int(firm_costs)
                except ValueError:
                    print(f"Какая-то ошибка в файле... Проверьте данные для следующей фирмы: {firm_name}")
                else:
                    firms_dict[firm_name] = firm_profit

                    if firm_profit > 0:
                        # Небольшой хук, чтобы избежать длинной арифметики
                        # Ничего личного, просто попытка поэкспериментировать :) См. task03.py за объяснениями
                        add_avg_profit = (firm_profit - counts[1]) / (counts[0] + 1)
                        counts = [sum(i) for i in zip(counts, [1, add_avg_profit])]
    except IOError:
        print("Ошибка ввода/вывода! Сделайте с этим что-нибудь...")

    return [firms_dict, {"average_profit": counts[1]}]


def main():
    firms_profit = profit_calc(r"task07_input.txt")

    try:
        with open(r"task07_output.txt", 'w') as f_obj:
            dump(firms_profit, f_obj)
    except IOError:
        print("Ошибка ввода/вывода! Сделайте с этим что-нибудь...")


if __name__ == '__main__':
    main()
