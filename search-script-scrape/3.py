# The number of people who visited a U.S. government website using Internet Explorer 6.0
# in the past 90 days.

import json
import requests
response = requests.get('https://analytics.usa.gov/data/live/browsers.json')
data = json.loads(response.text)
visitors = data['totals']['browser']['Internet Explorer']
print(visitors)