import json
from log import *

results = {}
temp_1 = {}
temp_2 = {}
temp_3 = {}
temp_4 = {}
temp_5 = {}
temp_6 = {}
temp_7 = {}
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