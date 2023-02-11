# Программа выдает список слов в случайном порядке.
# Печатаются все слова из представленного списка
# Created by Luero. 20/05/2022

import random
words = ["валенок", "цветок", "стол", "танец", "мышь"]
newWords = []
print (words)
print ("\nСейчас программа выдаст этот же список, переставив слова в случайном порядке")
while words != []:
    for letter in words:
        index = random.randint(0, len(words)-1)
        newWords += [words[index]]
        del words[index]
print ("Вот новый список: ")
print (newWords)
input ("\n\nPress Enter to escape")
    
