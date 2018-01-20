CREATE TABLE users(
	username VARCHAR(20) NOT NULL,
	userid INTEGER NOT NULL,
	password VARCHAR(256) NOT NULL,
	salt VARCHAR(16) NOT NULL,
	PRIMARY KEY(userid)
	);
	
CREATE TABLE posts(
	postid INTEGER NOT NULL,
	postcontent TEXT(500) NOT NULL,
	ownerid INTEGER NOT NULL,
	PRIMARY KEY(postid),
	FOREIGN KEY(ownerid)
	);
	
CREATE TABLE comments(
	commentid INTEGER NOT NULL,
	userid INTEGER NOT NULL,
	commentcontent TEXT(500) NOT NULL,
	PRIMARY KEY(commentid),
	FOREIGN KEY(userid)
	);

