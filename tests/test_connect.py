# -*- coding: utf-8 -*-
"""astar_devopstool.connect 单元测试（FTP/SFTP/SSH 通过 mock 模拟）"""

import socket
from unittest import TestCase, mock, skipUnless

from astar_devopstool import connect
from astar_devopstool.common import FTPCode

HAS_PARAMIKO = False
try:
    import paramiko  # noqa: F401
    HAS_PARAMIKO = True
except ImportError:
    pass


class TestConnect(TestCase):
    def test_ftp_put_connection_failure(self):
        with mock.patch('ftplib.FTP', side_effect=socket.error('boom')):
            r = connect.ftp_put('a.txt', '/remote', '192.0.2.1')
        self.assertEqual(r, FTPCode.IP_CANNOT_FOUND.value)

    def test_ftp_put_success(self):
        fake_ftp = mock.MagicMock()
        with mock.patch('ftplib.FTP', return_value=fake_ftp), \
                mock.patch('builtins.open', mock.mock_open(read_data=b'data')):
            r = connect.ftp_put('a.txt', '/remote', 'host')
        self.assertEqual(r, FTPCode.SUCCESSFUL.value)
        fake_ftp.storbinary.assert_called_once()
        fake_ftp.quit.assert_called_once()

    def test_sftp_put_requires_paramiko(self):
        with mock.patch.object(connect, 'paramiko_flag', False):
            with self.assertRaises(ImportError):
                connect.sftp_put('a', 'b', 'host')

    def test_sftp_get_requires_paramiko(self):
        with mock.patch.object(connect, 'paramiko_flag', False):
            with self.assertRaises(ImportError):
                connect.sftp_get('a', 'b', 'host')

    def test_ssh_requires_paramiko(self):
        with mock.patch.object(connect, 'paramiko_flag', False):
            with self.assertRaises(ImportError):
                connect.SSHClient('host')

    @skipUnless(HAS_PARAMIKO, 'paramiko not installed')
    @mock.patch.object(connect, 'paramiko_flag', True)
    @mock.patch('paramiko.SSHClient', return_value=mock.MagicMock())
    @mock.patch('paramiko.RSAKey.from_private_key_file', return_value=mock.MagicMock())
    @mock.patch('paramiko.Transport', return_value=mock.MagicMock())
    def test_ssh_success(self, *_):
        connect.SSHClient('host', private_key_file='key.pem')
        from paramiko import SSHClient
        SSHClient.return_value.exec_command.assert_called_once_with('df')

    @skipUnless(HAS_PARAMIKO, 'paramiko not installed')
    @mock.patch.object(connect, 'paramiko_flag', True)
    @mock.patch('paramiko.SFTPClient.from_transport', return_value=mock.MagicMock())
    @mock.patch('paramiko.Transport', return_value=mock.MagicMock())
    def test_sftp_put_success(self, *_):
        connect.sftp_put('a', 'b', 'host')
        from paramiko import SFTPClient
        SFTPClient.from_transport.return_value.put.assert_called_once_with('a', 'b')

    @skipUnless(HAS_PARAMIKO, 'paramiko not installed')
    @mock.patch.object(connect, 'paramiko_flag', True)
    @mock.patch('paramiko.SFTPClient.from_transport', return_value=mock.MagicMock())
    @mock.patch('paramiko.Transport', return_value=mock.MagicMock())
    def test_sftp_get_success(self, *_):
        connect.sftp_get('a', 'b', 'host')
        from paramiko import SFTPClient
        SFTPClient.from_transport.return_value.get.assert_called_once_with('a', 'b')
