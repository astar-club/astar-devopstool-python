# -*- coding: utf-8 -*-
"""astar_devopstool.ip 单元测试（网络/注册表操作通过 mock 模拟）"""

import sys
import socket
import importlib
from unittest import TestCase, mock

import astar_devopstool.ip as ip


class TestIp(TestCase):
    def test_tohex_empty(self):
        self.assertEqual(getattr(ip, '__toHex')(''), '')

    def test_tohex_str(self):
        # ord('A') = 65 = 0x41 ; 'ab' -> 61,62
        self.assertEqual(getattr(ip, '__toHex')('A'), '41')
        self.assertEqual(getattr(ip, '__toHex')('ab'), '61,62')

    def test_tohex_int(self):
        self.assertEqual(getattr(ip, '__toHex')(0), '00')
        self.assertEqual(getattr(ip, '__toHex')(7), '07')
        self.assertEqual(getattr(ip, '__toHex')(255), 'ff')

    def test_get_local_ip_by_socket(self):
        with mock.patch('socket.getfqdn', return_value='myhost'), \
                mock.patch('socket.gethostbyname', return_value='10.0.0.5'):
            self.assertEqual(ip.get_local_ip_by_socket(), '10.0.0.5')

    def test_reg_iesettings_empty_op(self):
        self.assertIsNone(ip.regIESettings(''))

    def test_reg_iesettings_invalid_ip(self):
        self.assertIsNone(ip.regIESettings('ProxyOnly', ip='999.999.999.999'))

    def test_reg_iesettings_off(self):
        m = mock.mock_open()
        with mock.patch('builtins.open', m), \
                mock.patch('astar_devopstool.ip.os.popen') as popen, \
                mock.patch('astar_devopstool.ip.os.getcwd', return_value='/tmp'):
            r = ip.regIESettings('Off')
        self.assertIsNone(r)
        written = m().write.call_args[0][0]
        self.assertIn('46,00,00,00,00,00,00,00,01', written)
        popen.assert_called_once()

    def test_get_ip_by_fcntl(self):
        fake_fcntl = mock.MagicMock()
        packed = socket.inet_aton('192.168.1.10')
        fake_fcntl.ioctl.return_value = b'\x00' * 20 + packed
        with mock.patch.dict(sys.modules, {'fcntl': fake_fcntl}):
            importlib.reload(ip)
            try:
                with mock.patch('socket.socket') as sock_cls:
                    sock = sock_cls.return_value
                    sock.fileno.return_value = 3
                    result = ip.get_ip_address_by_fcntl('eth0')
                self.assertEqual(result, '192.168.1.10')
                fake_fcntl.ioctl.assert_called_once()
            finally:
                importlib.reload(ip)
