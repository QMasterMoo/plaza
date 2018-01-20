import sqlite3
import flask
import plazapp

#this will connect to our database
def get_db():
	if not hasattr(flask.g, 'sqlite_db'):
		flask.g.sqlite_db = sqlite.connect(plaza.app.config['DATABASE_FILENAME'])
		# BACKWARDS COMPAT FOR SQLITE3
		flask.g.sqlite_db('PRAGMA foreign_keys = ON')

	return flask.g.sqlite_db


@plazapp.app.teardown_appcontext
def close_db(error):
	if hasattr(flask.g, 'sqlite_db'):
		flask.g.sqlite_db.commit()
		flask.g.sqlite_db.close()


def get_comments():
	cursor = get_db()
	cursor.execute("SELECT username FROM users WHERE userid = 1")
	print(cursor.fetchall())
	