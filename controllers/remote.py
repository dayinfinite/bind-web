#!/usr/bin/env python
# coding=utf-8


import os
import sys
import paramiko
from ..config import Config


def Filexits(file):
    return os.path.exists(file)

def SSH_remote(ip, command):
    key = paramiko.RSAKey.from_private_key_file(Config['pkey'])
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AuthAddPolicy())
    ssh.connect(ip, 22, Config['user'], pkey=key, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(command)
    ssh.close()
    return stdout.readlines()


def SCP_remote(ip, localfile, remotefile):
    key = paramiko.RSAKey.from_private_key_file(Config['pkey'])
    scp = paramiko.Transport((ip, 22))
    scp.connect(username=Config['user'], pkey=key, timeout=5)
    sftp = paramiko.SFTPClient.from_transport(scp)
    stdin, stdout, stderr = sftp.put(localfile, remotefile)
    scp.close()
    return stdout.readlines()
