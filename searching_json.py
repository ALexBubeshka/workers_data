import json

def searching_el(fieldNames):
    with open('employees.json', 'r') as file:
        data = json.load(file)

        for k, v in data.items():
            if v['Full name"'] == fieldNames[0]:
                print(v['Full name'])

            if v['Sex'] == fieldNames[1]:
                print(v['Sex'])

            if v['Birth date'] == fieldNames[2]:
                print(v['Birth date'])

            if v['Marital status'] == fieldNames[3]:
                print(v['Marital status'])

            if v['Phone numbers'] == fieldNames[4]:
                print(v['Phone numbers'])

            if v['Job title'] == fieldNames[5]:
                print(v['Job title'])

            if v['salary'] == fieldNames[6]:
                print(v['salary'])