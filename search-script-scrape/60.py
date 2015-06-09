# Number of chapters in Title 20 (Education) of the United States Code.

# Note: currently not working.

import requests as r
import bs4
url = r.get('https://www.law.cornell.edu/uscode/text/20')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div#main supcontentreg ul li")[0]
print(select.text)