# The highest minimum wage as mandated by state law.

import requests as r
import bs4
url = r.get('http://www.ncsl.org/research/labor-and-employment/state-minimum-wage-chart.aspx')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("tr td p")[23]
print(select.text)