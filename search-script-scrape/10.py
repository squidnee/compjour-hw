# The title of the highest paid California city government position in 2010

import csv
csv_path = './static/2010_StateDepartment.csv'
csv_file = open(csv_path, 'r')
csv_data = list(csv.DictReader(csv_file))
print(csv_data)