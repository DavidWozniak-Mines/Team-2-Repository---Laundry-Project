#stuff that makes flask work
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass
with app.app_context():
    db.create_all()
def add_event(event_description):
    new_event = Event(event=event_description)
    db.session.add(new_event)
    db.session.commit()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)  
    event = db.Column(db.String(200), nullable=False) 

if __name__=="__main__":
    app.run(debug=True)
@app.route("/hello")
def hello():
    return "Hello, Welcome to Laundrysite"
  
@app.route("/")
def index():
    return "Homepage of Laundrysite"

