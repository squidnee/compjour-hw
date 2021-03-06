# The non-profit organization with the highest total revenue,
# according to the latest listing in ProPublica's Nonprofit Explorer.

import requests as r
import json
atts = {'order': 'revenue', 'sort_order': 'desc'}
response = r.get('https://projects.propublica.org/nonprofits/api/v1/search.json', params=atts)
data = json.loads(response.text)
print(data['filings'][0]['organization']['name'])