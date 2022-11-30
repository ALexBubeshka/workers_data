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

      def building_adding_json(new_employee):
      try:
            keys = []
            with open('employees.json', 'r') as file:
                  data = json.load(file)
                  for k, v in data.items():
                  keys.append(k)
            new_empl_key = int(keys[-1]) + 1
      except:
            logging.error('Error',exc_info=True)

      casted_phones = [int(item) for item in new_employee[6].split(sep=",")]
      information = {'Full name': new_employee[0], 'Sex': new_employee[1], 'Birth date': new_employee[2],
                        'Marital status': new_employee[3], 'Job title': new_employee[4], 'salary': int(new_employee[5]),
                        'Phone numbers': casted_phones}
      data[new_empl_key] = information

      with open('employees.json', 'w')as file:
            json.dump(data, file, indent=4)



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