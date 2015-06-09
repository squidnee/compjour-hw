# The number of international travel alerts from the U.S. State Department
# currently in effect.

import requests as r
import bs4
url = r.get('http://travel.state.gov/content/passports/english/alertswarnings.html')
soup = bs4.BeautifulSoup(url.text)
select = soup.select('td.alert')
s = list(select)
print(len(s))