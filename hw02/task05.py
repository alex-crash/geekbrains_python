"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

while True:
    number = input("Введите число (q для выхода): ")
    if number.isdigit():
        number = int(number)

        index = len(my_list)
        while index > 0:
            if my_list[index - 1] >= number:
                break
            index -= 1

        my_list.insert(index, number)
        print(f"Результат: {my_list}")
    elif number == 'q':
        break
    else:
        print("Это не число!")