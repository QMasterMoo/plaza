import flask
from flask import request, make_response, redirect
import plazapp
from plazapp.do_login_things import hash_password
from plazapp.model import check_hash, get_uid, create_user

@plazapp.app.route('/register.html')
def show_register():
	# Grab cookies
	log_status = request.cookies.get('loggedin')
	# Redirect if already logged in
	if log_status == "yes":
		return redirect("/", code=302)

	payload = {}
	response = make_response(flask.render_template("register.html", **payload))
	return response

@plazapp.app.route('/register.html', methods = ["POST"])
def show_register_post():
	# Grab cookies
	log_status = request.cookies.get('loggedin')
	# Redirect if already logged in
	if log_status == "yes":
		return redirect("/", code=302)

	# Grab login data
	username = flask.request.values.get('username')
	password = flask.request.values.get('password')

	hash_tup = hash_password(username, password)
	maybe_uid = get_uid(username)


	payload = {}
	# Make sure the user doesn't already exist
	if maybe_uid == None:
		response = redirect("/", code=302)
		response.set_cookie('loggedin', 'yes')
		#insert user
		create_user(username, hash_tup[1], hash_tup[0])
		uid = get_uid(username)
		response.set_cookie('uid', str(uid))
		return response
	# Redirect to index
	return redirect("/register.html", code=302)