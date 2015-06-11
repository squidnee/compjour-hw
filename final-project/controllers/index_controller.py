import json
import requests
import os

def get_data():
	data_path = '../data/pizza_request_dataset.json'
	read_data = open(os.path.join(os.path.dirname(__file__), data_path))
	data = json.loads(read_data.read())
	return data

def post_status(data):
	success = {}
	fail = {}
	for d in data:
		up = int(d['number_of_upvotes_of_request_at_retrieval'])
		down = int(d['number_of_downvotes_of_request_at_retrieval'])
		votes = (up - down)
		if d['requester_received_pizza'] == True:
			if str(votes) in success:
				success[str(votes)] += 1
			else:
				success[str(votes)] = 1
		else:
			if votes in fail:
				fail[str(votes)] += 1
			else:
				fail[str(votes)] = 1

		total = [success, fail]
	return total

def user_karma(data):
	success = {'7500+':0, '500-7500':0, '200-500':0, '0-200':0}
	fail = {'7500+':0, '500-7500':0, '200-500':0, '0-200':0}
	for d in data:
		karma = int(d['requester_upvotes_minus_downvotes_at_request'])
		if d['requester_received_pizza'] == True:
			if karma > 7500:
				success['7500+'] += 1;
			elif karma > 500:
				success['500-7500'] += 1;
			elif karma > 200:
				success['200-500'] += 1;
			else:
				success['0-200'] += 1;
		else:
			if karma > 7500:
				fail['7500+'] += 1;
			elif karma > 500:
				fail['500-7500'] += 1;
			elif karma > 200:
				fail['200-500'] += 1;
			else:
				fail['0-200'] += 1;

	success_array = []
	fail_array = []
	for k in success:
		success_array.append([k, success[k]])
	for k in fail:
		fail_array.append([k, fail[k]])
	total = [success_array, fail_array]
	return total
print(user_karma(get_data()))

def num_chars_in_post(data):
	success = {'1000+':0, '500-1000':0, '200-500':0, '0-200':0}
	fail = {'1000+':0, '500-1000':0, '200-500':0, '0-200':0}
	for d in data:
		chars = len(d['request_text'])
		if d['requester_received_pizza']:
			if chars > 1000:
				success['1000+'] += 1;
			elif chars > 500:
				success['500-1000'] += 1;
			elif chars > 200:
				success['200-500'] += 1;
			else:
				success['0-200'] += 1;
		else:
			if chars > 1000:
				fail['1000+'] += 1;
			elif chars > 500:
				fail['500-1000'] += 1;
			elif chars > 200:
				fail['200-500'] += 1;
			else:
				fail['0-200'] += 1;

	success_array = []
	fail_array = []
	for k in success:
		success_array.append([k, success[k]])
	for k in fail:
		fail_array.append([k, fail[k]])
	total = [success_array, fail_array]
	return total

def edited(data):
	success_e = []
	success = []
	fail_e = []
	fail = []
	for d in data:
		if d['requester_received_pizza']:
			if d['post_was_edited']:
				success_e.append(0)
			else:
				success.append(0)
		else:
			if d['post_was_edited']:
				fail_e.append(0)
			else:
				fail.append(0)
		total = [len(success_e), len(success), len(fail_e), len(fail)]
	return total

def acc_age(data):
	success = {'0-10': 0, '10-50': 0, '50-250': 0, '250-1000':0, '1000+': 0}
	fail = {'0-10': 0, '10-50': 0, '50-250': 0, '250-1000':0, '1000+': 0}
	for d in data:
		age = int(d['requester_account_age_in_days_at_request'])
		if d['requester_received_pizza']:
			if age > 1000:
				success['1000+'] += 1;
			elif age > 250:
				success['250-1000'] += 1;
			elif age > 50:
				success['50-250'] += 1;
			elif age > 10:
				success['10-50'] += 1;
			else:
				success['0-10'] += 1;
		else:
			if age > 1000:
				fail['1000+'] += 1;
			elif age > 250:
				fail['250-1000'] += 1;
			elif age > 50:
				fail['50-250'] += 1;
			elif age > 10:
				fail['10-50'] += 1;
			else:
				fail['0-10'] += 1;

	success_array = []
	fail_array = []
	for k in success:
		success_array.append([k, success[k]])
	for k in fail:
		fail_array.append([k, fail[k]])
	total = [sorted(success_array), sorted(fail_array)]
	return total