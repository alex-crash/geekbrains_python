"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input()."""

my_list = input("Введите элементы списка через пробел: ").split()

index = 1
while index < len(my_list):
    my_list[index - 1], my_list[index] = my_list[index], my_list[index - 1]
    index += 2

print(f"Новый список: {my_list}")
