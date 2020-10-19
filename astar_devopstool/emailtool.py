#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: email.py
# @time: 2019/5/27 11:20
# @Software: PyCharm


__author__ = 'A.Star'

import smtplib
from email.mime.text import MIMEText
from astartool.string import is_email
from astar_devopstool.exception import EmailError


def send_mail(username, passwd, recv, title, content, mail_host='smtp.ym.163.com', port=25):
    """
    发送邮件函数，默认使用163smtp
    :param mail_host: 邮箱服务器，16邮箱host: smtp.163.com
    :param port: 端口号,163邮箱的默认端口是 25
    :param username: 邮箱账号 xx@163.com
    :param passwd: 邮箱密码(不是邮箱的登录密码，是邮箱的授权码)
    :param recv: 邮箱接收人地址str or list，多个账号以逗号隔开
    :param title: 邮件标题
    :param content: 邮件内容
    :return:
    """
    if not isinstance(recv, (str, bytes)):
        for each in recv:
            if not is_email(each):
                raise EmailError('Email Error!')
        recv = ','.join(recv)
    msg = MIMEText(content)  # 邮件内容
    msg['Subject'] = title  # 邮件主题
    msg['From'] = username  # 发送者账号
    msg['To'] = recv  # 接收者账号列表
    smtp = smtplib.SMTP(mail_host, port=port)  # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
    smtp.login(username, passwd)  # 登录发送者的邮箱账号，密码
    # 参数分别是 发送者，接收者，第三个是把上面的发送邮件的 内容变成字符串
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()  # 发送完毕后退出smtp
    # print('email send success.')
