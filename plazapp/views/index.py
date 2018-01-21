import flask
from flask import request
from flask import make_response
import plazapp
from random import randint
from plazapp.model import get_posts

@plazapp.app.route('/')
def show_index():
        log_status = request.cookies.get('loggedin')
        payload = {}

        posts = get_posts(10)
        
        payload['posts'] = []
        for post in posts:
            post_dict = {}
            post_dict['title'] = post[3]
            post_dict['pid'] = post[2]
            post_dict['commentcount'] = randint(1, 100)
            payload['posts'].append(post_dict)



        if log_status == "yes":
                 payload['loggedin'] = False
        else:
                 payload['loggedin'] = True
        
        response = make_response(flask.render_template("index.html", **payload))
        return response
