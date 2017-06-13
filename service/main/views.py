#!/usr/bin/env python
# coding=utf-8

from flask import Flask, url_for, request, jsonify
from .. import db
from ..models import Dns_host, Dns_zone, Bind_cluster
from utils import utils
from . import main
from datetime import datetime
from flask_login import current_user, login_required
import json



@main.route('/record', methods=['GET', 'POST'])
def host():
    zone = request.json['zone']
    print zone
    return jsonify(request.json)

#    zone = Dns_zone.query.filter_by(zone=request.json['zone_msg']['zone']).first()
#    if zone == None:
#        db.session.add(zone_msg=request.json['zone_msg'])
#        db.session.commit()
#        return utils.utils(request.json['zone_msg'])

@main.route('/zone', methods=['GET', 'POST'])
def zone():
    pass


@main.route('/bind', methods=['GET', 'POST'])
def bind():
    pass
