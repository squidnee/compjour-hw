# Number of days until Texas's next scheduled execution.

import requests as r
import bs4
from datetime import date, datetime
url = r.get('http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html').text
soup = bs4.BeautifulSoup(url)
select = soup.select("tr td")[0].text
print(select)