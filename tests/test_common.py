# -*- coding: utf-8 -*-
"""astar_devopstool.common 单元测试"""

from unittest import TestCase

from astar_devopstool.common import (
    FTPCode,
    License,
    Language,
    Plantform,
    LICENSE_SHORT,
)


class TestCommon(TestCase):
    def test_ftp_code_values(self):
        self.assertEqual(FTPCode.SUCCESSFUL.value, 0)
        self.assertEqual(FTPCode.IP_CANNOT_FOUND.value, 1)
        self.assertEqual(FTPCode.LOGIN_ERROR.value, 2)
        self.assertEqual(FTPCode.CANNOT_FOUND_CD.value, 3)
        self.assertEqual(FTPCode.FILE_CANNOT_READ.value, 4)

    def test_license_enum(self):
        self.assertEqual(
            License.BSD.value, 'License :: OSI Approved :: BSD License'
        )
        self.assertEqual(
            License.APACHE.value, 'License :: OSI Approved :: Apache Software License'
        )

    def test_language_enum(self):
        self.assertEqual(Language.PYTHON.value, 'PYTHON')
        self.assertEqual(Language.CPP.value, 'C++')

    def test_plantform_enum(self):
        self.assertEqual(Plantform.WINDOWS.value, 'windows')
        self.assertEqual(Plantform.LINUX.value, 'linux')
        self.assertEqual(Plantform.ALL.value, 'all')

    def test_license_short_mapping(self):
        self.assertEqual(LICENSE_SHORT[License.BSD], 'BSD License')
        self.assertEqual(LICENSE_SHORT[License.APACHE], 'Apache Software License')
        self.assertEqual(
            LICENSE_SHORT[License.GPLV3], 'GNU General Public License v3 (GPLv3)'
        )
