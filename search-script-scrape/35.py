# Most viewed data set on New York state's open data portal as of this month.

import requests as r
import bs4
url = r.get('https://data.ny.gov/browse')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div.titleLine span")[0].text
print(select)