# The number of university-related datasets currently listed at data.gov.

import bs4
import requests as r
url = r.get('http://catalog.data.gov/dataset?q=university')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div.new-results")[0].text
print(select)