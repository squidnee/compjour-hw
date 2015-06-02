import json
import requests
import os

data = '../data/pizza_request_dataset.json'

def load():
	f = json.loads(open(os.path.join(os.path.dirname(__file__), data)))
	return f

def post_upvotes():
	return 0

def post_downvotes():
	return 0

def user_upvotes():
	return 0

def num_chars():
	return 0

def edited():
	return false

def num_posts():
	return 0

def age():
	return 0