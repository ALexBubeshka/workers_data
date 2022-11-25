from easygui import *
import sys
from reading_json import data
from del_json import *

fieldNames = None
exempl_1 = None
def start_interface ():
    msg = "Добро пожаловать в базу данных работников\nВыберете один из пунктов"
    title = 'База данных работников'
    choices = ['Вывести полную базу данных','Добавление работника в базу данных','Удаление работника из базы данных','Отбор по критериям','Поиск']
    choice = choicebox(msg, title, choices)
    return str(choice)

def choice_interface(choice):
    global fieldNames
    global exempl_1
    if choice == 'Вывести полную базу данных':
        message = data
        title = 'Полная база данных'
        output = ynbox(message,title,("Да","Нет"))
        if output:
            choice_interface(start_interface())
        else:
            sys.exit
    elif choice == 'Добавление работника в базу данных':
        message = 'Заполните поля'
        title = 'Новый работник'
        fieldNames = ['ФИО','Пол','Дата рождения','Семейное положение','Телефон','Должность','Зарплата']
        fieldValues = multenterbox(message,title,fieldNames)
        if fieldValues is None:
            choice_interface(start_interface())
        while 1:
            errmsg = ""
            for i, name in enumerate(fieldNames):
                if fieldValues[i].strip() == "":
                    errmsg += "Необходимо заполнить поле {}\n\n".format(name)
            if errmsg == "":
                break
            fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
            if fieldValues is None:
                break
        print("Новый работник{}".format(fieldValues))
        msgbox('Работник добавлен')
        choice_interface(start_interface())
    elif choice == 'Удаление работника из базы данных':
        message = 'Введите ФИО работника'
        title = 'Удаление работника из базы данных'
        d_text = ''
        output = enterbox(message, title, d_text)
        exempl_1 = output
        if output:
            del_el(exempl_1)
            message = str(output) +"\nХотите еще одного работника удалить из базы данных?"
            title = 'Удаление'
            output = ynbox(message,title,("Да","Нет"))
            if output:
                choice_interface('Удаление работника из базы данных')
            else:
                choice_interface(start_interface())
        else:
            choice_interface(start_interface())
    elif choice == 'Отбор по критериям':
        message = 'Выберете один или несколько критерий отбора'
        title = 'Отбор по критериям'
        fieldNames = ['ФИО','Пол','Дата рождения','Семейное положение','Телефон','Должность','Зарплата']
        fieldValues = multchoicebox(message,title,fieldNames)
        if fieldValues is None:
            choice_interface(start_interface())
    elif choice == 'Поиск':
        message = 'Введите что нужно найти'
        title = 'Поиск'
        d_text = ''
        output = enterbox(message,title,d_text)
        if output:
            message = str(output) +"\nХотите еще что-либо найти?"
            title = 'Поиск'
            output = ynbox(message,title,("Да","Нет"))
            if output:
                choice_interface('Поиск')
            else:
                choice_interface(start_interface())
        else:
            choice_interface(start_interface())

choice_interface(start_interface())