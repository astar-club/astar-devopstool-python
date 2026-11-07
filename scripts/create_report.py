# -*- coding: utf-8 -*-

import astar_devopstool
from astar_devopstool.version_announcement import version_release_announcement_template
from astar_devopstool.common import License, LICENSE_SHORT, Language, Plantform

version_dict = {
    'project_name': 'astar_devopstool',
    'version': astar_devopstool.__version__,
    '版本': astar_devopstool.__version__,
    '日期': '2026-11-3',
    '授权协议': LICENSE_SHORT[License.BSD],
    '开发语言': Language.PYTHON.value,
    '操作系统': "跨平台",
    '分类': "运维工具、工具包",
    '开源地址-gitee': '[https://gitee.com/snowlandltd/astar-devopstool-python]'
                  '(https://gitee.com/snowlandltd/astar-devopstool-python)',
    '开源地址-github': '[https://github.com/astar-club/astar-devopstool-python]'
                   '(https://github.com/astar-club/astar-devopstool-python)',
    '开源下载-pypi': '[https://pypi.org/project/astar-devopstool/]'
                 '(https://pypi.org/project/astar-devopstool/)'
}

content = """
### 新增

1. 中英文文档（doc/README.zh.md、doc/README.en.md）与 0.1 版 API 文档（doc/api/v0.1/index.md）
2. GitHub Actions 工作流：PyPI 自动发布与 Codecov 覆盖率统计

### 变更

1. 版本升级至 0.1
2. 安装方式迁移到现代 pyproject.toml（PEP 621），移除 setup.py 与 requirements 文件
3. 非核心功能改为可选依赖（extras：ssh / gitlab / host / all），核心仅依赖 astartool
4. 测试移出包目录（tests/），避免被打入发行版

"""

version_release_announcement_template(version_dict, content=content, file_name="../doc/version_release/version_release_v0.1.md")
