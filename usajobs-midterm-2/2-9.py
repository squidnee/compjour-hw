import requests
api_url = "https://data.usajobs.gov/api/jobs"
resp = requests.get(api_url, 
	params = {"CountrySubDivision": 'California',
	'NumberofJobs': 250})
data = resp.json()

dict = {'Full-time': 0, 'Other': 0}
for job in data['JobData']:
	if 'full' in job['WorkSchedule'].lower():
		dict['Full-time'] += 1
	else:
		dict['Other'] += 1

print(dict)