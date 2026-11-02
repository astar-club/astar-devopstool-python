# -*- coding: utf-8 -*-
"""astar_devopstool.ftphelper.FTPTool 单元测试（FTP 连接通过 mock 模拟）"""

from unittest import TestCase, mock

from astar_devopstool.ftphelper import FTPTool


class TestFTPTool(TestCase):
    def test_get_file_name(self):
        tool = FTPTool.__new__(FTPTool)
        tool.log_file = None
        line = "drwxr-xr-x   2 user group   4096 Jan 01 10:00 mydir"
        arr = tool.get_file_name(line)
        self.assertEqual(arr[0], 'd')
        self.assertEqual(arr[1], 'mydir')

    def test_get_file_list_excludes_dot(self):
        tool = FTPTool.__new__(FTPTool)
        tool.log_file = None
        tool.file_list = []
        tool.get_file_list("drwxr-xr-x   2 user group 4096 Jan 01 10:00 .")
        tool.get_file_list("drwxr-xr-x   2 user group 4096 Jan 01 10:00 ..")
        tool.get_file_list("drwxr-xr-x   2 user group 4096 Jan 01 10:00 real")
        self.assertEqual(tool.file_list, [['d', 'real']])

    def test_is_same_size(self):
        tool = FTPTool.__new__(FTPTool)
        tool.log_file = None
        tool.ftp = mock.MagicMock()
        tool.ftp.size.return_value = 100
        with mock.patch(
            'astar_devopstool.ftphelper._ftphelper.os.path.getsize',
            return_value=100,
        ):
            self.assertTrue(tool.is_same_size('local', 'remote'))
        with mock.patch(
            'astar_devopstool.ftphelper._ftphelper.os.path.getsize',
            return_value=50,
        ):
            self.assertFalse(tool.is_same_size('local', 'remote'))

    def test_upload_file(self):
        tool = FTPTool.__new__(FTPTool)
        tool.log_file = None
        tool.ftp = mock.MagicMock()
        with mock.patch(
            'astar_devopstool.ftphelper._ftphelper.os.path.isfile',
            return_value=True,
        ), mock.patch('builtins.open', mock.mock_open(read_data=b'x')):
            tool.upload_file('local.txt', 'remote.txt')
        tool.ftp.storbinary.assert_called_once()

    def test_download_file_skip_if_same(self):
        tool = FTPTool.__new__(FTPTool)
        tool.log_file = None
        tool.ftp = mock.MagicMock()
        tool.ftp.size.return_value = 100
        with mock.patch(
            'astar_devopstool.ftphelper._ftphelper.os.path.getsize',
            return_value=100,
        ):
            tool.download_file('local.txt', 'remote.txt')
        tool.ftp.retrbinary.assert_not_called()

    def test_download_file(self):
        tool = FTPTool.__new__(FTPTool)
        tool.log_file = None
        tool.ftp = mock.MagicMock()
        tool.ftp.size.return_value = 0
        with mock.patch(
            'astar_devopstool.ftphelper._ftphelper.os.path.getsize',
            return_value=50,
        ), mock.patch('builtins.open', mock.mock_open()):
            tool.download_file('local.txt', 'remote.txt')
        tool.ftp.retrbinary.assert_called_once()

    def test_construction(self):
        fake_ftp = mock.MagicMock()
        with mock.patch(
            'astar_devopstool.ftphelper._ftphelper.FTP', return_value=fake_ftp
        ):
            tool = FTPTool('host', user='u', passwd='p')
        self.assertEqual(tool.host, 'host')
        self.assertEqual(tool.port, 21)
        fake_ftp.connect.assert_called()
