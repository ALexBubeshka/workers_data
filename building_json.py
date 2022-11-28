from db import employees
import json
# from reading_json import reading_json

def building_first_json():

    with open('employees.json', 'w') as db:
        json.dump(employees, db, indent=4)
    print()
    # reading_json()

building_first_json()

