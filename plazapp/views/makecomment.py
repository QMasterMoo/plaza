import flask
from flask import request
from flask import make_response, redirect
import plazapp
from plazapp.model import set_comment

@plazapp.app.route('/p/<post_id>/makecomment.html')
def show_makecomment(post_id):
	payload = {}
	payload['postid'] = post_id

	response = make_response(flask.render_template("makecomment.html", **payload))

	return response

@plazapp.app.route('/p/<post_id>/makecomment.html', methods=['POST'])
def show_makecomment_post(post_id):
	payload = {}
	payload['postid'] = post_id
	# INSERT INTO DB
	content = request.form['content']
	uid = request.cookies.get('uid')
	
	# Confirm user logged in
	if uid == None or uid == '0':
		response = redirect("/login.html", code=302)
	else:
		set_comment(uid, post_id, content)
		response = redirect("/p/%s" % post_id, 302)


	

	return response