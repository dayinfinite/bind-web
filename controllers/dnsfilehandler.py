#!/usr/bin/env python
# coding=utf-8


import os
import sys
from ..service import db
from jinja2 import Template, Environment, FileSystemLoader


def templatExits(tfile):
    if os.path.isfile(tfile):
        return "{0} is exits".format(tfile)

class DNSFileHandler:

    def __init__(self):
        pass

    def CreateZoneFile(self, zone, cluster, zone_record, domain_record):
        env = Environment(loader=PackageLoader('service/templates/'))
        template = env.get_template('db.zone_template')
        temp = template.render(zone, zone_record, domain_record)
        with open('db.{0}'.format(zone), 'w') as zonefile:
            zonefile.write(temp)

    def CreateNamedFile(self, zones, type, ips=None):
        env = Environment(loader=PackageLoader('service/templates/'))
        template = env.get_template('named.conf')
        temp = template.render(zone, type, ips)
        with open('named.conf', 'w') as named_conf:
            named_conf.write(temp)
