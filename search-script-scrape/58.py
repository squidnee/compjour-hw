# The number of published research papers from the NSA.

import requests as r
import bs4
url = r.get('https://www.nsa.gov/research/publications/')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("table.dataTable tr")
count = 0
for s in select:
	count += 1
print(count)