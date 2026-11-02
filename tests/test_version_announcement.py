# -*- coding: utf-8 -*-
"""astar_devopstool.version_announcement 单元测试"""

from unittest import TestCase

from astar_devopstool.version_announcement import (
    version_release_announcement_template,
    generate_readme_template_md,
    generate_readme_template_rst,
    generate_readme_template,
)


class TestVersionAnnouncement(TestCase):
    def test_release_template(self):
        data = {
            'project_name': 'astar_devopstool',
            'version': '0.1',
            '日期': '2026-01-01',
        }
        out = version_release_announcement_template(
            data, content='### 新增\n1. 新功能', print_file=False
        )
        # 标题仅在写入文件时由 auto_title 生成，返回内容含信息表与更新内容
        self.assertIn('|日期|2026-01-01|', out)
        self.assertIn('## 更新内容', out)
        self.assertIn('### 新增', out)

    def test_release_template_missing_version(self):
        # 缺少 version 键应抛出 ParameterValueError
        with self.assertRaises(Exception):
            version_release_announcement_template(
                {'project_name': 'x'}, print_file=False
            )

    def test_readme_template_md(self):
        out = generate_readme_template_md('astar-devopstool', print_file=False)
        self.assertIn('# astar-devopstool', out)
        self.assertIn('pypi/v/astar-devopstool', out)

    def test_readme_template_rst(self):
        out = generate_readme_template_rst('astar-devopstool', print_file=False)
        self.assertIn('astar-devopstool', out)

    def test_readme_template_dispatch(self):
        import os
        import tempfile
        fd, path = tempfile.mkstemp(suffix='.md')
        os.close(fd)
        os.remove(path)  # 先删除，避免 auto_title 因文件已存在而交互询问
        try:
            generate_readme_template(
                'astar-devopstool', print_file=True, file_name=path,
                doc_type='markdown',
            )
            with open(path, encoding='utf-8') as f:
                content = f.read()
            self.assertIn('# astar-devopstool', content)
        finally:
            if os.path.exists(path):
                os.remove(path)
