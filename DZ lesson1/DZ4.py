number = input ("Введите целое положительное число:")
max = 0
for i in number:
    while int (i) > max:
        max = int (i)
print (max)
