revenue = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))

if revenue > costs:
    print("Фирма отработала с прибылью.")

    profit = (revenue - costs)
    print(f"Рентабельность выручки: {profit / revenue}")

    number_of_employees = int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль в расчете на сотрудника: {profit / number_of_employees}")
else:
    print("Фирма отработала в убыток.")
