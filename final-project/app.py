import controller
from flask import flask
from flask import abort
from flask import render_template
app = Flask(__name__)

bool success = true
bool fail = false

@app.route("/")
def index():
	data = controller.load()
	layout = 'index.html'
	return render_template(layout, data=data)

## Still figuring out what to put here. Will be updated soon. ##
@app.route('/<row_id>/')
def success(row_id):
	return

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)