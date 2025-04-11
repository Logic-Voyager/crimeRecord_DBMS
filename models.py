from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Crime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    location = db.Column(db.String(255))
    crime_type = db.Column(db.String(100))  # New
    severity = db.Column(db.String(50))     # New
    evidence = db.Column(db.String(255))    # New
