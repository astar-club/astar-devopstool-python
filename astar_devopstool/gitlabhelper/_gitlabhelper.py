#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: _gitlabhelper.py
# @time: 2022/01/04 15:15
# @Software: PyCharm
import datetime
import re

import gitlab.v4.objects.branches
from gitlab.v4.objects.commits import ProjectCommit
from gitlab import Gitlab as PyGitlab
from collections import Counter


class Gitlab(PyGitlab):
    def __init__(self, *args, **kwargs):
        super(Gitlab, self).__init__(*args, **kwargs)

    def statistical_submission(self, start_time: (str, datetime.datetime) = '2021-02-20',
                               end_time: (str, datetime.datetime) = None,
                               projects=None,
                               branches=None):
        """
        统计提交
        :param start_time:
        :param print_file:
        :param file_name:
        :param encoding:
        :param projects:
        :param branches:
        :return:
        """
        if isinstance(start_time, (datetime.datetime, datetime.date)):
            start_time = start_time.strftime('%Y-%m-%d')
        if isinstance(end_time, (datetime.datetime, datetime.date)):
            end_time = end_time.strftime('%Y-%m-%d')
        assert re.match(r'\d{4}-\d{2}-\d{2}', start_time) is not None, "start_time 应为yyyy-mm-dd格式"
        assert re.match(r'\d{4}-\d{2}-\d{2}', end_time) is not None, "end_time 应为yyyy-mm-dd格式"
        # 先把所有项目查出来，all=True 一定要加上。不然查出来的只有第一页项目
        if projects is None or (isinstance(projects, str) and projects.lower() == 'all'):
            projects = self.projects.list(all=True)
        else:
            # 已经传入了projects
            pass
        # 遍历每一个项目
        result = {}
        for project in projects:
            # 把每个项目下面的所有分支查出来
            if branches is None:
                branches = project.branches.list()

            # 然后再遍历每一个分支
            commits_set = set()
            for branch in branches:
                # 获取一段时间内，指定分支的 commits
                if isinstance(branch, gitlab.v4.objects.branches.ProjectBranch):
                    query_parameters = {'since': start_time, 'until': end_time,
                                        'ref_name': branch.name}
                elif isinstance(branch, str):
                    query_parameters = {'since': start_time, 'until': end_time,
                                        'ref_name': branch}
                else:
                    raise ValueError('branch 参数错误')
                commits = project.commits.list(all=True, query_parameters=query_parameters)
                commits_set.update(commits)
            # 然后再遍历每个提交记录，查询每个提交记录的人和量
            for commit in commits_set:
                author_name = commit.author_name
                com = project.commits.get(commit.id)
                # 提交代码 增量、删除、总量
                stats = Counter(com.stats)
                if author_name in result:
                    result[author_name] += stats
                else:
                    result[author_name] = stats
        return result


