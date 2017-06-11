#!/usr/bin/env python
# coding=utf-8


import os
import sys
from service import db
from controllers.dnsfilehandler import DNSFileHandler
from controllers.dnshandler import DNSHandler
import json


def main(Message):

    msg = json.dumps(Message)
    zone_msg = db.query