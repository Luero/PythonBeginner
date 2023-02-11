# Игра "Викторина" с набором баллов и вопросами по Python
# Created by Luero. 31/05/2022
# Amended by storage of records in txt file 15/06/2022

import sys
def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode, encoding = 'utf-8')
    except IOError as e:
        print ('Невозможно открыть файл', file_name, '\n', e)
        input('Нажмите Enter, чтобы выйти')
        sys.exit()
    else:
        return the_file
def next_line(the_file):
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line
def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    nominal = 0
    answers = []
    for i in range (4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    nominal = next_line(the_file)
    explanation = next_line(the_file)
    return category, question, answers, correct, nominal, explanation
def welcome(title):
    print ('\t\tДобро пожаловать в игру "Викторина"!\n')
    print ('\t\t', title, '\n')
def records(name, score):
    score = str(score)
    rec_new = name + ' : ' + score + ' | '
    f = open('records.txt', 'a+', encoding = 'utf-8')
    f.writelines(rec_new)
    print ('\nВаш счет записан.')
    f.close()
def open_records():
    f = open('records.txt', 'r', encoding = 'utf-8')
    rec = f.readlines()
    print ('\nВот полный список рекордов: ')
    print(rec)
    f.close()
def main():
    trivia_file = open_file('Викторина.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    category, question, answers, correct, nominal, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range (4):
            print('\t', i+1, '-', answers[i])
        answer = input('Ваш ответ: ')
        if answer == correct:
            print('\nДа!', end=' ')
            nominal = int(nominal)
            score += nominal
        else:
            print('\nНет...')
        print(explanation)
        print('Счет: ', score, '\n\n')
        category, question, answers, correct, nominal, explanation = next_block(trivia_file)
    trivia_file.close()
    print('Это был последний вопрос...')
    print('На Вашем счету', score)
    name = input('Введите имя: ')
    records(name, score)
    open_records()

main ()
input('\n\nPress Enter to escape')
    
