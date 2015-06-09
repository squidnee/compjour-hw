# The total number of notices published on the most recent date to the Federal Register.

import requests as r
import json
url = r.get('https://www.federalregister.gov/api/v1/articles?conditions%5Bpublication_date%5D%5Bis%5D=06%2F09%2F2015&conditions%5Btype%5D=NOTICE')
data = json.loads(url.text)
print(data['count'])