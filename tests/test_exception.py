# -*- coding: utf-8 -*-
"""astar_devopstool.exception 单元测试"""

from unittest import TestCase

from astar_devopstool.exception import EmailError


class TestException(TestCase):
    def test_is_value_error(self):
        self.assertTrue(issubclass(EmailError, ValueError))

    def test_can_be_raised(self):
        with self.assertRaises(EmailError):
            raise EmailError('邮件格式错误')

    def test_message_preserved(self):
        err = EmailError('bad email')
        self.assertEqual(str(err), 'bad email')
