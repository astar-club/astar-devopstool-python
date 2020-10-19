#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: common .py
# @time: 2020/9/27 5:09
# @Software: PyCharm

from enum import Enum


class FTPCode(Enum):
    SUCCESSFUL = 0
    IP_CANNOT_FOUND = 1
    LOGIN_ERROR = 2
    CANNOT_FOUND_CD = 3
    FILE_CANNOT_READ = 4