number = int(input("Введите целое положительное число: "))

max_digit = 0

while number > 0:
    current_digit = number % 10

    if current_digit > max_digit:
        max_digit = current_digit

    number //= 10

print(f"Самая большая цифра в числе: {max_digit}")
