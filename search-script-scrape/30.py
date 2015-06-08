# The total number of inmates executed by Florida since 1976.

import bs4
import requests
response = requests.get('http://www.dc.state.fl.us/oth/deathrow/execlist.html')
soup = bs4.BeautifulSoup(response.text)
print(len(soup.select('tr')))