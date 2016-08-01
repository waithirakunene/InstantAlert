from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import db
from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
      
    

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

   

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))    

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    send_to = db.Column(db.Integer, db.ForeignKey('users.id'))
    message_body = db.Column(db.String(64), unique=True, index=True)


class Farmer(db.Model):
    __tablename__= 'farmers'
    id = db.Column(db.Integer,primary_key=True)
    farmers_name = db.Column(db.String(64))
    farmers_id_no = db.Column(db.Integer, unique=True)
    gender = db.Column(db.String)
    location = db.Column(db.String)
    type_of_farming = db.Column(db.String)




   

