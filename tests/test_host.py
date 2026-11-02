# -*- coding: utf-8 -*-
"""astar_devopstool.host 单元测试（psutil/pycurl 通过 mock 或守卫测试）"""

from unittest import TestCase, mock

from astar_devopstool import host


class TestHost(TestCase):
    def test_web_status_report(self):
        s = host.get_web_status_report(
            200, 0.01, 0.02, 0.03, 0.04, 0.05, 1024, 256, 2048
        )
        self.assertIn('HTTP状态码：200', s)
        self.assertIn('DNS解析时间：10.00', s)
        self.assertIn('平均下载速度：2048', s)

    def test_mac_address(self):
        mac = host.get_mac_address()
        self.assertEqual(len(mac), 12)
        self.assertTrue(all(c in '0123456789abcdef' for c in mac))

    def test_cpu_status_requires_psutil(self):
        with mock.patch.object(host, 'psutil_flag', False):
            with self.assertRaises(ImportError):
                host.get_cpu_status()

    def test_memory_status_requires_psutil(self):
        with mock.patch.object(host, 'psutil_flag', False):
            with self.assertRaises(ImportError):
                host.get_memory_status()

    def test_dist_usage_requires_psutil(self):
        with mock.patch.object(host, 'psutil_flag', False):
            with self.assertRaises(ImportError):
                host.get_dist_usage()

    def test_net_io_requires_psutil(self):
        with mock.patch.object(host, 'psutil_flag', False):
            with self.assertRaises(ImportError):
                host.get_net_io_conters()

    def test_web_status_requires_pycurl(self):
        with mock.patch.object(host, 'pycurl_import_flag', False):
            with self.assertRaises(ImportError):
                host.get_web_status()

    def test_dist_status(self):
        fake = mock.MagicMock()
        fake.readlines.return_value = ['/dev/sda1  100G  50G  50G  50% /\n']
        with mock.patch('astar_devopstool.host.os.popen', return_value=fake):
            r = host.get_dist_status()
        self.assertIn('/dev/sda1', r)
