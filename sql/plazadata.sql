INSERT INTO users(username, password, salt)
VALUES ('sac', 'fish123', 'a1b2');

INSERT INTO users(username, password, salt)
VALUES ('al', 'ccdc76be3ffe8676a21fee1e957316028aa684662f628e40466e1ce2583313e91b6d91ecb86e4882e92af580b7a6d4d8297f7102cfb52cd597a581f38d7fc7a3', 'la');

INSERT INTO users(username, password, salt)
VALUES ('koni', 'fiszzh123', 'azz2');

INSERT INTO posts(postcontent, ownerid, posttitle)
VALUES ('This is the first content', '1', 'title1');

INSERT INTO posts(postcontent, ownerid, posttitle)
VALUES ('This is the first content', '3', 'title2');

INSERT INTO posts(postcontent, ownerid, posttitle)
VALUES ('This is the first content', '3', 'title3');

INSERT INTO comments(userid, postid, commentcontent)
VALUES ('1', '1', 'fuckin first comment biatch');

INSERT INTO comments(userid, postid, commentcontent)
VALUES ('2', '2', 'fuckin second comment biatch');

INSERT INTO comments(userid, postid, commentcontent)
VALUES ('2', '3', 'conk');