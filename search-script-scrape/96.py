# The number of scheduled arguments according to the most recent
# U.S. Supreme Court argument calendar.

import requests as r
import bs4
url = r.get('http://www.supremecourt.gov/oral_arguments/argument_calendars.aspx')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div.dslist li a")
s = list(select)
print(len(s) / 2)