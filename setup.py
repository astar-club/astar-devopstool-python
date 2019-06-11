#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: setup.py.py
# @time: 2019/5/27 11:04
# @Software: PyCharm


__author__ = 'A.Star'


from setuptools import setup, find_packages
import astar_devopstool
from astartool.setuptool import load_install_requires


setup(
    name="astar-devopstool",
    version=astar_devopstool.__version__,
    description=(
        'Python devopstool'
    ),
    long_description=open('description.rst').read(),
    author='A.Star',
    author_email='astar@snowland.ltd',
    maintainer='A.Star',
    maintainer_email='astar@snowland.ltd',
    license='Apache v2.0 License',
    packages=find_packages(),
    platforms=["all"],
    url='http://182.61.50.242:10010/thirdparty/astar-devopstool-python',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=load_install_requires(),
)