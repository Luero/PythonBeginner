# Однокарточная игра "Война"
# Все игроки тягнут по одной карте из колоды, выигрывает тот, кто вытянул карту наибольшим номиналом
# Created by Luero, 24/06/2022

import cards, games

class W_Card(cards.Card):
    @property
    def value(self):
        if self.rank != "A":
            v = W_Card.RANKS.index(self.rank) + 1
        elif self.rank == "A":
            v = 11
        return v

class W_Deck(cards.Deck):
    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank,suit))

class W_Player(cards.Hand):
    def __init__(self, name):
        super(W_Player, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ':\t' + super(W_Player, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep
    def take (self, deck):
        choice_range = len(deck.cards)
        print ('\nСейчас в колоде ', choice_range, ' карт')
        print (self.name, ', тяните карту')
        choice = int(input('\nВведите номер выбранной карты: '))
        try:
            card = deck.cards[choice]
            self.add(card)
            deck.cards.remove(card)
        except IndexError as e:
            while choice not in range(choice_range):
                print ('\nСтолько карт в колоде нет, попробуйте еще раз.')
                choice = int(input('\nВведите номер выбранной карты: '))
                card = deck.cards[choice]
                self.add(card)
                deck.cards.remove(card)
        except ValueError and TypeError as e:
            print ('Это не число!')
            choice = int(input('\nВведите номер выбранной карты: '))
            card = deck.cards[choice]
            self.add(card)
            deck.cards.remove(card)

    @property
    def total(self):
        t = 0
        for card in self.cards:
            t += card.value
        return t

class W_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)
        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()
    def play(self):
        print ('\nСейчас игроки по очереди будут тянуть карты.')
        for player in self.players:
            player.take(self.deck)
            print (player)
        self.__winner()
    def __winner(self):
        results = []
        for player in self.players:
            score = player.total
            entry = (score, player.name)
            results.append(entry)
        results.sort(reverse = True)
        winner = results[:1]
        winner_name = winner[0][1]
        print ('\nПобеда за ', winner_name, '!')
        print ('Он набрал', winner[0][0], 'очков!')
        for player in self.players:
            player.clear()

def main():
    print ('Добро пожаловать в карточную игру "Война"!')
    print ('Правила просты: каждый из игроков тянет карту из колоды. Выигрывает тот, у кого на руках будет самая старшая карта')
    print ('Ну что, поехали?')
    names = []
    try:
        p = int(input('\nСколько игроков будет играть? <2-7>: '))
    except TypeError and ValueError as e:
        print ('Вы ввели не число.')
        p = int(input('\nСколько игроков будет играть? <2-7>: '))
    if p not in range (2,7):
        print ('Введите число от 2 до 7')
        int(input('\nСколько игроков будет играть? <2-7>: '))
    for player in range (p):
        name = input ('Введите имя игрока: ')
        names.append(name)
    game = W_Game(names)
    choice = None
    while choice !='n':
        game.play()
        choice = input ('Хотите сыграть еще? <y/n>:').lower()
    if choice == 'n':
        print ('\nСпасибо за игру!')
        print ('До встречи!')
    input ('\nPress Enter to escape')

main()
            
                    
