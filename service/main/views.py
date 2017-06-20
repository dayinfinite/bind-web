#!/usr/bin/env python
# coding=utf-8

from flask import Flask, url_for, request, jsonify
from .. import db
from ..models import Dns_host, Dns_zone, Bind_cluster
from utils import utils
from . import main
from flask_login import current_user, login_required
import json



@main.route('/record', methods=['GET', 'POST'])
def host():
    data = request.json['data']
    if not Dns_zone.query.filter_by(zone=data['zone']).first():
        return jsonify({'status': 'fail', 'reason': 'zone is not exits'})
    if Dns_host.query.filter_by(host=data['host'],
                                zone=data['zone'],
                                data=data['data'],
                                cluster=data['cluster']).first():
        return jsonify({'status': 'exits'})
    host_record = Dns_host(zone=data['zone'],
                           type=data['type'],
                           host=data['host'],
                           data=data['data'],
                           ttl=data['ttl'],
                           status=data['status'],
                           cluster=data['cluster']
                           )
    db.session.add(host_record)
    db.session.commit()
    utils.utils({'zone': data['zone'],
                 'cluster': data['cluster']})
    return jsonify(request.json)


@main.route('/zone', methods=['GET', 'POST'])
def zone():
    data = request.json
    if Dns_zone.query.filter_by(zone=data['zone']).first():
        return jsonify({'status': 'exits'})
    zone_record = Dns_zone(zone=data['zone'],
                           type=data['type'],
                           master_domain=data['master_domain'],
                           mail_domain=data['mail_domain'],
                           soa_serial=data['soa_serial'],
                           soa_refresh=data['soa_refresh'],
                           soa_retry=data['soa_retry'],
                          soa_expire=data['soa_expire'],
                           soa_mininum=data['soa_mininum'])
    db.session.add(zone_record)
    db.session.commit()
    utils.utils({'zone': data['zone'],'cluster': ''})
    return jsonify(request.json)

@main.route('/bind', methods=['GET', 'POST'])
def bind():
    data = request.json
    if Bind_cluster.query.filter_by(cluster=data['cluster'], bind_ip=data['bind_ip']).first():
        return jsonify({'status': 'exits'})
    ip_record = Bind_cluster(cluster=data['cluster'], bind_ip=data['bind_ip'])
    db.session.add(ip_record)
    db.session.commit()
    return jsonify(request.json)


@main.route('/hostname' , methods=['GET', 'POST'])
def hostname():
    data = request.json

    if not Dns_zone.query.filter_by(zone=data['zone']).first():
        return "{0} not exits".format(data['zone'])

    for i in range(len(data['data'].split('.')))[::-1]:
        zone = '.'.join(data['data'].split('.')[::-1][i:4]) + ".in-addr.arpa."
        host = '.'.join(data['data'].split('.')[::-1][0:i])
        if Dns_zone.query.filter_by(zone=zone).first():
            if Dns_host.query.filter_by(host=data['host'],zone=data['zone'],data=data['data']).first() or Dns_host.query.filter_by(host=host, zone=zone, data=data['host']+'.'+data['zone']).first():
                return jsonify({
                    "status": "failed",
                    "reason": "hostname is exits"}
                )
            else:
                domain_A = Dns_host(zone=data['zone'],
                                    type=data['type'],
                                    host=data['host'],
                                    data=data['data'],
                                    ttl=data['ttl'],
                                    status=data['status'],
                                    cluster='ALL'
                                   )
                domain_PTR = Dns_host(zone=zone,
                                      type='PTR',
                                      host=host,
                                      data=data['host']+'.'+data['zone'],
                                      ttl=data['ttl'],
                                      status=data['status'],
                                      cluster='ALL'
                                   ) 
                db.session.add(domain_A)
                db.session.add(domain_PTR)
                db.session.commit()
                return jsonify({"status": 'suc'})
    return jsonify({"status": 'fail', "reason": '域不存在'})
