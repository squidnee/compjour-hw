# The current humidity level at Great Smoky Mountains National Park.

import requests as r
import json
url = r.get('http://api.wunderground.com/api/f73aadbe8067d45a/conditions/q/37738.1.99999.json')
data = json.loads(url.text)
print(data['current_observation']['relative_humidity'])