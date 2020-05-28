# -*- encoding=UTF-8 -*-

from easystagram import db
import random
from datetime import datetime

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    url = db.Column(db.String(512))
    created_date = db.Column(db.DateTime)

    def __init__(self, url,user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime

    def __repr__(self):
        return '<Image %d %s>' % (self.id, self.url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    images = db.relationship('Image')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.head_url = 'https://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.username)
