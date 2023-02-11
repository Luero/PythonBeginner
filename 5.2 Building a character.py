# Генератор персонажа ролевой игры
# У игрока есть 30 пунктов, которые можно распределить между 4-мя характеристиками
# Игрок может перераспределять пункты
# Created by Luero, 20/05/2022

pull = 30
character = ("Сила", "Здоровье", "Мудрость", "Ловкость")
stats = []
print ('\nПриветствую тебя в программе \"Генератор персонажа\"!')
print ('\nУ тебя есть 30 баллов, чтобы распределить их между четырьмя характеристиками:')
print ('"Сила", "Здоровье", "Мудрость", "Ловкость".')
print ('После распределения ты сможешь изменить выбор.')
print ('\nИтак, поехали! Давай создадим твоего персонажа')

while len(stats) < 3:
        for stat in character:
                print ('\nСколько баллов присвоить параметру ', stat, '?')
                char = int(input('\nВведи значение: '))
                if char > pull:
                   print ('У тебя недостаточно баллов.')
                   stats.append(0)
                   print ('Осталось', pull, ' баллов.')
                else:
                   stats.append(char)
                   pull -= char
                   print ('Осталось', pull, ' баллов.')
        
print ('\nТекущие характеристики персонажа: ')
for stat in  character:
    print (stat)
for number in stats:
    print (number)
print ('Осталось', pull, ' баллов.')
print ('\nУ тебя есть возможность перераспределить/дополнить баллы')

new_character = {"Сила" : stats [0],
                     "Здоровье" : stats [1],
                     "Мудрость" : stats [2],
                     "Ловкость" : stats [3]}

choice = int(input("""
 Если хочешь закончить, нажми 0.
 Если хочешь продолжить, нажми 1. """))

while choice != 0:
    change = input ('\nКакую характеристику ты хотел бы изменить?')
    change = change.title()
    if change in new_character:
        print ("""  \nЕсли ты хочешь добавить баллы, нажми 1.
Если ты хочешь убрать баллы, нажми 0. """)
        operation = int (input ('\nВведи номер операции: '))
        if operation == 1:
            new_char = int (input ('\nСколько баллов нужно добавить?'))
            if new_char <= pull:
                pull -= new_char
                new_character [change] = new_character.get(change) + new_char
                print ('\nТеперь характеристика ', change, ' составляет ', new_character.get(change))
                print ('Текущие характеристики персонажа: ', new_character)
                print ('Текущий остаток баллов: ', pull)
                choice = int (input ('\nПродолжим?'))
            else:
                print ('\nУ тебя недостаточно баллов.')
                choice = int (input ('\nПродолжим?'))
        elif operation == 0:
            new_char = int (input ('\nСколько баллов нужно вернуть в пулл?'))
            if new_char <= new_character.get(change):
                new_character [change]= new_character.get(change) - new_char
                pull += new_char
                print ('\nТеперь характеристика ', change, ' составляет ', new_character.get(change))
                print ('Текущие характеристики персонажа: ', new_character)
                print ('Текущий остаток баллов: ', pull)
                choice = int (input ('\nПродолжим?'))
            else:
                print ('\nУ тебя недостаточно баллов в этой характеристике.')
                print ('Ее значение составляет: ', new_character.get(change))
                choice = int (input ('\nПродолжим?'))
        else:
            print ('\nВы ввели недопустимое значение.')
            choice = int (input ('Продоложим?'))
    else:
        print ('\nУ персонажа нет такой характеристики.')
        choice = int (input ('Продолжим?'))
print ('\nПонял! До встречи!')
input ('\n\nPress Enter to escape.')

    
