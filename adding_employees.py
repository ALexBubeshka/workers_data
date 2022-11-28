from db import employees
import json



def building_adding_json(new_employee):

    keys = []
    with open('employees.json', 'r') as file:
        data = json.load(file)
        for k, v in data.items():
            keys.append(k)
    new_empl_key = int(keys[-1]) + 1
    print(new_empl_key)

    data[employees][new_empl_key]['Full name'].append(new_employee[0])
    data[new_empl_key]['Sex'].append(new_employee[1])
    data[new_empl_key]['Birth date'].append(new_employee[2])
    data[new_empl_key]['Marital status'].append(new_employee[3])
    data[new_empl_key]['Job title'].append(new_employee[4])
    data[new_empl_key]['salary'].append(new_employee[5])
    data[new_empl_key]['Phone numbers'].append(new_employee[6])

    print(data)

    with open('employees.json', 'w')as file:
        json.dump(data, file, indent=4)





#    print(data)

#    with open('employees.json', 'w')as file:
#        json.dump(data, file, indent=4)
 #   t1 = ()
'''    data[new_empl_key] = str('{'
                             '"Full name": "'+ new_employee[0] +'",'
                             '"Sex": "'+ new_employee[1] +'",'
                             '"Birth date": "'+ new_employee[2] +'",'
                             '"Marital status": "'+ new_employee[3] +'",'
                             '"Job title": "'+ new_employee[4] +'",'
                              '"salary": "'+ new_employee[5] +'"}')'''



    # data.update({new_empl_key:{v['Full name']:new_employee[0], v['Sex']:new_employee[1], v['Birth date']:new_employee[2], v['Marital status']:new_employee[3], v['Job title']:new_employee[4], v['salary']:new_employee[5], v['Phone numbers']:new_employee[6]}})


#    data[employees][new_empl_key] = str(v['Full name'] == new_employee[0]), v['Sex'] == new_employee[1], v['Birth date'] == new_employee[2], v['Marital status'] == new_employee[3], v['Job title'] == new_employee[4], v['salary'] == new_employee[5], v['Phone numbers'] == new_employee[6]



    #with open('employees.json', 'w')as file:
     #   json.dump(data, file, indent=4)
'''    data[str(new_empl_key)]['Full name'].append(str(new_employee[0]))
    data[str(new_empl_key)]['Sex'] = str(new_employee[1])
    data[str(new_empl_key)]['Birth date'] = str(new_employee[2])
    data[str(new_empl_key)]['Marital status'] = str(new_employee[3])
    data[str(new_empl_key)]['Job title'] = str(new_employee[4])
    data[str(new_empl_key)]['salary'] = str(new_employee[5])
    data[str(new_empl_key)]['Phone numbers'] = str(new_employee[6])

    print(data)

    with open('employees.json', 'w')as file:
        json.dump(data, file, indent=4)'''



