import json
from log import *

data = ''
def reading_json():
    try:  
        global data
        with open('employees.json', 'r') as file:
            data = json.load(file)
            for k, v in data.items():
                print(k, v)
        with open('employees.json', 'w')as f:
            json.dump(data, f, indent=4)
    except:
        logging.error('Error',exc_info=True)  

reading_json()
