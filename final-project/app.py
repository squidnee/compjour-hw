from flask import Flask, abort, render_template, request, redirect
from controllers import index_controller as i
from controllers import sends_controller as s
from urllib.parse import quote_plus, unquote_plus
import json

app = Flask(__name__)

data = index_controller.get_data()

def total_items(data):
	items = list(data)
	return len(items)

def get_success_rate(data):
	success = sum([d['requester_received_pizza'] for d in data])
	rate = 100.0 * (success / len(list(data)))
	return rate

@app.route("/")
def index():
	post_status = i.post_status(data)
	karma = i.user_karma(data)
	chars = i.num_chars_in_post(data)
	edited = i.edited(data)
	age = i.acc_age(data)
	items = total_items(data)
	rate = get_success_rate(data)
	return render_template('index.html', data=data, post_status=post_status, karma=karma,
		chars=chars, edited=edited, age=age, items=items, rate=rate)

## NOTE: This page is not technically part of my final project...consider it something that
## I'd like to finish up when I have a wee bit more time on my hands. Essentially, I'd like to take
## the top most 'altruistic' users on the subreddit (aka the ones who have contributed 3 or more pizzas,
## with each pizza going to a unique user) and then collecting information on each user to see if we can learn
## more about altruistically-inclined people, based on the subreddits they follow, number of upvotes they have, etc.
def sends():
	best_user = s.best_user(data)
	return render_template('sends.html', best_user=best_user)

@app.route("/search", methods=['POST'])
def search():
	search_query = request.form.get('query')
	path = quote_plus(search_query)
	return redirect("/query/%s" % path)

@app.route("/query/<query>")
def results(query):
	return render_template('results.html')

@app.route('/<row_id>/')
def success(row_id):
	return

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)