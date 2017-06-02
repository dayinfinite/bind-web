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
    bind_ip = db.Column(db.String(64), unique=False)
    timestamp = db.Column(db.DateTime(), datetime.datetime.now())

class dns_zone(db.Model):

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
    status = db.Column(db.String(64), unique=False)
    cluster_id = db.Column(db.Integer, db.Foreignkey('bind_cluster.id'))
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now())

class dns_host(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.Integer, db.Foreignkey('dns_zone.id'))
    host = db.Column(db.String(64), unique=True)
    type = db.Column(db.String(64), unique=True)
    data = db.Column(db.String(64), unique=True)
    ttl = db.Column(db.Integer, unique=True)
    priority = db.Column(db.Integer, unique=True)
    port = db.Column(db.Integer, unique=True)
    weight = db.Column(db.Integer, unique=True)
    status = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())
