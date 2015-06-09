# The number of Government Accountability Office reports and testimonies
# on the topic of veterans

import requests as r
import bs4

url = r.get('http://www.gao.gov/browse/topic')
soup = bs4.BeautifulSoup(url.text)
select = soup.select('ul.column a')[30].next_element.next_element.next_element
print(select.text.strip("()"))