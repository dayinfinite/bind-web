#!/usr/bin/env python
# coding=utf-8


import os
import sys 
import paramiko 
dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(dir_name)
import config


def Filexits(file):
    return os.path.exists(file)

def SSH_remote(ip, command):
    key = paramiko.RSAKey.from_private_key_file(config.pkey)
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(ip, 22, username=config.user, pkey=key, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(command)
    msg = [stdout.read(), stderr.read()]
    ssh.close()
    return msg

def SCP_remote(ip, localfile, remotefile):
    key = paramiko.RSAKey.from_private_key_file(config.pkey)
    scp = paramiko.Transport((ip, 22))
    scp.connect(username=config.user, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(scp)
    msg = sftp.put(remotefile, localfile)
    scp.close()
    return msg
