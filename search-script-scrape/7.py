# The number of listed federal executive agency internet domains.

import csv
import requests
response = requests.get('https://inventory.data.gov/dataset/fe9eeb10-2e90-433e-a955-5c679f682502/resource/b626ef1f-9019-41c4-91aa-5ae3f7457328/download/federalexecagncyintntdomains03302015.csv')
reader = csv.DictReader(response.text.splitlines())
data = list(reader)
print(len(data))