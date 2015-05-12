import json
import os
import requests
from operator import itemgetter

cali_data = 'data-hold/california.json'
rawdata = open(cali_data).read()
jobs = json.loads(rawdata)['jobs']

def cleanmoney(val):
	x = val.replace('$', '').replace(',', '')
	return float(x)

def cleansalarymax(job):
	return cleanmoney(job['SalaryMax'])

salary_under = []
for job in jobs:
	if cleanmoney(job['SalaryMax']) < 100000:
		diff = cleansalarymax(job) - cleanmoney(job['SalaryMin'])
		salary_under += [job['JobTitle'], cleanmoney(job['SalaryMin']),
			cleansalarymax(job), diff]

sort = sorted(salary_under, key = itemgetter(2), reverse = True)
big_diff = sort[0]

print("%s,%s,%s" % (big_diff[0], big_diff[1], big_diff[2]))