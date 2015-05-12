import requests
api_url = "https://data.usajobs.gov/api/jobs"
resp = requests.get(api_url, 
	params = 
	{'CountrySubDivision': 'California', 'NumberOfJobs': 250})
data = resp.json()

dict = {}

for job in data['JobData']:
	org = job['OrganizationName']
	if org in dict:
		dict[org] += 1
	else:
		dict[org] = 1
print(dict)
	