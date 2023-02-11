# Компьютер отгадывает число
# Created by Luero, 27.04.2022

import random
print ('Загадай натуральное число от 1 до 100, а я попробую его отгадать.')
print ('Если я угадаю, нажми 1.')
input ('Введи слово \" готов \", если загадал.')

tries = 0
maxBorder = 100
minBorder = 1
check = ""
while check != "да":
    tries += 1
    guess = random.randint (minBorder, maxBorder)
    print ('\nПопробую ', guess)
    check = input('\nУгадал?').lower()
    if check !="да":
        addCheck = input('\nТвое число меньше?').lower()
        if addCheck == "да":
            maxBorder = guess
        elif addCheck == "нет":
            minBorder = guess
        else:
            print ('Что-то пошло не так, я сегодня не в форме. Прости...')
    
print ('\nУра! Какой я все-таки умный!')
print ('Я отгадал число всего лишь с ', tries, "попытки")

input ('\n\nPress Enter to escape')
