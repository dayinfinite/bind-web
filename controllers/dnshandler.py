#!/usr/bin/env python
# coding=utf-8


import os
import sys
import datime.datime
from .remote import SSH_remote, SCP_remote

class DNSHandler:

    def __init__(self):
        pass


    def CheckNamedConf(self, ip): 
        msg = SSH_remote(ip, "/home/named/sbin/named-checkconf")
        return msg

    def CheckZoneConf(self, ip, zone, zonefile):
        msg = SSH_remote(ip, "/home/named/sbin/named-checkzone %s  %s" % zone, "/home/named/zone-files"+ zonefile)
        return msg

    def RemoteBindReload(self, ip):
        msg = SSH_remote(ip, "/etc/init.d/named reload")
        return msg

    def CopyToRemote(self, ip, file):
        msg = SCP_remote(ip, file)
        return msg
