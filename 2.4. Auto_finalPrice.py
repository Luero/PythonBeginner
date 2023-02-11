# Автодилер
# Программа рассчитывает наценки на авто (налог, регистрационный сбор, агентский сбор, цену доставки)
# Created by Luero, 23/04/2022

initialPrice = int(input('Введите стоимость автомобиля без наценок'))
tax = initialPrice * 20 / 100
regFee = initialPrice *11/100
agentFee = int("15000")
transportFee = 30000
finalPrice = initialPrice + tax + regFee + agentFee + transportFee
print ('\nОкончательная цена авто составляет ', finalPrice)
input ('\n\nPress Enter to escape')                   
