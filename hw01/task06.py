a = float(input("a = "))
b = float(input("b = "))

day = 1
while a < b:
    a *= 1.1
    day += 1

print(f"{day}")
