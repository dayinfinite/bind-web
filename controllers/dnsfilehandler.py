#!/usr/bin/env python
# coding=utf-8
'''This dns file operate'''

import os
from jinja2 import Environment, PackageLoader


def TemplatExits(tfile):
    if os.path.isfile(tfile):
        return "{0} is exits".format(tfile)


class DNSFileHandler(object):
    """This create file about dns"""

    def __init__(self):
        pass

    def CreateZoneFile(self, zone, cluster, zone_record, domain_record):
        env = Environment(loader=PackageLoader(package_name='service', 
                                               package_path='templates', 
                                               encoding='utf-8'))
        template = env.get_template('db.zone_template')
        temp = template.render(zone=zone,
                               zone_record=zone_record, 
                               domain_record=domain_record)
        with open('db.{0}'.format(zone), 'w') as zonefile:
            zonefile.write(temp)

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
