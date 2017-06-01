# -*- coding:utf-8 -*-
# __author__ = 'dayinfinte'

import records
import sys
import os
import ConfigParser


def DB():
    db = ConfigParser.ConfigParser()
    db.read('../config/config.ini')
    url = db.get("db", "url")
    print "url=%s" % url

    
if __name__ == '__main__':
    DB()
