import json
from operator import itemgetter
with open("sample-barchart-2.html") as f:
	html = f.read()
with open("data-hold/domestic-jobcount.json") as f:
	data = json.loads(f.read())

sort = sorted(data, key=itemgetter(1), reverse = True)

chartdata = [['State', 'Jobs']]
chartdata.extend(sort[0:10])
table = []
for s in sort:
	table.append("<tr><td>%s</td><td>%s</td></tr>" % (s[0], s[1]))

table = "\n".join(table)

with open("2-7.html", 'w') as f:
	html = html.replace('#CHART_DATA#', str(chartdata))
	html = html.replace('#TABLE_ROWS#', table)
	f.write(html)