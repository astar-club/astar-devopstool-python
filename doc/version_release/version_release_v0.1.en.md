# astar_devopstool-0.1 Released!

**Version: 0.1**
**Author:  ASTARTOOL ROBOT**
**Date:    2026-11-03 05:29:54.117363**


| Info | Value |
|:--:|:--:|
| Version | 0.1 |
| Date | 2026-11-3 |
| License | BSD License |
| Language | PYTHON |
| OS | Cross-platform |
| Category | Ops tools, utility kit |
| Gitee | [https://gitee.com/snowlandltd/astar-devopstool-python](https://gitee.com/snowlandltd/astar-devopstool-python) |
| GitHub | [https://github.com/astar-club/astar-devopstool-python](https://github.com/astar-club/astar-devopstool-python) |
| PyPI | [https://pypi.org/project/astar-devopstool/](https://pypi.org/project/astar-devopstool/) |

## What's New


### Added

1. Bilingual documentation (`doc/README.zh.md`, `doc/README.en.md`) and the 0.1 API reference (`doc/api/v0.1/index.md`)
2. GitHub Actions workflows: automated PyPI publishing and Codecov coverage reporting

### Changed

1. Version bumped to 0.1
2. Migrated packaging to modern `pyproject.toml` (PEP 621); removed `setup.py` and `requirements` files
3. Non-core features are now optional dependencies (extras: `ssh` / `gitlab` / `host` / `all`); the core only depends on `astartool`
4. Tests moved out of the package directory (`tests/`) so they are not shipped in the distribution
