# astar-devopstool 中文文档

> 版本：见 `astar_devopstool.__version__`（当前为 0.1）

## 简介

`astar-devopstool` 是一组 Python 运维 / 开发辅助工具，包含 FTP/SFTP 传输、
邮件发送、GitLab 提交统计、主机监控、IP 与代理工具、版本发布通告等模块。

为了不让包过重，**非核心功能以可选依赖（extras）的形式提供**，
你可以只安装自己需要的部分。

## 安装

```bash
# 仅核心功能（基础库 astartool）
pip install astar-devopstool

# SFTP / SSH 功能（依赖 paramiko）
pip install "astar-devopstool[ssh]"

# GitLab 统计功能（依赖 python-gitlab）
pip install "astar-devopstool[gitlab]"

# 主机监控功能（依赖 psutil）
pip install "astar-devopstool[host]"

# 安装全部可选功能
pip install "astar-devopstool[all]"
```

未安装对应可选依赖时，相关模块仍可导入，但调用具体功能会抛出清晰的
`ImportError` 并提示应安装的 extra。

## 模块说明

### common

提供常用枚举：`FTPCode`（FTP 操作返回码）、`License`、`Language`、`Plantform` 等。

### connect

基于标准库 `ftplib` 与 `paramiko` 的连接与传输工具。

- `ftp_put(file_from, file_to, host, ...)`：使用标准库 ftplib 上传文件，无需额外依赖。
- `sftp_put(...)` / `sftp_get(...)`：基于 paramiko 的 SFTP 上传 / 下载，**需安装 `[ssh]`**。
- `SSHClient(host, port=22, username, private_key_file)`：基于 paramiko 的 SSH 客户端，**需安装 `[ssh]`**。

### ftphelper

`FTPTool` 类：对 `ftplib` 的封装，支持递归上传 / 下载目录、判断文件大小是否一致等（仅依赖标准库）。

```python
from astar_devopstool.ftphelper import FTPTool

ftp = FTPTool(host='127.0.0.1', user='user', passwd='pass')
ftp.upload_file('local.txt', 'remote.txt')
ftp.close()
```

### emailtool

`send_mail(username, passwd, recv, title, content, ...)`：基于标准库
`smtplib` / `email` 的邮件发送函数，支持抄送与附件。

### gitlabhelper

`Gitlab`：继承自 `python-gitlab` 的 `Gitlab`，提供
`statistical_submission(start_time, end_time, projects=None, branches=None)`
提交统计功能，**需安装 `[gitlab]`**。

### host

主机监控工具，**需安装 `[host]`**（依赖 `psutil`）：

- `get_cpu_status()`：CPU 逻辑 / 物理核心数与使用率
- `get_memory_status()`：内存与交换分区信息
- `get_dist_usage()`：磁盘使用
- `get_net_io_conters(pernic=True)`：网络 IO 统计
- `get_web_status(URL)`：基于 `pycurl` 的 Web 服务质量探测（需额外安装 `pycurl`）

### ip

IP 与代理相关工具：`regIESettings(...)`、`get_local_ip_by_socket()`、
`get_ip_address_by_fcntl(...)` 等。

### version_announcement

版本发布通告与 README 模板生成：

- `version_release_announcement_template(...)`
- `generate_readme_template(...)` / `generate_readme_template_md(...)` / `generate_readme_template_rst(...)`

## 开发

```bash
pip install -r test-requirements.txt
pip install ".[all]"
coverage run -m unittest discover -s tests -t .
coverage report
```

## 许可证

Apache-2.0
