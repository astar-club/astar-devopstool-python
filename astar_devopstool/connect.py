#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: connect.py
# @time: 2019/5/27 13:13
# @Software: PyCharm


__author__ = 'A.Star'

import paramiko


def sftp_put(file_from, file_to, host: str, port=22, username='root', password='admin'):
    with paramiko.Transport((host, port)) as t:
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(file_from, file_to)


def sftp_get(file_from, file_to, host: str, port=22, username='root', password='admin'):
    with paramiko.Transport((host, port)) as t:
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(file_from, file_to)


def SSHClient(host, port=22, username='root', private_key_file=None):
    private_key = paramiko.RSAKey.from_private_key_file(private_key_file)
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, pkey=private_key)
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    stdin, stdout, stderr = ssh.exec_command('df')
    print(stdout.read())
    transport.close()
