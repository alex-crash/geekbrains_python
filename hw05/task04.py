"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

NUMBERS = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}


def main():
    try:
        with open(r"task04_input.txt") as input_obj, open(r"task04_output.txt", 'w') as output_obj:
            for line in input_obj:
                word = line.split()[0]
                output_obj.writelines(line.replace(word, NUMBERS[word]))
    except IOError:
        print("Ошибка ввода/вывода! Сделайте с этим что-нибудь...")


if __name__ == '__main__':
    main()
