# The number of people on FBI's Most Wanted List for white collar crimes.

import requests as r
import bs4
url = r.get('http://www.fbi.gov/wanted/wcc/@@wanted-group-listing')
soup = bs4.BeautifulSoup(url.text)
count = 0
select = soup.select("div.wanted-person-container-wrapper")
for s in select:
	count+=1
print(count)