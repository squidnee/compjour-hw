# The number of workplace fatalities at reported 
# to the federal and state OSHA in the latest fiscal year.

import requests as r
import bs4
url = r.get('https://www.osha.gov/dep/fatcat/dep_fatcat.html')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("h5")[1].text
print(select)