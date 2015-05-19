# The number of librarian-related job positions that the federal government
# is currently hiring for.

import requests
url = "https://data.usajobs.gov/api/jobs?Title=Librarian'"
resp = requests.get(url)
librarianjobs = resp.json()
print(librarianjobs['TotalJobs'])