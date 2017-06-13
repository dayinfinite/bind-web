#!/usr/bin/env python
# coding=utf-8


from service.models import Bind_cluster, Dns_zone, Dns_host
from controllers.dnsfilehandler import DNSFileHandler
from controllers.dnshandler import DNSHandler
import json


def utils(Message):

    msg = json.dumps(Message)
    ips = Bind_cluster.query.filter_by(cluster=msg['cluster']).all()
    zone_record = Dns_zone.query.filter_by(zone=msg['zone']).first()
    domain_record = Dns_host.query.filter_by(cluster=msg['cluster']).all()

    ZoneMsg = DNSFileHandler.CreateZoneFile(zone_record, domain_record)
    if ZoneMsg['status']:
        print "zone文件创建完成"

    NameMsg = DNSFileHandler.reateNamedFile(Dns_host.query.filter_by().all(), type='master')
    if NameMsg['status']:
        print "bind主配置文件创建完成"

    for ip in ips:
        print DNSHandler.CopyToRemote(ip, file=ZoneMsg['file'])
        print DNSHandler.CopyToRemote(ip, file=NameMsg['file'])
        print DNSHandler.CheckNamedConf(ip)
        print DNSHandler.CheckZoneConf(ip, msg['zone'], ZoneMsg['file'])
        print DNSHandler.RemoteBindReload(ip)
        return "ok"
