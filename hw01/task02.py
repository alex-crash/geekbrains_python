time_in_seconds = int(input("Введите время в секундах: "))

hours = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
seconds = (time_in_seconds % 60)

print(f"Время в формате чч:мм:сс - {hours:02}:{minutes:02}:{seconds:02}")
