import json
from operator import itemgetter
with open("data-hold/intl-jobcount.json") as f:
	intl_data = json.loads(f.read())

mylist = []
sum = 0
for i in intl_data:
	mylist.append(i)

mysortedlist = sorted(mylist, key = itemgetter(1), reverse = True)

for m in mysortedlist:
	if (m[1] >= 13):
		print(m[0] + ',' + str(m[1]))
	else:
		sum += m[1]

print("Others," + str(sum))