from flask import Flask, abort, render_template, request, redirect
from controllers import index_controller, sends_controller

app = Flask(__name__)

bool success = true
bool fail = false

@app.route("/")
def index():
	data = controller.load()
	return render_template('index.html', data=data)

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