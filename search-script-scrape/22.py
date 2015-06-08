# The names of the committees that Sen. Barbara Boxer currently serves on.

# Note: currently not working.

import requests as r
import bs4
url = r.get('http://www.senate.gov/general/committee_assignments/assignments.htm').text
soup = bs4.BeautifulSoup(url)
select = soup.select("td a")
for s in select:
	if s.text.find('Boxer'):
		print(s.select("tr a").text)