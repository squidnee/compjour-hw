# The number of proposed U.S. federal regulations 
# in which comments are due within the next 3 days.

import requests as r
import bs4
url = r.get('http://www.regulations.gov/#!searchResults;rpp=25;po=0;cs=3;dct=N%/252BFR%/252BPR')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("div h1")[0].text
print(select)