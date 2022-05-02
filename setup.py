#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: setup.py.py
# @time: 2019/5/27 11:04
# @Software: PyCharm


__author__ = 'A.Star'

from setuptools import find_packages
import astar_devopstool
from astar_devopstool.common import License, Plantform
from astartool.setuptool import load_install_requires, setup

setup(
    name="astar-devopstool",
    version=astar_devopstool.__version__,
    description=(
        'Python devopstool'
    ),
    long_description=open('README.rst', encoding='utf-8').read(),
    author='A.Star',
    author_email='astar@snowland.ltd',
    maintainer='A.Star',
    maintainer_email='astar@snowland.ltd',
    license='Apache v2.0 License',
    packages=find_packages(),
    platforms=[Plantform.ALL.value],
    url='https://github.com/astar-club/astar-devopstool-python',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        License.BSD.value,
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=load_install_requires(),

)
