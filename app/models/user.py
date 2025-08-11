from . import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    refresh_token = db.Column(db.Text, nullable=True)