import flask
from flask import request, make_response, redirect
import plazapp
from plazapp.do_login_things import hash_password
from plazapp.model import check_hash, get_uid

@plazapp.app.route('/login.html')
def show_login():
	# Grab cookies
	log_status = request.cookies.get('loggedin')
	# Redirect if already logged in
	if log_status == "yes":
		return redirect("/", code=302)

	payload = {}
	response = make_response(flask.render_template("login.html", **payload))
	return response

@plazapp.app.route('/login.html', methods = ["POST"])
def show_login_post():
	# Grab cookies
	log_status = request.cookies.get('loggedin')
	# Redirect if already logged in
	if log_status == "yes":
		return redirect("/", code=302)

	# Grab login data
	username = flask.request.values.get('username')
	password = flask.request.values.get('password')

	hashword = hash_password(username, password)[1]

	hash_match = check_hash(username, hashword)

	payload = {}
	# Render pages
	if hash_match:
		response = redirect("/", code=302)
		response.set_cookie('loggedin', 'yes')
		# QUERY UID ON USERNAME
		uid = get_uid(username)
		response.set_cookie('uid', str(uid))
		return response
	# Redirect to index
	return redirect("/login.html", code=302)