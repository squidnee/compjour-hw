# In the current dataset behind Medicare's Nusring Home Compare website, 
# the total amount of fines received by penalized nursing homes.

import requests as r
import json
url = r.get('https://data.medicare.gov/resource/t8q7-k6ku.json')
data = json.loads(url.text)
total = 0
for d in data:
	total += float(d['total_amount_of_fines_in_dollars'])
print(total)