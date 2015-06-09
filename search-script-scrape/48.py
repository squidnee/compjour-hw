# The difference in total White House staffmember salaries in 2014 versus 2010.

import requests as r
import json
url14 = r.get('https://open.whitehouse.gov/resource/bjhy-fcuv.json')
url10 = r.get('https://open.whitehouse.gov/resource/rcp4-3y7g.json')

json14 = json.loads(url14.text)
json10 = json.loads(url10.text)

salary14 = 0
for j in json14:
	salary14 += float(j['salary'])
total14 = salary14

salary10 = 0
for k in json10:
	salary10 += float(k['salary'])
total10 = salary10

print(total14 - total10)