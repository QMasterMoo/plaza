import flask
from flask import request
from flask import make_response
import plazapp

@plazapp.app.route('/')
def show_index():
	payload = {}
	payload['test'] = 'yo'
	response = make_response(flask.render_template("index.html", **payload))
	response.set_cookie('read', 'nah')
	return response

@plazapp.app.route('/', methods=['post'])
def show_index_post():
	payload = {}
	post_data = request.form

	response = make_response(flask.render_template("index.html", **payload))
	response.set_cookie('read', 'yeah')

	return response
