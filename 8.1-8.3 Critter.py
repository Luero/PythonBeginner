# Игра "Моя зверушка"
# Можно кормить зверушку и играть с ней
# Created by Luero, 04/06/2022

class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
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
        fun = int(input('Cколько времени ты хочешь поиграть со зверушкой?'))
        print('Уиии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    def eat(self):
        food = int(input('Сколько еды дать питомцу?'))
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
    crit_name = input ('Как ты назовешь зверушку?')
    crit = Critter(crit_name)
    choice = None
    while choice != '0':
        print("""
                Моя зверушка.
                0 - Выйти
                1 - Узнать о самочувствии
                2 - Покормить
                3 - Поиграть
                """)
        choice = input('Ваш выбор: ')
        print()
        if choice == '0':
            print ('До свидания!')
        elif choice == '1':
            crit.talk()
        elif choice == '2':
            crit.eat()
        elif choice == '3':
            crit.play()
        elif choice == '4':
            print(crit)
        else:
            print ('Введите значение из меню.')

main()
input ('\n\nPress Enter to escape')
