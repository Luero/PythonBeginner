# "Кто твой папа?"
# Пользователь вводит имя человека, а программа называет отца этого человека.
# Есть возможность добавлять, заменять и удалять пары "сын/дочь - отец"
# Created by Luero. 23/05/2022

book = {"Ксюша" : "Геннадий",
        "Стас" : "Сергей",
        "Оксана" : "Алексей",
        "Настя" : "Евгений"}
print ('В данной прорамме содержится информация об именах отцов.')
choice = None
while choice != "0":
    print ("""
            Выход - нажмите 0.
            Узнать имя отца - нажмите 1.
            Заменить имя отца - нажмите 2.
            Создать новую пару - нажмите 3.
            Удалить пару - нажмите 4. """)
    choice = input ('\nВведите Ваш выбор: ')
    if choice == "1":
        name = input ('\nВведите имя: ')
        name = name.title()
        if name in book:
            print ('Имя отца ', book.get(name))
        else:
            print ('Имени отца этого человека нет в справочнике.')
    elif choice == "2":
        name = input ('\nВведите имя: ')
        name = name.title()
        if name in book:
            newName = input ('Введите новое имя отца:')
            book[name] = newName
            print ('Добавлена новая информация об имени отца ', name)
        else:
            print ('Такого имени нет в справочнике')
    elif choice == "3":
        name = input ('\nДля кого Вы хотите добавить информацию об отце?')
        name = name.title()
        if name not in book:
            fatherName = input ('Введите имя отца')
            book[name] = fatherName
            print ('Информация об отце для ', name, 'добавлена')
        else:
            print ('Такое имя уже есть, дайте другое имя.')
    elif choice == "4":
        name = input ('Информацию о каком имени Вы хотите удалить?')
        name = name.title()
        if name in book:
            del book[name]
            print ('Информация об отце для ', name, 'удалена.')
        else:
            print ('Такого имени нет в справочнике.')
    else:
        print ('Введите допустимое значение выбора из меню.')
print ('До встречи!')
input ('\nPress Enter to escape')
