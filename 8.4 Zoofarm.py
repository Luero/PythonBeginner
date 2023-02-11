# Игра "Зооферма"
# У пользователя несколько животных, которых можно одновременно кормить, либо играть с ними
# Created by Luero, 04/06/2022

import random

class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        hunger = random.randint(0, 10)
        boredom = random.randint (0, 10)
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        print('Привет! Я ', self.name, ' ^_^ \n')
    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'прекрасно'
        elif 5 <= unhappiness <= 10:
            m = 'неплохо'
        elif 11 <= unhappiness <= 15:
            m = 'не сказать, чтобы хорошо'
        else:
            m = 'ужасно'
        return m
    def talk(self):
        print ('Меня зовут ', self.name, ', и сейчас я чувствую себя ', self.mood, '\n')
        self.__pass_time()
    def play(self):
        print('Я - ', self.name)
        fun = int(input('Cколько времени ты хочешь поиграть со мной?'))
        print('Уиии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    def eat(self):
        print('Я - ', self.name)
        food = int(input('Сколько еды ты мне дашь?'))
        print('Мрр... Спасибо!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def __str__(self):
        bored = str(self.boredom)
        hungered = str(self.hunger)
        rep = 'Объект класса Critter \n'
        rep += 'имя: ' + self.name + '\n' + 'уровень скуки: '
        rep += bored + '\n' + 'уровень голода: ' + hungered + '\n'
        return rep
def main():
    crit1_name = input ('Как ты назовешь свою первую зверушку?')
    crit1 = Critter(crit1_name)
    crit2_name = input('Как ты назовешь свою вторую зверушку?')
    crit2 = Critter(crit2_name)
    crit3_name = input('А теперь введи имя для третьей зверушки: ')
    crit3 = Critter(crit3_name)
    crits = [crit1, crit2, crit3]
    choice = None
    while choice != '0':
        print("""
                Ты - хозяин небольшой зоофермы.
                Вот что ты можешь сделать:
                
                0 - Выйти
                1 - Узнать о самочувствии питомцев
                2 - Покормить питомцев
                3 - Поиграть с питомцами
                """)
        choice = input('Ваш выбор: ')
        print()
        if choice == '0':
            print ('До свидания!')
        elif choice == '1':
            for i in crits:
                i.talk()
        elif choice == '2':
            for i in crits:
                i.eat()
        elif choice == '3':
            for i in crits:
                i.play()
        elif choice == '4':
            for i in crits:
                print(i)
        else:
            print ('Введите значение из меню.')

main()
input ('\n\nPress Enter to escape')
    
