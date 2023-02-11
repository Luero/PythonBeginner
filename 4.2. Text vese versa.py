# Программа принимает текст из пользовательского ввода и печатает в обратном порядке
# Created by Luero, 16/05/2022

print ('Я могу написать Ваш текст наоборот!')
message = input ('\n Введите Ваш текст: \n')
length = len(message)
for i in range(length):
    position = length - 1
    length -=1
    print (message[position], end = "")

input ('\n\n Press Enter to escape')
