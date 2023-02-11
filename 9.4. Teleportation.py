# Приключенческая игра, в которой игрок может менять свое местонахождение, перемещаясь к одному из мест, ближайших к текущему
# Created by Luero, 25/06/2022

class Player(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        rep = "Игрок" + self.name
        return rep
    def travel(self, area):
        import random
        i = len(area.places)
        current_pl_ind = random.randrange(i)
        current_place = area.places[current_pl_ind]
        print (current_place)
        cont_travel = None
        while cont_travel != 'n':
            cont_travel = input ('\nБудем перемещаться отсюда? <y/n>:')
            if cont_travel == 'y':
                try:
                    range_of_travel = random.randint(current_pl_ind - 1, current_pl_ind + 1)
                    destination = area.places[range_of_travel]
                except IndexError as e:
                        print ('Дальше перемещаться уже некуда... Попробуем еще раз')
                        range_of_travel = random.randint(current_pl_ind - 1, current_pl_ind + 1)
                        destination = area.places[range_of_travel]
                print ('\nБлагодаря своей супер силе ты совершил скачок в пространстве!', destination)
            elif cont_travel == 'n':
                print ('Хорошо, передохнём...')
            else:
                print ('Введите "y" или "n"')
            
class Place(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        rep = "\nВы попали в прекрасное место - " + self.name
        return rep

class Area(object):
    def __init__(self):
        places = []
        self.places = places
        places_to_travel = ["Франция", "Англия", "Ирландия", "Исландия", "Норвегия", "Швеция", "Россия", "Америка", "Мексика", "Бразилия"]
        for place in places_to_travel:
            place = Place(place)
            places.append(place)
    def __str__(self):
        rep = "Это пространство включает такие прекрасные места! " + self.places
        return rep

class Game(object):
    def __init__(self, name):
        self.area = Area()
        self.player = Player(name)
    def play (self):
        choice = None
        while choice != 'n':
            choice = input('\nГотов к путешествию? <y/n>:').lower()
            if choice == 'y':
                self.player.travel(self.area)
            elif choice == 'n':
                print ('Я понял, путешествия отнимают много энергии, нужно отдохнуть')
                print ('\nДо встречи!')
            else:
                print ('Введите "y" или "n"')

def main():
    print ('\n\tТы - любознательный путешественник, у которго есть супер способность - телепортация!')
    print ('\tТы получил ее, когда спал, и сейчас самое время ей воспользоваться')
    name = input('Скажи, путешественник, как тебя зовут?')
    game = Game(name)
    game.play()
    input ('\nPress Enter to escape')

main()
            
         
        
