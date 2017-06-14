#!/usr/bin/env python
# coding=utf-8
'''This dns file operate'''

import os
from jinja2 import Environment, FileSystemLoader

def TemplatExits(file):
    if os.path.isfile(file):
        return {"status": True, 'filename': file}


class DNSFileHandler(object):
    """This create file about dns"""

    def __init__(self):
        pass

    def CreateZoneFile(self, zone_record, domain_record):
        env = Environment(loader=FileSystemLoader(searchpath='service/templates/'))
        template = env.get_template('db.zone_template')
        temp = template.render(zone_record=zone_record, 
                               domain_record=domain_record)
        file = 'db.{0}'.format(zone_record['zone'])
        with open('tmp/'+file, 'w') as zonefile:
            zonefile.write(temp)
        return TemplatExits(file)


    def CreateNamedFile(self, zones, type, ips=None):
        env = Environment(loader=FileSystemLoader(searchpath='service/templates/'))
        template = env.get_template('named.conf')
        temp = template.render(zones=zones,
                               type=type,
                               ips=ips)
        with open('tmp/named.conf', 'w') as named_conf:
            named_conf.write(temp)
        return TemplatExits(named.conf)


if __name__ == '__main__':
    zone_record = {
            'zone': 'sina.com',
            'type': 'master',
            'master_domain': 'root.sina.com.',
            'mail_domain': 'mail.sina.com.',
            'soa_serial': 2016073101,
            'soa_refresh': 3600,
            'soa_retry': 3600,
            'soa_expire': 3600,
            'soa_mininum': 3600
            }

    domain_record = [{
            'zone': 'sina.com',
            'host': 'www',
            'type': 'A',
            'data': '1.1.1.1',
            'ttl': 180,
            'prioriry': None,
            'port': None,
            'weight': None,
            'status': 'on',
            'cluster': 'XG01'
            }]
    test = DNSFileHandler()
    test.CreateZoneFile(zone_record, domain_record)
