# The domain of the most visited U.S. government website right now.

import requests as r
import json
url = r.get('https://analytics.usa.gov/data/live/top-pages-realtime.json')
json = json.loads(url.text)
visited = json['data'][0]['page_title']
print(visited)