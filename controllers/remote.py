#!/usr/bin/env python
# coding=utf-8


import os
import paramiko
from config import pkey, user


def Filexits(file):
    return os.path.exists(file)


def SSH_remote(ip, command):
    key = paramiko.RSAKey.from_private_key_file(pkey)
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(ip, 22, user, pkey=key, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(command)
    ssh.close()
    return stdout.readlines()


def SCP_remote(ip, localfile, remotefile):
    key = paramiko.RSAKey.from_private_key_file(pkey)
    scp = paramiko.Transport((ip, 22))
    scp.connect(username=user, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(scp)
    stdin, stdout, stderr = sftp.put(localfile, remotefile)
    scp.close()
    return stdout.readlines()
