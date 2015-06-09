# The latest release date for T-100 Domestic Market (U.S. Carriers) statistics report

import requests as r
import bs4
url = r.get('http://www.transtats.bts.gov/airports.asp')
soup = bs4.BeautifulSoup(url.text)
count=0
select = soup.select("select#End_YearMonth option.selected")
for s in select:
	count+=1
print(select[count].text)