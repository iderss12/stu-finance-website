import datetime
from . import db


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postName = db.Column(db.String(100), nullable=False)
    postBody = db.Column(db.Text)
    postAuthor = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, postName, postBody, postAuthor, category):
        self.postName = postName
        self.postBody = postBody
        self.postAuthor = postAuthor
        self.category = category


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postId = db.Column(db.Integer)
    commenterName = db.Column(db.String(100), nullable=True)
    comment = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, postId, commenterName, comment):
        self.postId = postId
        self.commenterName = commenterName
        self.comment = comment
