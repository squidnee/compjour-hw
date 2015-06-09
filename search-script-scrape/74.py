# The description of the bill most recently signed into law by the governor of Georgia.

import requests as r
import bs4
url = r.get('http://gov.georgia.gov/bills-signed/2015')
soup = bs4.BeautifulSoup(url.text)
select = soup.select('table')[0].select('td')[1].text
print(select)