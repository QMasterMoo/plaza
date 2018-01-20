import flask
from flask import request
from flask import make_response
import plazapp

@plazapp.app.route('/p/<post_id>')
def show_post(post_id):
	payload = {}
	payload['post_id'] = post_id
	response = make_response(flask.render_template("post.html", **payload))

	return response

