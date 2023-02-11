# "Угадай число" с пользовательским интерфейсом
# Created by Luero, 03/07/2022

import random
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid() 
        self.secret = random.randint(1, 100)
        self.tries = 9        
        self.create_widgets()

    def create_widgets(self):        
        Label(self,
              text = 'Компьютер загадал натуральное число от 1 до 100.').grid(row = 0, column = 0, columnspan = 3, sticky = W)
        Label(self,
              text = 'Ваша задача - отгадать число за 10 попыток.').grid(row = 1, column = 0, columnspan = 2, sticky = W)
        Label(self,
              text = 'После каждой попытки будет выдаватться подсказка').grid(row = 2, column = 0, columnspan = 3, sticky = W)        
        Label(self,
              text = 'Ваше предположение: ').grid(row = 3, column = 0, sticky = W)
        self.guess = Entry(self)
        self.guess.grid(row = 3, column = 1, sticky = W)        
        Button(self,
               text = 'Отправить ответ',
               command = self.playing).grid(row = 3, column = 2, sticky = W)
        self.text = Text(self, width = 40, height = 20, wrap = WORD, spacing1 = 1, spacing2 = 2)
        self.text.grid(row = 4, column = 0, sticky = W)
          
    def update_forms(self):
        self.tries_count()
        self.guess = Entry(self)
        self.guess.grid(row = 3, column = 1, sticky = W)        
        Button(self,
               text = 'Отправить ответ',
               command = self.playing).grid(row = 3, column = 2, sticky = W)
        
    def tries_count(self):
        self.tries -= 1        

    def playing(self):            
        while self.tries > 0:            
            guess_f = self.guess.get()            
            self.text.insert(0.0, guess_f)            
            triesleft = 10 - self.tries
            i = int(guess_f)
            if i > self.secret:
                self.tries = str(self.tries)
                text = '\nПопробуй меньше...\n'
                text += 'У тебя осталось ' + self.tries + ' попыток.\n'
                self.tries = int(self.tries)
                self.text.insert(0.0, text)
                self.update_forms()
            elif i < self.secret:
                self.tries = str(self.tries)
                text = '\nПопробуй больше...\n'
                text += 'У тебя осталось ' + self.tries + ' попыток.\n'
                self.tries = int(self.tries)
                self.text.insert(0.0, text)
                self.update_forms()
            elif i == self.secret:
                self.guess.destroy()                
                triesleft = str(triesleft)
                text = 'Вы угадали, поздравляю! Вы справились за ' + triesleft + ' попыток.'
                self.text.delete(0.0, END)
                self.text.insert(0.0, text)
                break            
        if self.tries == 0:
            self.guess.destroy()            
            self.secret = str(self.secret)
            text = 'Game over! '
            text += '\nЯ загадал ' + self.secret
            self.text.delete(0.0, END)
            self.text.insert(0.0, text)
                

root = Tk()
root.title('Угадай число')
app = Application(root)
root.mainloop()
        

        
