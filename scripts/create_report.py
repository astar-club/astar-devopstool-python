# -*- coding: utf-8 -*-

import astar_devopstool
from astar_devopstool.version_announcement import version_release_announcement_template
from astar_devopstool.common import License, LICENSE_SHORT, Language, Plantform

version_dict = {
    'project_name': 'astar_devopstool',
    'version': astar_devopstool.__version__,
    '版本': astar_devopstool.__version__,
    '日期': '2022-5-2',
    '授权协议': LICENSE_SHORT[License.BSD],
    '开发语言': Language.PYTHON.value,
    '操作系统': "跨平台",
    '分类': "运维工具、工具包",
    '开源地址-gitee': '[https://gitee.com/snowlandltd/astar-devopstool-python]'
                  '(https://gitee.com/snowlandltd/astar-devopstool-python)',
    '开源下载-pypi': '[https://pypi.org/project/astar-devopstool/]'
                 '(https://pypi.org/project/astar-devopstool/)'
}

content = """
### 新增

1. common下新增了常量和枚举类，用于选择语言、平台、开源证书等
2. readme新增导出开源许可证


### 优化

1. 邮件多发、邮件多附件发送
2. 发布公告模板优化

"""

version_release_announcement_template(version_dict, content=content, file_name="../doc/version_release/version_release_v0.0.7.md")
