import json
import requests
import os
cali_data = 'data-hold/california.json'
if not os.path.exists(cali_data):
	print("Can't find", cali_data, "so fetching remote copy...")
	resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
	f = open(cali_data, 'w')
	f.write(resp.text)
	f.close()
rawdata = open(cali_data).read()
jobs = json.loads(rawdata)['jobs']

def cleanmoney(val):
	x = val.replace('$', '').replace(',', '')
	return float(x)

def cleansalarymax(job):
	return cleanmoney(job['SalaryMax'])

sortjobs = sorted(jobs, key = cleansalarymax, reverse = True)

for job in sortjobs[0:5]:
	print('%s,%d,%d' % (job['JobTitle'], cleanmoney(job['SalaryMin']),
		cleanmoney(job['SalaryMax'])))