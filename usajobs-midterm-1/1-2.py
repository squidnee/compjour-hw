import requests
data_url = "https://data.usajobs.gov/api/jobs"
states = ['Alaska', 'Hawaii']
t = 0

for s in states:
	atts = {"CountrySubdivision": s, "NumberOfJobs": 1}
	response = requests.get(data_url, params = atts)
	data = response.json()
	jobs = (s, data['TotalJobs'])
	print('%s has %s job listings.' %(jobs))
	t = t + int(data['TotalJobs'])


print('Together, they have %s total job listings.' %(t))