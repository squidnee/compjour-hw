import json
import os
import requests
usajobs_url = "https://data.usajobs.gov/api/jobs"
codes_url = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
sdata = requests.get(codes_url).json()
mylist = []
for d in sdata:
	sname = d
	atts = {'CountrySubDivision': sname, 'NumberOfJobs': 1}
	resp = requests.get(usajobs_url, params = atts)
	data = resp.json()
	jobcount = int(data['TotalJobs'])
	mylist.append([sname, jobcount])

os.makedirs("data-hold", exist_ok = True)
f = open("data-hold/domestic-jobcount.json", 'w')
f.write(json.dumps(mylist, indent = 2))
f.close()