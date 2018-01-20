import flask
import plazapp
from plazapp.model import test

@plazapp.app.route('/')
def show_index():
	payload = {}
	return flask.render_template("index.html", **payload)
