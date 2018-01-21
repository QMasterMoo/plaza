import flask
from flask import request
from flask import make_response
import plazapp
from plazapp.model import *

@plazapp.app.route('/')
def show_index():
        log_status = request.cookies.get('loggedin')
        payload = {}
        post1 = {'postid': 1, 'title':'conk', 'commentcount': 10}
        post2 = {'postid': 2, 'title':'worldstar', 'commentcount': 21}
        post3 = {'postid': 3, 'title':'ferda', 'commentcount': 3771}
        payload['posts'] = [post1, post2, post3]
        if log_status == "yes":
                 payload['loggedin'] = True
        else:
                 payload['loggedin'] = False
        
        response = make_response(flask.render_template("index.html", **payload))
        return response
