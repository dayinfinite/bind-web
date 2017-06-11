#!/usr/bin/env python
# coding=utf-8

from flask import Flask, url_for, request, jsonify
from .. import db
from ..models import Dns_host, Dns_zone, Bind_cluster
from . import main
from datetime import datetime
from flask_login import current_user, login_required
import json


@main.route('/addhost', methods=['GET', 'POST'])
def add_zone():
    zone = Dns_zone.query.filtey_by(zone=request.json['zone_msg']['zone']).first()
    if zone == None:
        db.session.add(zone_msg=request.json['zone_msg'])
        db.session.commit()
        return main(request.json['zone_msg'])
