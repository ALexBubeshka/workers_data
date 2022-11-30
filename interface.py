from easygui import *
import sys
from reading_json import data
from del_json import *
import searching_json
from adding_employees import building_adding_json
from log import *


fieldValues = None
exempl_1 = None
new_employee = None
def start_interface ():
    logging.info('Запущен главный экран приложения')
    msg = "Добро пожаловать в базу данных работников\nВыберете один из пунктов"
    title = 'База данных работников'
    choices = ['Вывести полную базу данных','Добавление работника в базу данных','Удаление работника из базы данных','Отбор по критериям']
    choice = choicebox(msg, title, choices)
    choice_interface(choice)
    return str(choice)

def choice_interface(choice):
    try:
        global fieldValues
        global exempl_1
        global new_employee
        if choice == 'Вывести полную базу данных':
            logging.info('Выбран пунк - Вывести полную базу данных')
            message = json.dumps(data, indent=4, sort_keys=True)
            title = 'Полная база данных'
            output = ynbox(message, title, ("Да", "Нет"))
            if output:
                choice_interface(start_interface())
            else:
                sys.exit
        elif choice == 'Добавление работника в базу данных':
            logging.info('Выбран пунк - Добавление работника в базу данных')
            message = 'Заполните поля'
            title = 'Новый работник'
            fieldNames = ['ФИО','Пол','Дата рождения','Семейное положение','Должность','Зарплата','Телефон']
            fieldValues = multenterbox(message,title,fieldNames)
            new_employee = fieldValues
            if fieldValues is None:
                choice_interface(start_interface())
            while 1:
                errmsg = ""
                for i, name in enumerate(fieldNames):
                    if fieldValues[i].strip() == "":
                        errmsg += "Необходимо заполнить поле {}\n\n".format(name)
                        logging.warning('Заполнены не все поля')
                if errmsg == "":
                    break
                fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
                if fieldValues is None:
                    break
            building_adding_json(new_employee)
            logging.warning(f'Добавлен новый работник -{new_employee}')
            message = "Новый работник{}".format(fieldValues) + "\nХотите еще добавить работников?"
            title = 'Добавление работника в базу данных'
            output = ynbox(message,title,("Да","Нет"))
            if output:
                choice_interface('Добавление работника в базу данных')
            else:
                choice_interface(start_interface())
            choice_interface(start_interface())
        elif choice == 'Удаление работника из базы данных':
            logging.info('Выбран пунк - Удаление работника из базы данных')
            message = 'Введите ФИО работника'
            title = 'Удаление работника из базы данных'
            d_text = ''
            output = enterbox(message, title, d_text)
            exempl_1 = output
            if output:
                del_el(exempl_1)
                logging.warning(f'Удален из базы {output}')
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
            logging.info('Выбран пунк - Отбор по критериям')
            message = 'Заполните поля'
            title = 'Отбор по критериям'
            fieldNames = ['ФИО','Пол','Дата рождения','Семейное положение','Должность','Зарплата','Телефон']
            fieldValues = multenterbox(message,title,fieldNames)
            fieldValues = [x for x in fieldValues if x]
            str(fieldValues)
            if fieldValues is None:
                choice_interface(start_interface())
            else:
                searching_json.searching_el(fieldValues)
                logging.info(f'Выведен список - {json.dumps(searching_json.results, indent=4)}')
                message = json.dumps(searching_json.results, indent=4) + "\nХотите еще раз найти?"
                title = 'Отбор по критериям'
                output = ynbox(message,title,("Да","Нет"))
                if output:
                    choice_interface('Отбор по критериям')
                else:
                    choice_interface(start_interface())
    except:
        logging.error('Программа не запустилась')