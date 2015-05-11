import json
from operator import itemgetter
with open("sample-geochart-2.html") as f:
	html = f.read()
with open("data-hold/intl-jobcount.json") as f:
	data = json.loads(f.read())

chartdata = [['Country', 'Jobs']]
chartdata.extend(d for d in data if d[1] > 1)
table = []
for c in chartdata:
	table.append("<tr><td>%s</td><td>%s</td></tr>" % (c[0], c[1]))

table = "\n".join(table)

with open("2-8.html", 'w') as f:
	html = html.replace('#CHART_DATA#', str(chartdata))
	html = html.replace('#TABLE_ROWS#', table)
	f.write(html)