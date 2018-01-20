import flask
from flask import request
from flask import make_response
import plazapp

@plazapp.app.route('/')
def show_login():
	payload = {}
	payload['test'] = 'yo'
	response = make_response(flask.render_template("index.html", **payload))
	response.set_cookie('read', 'nah')
	return response
