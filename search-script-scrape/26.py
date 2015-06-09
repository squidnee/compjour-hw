# The dropout rate for all of Santa Clara County high schools, 
# according to the latest cohort data in CALPADS.

import requests as r
import bs4
url = r.get('http://dq.cde.ca.gov/dataquest/cohortrates/GradRates.aspx?cds=43000000000000&TheYear=2013-14&Agg=O&Topic=Dropouts&RC=County&SubGroup=Ethnic/Racial')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("tr")[1].select("td")[6].text
print(select)