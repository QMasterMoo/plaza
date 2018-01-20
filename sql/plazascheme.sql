CREATE TABLE users(
	username VARCHAR(20) NOT NULL,
	userid VARCHAR(40) NOT NULL,
	password VARCHAR(256) NOT NULL,
	PRIMARY KEY(username)
	);
	
CREATE TABLE posts(
	postid INTEGER NOT NULL,
	postcontent TEXT(500) NOT NULL,
	ownerid VARCHAR(20) NOT NULL,
	PRIMARY KEY(postid)
	);
	
CREATE TABLE comments(
	commentid INTEGER NOT NULL,
	userid VARCHAR(40) NOT NULL,
	commentcontent TEXT(500) NOT NULL,
	PRIMARY KEY(commentid)
	);
	
