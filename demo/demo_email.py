#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo_email.py
# @time: 2019/5/27 11:19
# @Software: PyCharm


__author__ = 'A.Star'

import configparser
from astar_devopstool.email import *

cp = configparser.ConfigParser()
cp.read('config.conf')

if __name__ == '__main__':
    email_user = cp.get('email', 'user')  # 发送者账号
    email_pwd = cp.get('email', 'password')  # 发送者密码,授权码
    maillist = ['astar@snowland.ltd']
    title = '这是一封来自雪域的测试邮件'
    content = '测试邮件，请勿回复！'
    send_mail(email_user, email_pwd, maillist, title, content)
