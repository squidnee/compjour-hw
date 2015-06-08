# The last time the CIA's Leadership page has been updated.

import requests as r
import bs4
url = r.get('https://www.cia.gov/about-cia/leadership')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div.documentByLine div")[2]
print(select.text)