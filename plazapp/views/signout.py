import flask
from flask import request, make_response, redirect
import plazapp

@plazapp.app.route('/signout.html')
def show_signout():
	# Grab cookies
	log_status = request.cookies.get('loggedin')
	# Redirect if already logged out
	if log_status == "no":
		return redirect("/", code=302)

	payload = {}
	response = make_response(flask.render_template("signout.html", **payload))
	return response

# Since we use a button to logout we need to handle post requests with it
@plazapp.app.route('/signout.html', methods=['POST'])
def show_signout_post():
	# Grab cookies
	log_status = request.cookies.get('loggedin')
	# Redirect if already logged out
	if log_status == "no":
		return redirect("/", code=302)

	payload = {}
	response = redirect("/", code=302)
	response.set_cookie('loggedin', 'no')
	response.set_cookie('uid', '0')
	return response