from easygui import *
import sys
from reading_json import data
from del_json import *
import searching_json
from adding_employees import building_adding_json

fieldValues = None
exempl_1 = None
new_employee = None
def start_interface ():
    msg = "Добро пожаловать в базу данных работников\nВыберете один из пунктов"
    title = 'База данных работников'
    choices = ['Вывести полную базу данных','Добавление работника в базу данных','Удаление работника из базы данных','Отбор по критериям']
    choice = choicebox(msg, title, choices)
    return str(choice)

def choice_interface(choice):
    global fieldValues
    global exempl_1
    global new_employee
    if choice == 'Вывести полную базу данных':
        message = json.dumps(data, indent=4, sort_keys=True)
        title = 'Полная база данных'
        output = ynbox(message, title, ("Да", "Нет"))
        if output:
            choice_interface(start_interface())
        else:
            sys.exit
    elif choice == 'Добавление работника в базу данных':
        message = 'Заполните поля'
        title = 'Новый работник'
        fieldNames = ['ФИО','Пол','Дата рождения','Семейное положение','Должность','Зарплата','Телефон']
        fieldValues = multenterbox(message,title,fieldNames)
        new_employee = fieldValues
#        building_adding_json(new_employee)
        if fieldValues is None:
            choice_interface(start_interface())
        while 1:
            building_adding_json(new_employee)
            errmsg = ""
            for i, name in enumerate(fieldNames):
                if fieldValues[i].strip() == "":
                    errmsg += "Необходимо заполнить поле {}\n\n".format(name)
            if errmsg == "":
                break
            fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
            if fieldValues is None:
                break
        message = "Новый работник{}".format(fieldValues) + "\nХотите еще добавить работников?"
        title = 'Добавление работника в базу данных'
        output = ynbox(message,title,("Да","Нет"))
        if output:
            choice_interface('Добавление работника в базу данных')
        else:
            choice_interface(start_interface())
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
        message = 'Заполните поля'
        title = 'Новый работник'
        fieldNames = ['ФИО','Пол','Дата рождения','Семейное положение','Должность','Зарплата','Телефон']
        fieldValues = multenterbox(message,title,fieldNames)
        fieldValues = [x for x in fieldValues if x]
        str(fieldValues)
        if fieldValues is None:
            choice_interface(start_interface())
        else:
            searching_json.searching_el(fieldValues)
            message = json.dumps(searching_json.results, indent=4) + "\nХотите еще раз найти?"
            title = 'Отбор по критериям'
            output = ynbox(message,title,("Да","Нет"))
            if output:
                choice_interface('Отбор по критериям')
            else:
                choice_interface(start_interface())

choice_interface(start_interface())