time_second = int (input ("Введите время в секундах: "))
hour = time_second // 3600
minute = (time_second % 3600) // 60
second = (time_second % 3600) % 60
print (f"Время: {hour} : {minute} : {second}")

