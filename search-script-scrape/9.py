# The number of roll call votes that were rejected by a margin of less than 5 votes,
# in the first session of the U.S. Senate in the 114th Congress.

import requests as r
import xml.etree.ElementTree as e
xml = r.get('http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.xml').text
root = e.fromstring(xml)
count = 0
for r in root[3]:
	yes = r[5][0].text
	no = r[5][1].text
	if (int(yes) - int(no) <= 5):
		count+=1
print(count)