# -*- coding: utf-8 -*-
"""版本号相关的单元测试"""

from unittest import TestCase

from astar_devopstool import __version__
from astar_devopstool.version_announcement import get_version


class TestVersion(TestCase):
    def test_package_version(self):
        self.assertEqual(__version__, '0.1')

    def test_get_version(self):
        self.assertEqual(get_version((0, 1, 0, 'final', 0)), '0.1')
        self.assertEqual(get_version((1, 2, 3, 'final', 0)), '1.2.3')
