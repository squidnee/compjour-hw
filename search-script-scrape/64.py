# from March 1 to 7, 2015, the number of times in which designated
# FDA policy makers met with persons outside the U.S. federal executive branch.

import requests as r
import bs4
url = r.get('http://www.fda.gov/NewsEvents/MeetingsConferencesWorkshops/PastMeetingsWithFDAOfficials/ucm439318.htm')
soup = bs4.BeautifulSoup(url.text)
select = soup.select('h4')
s = list(select)
print(len(s))