#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: test_version .py
# @time: 2020/12/4 15:15
# @Software: PyCharm

from unittest import TestCase
from astartool.project._decorators import std_logging
from astar_devopstool.version_announcement._report import generate_readme_template
import os

osp = os.path


class TestVersion(TestCase):
    @std_logging()
    def setUp(self):
        pass

    @std_logging()
    def tearDown(self):
        pass

    def test_docs(self):
        """
        测试能否正常输出
        :return:
        """
        real_path = osp.realpath(__file__)
        # 当前文件所在的目录，即父路径
        father_path = osp.split(real_path)[0]

        docs = generate_readme_template('astar-devopstool-python',
                                        pypi_name='astar-devopstool',
                                        print_file=True,
                                        file_name=osp.join(father_path, 'readme.md')
                                        )
        print(docs)
