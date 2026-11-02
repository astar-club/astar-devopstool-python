# astar-devopstool

[![version](https://img.shields.io/pypi/v/astar-devopstool.svg)](https://pypi.python.org/pypi/astar-devopstool)
[![gitee](https://gitee.com/snowlandltd/astar-devopstool-python/badge/star.svg)](https://gitee.com/snowlandltd/astar-devopstool-python/stargazers)
[![github](https://img.shields.io/github/stars/astar-club/astar-devopstool-python)](https://img.shields.io/github/stars/astar-club/astar-devopstool-python)
[![download](https://img.shields.io/pypi/dm/astar-devopstool.svg)](https://pypi.org/project/astar-devopstool)
[![wheel](https://img.shields.io/pypi/wheel/astar-devopstool.svg)](https://pypi.python.org/pypi/astar-devopstool)
![licence](https://img.shields.io/pypi/l/astar-devopstool.svg)
![status](https://img.shields.io/pypi/status/astar-devopstool.svg)

一组 Python 运维 / 开发辅助工具，包含 FTP/SFTP 传输、邮件发送、GitLab 提交统计、
主机监控、IP 与代理工具、版本发布通告等模块。

## 安装

项目的非核心功能以**可选依赖（extras）**形式提供，可按需安装，避免引入过重依赖：

```bash
pip install astar-devopstool            # 仅核心功能（基础库 astartool）
pip install "astar-devopstool[ssh]"     # + SFTP / SSH（依赖 paramiko）
pip install "astar-devopstool[gitlab]"  # + GitLab 统计（依赖 python-gitlab）
pip install "astar-devopstool[host]"    # + 主机监控（依赖 psutil）
pip install "astar-devopstool[all]"     # 全部可选功能
```

未安装对应可选依赖时，相关模块仍可导入，但调用具体功能会抛出清晰的
`ImportError` 并提示应安装的 extra。

## 文档

- 中文文档：[doc/README.zh.md](doc/README.zh.md)
- English documentation：[doc/README.en.md](doc/README.en.md)
- API 文档（v0.1）：[doc/api/v0.1/index.md](doc/api/v0.1/index.md)

## 许可证

Apache-2.0

## 参考资料

[1] https://github.com/ASTARCHEN/astartool

[2] https://blog.csdn.net/qq_43057091/article/details/82179301

[3] https://blog.csdn.net/qq_41841569/article/details/83824278

[4] ftp自动下载、自动上传脚本，可以递归目录操作 http://blog.csdn.net/ouyang_peng/article/details/79271113
