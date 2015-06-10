from flask import Flask, abort, render_template, request, redirect
from controllers import index_controller, sends_controller

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
	post_status = index_controller.post_status(data)
	karma = index_controller.user_karma(data)
	chars = index_controller.num_chars_in_post(data)
	edited = index_controller.edited(data)
	age = index_controller.acc_age(data)
	items = total_items(data)
	rate = get_success_rate(data)
	return render_template('index.html', data=data, post_status=post_status, karma=karma, chars=chars, edited=edited, age=age, items=items, rate=rate)

@app.route("/search", methods=['POST'])
def search():
	query = request.form.get('query')
	path = quote_plus(query)
	return redirect("/address/%s" % path)

@app.route("/index_results")

@app.route('/<row_id>/')
def success(row_id):
	return

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)