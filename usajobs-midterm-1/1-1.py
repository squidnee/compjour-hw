import requests
base_url = "https://data.usajobs.gov/api/jobs"
state = 'New York'
atts = {"CountrySubdivision": state, 'NumberOfJobs': 1}
response = requests.get(base_url, params = atts)
data = response.json()
print("%s has %s job listings." %(state, data['TotalJobs']))