# The number of people on FBI's Most Wanted List for white collar crimes.

import requests as r
import bs4
url = r.get('http://www.fbi.gov/wanted/wcc/@@wanted-group-listing')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div.wanted-person-container-wrapper")
s = list(select)
print(len(s))