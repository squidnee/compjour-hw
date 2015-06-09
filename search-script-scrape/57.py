# The number of comments posted to the regulation that is currently at the top of 
# Regulations.gov's "What's Trending" list.

# Note: currently not working.

import requests as r
import bs4
url = r.get('http://www.regulations.gov/#!docketDetail;D=APHIS-2014-0098')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("h2")[0]
print(select.text)