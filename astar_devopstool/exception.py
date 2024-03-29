#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: exception.py
# @time: 2019/12/17 20:39
# @Software: PyCharm


class EmailError(ValueError):
    """
    邮件异常类
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
