#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: ip.py
# @time: 2019/6/4 9:49
# @Software: PyCharm
import getopt
import os
import re
import socket
import struct
import sys

try:
    import fcntl
except ImportError:
    pass
__author__ = 'A.Star'

'''
  # Title   : setRegProxy
  # Author  : Solomon Xie
  # Utility : Via Registry key of windows, change proxy settings of IE on Windows.
  # Require : Python 2.x, Windows 7
  # Reg Path: HKUC\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections
  # Anlysis : 注册表的二进制值(及关键信息)如下："46 00 00 00 00 00 00 00 开关 00 00 00 IP长度 00 00 00 IP地址 00 00 00 是否跳过本地代理 21 00 00 00 PAC地址"
  # Method  : 通过在cmd中导入reg文件的方式执行并立即生效。
  # Notes   : - 二进制值的设置选项在代码中已经体现了。本代码可以根据需要自动设置代理。
  # switcher: 开关：0F全部开启(ALL)；01全部禁用(Off)
              03使用代理服务器(ProxyOnly)；05使用自动脚本(PacOnly)；
              07使用脚本和代理(ProxyAndPac)；09自动检测设置(D)；
              0B自动检测并使用代理(DIP)；0D自动检测并使用脚本(DS)；
'''


def regIESettings(op, noLocal=False, ip='', pac='http://xduotai.com/pRsO3NGR3-.pac'):
    """
      根据需求生成Windows代理设置注册表的.reg文件内容
      DefaultConnectionSettings项是二进制项
      而具体这个二进制文件怎么解析，在收藏的PDF中有详细解释。
    """
    if not op: return
    # 如果是设置IP代理的模式 则检查IP地址的有效性(允许为空，但不允许格式错误)
    if 'Proxy' in op and not ip == '':
        # if len(extractIp(ip))==0
        if 1 > len(re.findall('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s*:{0,1}\s*([0-9]{1,5}){0,1}', ip)):
            # print('---Unexpected IP Address:%s---' % ip)
            return
    options = {'On': '0F', 'Off': '01', 'ProxyOnly': '03', 'PacOnly': '05', 'ProxyAndPac': '07', 'D': '09', 'DIP': '0B',
               'DS': '0D'}
    if op == 'Off':
        reg_value = '46,00,00,00,00,00,00,00,01'
    else:
        switcher = options.get(op)
        if not switcher:
            # print( '\n---Unexpected Option. Please check the value after [-o]---\n')
            return
        skipLocal = '07,00,00,00,%s' % __toHex('<local>') if noLocal else '00'
        reg_value = '46,00,00,00,00,00,00,00,%(switcher)s,00,00,00,%(ipLen)s,00,00,00,%(ip)s00,00,00,%(skipLocal)s,21,00,00,00%(pac)s' % (
            {'switcher': switcher, 'ipLen': __toHex(len(ip)), 'ip': __toHex(ip) + ',' if ip else '',
             'infoLen': __toHex(len('<local>')), 'skipLocal': skipLocal, 'pac': ',' + __toHex(pac) if pac else ''})
    settings = 'Windows Registry Editor Version 5.00\n[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections]\n"DefaultConnectionSettings"=hex:%s' % reg_value
    # print 'Using proxy address: %s' % ip
    # print(op, ip, pac)
    # print(options[op] + '\n' + __toHex(ip) + '\n' + __toHex(pac))
    # print(settings)
    # === 生成reg文件并导入到注册表中 ===
    filePath = '%s\DefaultConnectionSettings.reg' % os.getcwd()
    with open(filePath, 'w') as f:
        f.write(settings)
    cmd = 'reg import "%s"' % filePath
    result = os.popen(cmd)
    # if len(result.readlines()) < 2:
    #     print('---Successfully import proxy into Registry on this machine.---')
    return


def get_local_ip_by_socket():
    """
    获取本地IP(通过socket)
    :return:
    """
    name = socket.getfqdn(socket.gethostname())
    return socket.gethostbyname(name)


def get_ip_address_by_fcntl(ifname='eth0'):
    """
    通过fcntl获取IP
    :param ifname:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def __toHex(obj):
    if obj == '':
        return ''
    elif obj == 0 or obj == '0' or obj == '00':
        return '00'
    if isinstance(obj, str):
        rehex = (str(hex(ord(s))).replace('0x', '') for s in obj)
        return ','.join(rehex)
    elif isinstance(obj, int):
        num = str(hex(obj)).replace('0x', '')
        return num if len(num) > 1 else '0' + num  # 如果是一位数则自动补上0，7为07，e为0e


if __name__ == '__main__':
    # 获取文件外部参数
    # 用法：在命令行中输入./ip.py -o "ProxyOnly" -l --proxy"0.0.0.0:80" -l
    opts, args = getopt.getopt(sys.argv[1:], 'o:p:a:l', ['option=', 'proxy=', 'pac=', 'local'])
    # print(opts, args)  # 调试用
    if len(opts) > 0:
        op, ip, pac = '', '', ''
        noLocal = False
        for o, a in opts:
            if o == '-o' or o == '--option':
                op = a
            elif o == '-p' or o == '--proxy':
                ip = a
            elif o == '-a' or o == '--pac':
                pac = a
            elif o == '-l' or o == '--local':
                noLocal = False
        pac = 'http://xduotai.com/pRsO3NGR3-.pac' if not pac else pac
        if op == 'ProxyOff':
            regIESettings(op='Off', ip=ip, pac=pac, noLocal=noLocal)
            regIESettings(op='PacOnly', ip=ip, pac=pac, noLocal=noLocal)
        elif op == 'PacOff':
            regIESettings(op='Off', ip=ip, pac=pac, noLocal=noLocal)
            regIESettings(op='ProxyOnly', ip=ip, pac=pac, noLocal=noLocal)
        else:
            regIESettings(op=op, ip=ip, pac=pac, noLocal=noLocal)
