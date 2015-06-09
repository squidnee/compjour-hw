# The number of proposed U.S. federal regulations 
# in which comments are due within the next 3 days.

import requests as r
import json
url = r.get('http://api.data.gov:80/regulations/v3/documents.json?api_key=DEMO_KEY&countsOnly=1&rpp=1000&cs=3')
data = json.loads(url.text)
print(data['totalNumRecords'])