#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: version .py
# @time: 2020/12/4 14:44
# @Software: PyCharm

from astartool.setuptool import get_version, get_docs_version, get_complete_version, get_main_version, \
    get_git_changeset, get_version_tuple

__all__ = [
    'get_version',
    'get_main_version',
    'get_complete_version',
    'get_docs_version',
    'get_git_changeset',
    'get_version_tuple'
]
