import requests
url = "https://data.usajobs.gov/api/jobs"
states = sorted(['California', 'Florida', 'New York', 'Maryland'])
t = 0
state_data = list()

for s in states:
	atts = {"CountrySubdivision": s, "NumberOfJobs": 1}
	response = requests.get(url, params = atts)
	data = response.json()
	jobs = (data['TotalJobs'])
	state_data += [[s, jobs]]
	
print(state_data)