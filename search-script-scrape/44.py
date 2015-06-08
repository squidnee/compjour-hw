# Number of people visiting a U.S. government website right now.

import json
import requests as r
url = r.get('https://analytics.usa.gov/data/live/realtime.json')
data = json.loads(url.text)['data'][0]['active_visitors']
print(data)