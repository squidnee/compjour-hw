# Percentage of NYPD stop-and-frisk reports in which the suspect was white in 2014.

import requests as r
import bs4
url = r.get('http://www.nyclu.org/content/stop-and-frisk-data').text
soup = bs4.BeautifulSoup(url)
data = soup.select("div.margins li")[12].text.splitlines()
print(data[4])