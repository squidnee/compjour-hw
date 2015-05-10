import json
with open("data-hold/intl-jobcount.json") as f:
	intl_data = json.loads(f.read())

mylist = []
for i in intl_data:
	if (i[1] > 10):
		mylist.append(i)

mysortedlist = []
from operator import itemgetter
mysortedlist += sorted(mylist, key=itemgetter(1))

for s in mysortedlist:
	print(s[0] + ',' + str(s[1]))