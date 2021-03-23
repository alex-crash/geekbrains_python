"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
только числами. Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на
экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
этом работа скрипта не должна завершаться.
"""


class NotANumberException(Exception):
    def __init(self, text):
        self.text = text


def is_float(float_str: str):
    try:
        float(float_str)
    except ValueError:
        return False
    else:
        return True


def main():
    my_list = []

    while True:
        user_input = input("Введите следующее число (stop для выхода): ")

        if user_input == 'stop':
            break

        try:
            if user_input.isdigit():
                number = int(user_input)
            elif is_float(user_input):
                number = float(user_input)
            else:
                raise NotANumberException("Введено не число, пропускаем...")
        except NotANumberException as e:
            print(e)
        else:
            my_list.append(number)

    print(f"Список введенных чисел: {my_list}")


if __name__ == '__main__':
    main()