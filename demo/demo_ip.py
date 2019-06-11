#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo_ip.py
# @time: 2019/6/4 10:08
# @Software: PyCharm


__author__ = 'A.Star'

import warnings
import subprocess
import time


warnings.filterwarnings("ignore")

# url = 'https://www.hizhi.vip/m_index.html'
url = 'http://www.snowland.ltd'


def ping(cmd='ping 180.76.145.168'):
    while 1:
        st = time.clock()
        sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        sub.wait()
        et = time.clock()
        print(et-st)
    # print(sub.read()
