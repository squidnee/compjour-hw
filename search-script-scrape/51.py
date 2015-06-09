# The title of the most recent decision handed down by the U.S. Supreme Court.

import requests as r
import bs4
url = r.get('http://www.supremecourt.gov/opinions/slipopinions.aspx')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("table td")[5]
print(select.text)