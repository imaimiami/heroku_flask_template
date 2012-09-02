from __init__ import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.user_name
