# The highest salary possible for a White House staffmember in 2014.

import json
import requests as r
url = r.get('https://open.whitehouse.gov/resource/bjhy-fcuv.json')
data = json.loads(url.text)
print(data)