#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo.py
# @time: 2019/5/27 11:15
# @Software: PyCharm


__author__ = 'A.Star'

from astar_devopstool.host import *


if __name__ == '__main__':
    code = get_web_status('www.baidu.com')
    print(get_web_status_report(*code))
