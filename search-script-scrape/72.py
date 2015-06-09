# The number of magnitude 4.5+ earthquakes detected worldwide by the USGS.

import requests as r
import json
url = r.get('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson')
data = json.loads(url.text)
print(data['metadata']['count'])