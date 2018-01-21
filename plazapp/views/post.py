import flask
from flask import request
from flask import make_response
import plazapp
from plazapp.model import get_comments, get_title, get_posttext

@plazapp.app.route('/p/<post_id>')
def show_post(post_id):
	payload = {}
	comments = get_comments(post_id)
	payload['posttitle'] = get_title(post_id)
	payload['posttext'] = get_posttext(post_id)

	payload['comments'] = []
	for comment in comments:
		com_dict = {}
		com_dict['commentid'] = comment[0]
		com_dict['commenttext'] = comment[3]
		payload['comments'].append(com_dict)


	response = make_response(flask.render_template("post.html", **payload))

	return response

