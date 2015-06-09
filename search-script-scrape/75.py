# Total number of officer-involved shooting incidents listed 
# by the Philadelphia Police Department.

import requests as r
import bs4
url = r.get('https://www.phillypolice.com/ois/')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("tr td a")
s = list(select)
print(len(s))