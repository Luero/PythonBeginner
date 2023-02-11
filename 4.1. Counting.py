# Программа считает по просьбе пользователя
# Нужно ввести начало, конец и интервал счета
# Created by Luero, 16/05/2022

start = int(input('Введите начало счета: '))
end = int(input('Введите конец счета: '))
end +=1
interval = int(input('Введите интервал счета: '))
for i in range (start, end, interval):
    print (i, " ", end = '')
input ('\n\nPress Enter to escape')
