import json
with open("data-hold/domestic-jobcount.json") as f:
	dom_data = json.loads(f.read())

mylist = []
for d in dom_data:
	if (d[1] < 100):
		mylist.append(d)

mysort = sorted(mylist)
for m in mysort:
	print(m[0] + "," + str(m[1]))