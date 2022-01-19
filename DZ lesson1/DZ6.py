a = float (input ("Введите результат первого дня в км: "))
b = float (input ("Введите желаемый для достижения результат в км: "))
day = 1
while a < b :
    a = a + (a * 0.1)
    day += 1
print(day)