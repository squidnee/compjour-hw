# Number of FOIA requests made to the Chicago Public Library.

import requests as r
import json
url = r.get('https://data.cityofchicago.org/resource/n379-5uzu.json')
print(len(json.loads(url.text)))