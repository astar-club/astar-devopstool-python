#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: connect.py
# @time: 2019/5/27 13:13
# @Software: PyCharm


__author__ = 'A.Star'

import ftplib
import os
import socket

try:
    import paramiko
    paramiko_flag = True
except:
    paramiko_flag = False

from astar_devopstool.common import FTPCode


def ftp_put(file_from, file_to, host: str, port=22, username='root', password='admin', buffer_size=1024 * 8):
    """
    ftp发送文件
    :param file_from:
    :param file_to:
    :param host:
    :param port:
    :param username:
    :param password:
    :param buffer_size:
    :return:
    """
    dir_rute = file_to
    try:
        f = ftplib.FTP(host)  ####连接ftp服务器
    except (socket.error, socket.gaierror):
        print('ERROR:cannot reach " %s"' % host)
        return FTPCode.IP_CANNOT_FOUND.value
    print('***Connected to host "%s"' % host)
    try:
        f.login(username, password)  ###登录ftp服务器
    except ftplib.error_perm:
        print('ERROR: cannot login "%s"' % username)
        f.quit()
        return FTPCode.LOGIN_ERROR.value
    print('*** Logged in as "%s"' % username)
    try:
        f.cwd(dir_rute)
    except ftplib.error_perm:
        print('ERRORL cannot CD to "%s"' % dir_rute)
        f.quit()
        return FTPCode.CANNOT_FOUND_CD.value
    print('*** Changed to "%s" folder' % dir_rute)
    try:
        if isinstance(file_from, str):
            with open(file_from, 'rb') as file_handle:  # 以写模式在本地打开文件
                f.storbinary('STOR %s' % os.path.basename(file_from), file_handle,
                             buffer_size)  # 传一个回调函数给storbinary() 它在每接收一个二进制数据时都会被调用

        else:  # isinstance(file_from, _io.BufferedReader)
            file_name, file_handle = file_from.name, file_from
            f.storbinary('STOR %s' % os.path.basename(file_name), file_handle,
                         buffer_size)  # 传一个回调函数给storbinary() 它在每接收一个二进制数据时都会被调用

    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % file_from)
        os.unlink(file_from)
        return FTPCode.FILE_CANNOT_READ.value
    else:
        print('*** ftp up "%s" to CWD ok' % file_from)
    f.quit()
    return FTPCode.SUCCESSFUL.value


def sftp_put(file_from, file_to, host: str, port=22, username='root', password='admin'):
    """
    ftp发送文件
    :param file_from:
    :param file_to:
    :param host:
    :param port:
    :param username:
    :param password:
    :return:
    """
    with paramiko.Transport((host, port)) as t:
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(file_from, file_to)


def sftp_get(file_from, file_to, host: str, port=22, username='root', password='admin'):
    """
    ftp获得文件
    :param file_from:
    :param file_to:
    :param host:
    :param port:
    :param username:
    :param password:
    :return:
    """
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
