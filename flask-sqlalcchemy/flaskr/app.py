# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///demo_database.db'
# print("SqlAlchemy : ", app.config['SQLALCHEMY_DATABASE_URI'])
# db = SQLAlchemy(app)
# print("DB : ",db)


# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(100), nullable=False)
#     lastname = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     age = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime(timezone=True),
#                            server_default=func.now())
#     bio = db.Column(db.Text)

#     def __repr__(self):
#         return f'<Student {self.firstname}>'

    
# db.create_all()        
# # print("CREATE ALL : ",db.create_all())
# print("Success...!")
# if __name__ ==  '__main__':
#     app.run()


from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
 
app = Flask(__name__)
app.debug = True
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)
 
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
 
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

with app.app_context():
    db.create_all()
    
 
if __name__ == '__main__':
    app.run()