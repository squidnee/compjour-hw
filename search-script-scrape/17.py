# In the "Justice News" RSS feed maintained by the Justice Department, 
# the number of items published on a Friday.

import bs4
import requests as r
url = r.get('http://www.justice.gov/briefing-room')
soup = bs4.BeautifulSoup(url.text)
date = soup.select("div.view-content")
count = 0
for d in date:
	if d.text.find('Friday'):
		count+=1
print(count)