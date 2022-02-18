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
import warnings
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Union, Tuple

from astartool.string import is_email

from astar_devopstool.exception import EmailError


def send_mail(username, passwd, recv, title, content, mail_host='smtp.ym.163.com', port=25, *,
              cc=None,
              attachment_file: Union[List[bytes], Tuple[bytes], bytes] = None,
              attachment_name: Union[List[str], Tuple[str], str] = None):
    """
    发送邮件函数，默认使用163smtp
    :param mail_host: 邮箱服务器，16邮箱host: smtp.163.com
    :param port: 端口号,163邮箱的默认端口是 25
    :param username: 邮箱账号 xx@163.com
    :param passwd: 邮箱密码(不是邮箱的登录密码，是邮箱的授权码)
    :param recv: 邮箱接收人地址str or list，多个账号以逗号隔开
    :param title: 邮件标题
    :param content: 邮件内容
    :param cc: 抄送，格式与recv一致
    :param attachment_file: 附件内容,可以是列表，元祖或者字节格式，若为字节格式，则仅能单附件， default None，表示没有附件
    :param attachment_name: 附件名，可以是列表，元祖或者字符串格式，若为字符串格式，则仅能单附件， default None，表示没有附件
    :return:
    """
    if not isinstance(recv, (str, bytes)):
        for each in recv:
            if not is_email(each):
                raise EmailError('邮件接受者格式错误')
        recv_str = ','.join(recv)
    else:
        recv_str = recv
        if ',' in recv:
            recv = recv.split(',')
        elif ';' in recv:
            recv = recv.split(';')
        else:
            recv = [recv]
    msg = MIMEMultipart()  # 邮件内容
    msg['Subject'] = title  # 邮件主题
    msg['From'] = username  # 发送者账号
    msg['To'] = recv_str  # 接收者账号列表
    if cc is not None:
        if not isinstance(cc, (str, bytes)):
            for each in cc:
                if not is_email(each):
                    raise EmailError('邮件抄送者格式错误')
            cc_str = ','.join(cc)

        else:
            cc_str = cc
            if ',' in recv:
                cc = cc.split(',')
            elif ';' in recv:
                cc = cc.split(';')
            else:
                cc = [cc]
        msg['Cc'] = cc_str
    smtp = smtplib.SMTP(mail_host, port=port)  # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
    smtp.login(username, passwd)  # 登录发送者的邮箱账号，密码
    # 参数分别是 发送者，接收者，第三个是把上面的发送邮件的 内容变成字符串
    text = MIMEText(content, "plain", "utf-8")  # 使用UTF-8编码格式保证多语言的兼容性
    msg.attach(text)
    if attachment_file is not None:
        if isinstance(attachment_file, (list, tuple)):
            assert len(attachment_file) == len(attachment_name)
            for file, name in zip(attachment_file, attachment_name):
                att = MIMEBase("application", "octet-stream")
                att.set_payload(file)
                att.add_header("Content-Disposition", "attachment", filename=Header(name, "utf-8").encode())
                encoders.encode_base64(att)
                msg.attach(att)
        elif isinstance(attachment_file, bytes):
            att = MIMEBase("application", "octet-stream")
            att.set_payload(attachment_file)
            att.add_header("Content-Disposition", "attachment", filename=Header(attachment_name, "utf-8").encode())
            encoders.encode_base64(att)
            msg.attach(att)
        else:
            warnings.warn("没有对应的附件格式或者附件格式不正确")
    if cc:
        email_list = recv + cc
    else:
        email_list = recv
    for each in email_list:
        smtp.sendmail(username, each, msg.as_string())
    smtp.quit()  # 发送完毕后退出smtp

