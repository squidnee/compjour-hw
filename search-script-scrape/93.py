# Number of Github repositories maintained by the GSA's 18F organization,
# as listed on Github.com.

import requests as r
import bs4
url = r.get('https://github.com/18F?page=13&query=&utf8=%E2%9C%93')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div.repo-list-item")[0]
s = list(select)
print(len(s) + (12*20))