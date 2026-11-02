# -*- coding: utf-8 -*-
"""astar_devopstool.emailtool 单元测试（SMTP 通过 mock 模拟，不真实发信）"""

from unittest import TestCase, mock

from astar_devopstool.emailtool import send_mail
from astar_devopstool.exception import EmailError


class TestEmailTool(TestCase):
    def test_invalid_recv_raises(self):
        # 收件人为列表时才会逐个校验格式
        with self.assertRaises(EmailError):
            send_mail('a@b.com', 'pw', ['not-an-email'], 'title', 'content')

    def test_invalid_cc_raises(self):
        with self.assertRaises(EmailError):
            send_mail('a@b.com', 'pw', 'a@b.com', 'title', 'content', cc=['bad'])

    def test_send_mail_builds_and_sends(self):
        with mock.patch('astar_devopstool.emailtool.smtplib.SMTP') as smtp_cls:
            inst = smtp_cls.return_value
            send_mail('a@b.com', 'pw', 'a@b.com', 'title', 'content')
            inst.login.assert_called_once_with('a@b.com', 'pw')
            inst.sendmail.assert_called_once()
            inst.quit.assert_called_once()

    def test_send_mail_with_attachment(self):
        with mock.patch('astar_devopstool.emailtool.smtplib.SMTP') as smtp_cls:
            inst = smtp_cls.return_value
            send_mail(
                'a@b.com',
                'pw',
                'a@b.com',
                'title',
                'content',
                attachment_file=b'data',
                attachment_name='f.txt',
            )
            inst.sendmail.assert_called_once()

    def test_send_mail_multiple_recv(self):
        with mock.patch('astar_devopstool.emailtool.smtplib.SMTP') as smtp_cls:
            inst = smtp_cls.return_value
            send_mail('a@b.com', 'pw', ['a@b.com', 'c@d.com'], 'title', 'content')
            # 每个收件人都应被调用 sendmail
            self.assertEqual(inst.sendmail.call_count, 2)
