# The names of the committees that Sen. Barbara Boxer currently serves on.

# Note: currently not working.

import requests as r
import bs4
url = r.get('http://www.senate.gov/general/committee_assignments/assignments.htm')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("td a")
for s in select:
	if s.text.find('Boxer'):
		print(s.text)
	else:
		s.next_element