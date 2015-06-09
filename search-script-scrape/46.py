# The number of Pinterest accounts maintained by U.S. State Department
# embassies and missions.

import bs4
import requests as r
url = r.get('http://www.state.gov/r/pa/ode/socialmedia/')
soup = bs4.BeautifulSoup(url.text)
pinterest = soup.select("tbody tr td")[0]
print(pinterest.text)