import flask
from flask import request
from flask import make_response
import plazapp
from plazapp.model import get_comments, get_title, get_posttext

@plazapp.app.route('/p/<post_id>')
def show_post(post_id):
	payload = {}
	get_comments(post_id)
	payload['posttitle'] = get_title(post_id)
	payload['posttext'] = get_posttext(post_id)

	response = make_response(flask.render_template("post.html", **payload))

	return response

