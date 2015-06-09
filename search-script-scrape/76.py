# The total number of publications produced by the U.S. Government Accountability Office.

import requests as r
import bs4
url = r.get('http://www.gao.gov/browse/date/custom?adv_begin_date=&adv_end_date=mm%2Fdd%2Fyyyy&all=')
soup = bs4.BeautifulSoup(url.text)
select = soup.select("h2.scannableTitle")[0].text.split()
print(select[8])