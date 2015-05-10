import json
import os
import requests
usajobs_url = "https://data.usajobs.gov/api/jobs"
codes_url = "http://stash.compjour.org/data/usajobs/CountryCode.json"
cdata = requests.get(codes_url).json()
mylist = []
for d in cdata['CountryCodes']:
	if d['Code'] != 'US' and d['Value'] != 'Undefined':
		cname = d['Value']
		atts = {'Country': cname, 'NumberOfJobs': 1}
		resp = requests.get(usajobs_url, params = atts)
		data = resp.json()
		jobcount = int(data['TotalJobs'])
		mylist.append([cname, jobcount])

os.makedirs("data-hold", exist_ok = True)
f = open("data-hold/intl-jobcount.json", 'w')
f.write(json.dumps(mylist, indent = 2))
f.close()