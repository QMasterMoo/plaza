import flask
from flask import request
from flask import make_response
import plazapp

@plazapp.app.route('/login.html')
def show_login():
	payload = {}
	response = make_response(flask.render_template("login.html", **payload))
	return response
