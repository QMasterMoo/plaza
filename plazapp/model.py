import sqlite3
import flask
import plazapp

#this will connect to our database
def get_db():
	if not hasattr(flask.g, 'sqlite_db'):
		flask.g.sqlite_db = sqlite3.connect(plazapp.app.config['DATABASE_FILENAME'])
		# BACKWARDS COMPAT FOR SQLITE3
		flask.g.sqlite_db('PRAGMA foreign_keys = ON')

	return flask.g.sqlite_db

@plazapp.app.teardown_appcontext
def close_db(error):
	if hasattr(flask.g, 'sqlite_db'):
		flask.g.sqlite_db.commit()
		flask.g.sqlite_db.close()


def get_comments():
	cursor = get_db().cursor()
	cursor.execute("SELECT * FROM comments")
	print(cursor.fetchall())
	
def get_commentor():
	cursor = get_db().cursor()
	cursor.execute("SELECT userid FROM comments WHERE userid = 1")
	print(cursor.fetchall())
	
def get_username():
	cursor = get_db().cursor()
	cursor.execute("SELECT username FROM users WHERE userid = 1")
	print(cursor.fetchall())
	
def get_posts():
	cursor = get_db().cursor()
	cursor.execute("SELECT postid FROM posts WHERE postid = 1")
	print(cursor.fetchall())
	
def get_poster():
	cursor = get_db().cursor()
	cursor.execute("SELECT userid FROM comments WHERE commentid = 1")
	print(cursor.fetchall())
	
def set_comment(userid, postid, content):
	cursor = get_db().cursor()
	cursor.execute("INSERT INTO comments(userid, postid, commentcontent) VALUES('%d', '%d', '%s')" % (userid, postid, content))
	print(cursor.fetchall())
	
def check_hash(username, hash_in):
	cursor = get_db().cursor()
	cursor.execute("SELECT password FROM users WHERE username = '%s'" % username)
	temp = cursor.fetchone()
	print(temp)
	if temp != None:
		return temp[0] == hash_in
	else:
		return False

def get_uid(username):
	cursor = get_db().cursor()
	cursor.execute("SELECT userid FROM users WHERE username='%s'" % username)
	return cursor.fetchone()[0]
