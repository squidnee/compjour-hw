import json
import os
import requests
from operator import itemgetter
from datetime import datetime

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

collection_date = datetime.strptime(jdata['date_collected'], '%Y-%m-%dT%H:%M:%S')

def cleanmoney(val):
	x = val.replace('$', '').replace(',', '')
	return float(x)

def cleansalarymax(job):
	return cleanmoney(job['SalaryMax'])

for job in jobs:
	expire_date = datetime.strptime(job['EndDate'], '%m/%d/%Y')
	daysleft = str(expire_date - collection_date)
	if (cleansalarymax(job) >= 90000):
		if daysleft < 5 and daysleft >= 0:
			print('%s,%s,%s' % (job['JobTitle'], daysleft, job['ApplyOnlineURL']))