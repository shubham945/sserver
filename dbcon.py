from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytz import timezone
import hashlib

db = SQLAlchemy()
SECRET_KEY = "Prajyot Prabhat Ranvijay"

## DB TABLES
class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    pushtoken = db.Column(db.String(700))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.pushToken = ""

    def __repr__(self):
        return '<AppUser %r with email %r>' % (self.username, self.email)




## DB METHODS

## Injects db connection inside of flask app
def inject_db(app):
    """
        Injects database inside flask app.
    """
    db.init_app(app)
    return app
