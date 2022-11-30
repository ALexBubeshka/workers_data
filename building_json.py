from db import employees
import json
from log import *

def building_first_json():
    try:
        with open('employees.json', 'w') as db:
            json.dump(employees, db, indent=4)
    except:
        logging.error('Error',exc_info=True)

building_first_json()