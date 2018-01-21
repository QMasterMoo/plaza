import flask
from flask import request
from flask import make_response
import plazapp
from plazapp.model import *

@plazapp.app.route('/')
def show_index():
	payload = {}
	post1 = {'postid': 1, 'title':'conk', 'commentcount': 10}
	post2 = {'postid': 2, 'title':'worldstar', 'commentcount': 21}
	post3 = {'postid': 3, 'title':'ferda', 'commentcount': 3771}
	payload['posts'] = [post1, post2, post3]
	response = make_response(flask.render_template("index.html", **payload))

	get_comments()
	get_commentor()
	get_username()
	get_posts()
	get_poster()
	return response
