# The number of datasets currently listed on data.gov.

import bs4
import requests
response = requests.get('http://www.data.gov/')
soup = bs4.BeautifulSoup(response.text)
link = soup.select("small a")[0]
print(link.text)