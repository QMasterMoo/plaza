CREATE TABLE users(
	username VARCHAR(20) NOT NULL,
	userid INTEGER PRIMARY KEY AUTOINCREMENT,
	password VARCHAR(256) NOT NULL,
	salt VARCHAR(16) NOT NULL
	);
	
CREATE TABLE posts(
	postid INTEGER PRIMARY KEY AUTOINCREMENT,
	postcontent TEXT(500) NOT NULL,
	ownerid INTEGER NOT NULL,
	posttitle VARCHAR(50) NOT NULL,
	FOREIGN KEY(ownerid) REFERENCES users(userid)
	);
	
CREATE TABLE comments(
	commentid INTEGER PRIMARY KEY AUTOINCREMENT,
	userid INTEGER NOT NULL,
	postid INTEGER NOT NULL,
	commentcontent TEXT(500) NOT NULL,
	FOREIGN KEY(userid) REFERENCES users(userid)
	);

