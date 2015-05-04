import requests
url = "https://data.usajobs.gov/api/jobs"
countries = ['China', 'South Africa', 'Tajikistan']
t = 0

for c in countries:
	atts = {"Country": c, "NumberOfJobs": 1}
	response = requests.get(url, params = atts)
	data = response.json()
	jobs = (c, data['TotalJobs'])
	print('%s has %s job listings.' %(jobs))
	t = t + int(data['TotalJobs'])

print('Together, they have %s total job listings.' %(t))