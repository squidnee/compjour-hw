# Number of medical device recalls issued by the U.S. Food and Drug Administration in 2013.

import requests as r
import bs4
url = r.get('http://www.fda.gov/MedicalDevices/Safety/ucm384618.htm')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("table")[0]
s = list(select.select("tr"))
print(len(s))