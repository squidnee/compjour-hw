import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json'
data = json.loads(requests.get(data_url).text)

hashtag_objs = data['entities']['hashtags']
hashtag_texts = []
for h in hashtag_objs:
    hashtag_texts.append(h['text'])

url_objs = data['entities']['urls']
url_links = []
for u in url_objs:
	url_links.append(u['display_url'])

print('A.', data['created_at'])
print('B.', data['user']['created_at'])
print('C.', data['text'])
print('D.', data['user']['screen_name'])
print('E.', data['id'])
print('F.', str(len(data['entities']['user_mentions'])))
print('G.', ','.join(hashtag_texts))
print('H.', ','.join(url_links))