#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: tool.py
# @time: 2019/5/27 11:06
# @Software: PyCharm


__author__ = 'A.Star'

import os
import sys

import psutil
try:
    import pycurl

    pycurl_import_flag = True
except:
    pycurl_import_flag = False


def get_dist_status():
    """
    得到磁盘使用情况
    :return:
    """
    disk_status = os.popen('df -h').readlines()
    return ''.join(disk_status)


def get_web_status(URL="www.snowland.ltd"):
    """
    该脚本可以定位访问web页面的服务质量
    通过Python下的pycurl模块来实现定位
    它可以通过调用pycurl提供的方法，来探测Web服务质量
    比如了解相应的HTTP状态码、请求延时、HTTP头信息、下载速度等

    :param 探测目标URL

    """
    if not pycurl_import_flag:
        raise ImportError('please install pycurl')
    # 创建一个Curl对象
    c = pycurl.Curl()
    # 定义请求的URL变量
    c.setopt(pycurl.URL, URL)
    # 定义请求连接的等待时间
    c.setopt(pycurl.CONNECTTIMEOUT, 5)
    # 定义请求超时时间
    c.setopt(pycurl.TIMEOUT, 5)
    # 屏蔽下载进度条
    c.setopt(pycurl.FORBID_REUSE, 1)
    # 指定HTTP重定向的最大数为1
    c.setopt(pycurl.MAXREDIRS, 1)
    # 完成交互后强制断开连接，不重用
    c.setopt(pycurl.NOPROGRESS, 1)
    # 设置保存DNS信息的时间为30秒
    c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)

    # 创建一个文件对象，以“wb”方式打开，用来存储返回的http头部及页面的内容
    indexfile = open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt", "wb")
    # 将返回的HTTP HEADER定向到indexfile文件
    c.setopt(pycurl.WRITEHEADER, indexfile)
    # 将返回的HTML内容定向到indexfile文件
    c.setopt(pycurl.WRITEDATA, indexfile)

    # 捕捉Curl.perform请求的提交，如果错误直接报错退出
    try:
        c.perform()
    except ConnectionError as e:
        print("连接错误")
        indexfile.close()
        c.close()
        sys.exit()

    # DNS解析所消耗的时间
    NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
    # 建立连接所消耗的时间
    CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
    # 从建立连接到准备传输所消耗的时间
    PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
    # 从建立连接到传输开始消耗的时间
    STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
    # 传输结束所消耗的总时间
    TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
    # 返回HTTP状态码
    HTTP_CODE = c.getinfo(c.HTTP_CODE)
    # 下载数据包的大小
    SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
    # HTTP头部大小
    HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
    # 平均下载速度
    SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

    indexfile.close()
    c.close()
    return HTTP_CODE, NAMELOOKUP_TIME, CONNECT_TIME, PRETRANSFER_TIME, STARTTRANSFER_TIME, TOTAL_TIME, SIZE_DOWNLOAD, HEADER_SIZE, SPEED_DOWNLOAD


def get_web_status_report(HTTP_CODE, NAMELOOKUP_TIME, CONNECT_TIME, PRETRANSFER_TIME, STARTTRANSFER_TIME, TOTAL_TIME,
                          SIZE_DOWNLOAD, HEADER_SIZE, SPEED_DOWNLOAD):
    return """\
    HTTP状态码：%d 
    DNS解析时间：%.2f ms 
    建立连接时间：%.2f ms 
    准备传输时间：%.2f ms 
    传输开始时间：%.2f ms 
    传输结束总时间：%.2f ms 
    下载数据包大小：%d bytes/s 
    HTTP头部大小：%d byte 
    平均下载速度：%d bytes/s """ % (
    HTTP_CODE, NAMELOOKUP_TIME * 1000, CONNECT_TIME * 1000, PRETRANSFER_TIME * 1000, STARTTRANSFER_TIME * 1000,
    TOTAL_TIME * 1000, SIZE_DOWNLOAD, HEADER_SIZE, SPEED_DOWNLOAD)


def get_cpu_status():
    """CPU信息
    :return CPU逻辑数量,
    :return CPU物理核心
    :return CPU当前使用率"""
    return psutil.cpu_count(), psutil.cpu_count(logical=False), psutil.cpu_percent()  #


def get_memory_status():
    """\
    内存信息
    :return 系统总计内存
    :return 系统已经使用内存
    :return 系统空闲内存
    :return swap内存信息"""
    mem = psutil.virtual_memory()  # 实例化内存对象
    return mem.total, mem.used, mem.free, psutil.swap_memory()


def get_dist_usage():
    """得到硬盘使用"""
    return psutil.disk_usage('/')


def get_net_io_conters(pernic=True):
    """得到网络信息"""
    return psutil.net_io_counters(pernic=pernic)

