#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: common .py
# @time: 2020/9/27 5:09
# @Software: PyCharm

from enum import Enum
from astartool.data_structure import KeyMap


class FTPCode(Enum):
    SUCCESSFUL = 0
    IP_CANNOT_FOUND = 1
    LOGIN_ERROR = 2
    CANNOT_FOUND_CD = 3
    FILE_CANNOT_READ = 4


class License(Enum):
    MIT = 'License :: OSI Approved :: MIT License'
    BSD = 'License :: OSI Approved :: BSD License'
    LGPLV2_PLUS = 'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)'
    GPL = "License :: OSI Approved :: GNU General Public License (GPL)"
    GPLV2 = "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
    GPLV2_PLUS = "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)"
    GPLV3 = "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    GPLV3_PLUS = "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    LGPLV2 = "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)"
    AGPLV3_PLUS = "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)"
    PYTHON = "License :: OSI Approved :: Python License (CNRI Python License)"
    APACHE = "License :: OSI Approved :: Apache Software License"


class Language(Enum):
    PYTHON = 'PYTHON'
    JULIA = 'JULIA'
    MATLAB = 'MATLAB'
    JAVASCRIPT = 'JAVASCRIPT'
    JAVA = 'JAVA'
    CSHARP = 'C#'
    HTML = 'HTML'
    CSS = 'CSS'
    CPP = 'C++'
    C = 'C'
    PHP = 'PHP'


class Plantform(Enum):
    MACOS = 'mac'
    WINDOWS = 'windows'
    LINUX = 'linux'
    UNIX = 'unix'
    ALL = 'all'

LICENSE_SHORT = KeyMap({
    License.MIT: 'MIT License',
    License.BSD: 'BSD License',
    License.LGPLV2_PLUS: 'GNU Lesser General Public License v2 or later (LGPLv2+)',
    License.GPL: "GNU General Public License (GPL)",
    License.GPLV2: "GNU General Public License v2 (GPLv2)",
    License.GPLV2_PLUS: "GNU General Public License v2 or later (GPLv2+)",
    License.GPLV3: "GNU General Public License v3 (GPLv3)",
    License.GPLV3_PLUS: "GNU General Public License v3 or later (GPLv3+)",
    License.LGPLV2: "GNU Lesser General Public License v2 (LGPLv2)",
    License.AGPLV3_PLUS: "GNU Affero General Public License v3 or later (AGPLv3+)",
    License.PYTHON: "Python License (CNRI Python License)",
    License.APACHE: "Apache Software License"
}
)


