"""
6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
чтобы для каждого предмета были все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести его на экран.

Примеры строк файла:
Информатика:   100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —

Пример словаря: {“Информатика”: 170, “Физика”: 40,“Физкультура”: 30}
"""


def main():
    subj_dict = {}

    try:
        with open(r"task06.txt") as f_obj:
            for line in f_obj:
                subject_info = line.split()

                subject_name = subject_info[0].split(':')[0]
                hours = map(lambda s: s.split('(')[0], subject_info[1:])

                try:
                    sum_hours = sum([int(x) for x in hours if x != '—'])
                except ValueError:
                    print(f"Какая-то ошибка в файле...")
                else:
                    subj_dict[subject_name] = sum_hours
    except IOError:
        print("Ошибка ввода/вывода! Сделайте с этим что-нибудь...")

    print(subj_dict)


if __name__ == '__main__':
    main()
