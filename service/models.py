# -*- coding:utf-8 -*-
# __author__ = 'dayinfinte'

from . import db, login_manager
from wtforms import validators
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import Serializer
import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        return self.password

    @property.setter
    def password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(password)

class bind_cluster(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    cluster = db.Column(db.String(64), unique=False)
    bind_ip = db.Column(db.String(64), unique=True)

class dns_zone(db.Model):

    id = db.Column(db.Integer, primary_key=True)


