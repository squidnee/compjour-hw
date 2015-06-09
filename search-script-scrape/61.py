# The number of miles traveled by the current U.S. Secretary of State.

import requests as r
import bs4
url = r.get('http://www.state.gov/secretary/travel/index.htm')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div.travel-wrap li#total-mileage span")[0].text
print(select)