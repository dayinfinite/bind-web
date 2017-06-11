#!/usr/bin/env python
# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, validators, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from ..models import User, Bind_cluster, Dns_zone, Dns_host