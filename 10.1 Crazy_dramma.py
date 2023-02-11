# Программа "Сумашедший драмматург" (задание по переделке "Сумашедшего сказочника")
# Created by Luero, 27/06/2022

from tkinter import*

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = 'Введите данные для создания нового рассказа').grid(row = 0, column = 0, columnspan = 2, sticky = W)
        Label(self,
              text = 'Имя главного героя:').grid(row = 1, column = 0, sticky = W)
        self.hero_name = StringVar()
        self.hero_name.set(None)
        hero_names = ['Коля','Вася','Петя','Ваня']
        column = 0
        for name in hero_names:
            Radiobutton(self,
                        text = name,
                        variable = self.hero_name,
                        value = name).grid(row = 3, column = column, sticky = W)
            column +=1
        Label(self,
              text = 'Имя женщины').grid(row = 4, column = 0, sticky = W)
        self.woman_name = Entry(self)
        self.woman_name.grid(row = 4, column = 1, sticky = W)
        Label(self,
              text = 'Выберите одно или несколько прилагательных').grid(row = 5, column = 0, columnspan = 2, sticky = W)
        self.is_nice = BooleanVar()
        Checkbutton(self,
                    text = 'приятное',
                    variable = self.is_nice).grid(row = 5, column = 2, sticky = W)
        self.is_exciting = BooleanVar()
        Checkbutton(self,
                    text = 'волнующее',
                    variable = self.is_exciting).grid(row = 5, column = 3, sticky = W)
        self.is_wonderful = BooleanVar()
        Checkbutton(self,
                    text = 'завораживающее',
                    variable = self.is_wonderful).grid(row = 5, column = 4, sticky = W)
        Label(self,
              text = 'Выберите концовку').grid(row = 6, column = 0, sticky = W)
        happy_end = 'жили они долго и счастливо'
        not_happy_end = ', к сожалению, что-то пошло не так... Что ж, бывает.'
        self.ending1 = StringVar()
        self.ending1.set(None)
        Radiobutton(self,
                    text = 'Счастливый финал',
                    variable = self.ending1,
                    value = happy_end).grid(row = 6, column = 1, sticky = W)
        self.ending2 = StringVar()
        self.ending2.set(None)
        Radiobutton(self,
                    text = 'Не очень счастливый конец',
                    variable = self.ending2,
                    value = not_happy_end).grid(row = 6, column = 2, columnspan = 2, sticky = W)
        Button(self,
               text = 'Получить рассказ',
               command = self.tell_story).grid(row = 7, column = 0, sticky = W)
        self.story_txt = Text (self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 9, column = 0, columnspan = 5)

    def tell_story(self):
        hero_name = self.hero_name.get()
        woman_name = self.woman_name.get()
        adj = ''
        if self.is_nice.get():
            adj += 'приятное, '
        if self.is_exciting.get():
            adj += 'волнующее, '
        if self.is_wonderful.get():
            adj += 'завораживающее'
        ending = self.ending1.get() + self.ending2.get()
        story = 'Жил-был на свете ' + hero_name
        story += ', и очень ему хотелось любви.'
        story += ' Однажды, прогуливаясь в парке среди каштанов, ' + hero_name + ' увидел смеющуюся девушку.'
        story += ' И тогда ' + adj + ' чувство охватило нашего героя.'
        story += ' Он подошел к ней и сказал: "Именно о тебе я всегда мечтал! Как тебя зовут?"'
        story += ' Девушка ответила: "' + woman_name + '". '
        story += hero_name + ' сказал: "' + woman_name + ', за углом стоит мой мотоцикл, давай укатим с тобой в закат?"'
        story += ' Девушка задумалась, а внезапный вой сирены пожарной машины помешал автору услышать ее ответ...'
        story += ' Но я точно знаю, что в итоге ' + ending
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0,story)

root = Tk()
root.title('Сумашедший драматург')
app = Application(root)
root.mainloop()
