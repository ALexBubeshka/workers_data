import json

results = {}
temp_1 = {}
temp_2 = {}
temp_3 = {}
temp_4 = {}
temp_5 = {}
temp_6 = {}
temp_7 = {}
def searching_el(fieldValues):
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

def searching_el_2(fieldValues):
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


'''                    results[k] = v
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

    

def correction(fieldValues):

    for k, v in results.items():
        for j in range(len(results)):
            if fieldValues[j] not in results.values():
                del results[k]
                correction(fieldValues)
            break
        break'''


#                if fieldValues[j] not in data:
 #                   while j < len(fieldValues):
  #                      if fieldValues[j] not in data:
   #                         if j + 1 < len(fieldValues):
    #                            j += 1
     #                       else:
      #                          break
       #                 else:
        #                    results[k] = v
         #           i += 1
          #      else:
           #         results[k] = v


#def building_serch_result_json():
 #   with open('serch_result', 'w') as file:
  #      json.dump(results, file, indent=4)


#            print(k)
#    searching_el(fieldValues)
