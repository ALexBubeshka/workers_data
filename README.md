Программа для обработки и хранения данных работников предприятия.
==================================
Всем привет. Рад Вам представить нашу программу по решению проблем с хранением данных по работникам на предприятии. Программа написана с использованием графического интерфейса - EasyGUI. Данные всех сотрудних хранятся в JSON формате, что позволяет с легкотью использовать не только в данной программе.

<a href="https://files.fm/f/4zb6bgpyp"><img src="https://files.fm/thumb_show.php?i=4zb6bgpyp"></a>

Установка EasyGUI:
-------------
1.Запустить программу “командная строка” (cmd.exe)

2.Ввести команду - pip install easygui

    >>> pip install easygui
    
Блок по выводу полной базы данных
---------------------------------

<a href="https://files.fm/f/s25z6hhk7"><img src="https://files.fm/thumb_show.php?i=s25z6hhk7"></a>

Выводится вся база данных которая записана в JSON

        message = json.dumps(data,indent=4,sort_keys=True)
        title = 'Полная база данных'
        output = ynbox(message,title,("Да","Нет"))


Блок по добавлению работника в базу данных
------------------------------------------

<a href="https://files.fm/f/39qx39tg4"><img src="https://files.fm/thumb_show.php?i=39qx39tg4"></a>

Отработка интерфейса

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
            message = "Новый работник{}".format(fieldValues) + "\nХотите еще раз найти?"
            title = 'Добавление работника в базу данных'
            output = ynbox(message,title,("Да","Нет"))
            if output:
                choice_interface('Добавление работника в базу данных')
            else:
                choice_interface(start_interface())
            choice_interface(start_interface())



Блок по удалению работника из базы данных
-----------------------------------------

<a href="https://files.fm/f/qry2szk33"><img src="https://files.fm/thumb_show.php?i=qry2szk33"></a>

Отработка интерфейса

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


Блок по отбору информации по критериям
---------------------------------------

<a href="https://files.fm/f/argbs5ve2"><img src="https://files.fm/thumb_show.php?i=argbs5ve2"></a>

Отработка интерфейса

      elif choice == 'Отбор по критериям':
            message = 'Заполните поля'
            title = 'Новый работник'
            fieldNames = ['ФИО','Пол','Дата рождения','Семейное положение','Телефон','Должность','Зарплата']
            fieldValues = multenterbox(message,title,fieldNames)
            if fieldValues is None:
                choice_interface(start_interface())

Над проектом работали
---------------------------------------
Руткевич Вадим (https://github.com/vad1m24) Бубешко Александр (https://github.com/ALexBubeshka)
