# Программа "Счет, пожалуйста!"
# Показывает меню с блюдами и ценами, принимает заказ и выводит на экран сумму счета
# Created by Luero, 03/07/2022

from tkinter import *

class Application(Frame):

    MENU = [("Оливье", "250", "р."), ("Мимоза", "300", "р."), ("Сельдь под шубой", "350", "р."), ("Цезарь", "280", "р.")]
    SOUPS = [("Солянка", "300", "р."), ("Борщ", "300", "р."), ("Лапша куриная", "250", "р.")]
    DISHES = [("Шашлык", "350", "р."), ("Котлета куриная", "200", "р."), ("Судак под маринадом", "250", "р.")]

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
               
    def create_widgets(self):
        
        Label(self,
              text = 'Меню',
              font = ('Helvetica', 12, 'bold'),
              fg = 'dark blue').grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = 'Салаты',
              font = ('Helvetica', 10, 'bold')).grid(row = 1, column = 0, sticky = W)        
        row = 2
              
        items = []

        for item in range(len(Application.MENU)):            
            self.item = BooleanVar()
            Checkbutton(self,
                        text = Application.MENU[item][0],
                        variable = self.item).grid(row = row, column = 0, sticky = W)
            Label(self,
                  text = Application.MENU[item][1] + Application.MENU[item][2]).grid(row = row, column = 2, sticky = W)
            row += 1
            items.append(self.item)

        Label(self,
              text = 'Супы',
              font = ('Helvetica', 10, 'bold')).grid(row = 7, column = 0, sticky = W)        
        row = 8
        soups = []

        for soup in range(len(Application.SOUPS)):
            self.soup = BooleanVar()
            Checkbutton(self,
                        text = Application.SOUPS[soup][0],
                        variable = self.soup).grid(row = row, column = 0, sticky = W)
            Label(self,
                  text = Application.SOUPS[soup][1] + Application.SOUPS[soup][2]).grid(row=row, column = 2, sticky = W)
            row += 1
            soups.append(self.soup)
     
        Label(self,
              text = 'Горячее',
              font = ('Helvetica', 10, 'bold')).grid(row = 11, column = 0, sticky = W)        
        row = 12
        dishes = []

        for dish in range (len(Application.DISHES)):
            self.dish = BooleanVar()
            Checkbutton(self,
                        text = Application.DISHES[dish][0],
                        variable = self.dish).grid(row = row, column = 0, sticky = W)
            Label(self,
                  text = Application.DISHES[dish][1]+ Application.DISHES[dish][2]).grid(row = row, column = 2, sticky = W)
            row += 1
            dishes.append(self.dish)
             
        Button(self,
               text = 'Заказать',
               command = lambda: self.order(items, soups, dishes)).grid(row = 15, column = 0, sticky = W)
        Label(self,
              text = 'Ваш заказ',
              font = ('Helvetica', 10, 'bold'),
              fg = 'dark blue').grid(row = 3, column = 4, sticky = W)
        self.check_order = Text(self, width = 30, height = 15, wrap = WORD, padx = 3, font = ('Helvetica', 10))
        self.check_order.grid(row = 4, column = 4, columnspan = 3,  rowspan = 8)
        Label(self,
              text = 'Ваш счет: ',
              font = ('Helvetica', 10, 'bold'),
              fg = 'dark blue').grid(row = 12, column = 4, sticky = W)
        self.bill = Entry(self, bg = 'light blue', font = ('Helvetica', 10))
        self.bill.grid(row = 12, column = 5, sticky = W)

    def order(self, items, soups, dishes):       
        
        order = ''
        summa = 0
        for self.item in items:    
            if self.item.get() == True:
                code = items.index(self.item)
                order += Application.MENU[code][0]
                order += '\n'
                price = int(Application.MENU[code][1])
                summa += price
        for self.soup in soups:            
            if self.soup.get() == True:
                code = soups.index(self.soup)
                order += Application.SOUPS[code][0]
                order += '\n'
                price = int(Application.SOUPS[code][1])
                summa += price
        for self.dish in dishes:            
            if self.dish.get() == True:
                code = dishes.index(self.dish)
                order += Application.DISHES[code][0]
                order += '\n'
                price = int(Application.DISHES[code][1])
                summa += price
        self.check_order.delete(0.0, END)
        self.check_order.insert(0.0, order)
        self.bill.delete(0, END)
        self.bill.insert(0, summa)

root = Tk()
root.title('Кафе "Снежинка"')
app = Application (root)
root.mainloop()
            
            
            
