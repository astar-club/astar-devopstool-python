# astar_devopstool-0.1已发布！

**Version: 0.1**
**Auth:    ASTARTOOL ROBOT**
**Date:    2026-11-03 05:29:54.117363**


|信息|值|
|:--:|:--:|
|版本|0.1|
|日期|2026-11-3|
|授权协议|BSD License|
|开发语言|PYTHON|
|操作系统|跨平台|
|分类|运维工具、工具包|
|开源地址-gitee|[https://gitee.com/snowlandltd/astar-devopstool-python](https://gitee.com/snowlandltd/astar-devopstool-python)|
|开源地址-github|[https://github.com/astar-club/astar-devopstool-python](https://github.com/astar-club/astar-devopstool-python)|
|开源下载-pypi|[https://pypi.org/project/astar-devopstool/](https://pypi.org/project/astar-devopstool/)|

## 更新内容


### 新增

1. 中英文文档（doc/README.zh.md、doc/README.en.md）与 0.1 版 API 文档（doc/api/v0.1/index.md）
2. GitHub Actions 工作流：PyPI 自动发布与 Codecov 覆盖率统计

### 变更

1. 版本升级至 0.1
2. 安装方式迁移到现代 pyproject.toml（PEP 621），移除 setup.py 与 requirements 文件
3. 非核心功能改为可选依赖（extras：ssh / gitlab / host / all），核心仅依赖 astartool
4. 测试移出包目录（tests/），避免被打入发行版


