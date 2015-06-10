import json
import requests
import os

def get_data():
	data_path = '../data/pizza_request_dataset.json'
	read_data = open(os.path.join(os.path.dirname(__file__), data_path))
	data = json.loads(read_data.read())
	return data

def best_user(data):
	gifted = {}
	most_gifted = []
	for d in data:
		user = d['giver_username_if_known']
		if d['requester_received_pizza']:
			if user != 'N/A':
				if user in gifted:
					gifted[user] += 1
				else:
					gifted[user] = 1
				if gifted[user] >= 3:
					if user not in most_gifted:
						most_gifted.append(user)
	return most_gifted