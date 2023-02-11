# Иммитатор телевизора
# Можно переключать каналы в диапазоне и менять уровень громкости
# Created by Luero, 04/06/2022

CHANNELS = {1 : 'Россия',
            2 : 'СТС',
            3 : 'MTV',
            4 : 'National Geographic'}
class television(object):
    def __init__(self, channel = CHANNELS[1], volume = 5):
        print('Вы включили телевизор.')
        self.channel = channel
        self.volume = volume
        self.__status()
    def sound(self):
        choice = int(input('Введите уровень громкости от 0 до 10: '))
        if choice in range (0, 10):
            self.volume = choice
            self.__status()
        elif choice < 0:
            print ('Тише некуда! Поставлю на 0.')
            self.volume = 0
            self.__status()
        elif choice > 10:
            print ('Так громко я не умею... Поставлю на максимум.')
            self.volume = 10
            self.__status()
        else:
            print ('Что-то пошло не так...')
    def chan_swap(self):
        i = int(input('Введите номер канала от 1 до 4.'))
        if i in CHANNELS:
            self.channel = CHANNELS[i]
            print('Вы переключили на ', self.channel)
            self.__status()
        else:
            print('Такого канала нет в списке.')
    def __status(self):
        print('Текущий канал: ', self.channel, '. Текущая громкость: ', self.volume)
def main():
    tele = television()
    choice = None
    while choice != '0':
        print ("""
                    Программа "Ваш телевизор"

                    0 - Выйти
                    1 - Изменить громкость
                    2 - Переключить канал
                    """)
        choice = input('Ваш выбор: ')
        print()
        if choice == '0':
            print('Вы выключили телевизор.')
        elif choice == '1':
            tele.sound()
        elif choice == '2':
            tele.chan_swap()
        else:
            print('Вы ввели недопустимый выбор.')

main()
input ('\n\nPress Enter to escape')
    
