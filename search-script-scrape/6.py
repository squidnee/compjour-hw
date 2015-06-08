# From 2010 to 2013, the change in median cost of health, dental, and 
# vision coverage for California city employees.

# NOTE: Currently has an error.

import requests as r
import bs4
url = r.get('http://gcc.sco.ca.gov/Reports/State/State.aspx?fiscalyear=2013&rpt=1&chart=1&trend=1')
soup = bs4.BeautifulSoup(url.text)
cost = soup.select("div.group div.row span.label")[1].text

url2 = r.get('http://gcc.sco.ca.gov/Reports/State/State.aspx?fiscalyear=2010&rpt=1&chart=1&trend=1')
soup2 = bs4.BeautifulSoup(url2.text)
cost2 = soup2.select("div.group div.row span.label")[1].text
print(int(cost) - int(cost2))
