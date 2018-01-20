INSERT INTO users(username, userid, password)
VALUES ('sac', 'sac123', 'fish123');

INSERT INTO posts(postid, postcontent, ownerid)
VALUES ('1', 'This is the first content', 'sac123');

INSERT INTO comments(commentid, userid, commentcontent)
VALUES ('1', 'sac123', 'fuckin first comment biatch');