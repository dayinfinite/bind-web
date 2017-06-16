#!/usr/bin/env python
# coding=utf-8
'''This is remote doc'''


from remote import SSH_remote
from remote import SCP_remote

class DNSHandler(object):


    def __init__(self):
        pass


    def CheckNamedConf(self, ip): 
        msg = SSH_remote(ip, "/home/named/sbin/named-checkconf")
        return msg

    def CheckZoneConf(self, ip, zone, zonefile):
        msg = SSH_remote(ip, "/home/named/sbin/named-checkzone {zone} {zonefile}".format(zone=zone, zonefile="/home/named/zone-files/"+ zonefile))
        return  msg

    def RemoteBindReload(self, ip):
        msg = SSH_remote(ip, "/etc/init.d/named reload")
        return  msg


    def CopyToRemote(self, ip, localfile, remotefile):
        msg = SCP_remote(ip, localfile, remotefile)
        return  msg

if __name__ == '__main__':
    test = DNSHandler()
    ip = '172.16.3.140'
    zone = 'db.sina.com'
    zonefile = 'db.git.xiaojukeji.com'
    localfile  = '/home/named/zone-files/' + zone
    remotefile = 'tmp/' + zone
    msg = test.CheckNamedConf(ip)
    #print test.RemoteBindReload(ip)
    #print test.CopyToRemote(ip, localfile, remotefile) 
