INSERT INTO users(username, userid, password, salt)
VALUES ('sac', '1', 'fish123', 'a1b2');

INSERT INTO users(username, userid, password, salt)
VALUES ('al', '2', 'fish123', 'a1b2');

INSERT INTO users(username, userid, password, salt)
VALUES ('koni', '3', 'fiszzh123', 'azz2');

INSERT INTO posts(postid, postcontent, ownerid)
VALUES ('1', 'This is the first content', '1');

INSERT INTO posts(postid, postcontent, ownerid)
VALUES ('2', 'This is the first content', '3');

INSERT INTO posts(postid, postcontent, ownerid)
VALUES ('3', 'This is the first content', '3');

INSERT INTO comments(commentid, userid, postid, commentcontent)
VALUES ('1', '1', '1', 'fuckin first comment biatch');

INSERT INTO comments(commentid, userid, postid, commentcontent)
VALUES ('2', '2', '2', 'fuckin second comment biatch');

INSERT INTO comments(commentid, userid, postid, commentcontent)
VALUES ('3', '2', '3', 'conk');