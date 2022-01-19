revenue = int (input ("Введите сумму выручки: "))
cost = int (input ("Введите сумму издержек: "))
if revenue > cost:
 print ("Прибыль!")
 profit = revenue - cost
 profitability = profit / revenue
 print (f" Рентабельность фирмы {profitability} ")
 workers_count = int (input ("Введите численность сотрудников фирмы: "))
 profit_for_workers = float (profit / workers_count )
 print (f" Прибыль на одного сотрудника: {profit_for_workers}")
else:
  print ("Убыток!")
