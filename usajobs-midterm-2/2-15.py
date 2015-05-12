import json
import os
import requests
from operator import itemgetter

with open("sample-geochart-cities.html") as f:
	html = f.read()

CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jdata = json.loads(rawdata)
jobs = jdata['jobs']

def get_ca_cities(job):
	cali_cities = []
	location = job['Locations']
	for l in location:
		if "California" in l.lower():
			cali_cities += l

num_cityjobs = {}

for job in jobs:
	city = get_ca_cities(job)
	if city in num_cityjobs:
		num_cityjobs[city] += 1
	else:
		if city is not None:
			num_cityjobs[city] = 1

chartdata = []
table = []
for n in num_cityjobs:
	chartdata.append([n[0], n[1]])
	table.append([n[0], n[1]])

sort = sorted(num_cityjobs, key = itemgetter(1), reverse = True)
for s in sort:
	table.append("<tr><td>%s</td><td>%s</td></tr>" % (s[0], s[1]))

table = "\n".join(table)

with open("2-15.html", 'w') as f:
    html = html.replace("#CHART_DATA#", str(chartdata)) 
    html = html.replace("#TABLE_ROWS#", table)
    f.write(html)