import requests
import json
url = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'
data = json.loads(requests.get(url).text)
quakes = data['features']

########
# Task A
print('A.', data['metadata']['title'])

########
# Task B
print("B.", data['metadata']['count'])

########
# Task C
print("C.", max([q['properties']['mag'] for q in quakes]))

########
# Task D
print("D.", len([q for q in quakes if q['properties']['tsunami'] == 1]))

########
# Task E
def get_mag(quake):
	return quake['properties']['mag']

q = min(quakes, key = get_mag)
print("E.", q['properties']['title'])

########
# Task F
def get_title(quake):
	return quake['properties']['felt']

q = max(quakes, key = get_title)
print("F.", q['properties']['title'])

########
# Task G
import time
qsecs = [q['properties']['time'] / 1000 for q in quakes]
qsecs = sorted(qsecs, reverse = True)
tsec = qsecs[0]
timeobj = time.gmtime(tsec)
print("G.", time.strftime('%Y-%m-%d %H:%M', timeobj))

########
# Task H
qsecs = sorted(qsecs, reverse = False)
tsec = qsecs[0]
timeobj = time.gmtime(tsec)
print("H.", time.strftime('%A, %B %d', timeobj))

########
# Task I
tobjs = [time.gmtime(s) for s in qsecs]
wdays = [s.tm_wday for s in tobjs]
x = [d for d in wdays if d in range(0, 6)]
print("I.", len(x))

########
# Task J
hours = [s.tm_hour for s in tobjs]
x = [h for h in hours if h in range(5, 9)]
print("J.", len(x))

########
# Task K
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat /2 ) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers.
    return c * r

def distance_from_stanford(quake):
    stanford_lng = -122.166
    stanford_lat = 37.424
    coords = quake['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]
    return haversine(lng, lat, stanford_lng, stanford_lat)

q = max(quakes, key = distance_from_stanford)
print('K.', q['properties']['title'])

########
# Task L
def distance_from_paris(quake):
	paris_lng = -0.8655079999999999
	paris_lat = 44.562918
	coords = quake['geometry']['coordinates']
	lng = coords[0]
	lat = coords[1]
	return haversine(lng, lat, paris_lng, paris_lat)

q = max(quakes, key = distance_from_paris)
print("L.", q['properties']['title'])

########
# Task M
basemap_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400'
markers_str = 'markers=color:orange'
for q in quakes:
	coords = q['geometry']['coordinates']
	lng = str(coords[0])
	lat = str(coords[1])
	s = '%7C' + lat + ',' + lng
	markers_str += s

print("M.", basemap_url + '&' + markers_str)

########
# Task N
markers_str2 = 'markers=color:red'
coords = [q['geometry']['coordinates'] for q in quakes if q['properties']['mag'] > 6]
lng = str(coords[0])
lat = str(coords[1])
s = '%7C' + lat + ',' + lng
markers_str2 += s

print("N.", basemap_url + '&' + markers_str2)