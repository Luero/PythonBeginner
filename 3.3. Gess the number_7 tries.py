# Игра "Отгадай число"
# Компьютер загадывает число, нужно отгадать его за 7 попыток
# Created by Luero, 22.04.2022

import random
secret = random.randint (1, 100)
tries = 7

print ('Компьютер загадал натуральное число от 1 до 100.')
print ('Ваша задача - отгадать число за 7 попыток.')
print ('После каждой попытки будет выдаваться подсказка.')
print ('Ну что, поехали?')

while tries > 0:
    guess = int (input('\nВаше предположение: '))
    tries -= 1
    triesleft = 7-tries
    if guess == secret:
        print ('Вы угадали, поздравляю!')
        print ('Yahoo!!!')
        print ('Вы справились за ', triesleft, ' попыток.')
        break
    elif guess > secret:
        print ('Попробуй меньше...')
        print ('Осталось ', tries, 'попыток.')
    elif guess < secret:
        print ('Попробуй больше...')
        print ('Осталось ', tries, 'попыток.')
if tries == 0:
    print ('\nGame over!')
    print ('Ваши попытки закончились... Я загадал ', secret)

input ('\n\nPress Enter to escape')
