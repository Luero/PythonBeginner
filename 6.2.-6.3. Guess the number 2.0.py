# Игра "Отгадай число" 2.0
# С использованием функции ask_number
# Created by Luero, 29/05/2022

def ask_number (question, low, high):
    response = None
    while response not in range (low, high):
        response = int(input(question))
        return response
def main ():
    import random
    low = 0
    high = 100
    number = random.randint (low, high)
    print ('Я загадал число от 1 до 100.')
    print ('Попробуй отгадать его за 5 попыток.\n')
    tries = 5
    guess = None
    while tries !=0 and guess != number:
        guess = ask_number ("\nТвоя догадка: ", low, high)
        tries -=1
        if guess == number:
            print ('Ура! Это именно ', guess)
        else:
            print ('\nНет, попробуй еще раз.')
            if guess < number:
                print ('Больше...')
            elif guess > number:
                print ('Меньше...')
            else:
                print ('У меня тут ошибочка...')
    if tries == 0:
        print ('Твои попытки закончились.')
        print ('Это было число ', number)
    else:
        print ('Что-то в моей программе пошло не так... Извини =(')
main()
input ('\n\nPress Enter to escape')
