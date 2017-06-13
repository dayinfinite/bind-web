# -*- coding:utf-8 -*-
# __author__ = 'dayinfinte'

from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import Serializer
from datetime import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Bind_cluster(db.Model):
    __tablename__ = 'bind_cluster'
    id = db.Column(db.Integer, primary_key=True)
    cluster = db.Column(db.String(64), unique=False)
    bind_ip = db.Column(db.String(64), unique=False)
    timestamp = db.Column(db.DateTime(), default=datetime.now())


class Dns_zone(db.Model):
    __tablename__ = 'dns_zone'
    id = db.Column(db.Integer, primary_key=True)
    zone = db.Column(db.String(64), unique=False)
    type = db.Column(db.String(64), unique=False)
    master_domain = db.Column(db.String(64), unique=True)
    mail_domain = db.Column(db.String(64), unique=True)
    soa_serial = db.Column(db.Integer, unique=True)
    soa_refresh = db.Column(db.Integer, unique=True)
    soa_retry = db.Column(db.Integer, unique=True)
    soa_expire = db.Column(db.Integer, unique=True)
    soa_minimum = db.Column(db.Integer, unique=True)
    timestamp = db.Column(db.DateTime(), default=datetime.now())


class Dns_host(db.Model):
    __tablename__ = 'dns_host'
    id = db.Column(db.Integer, primary_key=True)
    zone = db.Column(db.Integer, unique=True) 
    host = db.Column(db.String(64), unique=True)
    type = db.Column(db.String(64), unique=True)
    data = db.Column(db.String(64), unique=True)
    ttl = db.Column(db.Integer, unique=True)
    priority = db.Column(db.Integer, unique=True)
    port = db.Column(db.Integer, unique=True)
    weight = db.Column(db.Integer, unique=True)
    status = db.Column(db.String(64), unique=True)
    cluster = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
