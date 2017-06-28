#!/usr/bin/env python
# coding=utf-8


from service.models import Bind_cluster, Dns_zone, Dns_host
from controllers.dnsfilehandler import DNSFileHandler
from controllers.dnshandler import DNSHandler
import json


def utils(Message):
    msg = Message
    ips = Bind_cluster.query.filter_by(cluster=msg['cluster']).all()
    zone_record = Dns_zone.query.filter_by(zone=msg['zone']).first()
#    domain_record = Dns_host.query.filter_by(cluster=msg['cluster'],
#                                             zone=msg['zone']).all()
#
#    DNSFileHandler.CreateZoneFile(zone_record, domain_record)
#    DNSFileHandler.reateNamedFile(Dns_host.query.all(), type='master')


    for ip in ips:
        # print DNSHandler.CopyToRemote(ip, file=ZoneMsg['file'])
        # print DNSHandler.CopyToRemote(ip, file=NameMsg['file'])
        # print DNSHandler.CheckNamedConf(ip)
        # print DNSHandler.CheckZoneConf(ip, msg['zone'], ZoneMsg['file'])
        # print DNSHandler.RemoteBindReload(ip)
        return "ok"


if __name__ == "__main__":
    Message={
        "cluster": "XG01",
        "zone": "sina.com",
        "zone_type": "hostname"
    }

