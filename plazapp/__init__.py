import flask

# app is our object
app = flask.Flask(__name__)

# Read config file
app.config.from_object('plazapp.config')

# idk if we need this
app.config.from_envvar('PLAZAPP_SETTINGS', silent=True)

# Flask circular input
# MODEL VIEW CONTROLLER model
import plazapp.views
import plazapp.model