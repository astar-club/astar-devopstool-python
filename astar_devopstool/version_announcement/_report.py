#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: report .py
# @time: 2020/12/4 14:45
# @Software: PyCharm


from astartool.project import auto_title

def version_release_announcement_template(
        data_dict:dict,
        print_file=True,
        file_name=None,
        *,encoding='utf-8'
) -> str:
    """
    发布通告模板
    :param data_dict:
    :param print_file:
    :param file_name:
    :param encoding:
    :return:
    """
    s = ["|"+str(k)+"|"+str(v)+"|" for k, v in data_dict]
    docs = '|信息|值|\n' +\
           '|:--:|:--:|\n' +\
           "\n".join(s)

    if print_file:
        auto_title(file_name, encoding=encoding)
        with open(file_name, "a+", encoding=encoding) as f:

            f.write(docs)
    return docs


def generate_readme_template(
        project_name,
        pypi_name=None,
        print_file=True,
        file_name=None,
        gitee=None,
        github=None,
        gitee_name=None,
        github_name=None,
        gitee_url=None,
        github_url=None,
        *,encoding='utf-8'
):
    """
    生成readme模板
    :param project_name: 项目名称
    :param pypi_name: pypi名称
    :param print_file: 是否打印出文件
    :param file_name: 文件名
    :param gitee: 有无gitee仓库
    :param github: 有无gitee仓库
    :param gitee_name: gitee仓库名
    :param github_name: github仓库名
    :param gitee_url:
    :param github_url:
    :return:
    """
    if pypi_name is None:
        pypi_name = project_name
    if gitee_name is None:
        gitee_name = project_name
    if github_name is None:
        github_name = project_name

    if gitee:
        gitee_stars="[![gitee](https://gitee.com/snowlandltd/{gitee_name}/badge/star.svg)](https://gitee.com/snowlandltd/{gitee_name}/stargazers)\n".format(gitee_name=gitee_name)
    else:
        gitee_stars =''
    if github:
        github_stars = "[![github](https://img.shields.io/github/stars/astar-club/{github_name})](https://img.shields.io/github/stars/astar-club/{github_name})\n".format(github_name=github_name)
    else:
        github_stars = ''

    docs = """
# {project_name}

[![version](https://img.shields.io/pypi/v/{pypi_name}.svg)](https://pypi.python.org/pypi/{pypi_name})
{gitee_stars}{github_stars}[![download](https://img.shields.io/pypi/dm/{pypi_name}.svg)](https://pypi.org/project/{pypi_name})
[![wheel](https://img.shields.io/pypi/wheel/{pypi_name}.svg)](https://pypi.python.org/pypi/{pypi_name})
![status](https://img.shields.io/pypi/status/{pypi_name}.svg)





### 参考资料

[1] https://github.com/ASTARCHEN/astartool

[2] https://github.com/astar-club/astar-devopstool-python

    """.format(project_name=project_name,
               pypi_name=pypi_name,
               github_stars=github_stars,
               gitee_stars=gitee_stars)

    if print_file:
        auto_title(file_name, encoding=encoding)
        with open(file_name, "a+", encoding=encoding) as f:
            f.write(docs)
    return docs