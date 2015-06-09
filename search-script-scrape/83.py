# The sum of White House staffermember salaries in 2014.

import json
import requests as r
url = r.get('https://open.whitehouse.gov/resource/bjhy-fcuv.json')
data = json.loads(url.text)
salary = 0
for d in data:
	salary += float(d['salary'])
print(salary)