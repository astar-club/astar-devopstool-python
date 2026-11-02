# astar-devopstool Documentation (English)

> Version: see `astar_devopstool.__version__` (currently 0.1)

## Introduction

`astar-devopstool` is a collection of Python DevOps / development helper tools,
covering FTP/SFTP transfer, email sending, GitLab commit statistics, host
monitoring, IP & proxy utilities, and version release announcements.

To keep the package lightweight, **non-core features are provided as optional
dependencies (extras)**, so you can install only what you need.

## Installation

```bash
# Core features only (base library astartool)
pip install astar-devopstool

# SFTP / SSH features (depends on paramiko)
pip install "astar-devopstool[ssh]"

# GitLab statistics (depends on python-gitlab)
pip install "astar-devopstool[gitlab]"

# Host monitoring (depends on psutil)
pip install "astar-devopstool[host]"

# Install all optional features
pip install "astar-devopstool[all]"
```

Modules can still be imported without the corresponding optional dependency,
but calling the relevant feature raises a clear `ImportError` telling you which
extra to install.

## Modules

### common

Common enums: `FTPCode` (FTP return codes), `License`, `Language`, `Plantform`, etc.

### connect

Connection and transfer utilities based on the standard `ftplib` and `paramiko`.

- `ftp_put(file_from, file_to, host, ...)`: upload via stdlib `ftplib`, no extra dependency.
- `sftp_put(...)` / `sftp_get(...)`: SFTP upload / download via `paramiko`, **requires `[ssh]`**.
- `SSHClient(host, port=22, username, private_key_file)`: SSH client via `paramiko`, **requires `[ssh]`**.

### ftphelper

`FTPTool` class: a wrapper around `ftplib` supporting recursive upload / download
and file-size equality checks (standard library only).

```python
from astar_devopstool.ftphelper import FTPTool

ftp = FTPTool(host='127.0.0.1', user='user', passwd='pass')
ftp.upload_file('local.txt', 'remote.txt')
ftp.close()
```

### emailtool

`send_mail(username, passwd, recv, title, content, ...)`: email sending built on
the standard `smtplib` / `email`, with CC and attachment support.

### gitlabhelper

`Gitlab`: subclasses `python-gitlab`'s `Gitlab` and provides
`statistical_submission(start_time, end_time, projects=None, branches=None)`
for commit statistics, **requires `[gitlab]`**.

### host

Host monitoring utilities, **requires `[host]`** (depends on `psutil`):

- `get_cpu_status()`: CPU logical / physical cores and usage
- `get_memory_status()`: memory and swap information
- `get_dist_usage()`: disk usage
- `get_net_io_conters(pernic=True)`: network IO counters
- `get_web_status(URL)`: Web service quality probe via `pycurl` (requires `pycurl` installed)

### ip

IP and proxy utilities: `regIESettings(...)`, `get_local_ip_by_socket()`,
`get_ip_address_by_fcntl(...)`, etc.

### version_announcement

Version release announcements and README template generation:

- `version_release_announcement_template(...)`
- `generate_readme_template(...)` / `generate_readme_template_md(...)` / `generate_readme_template_rst(...)`

## Development

```bash
pip install -r test-requirements.txt
pip install ".[all]"
coverage run -m unittest discover -s tests -t .
coverage report
```

## License

Apache-2.0
