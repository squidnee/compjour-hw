import json
import requests
import os

def get_data():
	data_path = '../data/pizza_request_dataset.json'
	read_data = open(os.path.join(os.path.dirname(__file__), data_path))
	data = json.loads(read_data.read())
	return data

def post_status(data):
	success = []
	fail = []
	for d in data:
		up = int(d['number_of_upvotes_of_request_at_retrieval'])
		down = int(d['number_of_downvotes_of_request_at_retrieval'])
		votes = (up - down)
		if d['requester_received_pizza'] == True:
			success.append(votes)
		else:
			fail.append(votes)
		total = [sorted(success, reverse=False), sorted(fail, reverse=True)]
	return total

def user_karma(data):
	success = []
	fail = []
	for d in data:
		karma = int(d['requester_upvotes_minus_downvotes_at_request'])
		if d['requester_received_pizza'] == True:
			success.append(karma)
		else:
			fail.append(karma)
		total = [sorted(success, reverse=False), sorted(fail, reverse=True)]
	return total

def num_chars_in_post(data):
	success = []
	fail = []
	for d in data:
		chars = len(d['request_text'])
		if d['requester_received_pizza']:
			success.append(chars)
		else:
			fail.append(chars)
		total = [sorted(success, reverse=False), sorted(fail, reverse=False)]
	return total

def edited(data):
	success = []
	fail = []
	for d in data:
		if d['requester_received_pizza']:
			if d['post_was_edited']:
				success.append(0)
			else:
				success.append(1)
		else:
			if d['post_was_edited']:
				fail.append(0)
			else:
				fail.append(1)
		total = [sorted(success, reverse=False), sorted(fail, reverse=False)]
	return total

def acc_age(data):
	success = []
	fail = []
	for d in data:
		age = int(d['requester_account_age_in_days_at_request'])
		if d['requester_received_pizza']:
			success.append(age)
		else:
			fail.append(age)
		total = [sorted(success, reverse=False), sorted(fail, reverse=False)]
	return total