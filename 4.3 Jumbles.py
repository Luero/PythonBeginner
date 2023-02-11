# Игра "Анаграмы"
# Created by Luero, 17/05/2022

import random
WORDS = ("колотушка", "ставни", "окно", "грильяж", "подсолнух")
HINTS = ("Кое-что, чем можно бить-колотить",
         "Ими в старину закрывалось окно",
         "... в Европу",
         "Конфеты с начинкой из орехов с медом",
         "Желтый большой цветок")
number = random.randrange(0, len(WORDS))
word = WORDS[number]
hint = HINTS[number]
score = len(WORDS[number])
correct = word
jumble = ''
yes = 'Да'
no = 'Нет'

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word [ : position] + word [(position + 1) :]
print ('Приветствую в игре "Анограмы"!')
print ('Ты можешь получить одну подсказку, но это уменьшит счет в два раза.')
print ('\nВот анаграма, которую я предлагаю решить: ', jumble)
guess = input ('\nПопробуйте отгадать исходное слово: ')
if guess.lower () != correct and guess != '':
    print ('К сожалению, Вы не правы')
    hintRequest = input ('Нужна ли Вам подсказка?')
    if hintRequest.lower () == yes.lower ():
        print (hint)
        score /= 2
    else:
        guess = input ('\nПопробуйте еще раз: ')
    while guess.lower () != correct and guess != '':
        guess = input ('\nПопробуйте еще раз: ')
if guess.lower () == correct:
    print ('Вы угадали!')
    print ('Ваш счет: ', score)
print ('Спасибо за игру!')
input ('\n\nPress Enter to escape')
    

