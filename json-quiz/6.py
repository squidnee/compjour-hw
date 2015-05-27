import requests
import json
import os

url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"

if os.path.exists(tempfilename):
	tfile = open(tempfilename, "r")
	j = tfile.read()
else:
	j = requests.get(url).text
	tfile = open(tempfilename, "w")
	tfile.write(j)

tfile.close()
accounts = json.loads(j)

############
## Task A ##

total = len([a for a in accounts if a['id'] > 0])
print("A.", total)

############
## Task B ##

x = len([a for a in accounts if a['followers_count'] > 10000])
print("B.", x)

############
## Task C ##

x = 0
x = len([a for a in accounts if a['verified'] == True])
print("C.", x)

############
## Task D ##

counts = []
for a in accounts:
	counts.append(a['followers_count'])
maxval = max(counts)
print("D.", maxval)

############
## Task E ##

tweets = []
for a in accounts:
	tweets.append(a['statuses_count'])
maxval = sorted(tweets, reverse = True)[0]
print("E.", maxval)

############
## Task F ##

from operator import itemgetter
x = max(accounts, key = itemgetter('followers_count'))
print("F.", x['screen_name'], 'has', x['followers_count'], 'followers')

############
## Task G ##

x = len([a for a in accounts if a['verified'] == False])
y = max(accounts, key = itemgetter('statuses_count'))
print("G.", y['screen_name'], 'has', y['statuses_count'], 'tweets')

############
## Task H ##

total = sum([a['followers_count'] for a in accounts])
print('H.', round(total / len(accounts)))

############
## Task I ##

total = []
for a in accounts:
	total.append(a['followers_count'])
sort_total = sorted(total)
median = len(sort_total)
print('I.', sort_total[round((median-1)/2)])
