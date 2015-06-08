# The number of times when a New York heart surgeon's rate of patient deaths 
# for all cardiac surgical procedures was "significantly higher" than the statewide rate,
# according to New York state's analysis.

import json
import requests
response = requests.get('https://health.data.ny.gov/resource/dk4z-k3xb.json')
data = json.loads(response.text)
deaths = [d for d in data if d['comparison_results'].find('significantly higher') != -1]
print(len(deaths))
