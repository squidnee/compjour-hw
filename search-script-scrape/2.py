# The name of the most recently added dataset on data.gov.

import bs4
import requests
response = requests.get('http://www.data.gov/')
soup = bs4.BeautifulSoup(response.text)
link = soup.select("article header h2.entry-title a")[0]
print(link.text)