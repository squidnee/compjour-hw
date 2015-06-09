# The title of the most recent decision handed down by the U.S. Supreme Court.

import requests as r
import bs4
url = r.get('http://www.supremecourt.gov/')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div.panel.panel-scus-two div.panel-body div.recentdecisions ul li a")[0]
print(select.text)