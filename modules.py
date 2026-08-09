import sys

#   - sys
#     - version  - python version
#     - platform - operating system
#     - exit()   - stop program
#     - argv     - command line argument
#     - path     - module search path

# print(sys.version)
# print(sys.platform)
# # sys.exit()  # stop program
# print(sys.argv)
# print(sys.path)


#   - json
#     - dumps    - json string
#     - loads    - json string to python
#     - dump     - save json to file
#     - load     - read json from file

import json
JSON_PATH = r'C:\Users\Parveen\Desktop\python_projects\python_series\python_practise\data.json'

with open(JSON_PATH, 'r') as file:
    data = json.load(file)
    print(data)


import csv
CSV_PATH = r'C:\Users\Parveen\Desktop\python_projects\python_series\python_practise\data.csv'

with open(CSV_PATH, 'r') as file:
    data = csv.reader(file)
    print(list(data))


# datetime -- datetime,date,timedelta
#     - datetime.now   - current date/time
#     - date.today     - current date
#     - timedelta      - Add/Substract Days
#     - strftime       - format date
#     - strptime       - convert string to date

import datetime
print(datetime.datetime.now())
print(datetime.date.today())
