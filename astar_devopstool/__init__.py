#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: __init__.py.py
# @time: 2019/5/27 11:04
# @Software: PyCharm


__author__ = 'A.Star'

from astartool.setuptool import get_version

version = (0, 0, 3, 'alpha', 0)
__version__ = get_version(version)
del get_version
