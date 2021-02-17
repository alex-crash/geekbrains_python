"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
весна, лето, осень). Напишите решения через list и через dict. """

while True:
    number = input("Введите номер месяца: ")
    if number.isdigit():
        number = int(number)
        if 1 <= number <= 12:
            break
        else:
            print("Это не номер месяца!")
    else:
        print("Это не число!")

seasons_list = ["зима", "весна", "лето", "осень"]
seasons_dict = {0: "зима", 1: "весна", 2: "лето", 3: "осень"}

season = number % 12 // 3

print(f"Время года (по списку): {seasons_list[season]}")
print(f"Время года (по словарю): {seasons_dict[season]}")
