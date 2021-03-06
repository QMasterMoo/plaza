import flask
from flask import request
from flask import make_response, redirect
import plazapp
from plazapp.model import set_post

@plazapp.app.route('/makepost.html')
def show_makepost():
	payload = {}

	response = make_response(flask.render_template("makepost.html", **payload))

	return response

@plazapp.app.route('/makepost.html', methods=['POST'])
def show_makepost_post():
	payload = {}
	# INSERT INTO DB
	title = request.form['title']
	content = request.form['content']
	uid = request.cookies.get('uid')
	# Confirm user logged in
	if uid == None or uid == '0':
		response = redirect("/login.html", code=302)
	else:
		set_post(uid, title, content)
		response = redirect("/", 302)

	return response