from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from secret import path

database_path = path 

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    
    
def db_drop_and_create_all(app):
    with app.app_context():
        db.drop_all()
        db.create_all() 
  

class Articles(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    
    
    def __init__(self, title, body):
        self.name = title
        self.body = body
    
    
    def __repr__(self):
        return f"articles(title = {self.title}, body = {self.body}, date = {self.date})"