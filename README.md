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
Для добавления нового работника необходимо заполнить все поля. Если одно или несколько полей будут не заполнены, то программа попрости их заполнить.

<a href="https://files.fm/f/39qx39tg4"><img src="https://files.fm/thumb_show.php?i=39qx39tg4"></a>

Отработка кода

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
Для удаления необходимо ввести полностью ФИО работника.

<a href="https://files.fm/f/qry2szk33"><img src="https://files.fm/thumb_show.php?i=qry2szk33"></a>

Отработка кода

    def del_el(exempl_1):
    try:
        global del_element
        with open('employees.json', 'r') as file:
            data = json.load(file)
            for k, v in data.items():
                if v['Full name'] == exempl_1:
                    del data[k]
                    break
        with open('employees.json', 'w')as file:
            json.dump(data, file, indent=4)
    except:
        logging.error('Error',exc_info=True)


Блок по отбору информации по критериям
---------------------------------------
Можно сразу вводить несколько критериев отбора или остановиться на одном. 

<a href="https://files.fm/f/argbs5ve2"><img src="https://files.fm/thumb_show.php?i=argbs5ve2"></a>

Отработка кода

      def searching_el(fieldValues):
    try:
        global results
        with open('employees.json', 'r') as file:
            data = json.load(file)
            for k, v in data.items():
                for i in range(len(fieldValues)):
                    if v['Full name'] == fieldValues[i]:
                        results[k] = v
                    elif v['Sex'] == fieldValues[i]:
                        results[k] = v
                    elif v['Birth date'] == fieldValues[i]:
                        results[k] = v
                    elif v['Marital status'] == fieldValues[i]:
                        results[k] = v
                    elif v['Job title'] == fieldValues[i]:
                        results[k] = v
                    elif str(v['salary']) == fieldValues[i]:
                        results[k] = v
                    elif str(v['Phone numbers'][0]) == fieldValues[i]:
                        results[k] = v
                    elif str(v['Phone numbers'][1]) == fieldValues[i]:
                        results[k] = v
            searching_el_2(fieldValues)
    except:
        logging.error('Error',exc_info=True)
    def searching_el_2(fieldValues):
    try:
        global results
        for k, v in results.items():
            i = 0
            if v['Full name'] == fieldValues[i] or v['Sex'] == fieldValues[i] or v['Birth date'] == fieldValues[i] or v['Marital status'] == fieldValues[i] or v['Job title'] == fieldValues[i] or str(v['salary']) == fieldValues[i] or str(v['Phone numbers'][0]) == fieldValues[i] or str(v['Phone numbers'][1]) == fieldValues[i]:
                temp_1[k] = v
        if len(fieldValues) > 1:
            fieldValues.pop(0)
            for k, v in temp_1.items():
                i = 0
                if v['Full name'] == fieldValues[i] or v['Sex'] == fieldValues[i] or v['Birth date'] == fieldValues[i] or v['Marital status'] == fieldValues[i] or v['Job title'] == fieldValues[i] or str(v['salary']) == fieldValues[i] or str(v['Phone numbers'][0]) == fieldValues[i] or str(v['Phone numbers'][1]) == fieldValues[i]:
                    temp_2[k] = v
            if len(fieldValues) > 1:
                fieldValues.pop(0)
                for k, v in temp_2.items():
                    i = 0
                    if v['Full name'] == fieldValues[i] or v['Sex'] == fieldValues[i] or v['Birth date'] == fieldValues[i] or v['Marital status'] == fieldValues[i] or v['Job title'] == fieldValues[i] or str(v['salary']) == fieldValues[i] or str(v['Phone numbers'][0]) == fieldValues[i] or str(v['Phone numbers'][1]) == fieldValues[i]:
                        temp_3[k] = v
                if len(fieldValues) > 1:
                    fieldValues.pop(0)
                    for k, v in temp_3.items():
                        i = 0
                        if v['Full name'] == fieldValues[i] or v['Sex'] == fieldValues[i] or v['Birth date'] == fieldValues[i] or v['Marital status'] == fieldValues[i] or v['Job title'] == fieldValues[i] or str(v['salary']) == fieldValues[i] or str(v['Phone numbers'][0]) == fieldValues[i] or str(v['Phone numbers'][1]) == fieldValues[i]:
                            temp_4[k] = v
                    if len(fieldValues) > 1:
                        fieldValues.pop(0)
                        for k, v in temp_4.items():
                            i = 0
                            if v['Full name'] == fieldValues[i] or v['Sex'] == fieldValues[i] or v['Birth date'] == fieldValues[i] or v['Marital status'] == fieldValues[i] or v['Job title'] == fieldValues[i] or str(v['salary']) == fieldValues[i] or str(v['Phone numbers'][0]) == fieldValues[i] or str(v['Phone numbers'][1]) == fieldValues[i]:
                                temp_5[k] = v
                        if len(fieldValues) > 1:
                            fieldValues.pop(0)
                            for k, v in temp_5.items():
                                i = 0
                                if v['Full name'] == fieldValues[i] or v['Sex'] == fieldValues[i] or v['Birth date'] == fieldValues[i] or v['Marital status'] == fieldValues[i] or v['Job title'] == fieldValues[i] or str(v['salary']) == fieldValues[i] or str(v['Phone numbers'][0]) == fieldValues[i] or str(v['Phone numbers'][1]) == fieldValues[i]:
                                    temp_6[k] = v
                        else:
                            results = temp_5
                    else:
                        results = temp_4
                else:
                    results = temp_3
            else:
                results = temp_2
        else:
            results = temp_1
    except:
        logging.error('Error',exc_info=True)
        
        
Блок по логированию
-------------------
    logging.basicConfig(
    level=logging.DEBUG,
    filename = "mylog.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

Над проектом работали
---------------------------------------
Руткевич Вадим (https://github.com/vad1m24) Бубешко Александр (https://github.com/ALexBubeshka)
