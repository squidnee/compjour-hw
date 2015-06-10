from flask import Flask, abort, render_template, request, redirect
from controllers import index_controller as i
from controllers import sends_controller as s
from urllib.parse import quote_plus, unquote_plus
import json

app = Flask(__name__)

data = i.get_data()

def total_items(data):
	items = list(data)
	return len(items)

def get_success_rate(data):
	success = sum([d['requester_received_pizza'] for d in data])
	rate = 100.0 * (success / len(list(data)))
	return rate

items = total_items(data)
rate = get_success_rate(data)
@app.route("/")
def index():
	return render_template('index.html', data=data, items=items, rate=rate)

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
	return redirect("/%s" % path)

@app.route("/posts/")
def posts():
	temp = "posts.html"
	html = open("./templates/posts.html").read()
	post_status = i.post_status(data)

	filtered = []

	for suc in post_status[0]:
		filtered.append([1, suc])

	for fail in post_status[1]:
		filtered.append([0, fail])

	chartdata = []
	chartdata.extend(filtered)
	with open("./templates/posts.html", 'w') as f:
		html = html.replace('#CHART_DATA#', str(chartdata))
		f.write(html)
	return render_template(temp, data=data, items=items, rate=rate)

@app.route("/karma/")
def karma():
	temp = "karma.html"
	html = open("./templates/karma.html").read()
	karma = i.user_karma(data)

	filtered = []

	for suc in karma[0]:
		filtered.append([1, suc])

	for fail in karma[1]:
		filtered.append([0, fail])

	chartdata = []
	chartdata.extend(filtered)
	with open("./templates/karma.html", 'w') as f:
		html = html.replace('#CHART_DATA#', str(chartdata))
		f.write(html)
	return render_template(temp, data=data, items=items, rate=rate)

@app.route("/chars/")
def chars():
	temp = "chars.html"
	chars = i.num_chars_in_post(data)
	html = open("./templates/chars.html").read()

	filtered = []

	for suc in chars[0]:
		filtered.append([1, suc])

	for fail in chars[1]:
		filtered.append([0, fail])

	chartdata = []
	chartdata.extend(filtered)
	with open("./templates/chars.html", 'w') as f:
		html = html.replace('#CHART_DATA#', str(chartdata))
		f.write(html)
	return render_template(temp, data=data, chars=chars, items=items, rate=rate)

@app.route("/edited/")
def edited():
	temp = "edited.html"
	edited = i.edited(data)
	html = open("./templates/edited.html").read()

	filtered = []

	for suc in edited[0]:
		filtered.append([1, suc])

	for fail in edited[1]:
		filtered.append([0, fail])

	chartdata = []
	chartdata.extend(filtered)
	with open("./templates/edited.html", 'w') as f:
		html = html.replace('#CHART_DATA#', str(chartdata))
		f.write(html)
	return render_template(temp, data=data, items=items, rate=rate)

@app.route("/age/")
def age():
	temp = "age.html"
	age = i.acc_age(data)
	html = open("./templates/age.html").read()

	filtered = []

	for suc in age[0]:
		filtered.append([1, suc])

	for fail in age[1]:
		filtered.append([0, fail])

	chartdata = []
	chartdata.extend(filtered)
	with open("./templates/age.html", 'w') as f:
		html = html.replace('#CHART_DATA#', str(chartdata))
		f.write(html)
	return render_template(temp, data=data, items=items, rate=rate)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)