"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу. """

special_char = 'q'


def get_numbers():
    """
    Запрашивает строку чисел у пользователя

    :return: список введенных чисел и флаг выхода
    """

    while True:
        user_input = input("Введите строку чисел, разделенных пробелом (q для выхода): ").split()

        flag = special_char in user_input
        index = user_input.index(special_char) if flag else len(user_input)

        try:
            return list(map(int, user_input[:index])), flag
        except ValueError:
            print("Это не список чисел!")


list_sum = 0

while True:
    num_list, exit_flag = get_numbers()
    list_sum += sum(num_list)

    print(f"Новая сумма: {list_sum}")

    if exit_flag:
        break
