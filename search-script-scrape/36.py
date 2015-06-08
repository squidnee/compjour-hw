# Total number of visitors to the White House in 2012.

import csv
import requests as r
from io import StringIO
url = 'http://www.whitehouse.gov/sites/default/files/disclosures/whitehouse-waves-2012.csv'
resp = r.get(url)
data = csv.DictReader(StringIO(resp.text))
rows = list(data)
visitors = len([r for r in rows])
print(visitors)