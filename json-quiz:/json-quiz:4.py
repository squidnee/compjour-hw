import requests
import json

url = 'http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json'
data = json.loads(requests.get(url).text)
artists = data['artists'][0]['genres']

print('A.', str(len(data['artists'])))
print('B.', data['artists'][4]['name'])
print('C.', data['artists'][11]['followers']['total'])
print('D.', ', '.join(artists))
print('E.', data['artists'][19]['images'][0]['url'])