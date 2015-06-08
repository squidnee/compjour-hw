# The number of women currently serving in the U.S. Congress,
# according to Sunlight Foundation data.

import csv
import requests
from io import StringIO
CSVURL = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
response = requests.get(CSVURL)
data = csv.DictReader(StringIO(response.text))
rows = list(data)
women = len([i for i in rows if i['gender'] == 'F' and i['in_office'] == '1'])
print(women)