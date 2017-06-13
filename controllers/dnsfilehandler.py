#!/usr/bin/env python
# coding=utf-8
'''This dns file operate'''

import os
from jinja2 import Environment, PackageLoader


def TemplatExits(file):
    if os.path.isfile(file):
        return {"status": True, 'filename': file}


class DNSFileHandler(object):
    """This create file about dns"""

    def __init__(self):
        pass

    def CreateZoneFile(self, zone_record, domain_record):
        env = Environment(loader=PackageLoader(package_name='service', 
                                               package_path='templates', 
                                               encoding='utf-8'))
        template = env.get_template('db.zone_template')
        temp = template.render(zone_record=zone_record, 
                               domain_record=domain_record)
        file = 'db.{0}'.format(zone_record['zone'])
        with open(file, 'w') as zonefile:
            zonefile.write(temp)
        return TemplatExits(file)



    def CreateNamedFile(self, zones, type, ips=None):
        env = Environment(loader=PackageLoader(package_name='service',
                                               package_path='templates',
                                               encoding='utf-8'))
        template = env.get_template('named.conf')
        temp = template.render(zones=zones,
                               type=type,
                               ips=ips)
        with open('named.conf', 'w') as named_conf:
            named_conf.write(temp)
        return TemplatExits(named.conf)
