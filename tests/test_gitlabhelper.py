# -*- coding: utf-8 -*-
"""astar_devopstool.gitlabhelper.Gitlab 单元测试（GitLab API 通过 mock 模拟）"""

from unittest import TestCase, mock, skipUnless

from astar_devopstool.gitlabhelper import Gitlab
from astar_devopstool.gitlabhelper import _gitlabhelper as gitlab_mod

HAS_GITLAB = False
try:
    import gitlab  # noqa: F401
    HAS_GITLAB = True
except ImportError:
    pass


class TestGitlabHelper(TestCase):
    def test_init_requires_gitlab(self):
        with mock.patch.object(gitlab_mod, 'gitlab_flag', False):
            with self.assertRaises(ImportError):
                Gitlab('https://gitlab.com', 'token')

    @skipUnless(HAS_GITLAB, 'python-gitlab not installed')
    @mock.patch.object(gitlab_mod, 'gitlab_flag', True)
    def test_statistical_submission(self, *_):
        gl = Gitlab.__new__(Gitlab)

        fake_commit = mock.MagicMock()
        fake_commit.author_name = 'Alice'
        fake_commit.id = 'abc'
        fake_commit.stats = {'additions': 1, 'deletions': 2, 'total': 3}

        fake_com = mock.MagicMock()
        fake_com.stats = {'additions': 1, 'deletions': 2, 'total': 3}

        fake_project = mock.MagicMock()
        fake_project.branches.list.return_value = []
        fake_project.commits.list.return_value = [fake_commit]
        fake_project.commits.get.return_value = fake_com

        fake_projects = mock.MagicMock()
        fake_projects.list.return_value = [fake_project]

        gl.projects = fake_projects

        result = gl.statistical_submission(
            '2021-01-01', '2021-12-31', projects='all', branches=['main']
        )
        self.assertIn('Alice', result)
        self.assertEqual(result['Alice']['total'], 3)
        self.assertEqual(result['Alice']['additions'], 1)
