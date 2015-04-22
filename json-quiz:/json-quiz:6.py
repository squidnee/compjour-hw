import requests
import json
import os

url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"
text = requests.get(url).text

if os.path.exists(tempfilename):
	tfile = open(tempfilename, "r")
	j = tfile.read()
else:
	j = text
	tfile = open(tempfilename, "w")
	tfile.write(j)

	tfile.close()
	accounts = json.loads(j)

############
## Task A ##

total = str(len(accounts['urls']))
print("A.", total)

############
## Task B ##

x = 0
for a in accounts:
	if a['followers_count'] > 10000:
		x += 1

print("B.", x)

############
## Task C ##



############
## Task D ##

counts = []
for a in accounts:
	counts.append(a['followers_count'])
maxval = sorted(counts, reverse = True)[0]
print("D.", maxval)

############
## Task E ##



############
## Task F ##

from operator import itemgetter