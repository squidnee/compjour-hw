# Total number of clinical trials as recorded by the National Institutes of Health.

import bs4
import requests as r
data = r.get('https://clinicaltrials.gov/')
soup = bs4.BeautifulSoup(data.text)
trials = soup.select("span.highlight")[0]
print(trials.text)